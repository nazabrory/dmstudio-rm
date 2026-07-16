![](../HeaderCell.jpg) |  Displaying Log Sheet Column Data Defining the drilhole data columns for display in the log sheet.  
---|---  
  
# Overview

In this portion of the tutorial you are going to define the drillhole data columns to be displayed in your log sheet.

## Prerequisites

Required:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

  * Inserted a new VB2675 Log sheet - see exercises on the [Opening, Copying and Inserting Log Sheets](<Opening_Copying_and_Inserting_Log_Sheets.md>) page.

  * Selected the hole VB2737 in the newly inserted log sheet - see exercise on the [Selecting Drillholes](<Opening_Copying_and_Inserting_Log_Sheets.md>) page.

Recommended:

  * Modified the log View settings for the VB2737 Log sheet - see exercise on the [Modifying Log View Settings](<Modifying_Log_View_Settings.md>) page.

## Exercise: Displaying Log sheet Column Data

In this exercise, you are going to define the downhole data columns to be displayed in the VB2737 log sheet. This includes the following tasks:

  * Defining the downhole columns

  * Setting the column display order

**Defining the Downhole Columns**

  1. Using the Manage ribbon select the Layout toggle to enable it, if not already selected.

  2. Select the Logs window.

  3. Select the VB2737 sheet tab.

  4. Left-click anywhere within the Log View to show the surrounding frame as a dotted line, then right click to select  Hole Log Frame (VB2737) Properties Select _L og_ | _H_ ole... .

![note.gif \(1017 bytes\)](../images/note.gif) |  If _Log_ | _H_ ole... is greyed out, click inside the Log Header area in the log sheet - this should activate the function.  
---|---  
  
  1. In the Log View Properties dialog, select the Columns tab.

  2. In the Columns group, click Add....  
  
![](../Images/dp_Displaying%20Log%20Columns%201.jpg)

![note.gif \(1017 bytes\)](../images/note.gif) |  Log sheet columns can also be moved up or down, deleted, copied and renamed using the relevant buttons in the Columns group.  
---|---  
  3. In the Column Wizard (1) dialog, select the Data Column option and then click Next.  
  
![](../Images/dp_Displaying%20Log%20Columns%202.jpg)  

  4. In the Column Wizard (2) dialog, table list, select [Assays$_vb_assays], click Next.  
  
![](../Images/dp_Displaying%20Log%20Columns%203.jpg)  

  5. In the Column Wizard (3) dialog, fields list, select [Density], click Next.  
  
![](../Images/dp_Displaying%20Log%20Columns%204.jpg)  

  6. In the Column Wizard (4) dialog, style list, select [Line Graph], click End.  
  
![](../Images/dp_Displaying%20Log%20Columns%205.jpg)  

  7. Back in the Log View Properties dialog, Columns in View pane, check that the data column DENSITY has been added to the bottom of the list, as shown below:  
  
![](../Images/dp_Displaying%20Log%20Columns%206.jpg)  

  8. Click Apply (do not close the Log View Properties dialog).

  9. In the VB2737 sheet tab, check that the log sheet now includes the extra DENSITY column on the far right, as shown below:  
  
![](../Images/dp_Displaying%20Log%20Columns%207.jpg)

Setting the Column Display Order

  1. In the Log View Properties dialog, Select the Columns tab.

  2. In the Columns group, Columns in View pane, select the [Elevation] column, click Up (x5).

  3. Select the [DENSITY] column, click Up (x3).

  4. In the Columns in View pane, check that your column order is as shown below, click OK:  
  
![](../Images/Plot10.jpg)  

  5. In the VB2737 sheet tab, check that the log sheet now displays the log sheet columns as shown below:  
  
![](../Images/Plot11.jpg)  
  

![note.gif \(1017 bytes\)](../images/note.gif) |  The Hole Log Frame is no longer centred in the page and also extends beyond the page limits. This will be corrected in the next exercise.  
---|---  

![](../Images/NextExercise.gif)[Proceed to the next topic](<formatting_the_hole_log_frame.md>)