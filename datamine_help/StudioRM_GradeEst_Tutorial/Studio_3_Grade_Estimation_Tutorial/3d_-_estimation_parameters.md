![](../HeaderCell.jpg) |  Defining 3D Estimation Parameters Using ESTIMATE to defining 3-dimensional estimation parameters.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the process ESTIMATE to define and export two sets of estimation parameters. These parameters will be exported to a parameter file and will make use of the previously defined 3D search and variogram parameter files.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the introductory page Grade Estimation Parameter File, in the Grade Estimation User Guide.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     1.        * _ubmz

       * _udhz

       * _ueps

       * _uepv

## Exercise: Defining and Exporting Estimation Parameters Using ESTIMATE

In this exercise you are going to define two sets of estimation parameters i.e. one set for each of the Cu and Ag grades for zone 1 and use:

  * zonal control and restrict estimation of the two grades into zone 1 only i.e. ZONE=1.

  * the search volume to control anisotropy.

  * search volume 1 (SREFNUM=1) for the zone 1 estimates

  * ordinary kriging

  * Cu and Ag estimates to use variogram models 1 and 2 (VREFNUM=1, 2) respectively.

The estimation parameters for this exercise are listed in the table below:

Field (Column) |  Record (Row) |  |  Description/Comments  
---|---|---|---  
|  1 |  2 |   
EDESC |  Estima Param 1 |  Estima Param 2 |  Estimation run description  
EREFNUM |  1 |  2 |  Estimation run reference number  
VALUE_IN |  CU |  AG |  Input grade field  
VALUE_OU |  CU |  AG |  Output grade field names  
SREFNUM |  1 |  1 |  Search volume reference number (in this exercise, both runs use the same set of search parameters)  
ZONE * |  1 |  1 |  First field controlling estimation by zone  
[ZONE2_F] * |  0 |  0 |  Second field controlling estimation by zone  
NUMSAM_F ** |  NCU |  NAG |  Output field to contain number of samples used (optional)  
SVOL_F ** |  SCU |  SAG |  Output field to contain search volume number (optional)  
VAR_F ** |  VCU |  VAG |  Output field to contain estimation variance (optional)  
MINDIS_F ** |  |  |  Output field to contain transformed distance to nearest sample  
IMETHOD |  3 |  3 |  Estimation method: 1=NN, 2=IPD, 3=OK, 4=SK, 5=ST  
ANISO * |  1 |  1 |  Anisotropy method: 1=search volume, 2=use ANANGLE  
ANANGLE1 * |  0 |  0 |  Anisotropy angle 1 (only applicable if IMETHOD=1,2.)  
ANANGLE1 * |  0 |  0 |  Anisotropy angle 2 (only applicable if IMETHOD=1,2.)  
ANANGLE1 * |  0 |  0 |  Anisotropy angle 3 (only applicable if IMETHOD=1,2.)  
ANDIST1 * |  1 |  1 |  Anisotropy distance 1  
ANDIST2 * |  1 |  1 |  Anisotropy distance 2  
ANDIST3 * |  1 |  1 |  Anisotropy distance 3  
POWER |  2 |  2 |  Power of distance for IPD weighting  
ADDCON |  0 |  0 |  IPD - constant added to distance ST - additive constant for lognormal  
VREFNUM |  1 |  2 |  Variogram reference number (only applicable if IMETHOD=3,4)  
LOG |  0 |  0 |  Lognormal kriging flag: 0=Linear Kriging, 1=Lognormal Kriging  
MKNUG_F * |  |  |   
GENCASE |  0 |  0 |  Lognormal kriging flag: 0=Rendu, 1=General Case (only applicable if LOG=1)  
DEPMEAN |  0 |  0 |  Mean for lognormal variance calculation (only applicable if LOG=1)  
TOL |  0.010 |  0.010 |  Convergence tolerance for lognormal kriging (only applicable if GENCASE=1)  
MAXITER |  3 |  3 |  Maximum iterations for log kriging (only applicable if GENCASE=1)  
KRIGNEGW |  0 |  0 |  Treatment of negative kriging weights: 0=keep & use, 1=ignore -ve weighted samples  
KRIGVARS |  1 |  1 |  Treatment of negative kriging variance >sill: 0=keep KV>sill, 1=set KV equal to sill (only applicable if LOG=0)  
LOCALMNP |  2 |  2 |  Method for calculation of local mean: 1=field from &PROTO, 2 = calculate mean (only applicable if IMETHOD=4)  
LOCALM_F |  |  |  Name of local mean field in the input block model file (only applicable if IMETHOD=4)  
CUTOFF * |  |  |  Indicator Kriging parameter  
BINGRADE * |  |  |  Indicator Kriging parameter  
ABVGRADE * |  |  |  Indicator Kriging parameter  
  
