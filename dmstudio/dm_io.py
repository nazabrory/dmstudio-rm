'''
dmstudio.dm_io
--------------

High-level pandas DataFrame ↔ Datamine binary file (.dm/.dmx) I/O module.

Provides:
- read_datamine()            : Read a .dm or .dmx binary file into a pandas DataFrame.
- read_datamine_header()     : Lightweight header and metadata inspection without loading records.
- read_datamine_summary()    : High-level summary metrics for logging and validation.
- to_datamine()              : Save a pandas DataFrame to a Datamine .dm or .dmx binary file.
- patch_dataframe()          : Monkey-patch pandas.DataFrame to support the .to_datamine() method.
'''
import os
import tempfile
from typing import Any, List, Optional, Union

import pandas as pd
import win32com.client

from dmstudio import special


# Recognized global/implicit block model attribute names
_BLOCK_MODEL_ATTRIBUTES = [
    'XMORIG', 'YMORIG', 'ZMORIG',
    'XINC', 'YINC', 'ZINC',
    'NX', 'NY', 'NZ',
    'XSUBDIV', 'YSUBDIV', 'ZSUBDIV',
    'ROTX', 'ROTY', 'ROTZ',
    'DX', 'DY', 'DZ',
]
_BLOCK_MODEL_ATTRIBUTES_SET = set(_BLOCK_MODEL_ATTRIBUTES)


def resolve_table_path(
    table_name: Union[str, os.PathLike],
    project_folder: Optional[Union[str, os.PathLike]] = None,
    cmd: Optional[Any] = None,
) -> str:
    '''
    resolve_table_path
    ------------------

    Centralized table path resolution seam that resolves bare logical Datamine table names
    (e.g. 'collars', 'zone_bm'), relative paths, and extensionless identifiers to verified
    .dm or .dmx files in either the active Studio RM project directory or local filesystem.

    Resolution follows a strict three-tier precedence:
      1. Exact file match (absolute or relative to current working directory).
      2. Extension probing (.dm, .dmx) in current working directory / relative base.
      3. Active project folder probing (via explicit project_folder, cmd.oScript.ActiveProject,
         or active Studio RM COM session).

    Parameters:
    -----------
    table_name: str or os.PathLike
        Logical table name, filename, or file path.
    project_folder: Optional[str or os.PathLike]
        Explicit project directory path (useful for testing or non-standard project roots).
    cmd: Optional[Any]
        Studio RM command engine instance with active COM session.

    Returns:
    --------
    str:
        Verified absolute path to the .dm or .dmx file on disk.

    Raises:
    -------
    ValueError:
        If table_name is not a string/PathLike or is empty/whitespace.
    RuntimeError:
        If the table cannot be resolved across any evaluated location.
    '''
    if table_name is None or not isinstance(table_name, (str, os.PathLike)):
        raise ValueError(
            f"table_name must be a non-empty string or path, got {type(table_name).__name__ if table_name is not None else 'None'}."
        )
    clean_name = str(table_name).strip()
    if not clean_name:
        raise ValueError("table_name cannot be empty or whitespace.")

    evaluated_paths: List[str] = []

    def _check(path_str: str) -> Optional[str]:
        norm = os.path.normpath(path_str)
        if norm not in evaluated_paths:
            evaluated_paths.append(norm)
        if os.path.isfile(norm):
            return os.path.abspath(norm)
        return None

    # Tier 1: Exact match (as given, relative to CWD or absolute)
    res = _check(clean_name)
    if res:
        return res

    # Tier 2: Extension probing (.dm, .dmx) in CWD / relative directory
    for ext in ('.dm', '.dmx'):
        if not clean_name.lower().endswith(ext):
            res = _check(clean_name + ext)
            if res:
                return res

    # Tier 3: Active project folder probing
    proj_dir: Optional[str] = None
    if project_folder is not None:
        proj_dir = str(project_folder).strip()
    elif cmd is not None and getattr(cmd, 'oScript', None):
        studio_app = cmd.oScript
        if getattr(studio_app, 'ActiveProject', None):
            proj_dir = getattr(studio_app.ActiveProject, 'Folder', None) or getattr(
                studio_app.ActiveProject, 'Directory', None
            )
    else:
        try:
            from dmstudio import dmfiles
            dmf = dmfiles.init()
            if dmf.oScript and getattr(dmf.oScript, 'ActiveProject', None):
                proj_dir = getattr(dmf.oScript.ActiveProject, 'Folder', None) or getattr(
                    dmf.oScript.ActiveProject, 'Directory', None
                )
        except Exception as e:
            pass

    if proj_dir:
        candidates = [
            os.path.join(proj_dir, clean_name),
            os.path.join(proj_dir, os.path.basename(clean_name)),
        ]
        base = os.path.basename(clean_name)
        for ext in ('.dm', '.dmx'):
            if not clean_name.lower().endswith(ext):
                candidates.append(os.path.join(proj_dir, clean_name + ext))
            if not base.lower().endswith(ext):
                candidates.append(os.path.join(proj_dir, base + ext))

        for cand in candidates:
            res = _check(cand)
            if res:
                return res

    eval_list = '\n'.join(f'  - {p}' for p in evaluated_paths)
    raise RuntimeError(
        f"Could not resolve Datamine table '{clean_name}' (file does not exist). Evaluated candidate locations:\n{eval_list}"
    )



