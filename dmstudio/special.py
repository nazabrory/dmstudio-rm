'''
dmstudio.special
================

Python package with modified studio processes. The package is designed to make processes such as inpfil easier to use
and to facilitate more readable code.



'''

import os
import uuid

import pandas as pd

import dmstudio.dmfiles
import dmstudio.dmcommands
from dmstudio import validator

# -----------------------------------------------------------------------------------#
# Special fields
#------------------------------------------------------------------------------------#
# certain fields are required to be 8 characters
CHAR8_FIELDS = ['VALUE_IN', 'VALUE_OU', 'NUMSAM_F', 'SVOL_F', 'VAR_F', 'MINDIS_F']

#  fields that are always implicit
IMPLICIT_FIELDS = ['XMORIG', 'YMORIG', 'ZMORIG', 'NX', 'NY', 'NZ','X0','Y0','Z0','ANGLE1','ANGLE2','ANGLE3','ROTAXIS1','ROTAXIS2','ROTAXIS3']

#------------------------------------------------------------------------------------#


class dmfile_def(object):

    '''
    dmfile_def
    ----------

    Class for interactively creating a datamine file definition as a pandas dataframe. The file definition is to be
    used for an input for processes such as special.inpfil.

    Object Properties:
    ------------------

    dmfile_def.definition: pandas dataframe
        Dataframe to hold datamine file definition


    '''

    def __init__(self, definition=None):

        columns = ['Field Name', 'Field Type', 'Length', 'Keep', 'Default']

        if definition is None:
            self.definition = pd.DataFrame(columns=columns)
        else:
            for col in columns:
                if col not in definition.columns:
                    raise ValueError("Column " + col + " not found in definition. Columns 'Field Name', 'Field Type', 'Length'," \
                                             " 'Keep', 'Default' are required")
            self.definition = definition


    def add_field(self, field_name, field_type, length='', keep='Y', default=''):

        data = {'Field Name': field_name, 'Field Type': field_type, 'Length': length, 'Keep': keep,
                'Default': default}

        dmtemp = pd.DataFrame([data])
        field_order = ['Field Name', 'Field Type', 'Length', 'Keep', 'Default']
        dmtemp = dmtemp[field_order]
        self.definition = pd.concat([self.definition, dmtemp], ignore_index=True)

def inpfil(csv=None, out_o=None, definition=None, df=None, cmd=None, project_folder=None):
    '''
    inpfil
    ------
    Datamine INPFIL wrapper. Creates a Datamine binary file from a pandas DataFrame
    or CSV file according to a field definition schema.

    Parameters:
    -----------
    csv: Optional[str]
        Path to CSV file. Optional if df is provided.
    out_o: str
        Target Datamine output table name.
    definition: Optional[pd.DataFrame]
        Schema definition DataFrame. If None, derived from df or csv.
    df: Optional[pd.DataFrame]
        Direct pandas DataFrame to export. If provided, skips reading from csv.
    cmd: Optional[Any]
        Studio RM command engine or dmfiles instance.
    project_folder: Optional[str]
        Explicit project directory to stage temporary files.
    '''
    if df is not None:
        if definition is None:
            definition = pd_to_definition(df)
    elif csv is not None:
        df = pd.read_csv(csv)
        if definition is None:
            definition = csv_to_definition(csv)
    else:
        raise ValueError("Either 'df' or 'csv' must be provided to inpfil.")

    # Make a shallow copy of definition to avoid mutating caller's DataFrame
    definition = definition.copy()

    arguments = " 'csvfile' "

    for i in range(len(definition)):
        idx = definition.index[i]
        field_name = str(definition['Field Name'].iloc[i]).strip()

        if field_name in CHAR8_FIELDS:
            definition.loc[idx, 'Field Type'] = 'A'
            definition.loc[idx, 'Length'] = 8

        if field_name in IMPLICIT_FIELDS:
            definition.loc[idx, 'Field Type'] = 'N'
            definition.loc[idx, 'Keep'] = 'N'
            if field_name in df.columns and len(df) > 0:
                definition.loc[idx, 'Default'] = df[field_name].iloc[0]

        for column in definition.columns:
            if column == 'Length' and definition['Field Type'].iloc[i] == 'N':
                continue
            arguments += " '" + (str(definition[column].iloc[i])).strip()[:8] + "' "

    if cmd is not None:
        dmf = cmd if hasattr(cmd, 'inpfil') else getattr(cmd, 'dmfiles', None) or dmstudio.dmfiles.init()
    else:
        dmf = dmstudio.dmfiles.init()

    # Determine project folder for staging temporary INPFIL data file
    if project_folder is None:
        try:
            if hasattr(dmf, 'oScript') and dmf.oScript and getattr(dmf.oScript, 'ActiveProject', None):
                project_folder = getattr(dmf.oScript.ActiveProject, 'Folder', None) or getattr(dmf.oScript.ActiveProject, 'Directory', None)
        except Exception as e:
            pass
    if not project_folder:
        project_folder = os.getcwd()

    # Underscore-prefixed temporary file name to prevent unmanaged project pollution
    temp_csv_name = '_in_' + uuid.uuid4().hex[:8] + '.csv'
    temp_csv_path = os.path.join(project_folder, temp_csv_name)

    # Save data rows without headers/index, formatting floats cleanly
    formatted_rows = []
    for _, row in df.iterrows():
        row_vals = []
        for fname in df.columns:
            val = row[fname]
            if isinstance(val, float) and not (val != val) and val == int(val):
                row_vals.append(str(int(val)))
            elif val is None or (isinstance(val, float) and val != val):
                row_vals.append('-')
            else:
                row_vals.append(str(val))
        formatted_rows.append(','.join(row_vals))

    with open(temp_csv_path, 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(formatted_rows) + '\n')

    # '!' = end of DD
    # 'Y' = answer to INPFIL's "Use system file? Y/N" prompt
    # temp_csv_name = local CSV file containing the data rows
    arguments += " '!' 'Y' '" + temp_csv_name + "' "

    # Strip extension from out_o — Datamine logical names have no extension
    out_name = os.path.splitext(out_o)[0] if out_o and out_o != 'optional' else out_o

    try:
        dmf.inpfil(out_o=out_name, arguments=arguments)
    finally:
        if os.path.exists(temp_csv_path):
            try:
                os.remove(temp_csv_path)
            except Exception as e:
                pass

