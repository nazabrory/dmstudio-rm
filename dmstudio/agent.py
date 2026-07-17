'''
dmstudio.agent
--------------

AI agent helper module for Datamine Studio RM scripting.

Provides:
- list_commands()         : Return all available Datamine command names and descriptions.
- get_command_schema()    : Return the JSON schema (parameters, types) for a given command.
- search_commands()       : Fuzzy-search commands by name or keyword.
- read_datamine()         : Read a .dm or .dmx binary file into a pandas DataFrame using
                            the DmFile.DmTableADO COM object — no proprietary deps required.
- dialog_dismiss_context(): Context manager that auto-dismisses blocking Studio RM modal
                            dialogs in a background thread (opt-in).
'''
import re
import threading
import time
import inspect
import contextlib

import pandas as pd
import win32com.client

from dmstudio import dmcommands, dmfiles


# ---------------------------------------------------------------------------
# Command discovery helpers
# ---------------------------------------------------------------------------

def _get_init_classes():
    '''Return the list of init classes to inspect (both dmcommands and dmfiles).'''
    classes = []
    # dmcommands
    if inspect.isclass(dmcommands.init):
        classes.append(dmcommands.init)
    else:
        classes.append(type(dmcommands.init))
    # dmfiles
    if inspect.isclass(dmfiles.init):
        classes.append(dmfiles.init)
    else:
        classes.append(type(dmfiles.init))
    return classes


def list_commands():
    '''
    list_commands
    -------------

    Return a list of all available Datamine command wrapper names exposed
    by dmstudio.dmcommands.init and dmstudio.dmfiles.init. Each entry is a dict with 'name' and 'doc' keys.

    Returns:
    --------
    list of dict
        [{'name': 'copy', 'doc': 'COPY ...'}, ...]
    '''
    results = []
    seen = set()
    classes = _get_init_classes()

    for cls in classes:
        # Walk the init class for all callable, non-dunder methods
        for name in dir(cls):
            if name.startswith('_') or name in ('run_command', 'parse_infields_list'):
                continue
            if name in seen:
                continue
            try:
                attr = getattr(cls, name)
            except Exception:
                continue
            if callable(attr):
                doc = inspect.getdoc(attr) or ''
                first_line = doc.split('\n')[0].strip()
                results.append({'name': name, 'doc': first_line})
                seen.add(name)

    return sorted(results, key=lambda x: x['name'])


def get_command_schema(cmd_name):
    '''
    get_command_schema
    ------------------

    Return a JSON-serialisable schema for a given Datamine command wrapper.

    Parameters:
    -----------
    cmd_name: str
        Name of the command (case-insensitive), e.g. 'copy', 'COPY', 'protom'.

    Returns:
    --------
    dict
        {
          'name': str,
          'doc': str,
          'parameters': [{'name': str, 'default': any, 'annotation': str}, ...]
        }

    Raises:
    -------
    ValueError
        If the command is not found.
    '''
    cmd_name_lower = cmd_name.lower()
    classes = _get_init_classes()
    func = None

    # Search init class methods first (where all wrappers live)
    for cls in classes:
        for name in dir(cls):
            if name.lower() == cmd_name_lower:
                try:
                    func = getattr(cls, name)
                    if callable(func):
                        break
                except Exception:
                    pass
        if func is not None:
            break

    # Fallback 1: search module-level names in dmcommands
    if func is None:
        for name in dir(dmcommands):
            if name.lower() == cmd_name_lower:
                try:
                    attr = getattr(dmcommands, name)
                    if callable(attr):
                        func = attr
                        break
                except Exception:
                    pass

    # Fallback 2: search module-level names in dmfiles
    if func is None:
        for name in dir(dmfiles):
            if name.lower() == cmd_name_lower:
                try:
                    attr = getattr(dmfiles, name)
                    if callable(attr):
                        func = attr
                        break
                except Exception:
                    pass

    if func is None:
        raise ValueError('Command not found: {}'.format(cmd_name))

    try:
        sig = inspect.signature(func)
    except (ValueError, TypeError):
        sig = None

    params = []
    if sig:
        for pname, param in sig.parameters.items():
            if pname in ('self', 'cls'):
                continue
            default = param.default
            if default is inspect.Parameter.empty:
                default = None
            annotation = str(param.annotation) if param.annotation is not inspect.Parameter.empty else 'any'
            params.append({'name': pname, 'default': str(default), 'annotation': annotation})

    doc = inspect.getdoc(func) or ''

    return {
        'name': cmd_name,
        'doc': doc,
        'parameters': params,
    }



