![](../HeaderCell.jpg) |  Creating a Single Histogram Chart Sheet Creating and formatting a single histogram chart sheet.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools and methods used to create a single histogram chart sheet in the Plots window.

![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%208.jpg)

## Prerequisites

You have already completed the following:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

## Exercise: Creating a Single Histogram Chart Sheet

In this exercise, you are going to create a single histogram chart sheet using the AU grade field from the data file _vb_holesc. This includes the following tasks:

  * **Defining a new chart, selecting a data file and****multiple chart types**

  * **S** etting the chart's model, bin size, grid, axes and color parameters

  * Displaying summary statistics on the chart

  * Renaming the sheet.

**Defining a New Chart, Selecting a Data File and Multiple Chart Types**

  1. Select the Plots window.

  2. Activate the  Manage ribbon and select  Sheets | Charts | Histogram Select  Insert | Chart | Histogram .

  3. In the Histogram dialog, Data Selection tab, Files and Fields group, select the Data File option, click Browse.

  4. In the Project Browser dialog, Database Tables pane, select the table _vb_holesc., click OK.

  5. Back in the Histogram dialog, in the Files and Fields group, Value Fields list, select [AU].

  6. In the Chart Types group, select the Incremental Histogram - Normal, Cumulative Histogram - Normal, Probability Plot - Normal check boxes.

  7. Select the Frequency and Bin (x2) options.

  8. Check that the other Chart Types group options and check boxes are cleared.

  9. In the Histogram Parameters group, select the Ignore Samples Out of Range option, define the Minimum No of Samples as '0'.

  10. In the Chart Layout group, select Individual Charts and Delete Empty Charts.

  11. Check that your settings are as shown below, click Apply:  
  
![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%201.jpg)  

  12. In the Preview pane, check that your selected histogram is as shown below:  
  
![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%202.jpg)  

  13. In the Chart Thumbnails pane,check that three charts are listed as shown below:  
  
![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%203.jpg)  

![note.gif \(1017 bytes\)](../images/note.gif) | 
     * To view one of the other charts in the set, select the required chart using one of the following methods:
     *        * select a chart in the Chart Thumbnail pane
       * or a chart item from the list in the Charts tab.
     * Unwanted charts can be deleted by, in the Charts tab,Chart List pane, right-clicking the chart item and selecting Delete.   
---|---  
  
  14. In the Summary pane, check that the listed message is as shown below:  
  
![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%204.jpg)

Setting the Chart's Model, Bin Size, Grid, Axes and Color Parameters

  1. Select the Format tab.

  2. Set the Model, Custom Bin Size, Grid, Axes, Color Palette and Charts Annotation Size settings as shown below, click Apply:  
  
![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%205.jpg)  
  

![note.gif \(1017 bytes\)](../images/note.gif) |  Ticking the Charts Annotation Size checkbox enables the display of the chart legends.  
---|---  
  
![note.gif \(1017 bytes\)](../images/note.gif)| 
     * These Format settings, other than the Custom Axes option and associated settings, are applied to all three charts in this set i.e. the (incremental) histogram, the cumulative histogram and the probability plot.
     * Using the Custom Bin Size option applies the defined custom settings to all three charts - this may not give the desired result across all three charts.
     * If the Use Custom Axes option is selected, the defined custom settings apply only to the selected Chart Type. Custom axes settings can be defined separately for each Chart Type.
     * In order to apply a full set of custom Format settings to each of these charts, one would need to generate three separate chart objects i.e. three separate chart sheets, one for each chart type. In this exercise, the three charts are all part of the same object.   
---|---  
  3. In the Preview pane,check that your selected (first) histogram is as shown below:  
  
![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%206.jpg)  

Displaying Summary Statistics on the Chart

  1. Select the Statistics tab.

  2. In the Statistics pane, select the Display Parameters Graphically option,

  3. Select the check boxes next to the required summary statistics items listed in the NAME column, as shown below, click Apply:  
  
![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%207.jpg)  

  4. In the Preview pane, check that your scatter plot now includes a list of summary statistics, as shown below, click OK:  
  
![](../Images/dp_Creating%20a%20Single%20Histogram%20Chart%20Sheet%208.jpg)  

![note.gif \(1017 bytes\)](../images/note.gif) |  The summary statistics are automatically positioned top left, above the chart. The position these summary statistics items can be edited by using click-and-drag; the orientation can be changed using double-click.  
---|---  
  5. Check that a new sheet has been added to the Plots window and that in the Sheets control bar, a new sheet is listed under the Plots folder.

Renaming the Sheet

  1. In the Plots window, right-click on the sheet tab (at the bottom of the Plots window), select Rename.

  2. In the Rename Sheet dialog, define the Name: as 'Histogram 1', click OK.

  3. Check that the sheet has been renamed in both the Plots window and the Sheets control bar.

![](../Images/NextExercise.gif)[Proceed to the next topic](<Creating_a_Multiple_Histogram_Chart_Sheet.md>)