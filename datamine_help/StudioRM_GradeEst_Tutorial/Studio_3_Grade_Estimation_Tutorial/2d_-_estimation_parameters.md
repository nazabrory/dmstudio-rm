# 2D - Estimation Parameters

![](../HeaderCell.jpg) |  Defining 2D Estimation Parameters Defining 2 dimensional estimation parameters for use in a grade estimation run.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the Datamine Table Editor to define two sets of estimation parameters. This set of parameters will be stored in a parameter file and will make use of the previously defined search parameter and variogram parameter files.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the introductory page Grade Estimation Parameter File, in the Grade Estimation User Guide.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * none

## Exercise: Defining Estimation Parameters using the Datamine Table Editor

In this exercise you are going to define three sets of estimation parameters for the 'Au' grade field:

  * a Nearest Neighbour (NN) run, an Inverse Power Distance (IPD) run and an Ordinary Kriging (OK) run

  * output grade fields AU_NN, AU_IPD and AU_OK respectively

  * using no zonal control

  * using the search volume to control anisotropy.

Use the search parameters and first variogram parameter set (i.e. VREFNUM = 1) from the previous three exercises.

![](../Images/Tip.gif) |  Add a description field to your estimation parameter file:

  * Use Datamine Table Editor to add a field to the parameter file, name it e.g. DESCRIP(A24))
  * Briefly describe each estimation parameter set in the estimation parameter file
  * The addition of this description field makes it easier to distinguish between different grade estimation runs when dealing with multiple grade fields and/or zones or when comparing different grade estimation runs for a single grade field. 

  
---|---  
  
## Creating a New Estimation Parameter Table

Create a new estimation parameters file 2depar1 with the three grade runs for 'Au'. The estimation parameters are listed in the table below:

Field (Column) |  Record (Row) |  |  |  Description  
---|---|---|---|---  
|  1 |  2 |  3 |   
EDESC (A16) |  AU - NN Method |  AU - IPD Method |  AU - OK Method |  Estimation Parameter Set Description  
VALUE_IN (A8) |  AU |  AU |  AU |  Input grade field  
VALUE_OU (A8) |  AU_NN |  AU_IPD |  AU_OK |  Output grade field names;a different name is required for each run  
NUMSAM_F (A8) |  - |  - |  - |  Output field to contain number of samples used (optional)  
SVOL_F (A8) |  - |  - |  - |  Output field to contain search volume number (optional)  
VAR_F (A8) |  VAR_NN |  VAR_IPD |  VAR_OK |  Output field to contain estimation variance (optional)  
MINDIS_F (A8) |  - |  - |  - |  Output field to contain transformed distance to nearest sample (optional)  
SREFNUM (N) |  1 |  1 |  1 |  Search volume reference number (in this exercise, both runs use the same set of search parameters)  
IMETHOD (N) |  1 |  2 |  3 |  Estimation method: 1=NN, 2=IPD, 3=OK, 4=SK, 5=ST  
POWER (N) |  2 |  2 |  2 |  Power of distance for IPD weighting  
ADDCON (N) |  0 |  0 |  0 |  IPD - constant added to distance ST - additive constant for lognormal  
VREFNUM (N) |  0 |  0 |  1 |  Variogram reference number (only applicable if IMETHOD=3,4)  
KRIGNEGW (N) |  0 |  0 |  0 |  Treatment of negative kriging weights: 0=keep & use, 1=ignore -ve weighted samples  
KRIGVARS (N) |  0 |  0 |  1 |  Treatment of negative kriging variance >sill: 0=keep KV>sill, 1=set KV equal to sill (only applicable if LOG=0)  
  
  1. Select the Design window.

  2. Activate the  Home ribbon and select  Products | Table Editor Select  Tools | CAE Products | Table Editor .
  3. In the Datamine Table Editor dialog, select File | New Table | From More Definitions....

  4. In the Insert Definition dialog, select [Estimation Parameters - Standard] and click OK.

  5. In the Datamine Table Editor dialog, click Add Column.

  6. In the Add Column dialog, define a new field Name: 'KRIGVARS' using the parameters shown below, click OK:  
  
![](../Images/get_NewEstimationParamFileUsingTableEditor%201.gif)  

  7. In the Datamine Table Editor dialog, select Add | Record (x3).

  8. Type in the values shown in the parameters table above step 1.

  9. Select File | Save As....

  10. In the Save As dialog, select your project folder and define the File name '2depar1.dm', click Save.

  11. Select File | Exit.

![note.gif \(1017 bytes\)](../images/note.gif) |  When defining estimation parameters in an estimation parameter file:

  * define a search parameter file
  * define a variogram model file if kriging estimation methods are used
  * give these set of parameter files a project prefix in their filenames so that they can easily be recognised as belonging to the same set.

  
---|---  
  
**![](../images/UpArrow.gif)**Top of page