def search_commands(query):
    '''
    search_commands
    ---------------

    Search command names and docstrings for a keyword or phrase.

    Parameters:
    -----------
    query: str
        Search term (case-insensitive).

    Returns:
    --------
    list of dict
        Matching commands: [{'name': str, 'doc': str}, ...]
    '''
    query_lower = query.lower()
    results = []
    for entry in list_commands():
        if query_lower in entry['name'].lower() or query_lower in entry['doc'].lower():
            results.append(entry)
    return results


# ---------------------------------------------------------------------------
# Native Datamine file reader 
# ---------------------------------------------------------------------------

def read_datamine(filepath):
    '''
    read_datamine
    -------------

    Read a Datamine binary file (.dm or .dmx) into a pandas DataFrame using
    the DmFile.DmTableADO COM object. 

    Parameters:
    -----------
    filepath: str
        Full or relative path to a .dm or .dmx file.

    Returns:
    --------
    pandas.DataFrame
        All records and fields from the Datamine file.

    Raises:
    -------
    RuntimeError
        If the DmFile.DmTableADO COM object is not available or the file
        cannot be opened.
    '''
    try:
        table = win32com.client.Dispatch('DmFile.DmTableADO')
    except Exception as e:
        raise RuntimeError(
            'Could not initialise DmFile.DmTableADO COM object. '
            'Ensure Datamine Studio RM is installed: {}'.format(e)
        )

    try:
        table.Open(filepath, 0)  # 0 = read-only
    except Exception as e:
        raise RuntimeError('Could not open Datamine file "{}": {}'.format(filepath, e))

    try:
        schema = table.Schema
        n_fields = schema.FieldCount

        # Determine field names (1-based index)
        field_names = []
        for i in range(1, n_fields + 1):
            try:
                field_names.append(schema.GetFieldName(i))
            except Exception:
                field_names.append('FIELD_{}'.format(i))

        rows = []
        try:
            table.MoveFirst()
        except Exception:
            pass

        while not table.EOF:
            row = {}
            for i, fname in enumerate(field_names, start=1):
                try:
                    row[fname] = table.GetColumn(i)
                except Exception:
                    row[fname] = None
            rows.append(row)
            try:
                table.MoveNext()
            except Exception:
                break

        return pd.DataFrame(rows) if rows else pd.DataFrame(columns=field_names)

    finally:
        try:
            table.Close()
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Auto-dialog dismissal context manager (opt-in)
# ---------------------------------------------------------------------------

