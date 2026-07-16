![](../HeaderCell.jpg) |  Displaying Plot Sheet Data Selecting the correct plot sheet data for display.  
---|---  
  
# Overview

In this portion of the tutorial you are going to define which data are to be displayed on a plot sheet. This is done by means of the plot sheet's data Overlays.

## Prerequisites

Required:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises on the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

  * Copied and renamed the Plan sheet - see previous exercises on the [Opening, Copying and Inserting Plot Sheets](<Opening_Copying_and_Inserting_Plot_Sheets.md>) page.

## Link to exercises

The following exercises are available on this page:

  * Displaying Plot Sheet Data

## Exercise: Displaying Plot Sheet Data

In this exercise, you are going to load data objects and select the data Overlays that are to be displayed in the Plan 2 plot sheet, these include the overlays for the static drillholes, topography contours and fault surfaces.

Controlling the Display of Data

  1. Using the Project Files control bar, expand the All Files folder and drag the following objects into the Plots window to load them into memory:  
  
_vb_collars.dm  
_vb_faulttr,dm  
_vb_holes.dm  
_vb_mintr.dm  
_vb_modgrd.dm  
_vb_modopt.dm  
_vb_stopo.dm  
_vb_stopotr.dm  
_vb_viewdefs.dm  
  
(You may receive a message indicating the model file you are loading is read-only - if so, click OK to continue)  

  2. Select the Plan tab.
  3. Open the Sheets control bar, and Plots | Plan | Plan Projection | Overlays \- you should see the following:  
  
![](../Images/Plot4.jpg)  

  4. Turn ON the display of only the following Overlays (by ticking or clearing the relevant boxes to the left of each Overlay item):

  1.      1.         * Grid
        * _vb_stopo.dm (strings)
        * _vb_holes (drillholes)
        * _vb_faulttr/_vb_faultpt (wireframe)

  5. Select the Plan sheet tab, check that only the drillholes, topography contours and fault surfaces are displayed, as shown below.  
  
![](../Images/dp_Displaying%20Plot%20Sheet%20Data%201.gif)

![note.gif \(1017 bytes\)](../images/note.gif) |  An overlay represents a single view of a loaded data file or object. Each data file (object) can have multiple overlays. This means that you can simultaneously view the same object in different ways on a plot sheet. This can be used for example, to display a block model slice as filled colored blocks on one overlay and as hatched blocks, with a different color legend on another.  
---|---  
  
![](../Images/NextExercise.gif)[Proceed to the next topic](<Formatting_Overlays.md>)