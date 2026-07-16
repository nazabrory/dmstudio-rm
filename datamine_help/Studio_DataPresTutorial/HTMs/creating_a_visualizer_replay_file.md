![](../HeaderCell.jpg) |  Creating a Visualizer Replay File Creating a Visualizer Replay File.  
---|---  
  
# Overview

In this portion of the tutorial you are going to create a standard Visualizer Replay File that can be used for presentation purposes.

## Prerequisites

You have already completed the following:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the Opening and Saving Projects page.

## Links to exercises

The following exercises are available on this page:

  * Creating a Visualizer Replay File

## Exercise: Creating a Visualizer Replay File

In this exercise, you are going to create a Visualizer Replay File from the data loaded in the Design and Visualizer windows and save it to the file Visualizer View 1.gvp. This exercise contains the following tasks:

  * Displaying and Formatting loaded data
  * Creating a Visualizer Replay file
  * Adding the file to the project.

**Displaying and Formatting loaded data**

  1. Select the Design window.
  2. In the View Control toolbar, click Use Clipping to toggle OFF the primary clipping.
  3. In the View Control toolbar, click Get View, in the Command toolbar, Run Command line, type '1' (i.e. the Plan view), press <Enter>.
  4. In the Sheets control bar, fully expand the Design folder.
  5. Turn ON the display of only the following Overlays (i.e. check the boxes to the left of each item): 
     * _vb_holes(drillholes)
     * _vb_faulttr/_vb_faultpt (wireframe)
     * _vb_mintr/minpt (wireframe)
     * _vb_stopotr/stopopt (wireframe)
  6. Using the Format Display dialog, format each of the following Overlays, setting the Style tab, Display As options to Faces: 
     * _vb_faulttr/_vb_faultpt (wireframe)
     * _vb_mintr/minpt (wireframe)
     * _vb_stopotr/stopopt (wireframe)
  7. Compare your Design window view with that shown below:  
  
  
![](../Images/dp_Creating%20Visualizer%20Replay%20Files%201.jpg)  

  8. Select _F_ ormat | Visualizer | Update Visualizer Objects.
  9. In the Visualizer window, rotate, pan and zoom the view so that you view the data from above and the south west.
  10. Right-click, select Wireframe | Make Transparent, compare your view to that shown below:  
  
  
![](../Images/dp_Creating%20Visualizer%20Replay%20Files%202.jpg)  

**Creating a Visualizer Replay file**

  1. Select File | Publish Visualizer View.
  2. In the Save visualizer replay file dialog, select the Save in folder [DataPres], define the File name as 'Visualizer View 1', select the Save as type [CAE visualizer replay files (*.gvp,*.gvz)], click Save.  
  
  
![](../Images/dp_Creating%20Visualizer%20Replay%20Files%203.jpg)

**Adding the file to the project**

  1. In the Project Files control bar, click Add Existing Files to Project.
  2. In theSelect files to add to projectdialog, select theFiles of typeoption [All Files (*.*)]
  3. Select the fileVisualizer View 1.gvzfrom the file list, clickOpen.
  4. In theStudio 3confirmation dialog, clickOK.
  5. In theProject Filescontrol bar, check that the file has been added to theAll Files (*.*)folder.   
  
![note.gif \(1017 bytes\)](../images/note.gif) |  The above 3 steps are not required if the Detect files added...while the project is open option is set. This can be set under File | Settings... | General.  
---|---  

![](../Images/NextExercise.gif)[Proceed to the next topic](<viewing_a_visualizer_replay_file.md>)

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