def read_datamine_header(
    filepath: Union[str, os.PathLike],
    project_folder: Optional[Union[str, os.PathLike]] = None,
    cmd: Optional[Any] = None,
) -> dict:
    '''
    read_datamine_header
    --------------------

    Lightweight metadata and schema inspection for Datamine binary files (.dm or .dmx).
    Queries total record count, column schemas (names, types, character lengths, defaults),
    and global/model header attributes (e.g. XMORIG, YMORIG, ZMORIG, cell increments)
    directly via DmFile.DmTableADO in milliseconds, without loading table records into memory.

    Accepts bare logical table names (e.g. 'collars') and resolves paths against the active
    Studio RM project directory or local filesystem via resolve_table_path.

    Parameters:
    -----------
    filepath: str or os.PathLike
        Logical table name, relative path, or full path to a .dm or .dmx file.
    project_folder: Optional[str or os.PathLike]
        Optional explicit project folder to search for tables.
    cmd: Optional[Any]
        Optional Studio RM command engine instance with active COM session.

    Returns:
    --------
    dict
        Metadata dictionary with keys:
          - 'filepath': str (absolute path)
          - 'record_count': int
          - 'field_count': int
          - 'fields': list of dicts (name, type, type_name, size, size_chars, default, implicit)
          - 'field_names': list of str
          - 'attributes': dict of global/model attributes from the first record
          - 'description': str
          - 'double_precision': bool
          - 'type_hint': int or None

    Raises:
    -------
    RuntimeError
        If the file does not exist, cannot be opened, or COM object is unavailable.
    '''
    abs_path = resolve_table_path(filepath, project_folder=project_folder, cmd=cmd)

    try:
        table = win32com.client.Dispatch('DmFile.DmTableADO')
    except Exception as e:
        raise RuntimeError(
            'Could not initialise DmFile.DmTableADO COM object. '
            'Ensure Datamine Studio RM is installed: {}'.format(e)
        )

    try:
        table.Open(abs_path, 0)  # 0 = read-only
    except Exception as e:
        raise RuntimeError('Could not open Datamine file "{}": {}'.format(filepath, e))

    try:
        try:
            raw_count = table.GetRowCount()
            record_count = int(raw_count) if raw_count is not None else 0
        except Exception as e:
            record_count = 0

        schema = table.Schema
        n_fields = int(schema.FieldCount) if schema and schema.FieldCount else 0

        fields = []
        field_names = []
        for i in range(1, n_fields + 1):
            try:
                name = schema.GetFieldName(i)
            except Exception as e:
                name = 'FIELD_{}'.format(i)
            field_names.append(name)

            try:
                field_type = schema.GetFieldType(i)
            except Exception:
                field_type = 1
            type_name = 'alphanumeric' if field_type == 3 else 'numeric'

            try:
                field_size = schema.GetFieldSize(i)
            except Exception:
                field_size = 4

            try:
                size_chars = schema.GetFieldSizeChars(i)
            except Exception:
                size_chars = field_size

            try:
                field_default = schema.GetFieldDefault(i)
            except Exception:
                field_default = None

            try:
                is_implicit = bool(schema.IsFieldImplicit(i))
            except Exception:
                is_implicit = False

            fields.append({
                'name': name,
                'type': field_type,
                'type_name': type_name,
                'size': field_size,
                'size_chars': size_chars,
                'default': field_default,
                'implicit': is_implicit,
            })

        attributes = {}
        # 1. Attempt to capture model attributes from first record
        try:
            table.MoveFirst()
            if not getattr(table, 'EOF', False):
                implicit_field_names = [f['name'] for f in fields if f.get('implicit')]
                check_keys = _BLOCK_MODEL_ATTRIBUTES_SET.union(k.upper() for k in implicit_field_names)
                name_map = {f['name'].upper(): f['name'] for f in fields}

                for key in check_keys:
                    if key in name_map:
                        actual_name = name_map[key]
                        try:
                            val = table.GetNamedColumn(actual_name)
                            if val is not None:
                                attributes[actual_name] = val
                        except Exception:
                            pass
        except Exception:
            pass

        # 2. Fallback to schema field defaults (crucial for 0-record prototype models)
        for f in fields:
            fname = f['name']
            fname_upper = fname.upper()
            if (fname_upper in _BLOCK_MODEL_ATTRIBUTES_SET or f.get('implicit')) and fname not in attributes:
                default_val = f.get('default')
                if default_val is not None:
                    attributes[fname] = default_val

        description = getattr(schema, 'Description', '')
        double_precision = bool(getattr(schema, 'DoublePrecision', False))
        type_hint = getattr(schema, 'TypeHint', None)

        return {
            'filepath': abs_path,
            'record_count': record_count,
            'field_count': n_fields,
            'fields': fields,
            'field_names': field_names,
            'attributes': attributes,
            'description': description,
            'double_precision': double_precision,
            'type_hint': type_hint,
        }

    finally:
        try:
            table.Close()
        except Exception as e:
            pass