def csv_to_definition(csv):

    df = pd.read_csv(csv)

    return pd_to_definition(df);

def pd_to_definition(df):

    field_names = []
    an = []
    length = []

    for column in df.columns:

        field_names.append(column)

        if df[column].dtype=='float64' or df[column].dtype=='int64':
            an.append('N')
            length.append('')
        else:
            an.append('A')
            if column in CHAR8_FIELDS:
                length.append(8)
            else:
                length.append(int((df[column].str.len().max()-1)/4+1)*4)

    definition = pd.DataFrame({'Field Name': field_names, 'Field Type': an, 'Length': length})
    definition['Keep']='Y'
    definition['Default']=''

    return definition


# -----------------------------------------------------------------------------------#
# Studio RM 3.1 Automation Helpers
# -----------------------------------------------------------------------------------#

def print_plot_sheet_to_pdf(oScript, plot_sheet_name, output_path, options=""):
    """
    Print a plot sheet to PDF using the Studio RM 3.1+ DmProject.PrintPlotSheetToPDF() method.

    Parameters:
    -----------
    oScript: COM object
        Active Studio COM application object (e.g. from dmstudio.initialize.studio())
    plot_sheet_name: str
        Name of the plot sheet to print.
    output_path: str
        Full file path for the output PDF.
    options: str
        Optional print options string.

    Example:
    --------
    >>> from dmstudio import initialize
    >>> oScript = initialize.studio('StudioRM')
    >>> print_plot_sheet_to_pdf(oScript, "From 3D", "C:\\Path\\To\\Output.pdf")
    """
    oScript.ActiveProject.PrintPlotSheetToPDF(plot_sheet_name, output_path, options)


def text_importer(oScript, scenario_file):
    """
    Run the Text Importer using a saved scenario file (.dminsv).
    Available for automation in Studio RM 3.1+.

    Parameters:
    -----------
    oScript: COM object
        Active Studio COM application object.
    scenario_file: str
        Full path to the Text Importer scenario file (.dminsv).

    Example:
    --------
    >>> from dmstudio import initialize, special
    >>> oScript = initialize.studio('StudioRM')
    >>> special.text_importer(oScript, "C:\\Path\\To\\import.dminsv")
    """
    oScript.ActiveProject.RunTextImporter(scenario_file)


def create_isoshells(oScript, strict=False, **kwargs):
    """
    Create isoshells via ParseCommand with name-value parameter pairs.
    Available for automation in Studio RM 3.1+.

    Parameters:
    -----------
    oScript: COM object
        Active Studio COM application object.
    strict: bool, optional
        If True, raises ValueError on syntax errors or unsafe patterns. Default is False.
    **kwargs: dict
        Name-value parameter pairs for the Create Isoshells command.
        Common parameters include: model, field, value, out, etc.

    Example:
    --------
    >>> from dmstudio import initialize, special
    >>> oScript = initialize.studio('StudioRM')
    >>> special.create_isoshells(oScript, model="blockmod", field="AU", value="1.0", out="isoshell")
    """
    command = "create-isoshells"
    for key, value in kwargs.items():
        command += " @{}={}".format(key, value)
    validator.validate_command(command, strict=strict)
    oScript.Parsecommand(command)

