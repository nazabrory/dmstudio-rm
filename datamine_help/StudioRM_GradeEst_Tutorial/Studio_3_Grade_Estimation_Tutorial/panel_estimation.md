![](../HeaderCell.jpg) |  Panel Estimation using PANELEST Using PANELEST to estimate grades into an irregular shaped panel.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the process PANELEST to estimate a grade into a set of panels (mining block) defined by closed strings, using an Ordinary Kriging estimation method.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the process description for PANELEST.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _2dblks

    * _srfsamp

    * _2dvpar1

## Exercise: Using PANELEST for Estimating Grades into Panels

In this exercise you are going to estimate a Au grade for a set of 2D panels using the Ordinary Kriging estimation methods and the following parameters:

  * Input Grade field: AU

  * Estimation method: Ordinary Kriging (IMETHOD=3)

  * Search Volume: all samples within the panel are used for the estimate

  * Variogram model: variogram model 1 (VMODNUM=1)

  * Vertical thickness for volume calculation: 10m (DPLUS=5, DMINUS=5)

  * Discretisation point spacing: 10m (XDSPACE=10, YDSPACE=10).

The panel outlines and sample points are shown in the image below. The panel strings are closed and each have an area of 104,000m2. The displayed sample points have low grade values colored blue and higher grade values colored in red.  

![](../Images/get_PANELEST%201.gif)

![](../Images/Tip.gif) |  Use PANELEST to estimate grades when estimating:

  * panel grades directly without first creating a block model
  * a single grade field at a time
  * into 2D or 3D panels e.g. open pit blast blocks, underground mining panels
  * using the estimation method NN, IPD or Ordinary Kriging
  * Indicator Kriging or Sichel's T estimation.

  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif) | 

  * 2D or 3D open or closed strings can be used to define panels.
  * panel strings must be coplanar and orthogonal to either the X, Y or Z axis.
  * panels can also be defined by sets of 2D or 3D discretisation points.
  * drillholes or suitable points data can be used as Sample Data files.

  
---|---  
  
## Defining the Input Samples, Variogram Model, Panel and Output Results Files

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Panels In the  Menu Bar , select  Models | Interpolation Processes | Estimate Grade of Panels .

  3. In the PANELEST dialog, Files tab, Input files group, set IN* by browsing for and selecting the sample file _srfsamp.

  4. Set VMOPARM* by browsing for and selecting the variogram model file _2dvpar1.

  5. Set PERIM* by browsing for and selecting the strings file _2dblks.

  6. In the Output files group, define a new output results file OUT* as 2dpres1.  
  
![](../Images/get_PANELEST%202.gif)

## Defining the Fields

  1. In the Fields tab, select the X* field [XPT], Y* field [YPT], Z* field [ZPT].

  2. Select the VALUE* field [AU] and the PANEL* field [PVALUE].

  3. Check that your fields are defined as shown below:

![](../Images/get_PANELEST%203.gif)

## Defining the Parameters

  1. In the Parameters tab, define MINNUM as '1' and MAXNUM as '480'.

  2. Define INSIDE as '1'.

  3. Define XDSPACE as '10', YDSPACE as '10' and ZDSPACE as '0'.

  4. Define MINDISC as '50'.

  5. Define DPLUS as '5' and DMINUS as '5'.

  6. Define IMETHOD as '3' and VMODNUM as '1'.

  7. Set the remainder of the parameters to their default values.

  8. Check that your parameters are as shown below:  
  
![](../Images/get_PANELEST%204.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * The MAXNUM value is set to a value greater than the number of samples.
     * The XDSPACE , YDSPACE and ZDSPACE values are typically set to half the sample spacing in the respective X, Y and Z directions.
     * For a 2D panel estimation, the ZDSPACE is irrelevant; this value would be set to a suitable vertical spacing for example an open pit blast block estimated using blast hole samples.
     * The DPLUS and DMINUS values are typically set to represent the height or width of the stoping panel above and below the string defining the panel limits. In this example, an arbitrary distance of '5' above and below the panel string gives a total panel height of 10m.  
---|---  

## Running the Estimation and Checking the Results

  1. Click OK.

  2. In the Command control bar, check that PANELEST has run to completion, check the summary results for each panel and that the file contains 12 records:  
  
![](../Images/get_PANELEST%205.gif)  

  3. In the Project Files control bar, All Tables folder, double-click 2dpres1.

  4. In the Table Editor dialog, check that the estimation results are as shown below, close the dialog:  
  
![](../Images/get_PANELEST%206.gif)

**![](../images/UpArrow.gif)**Top of page