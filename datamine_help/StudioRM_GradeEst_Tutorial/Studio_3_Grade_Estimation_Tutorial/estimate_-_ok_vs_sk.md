![](../HeaderCell.jpg) |  Ordinary vs Simple Kriging Using ESTIMATE for Ordinary and Simple Kriging estimation.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the process ESTIMATE to estimate grades using the Ordinary and Simple Kriging methods.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the help documentation notes page for ESTIMATE, in your Help file.

  * Read the Grade Estimation User Guide page Kriging.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _2dzmod1

    * _srfsamp

    * _2depar2

    * _2dspar1

    * _2dvpar1

## Links to exercises

The following exercises are available on this page:

  * Using ESTIMATE for Ordinary and Simple Kriging

##  Using ESTIMATE for Ordinary Kriging and Simple Kriging

In this exercise you are going to estimate Au grades into a 2D block model using the Ordinary and Simple Kriging estimation methods and the following parameters:

  * Input Grade field: AU

  * Output Grade fields: AU_OK, AU_SK

  * Estimation methods: Ordinary Kriging (OK), Simple Kriging (SK)

  * Search Volume: search volume 1 (SREFNUM=1)

  * Variogram model: variogram model 2 (VREFNUM=2)

  * Estimation options: zonal control (field ANOM), values 1 and 2

  * Simple Kriging Method: 2 (LOCALMNP=2) i.e. the local mean is calculated automatically.

This will be done by adding two Simple Kriging runs (one for each of the zones i.e. ANOM=1 and ANOM=2) to the existing estimation parameter file _2depar2 . The modified estimation estimation parameter file will then be saved out to a new file 2depar3.

![note.gif \(1017 bytes\)](../images/note.gif) |  Ordinary vs Simple Kriging For Ordinary Kriging (OK) a weight is calculated for each sample, and the sum of these weights is 1. For Simple Kriging(SK) a weight Wi is calculated for each sample and a weight of ( 1 - ΣWi ) is assigned to the mean grade. Simple Kriging is not as responsive as Ordinary Kringing to local trends in the data, since it depends partially on the mean grade, which is assumed to be known, and constant throughout the area.  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif) |  The local mean value required by Simple Kriging can be defined in one of the following two ways:

  * The local mean is obtained from a 'local mean' field in the input block model
  *     * Set estimation parameter LOCALMNP = 1
    * Define the name of the local mean field in the block model using the estimation parameter LOCALM_F
  * The local mean is calculated as the arithmetic mean of all samples lying in the search volume
  *     * Set estimation parameter LOCALMNP = 2.

  
---|---  
  
The input block model and sample points are shown in the image below. The blue block model cells represent the lower grade zone (field ANOM=1) while the red cells represent the higher grade zone (field ANOM=2). The displayed sample points have low grade values colored blue and higher grade values colored in red.  

![](../Images/get_ESTIMATE%20OKvsSK%201.gif)

![](../Images/Tip.gif) |  Use Simple Kriging when:

  * requiring the local mean to play a role in the grade estimate
  * wanting to reduce the effects of clustered data
  * wanting to produce a result that is "smoother" and more aesthetically pleasing.

  
---|---  
  
## Defining the Input Block Model and Sample Files

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Interpolate Select  Models | Interpolation Processes | Interpolate Grades from Menu .

  3. In the Grade Estimation (ESTIMATE) dialog, Files tab, select the Input subtab.

  4. In the Geological Model group, click Browse.

  5. In the Project Browser dialog, Database Tables pane, Block Models folder, select _2dzmod1 , click OK.

  6. In the Sample Data group, click Browse.

  7. In the Project Browser dialog, Database Tables pane, All Tables folder, select _srfsamp , click OK.

  8. In the Coordinates Fields group, select the X, Y and Z fields [XPT], [YPT], [ZPT].

  9. In the Zone Control Fields group, select the Zone 1 field [ANOM].

  10. Check that your parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%202.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * Drillholes or suitable points data can be used as Sample Data files. 
     * Both the Input Model and the Sample File need to be defined so that the Zone Control Fields can be selected.
     * The Zone Control Fields need to be present (and contain suitable matching zone field values) in both the Input Model and the Sample File.  
