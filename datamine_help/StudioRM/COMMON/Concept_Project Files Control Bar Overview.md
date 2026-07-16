# The Project Files Control Bar

To toggle the display of this control bar:

  * Activate the **Home** ribbon and select **Show >> Project Files Bar**.

  * Enter "toggle-project-files-bar" into the **[Command line](<Command_Toolbar.md>)** and press <Enter>.

The Project Files control bar is used to manage the files in the project folder. It categorizes them in folders according to a file type, e.g. points, strings, block models, macros, etc.. This is the tool for adding or removing files from the project, previewing or opening a Datamine file in the Datamine Table Editor, loading files into memory; copying and exporting project files.

A toolbar displays at the top of the **Project Files** control bar and contains the following options:

|  Description  
---|---  
![](../Icon_Popups/icProjectFiles_Collapse.gif) |  Collapse all folders in the tree, hiding their contents.  
![](../Icon_Popups/icProjectFiles_Refresh.gif) |  Refresh the project files list. This will also update the icons representing each file type. See [Project Icon Reference](<Project%20Icon%20Reference.md>).  
![](../Icon_Popups/icProjectFiles_AddNew.gif) |  Add new files to the project.  
![](../Icon_Popups/icProjectFiles_AddExisting.gif) |  Add existing files to the project.  
![](../Icon_Popups/icProjectFiles_Import.gif) |  Import external data files, saving them to Datamine format and adding them to the project.  
  
## External Files

"External" files are files that sit outside your project folder (the folder that includes your project file). You can recognize an external file by a vertical line on the left of the file icon. For example, the image below (shown at 4x size) displays a "local" file on the left (inside the project folder) and an "external" file on the right:

![](../Images/Project-Icon-External.png)

You can see where an external file is located by selecting and displaying the [Properties](<properties%20control%20bar%20overview.md>) control bar. 

## Project, Folder and Files Context Menus

Right-clicking a project, a folder or a file in the **Project Files** control bar displays a specific menu.

### Project-Level Menu

Right-click a project icon to display the following menu options:

Add |   
---|---  
\- New File | Add a new Datamine table or macro file to the current project; opens the [Add a New File](<newfile.md>) screen.   
\- Existing Files |  Add existing Datamine files to the current project; opens a file browser. The selected files are analyzed when added and sorted into the corresponding data type folder according to the information each file contains. **Note** : Datamine file(s) can also be added to the project by using drag-and-drop from a Windows Explorer window into the Project Files control bar.  
\- Import Files | Import external data files, saving them to Datamine's proprietary format and adding them to the project, using **Data Source Drivers** . A link to the original file is maintained, allowing the original data (in any supported format) to be reloaded or refreshed when required.  
**Save** | Save the current project file and associated settings.  
**Close** | Close the current project file. If changes have been made to any loaded files, a prompt displays to allow each qualifying file to be saved.  
**Paste** | If file data has been copied to the clipboard, paste it into the project. Only available if suitable clipboard contents exist.  
Rename... | Rename the current project file.  
Open Containing Folder | Open a file explorer window and display the contents of the project folder.  
**Properties** | Display general project summary information in the [Properties](<properties%20control%20bar%20overview.md>) control bar. This includes project folder location, last modified date and project file size.  
  
### Folder-Level Menu

Right-click any folder in the Project Files control bar to reveal the following menu options:

Add |   
---|---  
\- New File | Add a new Datamine table or macro file to the current project; opens the [Add a New File](<newfile.md>) screen.   
\- Existing Files |  Add existing Datamine files to the current project; opens a file browser. The selected files are analyzed when added and sorted into the corresponding data type folder according to the information each file contains. **Note** : Datamine file(s) can also be added to the project by using drag-and-drop from a Windows Explorer window into the Project Files control bar.  
\- Import Files | Import external data files, saving them to Datamine's proprietary format and adding them to the project, using **Data Source Drivers** . A link to the original file is maintained, allowing the original data (in any supported format) to be reloaded or refreshed when required.  
Cut | Not used.  
Copy | Not used.  
Paste | Not used.  
Delete | Not used.  
Rename | Not used.  
Properties | Display general folder summary information in the [Properties](<properties%20control%20bar%20overview.md>) control bar. This includes number of files contained.  
  
### Project Folder Menu

At the highest level of the 'tree', a project icon displays. Right-clicking it reveals the following:

Open Containing Folder | Open a Windows folder containing the open project.  
---|---  
  
### Data Type Folder Menu

