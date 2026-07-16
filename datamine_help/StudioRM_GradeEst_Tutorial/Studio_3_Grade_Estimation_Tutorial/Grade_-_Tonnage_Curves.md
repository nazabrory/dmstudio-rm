![](../HeaderCell.jpg) |  Grade-Tonnage Curves Creating grade-tonnage curves using Mining Power Pack.  
---|---  
  
# Overview

In this portion of the tutorial you are going to use Mining Power Pack to create grade-tonnage curves from a cut-off grades results table.

## Prerequisites

  * As this exercise uses Datamine's Mining Power Pack Excel plug-in, you will need a version of Microsoft® Excel version 2007 or higher installed on your local machine, with a version of Mining Power Pack that is compatible with your Office version - if in doubt, contact your Datamine representative for assistance.

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Grade Estimation Project](<Creating_a_New_Grade_Estimation_Project.md>) page.

  * Displayed toolbars and defined project settings - exercises in the [Displaying Grade Estimation Toolbars](<Display_Grade_estimate_Toolbars.md>) and [Defining Settings](<Defining_Settings.md>) pages.

  * [Files](<tutorial_files.md>) required for the exercises on this page:

  *     * _geres4

##  Exercise: Creating Grade-Tonnage Curves Using MPP

In this exercise you are going to use Mining Power Pack and the cut-off grade results table _geres4, (output from the TONGRAD process) to generate a set of grade-tonnage curves. The table contains results for calculated for 10 cut-off intervals, each 2 g/t in size.

![note.gif \(1017 bytes\)](../images/note.gif) |  What is a Tonnage Grade Curve?

  * Grade-Tonnage curves are plots of average grades and tonnes for a range of cut-offs.
  * These plots can have a variety of formats e.g.:
  *     * Average Grade Above Cutoff (Y axis) vs Tonnes (X axis), for the range of cutoffs at a specific block size
    * A combined plot of Tonnage (Y axis 1) vs Cut-off Grade (X axis) and Average Grade Above Cutoff (Y axis 2) vs Cut-off Grade.
  * This grade-tonnage curve can either be generated from a standard results table or a cut-off grades results table. The former is output when strings or wireframes are evaluated against a grade block model, while the latter is output from the processes TONGRAD or SMUHIS.

What is Mining Power Pack?

  * Mining Power Pack (2010) is an Add-In for MS Excel 2010®, primarily focused on providing utilities for working with geological and mining-related data within Excel.
  * It is not automatically installed along with Studio, but needs to be installed separately.
  * Most of the utilities enable the rapid processing and manipulation of mining evaluation data. In particular, the facilities in Mining Power Pack enable automatic weighting of mineral grade values, which otherwise are only obtained in Excel by a tedious and time-consuming entry of functions cell-by-cell. These capabilities complement the existing standard Excel functionality.

  
---|---  
  
![](../Images/Tip.gif) |  UseMining Power Packfor:

  * Tabulation, combination and calculations with mining and geological data.
  * Grade-tonnage curve generation and analysis.
  * Color-coding of mining and geological data.
  * Mining and geological unit conversion.
  * Analysis of graphs depicting mining and geological data.

  
---|---  
  
## Starting Mining Power Pack

  1. Select the Design window.

  2. Activate the  Report ribbon and select  Model Reserves | Mining Power Pack Select  Tools | CAE Products | Mining Power Pack .

  3. In Excel, on the Message Bar, click Enable Content.  
  
![](../Images/get_Grade%20Tonnage%20Curves%201.gif)  

  4. In Microsoft Excel, check that the Mining Power Pack menu bar item is displayed:  
  
![](../Images/get_Grade%20Tonnage%20Curves%202.gif)

## Inserting a New Worksheet

  1. Select File| New , then double-click Blank Workbook.

  2. In the title bar, check that a new worksheet has been created, as shown below:  
  
![](../Images/get_Grade%20Tonnage%20Curves%203.gif)  
  

## Importing a Datamine Table

  1. Select Mining Power Pack | Import/Export | Import Datamine File.

  2. In the Import Datamine File dialog, Import Options group, select the Use File System option.

  3. Set File: by browsing for and selecting the file C:\Database\MyTutorials\GradeEst\\_geres4.dm.

  4. Check the file contents in the File Preview pane, click Import:  
  
![](../Images/get_Grade%20Tonnage%20Curves%204.gif)  

  5. In Excel, check that the 8 rows (including the header) and 8 columns of the Datamine table have been imported, as shown below:  
  
![](../Images/get_Grade%20Tonnage%20Curves%205.gif)

## Creating a New Chart

  1. In the _geres4.dm worksheet, select the range A1:H8, as shown below:  
  
![](../Images/get_Grade%20Tonnage%20Curves%206.gif)  

  2. Select Mining Power Pack| Utilities | Chart analysis.

  3. In the Chart Analyser dialog, check that the Input Range: is set to '_geres4.dm'!$A$1:$H$8 .

  4. Define the settings as shown below, click Apply:  
  
![](../Images/get_Grade%20Tonnage%20Curves%207.gif)  

  5. Check that your chart has been generated as shown below:  
  
![](../Images/get_Grade%20Tonnage%20Curves%208.gif)  

  6. In the Chart Analyser dialog, click Exit.

![note.gif \(1017 bytes\)](../images/note.gif) |  Grade-Tonnage curves can also be created in Mining Power Pack using the following method:

  * Importing a standard results table i.e. not a cut-off grade results table.
  * Using the menu option Mining Power Pack|Utilities | Grade-Tonnage Curve.

  
---|---  
  
## Saving the Project and Exiting Mining Power Pack

  1. Select File | Save As.

  2. In the Save As dialog, browse to your project folder, define a new File name 'GTCurves1.xlsx', click Save.

  3. Select File |Exit.

  4. In the Microsoft Excel prompt dialog, click Don't Save.

![note.gif \(1017 bytes\)](../images/note.gif) |  The grade-tonnage table and the grade-tonnage curve can be embedded in Word documents or printed.  
---|---  
  
**![](../images/UpArrow.gif)**Top of page