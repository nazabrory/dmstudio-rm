# 3D - Search Parameters

![](../HeaderCell.jpg) |  Defining 3D Search Parameters Defining 3-dimensional sample search parameters for use in a grade estimation run.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the process ESTIMATE to define and export a set of 3D sample search parameters.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the introductory page Search Volumes, in the Grade Estimation User Guide.

  * [Files](<tutorial_files.md>)required for the exercises on this page:

  *     * none

## Exercise: Defining and Exporting Search Parameters Using ESTIMATE

In this exercise you are going to define three dynamic search volumes with the following general characteristics:

  * using an elliptical search method

  * using a first search volume based on a set of variogram model parameters

  * not using octant search

  * using a second search volume with a multiplying factor of 2

![](../Images/Tip.gif) |  As a starting point for defining sample search parameters:

  * Base the search ellipse axes lengths and orientations on the existing variogram model parameters for the data set i.e.
  *     * use the variogram model ranges as ellipse search distances
    * use variogram rotation angles as search ellipse rotation angles
  * As a minimum, define a search volume for each grade field for each geological zone

  
---|---  
  
The search volume parameters are listed in the table below:

Field (Column) |  Record (Row) |  |  |  Description  
---|---|---|---|---  
|  1 |  2 |  3 |   
SDESC |  Search Volume 1 |  Search Volume 2 |  Search Volume 3 |  Unique search volume description  
SREFNUM |  1 |  2 |  3 |  Unique search volume reference number  
SMETHOD |  2 |  2 |  2 |  1=Rectangular search, 2=Elliptical search  
SDIST1 |  150 |  120 |  60 |  Search distance 1 [m]  
SDIST2 |  90 |  115 |  50 |  Search distance 2 [m]  
SDIST3 |  30 |  15 |  15 |  Search distance 3 [m]; a value of 0 cannot be used  
SANGLE1 |  123 |  45 |  123 |  1st rotation angle i.e. about SAXIS1  
SANGLE2 |  42 |  40 |  42 |  2nd rotation angle i.e. about SAXIS2  
SANGLE3 |  0 |  0 |  0 |  3rd rotation angle i.e. about SAXIS3  
SAXIS1 |  3 |  3 |  3 |  1st rotation axis (1=X, 2=Y, 3=Z axis)  
SAXIS2 |  1 |  1 |  1 |  2nd rotation axis  
SAXIS3 |  3 |  3 |  3 |  3rd rotation axis  
MINNUM1 |  5 |  1 |  1 |  Minimum total number of samples in the first search volume  
MAXNUM1 |  20 |  20 |  20 |  Maximum total number of samples in the first search volume  
SVOLFAC2 |  2 |  2 |  2 |  Multiplying factor defining the size of the second search volume based on size of the first search volume i.e. the SDIST1, SDIST2 and SDIST3 parameters  
MINNUM2 |  5 |  1 |  1 |  Minimum total number of samples in the second search volume  
MAXNUM2 |  20 |  20 |  20 |  Maximum total number of samples in the second search volume  
SVOLFAC3 |  0 |  0 |  0 |  Multiplying factor defining the size of the third search volume based on size of the first search volume i.e. the SDIST1, SDIST2 and SDIST3 parameters  
MINNUM3 |  1 |  1 |  1 |  Minimum total number of samples in the third search volume  
MAXNUM3 |  20 |  20 |  20 |  Maximum total number of samples in the third search volume  
OCTMETH |  0 |  0 |  0 |  Use Octant search; 1=Yes, 2=No  
MINOCT |  2 |  2 |  2 |  Number of octants to contain samples; Set if OCTMETH=1  
MINPEROC |  1 |  1 |  1 |  Minimum number of samples per octant; Set if OCTMETH=1  
MAXPEROC |  4 |  4 |  4 |  Maximum number of samples per octant; Set if OCTMETH=1  
MAXKEY |  0 |  0 |  0 |  Maximum number of samples with same key field value  
  
## Defining a Set of Search Parameters using ESTIMATE

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Estimate | Interpolate Select  Models | Interpolation Processes | Interpolate Grades from Menu .

  3. In the Grade Estimation (ESTIMATE) dialog, Files tab, click Next

  4. .In the Grade Estimation (ESTIMATE) dialog, Unfolding tab, click Next

  5. In the Search Volumes tab, Index group, click Add.

  6. In the search volume list, check that a new search volume 'Search Volume 1' has been added.

  7. In the Shape sub-tab on the right, referring to the table of parameters at the start of the exercise, define the parameters as shown below:  
  
![](../Images/get_NewSearchParamFileUsingESTIMATE%201.gif)  

  8. In the Category sub-tab, referring to the table of parameters at the start of the exercise, define the parameters as shown below:  
  
![](../Images/get_NewSearchParamFileUsingESTIMATE%202.gif)

  9. In the Decluster sub-tab, Octants group, make sure that Use Octants option is cleared:  
  
![](../Images/get_NewSearchParamFileUsingESTIMATE%203.gif)

  10. Repeat steps 5 to 8 for the second and third sets of search parameters, using the values listed in the second and third rows of the table at the start of the exercise.

  11. In the Summary sub-tab, referring to the table of parameters at the start of the exercise, check that the three sets of parameters are as shown below:  
  
![](../Images/get_NewSearchParamFileUsingESTIMATE%204.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  When defining 3D search ellipsoid parameters,
     * the SDIST1, SDIST2 and SDIST3 parameters need to be set
     * the search ellipsoid typically has a dip direction and a dip defined by rotations about two axes:
     *        * First rotation SANGLE1 about SAXIS1 (typically = 3 i.e. axis Z)
       * Second rotation SANGLE2 about SAXIS2 (typically = 1 i.e. axis X)
     * a 3D search ellipsoid may require a third rotation SANGLE3 about another axis.
     * define axes and rotations as dip direction, dip, cross dip.  
---|---  

![](../Images/Tip.gif) |  When defining search ellipsoid axes and rotations:

  * use SDIST1, SANGLE1 about SAXIS1 (=3) to define the Dip Direction/Plunge axis
  * use SDIST2, SANGLE2 about SAXIS2 (=2) to define the Strike axis
  * if required, then use SDIST3, SANGLE3 about SAXIS3 to define the rotation for a more complex orientation
  * Note: this convention has not been used in the above exercise.

  
---|---  
  
## Exporting the Search Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Search Volumes tab, Index group, click Export.

  2. In the Project Browser dialog, select your project folder and define the Filename '3dspar1', click OK.
  3. In the Grade Estimation (ESTIMATE) dialog, click Cancel. 

**![](../images/UpArrow.gif)**Top of page