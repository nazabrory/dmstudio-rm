'''
dmstudio.command_registry
--------------------------

Command discovery module for Datamine Studio RM.

Provides a read-only index over all command wrappers exposed by
dmstudio.dmcommands.init, dmstudio.dmfiles.init, and their generated fallback equivalents.

Interface (seam):
    list_commands()             -> list[dict]
    get_command_schema(str)     -> dict
    search_commands(str)        -> list[dict]

No COM, threading, or pandas dependency — safe to import in any context,
including environments without Datamine Studio RM installed.
'''
import inspect

from dmstudio import dmcommands, dmfiles

try:
    from dmstudio import dmcommands_generated
except ImportError:
    dmcommands_generated = None

try:
    from dmstudio import dmfiles_generated
except ImportError:
    dmfiles_generated = None


# Canonical list of verified commands
VERIFIED_COMMANDS = {
    'accmlt', 'append', 'cokrig', 'compdh', 'copy',
    'count', 'delete', 'diffrn', 'dmedit', 'extra',
    'holes3d', 'ijkgen', 'join', 'mgsort', 'modtra',
    'output', 'selcop', 'seldel', 'selexy', 'sortx',
    'stats', 'tongrad', 'inpfil', 'estima', 'protom'
}


# ---------------------------------------------------------------------------
# Internal helpers (implementation — not part of the interface)
# ---------------------------------------------------------------------------

def _get_init_classes():
    '''Return the list of init classes to inspect (both dmcommands/dmfiles and generated/experimental).'''
    classes = []
    if inspect.isclass(dmcommands.init):
        classes.append(dmcommands.init)
    else:
        classes.append(type(dmcommands.init))
    if inspect.isclass(dmfiles.init):
        classes.append(dmfiles.init)
    else:
        classes.append(type(dmfiles.init))

    if dmcommands_generated is not None:
        if inspect.isclass(dmcommands_generated.init):
            classes.append(dmcommands_generated.init)
        else:
            classes.append(type(dmcommands_generated.init))

    if dmfiles_generated is not None:
        if inspect.isclass(dmfiles_generated.init):
            classes.append(dmfiles_generated.init)
        else:
            classes.append(type(dmfiles_generated.init))

    return classes


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def list_commands():
    '''
    list_commands
    -------------

    Return a list of all available Datamine command wrapper names exposed
    by verified and experimental modules. Each entry is a dict
    with 'name', 'doc', and 'experimental' keys.

    Returns:
    --------
    list of dict
        [{'name': 'copy', 'doc': 'COPY ...', 'experimental': False}, ...]
    '''
    results = []
    seen = set()
    classes = _get_init_classes()

    for cls in classes:
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
                experimental = name.lower() not in VERIFIED_COMMANDS
                results.append({
                    'name': name,
                    'doc': first_line,
                    'experimental': experimental
                })
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
          'parameters': [{'name': str, 'default': any, 'annotation': str}, ...],
          'experimental': bool
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

    # Fallback 3: search module-level names in dmcommands_generated
    if func is None and dmcommands_generated is not None:
        for name in dir(dmcommands_generated):
            if name.lower() == cmd_name_lower:
                try:
                    attr = getattr(dmcommands_generated, name)
                    if callable(attr):
                        func = attr
                        break
                except Exception as e:
                    pass

    # Fallback 4: search module-level names in dmfiles_generated
    if func is None and dmfiles_generated is not None:
        for name in dir(dmfiles_generated):
            if name.lower() == cmd_name_lower:
                try:
                    attr = getattr(dmfiles_generated, name)
                    if callable(attr):
                        func = attr
                        break
                except Exception as e:
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
        'experimental': cmd_name_lower not in VERIFIED_COMMANDS,
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
        Matching commands: [{'name': str, 'doc': str, 'experimental': bool}, ...]
    '''
    query_lower = query.lower()
    results = []
    for entry in list_commands():
        if query_lower in entry['name'].lower() or query_lower in entry['doc'].lower():
            results.append(entry)
    return results