Table Notes:

* Advanced option fields.

** Optional data fields added to the output model file.

##  Defining the Input Block Model and Samples Files

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Estimate | Interpolate Select  Models | Interpolation Processes | Interpolate Grades from Menu .

  3. In the Grade Estimation (ESTIMATE) dialog, Files tab, select the Input sub-tab.

  4. In the Geological Model group, click Browse.

  5. In the Project Browser dialog, Database Tables pane, Block Models folder, select _ubmz , click OK.

  6. In the Sample Data group, click Browse.

  7. In the Project Browser dialog, Database Tables pane, Drillholes folder, select _udhz , click OK.

  8. In the Coordinates Fields group, use the default X, Y,and Z values.

  9. In the Zone Control Fields group, select [ZONE] for Zone 1.

  10. Check that your parameters are as shown below:  
  
![](../Images/get_NewEstimationParamFileUsingESTIMATE%201.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * Both the Input Model and the Sample File need to be defined so that the Zone Control Fields can be selected.
     * The Zone Control Fields need to be present (and contain suitable matching zone field values) in both the Input Model and the Sample File.  
---|---  

## Defining The Input/Output Search Volume and Variogram Model Files

  1. In the Grade Estimation (ESTIMATE) dialog, Files tab, select the Output sub-tab.

  2. In the Parameter Files (Input and Output) group, clear the Use Defaults check box.

  3. Browse for and select the Search Volume File _ueps.

  4. Define a new Estimation Parameter File '3depar1'.

  5. Browse for and select the Variogram Model File_uepv.

  6. Check that your parameters are as shown below:  
  
![](../Images/get_NewEstimationParamFileUsingESTIMATE%202.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * Both the Search Volume File and the Variogram Model File need to be defined here so that the correct search and variogram reference numbers can be selected in the Estimation Types tab.  
---|---  

## Defining the Estimation Types

  1. In the Grade Estimation (ESTIMATE) dialog, Files tab, click Nexttwice.

  2. In the Search Volumes tab, browse for and import the file _ueps.dm, then check that 3 search volumes are listed in the Index pane, click Next .

  3. In the Variogram Models tab, check that 12 variogram models are listed in the Index pane, click Next >>.

  4. In the Estimation Types tab, Index group, click Add.

  5. In the estimation parameter list, check that a new estimation parameter description '1: Estima Param 1' has been added.

  6. In the Attributes sub-tab on the right, referring to the table of estimation parameters at the start of this exercise, define the settings shown below:  
  
![](../Images/get_NewEstimationParamFileUsingESTIMATE%203.gif)

  7. In the Options sub-tab, check that the Reset Negative Kriging Weightsto Zero option is unchecked..

  8. In the Indicator Estimation sub-tab, check that all options are greyed out.

  9. Repeat steps 3 to 7 ,referring to the table of parameters at the start of this exercise, define the parameters for the Ag grade field.

  10. In the Attributes subtab, check that your settings are as shown below:  
  
  
![](../Images/get_NewEstimationParamFileUsingESTIMATE%204.gif)

  11. In the Summary subtab, check that your parameters are as shown below:  
  
![](../Images/get_NewEstimationParamFileUsingESTIMATE%205.gif)  
![](../Images/get_NewEstimationParamFileUsingESTIMATE%206.gif)

## Exporting the Estimation Parameters to File

  1. In the Grade Estimation (ESTIMATE) dialog, Estimation Types tab, Index group, click Export.

  2. In the Project Browser dialog, define a Filename of '3depar1', click OK.
  3. In the Grade Estimation (ESTIMATE) dialog, click Cancel to exit the ESTIMATE dialog.  

**![](../images/UpArrow.gif)**Top of page