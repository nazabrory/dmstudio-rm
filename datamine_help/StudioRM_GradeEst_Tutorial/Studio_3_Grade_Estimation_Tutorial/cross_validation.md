![](../HeaderCell.jpg) |  Cross Validation Optimizing grade estimation parameters using cross validation.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the XVALID process which is used to optimize search, variogram and estimation parameters using the cross validation technique.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the process description for XVALID .

  * Read the help documentation notes page for [Cross Validation Notes](<Cross%20Validation%20Notes.md>).

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _srfsamp

    * _2dspar1

    * _2depar1

    * _2dvpar1

## Optimizing Estimation Parameters Using Cross Validation

In this exercise you are going to choose an 'optimum' set of estimation parameters, for estimating the output grade field AU_OK, by comparing the cross validation statistics results for different variogram models and search parameters as follows:

  * Variograms: compare a single vs. a double spherical model, keeping all other parameters constant

  * Search Volume: compare a non-octant vs. an octant search, keeping all other parameters constant.

![note.gif \(1017 bytes\)](../images/note.gif) |  The estimation parameter file _2depar1 contains three separate runs for estimating the input grade field AU. These three output grade fields are AU_NN, AU_IPD and AU_OK. This exercise focuses on optimizing the parameters for the AU_OK output grade field.  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif) |  How does the Cross-validation Technique work?

  * It removes each sample point in turn from the data file and estimates its value from the remaining data.
  * In this way a table of actual and estimated values is created. 
  * A detailed statistical analysis is then carried out comparing the actuals and estimates.
  * One (or more) of the estimation parameters can then be changed and the process rerun to see whether the new parameter(s) improve the results of the statistical analysis.
  * The method is iterative, requiring several runs to establish the best set of parameters.

  
---|---  
  
## Generating the First Set of Cross Validation Results using XVALID

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Variograms | Validate Select  Applications | Statistical Processes | Variograms | Cross Validate .

  3. In the XVALID dialog, Files tab, Input files group, set IN* by browsing for and selecting the file _srfsamp.

  4. Set SRCPARM* by browsing for and selecting the file _2dspar1.

  5. Set ESTPARM* by browsing for and selecting the file _2depar1.

  6. Set VMODPARM* by browsing for and selecting the file _2dvpar1.

  7. In the Output files group, check that XVSAMPS is undefined.

  8. Define a new XVSTATS output file '2dxvs1'.

  9. Check that SAMPOUT is undefined, check that your file names are as shown below:  
  
![](../Images/get_CrossValidation%201.gif)  

  10. In the Fields tab, select the X* field [XPT].

  11. Select the Y* field [YPT].

  12. Select the Z* field [ZPT].

  13. Check that your fiields are undefined as shown below:  
  
![](../Images/get_CrossValidation%202.gif)  

  14. In the Parameters tab, check that the value of SMINFAC is '0.0001'.  
  
![](../Images/get_CrossValidation%203.gif)  

  15. Click OK.

  16. In the Output window, check that the Summary Input Parameters are as shown below:  
  
![](../Images/get_CrossValidation%204.gif)  

  17. Check that the Cross-Validation Statistics for AU i.e. the third AU grade estimate (the output grade field AU_OK) are as shown below:  
  
  
![](../Images/get_CrossValidation%205.gif)

  18. Record your key input parameters and output statistics in a table similar to that shown below:  
  
  
![](../Images/get_CrossValidation%206.gif)

## Comparing Variogram Model Parameters using XVALID

  1. In the Output window, note the following Cross-Validation Menu options:  
  
![](../Images/get_CrossValidation%207.gif)

  2. In the Command toolbar (by default at the bottom-left of the main window) type in '2', press <Enter>.

  3. In the Datamine Table Editor dialog, move down to Record 3, the VREFNUM field cell.

  4. Change the value from '1' to '2', press <Enter>:  
  
![](../Images/get_CrossValidation%208.gif)  

  5. Select File | Save, then close the dialog.

  6. Back in the Command toolbar, type in '8', press <Enter>.

  7. Select the Output window and check that the summary parameters and validation statistics for the modified third AU grade estimate (i.e. output grade field AU_OK) are now as shown below:  
  
![](../Images/get_CrossValidation%209.gif)  
  
![](../Images/get_CrossValidation%2010.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  These statistics are saved to the output statistics file 2dxvs1 that was defined under the Output files tab when first setting up the process.  
---|---  
  8. Compare the results of these two cross validation runs which use different sets of variogram model parameters i.e. VREFNUM = 1 and then VREFNUM = 2.  

![note.gif \(1017 bytes\)](../images/note.gif) |  The following guidelines should be used when using Cross-Validation statistics to compare different runs. The statistics are listed in order of decreasing importance:
     * For an unbiased estimate, the means of the Estimates and Actuals should ideally be equal
     * mean difference (as % of actual) - aim is to make the statistic as close as possible to zero. It should be < 5% and hopefully < 2%.
     * kriging variance ratio - it should lie in the range between 0.8 and 1.2, and be as close as possible to 1.
     * correlation coefficient - always lies between -1 and +1 (a value of +1 shows perfect positive correlation). Aim to make the correlation coefficient as large as possible.
     * mean absolute difference - aim to make it as close as possible to zero
     * regression line slope (constant b) - slope of the line should ideally be equal to 1.
A change in the one of the input model variogram parameters (,estimation or search parameters) will often result in some of the statistics improving and others getting worse. The end result is likely to be a compromise. For a full description of the use of these Cross-validation statistics, please see the [Cross Validation Notes](<Cross%20Validation%20Notes.md>)  
---|---  
  9. Repeat steps 2 to 6 and reset the VREFNUM to '1'.

  10. In the Command toolbar type in '0', press <Enter> (to stop running XVALID).

![note.gif \(1017 bytes\)](../images/note.gif) |  Cross Validation can be used to compare sets and combinations of:

  * Variogram parameters
  * Search Volume parameters
  * Estimation parameters.

The optimization of variogram, search and estimation parameters using Cross Validation is an iterative process.  
---|---  
  
**![](../images/UpArrow.gif)**Top of page