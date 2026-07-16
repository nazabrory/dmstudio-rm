# Project Browser

To access this screen:

  * This screen is displayed in response to a wide range of system functions, whenever a project file needs to be selected from either your current project files, or from a local or network folder location.

The **Project Browser** can be used to load data into your current project and also review and edit summary information of other files.

Each file shown in the **Project Browser** is represented by a description and icon. The icon defines the type of file that is available for loading. See [Project Icon Reference](<Project%20Icon%20Reference.md>).

Added files appear in the **[Project Files](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)** control bar and (if your product supports one) the **Project Data** control bar. From there, you can load the data into memory and potentially view and edit it.

Files displayed may be filtered, if the command used to display the browser relates to a particular type of data (drillholes, for example). Otherwise, all project files are listed.

Tip: Right click files displayed in the **Database Tables** list for a context menu containing useful file management options.

Note: Regardless of how the browser is opened, any type of data can be added to your project.

### Manage Project Files

To load existing project files using the Project Browser:

This activity is used to load a file that has already been added to your project. If your file is not a part of your project yet, see the following procedure.

  1. Display the **Project Browser**.

  2. Use the **Database Tables** menu to locate the file you want to load.

Note: The **Project Browser** can only load one file at a time.

  3. Select a file to see its **Fields**. This display provides summary information on the fields (attributes) of the file.

  4. Review the file's **Properties** :

     * _Name_ The name of the file without a file extension.

     * _Full Path_ The fully qualified folder path to the file on disk.

     * _File Type_ See [File Types](<filetype.md>).

     * _Columns_ The number of fields in the file (fields, columns and attributes are synonymous).

     * _Records_ The number of data records (rows) in the selected file.

     * _Description_

     * _Precision_ Either _Single_ or _Extended_. All modern Studio products generate extended precision files.

     * _Linked_ If the file is a link file (a small file place holder containing the location of another file) this is _Yes_ , otherwise _No_.

     * _Exists_ _Yes_ if the file exists at the expected **Full Path** or _No_ if it is missing.

     * _Modified_ The last time the file was changed.

     * _Size_ The size of the file (on disk).

  5. Click **OK**.

The selected file loads and, if appropriate, displayed in the primary 3D window and associated linked windows.

To load a new file and add it your project in the same operation:

  1. Display the **Project Browser**.

  2. Browse for a new **Filename**.

A Windows browser displays.

  3. Locate the file on disk to load and click **Open**.

The selected file name displays.

  4. Click OK.

The selected file is loaded and added to the current project.

  5. Save your project.

Related topics and activities

  * [Loading and Refreshing Data](<Concept_Loading%20Data.md>)

  * [Data Import](<data%20import%20dialog.md>)

  * [Data Object Manager](<Data%20Manager%20Dialog.md>)

  * [The Project Files Control Bar](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)

  * [File Types](<filetype.md>)