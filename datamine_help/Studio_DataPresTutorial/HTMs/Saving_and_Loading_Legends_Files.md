![](../HeaderCell.jpg) |  Saving and Loading Legend Files How to export and import legend files.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools used to export and import legend files.

## Prerequisites

Required:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

## Link to exercises

The following exercises are available on this page:

  * Exporting a Legend to a Legend File
  * Importing a Legend File

## Exercise: Exporting a Legend to a Legend File

In this exercise, you are going to export a project legend to a legend file.

![note.gif \(1017 bytes\)](../images/Tip.gif) |  Save legends to Legend Files in order to share legends between projects for:

  * your own use across multiple Studio projects,
  * implementing formatting standards within a department, office or organization.

  
---|---  
  
The exercise steps are as follows:

Exporting to a Legend File

  1. Select the Plots window.
  2. Select Format |Legends... or in the Format toolbar, click Format Legends.
  3. In the Legends Manager dialog, legends pane, expand the project legends folder:  
  
![](../Images/dp_Exporting%20a%20Legend%20File%201.jpg)  
  
![note.gif \(1017 bytes\)](../images/note.gif)| System and User legends can also be selected for export to a legends file.  
---|---  
  4. In the slider bar on the right, page down (x1), right-click the Datamine: AU (_vb_holes) legend, select Save Legend.
  5. In the Save As dialog, browse to your project folder, define the File name: as 'Datamine: AU _vb_holes 2', select the Save as type [Datamine Legend Files (*.elg)], click Save:  
  
![](../Images/dp_Exporting%20a%20Legend%20File%202.jpg)
  6. Back in the Legends Manager dialog, click Close.
  7. In the Windows Explorer dialog, browse to your project folder and check that the new legend file Datamine AU _vb_holes 2.elg has been saved.

**![](../images/UpArrow.gif)**Top of page

## Exercise: Importing a Legend File

In this exercise, you are going to import the legend file Datamine AU _vb_holes 2.elg , created in the previous exercise. The exercise steps are as follows:

Importing a Legend File

  1. Select the Plots window.
  2. In the Format toolbar, click Format Legends or select Format |Legends....
  3. In the Legends Manager dialog, legends pane, select the project legends folder:  
  
![](../Images/dp_Importing%20a%20Legend%20File%201.jpg)  
![note.gif \(1017 bytes\)](../images/note.gif)| 
     * Legend files can also be imported either to the User Legends or the Project Legends folder.
     * User Legends are saved in the user.elg file and are available to all projects run on the PC on which the file is stored.
     * Project Legends are stored within a project file and so are only available in the current project.  
---|---  
  4. In the Available Legends group, click Load Legend....

  5. In the Open dialog, browse to your project folder, select the file Datamine AU _vb_holes 2.elg , click Open:  
  
![](../Images/dp_Importing%20a%20Legend%20File%202.jpg)  

  6. In the Available Legends group, project legends folder, check that the legend has been added to the bottom of the list:  
  
![](../Images/dp_Importing%20a%20Legend%20File%203.jpg)  

![note.gif \(1017 bytes\)](../images/note.gif) |  Studio uses the stored legend Name (displayed in the Legend Properties group on the right of the Legends Manager dialog, when a legend is selected from the list) and not the file name, when loading legend files.  
---|---  
  7. Back in the Legends Manager dialog, click Close.

![](../Images/NextExercise.gif)[Proceed to the next section](<Creating_a_Single_Histogram_Chart_Sheet.md>)

Checklist:

  1. The topic is stored in the relevant tutorial area of the RoboHelp X5 project.

  2. All topics created with this template are set at TOPIC-LEVEL to the relevant TUTORIAL build tag.

  3. Related topics are not normally required - use BROWSE SEQUENCES instead.

  4. Popups

  5. Browse sequences

  6. Index

  7. TOC

  8. Glossary Items

Document History |   
---|---  
Date |  Description  
201005 | 

  * Updated to reflect MR19 functionality

  
201107 | 

  * Updated to reflect MR20 functionality

  
201202 | 

  * Updated to:
  *     * reflect MR21 functionality
    * replace 'Datamine' term with 'Studio', 'CAE Mining', etc.
    * apply templates with new 'CAE Datamine Corporate' copyright notice