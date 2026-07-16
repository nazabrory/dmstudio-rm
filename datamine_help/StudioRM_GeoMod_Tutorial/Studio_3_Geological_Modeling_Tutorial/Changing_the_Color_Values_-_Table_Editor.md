# Changing the Color Values - Table Editor

![](../HeaderCell.gif) |  Changing the Color Values of Topography Contours How to change the default color of the topography contour strings using the Table Editor.  
---|---  
  
# Overview

In this part of the tutorial you will use DatamineTable Editor to change the default color of the topography contour strings.

## Prerequisites

  * Completed the [Creating a New Project](<Creating_a_New_Project.md>) exercise.

  * [Files](<Tutorial_Files_List.md>) required for the exercises on this page:

  *     * _ostopoi.dm

## Exercise: Changing the COLOUR Value of Topography Contours

In this exercise, you will edit the imported topography contour strings file _ostopoi that was imported from the CAD file _vb_stopo.dwg (see exercise [Importing Topography Contours from a CAD File](<Importing_Topography_Contours.md#Exercise1>)). The values in the default color field COLOUR will be changed from '1' (Grey) to '10' (Bright Green) using the Find and Replace tools.  

![note.gif \(1017 bytes\)](../Images/note.gif) | 

  * Default color values, stored in the standard Datamine field COLOUR, range from 1 to 64. These values and associated colors are displayed in the Standard DatamineCOLOURfields legend in the System Legends folder of the Legends Manager (Activate the Format ribbon and select Format|Legends).
  * 3D Objects (e.g. strings, wireframes, block models) can be colored either by setting default color values in the field COLOUR or by using color Legends.
  * Refer to the your online Help for more details on using Legends.

  
---|---  
  
## Creating a Working Copy of the Contour Strings

  1. Select the Project Files control bar, Strings folder.

  2. Right-click _ostopoi and select Copy.

  3. Right-click the folder Strings and select Paste.

  4. Right-click on Copy of_ostopoi and select Rename....

  5. In the Rename Project File dialog, define the new filename in To: as 'stopo.dm' and click OK.  

## Changing the COLOUR Value using the Datamine Table Editor

  1. In the Project Files control bar, expand the Strings folder.

  2. Double-click stopo.

  3. In the Table Editor dialog, select the column COLOUR(N) by clicking the title bar.

  4. Click Find.

  5. In the Find and Replace (in selection) dialog, Replace tab, type '1' in the Find What: box, and '10' in the Replace With: box.

  6. Select the Search option [By Records].

  7. Select the Match entire field contents check box, and click Replace All.

  8. In the Table Editor (1828 fields updated) dialog, click OK.

  9. In the Find and Replace (in selection) dialog, click Close.

  10. In the Table Editor dialog, check that the values in the COLOUR column are all set to "10" and click Save.

  11. Select File | Exit to close Table Editor\- discard the changes you have just made.

![note.gif \(1017 bytes\)](../Images/note.gif) | 

  * Datamine tables and *.csv files can be edited with Datamine Table Editor from within Windows Explorer (right-click table and select Open With | Table Editor)
  * Tables can also be edited and viewed using the processAED (this can be recorded and used in Macros and Scripts).

  
---|---  
  
**![](../Images/NextExercise.gif)**[Next Section](<Importing_Drillhole_Data_Tables.md>)