@contextlib.contextmanager
def dialog_dismiss_context(title='Studio RM', interval=1.0):
    '''
    dialog_dismiss_context
    ----------------------

    Context manager that spawns a background thread to automatically dismiss
    blocking "#32770" modal dialogs produced by Datamine Studio RM (e.g.
    "Duplicate Project File" prompts). This is opt-in: it only runs when
    explicitly used as a context manager.

    Parameters:
    -----------
    title: str
        Window title to match for dismissal. Default: 'Studio RM'.
    interval: float
        Polling interval in seconds. Default: 1.0.

    Usage:
    ------
    from dmstudio import agent, dmcommands
    cmd = dmcommands.init(version='StudioRM')

    with agent.dialog_dismiss_context():
        cmd.copy(in_i='source', out_o='dest')
    '''
    try:
        import win32gui
        import win32con
        _win32_available = True
    except ImportError:
        _win32_available = False

    stop_event = threading.Event()

    def _dismiss_loop():
        if not _win32_available:
            return
        while not stop_event.is_set():
            try:
                def _enum_callback(hwnd, _):
                    if not win32gui.IsWindowVisible(hwnd):
                        return
                    cls = win32gui.GetClassName(hwnd)
                    ttl = win32gui.GetWindowText(hwnd)
                    if cls == '#32770' and title in ttl:
                        # Try 'Yes' button (ID=6), then 'OK' button (ID=1)
                        for btn_id in (6, 1):
                            try:
                                import win32api
                                win32api.SendMessage(hwnd, win32con.WM_COMMAND, btn_id, 0)
                            except Exception:
                                pass
                win32gui.EnumWindows(_enum_callback, None)
            except Exception:
                pass
            time.sleep(interval)

    t = threading.Thread(target=_dismiss_loop, daemon=True)
    t.start()
    try:
        yield
    finally:
        stop_event.set()
        t.join(timeout=interval * 2)


def download_tutorials(target_dir):
    '''
    download_tutorials
    ------------------

    Download the latest tutorials and sample datasets from the GitHub repository
    and extract them into the specified target directory.

    Parameters:
    -----------
    target_dir: str
        Absolute or relative path to the folder where the "tutorials" directory
        should be created.
    '''
    import os
    import urllib.request
    import zipfile
    import tempfile
    import shutil

    # 1. Validate target directory
    target_dir = os.path.abspath(target_dir)
    os.makedirs(target_dir, exist_ok=True)
    
    url = "https://github.com/nazabrory/dmstudio/archive/refs/heads/master.zip"
    fallback_url = "https://github.com/nazabrory/dmstudio/archive/refs/heads/main.zip"
    
    # 2. Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as tmp_file:
        tmp_path = tmp_file.name
        
    try:
        # Download the zip
        try:
            print("Downloading tutorials from {}...".format(url))
            urllib.request.urlretrieve(url, tmp_path)
        except Exception:
            print("Failed to download from default branch. Trying fallback: {}...".format(fallback_url))
            urllib.request.urlretrieve(fallback_url, tmp_path)
        
        # 3. Extract the tutorials folder
        print("Extracting tutorials...")
        with zipfile.ZipFile(tmp_path, 'r') as zip_ref:
            # Find the top level directory name inside the zip (typically 'dmstudio-main')
            top_dir = None
            for name in zip_ref.namelist():
                if name.endswith('/tutorials/'):
                    top_dir = name.split('/')[0]
                    break
            
            if not top_dir:
                # Try fallback: look for any 'tutorials/' entry
                for name in zip_ref.namelist():
                    if 'tutorials/' in name:
                        top_dir = name.split('/')[0]
                        break
            
            if not top_dir:
                raise RuntimeError("Could not find 'tutorials' folder in the downloaded zip archive.")
            
            # Extract only files in the tutorials folder
            tutorials_prefix = "{}/tutorials/".format(top_dir)
            extracted_count = 0
            for member in zip_ref.infolist():
                if member.filename.startswith(tutorials_prefix) and not member.is_dir():
                    # Compute relative path under 'tutorials/'
                    rel_path = member.filename[len(tutorials_prefix):]
                    out_path = os.path.join(target_dir, 'tutorials', rel_path)
                    
                    # Ensure parent dir exists
                    os.makedirs(os.path.dirname(out_path), exist_ok=True)
                    
                    # Write file
                    with zip_ref.open(member) as source, open(out_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
                    extracted_count += 1
                    
        print("Successfully extracted {} tutorial files to: {}".format(
            extracted_count, os.path.join(target_dir, 'tutorials')
        ))
        
    finally:
        # Clean up temporary file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

