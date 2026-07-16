![](../Images/HeaderCell.gif) |  Scatter Plots - Statistics Configuring the statistical information your chart will display  
---|---  
  
# Scatter Plots - Statistics

### To access this dialog:

  * In the [Scatter Plots](<Chart_ScatterPlot.md>) dialog, select a chart from the scatter plot thumbnails pane, select the Statistics tab.

The Statistics tab is used to view the selected chart's summary statistics and define which statistics are displayed on the chart.

![](../Images/Chart_Scatter_Statistics%201.gif)

Field Details:

In the Statistics group:

![note.gif \(1017 bytes\)](../Images/note.gif) |  For the purpose of generating the log statistics (Sum of Logs, Mean of Logs, Logarithmic Variance), all values (i.e. those for the selected Value Fields), which are <= 0 (zero) or absent (-), are ignored. Logarithmic values are calculated to base 'e'.  
---|---  
  
Display Parameters Graphically: if selected, vertical lines will appear on the graph corresponding to the position, within the current data set, of the mean, geometric mean, log estimate mean and/or percentile positions for all selected percentiles. Once active, you can choose to set a color for each of these values.

Tick the following check boxes to display the listed item in the charts statistics box:

Column Header Rows: the column headers NAME (name of statistic), X Axis, Y Axis and DECIMALS (number of decimal places).

![note.gif \(1017 bytes\)](../Images/note.gif) |  The number of decimal places listed under the DECIMALS column can be edited individually for each statistic; this is done by typing in a new value in the corresponding cell in the displayed statistics table.  
---|---  
  
Total Records: the total number of data records for the selected object or file. This includes all keys and records with absent data values.

Total Samples: the total number of samples used to create the current chart. This takes into account any key fields that have been specified for the chart but does not include records with absent Value or Weight fields.

No. of Missing Values: the number of samples not used to create the current chart. This is the difference between Total Records and Total Samples.

No. of Values > Trace: the "trace" value is defined as 0.10E-29. The number of values greater than trace is therefore effectively the number of values greater than zero.

Maximum: the maximum value used to create the current chart.

Minimum: the minimum value used to create the current chart.

Range: the range of data values. This is equal to Maximum-Minimum .

Total: the sum total of all values used to create the current chart.

Mean: the mean of all values used to create the current chart.

Variance: the statistical variance of the values used to create the current chart. This is calculated as:

Variance = ∑( xi ẍ)2/ n = [ ∑xi2 (∑xi)2/ n ] / n 

where xi are sample values, ẍ is the mean of the samples and n is the number of samples.

Standard Deviation: the square root of the variance.

Standard Error: the standard error is also know as "the standard error of the mean" and is calculated as the Standard Deviation divided by the square root of Total Samples.

Coefficient of Variation: this is defined as the ratio of the Standard Deviation to the Mean.

Skewness: this is a measure of the asymmetry of the probability distribution of a variable. A negative skewness indicates that the left tail is longer than the right. Conversely, a positive skewness indicates the opposite - right is longer. A Standard Normal distribution has a skewness of zero:  
  
![](../Images/Charting_Skewness.gif)

Kurtosis: this is a measure of the "peakedness" of the probability distribution. A high kurtosis distribution has a sharper "peak" and longer, thinner "tails", while a low kurtosis distribution has a more rounded peak with wider "shoulders" (i.e., shorter "fatter" tails)*. A Standard Normal distribution has a kurtosis of zero:  
  
![](../Images/Charting_Kurtosis.gif)  
Image showing a high-kurtosis peak in red, and lower-kurtoses results in blue

Geometric Mean: the geometric mean is a type of average which is calculated by multiplying the n sample values together and then taking the nth root of the product. 

Sum of logs: the sum of the logs (base e) of the sample values.

Mean of logs: the mean of the logs (base e) of the sample values.

Logarithmic Variance: the variance of the logs (base e) of the sample values.

Log Estimate of Mean: an estimate of the arithmetic mean of the samples assuming a lognormal distribution.

Correlation Coefficient: this is a measure of the degree of linear correlation between two variables, here the Y Axis and X Axis field values. These two variables are said to be correlated if the scatter plot shows a significant rectilinear (straight line) trend. Correlation coefficient values range from -1 (a straight line with negative slope) to 1 (a straight line with positive slope). Both ends of this range indicate strong correlation between the variables; a lack of straight line correlation is indicated by values close to zero. The formula used to calculate the correlation coefficient (cc) is as follows:

cc = (N * ∑XY - ∑X*∑Y) / sqrt((N*∑XX - ∑X*∑X) * (N*∑YY - ∑Y*∑Y))  
  
where:  
  
N is the number of pairs  
∑X is the sum of the X values  
∑Y is the sum of the Y values  
∑XY is the sum of the product of X and Y  
∑XX is the sum of the product of X and X  
∑YY is the sum of the product of Y and Y

![note.gif \(1017 bytes\)](../Images/note.gif)| The value displayed here is the same in each of the Y Axis and X Axis columns as the value was calculated using from both sets of values; all the other statistics listed in the table are calculated separately for each axis.  
---|---  
  
5th ... 95th Percentile: the value of the variable (X Axis, Y Axis fields) below which a the Nth percent of the values fall; here these percentile values are calculated separately for each of the Y Axis and X Axis values.

## Changing the Formatting of Statistics

You can choose to enhance the display of your histogram to show vertical lines on the graph corresponding to the either the mean, log estimate mean, geometric mean and/or any values corresponding to any percentiles that have been selected. The Display Parameters Graphically option is used to enable or disable this facility. If selected, vertical lines are displayed in the selected color.

## Displaying the Statistics on the Chart

A range of parameters can be displayed, and if selected (i.e. the box is ticked), this information will be shown above each chart, aligned to the left border, e.g.:  
  
![](../Images/Chart_Scatter_Statistics%204.gif)

Select a check box on this panel to automatically update the preview with the relevant information. Note that the values to be displayed are shown in the green columns in the table, formatted to the define number of decimals (values displayed in the DECIMALS column).

By default, the displayed statistics are positioned top left - they can be repositioned by using the mouse cursor to click-and-drag.  

![openbook.gif \(910 bytes\)](../Images/openbook.gif)|  Related Topics  
---|---  
| [Scatter Plot Charts](<Chart_ScatterPlot.md>)[  
Scatter Plots - Data Selection](<Chart_ScatterPlot_DataSelection.md>)[  
Scatter Plots - Format](<Chart_ScatterPlot_Appearance.md>)[  
Scatter Plots - Charts](<Chart_ScatterPlot_Charts.md>)