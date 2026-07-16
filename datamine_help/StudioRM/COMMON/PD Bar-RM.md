# Project Data Control Bar

To toggle the display of this control bar: 

  * **Home** ribbon **> > Show >> Project Data**.

The Project Data control bar manages the data files associated with the open project. It is also used to access **3D** window and **Plots** window overlays.

  * See [3D Data Folders](<../VR_Help/SheetsOverview.md>).

  * See [The Plots Window](<Window_PLOTS_Overview.md>).

Data files are categorized according to their expected use (as denoted by the presence of system attributes). 

Data such as prototype models, variograms, geostatistics parameter files are represented by a folder container. If data of a particular type is associated with the project, a folder appears.

The **Project Data** bar displays a toolbar at the top to access useful file-related functions:

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
  
### 3D Folders

The context menus for the 3D folder are the same as those found for the Sheets control bar's [3D Data Folders](<../VR_Help/SheetsOverview.md>).

### Plots Folders

For more information on Plots folders, see [The Plots Window](<Window_PLOTS_Overview.md>).

  * [Import Project Files](<importfiles.md>)

  * [Properties Control Bar](<properties%20control%20bar%20overview.md>)

  * [3D Data Folders](<../VR_Help/SheetsOverview.md>)

  * [The Plots Window](<Window_PLOTS_Overview.md>)