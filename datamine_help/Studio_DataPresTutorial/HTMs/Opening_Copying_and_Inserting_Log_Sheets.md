![](../HeaderCell.jpg) |  Opening, Copying and Inserting Log Sheets Opening, copying and inserting new log sheets.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools and methods available for opening, copying and inserting new log sheets in the Logs window.

## Prerequisites

You have already completed the following:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

## Link to exercises

The following exercises are available on this page:

  * Preparing Dynamic Drillhole Data and an Initial Log
  * Copying and Renaming a Log Sheet

## Exercise: Preparing Dynamic Drillhole Data and an Initial Log

In this exercise, you are going to open the VB2675 sheet in the Logs window and view the corresponding Log sheet components in the Sheets control bar. This exercise contains the following tasks:

  * Constructing dynamic drillhole data to form a hole set for logging
  * Opening a Log Sheet
  * Viewing the Log Sheet Items in the Sheets Control Bar

Creating Dynamic Drillhole Data

More information on defining and building hole data can be found in your core system help file. In this exercise, assays, collars and survey data will be used to form a dynamic (multi-table) drillhole data set in memory, and one of the associated holes will be used as a basis for setting up a strip log.

  1. Unload any data that may be loaded from previous exercises (shortcut: click inside any plot sheet view and type "ua" to trigger the unload-all command.
  2. Select the Plots window.
  3. Select the Project Files control bar.
  4. Drag the following files into the Plots window from the All Files folder.  
  
_vb_collars.dm  
_vb_assays.dm  
_vb_surveys.dm  
_vb_lithology.dm  
  
(Note how only the collar point data is shown after loading - this is because the remaining 3 tables are non-visual, and will shortly be assembled into a 3D dynamic drillhole data set).
  5. Activate the  Sample Analysis ribbon and click  Define Holes Select Tools | Define Holes
  6. In the Define Hole Tables dialog, select the following options:  
  
Collars: _vb_collars.dm - set the Length, Azimuth and Inclination field assignments to [absent] and click OK.  
Assays: _vb_assays.dm - confirm all default field assignments and click OK.  
Surveys: _vb_surveys - confirm all default field assignments and ensure the Positive Dip Values Point option is set to Down. Click OK.  
Lithology: _vb_lithology.dm - change the Lithology field assignment to [NLITH] and the Description to [LITH]. Click OK.
  7. In the Define Hole Tables dialog, click OK.
  8. Activate the  Plot View ribbon and select  Scale | Fit Select  View | Scale | Fit all Data   

**Opening a Log Sheet**

  1. Activate the  Manage ribbon and select  Insert | Sheet | Log Select the  Logs window.

  2. Select the second VB2675 sheet tab.

  3. Check that your displayed sheet is as shown below:  
  
![](../Images/Plot6.jpg)

**Viewing the Log Sheet Items in the Sheets Control Bar**

  1. Select the Sheets control bar.

  2. Expand the Data Presentation Tutorial.dmproj project, expand the Logs folder.

  3. In the Logs folder, fully expand the second VB2675 folder by clicking on all the "+" boxes next to each item, as shown below:  
  
![](../Images/Plot7.jpg)

![note.gif \(1017 bytes\)](../images/note.gif) |  Clicking on different items listed below the VB2675 folder , in the Sheets control bar, will highlight the corresponding log sheet items in the Log sheet tab. Selected Log sheet items in the Logs window's sheet are indicated by dashed border lines.  
---|---  
  
**![](../images/UpArrow.gif)**Top of page

## Exercise: Copying and Renaming a Log Sheet

In this exercise, you are going to copy the second VB2675 sheet and then rename this sheet to 'VB2675 Fixed Name' . The exercise procedures are as follows:  

**Copying a Log Sheet**

  1. Select the Logs window.

  2. Select the second VB2675 sheet tab.

  3. Right-click the lowest VB 2675 log description in the Sheets control bar and click Copy VB2676.

  4. Right click the top-level  Logs folder in the  Sheets control bar and select  Paste Select  E dit | Copy Sheet .

  5. Check that a new sheet with the name 'Copy of VB2675' has been added to the Logs window, as shown below:  
  
![](../Images/Plot8.jpg)

![note.gif \(1017 bytes\)](../images/note.gif) |  In the Sheets control bar, a new sheet item, Copy of VB2675, is also added to the Logs folder at the bottom of the existing list of sheets.  
---|---  
  
**Renaming a Log Sheet**

  1. Right-click on the Copy of VB2675 sheet tab in the Logs window, select Rename....

  2. In the Rename Sheet dialog, define the Name: as 'VB2675 Fixed Name', click OK.

  3. Check that the sheet tab is now labeled 'VB2675 Fixed Name'.

![note.gif \(1017 bytes\)](../images/note.gif) |  The corresponding Sheets control bar sheet item is also renamed to VB2675 Fixed Name. Renaming a log sheet will turn off the "automatic naming" feature of that sheet. This "automatic renaming" can be reset by following the instructions in the Rename Sheet dialog.  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif) |  The log sheet is automatically named using the Hole name property. The log sheet can be renamed using the method shown in the exercise Copying and Renaming a Log Sheet.  
---|---  
  
![](../Images/NextExercise.gif)[Proceed to the next topic](<selecting_drillholes.md>)