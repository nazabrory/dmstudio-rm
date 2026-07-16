# 2D - Search Parameters

![](../HeaderCell.jpg) |  Defining 2D Search Parameters Defining 2 dimensional sample search parameters for use in a grade estimation run.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the Datamine Table Editor to define a set of 2-dimensional (2D) sample search parameters. These will be used in a later exercise to estimate gold (Au) grades for a 2 dimensional block model.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the introductory page Search Volumes, in the Grade Estimation User Guide.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * none

## Exercise: Defining Search Parameters using the Datamine Table Editor

![](../Images/Tip.gif) |  As a starting point for defining sample search parameters:

  * Base the search ellipse axes lengths and orientations on the existing variogram model parameters for the data set i.e.
  *     * use the variogram model ranges as ellipse search distances
    * use variogram rotation angles as search ellipse rotation angles
  * Define a search volume for each grade field for each geological or mineralization zone or domain
  * Store the set of search volume parameters in a single search parameters file and define a unique search reference number (SREFNUM) for each set.

  
---|---  
  
In this exercise you are going to define a dynamic search volume as follows:

  * using an elliptical search method

  * with a first search volume based on a set of variogram model parameters

  * not using octant search

  * including a second search volume with a multiplying factor of 2.

## Creating a New Search Volume Parameter Table

The new search volume parameters file 2dspar1 will have the parameters listed in the table below:

Field (Column) |  Record (Row) |  Description  
---|---|---  
|  1 |   
SDESC (A16) |  Search Volume 1 |  Unique search volume description  
SREFNUM (N) |  1 |  Unique search volume reference number  
SMETHOD (N) |  2 |  1=Rectangular search, 2=Elliptical search  
SDIST1 (N) |  240 |  Search distance 1 [m]  
SDIST2 (N) |  100 |  Search distance 2 [m]  
SDIST3 (N) |  10 |  Search distance 3 [m]; a value of 0 cannot be used  
SANGLE1 (N) |  -10 |  1st rotation angle i.e. about SAXIS1  
SANGLE2 (N) |  0 |  2nd rotation angle i.e. about SAXIS2  
SANGLE3 (N) |  0 |  3rd rotation angle i.e. about SAXIS3  
SAXIS1 (N) |  3 |  1st rotation axis (1=X, 2=Y, 3=Z axis)  
SAXIS2 (N) |  1 |  2nd rotation axis  
SAXIS3 (N) |  3 |  3rd rotation axis  
OCTMETH (N) |  2 |  Use Octant search; 1=Yes, 2=No  
MINOCT (N) |  2 |  Number of octants to contain samples; Set if OCTMETH=1  
MINPEROC (N) |  1 |  Minimum number of samples per octant; Set if OCTMETH=1  
MAXPEROC (N) |  4 |  Maximum number of samples per octant; Set if OCTMETH=1  
MINNUM1 (N) |  3 |  Minimum total number of samples in the first search volume  
MAXNUM1 (N) |  20 |  Maximum total number of samples in the first search volume  
SVOLFAC2 (N) |  2 |  Multiplying factor defining the size of the second search volume based on size of the first search volume i.e. the SDIST1, SDIST2 and SDIST3 parameters  
MINNUM2 (N) |  3 |  Minimum total number of samples in the second search volume  
MAXNUM2 (N) |  20 |  Maximum total number of samples in the second search volume  
SVOLFAC3 |  0 |  Multiplying factor defining the size of the third search volume based on size of the first search volume i.e. the SDIST1, SDIST2 and SDIST3 parameters  
MINNUM3 (N) |  1 |  Minimum total number of samples in the third search volume  
MAXNUM3 (N) |  20 |  Maximum total number of samples in the third search volume  
MAXKEY (N) |  0 |  Maximum number of samples with same key field value  
  
  1. Select the Design window.

  2. Activate the  Home ribbon and select  Products | Table Editor Select  Tools | CAE Products | Table Editor .
  3. In the Datamine Table Editor dialog, select File | New Table | From More Definitions....

  4. In the Insert Definition dialog, select [Search Volume Standard], click OK:  
  
![](../Images/get_NewSearchParamFileUsingTableEditor%201.gif)

  5. In the Datamine Table Editor dialog, select Add | Record.

  6. Type in the values shown in the parameters table above step 1.

  7. Select File | Save.

  8. In the Save As dialog, select your project folder and define the File name '2dspar1.dm', click Save.

  9. In the Datamine Table Editor dialog, select File | Exit.

![note.gif \(1017 bytes\)](../images/note.gif) |  When defining 2D search ellipse parameters, assuming that the SDIST3 direction is perpendicular to the plane of the 2D sample set (the default), then:

  * Search distance 3 (SDIST3) is usually set to 1 or greater; a value of 0 should not be used
  * Rotation angle 1 (SANGLE1) and rotation axis 1 (SAXIS1) set to 3 i.e. the Z axis, are used to define the direction of the major search axis (other axes and rotation angle combinations can be used to obtain the same search ellipse result)
  * Rotation angle 2 (SANGLE2) and Rotation angle 3 (SANGLE3) are set to 0.

  
---|---  
  
**![](../images/UpArrow.gif)**Top of page