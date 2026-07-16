![](../HeaderCell.jpg) |  Indicator Estimation Using ESTIMATE for Indicator Kriging estimation.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the process ESTIMATE to estimate grades using an Indicator Estimation method.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the help documentation notes page for ESTIMATE, in your Help file.

  * Read the Grade Estimation User Guide page on Kriging.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _2dzmod1

    * _srfsamp

    * _2dspar1

    * _2dvpar2

## Using ESTIMATE for Indicator Estimation

In this exercise you are going to estimate Au grades into a 2D block model using a Median Indicator Kriging estimation method and the following parameters:

  * Input Grade field: AU

  * Output Grade fields: AU

  * Estimation methods: Indicator Kriging (IK)

  * Search Volume: search volume 1 (SREFNUM=1)

  * Variogram model: variogram model 1 and 2 (VREFNUM=1,2)

  * Estimation options: zonal control (field ANOM), values 1 and 2

  * Median Indicator values: AU=267 (for zone ANOM=1) and AU=752 (for zone ANOM=2)

  * Cutoff Grades for ANOM = 1: AU=104, 266, 431, 570 (these are the grades at the 25%, 50%, 75% and 95% quantiles)

  * Cutoff Grades for ANOM = 2: AU=652, 746, 874, 1083 (these are the grades at the 25%, 50%, 75% and 95% quantiles).

This will be done by defining a total of eight Indicator Kriging runs, one for each of the four cutoffs (listed above) for each of the zones i.e. ANOM=1 and ANOM=2. These estimation parameters will then be saved to a new estimation parameter file 2depar4.

![note.gif \(1017 bytes\)](../images/note.gif) |  Indicator Estimation Indicator Estimation is a non parametric estimation method and so does not depend on the statistical distribution of the data as in standard (i.e. non-indicator estimation) Ordinary and Simple Kriging methods. The estimation method used with indicator estimation is typically ordinary kriging although other estimation methods can also be used e.g. inverse power distance, simple kriging.  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif) |  Advantages and Disadvantages of Indicator Kriging Advantages:

  * in general the indicator variograms are better behaved i.e. smoother
  * outliers do not cause a problem
  * the sill of the variogram can be calculated theoretically
  * gives recovered grade and tonnes by cutoff
  * non parametric i.e. it does not depend on the grade distribution (histogram) of the samples.

Disadvantages:

  * it can take longer to set up as in theory you need to calculate a variogram for each cutoff, although median IK can be used to avoid this
  * indicator variograms can be affected by clustering of samples
  * the recovered grades and tonnes cannot be related to a specific size of SMU
  * there can be order relation problems
  * there is no theoretical kriged variance
  * the Indicator Estimation method cannot be combined with non indicator estimation methods in the Datamine estimation parameter file
  * only one set of indicators (per Zonal Control zone) can be defined in a set of estimation parameters in the Datamine estimation parameter file.

  
---|---  
  
The input block model and sample points are shown in the image below. The blue block model cells represent the lower grade zone (field ANOM=1) while the red cells represent the higher grade zone (field ANOM=2). The displayed sample points are colored using a rainbow blue-red legend, with the lower grade values colored blue and the higher grade values colored in red.  

![](../Images/get_ESTIMATE%20IK%201.gif)

![](../Images/Tip.gif) |  Indicator Kriging is typically used for:

  * automatically defining boundaries between different zones in a block model e.g. low/high grade ore zones or rock types
  * estimating grades for complex (and inseparable) mixed data populations
  * estimating grades for highly skewed grade distributions
  * as an alternative to log normal kriging.

  
---|---  
  
## Defining the Input Block Model and Sample Files

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Interpolate Select  Models | Interpolation Processes | Interpolate Grades from Menu .

  3. In the Grade Estimation (ESTIMATE) dialog, Files tab, select the Input sub-tab.

  4. In the Geological Model group, click Browse.

  5. In the Project Browser dialog, Database Tables pane, Block Models folder, select _2dzmod1 , click OK.

  6. In the Sample Data group, click Browse.

  7. In the Project Browser dialog, Database Tables pane, All Tables folder, select _srfsamp , click OK.

  8. In the Coordinates Fields group, select the X, Y and Z fields [XPT], [YPT], [ZPT].

  9. In the Zone Control Fields group, select the Zone 1 field [ANOM].

  10. Check that your parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20IK%202.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * Drillholes or suitable points data can be used as Sample Data files. 
     * Both the Input Model and the Sample File need to be defined so that the Zone Control Fields can be selected.
     * The Zone Control Fields need to be present (and contain suitable matching zone field values) in both the Input Model and the Sample File.  
---|---  

## 

## Defining the Output Block Model, Input/Output Search Volume, Estimation and Variogram Model Files

  1. In the Grade Estimation (ESTIMATE) dialog, Files tab, select the Output subtab.

  2. In the Grade Model group, define a new model file '2dgmod4'.

  3. In the Parameter Files (Input and Output) group, clear the Use Defaults check box.

  4. Browse for and set the Search Volume File to _2dspar1.

  5. Define a new Estimation Parameter File '2depar4'.

  6. Browse for and set the Variogram Model File to _2dvpar2.

  7. Check that your parameters are as shown below:  
  
