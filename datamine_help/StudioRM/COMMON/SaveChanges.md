# Save Data/Set Auto Reload

When a project is closed or saved, you are asked to confirm what happens to your data. This is important to ensure your data is safeguarded from accidental loss. You are also given the chance to automatically reload data on exit. 

If new data has been added to the project, you are also asked how to store it (either as a separate file or within the current project file).

The general process of saving a project involves the following:

  1. Close or swap projects after making changes to the current one.

  2. Click **Yes** to save the project and display the **Save Project and File Data** screen.

     * Or, click **No** to close the project without saving.

     * Click **Cancel** to abort the project closedown.

  3. A Save Project File screen displays. Use this to save the modifications made to the current project file.

  4. If you choose to save data, the Save Data / Set Auto Reload screen displays. Select files to save (for each file, if changes have been made, saving is automatically selected).

This screen is also used to specify which data, if any, is reloaded automatically when the project is reopened.

## Automatic Reloading

All data objects can be saved. You can also elect whether an object is loaded automatically the next time the project is opened, using the Save Data / Set Auto Reload screen.

The Save Changes screen allows you to configure, on a file-by-file basis, both of the above before saving the project file. The resulting, saved project file will be appended with the information supplied so that when it is reloaded, only those objects previously specified will be reloaded, and if standalone Datamine files are associated with the project.

**Tip** : use the top-level check boxes to select or deselect all items in the column beneath.

## Saving Data

When saving changes to a project, decide how new object data is stored:

  * will new objects in memory be saved as Datamine files?

  * will new object data be stored within the current project file?

There are advantages and disadvantages to both methods; if you store a file as a **separate file** , you can use this data in other projects. An _association_ is made between your current project file and the data file, but this file must remain in the same location if it is to be reloaded automatically. This option is ideal when you have data that is relevant to more than one project. Any edits to the external Datamine file are then reflected in both projects when this data is loaded.

Otherwise, save the data within the current **project file** \- means that the data is archived along with all project settings, keeping the project self-contained and easily portable and distributable. You will not be able to edit the file contents without first loading the project into your application, therefore, archived data cannot be shared between projects. For files that are relevant to one project only, this option is useful.

Related topics and activities

  * [Loading Data](<Concept_Loading%20Data.md>)

  * [Loading and Saving Filtered Data](<Filtering_Data.md>)

  * [Data Structure](<Concept_The_Studio_3_Project_File.md>)

  * [Project Files](<Concept_The_Studio_3_Project_File.md>)