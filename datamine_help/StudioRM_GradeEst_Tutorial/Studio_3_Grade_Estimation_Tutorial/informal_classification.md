![](../HeaderCell.jpg) |  Informal Classification Informal classification of a grade block model into confidence categories.  
---|---  
  
# Overview

In this portion of the tutorial you are going to classify a grade block model into confidence categories using the kriging variance values. This will be done visually in the Design window.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _ubm5g

## Exercise: Informal Classification of Grade Estimates Using the Kriging Variance

In this exercise you are going to calculate a category field in the block model using the process EXTRA, based on a set of kriging variance ranges for the Au grade estimates (field VAU). The resultant model will then be formatted and viewed in the Design window using the following parameters:

  * Grade block model: 5m regular celled (no sub-cells), zone flagged, block model

  * Kriging variance field: VAU

  * Categories and variance ranges:

  *     * CAT = 1: VAU <= 3

    * CAT = 2: 3 > VAU <= 6

    * CAT = 3: 6 > VAU

The 3D grade block model and drillhole samples are shown in the image below. The block model cells are colored according to the three separate mineralization zones (cyan: ZONE=1, green: ZONE=2, red: ZONE=3). The fold axis of the ore body plunges at 35 degrees towards the East, the tabular to massive shaped limbs have a dip of 40 degrees, a maximum down dip length of 240m and a thichkness (perpendicular to the bottom contact) of 5m -45m . The drillholes are set in fans which are parallel with the dip direction of each limb and are spaced 50m apart .  

![](../Images/get_Informal%20Classification%200.gif)

![](../Images/Tip.gif) |  The informal classification of a block model's grade estimates using quantitative methods (e.g. search volume, number of samples, estimate variance) can be used to:

  * identify areas within the project that need further information or investigation (i.e. sampling, mapping or drilling)
  * provide the basis for formal resource/reserve classification and reporting methods used in association with internationally recognized codes (e.g. the JORC Code).

  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif) |  The following additional grade estimate fields can be included in the output block model :

  * search volume number
  * number of samples
  * estimate variance

This is done in ESTIMATE by, in the Estimation Types tab, Attributes sub-tab, defining suitable field names in the Model Fields group, as shown in the image below:  
  
![](../Images/get_Informal%20Classification%201.GIF) Please see the exercise [Estimation using Drillhole Data and Advanced Options](<ESTIMATE_-_Estimation_using_Drillhole_Data.md#Exercise1>) for further details.  
---|---  
  
## Calculating a Category Field for the Block Model

  1. Select the Design window.

  2. Activate the  Data ribbon and select  Data Tools | Expressions (top level button) Select  Edit | Transform | General .

  3. In the EXTRA dialog, Files tab, Input files group, set IN* by browsing for and selecting the file _ubm5g.

  4. In the Output files group, define a new OUT* file 'ubm5cat', click OK.:  
  
![](../Images/get_Informal%20Classification%202.GIF)  

  5. In the Expression Translator dialog, define the following set of commands, using the dialog controls or the keyboard, then click Test(remember to ensure the text is exactly as below - no additional spaces, tabs or line feeds):  
  
CAT;n = 1IF(VAU > 3 and VAU <= 6) CAT = 2ELSEIF(VAU > 6) CAT = 3END  
---  
  6. If the message in the Status pane is OK, as shown below, then click Execute:  
  
![](../Images/get_Informal%20Classification%203.GIF)

  1. Select the Command control bar, check that EXTRA has finished running and that the output file contains 28924 records, as shown by the message below:  
  
![](../Images/get_Informal%20Classification%204.GIF)

## Loading the Block Model

  1. Select the Design window.

  2. Select the Project Files control bar.

  3. Drag-and-drop the following Block Models file into the 3DDesign window:

     * ubm5cat

  4. In the Sheets control bar, 3DDesign-Overlays folder, select only the following check boxes (i.e. display these objects):  

     * ubm5cat (block model)

  5. In the View Control toolbar, click Plane by One Point.

  6. Click at any point in the Design window.

  7. In the Plane By One Point dialog, select Plan , click OK.

  8. Activate the  View ribbon and click  Zoom Fit | Zoom Plan In the  View Control toolbar, click  Zoom All Data .

  9. Double-click the  ubm5cat item in the  Sheets bar and view as an  Intersection- click OK In the  Design window, check that the block model is displayed as shown below:  
  
![](../Images/get_Informal%20Classification%205.gif)![](../Images/StudioRM_ESTIMATE7.jpg)  

## Formatting The Block Model Cells

  1. Select the Design window.

  2. In the Sheets control bar, Design-Overlays folder, double-click ubm5cat (block model).

  3. In the Format Display dialog, Overlay Format group, Style tab, Display As group, select the Blocks option, click OK.

  4. In the View Control toolbar, toggle off Use Clipping.

  5. In the Sheets control bar, Design-Overlays folder, right-click ubm5cat (block model) , select Quick Legend.

  6. In the Quick Legend dialog, Object group, select the Field [CAT].

  7. In the Bins group, select Use Unique Values, click Preview.

  8. In the Legend dialog, check that your legend is as shown below, close the dialog:  
  
![](../Images/get_Informal%20Classification%206.GIF)  

  9. Back in the Quick Legend dialog, click OK.
  10. Select the Design window.

  11. Select Format | VR View | Update VR Objects 'vro'.

  12. In the Sheets control bar, 3D-Block Models folder, double-click ubm5cat(block model).

  13. In the Block Model Properties dialog, Display Type group, select the Blocks option, in the Options group, clear the Show Hull check box. Click OK

  14. The model is still colored according to values stored in the ZONE field, so right-click the ubm5catitem and selectQuick Legend, and "CAT" from theField namedrop down list and select theUse Unique Valuesoption. ClickOK.

  15. In the 3DVR window, rotate and zoom the view, check that the block model is colored according to the field CAT as shown below:  
  
![](../Images/get_Informal%20Classification%207.GIF)

  16. Identify the areas of the block model that show a low (cyan), medium (green) or high (red) kriging variance.
  17. Double click the Default Section item in the Sections folder.
  18. Click North-South, then the Clipping to Back and click OK.
  19. Using the View ribbon's Edit Interactively option, grab-hold-move the various sliders to view a dynamic cross section through the data,  

![note.gif \(1017 bytes\)](../Images/note.gif) |  The legend used to color the block model on the CAT field, can also be used as an evaluation legend.  
---|---  
  
**![](../images/UpArrow.gif)**Top of page