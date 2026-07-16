![](../HeaderCell.jpg) |  Statistical Validation Validating the estimated block model cell grades using summary statistics.  
---|---  
  
# Overview

In this portion of the tutorial you are going to validate the estimated block model cell grades by comparing the summary statistics of the block model and the drillhole grades using the process STATS.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * Read the process description for STATS.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _ubm5g

    * _udhz5c

## Exercise: Validation of Block Model Grade Estimates Using STATS

In this exercise you are going to validate the block model cell estimates for the cyan ore zone (ZONE=1) by comparing the summary statistics of the four grade fields in the 5m composited drillhole samples to those in the 5x5x5m block model cells:

  * Grade block model: 5m regular celled (no sub-cells), zone flagged, block model

  * Sample data file: 5m composited drillholes

  * Grade fields: AU (g/t), CU (%), AG (g/t), CO (%)

  * Filter criteria: ZONE = 1 (i.e. the summary statistics will be restricted to the first mineralized zone).

The grades were estimated using the Search, Variogram and Estimation parameter files _ueps,_uepv and _uepe respectively.

The 3D grade block model and drillhole samples are shown in the image below.

![](../Images/get_StatsValidation%201.GIF)   

![note.gif \(1017 bytes\)](../Images/note.gif) |  In the above image, the block model cells are colored according to three separate mineralization zones (cyan: ZONE=1, green: ZONE=2, red: ZONE=3). The fold axis of the ore body plunges at 35 degrees towards the East, the tabular to massive shaped limbs have a dip of 40 degrees, a maximum down dip length of 240m and a thichkness (perpendicular to the bottom contact) of 5m -45m . The drillholes are set in fans which are parallel with the dip direction of each limb and are spaced 50m apart .tom contact) of between 5 and 45m . The drillholes are set in fans which are parallel with the dip direction of each limb and are spaced approximately 50m apart.  
---|---  
  
![](../Images/Tip.gif) |  Statistical validation of block model cell grades can be used to check:

  * presence of missing grade values
  * summary statistics for each grade field per mineralization zone.

  
---|---  
  
## Calculating Summary Statistics for the ZONE=1 Block Model Cells

  1. Select the Design window.

  2. Activate the  Sample Analysis ribbon and select  Statistics Processes (top-level button) Select  Applications | Statistical Processes | Compute Statistics .

  3. In the STATS dialog, Files tab, Input files group, set IN* by browsing for and selecting the block model file _ubm5g.  
  
![](../Images/get_StatsValidation%202.GIF)  

![note.gif \(1017 bytes\)](../Images/note.gif) |  The summary statistics can also be saved to an output file by defining a new filename in the OUT field in the Output files group.  
---|---  
  4. In the Fields tab, select the F1 field [CU], select the F2 field [AG].

  5. Select the F3 field [AU], select the F4 field [CO], select the F5 field [DENSITY]:  
  
![](../Images/get_StatsValidation%203.GIF)  

  6. In the Retrieval tab, click New.  
  
![](../Images/get_StatsValidation%205b.GIF)  

  7. In the Retrieval Criteria pane, type in 'ZONE = 1', click OK:  
  
![](../Images/get_StatsValidation%205a.GIF)   

  8. Follow the displayed output in the Command control bar, noting the 'Continue?' prompt.

  9. In the Command toolbar, with the cursor flashing in the Run Command box, press <Enter> five times, once for each prompt i.e. for each of the selected input fields.

  10. In the Command control bar, check that the process is complete and that your summary statistics for the CU and AU grade fields are as shown below:  
  
![](../Images/get_StatsValidation%206a.GIF)  
  
![](../Images/get_StatsValidation%206b.GIF)

## Calculating Summary Statistics for the Drillhole Data

  1. Select the Design window.

  2. Activate the  Sample Analysis ribbon and select  Statistics Processes (top-level button) Select  Applications | Statistical Processes | Compute Statistics .

  3. In the STATS dialog, Files tab, Input files group, set IN* by browsing for and selecting the drillholes file _udhz5c.  
  
![](../Images/get_StatsValidation%207.GIF)  

![note.gif \(1017 bytes\)](../Images/note.gif) |  The summary statistics can also be saved to an output file by defining a new filename in the OUT* field in the Output files group.  
---|---  
  4. In the Fields tab, select the F1 field [CU], select the F2 field [AG].

  5. Select the F3 field [AU], select the F4 field [CO], select the F5 field [DENSITY]:  
  
![](../Images/get_StatsValidation%203.GIF)  

  6. In the Retrieval tab, click the New button.  
  
![](../Images/get_StatsValidation%205b.GIF)  

  7. In the Retrieval Criteria pane, type in 'ZONE = 1', click OK:  
  
![](../Images/get_StatsValidation%205a.GIF)   

  8. Follow the displayed output in the Command control bar, noting the 'Continue?' prompt.

  9. In the Command toolbar, with the cursor flashing in the Run Command box, press <Enter> five times, once for each prompt i.e. for each of the selected input fields.

  10. In the Command control bar, check that the process is complete and that your summary statistics for the CU and AU grade fields are as shown below:  
  
![](../Images/get_StatsValidation%208a.GIF)  
  
![](../Images/get_StatsValidation%208b.GIF)  

  11. Compare the CU and AU summary statistics for the block model cells and the drillhole composites.

![note.gif \(1017 bytes\)](../Images/note.gif) |  Using the summary statistics for grade estimate validation, check that:

  * the means of the block model cell estimates and the drillhole samples are equal
  * the shapes of the distributions of the block model cell estimates and the drillhole samples are the same (this can be done using the summary statistics but is better done with histograms which can be generated using the process CHART)

Summary statistics are typically calculated:

  * for each grade field per mineralization zone
  * using a regular celled block model
  * using composited or declustered sample data.

  
---|---  
  
![note.gif \(1017 bytes\)](../Images/note.gif) |  STATNP can be used to calculate non parametric statistics, which include the Median value.  
---|---  
  
**![](../Images/UpArrow.gif)**Top of page