Right-clicking a data type folder (such as Geostats Parameters, for example) reveals the following menu options:

Add>> |   
---|---  
>> New File | Create a new, empty data table or macro using the **[Add New File](<newfile.md>)** screen.  
>> Existing Files | Add a file from disk to your project. The file can be of any type.   
>> Import Files | Use the [**Data Import**](<importfiles.md>) screen to import a data file to your project and set up automated data conversion using the Data Source Drivers.  
Paste | If data has been previously copied to the clipboard, paste it into the target folder.  
Open Containing Folder | Open a Windows folder containing the open project.  
  
### Item Context Menu Options 

**Note** : Not all commands in this section may be available. For instance, Re-import is only available if the data was originally imported using **Data Source Drivers**.

Right-click a file in the **Project Files** control bar to choose from one of the following options:

Open | Open the selected file in the Datamine Table Editor for viewing and editing the file's contents.  
---|---  
Load | Load the selected file(s) into memory. If data contains visible elements, the primary 3D window updates to show that data with the default overlay for the data type.  
Preview |  View the selected file in the InTouch Go utility. Use this utility to preview 2D or 3D data before or after it is loaded into memory **Note** : InTouch Go is a standalone application and does not require a license.  
Display |  Typically used for [**Plot file**](<filetype.md#Plot>) types, display the selected file in the legacy Graphics window. **Note** : This command launches the [DISPLA](<../Process_Help_XML/displa.md>) process.  
Re-Import |  If the selected file was imported using Data Source Drivers, re-import it using the associated driver and import settings. Use this option when the source file has been edited and the changes need to be shown in the resulting imported Datamine file. If the selected file was not imported using Data Source Drivers, this option is unavailable.  
Export | Export the selected data using Datamine's **Data Source Drivers** facility.  
Remove from Project | Display general folder summary information in the [Properties](<properties%20control%20bar%20overview.md>) control bar. This includes number of files contained.  
**Cut** | Cut the selected file(s) to the clipboard and remove it from the project.  
**Copy** | Copy the selected file(s) to the clipboard.  
**Delete** |  Delete the selected file from disk. **Warning** : This action will REMOVE THE SELECTED FILE FROM DISK PERMANENTLY. Care should be taken when using this command as it cannot be undone. A confirmation dialog will be displayed before this action is performed.  
**Rename** | Rename the selected file, on disk and in the control bar.  
Open Containing Folder |  Open a file browser showing the selected file.  
Properties | Display summary file information via the [Properties](<properties%20control%20bar%20overview.md>) control bar.  
  
## Adding and Overwriting Existing Files

Adding a file to the project, which is located in the project folder, and which has already been added to the project, will result in a message indicating the number of files successfully added to the project compared to the number requested and that the remaining files "could not be added as they either already exist in the project or are not compatible with the current Studio project."

Adding a file to the project, then adding a second file of the same name, where each of these files reside in different folders, one of which could be the project folder, displays the [Duplicate Project File](<duplicateprojectfile.md>) screen.

Here, you have two choices:

  * Replace the existing file with the new file. This cannot be undone.

  * Provide a different logical name for the new file. The latest file will coexist with the original in the project thereafter.

## Loading Data

There are several options for loading data via the **Project Files** control bar:

  * Loading Data into Memory: Unless a file has been loaded into memory, it cannot be viewed in the data windows (providing the file contains viewable data). The Project Files control bar supports a drag-and-drop interface that allows you to load a file (thus making it an object) by left clicking a file, holding the button down and dragging it into either the **Plots** or **3D** windows.

When a file has been loaded, the view of the data is automatically updated.

  * Loading Filtered Files: It is possible to filter data as part of the loading process by holding down the <Ctrl> key when using either the file's context menu option or the drag-and-drop method. This displays the [Object Filter](<Object%20Filter%20Dialog.md>) dialog, appropriate to the data type(s) being loaded, allowing **Data Fields** , **Coordinate Fields** , **Control Fields** and **Filters** settings to be defined.

  * Loading Multiple Files It is possible to select more than one file from the **Project Files** control bar, and drag them simultaneously into a data window to load multiple files in a single action. If an object fails to load, for example, if you elect to filter incoming data using the <Ctrl> key (see above) and you **Cancel** the filter screen for a particular file, you are given the option to load the remaining files.

Related topics and activities

  * [Browser Bars](<Studio%203%20Browsers.md>)

  * [Project Icon Reference](<Project%20Icon%20Reference.md>)

  * [Project Data Control Bar](<PD%20Bar-RM.md>)