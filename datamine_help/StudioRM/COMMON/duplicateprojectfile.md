# Duplicate Project File

To access this screen:

  * Attempt to load a file with the same name as one existing in the current project, but existing in a different location.

This screen is displayed whenever an attempt is made to introduce a new file into the project, which has an identical name to an existing item, but is found in a different location than the original.

**Note** : this screen is not displayed if you attempt to reload an existing file. In this situation, an object is created in memory with an automatically generated name to indicate it is a duplicate. See [Data Reload](<Data%20Reload%20Dialog.md>)

If a duplicate project file is detected, you have the following choices:

  * Replace the existing file with the new filethe file from the new location overwrites the existing file of the same name, with the new source location stored in the resulting object. When this data is refreshed, or reloaded, it is the _new_ source location that is relevant. In effect, all links to the original file are lost.

  * Provide a different logical name for the new fileedit the current file name (this must be different to the original file name). The term 'logical' indicates that the new description applied is used when referencing the data that is loaded; **the actual file name is not changed**. Both the original object and new object coexist within the same project, and even though the underlying file names are identical, they are referenced using different metadata in the application.

  * Don't ask again this sessiondefine future file duplicate checking behaviour:

    * If **checked** , duplicate project files are added to the project without further prompts in the current project session. 

    * If **unchecked** (the default setting), the **Duplicate Project File** screen reappears each time a project file is added that has a different file path to an identically named project file.

Related topics and activities

  * [Data Import](<data%20import%20dialog.md>)

  * [ Importing and Exporting Data](<Concept_Importing%20and%20Exporting%20Data.md>)

  * [Project Wizard](<ProjectWizard.md>)