---|---  

## Defining the Output Block Model, Input/Output Search Volume and Variogram Model Files

  1. In the Grade Estimation (ESTIMATE) dialog, Files tab, select the Output subtab.

  2. In the Grade Model group, define a new model '2dgmod3'.

  3. In the Parameter Files (Input and Output) group, clear the Use Defaults checkbox.

  4. Browse for and set the Search Volume File to _2dspar1.

  5. Browse for and set the Estimation Parameter File to _2depar2.

  6. Browse for and set the Variogram Model File to _2dvpar1.

  7. Check that your parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%203.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  The Search Volume File, Variogram Model File and the Estimation Parameter File need to be defined here so that the relevant search, variogram model and estimation parameters are displayed in the different tabs.  
---|---  

## Checking the Search Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Files tab, click Next >>.

  2. In the Search Volumes tab, Summary subtab, check that the Search Parameter Table contains a single sets of parameters, as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%204.gif)

## Checking the Variogram Model Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Search Volumes tab, click Next >>.

  2. In the Variogram Models tab, Summary subtab, check that the Variogram Model Table contains two sets of parameters, as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%205.gif)  
![](../Images/get_ESTIMATE%20OKvsSK%205b.gif)

## Adding the Simple Kriging Runs in the Estimation Types Tab

  1. In the Grade Estimation (ESTIMATE) dialog, Variogram Models tab, click Next >>.

  2. In the Estimation Types tab, Index group, check that 6 sets of estimation parameters are listed in the Index pane.  
  
![](../Images/get_ESTIMATE%20OKvsSK%205a.gif)  

  3. In the Index group, click Add.

  4. In the estimation parameter list, check that a new estimation parameter description '7: Estima Param 7' has been added.

  5. In the Attributes subtab on the right, define the parameters as shown below for ANOM=1:  
  
![](../Images/get_ESTIMATE%20OKvsSK%206.gif)  

  6. In the Options subtab, define the parameters as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%207.gif)  

  7. In the Indicator Estimation subtab, check that all options are greyed out.

  8. Repeat steps 3 to 7 , defining the parameters for the zone field, second zone i.e. ANOM=2.

  9. In the Summary subtab, check that your additional parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%208.gif)  
![](../Images/get_ESTIMATE%20OKvsSK%209.gif)  
![](../Images/get_ESTIMATE%20OKvsSK%209b.gif)

## Exporting the New Estimation Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Estimation Types tab, Index group, click Export.

  2. In the Project Browser dialog, define a new Filename '2depar3', click OK.

## Setting the Controls Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Estimation Types tab, click Next >>.

  2. In the Controls tab, Parameters subtab, check that the default parameters are selected, as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%2010.gif)  
  

![note.gif \(1017 bytes\)](../images/note.gif) |  The input block model contains only parent cells and not subcells: this can be identified by all the cells having the same size in the image shown at the top of the page. In this case, the default subcells estimation option is selected; selecting the Parent cell estimation using a full 3D matrix of points option will produce the same results. These two options will produce different estimation results when selected using a block model with subcells.  
---|---  

## Previewing and Running the Estimate

  1. In the Grade Estimation (ESTIMATE) dialog, Controls tab, click Next >>.

  2. In the Preview tab, Summary subtab, check that the Files group parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%2011.gif)  

  3. In the Preview tab, Summary subtab, check that the Fields group parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%2012.gif)  

  4. In the Preview tab, Summary subtab, check that the Parameters group settings are as shown below:  
  
![](../Images/get_ESTIMATE%20OKvsSK%2013.gif)   
![](../Images/get_ESTIMATE%20OKvsSK%2013b.gif)  

  5. Click Run.

  6. In the Command control bar, check that ESTIMATE has run successfully with the additional Simple Kriging runs and that the output file 2dgmod3 contains 780 records:  
  
![](../Images/get_ESTIMATE%20OKvsSK%2014.gif)

**![](../images/UpArrow.gif)**Top of page