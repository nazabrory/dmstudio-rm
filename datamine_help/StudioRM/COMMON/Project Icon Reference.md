# Project Control Bar Icons

Project files can be of various types (wireframes, strings etc.) and can come from a variety of file locations and in different formats.

Data can be imported from a data source, such as a simple text file, found within the project folder or externally and other variations, and combinations of scenarios. For this reason, project files are represented by a combination of an identifying icon, and specific formats for each file description.

This topic outlines the different icons displayed to differentiate these project file references, when viewed in the **[Project Files control bar](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)**.

**Note** : The current view of project icons in the **Project Files** control bar is correct up to the last time it was refreshed. Use F5 or the **Refresh** button to update it.

## Project File Icons

Certain areas of your application display project files in iconic format, for example, the Project Files control bar and the [Project Browser](<ProjectBrowser.md>) dialog.

Each file type is represented by a unique icon. The table below shows the different iconic identifiers available:

Icon |  File Type |  Description  
---|---|---  
Various |  Project Icon |  Top-level project icon shown at the top of the Project Files, Loaded Data, Holes and Sheets control bars.  
![](../Images_STUDIORM_ONLY/Project_Bar_Icons/Folder_Closed.png) |  Closed Folder |  Indicates a closed (collapsed) tree item. These items can be expanded to show the items within it.  
![](../Images_STUDIORM_ONLY/Project_Bar_Icons/Folder_Open.png) |  Open Folder |  Indicates an open (expanded) tree item. Expanded items show the items relevant to that menu section.  
![](../Images_STUDIORM_ONLY/Project_Bar_Icons/DSDIE.png) |  Imported File |  This overlay icon can be applied to other icon combinations, for example, an Excel or ASCII text file to show that it has been subject to the Data Import process, using Data Source Drivers.  
![](../Images/ProjectFile9_Not_In_Directory.gif) |  External File |  This overlay icon indicates that the file is not located within the currently defined project directory.  
![](../Images_STUDIORM_ONLY/Project_Bar_Icons/FileMissing.png) |  File Not Found |  Indicates a file that is associated with the current project, but could not be found in the location specified in the project file.  
![](../Images_STUDIORM_ONLY/Project_Bar_Icons/EPFile.png) |  .dmx file |  A file in the proprietary .dmx Datamine binary file format.  
![](../Images_STUDIORM_ONLY/Project_Bar_Icons/SPFile.png) |  .dm file |  A file in the legacy .dm Datamine binary file format.  
![](../Images_STUDIORM_ONLY/Project_Bar_Icons/ASCII.png) |  Text File |  Indicates an ASCII text file that is not associated with any other default application.  
  
In addition to the above icons, the list may also include system default icons for established file types (a comma delimited file may be associated with a Microsoft Excel icon, for example.

## Other Conditional Formatting

As well as associating project files with a particular icon, you application also formats the text used for the file name to indicate the state of the file in question, providing this option is enabled on your OS. This is DISABLED by default. To enable this option select Tools | Options in Windows Explorer, and select the option Show encrypted or compressed NTFS files in color.

Example| Means...  
---|---  
![](../Images/FileName_Black.gif)| Indicates an uncompressed file format.  
![](../Images/FileName_Blue.gif)| Indicates a compressed file format  
  
Related topics and activities

  * [Project Files Control Bar Overview](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)

  * [Project Browser](<ProjectBrowser.md>)