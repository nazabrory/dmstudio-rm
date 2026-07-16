![](../HeaderCell.jpg) |  Combining Wireframe Models Combining the required portions of two separate wireframe models.  
---|---  
  
# Overview

In this part of the tutorial you are going to extract and combine the required portions of two separate open pit and surface topography wireframes.

![](../Images/vrt_ExtractAndCombineWireframes%201.jpg)

## Prerequisites

  * Created a new project and added all the required tutorial files i.e. the exercise on the [Creating a New Project](<Creating_a_New_Project.md>) page.

  * Displayed the VR Window i.e. the exercise on the [Introducing the VR Window](<The_VR_Window_Principles.md>) page.

  * Displayed the VR toolbars i.e. the exercise on the [Displaying the Toolbars](<Displaying_the_Toolbars.md>) page.

  * Loaded the required data i.e. the exercises on the [Loading Data into the VR Window](<Loading_Data_Into_VR.md>) page.

  * [Files](<Tutorial_Files_List.md>) required for the exercises on this page:

  *     * _vb_qpitpt

    * _vb_qpittr

    * _vb_stopopt

    * _vb_stopotr

# Exercises

The following exercises are available on this page:

  * Combining Open Pit and Topography Wireframes

## Exercise: Combining Open pit and Topography Wireframes

In this exercise you are to use wireframe boolean commands to first extract and then combine the required portions of separate open pit design and surface topography wireframes.

## Displaying the Exercise Data and Controls

  1. Select the VR window.

  2. Select the Sheets control bar and expand the VR Wireframes folders.

  3. Select only the following check boxes (i.e. display these objects):

     * _vb_qpittr/_vb_qpitpt (wireframe)

     * _vb_stopotr/_vb_stopopt (wireframe)  

![note.gif \(1017 bytes\)](../Images/note.gif) |  Only these two wireframe objects should be displayed in the VR window; all other Strings, Wireframes and Block Model overlays should be hidden.  
---|---  
  4. In the Indicators toolbar, toggle ON the Axis Controller.

  5. In the VR View toolbar, click Plan.

  6. In the VR window, check that the surface topography (green) and the pit design (blue) are displayed:  
  
![](../Images/vrt_ExtractAndCombineWireframes%202.jpg)  

![note.gif \(1017 bytes\)](../Images/note.gif) |  The above images shows an unmined surface topography wireframe (green) and a planned open pit design wireframe (blue) which lies mostly below, but which also extends above the topography surface. In order to create a visually acceptable result, the blue portion above the topography and the green portion within the pit would, for example, need to be removed. The resultant wireframe pieces could, if required, also be combined into a single wireframe object.  
---|---  

## Extracting and Identifying the Individual Wireframe Portions

  1. In the Boolean Operations toolbar, click Extract Separate Wireframes.

  2. In the Extract Separate dialog, define the settings shown below, click OK:  
  
![](../Images/vrt_ExtractAndCombineWireframes%203.jpg)

  3. In the Studio 3 confirmation dialog, click Yes:  
  
![](../Images/vrt_ExtractAndCombineWireframes%204.jpg)  

  4. In the Sheets control bar, VR Wireframes folders, select only the following check boxes (i.e. display these objects):

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 1

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 2

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 3

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 4

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 5

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 6  

![note.gif \(1017 bytes\)](../Images/note.gif) |  The two wireframe objects used to generate these extractions should be hidden.  
---|---  
  5. Sequentially hide and then display each of the above wireframe extractions and identify which objects represent firstly, the topography outside the pit and secondly, the pit below the topography.

  6. Display only these objects, as shown below:  
  
![](../Images/vrt_ExtractAndCombineWireframes%205.jpg)  

![note.gif \(1017 bytes\)](../Images/note.gif) |  The three wireframe objects shown in the above image are:
     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 1 \- the pit below the topography surface.
     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 3 \- the pit below the topography surface (a very small portion - hardly visible).
     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 4 \- the topography outside the pit.  
---|---  

## Combining the Wireframes

  1. ## Select Data | Object Operations | Combine Objects.

  2. ## In the Combine Data Objects dialog, select the following three wireframe type Loaded Objects and add them to the Combine List:

  1.      * ## Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 1

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 3 

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 4

  3. ## Define a new object name 'PitTopo', check the selected objects and define the settings shown below, click OK:  
  
![](../Images/vrt_ExtractAndCombineWireframes%206.jpg)

  4. ## In the Loaded Data and Sheets control bars, check that the new PitTopo wireframe object and overlay are listed.

## 

## Unloading the Unwanted Objects

  1. Select Data | Unload.

  2. In the Data Unload dialog, using <Ctrl>+Click, select the following objects, click OK.

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 1

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 2

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 3

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 4

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 5

     * Extract:_vb_qpittr/_vb_qpitpt and_vb_stopotr/_vb_stopopt - 6

  3. In the VR window, in a zoomed northern view, check that the new object contains the following pit and topography components as shown below:  
  
![](../Images/vrt_ExtractAndCombineWireframes%207.jpg)

**![](../images/UpArrow.gif)**Top of page

Document History |   
---|---  
Date |  Description  
201106 | 

  * Added to reflect MR20 functionality

  
201202 | 

  * Updated to reflect MR21 functionality

  
  
Checklist:

  1. The topic is stored in the relevant tutorial area of the RoboHelp X5 project.

  2. All topics created with this template are set at TOPIC-LEVEL to the relevant TUTORIAL build tag.

  3. Related topics are not normally required - use BROWSE SEQUENCES instead.

  4. Popups

  5. Browse sequences

  6. Index

  7. TOC

  8. Glossary Items

Also, please check the online Procedures project for more information.