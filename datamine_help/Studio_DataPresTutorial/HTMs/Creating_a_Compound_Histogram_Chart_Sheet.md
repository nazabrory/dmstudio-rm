![](../HeaderCell.jpg) |  Creating a Compound Histogram Chart Sheet Creating and formatting a compound histogram chart sheet.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools and methods used to create a compound histogram chart sheet in the Plots window.

![](../Images/dp_Creating%20a%20Compound%20Histogram%20Chart%20Sheet%207.jpg)

## Prerequisites

You have already completed the following:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

## Exercise: Creating a Compound Histogram Chart Sheet

In this exercise, you are going to create a compound (stacked) histogram chart sheet using the CU grade field from the data file _vb_holesc. The ZONE field (mineralization zone code field) will be used as a Key Field to generate a compound histogram for the three mineralization zones. This includes the following tasks:

  * **Defining a new incremental compound chart and selecting a data file**

  * **S** etting the chart's model, bin size, grid, axes and color parameters

  * Displaying summary statistics on the chart

  * Renaming the sheet.

**Defining a New Incremental Compound Chart and Selecting a Data File**

  1. Select the Plots window.

  2. Activate the  Manage ribbon and select  Sheets | Charts | Histogram Select  Insert | Chart | Histogram .

  3. In the Histogram dialog, Data Selection tab, Files and Fields group, select the Data File option, click Browse.

  4. In the Project Browser dialog, Database Tables pane, select the table _vb_holesc., click OK.

  5. Back in the Histogram dialog, Files and Fields group, in the Value Fields list select [CU], in the Key Fields list select [ZONE].

  6. In the Chart Types group, select the Incremental Histogram - Normal check box and the corresponding Bin option.

  7. Select the Frequency option.

  8. Check that the other Chart Types group options and check boxes are cleared.

  9. In the Histogram Parameters group, select the Ignore Samples Out of Range option, define the Minimum No of Samples as '0'.

  10. In the Chart Layout group, select Compound Chart and Delete Empty Charts.

  11. Check that your settings are as shown below, click Apply:  
  
![](../Images/dp_Creating%20a%20Compound%20Histogram%20Chart%20Sheet%201.jpg)  

  12. In the Preview pane, check that your compound histogram chart is as shown below:  
  
![](../Images/dp_Creating%20a%20Compound%20Histogram%20Chart%20Sheet%202.jpg)

![note.gif \(1017 bytes\)](../images/note.gif) |  The compound chart consists of four superimposed histograms, one for all samples and one for each of the mineralization zones. Each histogram is shown in a different color.  
---|---  
  13. In the Chart Thumbnails pane,check that a single compound chart is listed, as shown below:  
  
![](../Images/dp_Creating%20a%20Compound%20Histogram%20Chart%20Sheet%203.jpg)  

     * select a chart in the Chart Thumbnail pane

     * or a chart item from the list in the Charts tab.

Unwanted charts can be deleted by, in the Charts tab,Chart List pane, right-clicking the chart item and selecting Delete. 

![note.gif \(1017 bytes\)](../images/note.gif) |  To view one of the other charts (if multiple charts are available) in the set, select the required chart using one of the following methods:  
---|---  
  14. In the Summary pane, check that the listed message is:  
  
![](../Images/dp_Creating%20a%20Compound%20Histogram%20Chart%20Sheet%204.jpg)

Setting the Chart's Model, Bin Size, Grid, Axes and Color Parameters

  1. Select the Format tab.

  2. Set the Model, Custom Bin Size, Grid, Axes, Color Palette and Charts Annotation Size settings, as shown below, click Apply:  
  
![](../Images/dp_Creating%20a%20Compound%20Histogram%20Chart%20Sheet%205.jpg)  

![note.gif \(1017 bytes\)](../images/note.gif) |  Ticking the Charts Annotation Size checkbox enables the display of the chart legends.  
---|---  
  3. In the Preview pane,check that the selected Compound Chart histogram is as shown below:  
  
![](../Images/dp_Creating%20a%20Compound%20Histogram%20Chart%20Sheet%206.jpg)  

![note.gif \(1017 bytes\)](../images/note.gif) |  In order that the bars within the same bin, from the three superimposed histograms, are visible, the bars are plotted in a staggered format adjacent to one another (and not one behind the other). The width of each bar equal to the 'bin size/number of charts'. In the above example, there are four charts and so each bar is a quarter of the bin width.  
---|---  
  4. Check that a new sheet has been added to the Plots window and that in the Sheets control bar, a new sheet is listed under the Plots folder.

Displaying the Chart in 3D

  1. In the Preview pane, right-click-and-drag the cursor down and to the left.

  2. Check that the chart is rotated into a 3D view as shown below:  
  
![](../Images/dp_Creating%20a%20Compound%20Histogram%20Chart%20Sheet%207.jpg)

Renaming the Sheet

  1. In the Plots window, right-click on the sheet tab (at the bottom of the Plots window), select Rename.

  2. In the Rename Sheet dialog, define the Name: as 'Histogram 3', click OK.

  3. Check that the sheet has been renamed in both the Plots window and the Sheets control bar.

![](../Images/NextExercise.gif)[Proceed to the next topic](<Editing_Histogram_Chart_and_Model_Parameters.md>)