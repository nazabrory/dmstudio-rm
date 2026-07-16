![](../Images/HeaderCell.gif) |  Histograms - Format Customizing the appearance of your histogram  
---|---  
  
# Histograms - Format

### To access this dialog:

  * Open the [Histogram](<Chart_Histogram.md>) dialog, select the Format tab.

This Format tab is used to control the histogram model, bin size, grid, axes and color parameters.

Field Details:

The Format tab is comprised of the following fields:

Model: this group contains the histogram model controls:

  * Fit Model on All Charts: select this option to fit and display histogram models on all listed histogram charts.  

![note.gif \(1017 bytes\)](../Images/note.gif) |  Each model's parameter set can be edited using the [Fit Model](<Chart_Histogram_FitModel.md>) dialog.  
---|---  

Custom Bin Size: select this option to define custom bin size values:

  * Bin Size for All Charts: define a bin size value.  
  

![note.gif \(1017 bytes\)](../Images/note.gif) |  How is the Default Bin Size Calculated? For a Normal chart type, using theScott's choiceformula: Bin Size = 3.5*s/n1/3, where s is the standard deviation and n the number of samples. The bin size value is rounded down to a 'sensible' value. For a Log chart type: Log Bin Size = (Log(Maximum Value) Log(Minimum Value)) / (Default Number of Bins for the Normal Histogram) If using the custom bin size option, as a general rule of thumb, check the resultant bin size so that when the number of data values is:
    * under 50, use five to seven bins,
    * 50 to 99, use six to 10 bins,
    * 100 to 249, use seven to 12 bins,
    * 250 and over, use 10 to 20 bins.  
---|---  

Grid: select the grid line Style and Colour parameters for the X and Y axes using the drop-down lists.

Axes: use this group to select either default or custom axes options and their parameters:

  * Use Default Axis: select this option to use default X and Y axis minimum, maximum and interval options for all charts.

  * Use Custom Axis: select this option to define custom minimum, maximum and interval options for each Chart Type.

Chart Type: from the Chart Type drop-down list, select a chart for custom axes definition. This drop-down is only available if the Use Custom Axis option is selected.

![note.gif \(1017 bytes\)](../Images/note.gif)| The drop-down lists the available charts, as selected in the Chart Types group on the Data Selection tab. In the example shown below, the selection results in three items being listed in the drop-down list i.e. [Histogram], [Probability Plot] and [Log Probability Plot].![](../Images/Chart_Hist_Format%203.gif)  
---|---  
  
Custom Axes: for each Chart Type. , define the corresponding custom axes parameters:

The fields below are automatically populated with suggested values to ensure that all graph details are initially visible:

X Axis: select this option to define the custom X axis parameters

Y Axis: select this option to define the custom Y axis parameters

Minimum: set the minimum value for the corresponding axis. This must be a numeric value that is less than the Maximum.

Maximum: set the maximum value for the corresponding axis. This must be a numeric value that is greater than the Minimum.

Interval: enter the interval spacing between value labels on the corresponding axis. This parameter cannot be customized for Y axes intervals.

If the custom axis option is used, it is possible to create a value range that does not include all values in the selected object or file. In this situation, you can control how these values are handled (ignored or pushed into the first/last bin) using the [Data Selection](<Chart_Histogram_DataSelection.md>) tab. If values are changed, clicking Apply will update the chart preview using the new settings.

![](../Images/Chart_Hist_Format%202.gif)  

Color Palette: chart histogram color settings.

  * Individual Charts: select a color palette for individual charts from the drop-down.

  * Compound Chart: select a color palette for compound charts from the drop-down.

Charts Annotation Size: select this option to define custom annotation font size settings.

  * Title: select a font size from the drop-down.

  * Legend: select a font size from the drop-down.

  * X Axis: select a font size from the drop-down.

  * Y Axis: select a font size from the drop-down.

Options: additional histogram chart formatting controls.

  * Display Data Set Name in Histogram Title: select this option to display the loaded data or data file name as a suffix in the histogram title.  

![note.gif \(1017 bytes\)](../Images/note.gif)| The histogram title can be edited using the [Histogram Properties](<Chart_Histogram_ChartProperties.md>) dialog.  
---|---  

![openbook.gif \(910 bytes\)](../Images/openbook.gif)|  Related Topics  
---|---  
| [Histograms](<Chart_Histogram.md>)[  
Histograms - Data Selection](<Chart_Histogram_DataSelection.md>)[  
Histograms - Preview](<Chart_Histogram_Preview.md>)[  
Histograms - Chart Parameters](<Chart_Histogram_ChartProperties.md>)[  
Histograms - Fit Model](<Chart_Histogram_FitModel.md>)