![](../Images/get_ESTIMATE%20IK%203.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  The Search Volume File, Variogram Model File and the Estimation Parameter File need to be defined here so that the relevant search, variogram model and estimation parameters are displayed in the various tabs.  
---|---  

## Checking the Search Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Files tab, click Next >>.

  2. In the Search Volumes tab, Summary subtab, check that the Search Parameter Table contains the set of search parameters shown below:  
  
![](../Images/get_ESTIMATE%20IK%204.gif)

![note.gif \(1017 bytes\)](../images/note.gif) |  Multiple Indicator Kriging Search Volumes When using multiple indicator kriging, the same set of search volume parameters must be used for each indicator cutoff in the set.  
---|---  
  
##  Checking the Variogram Model Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Search Volumes tab, click Next >>.

  2. In the Variogram Models tab, Summary subtab, check that the Variogram Model Table contains two sets of parameters, as shown below:  
  
![](../Images/get_ESTIMATE%20IK%205.gif)  
![](../Images/get_ESTIMATE%20IK%205b.gif)  
  

![note.gif \(1017 bytes\)](../images/note.gif) |  The variogram model file contains two variogram models:
     * model 1 is for the median indicator AU=267 (for zone ANOM=1)
     * model 2 is for the median indicator AU=752 (for zone ANOM=2)
     * each model consists of two spherical structures.  
---|---  

##  Defining a New Set of Indicator Kriging Estimation Parameters

![note.gif \(1017 bytes\)](../images/note.gif) |  Selecting Suitable Cutoffs The following methods are typically used to select cutoffs for multiple indicator kriging:

  * Use the maximum quartile (25%, 50%, 75%) and the maximum 95%* quantile grade values
  * Use the maximum decile (10%, 20%, ... 90%) and the maximum 95%* quantile grade values
  * Base cutoffs on values related to mineralization zones or grade control category boundaries.

* - The 95% quantile (or another more suitable top end quantile) is typically used, in addition to the quartiles or deciles, to cater for the 'upper tails' i.e. the high grade values in high positively skewed data distributions.  
---|---  
  
  1. In the Grade Estimation (ESTIMATE) dialog, Variogram Models tab, click Next >>.

  2. In the Estimation Types tab, Index group, click Reset and then Yes to remove any previous parameters.

  3. Check that the Index pane does not contain any items.

  4. In the Index group, click Add.

  5. In the estimation parameter list, check that a new estimation parameter description '1: Estima Param 1' has been added.

  6. Select the Attributes sub-tab on the right.

  7. In the Method group, select the Indicator Estimation-applies to all Estimation Parameters option.

  8. Define the remaining parameters as shown below:  
  
![](../Images/get_ESTIMATE%20IK%206.gif)  

  9. In the Options subtab, define the parameters as shown below:  
  
![](../Images/get_ESTIMATE%20IK%207.gif)  

  10. In the Indicator Estimation subtab, define the parameters as shown below:  
  
![](../Images/get_ESTIMATE%20IK%208.gif)  

  11. Repeat steps 4 to 10 , defining a set of parameters for each of the remaining cutoffs (266, 431, 570) for the first zone (i.e. ANOM=1).  

![note.gif \(1017 bytes\)](../images/note.gif) |  The cutoff values (listed in the brackets in step 11.) are used in the Indicator Estimation subtab, Cutoff Data group, Upper cutoff grade for current interval field when defining each set of cutoff parameters.  
---|---  
  12. Repeat steps 4 to 8 , for the second zone (i.e. setting ANOM=2 and using variogram model 2), defining a set of parameters for each of the cutoffs (652, 746, 874, 1083), remembering to select the correct Search and Variogram Definition and Zone Field Values groups' field values as highlighted below:  
  
![](../Images/get_ESTIMATE%20IK%209.gif)  

  13. In the Summary subtab, check that your 8 sets of parameters are the same as those shown below:  
  
![](../Images/get_ESTIMATE%20IK%2010a.gif)  
![](../Images/get_ESTIMATE%20IK%2010c.gif)  
  
  
  
![](../Images/get_ESTIMATE%20IK%2010b.gif)  
![](../Images/get_ESTIMATE%20IK%2010d.gif)

## Exporting the New Set of Estimation Parameters

  1. In the Grade Estimation (ESTIMATE) dialog, Estimation Types tab, Index group, click Export.

  2. In the Project Browser dialog, define a new Filename '2depar4', click OK.

## Running the Estimation From the Preview Tab

  1. In the Grade Estimation (ESTIMATE) dialog, Controls tab, click Next >>.

  2. In the Preview tab, Summary subtab, check your parameters.

  3. Click Run.

  4. In the Command control bar, check that ESTIMATE has run successfully with the Indicator Kriging runs and that the output file 2dgmod4 contains 780 records.

**![](../images/UpArrow.gif)**Top of page