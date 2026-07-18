import sys
import os
sys.path.insert(0, r"d:\Active\dmstudio-rm")

from dmstudio import dmcommands, initialize, sandbox

try:
    oScript = initialize.studio('StudioRM')
    project = oScript.ActiveProject
    print("Active project folder:", project.Folder if project else "None")

    dmc = dmcommands.init(version='StudioRM')
    # Initialize sandbox
    notebook_folder = r"d:\Active\dmstudio-rm\tutorials\collections\processes\extra"
    sandbox.initialize_sandbox(notebook_folder)

    # Copy files
    files_to_copy = ["_vb_assays.dmx"]
    sandbox.copy_database_files(files_to_copy)

    # Run extra
    print("Running extra...")
    dmc.extra(
        in_i='t_assays',
        out_o='t_extra_out',
        arguments="'AU=AU'"
    )
    print("Success!")
except Exception as e:
    import traceback
    print("Error:")
    traceback.print_exc()
