# Changes in Project Folder

To access this screen:

  * Display the Project Settings console and check Detect files added to or removed from the project folder while the project is open Then, add, remove or edit files in the project folder.

Datamine projects are associated with a folder on your local system or network. Every project file has a folder, and the link between project file and folder is dynamic. If set up to do so, changes to the contents of the folder are automatically picked up by your system. See [Project File](<Concept_The_Studio_3_Project_File.md>).

If a file change is detected, the **Changes in Project Folder** screen asks if you want to update the project (either add, remove or update the project file reference).

  * Choose **Yes** to update the project or **Yes to all** to update the project for the current and all other changes detected.

  * Click **No** to leave the project as it is. For example, if a new file is added to the project and you select No, a new project reference will not be added, although it can be added manually by other means. You can also choose No to all to ignore all detected changes.

You can also choose what happens to other changes detected in the project.

  * Automatically add files already in project directory: ensure that any files already in the directory selected to be the project directory are included in the project.

  * Automatically add files in project directory each time project is opened: ensure that any files added to the project directory outside of your application (for example, using Windows), since the project was last run, are added to the project. This selection will also ensure the Changes in Project Folder dialog is shown when changes are made to the project directory.

  * Automatically update project (no prompts): the project file is updated according to the settings above without user prompts. If disabled, prompts are displayed when project changes are actioned.

**Note** : You can define default settings for your project using similar options found in the **Project Settings** console. See [Project Settings: General](<Project%20Settings_General.md>). Remember to save your project afterwards.

  * [Project Settings](<ProjectSettings.md>)

  * [Project Settings: General](<Project%20Settings_General.md>)

  * [About Studio Projects](<Concept_The_Studio_3_Project_File.md>)

  * [Creating Projects](<ProjectWizard.md>)

  * [Saving Projects](<SaveChanges.md>)