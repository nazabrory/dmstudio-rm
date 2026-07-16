# Project Settings: General

To access this screen:

  * On the [Project Settings](<ProjectSettings.md>) screen, select the **General** tab.

Manage general project settings, including project update behaviour and scripting files.

To control how the project updates in the event of project folder changes:

  1. Display the **General Project Settings** screen.

  2. Choose which behaviour(s) occur during a project session, using **Automatic Project Updates** settings:

     * Detect new files in the project folder when the project is opened

       * If **checked** , the project is automatically updated to reference all files in the project folder, providing they have not been deliberated excluded (see below). 

If **Automatically update project** (see below) is also **unchecked** , the [Changes in Project Folder](<changesinprojectfolder.md>) screen displays on startup, allowing you to amend the update settings listed here.

       * If **unchecked** , new files in the project folder are not added to the project on startup and will need to be added manually if required.

Note: Files in sub folders of the project folder are _not_ added automatically to the project, regardless of the settings above.

     * Detect files added to or removed from the project folder while the project is open

       * If **checked** , any file changes in the project folder detected during a project session trigger the Changes in Project Folder screen to display. 

If **Automatically update project** (see below) is also **unchecked** , the [Changes in Project Folder](<changesinprojectfolder.md>) screen displays when changes are detected, allowing you to amend the update settings listed here.

       * If **unchecked** , project folder changes are not detected during a project session.

     * Automatically update project (no prompts)

Only available if either of the **Detect...** options are checked (see above).

       * If checked, the project file is updated automatically, without any user input or feedback. 

       * If unchecked, project folder changes automatically display the [Changes in Project Folder](<changesinprojectfolder.md>) to confirm changes and future detection behaviour.

     * Automatically Compress Files

       * If **checked** , tables are compressed when saving to conserve disk space. 

       * If **unchecked** , files are not compressed when saving. This is typically faster than compressing data first.

  3. Choose which file types are ignored when detecting changes to the project folder, by setting File Exclusions.

The list displays all currently excluded file types. You can use wildcard symbols '?' and '*' to add variable data. File exclusions are applied in the order shown in the resulting list. 

     * ![](../Images/Icons/ProjectSettings/NewExclusion.png) **New File Exclusion** create a new file exclusion, using optional wildcards.

     * ![](../Images/Icons/ProjectSettings/DeleteExclusion.png) **Delete File Exclusion** remove the highlighted exclusion from the list.

     * ![](../Images/Icons/ProjectSettings/MoveUp.png) ![](../Images/Icons/ProjectSettings/MoveDown.png) **Move Exclusion Up / Down** reposition the exclusion in the list to change its precedence.

  4. Click **OK** to update your project.

To force an automation script to run when the project next opens:

  1. Display the **General Project Settings** screen.

  2. To run a script automatically when the current project opens, specify an .htm or .html **Filename**. 

     * Use Currentadd the currently specified script filename to the Filename field. 

**Note** : the path can be absolute (fully qualified, for example "C:\Database\Scripts\Myscript.htm" or relative to the current project file, e.g. "\MyLocalScripts\MyScript.htm", where "MyLocalScripts" is a sub-folder of the current project directory.

     * Use Defaultadd the default script filename, click this button.

     * Use Blankdisplay a blank file, click this button.

     * Browsebrowse for a script file.

  3. Click **OK** to update your project.

Related topics and activities

  * [Project Settings](<ProjectSettings.md>)

  * [Project Wizard ](<ProjectWizard.md>)

  * [Automating Studio Products](<concept_studio%203%20scripting%20overview.md>)