def read_datamine_summary(
    filepath: Union[str, os.PathLike],
    project_folder: Optional[Union[str, os.PathLike]] = None,
    cmd: Optional[Any] = None,
) -> dict:
    '''
    read_datamine_summary
    ---------------------

    High-level summary of a Datamine binary file (.dm/.dmx) schema and model metrics.
    Suitable for logging in automated pipeline runs, diagnostics, and data validation.
    Accepts bare logical table names and resolves paths via resolve_table_path.

    Parameters:
    -----------
    filepath: str or os.PathLike
        Logical table name, relative path, or full path to a .dm or .dmx file.
    project_folder: Optional[str or os.PathLike]
        Optional explicit project folder to search for tables.
    cmd: Optional[Any]
        Optional Studio RM command engine instance with active COM session.

    Returns:
    --------
    dict
        Summary metrics dictionary:
          - 'filepath': str (absolute path)
          - 'filename': str (basename)
          - 'record_count': int
          - 'field_count': int
          - 'field_names': list of str
          - 'numeric_fields': list of str
          - 'alphanumeric_fields': list of str
          - 'is_block_model': bool
          - 'model_attributes': dict (e.g. XMORIG, YMORIG, ZMORIG, cell increments)
          - 'description': str
          - 'double_precision': bool
    '''
    header = read_datamine_header(filepath, project_folder=project_folder, cmd=cmd)

    numeric_fields = [f['name'] for f in header['fields'] if f.get('type_name') == 'numeric']
    alphanumeric_fields = [f['name'] for f in header['fields'] if f.get('type_name') == 'alphanumeric']

    # Case-insensitive model attribute resolution
    upper_attrs = {k.upper(): v for k, v in header['attributes'].items()}
    upper_field_names = {f.upper() for f in header['field_names']}
    model_attrs = {k: upper_attrs[k] for k in _BLOCK_MODEL_ATTRIBUTES if k in upper_attrs}
    is_block_model = all(
        (k in upper_attrs or k in upper_field_names)
        for k in ('XMORIG', 'YMORIG', 'ZMORIG')
    )

    return {
        'filepath': header['filepath'],
        'filename': os.path.basename(header['filepath']),
        'record_count': header['record_count'],
        'field_count': header['field_count'],
        'field_names': header['field_names'],
        'numeric_fields': numeric_fields,
        'alphanumeric_fields': alphanumeric_fields,
        'is_block_model': is_block_model,
        'model_attributes': model_attrs,
        'description': header['description'],
        'double_precision': header['double_precision'],
    }


