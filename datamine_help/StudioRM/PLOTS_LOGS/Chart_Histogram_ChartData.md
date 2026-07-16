![](../Images/HeaderCell.gif) |  Histograms - Chart Data Viewing a histogram's chart data  
---|---  
  
# Viewing Chart Data

### To access this dialog:

  * Open the [Histogram](<Chart_Histogram.md>) dialog, select a chart from the histogram thumbnails pane, select the Chart Data tab.

For the selected chart, the Chart Data tab tabulates the histogram bin data.

![note.gif \(1017 bytes\)](../Images/note.gif) |  The Chart Data tab only contains data if the Individual Charts option was selected on the [Data Selection](<Chart_Histogram_DataSelection.md>) tab. It is otherwise empty if the Compound Charts option was selected.  
---|---  
  
Field Details:

Chart Data: this group contains a table listing the histogram data, each record represents a histogram bin on the chart:

  * DATA: the bin number.

  * LOWER/MIDDLE/UPPER: the lower, middle and upper values of the selected bin.

  * MEAN: the arithmetic mean value of samples within each bin.

  * FREQUENCY: the number of samples in each bin.

  * CUM-FREQUENCY: the cumulative number of samples up to and including the current bin.

  * %FREQUENCY: the number of samples in the current bin expressed as a percentage of the total number of samples.

  * %CUM-FREQUENCY: the cumulative number of samples up to and including the current bin expressed as a percentage of the total number of samples

  * TOTAL: the total number of samples used for the selected histogram chart.

Additional Field Details for Probability Plots:

  * CUM-PROPORTION (U): the cumulative number of samples up to the upper limit of the current bin expressed as a proportion of the total number of samples.

  * CUM-PROPORTION (M): the cumulative number of samples up to the mid point of the current bin expressed as a proportion of the total number of samples.

  * INV-NORMAL: the inverse normal distribution values corresponding to the CUM-PROPORTION (M) values.

  * PROB-LINE: the INV-NORMAL value for the corresponding standard normal distribution. This is used for plotting the model.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Histograms](<Chart_Histogram.md>)[  
Histograms - Data Selection](<Chart_Histogram_DataSelection.md>)[  
Histograms - Preview](<Chart_Histogram_Preview.md>)[  
Histograms - Chart Parameters](<Chart_Histogram_ChartProperties.md>)[  
Histograms - Fit Model](<Chart_Histogram_FitModel.md>)