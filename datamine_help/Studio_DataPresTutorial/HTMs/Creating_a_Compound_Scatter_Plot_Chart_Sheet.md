![](../HeaderCell.jpg) |  Creating a Compound Scatter Plot Chart Sheet Creating and formatting a compound scatter plot chart sheet.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools and methods used to create a compound scatter plot chart sheet in the Plots window.

## Prerequisites

You have already completed the following:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

## Exercise: Creating a Compound Scatter Plot Chart Sheet

In this exercise, you are going to create a compound scatter plot chart sheet using the AU and CU grade fields from the data file _vb_holes. The LITH field (rock type field) will be used as a Key Field to generate five scatter plots, one for each rock type, overlain on the same set of axes. This includes the following tasks:

  * **Defining a new chart and selecting a loaded data object**

  * **S** etting the chart's symbol and color parameters using legends

  * Displaying summary statistics on the chart

  * Renaming the sheet.

**Defining a New Chart and Selecting a Loaded Data Object**

  1. Select the Plots window.

  2. Select Insert | Chart | Scatter Plot.

  3. In the Scatter Plot dialog, Data Selection tab, Files and Fields group, select Loaded Data, select [_vb_holes (drillholes)].

  4. In the X Axis field select [AU], in the Y Axis field select [CU], in the Key Field list select [LITH].

  5. In the Axis Scaling group, use the selected defaults.

  6. In the Layout group, select Compound Chart and Delete Empty Charts.

  7. Check that your settings are as shown below, click Apply:  
  
![](../Images/dp_Creating%20a%20Compound%20Scatter%20Chart%20Sheet%201.jpg)  

  8. In the Chart Thumbnails pane,check that a single Compound Chart is listed:  
  
![](../Images/dp_Creating%20a%20Compound%20Scatter%20Chart%20Sheet%202.jpg)  

  9. In the Preview pane,check that your Compound Chart is as shown below:  
  
![](../Images/dp_Creating%20a%20Compound%20Scatter%20Chart%20Sheet%203.jpg)

  10. In the Summary pane, check that a single chart has been generated as shown below:  
  
![](../Images/dp_Creating%20a%20Compound%20Scatter%20Chart%20Sheet%204.jpg)

Setting the Chart's Symbol and Color Parameters

  1. Select the Format tab.

  2. Set the Colour, Symbol and Models group settings as shown below, click Apply:  
  
![](../Images/dp_Creating%20a%20Compound%20Scatter%20Chart%20Sheet%205.jpg)

  3. In the Preview pane, check that your scatter plot symbols, colors and model are as shown below:  
  
![](../Images/dp_Creating%20a%20Compound%20Scatter%20Chart%20Sheet%206.jpg)  

Displaying Summary Statistics on the Chart

  1. Select the Statistics tab.

  2. In the Statistics pane, tick the boxes next to the required summary statistics listed in the NAME column, click Apply:  
  
![](../Images/dp_Creating%20a%20Compound%20Scatter%20Chart%20Sheet%207.jpg)  

  3. In the Preview pane, check that your scatter plot now includes a list of summary statistics, as shown below, click OK:  
  
![](../Images/dp_Creating%20a%20Compound%20Scatter%20Chart%20Sheet%208.jpg)

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * The summary statistics are for the compound data set i.e. all samples.
     * The summary statistics are automatically positioned top left, above the chart. The position this summary statistics box can be edited.   
---|---  
  4. Check that a new sheet has been added to the Plots window and that in the Sheets control bar, a new sheet is listed under the Plots folder.

Renaming the Sheet

  1. In the Plots window, right-click on the sheet tab (at the bottom of the Plots window), select Rename.

  2. In the Rename Sheet dialog, define the Name: as 'Scatterplot 3', click OK.

  3. Check that the sheet has been renamed in both the Plots window and the Sheets control bar.

![](../Images/NextExercise.gif)[Proceed to the next topic](<Editing_Scatter_Plot_Chart_Parameters.md>)