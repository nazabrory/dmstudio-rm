# ESTIMATE - Estimation using Drillhole Data

![](../HeaderCell.jpg) |  Estimation using Drillhole Data and Advanced Options Using drillhole data and ESTIMATE for grade estimation.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the process ESTIMATE to estimate grades into a 3D block model using drillhole data and the two different estimation methods.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the help documentation notes page for ESTIMATE in your Help file.

  * Read the Grade Estimation User Guide page on Kriging.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _ubm5z

    * _udhz

    * _ueps

    * _uepv

    * _uepe

## Estimation Using ESTIMATE, Drillhole Data and Advanced Options

In this exercise you are going to estimate a variety of grades (and Density) into a 3D block model using drillhole sample data and parameters, as listed below:

  * Input block model: 5m regular celled (no sub-cells), zone flagged, block model

  * Sample data file: drillholes

  * Input Grade fields: AU (g/t), CU (%), AG (g/t), CO (%)

  * Output Grade fields: same as input field names

  * Estimation methods: Inverse Power Distance, Ordinary Kriging (OK)

  * Search Volumes: one for each of the three mineralization zones (see parameter file)

  * Variogram models: one for each of the 4 grades for each of the three mineralization zones (see parameter file)

  * Estimation options:

  *     * zonal control (field ZONE), values 1, 2 and 3

    * set negative kriging weights to zero.

This will be done by using the existing Search, Variogram and Estimation parameter files _ueps,_uepv and _uepe respectively.

The input 3D block model and drillhole samples are shown in the image below:  

![](../Images/get_ESTIMATE%20DH%201.gif)   

![note.gif \(1017 bytes\)](../images/note.gif) |  In the above image, the block model cells are colored according to three separate mineralization zones (cyan: ZONE=1, green: ZONE=2, red: ZONE=3). The fold axis of the ore body plunges at 35 degrees towards the east, the tabular to massive shaped limbs have a dip of 40 degrees, a maximum down dip length of 240m and a thichkness (perpendicular to the bottom contact) of between 5 and 45m . The drillholes are set in fans which are parallel with the dip direction of each limb and are spaced approximately 50m apart.  
---|---  
  
![](../Images/Tip.gif) |  Use Drillhole sample data when:

  * estimating grades into a 3D block model
  * estimating grades into a pseudo 3D block model i.e. Z coordinate has been set to a constant reference elevation e.g. flat dipping tabular ore bodies
  * using sample length as a weighting factor for estimation.

  
---|---  
  
## Defining the Input Block Model and Sample Files

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Interpolate Select  Models | Interpolation Processes | Interpolate Grades from Menu .

  3. In the Grade Estimation (ESTIMATE) dialog, Files tab, select the Input subtab.

  4. In the Geological Model group, click Browse.

  5. In the Project Browser dialog, Database Tables pane, Block Models folder, select _ubm5z, click OK.

  6. In the Sample Data group, click Browse.

  7. In the Project Browser dialog, Database Tables pane, All Tables folder, select _udhz , click OK.

  8. In the Coordinates Fields group, select the X, Y and Z fields [X], [Y], [Z] (defaults).

  9. In the Zone Control Fields group, select the Zone 1 field [ZONE].

  10. Check that your parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20DH%202.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * Drillholes or suitable points data can be used as Sample Data files. 
     * Both the Input Model and the Sample File need to be browsed and selected so that the Zone Control Fields can be selected.
     * The Zone Control Fields need to be present (and contain suitable matching zone field values) in both the Input Model and the Sample File.  
---|---  

## Defining the Output Block Model, Input/Output Search Volume and Variogram Model Files

  1. In the Grade Estimation (ESTIMATE) dialog, Files tab, select the Output subtab.

  2. In the Grade Model group, define a new model filename '3dbm5g'.

  3. In the Parameter Files (Input and Output) group, clear the Use Defaults check box.

  4. Browse for and select the Search Volume File_ueps.

  5. Browse for and select the Estimation Parameter File_uepe.

  6. Browse for and select the Variogram Model File_uepv.

  7. Check that your parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20DH%203.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  The Search Volume File, Variogram Model File and the Estimation Parameter File need to be defined here so that the relevant search, variogram model and estimation parameters are displayed in the different tabs.  
---|---  

## Checking the Search Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Files tab, click Next >>.

  2. In the Search Volumes tab, Summary subtab, check that the Search Parameter Table contains three sets of parameters, as shown below:  
  
![](../Images/get_ESTIMATE%20DH%204.GIF)  
![](../Images/get_ESTIMATE%20DH%204b.GIF)  

![note.gif \(1017 bytes\)](../images/note.gif) |  In this example, the search parameter file contains three sets of search parameters, one for each mineralized zone. The orientation of the axes and the ranges of the AU grade variograms were used to determine the search volume parameters for all grade fields. Typically each grade field for each zone has a different set of search parameters.  
---|---  

## Checking the Variogram Model Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Search Volumes tab, click Next >>.

  2. In the Variogram Models tab, Summary subtab, check that the Variogram Model Table contains twelve sets of parameters. The first five are shown below:  
  
![](../Images/get_ESTIMATE%20DH%205.GIF)  

![note.gif \(1017 bytes\)](../images/note.gif) |  For the twelve sets of variogram model parameters:
     * each model consists of two spherical structures (i.e. ST1* and ST2* parameters are set)
     * models 1-3 and 5-8 are anisotropic
     * models 4 and 9-12 are isotropic.  
---|---  
  

## Checking the Estimation Types arameters

  1. In the Grade Estimation (ESTIMATE) dialog, Variogram Models tab, click Next >>.

  2. In the Estimation Types tab, Index group, check that 15 sets of estimation parameters are listed.

  3. In the estimation parameter list, select the first item [1:CU ZONE 1].

  4. In the Attributes subtab on the right, check that the parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20DH%206.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  Note the following parameters:
     * additional output model fields NCU, VCU and SCU, used to record, for each block model cell, the number of samples, estimation variance and search volume respectively used in the grade estimate for the cell (the other grade fields have corresponding field names)
     * this set of estimation parameters is for the CU grade field of ZONE = 1 and uses search volume number 1 as well as variogram model number 1  
---|---  
  5. In the Options subtab, check that the parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20DH%207.gif)

![note.gif \(1017 bytes\)](../images/note.gif) |  Resetting negative kriging weights to zero prevents the calculation of negative grade estimates.  
---|---  
  6. In the Indicator Estimation subtab, check that all options are greyed out.

  7. In the Summary subtab, check that 15 sets of parameters are listed. The first five are shown below:  
  
![](../Images/get_ESTIMATE%20DH%208.gif)

## Running the Estimation From the Preview Tab

  1. In the Grade Estimation (ESTIMATE) dialog, Estimation Types tab, click Next >>.

  2. In the Controls tab, click Next >>.

  3. In the Preview tab, Summary subtab, check your parameters.

  4. Click Run.

![note.gif \(1017 bytes\)](../images/note.gif) |  The progress report (percentage completion) and summary results of the estimation calculations are output to the Command control bar, and may take several minutes to complete.  
---|---  
  5. In the Command control bar, Summary Statistics section of the report at the bottom of the page, check that the grade estimation process has run successfully and that the output file 3dbm5g contains 28,924 records.  
  
![](../Images/get_ESTIMATE%20DH%209.gif)

**![](../images/UpArrow.gif)**Top of page