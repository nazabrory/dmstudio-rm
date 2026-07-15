import win32com.client
import sys
import glob
import numpy as np

def _scriptinit(dm_object):
    '''
    _scriptinit
    -----------

    Initialize the Studio COM object. Internal function.

    Parameters:
    -----------

    studio_object: str
        Datamine studio COM object to initialize

    Returns:
    --------

    ActiveX connection
    '''

    return win32com.client.Dispatch(dm_object);

def studio(version):
    '''
    studio
    ------

    Datamine Studio Initialization.

    Supports: 'Studio3', 'StudioRM', 'StudioRM3.1', 'StudioRM3.2', 'StudioRM3.3',
    and any future 'StudioRM3.x' string, plus 'StudioEM'.

    Parameters:
    -----------

    version: str
        Datamine studio version. Supported values:
          - 'Studio3'       : Datamine Studio version 3
          - 'StudioRM'      : Datamine Studio RM (latest registered)
          - 'StudioRM3.x'   : Datamine Studio RM 3.1, 3.2, 3.3 and any future 3.x release
          - 'StudioEM'      : Datamine Studio EM
          - None            : Auto-detect (tries StudioRM, then Studio3, then StudioEM)

    Notes:
    ------
    Studio RM 3.1+ introduces safer scripting practices. Python win32com.client.Dispatch()
    is unaffected by Studio RM 3.1+ "safer scripting" restrictions and remains the standard
    COM initialization method for all Python automation.

    All StudioRM3.x variants (3.1, 3.2, 3.3, ...) share the same COM ProgID:
    Datamine.StudioRM.Application. The version string is used for documentation and
    logging only, not for COM dispatch selection.
    '''

    oScript = None

    _make_dmdir()

    if version == 'StudioRM' or (isinstance(version, str) and version.startswith('StudioRM3.')):
        oScript = _scriptinit("Datamine.StudioRM.Application")
    elif version == 'Studio3':
        oScript = _scriptinit("Datamine.Studio.Application")
    elif version == 'StudioEM':
        oScript = _scriptinit("Datamine.StudioEM.Application")
    else:
        # no version given, will try to find a valid version
        try:
            oScript = _scriptinit("Datamine.StudioRM.Application")
        except Exception:
            try:
                oScript = _scriptinit("Datamine.Studio.Application")
            except Exception:
                try:
                    oScript = _scriptinit("Datamine.StudioEM.Application")
                except Exception:
                    raise RuntimeError("No valid Studio version is active")

    return oScript

def dmFile():

    print("here")
    # assert oDmFile = _scriptinit("DmFile.DmTableADO"), "Could not initialize dmTableADO"


def _make_dmdir():
    
    '''
    _make_dmdir
    -----------
    
    Internal function which creates a local ``_init_.py`` and python file ``dmdir.py`` which contains a list of dm files in the local 
    Datamine project directory passed to variables with name of file without dm file extension and leading and trailing underscores. 
    
    The purpose of the local python file is to facilitate importing the filenames as variables which can be referenced directly in the
    scripts. 
    
    Usage:
    ------
    
    >>>import dmdir as f
    >>>print f._someDmFile_
    someDmFile
    
    The imported variables can be used as inputs in scripts:
    
    >>>from dmstudio import dmcommands
    >>> dmc = dmcommands.init()
    >>> dmc.copy(in_i=f._someDmFile_, out_o='someDmFile2')
    
    '''

    dmdir_init = open('__init__.py', 'w')
    dmdir_init.write("'''\n")
    dmdir_init.write("Initialization file to enable importing of dmdir.py\n")
    dmdir_init.write("'''\n")
    dmdir_init.close()

    dmdir_f = open('dmdir.py', 'w')
    dmdir_f.write("'''\n")
    dmdir_f.write("List of datamine files in active datamine project directory\n")
    dmdir_f.write("\n")
    dmdir_f.write("This file will populate after initializing the script for the first time and will update after each command.\n")
    dmdir_f.write("\n")
    dmdir_f.write("Usage:\n")
    dmdir_f.write("------\n")
    dmdir_f.write("\n")
    dmdir_f.write(">>import dmdir as f\n")
    dmdir_f.write(">>print f._someDmFile_\n")
    dmdir_f.write("someDmFile\n")
    dmdir_f.write("\n")
    dmdir_f.write("'''\n")
    dmdir_f.write("\n")

    filenames = set()
    for ext in ("*.dm", "*.dmx"):
        for infile in glob.glob(ext):
            outname = infile.rsplit('.', 1)[0]
            filenames.add(outname)

    for outname in sorted(filenames):
        dmdir_f.write('_'+ outname + "_='" + outname + "'\n")

    dmdir_f.close()



