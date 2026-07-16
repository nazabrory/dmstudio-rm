'''
dmstudio.special
================

Python package with modified studio processes. The package is designed to make processes such as inpfil easier to use
and to facilitate more readable code.



'''

import dmstudio.dmfiles
import dmstudio.dmcommands
import pandas as pd

# -----------------------------------------------------------------------------------#
# Special fields
#------------------------------------------------------------------------------------#
# certain fields are required to be 8 characters
CHAR8_FIELDS = ['VALUE_IN', 'VALUE_OU', 'NUMSAM_F', 'SVOL_F', 'VAR_F', 'MINDIS_F']

#  fields that are always implicit
IMPLICIT_FIELDS = ['XMORIG', 'YMORIG', 'ZMORIG', 'NX', 'NY', 'NZ','X0','Y0','Z0','ANGLE1','ANGLE2','ANGLE3','ROTAXIS1','ROTAXIS2','ROTAXIS3']

#------------------------------------------------------------------------------------#

dmf = dmstudio.dmfiles.init()
dmc = dmstudio.dmcommands.init()

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

def inpfil(csv=None, out_o=None, definition=None):

    if definition is None:
        definition = csv_to_definition(csv)

    arguments = " 'csvfile' "
    df = pd.read_csv(csv)

    for i in range(len(definition)):

        if definition['Field Name'].iloc[i] in CHAR8_FIELDS:
            definition['Field Type'].iloc[i] = 'A'
            definition['Length'].iloc[i] = 8

        if definition['Field Name'].iloc[i].strip() in IMPLICIT_FIELDS:
            definition['Field Type'].iloc[i] = 'N'
            definition['Keep'].iloc[i] = 'N'
            definition['Default'].iloc[i] = df[definition['Field Name'].iloc[i]].iloc[0]

        for column in definition.columns:
            if column == 'Length' and definition['Field Type'].iloc[i] == 'N':
                continue
            arguments += " '" + (str(definition[column].iloc[i])).strip()[:8] + "' "

    # Create a temporary CSV file without headers to prevent Datamine from trying to parse the headers as data
    import os
    temp_csv = csv + ".temp_no_header"
    df.to_csv(temp_csv, header=False, index=False)

    arguments += "'!' 'Y' " + temp_csv

    try:
        dmf.inpfil(out_o=out_o, arguments=arguments)
    finally:
        if os.path.exists(temp_csv):
            os.remove(temp_csv)

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


def create_isoshells(oScript, **kwargs):
    """
    Create isoshells via ParseCommand with name-value parameter pairs.
    Available for automation in Studio RM 3.1+.

    Parameters:
    -----------
    oScript: COM object
        Active Studio COM application object.
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
    oScript.Parsecommand(command)

