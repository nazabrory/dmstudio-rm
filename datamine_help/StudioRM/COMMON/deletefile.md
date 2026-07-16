# Delete File(s) from Project

To access this screen:

  * Using the **[command line](<Command_Toolbar.md>)** , enter "delete-file".

  * Use the quick key combination "dfi".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **delete-file** and click **Run**.

Permanently delete a file from your project according to a wildcard expression, and remove the physical file from disk.

Note: You cannot undo this command. It is recommended that you backup data before deletion as it can't be retrieved once deleted.

## Using Filename Filters

To define a filename filter, type in a part of the filename together with one or more of the wildcard symbols '*' or '?' as prefix, intermediate character(s) or suffix. The filter will then be used to automatically select matching files from the project files list and display them in the pane below. Simply typing the '*' wildcard without any additional qualifying characters will result in all project files being listed. Some example filters are shown below:

  * _vb* \- selects all files that start with '_vb'

  * _vb???? \- select all files starting with '_vb' and which contain an additional 4 following characters

  * *vb* \- selects all files which contain the letters 'vb' at any position within the file name.

## Using <Ctrl> and <Del> to Delete Files

You can also use the shortcut keys <Ctrl> and <Del> to delete project files from your system. To do this, ensure that a file is highlighted in the Project Files control bar, and select both keys on your keyboard.

You will be presented with a confirmation dialog before this action is performed.

## Delete Files

To delete a file or files from the project based on a wildcard expression:

  1. Run the **delete-file** command.

  2. Enter a wildcard filter into the editable field.

  3. Review the **File(s) found** list. This lists all the project files that pass the filter.

  4. Click **OK** to (permanently) delete all files listed.