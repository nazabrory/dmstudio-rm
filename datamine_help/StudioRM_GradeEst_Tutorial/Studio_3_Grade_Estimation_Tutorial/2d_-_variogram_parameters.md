# 2D - Variogram Parameters

![](../HeaderCell.jpg) |  Defining 2D Variogram Model Parameters Defining 2 dimensional variogram model parameters for use in a grade estimation run.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the DatamineTable Editor to define two sets of 2-dimensional (2D) variogram model parameters. These will be used in a later exercise to estimate gold (Au) grades for a 2 dimensional block model.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the introductory page Variogram Models, in the Grade Estimation User Guide.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * none

## Exercise: Defining Variogram Model Parameters using the Datamine Table Editor

![note.gif \(1017 bytes\)](../images/note.gif) |  When modeling experimental variograms using the process VARFIT, the resultant models are saved to a variogram model file using the standard Studio variogram model conventions. If you have modeled experimental variograms using a different program, make sure that you use the correct transformations when converting the external modeling program's model results into Studio's variogram model parameter format. As an example, check the conversions to the following Studio variogram parameters:

  * Variogram axes and angles of rotation
  * Nugget, Spatial Variance (i.e. Sill - Nugget) and Sill.

  
---|---  
  
## Creating a New Variogram Model Parameter Table

Define a new variogram model parameters file 2dvpar1 with two variogram models, the first a single structure spherical model and the second a two structure spherical model, using the following standard Studio variogram model parameters:

Field (Column) |  Record (Row) |  |  Description/Comments  
---|---|---|---  
|  1 |  2 |   
VDESC |  AU 1-structure |  AU 2-structure |  Unique variogram description  
VREFNUM |  1 |  2 |  Unique variogram reference number  
VANGLE1 |  -10 |  -10 |  Rotation angle 1, defining orientation of range  
VANGLE2 |  0 |  0 |  Rotation angle 2, defining orientation of range  
VANGLE3 |  0 |  0 |  Rotation angle 3, defining orientation of range  
VAXIS1 |  3 |  3 |  First rotation axis (1=X axis, 2=Y axis, 3=Z axis)  
VAXIS2 |  1 |  1 |  Second rotation axis (1=X axis, 2=Y axis, 3=Z axis)  
VAXIS3 |  3 |  3 |  Third rotation axis (1=X axis, 2=Y axis, 3=Z axis)  
NUGGET |  0 |  0 |  Nugget variance (Co)  
ST1 |  1 |  1 |  Variogram model type for structure 1 (1=spherical, 2=power, 3=exponential, 4=gaussian, 5=De Wijsian)  
ST1PAR1 |  240 |  40 |  Structure 1, parameter 1 (Range in X direction for spherical model)  
ST1PAR2 |  80 |  40 |  Structure 1, parameter 2 (Range in Y direction for spherical model)  
ST1PAR3 |  80 |  80 |  Structure 1, parameter 3 (Range in Z direction for spherical model)  
ST1PAR4 |  90000 |  30000 |  Structure 1, parameter 4 (Spatial variance for spherical model - C value)  
ST2 |  0 |  1 |  Variogram model type for structure 1 (1=spherical, 2=power, 3=exponential, 4=gaussian, 5=De Wijsian)  
ST2PAR1 |  0 |  240 |  Structure 2, parameter 1 (Range in X direction for spherical model)  
ST2PAR2 |  0 |  100 |  Structure 2, parameter 2 (Range in Y direction for spherical model)  
ST2PAR3 |  0 |  80 |  Structure 2, parameter 3 (Range in Z direction for spherical model)  
ST2PAR4 |  |  60000 |  Structure 2, parameter 4 (Spatial variance for spherical model - C value)  
  
  1. Select the Design window.

  2. Activate the  Home ribbon and select  Products | Table Editor Select  Tools | CAE Products | Table Editor .
  3. In the Datamine Table Editor dialog, select File | New Table | Variogram-Model.

  4. Click in the column header of field ST3 (N), drag the horizontal slider bar all the way to the right, <Shift>+Click in the column header of field ST9PAR4 (N) , click Delete Column.

  5. In the Datamine Table Editor dialog, select Tools | Definition Editor....

  6. In the Definition Editor dialog, Columns group, check that the table now only contains the 19 fields shown below, click Close:  
  
![](../Images/get_NewVariogramModelParamFileUsingTableEditor%201.gif)  

  7. In the Datamine Table Editor dialog, select Add | Record (x2).

  8. Type in the two sets of variogram model parameters shown in the table above step 1.  

![note.gif \(1017 bytes\)](../images/note.gif) |  When defining 2D variogram model parameters, assuming that the Z axis direction is perpendicular to the plane of the 2D sample set (the default), then:
     * Rotation angle 1 (VANGLE1) and rotation axis 1 (SAXIS1) set to 3 i.e. the Z axis, are used to define the direction of the major search axis (other axes and rotation angle combinations can be used to obtain the same search ellipse result)
     * Rotation angle 2 (VANGLE2) and Rotation angle 3 (VANGLE3) are both set to 0.
     * Parameter 3 i.e. the Range in the Z direction for spherical model (ST1PAR3), is usually set to an arbitrary value greater than 0.  
---|---  
  9. Select File | Save As....

  10. In the Save As dialog, select your project folder and define the File name '2dvpar1.dm', click Save.

  11. Select File | Exit.

**![](../images/UpArrow.gif)**Top of page