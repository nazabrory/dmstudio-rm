# Data Options

To access this screen:

  * **Home** ribbon **> > Settings >> System >> Data**.

  * Use the command line entry 'show-system-options'. Select the Data tab.

Define general data handling settings for Studio operations.

Drawing Units |  Select either _Metric_ or _Imperial_ units for drawing information to the screen.  Once specified, these units are used in the 3D and Plots windows.  
---|---  
Data Units |  Select either _Metric_ or _Imperial_ units used when describing 3D object dimensions. Once specified, these units are used in the 3D and Plots windows.  
Model Intersection Plane |  Where the intersection of a block model and a plane is being displayed, an ambiguity can occur when the plane falls exactly on a cell boundary.  This is caused by the fact that the two adjacent cells will intersect the plane at the same point, so it is not clear which should be used to dictate drawing attributes. It's commonly called "Z-fighting". To resolve this ambiguity, your application detects the case where a plane falls on a major cell boundary, and then offsets the plane by a small amount so that it falls into either one cell, or the other.  
Drag and Drop | By default, you can drag and **Drop Multiple Data Types** in the same loading operation. Uncheck this to only load a single data type.  
Default Datamine File Format |  By default, your system can read both DM and DMX formats, but will write .dmx format files.  You can change this to .dm (legacy). Warning: Changing this setting updates the default format for ALL Studio applications on the host system, and may trigger a bulk file format upgrade or downgrade next time Studio applications are restarted and a project opened.  
Automatic Project Files Conversion |  If **Include Subfolders** is checked, automatic file conversion on startup (see the warning above) will include all files in all subfolders of the project folder.  If unchecked, only files in the project folder are converted.  
  
Related topics and activities

  * [System Options](<Options.md>)

  * [Options: Environment](<Options_Environment.md>)

  * [Plots Options](<Options_Plots.md>)

  * [Options: Project](<Options_Project.htm.md>)

  * [Options: 3D ](<Options_InTouch.md>)

    * [Options: 3D General](<Options_InTouch-General.md>)

    * [Options: 3D Initial States](<Options_InTouch-Initial-States.md>)

    * [Options: 3D Printing](<Options_InTouch-Printing.md>)

  * [Options: Commands](<Options_Commands.md>)