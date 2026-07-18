'''
dmstudio.dm_io
--------------

High-level pandas DataFrame ↔ Datamine binary file (.dm/.dmx) I/O module.

Provides:
- read_datamine()     : Read a .dm or .dmx binary file into a pandas DataFrame.
- to_datamine()       : Save a pandas DataFrame to a Datamine .dm or .dmx binary file.
- patch_dataframe()   : Monkey-patch pandas.DataFrame to support the .to_datamine() method.
'''
import os
import tempfile

import pandas as pd
import win32com.client

from dmstudio import special


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
