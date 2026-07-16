![](../HeaderCell.jpg) |  Inverse Power Distance Using GRADE for Inverse Power Distance and Ordinary Kriging estimation methods.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use the process GRADE to estimate grades using the Inverse Distance method.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the help documentation notes page for GRADE, in your Help file.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _2dpmod1

    * _srfsamp

## Using Grade to Perform a Basic Grade Estimation Run

In this exercise you are going to estimate Au grades into a 2D block model using the following parameters:

  * Grade field: AU

  * Estimation method: Inverse Power Distance (IPD)

  * Search Volume: see parameters below

  * Variogram model: see parameters below

  * No zonal control.

![](../Images/Tip.gif) |  Use GRADE to estimate grades into a block model when using:

  * a single grade field
  * estimation method NN, IPD or OK
  * a single search volume, parameters not saved in a search parameter file.

  
---|---  
  
## Estimating AU Using the Inverse Power Distance Method

  1. Select the Design window.

  2. Activate the  Estimate ribbon and select  Estimate | Basic In the  Modeling toolbar, click  Basic Grade Interpolation .

  3. In the GRADE dialog, Files tab, Input files group, set PROTO* by browsing for and selecting the file _2dpmod1.

  4. Set IN* by browsing for and selecting the file (from the All Tables folder) _srfsamp.

  5. In the Output files group, define a new output MODEL* '2dgmod1':  
  
![](../Images/get_GRADE%201.gif)  

  6. In the Fields tab, select the X* field [XPT] - note that the default value of 'X' must be changed.

  7. Select the Y* field [YPT].

  8. Select the Z* field [ZPT].

  9. Select the VALUE* field [AU].

  10. Check that your fields are defined as shown below:  
  
![](../Images/get_GRADE%202.gif)  

  11. In the Parameters tab, define the search parameters as shown below:  
  
![](../Images/get_GRADE%203.gif)  
  
  

  12. In the Parameters tab, define the estimation parameters as shown below:  
  
![](../Images/get_GRADE%204.gif)  

  13. Click OK.

  14. In the Command control bar, check that the grade estimation process has run successfully and that the output file 2dgmod1 contains 780 records:  
  
![](../Images/get_GRADE%205.gif)  

![note.gif \(1017 bytes\)](../images/note.gif) |  Multiple grade estimates can be done by:
     * generating the first grade block model using GRADE
     * if required, renaming the block model's grade field using the Table Editor
     * running GRADE on the next grade field, using the file output from the previous run as input.  
---|---  

**![](../images/UpArrow.gif)**Top of page