# Convenience aliases
read_dm_header = read_datamine_header
read_dm_summary = read_datamine_summary



def read_datamine(
    filepath: Union[str, os.PathLike],
    project_folder: Optional[Union[str, os.PathLike]] = None,
    cmd: Optional[Any] = None,
) -> pd.DataFrame:
    '''
    read_datamine
    -------------

    Read a Datamine binary file (.dm or .dmx) into a pandas DataFrame using
    the DmFile.DmTableADO COM object. Accepts bare logical table names and resolves
    paths via resolve_table_path.

    Parameters:
    -----------
    filepath: str or os.PathLike
        Logical table name, relative path, or full path to a .dm or .dmx file.
    project_folder: Optional[str or os.PathLike]
        Optional explicit project folder to search for tables.
    cmd: Optional[Any]
        Optional Studio RM command engine instance with active COM session.

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
    abs_path = resolve_table_path(filepath, project_folder=project_folder, cmd=cmd)

    try:
        table = win32com.client.Dispatch('DmFile.DmTableADO')
    except Exception as e:
        raise RuntimeError(
            'Could not initialise DmFile.DmTableADO COM object. '
            'Ensure Datamine Studio RM is installed: {}'.format(e)
        )

    try:
        table.Open(abs_path, 0)  # 0 = read-only
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


def to_datamine(df, filepath):
    '''
    to_datamine
    -----------

    Save a pandas DataFrame to a Datamine .dm or .dmx binary file using the special.inpfil utility.

    Parameters:
    -----------
    df: pandas.DataFrame
        DataFrame to export.
    filepath: str
        Target file path.
    '''
    import shutil
    import uuid

    # Generate a safe, simple alphanumeric temporary name for Datamine
    temp_name = 'df_out_' + uuid.uuid4().hex[:8]

    fd, temp_csv = tempfile.mkstemp(suffix='.csv')
    os.close(fd)
    try:
        df.to_csv(temp_csv, index=False)
        defn = special.pd_to_definition(df)
        
        # Use the simple temp name for the Datamine command to avoid path / backslash issues
        special.inpfil(csv=temp_csv, out_o=temp_name, definition=defn)

        # Locate the created file in either the active project folder or current working directory
        project_folder = None
        try:
            from dmstudio import dmfiles
            dmf = dmfiles.init()
            if dmf.oScript and dmf.oScript.ActiveProject:
                project_folder = getattr(dmf.oScript.ActiveProject, 'Folder', None) or getattr(dmf.oScript.ActiveProject, 'Directory', None)
        except Exception:
            pass

        if not project_folder:
            project_folder = os.getcwd()

        created_file = None
        for ext in ('.dm', '.dmx'):
            p = os.path.join(project_folder, temp_name + ext)
            if os.path.exists(p):
                created_file = p
                break

        if not created_file:
            # Fallback to current working directory if project folder search did not find it
            for ext in ('.dm', '.dmx'):
                p = os.path.join(os.getcwd(), temp_name + ext)
                if os.path.exists(p):
                    created_file = p
                    break

        if created_file:
            # Ensure target directory exists
            target_dir = os.path.dirname(os.path.abspath(filepath))
            if target_dir and not os.path.exists(target_dir):
                os.makedirs(target_dir, exist_ok=True)
            # Move and rename to the final requested path
            shutil.move(created_file, filepath)
            print('Saved DataFrame to Datamine file: {}'.format(filepath))
        else:
            raise RuntimeError('Datamine failed to generate output file.')
    finally:
        if os.path.exists(temp_csv):
            os.remove(temp_csv)


def patch_dataframe():
    '''
    patch_dataframe
    ---------------

    Monkey-patch pandas.DataFrame to expose the .to_datamine() method.
    '''
    pd.DataFrame.to_datamine = to_datamine
