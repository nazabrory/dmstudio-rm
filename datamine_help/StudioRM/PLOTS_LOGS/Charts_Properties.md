![](../Images/HeaderCell.gif) |  Chart Properties Managing chart properties  
---|---  
  
# Chart Properties

### To access this dialog:

  * In the Plots window, right-click a chart (i.e. Histogram, Scatter Plot, Variogram or Stereonet chart) and select ChartTypeProperties.

The Chart Properties dialog i.e. the Properties tab, is used to manage layout and appearance properties for the selected chart.

Field Details:

This dialog contains the following fields:

![note.gif \(1017 bytes\)](../Images/note.gif) |  The Plots window is automatically updated when any of the settings are changed.  
---|---  
  
General: this group contains general chart settings; these control which chart or page is displayed:

  * Number of Charts: read only; displays the total number of charts that can be found within the selected chart object.

  * Current Chart: select a chart number to define the currently displayed chart. For a compound chart, this will always be '1' as there will only be one 'chart' to show. For multiple-chart items where more than one data series has been isolated (according the key, value and/or weight fields), you can edit this field to show another chart in the range. If multiple charts exist, and a single chart from that range is displayed at any one time (that is, there is a single Row and Column \- see below), the Current Chart and Current Page values will always be identical (and will be updated automatically). Where multiple charts are displayed at once, within the same plot item, the Current Chart value will show the highest index number for all visible charts.

  * Current Page: select a page number to define the currently displayed page. For example, if 8 charts exist in a sequence and 2 charts are shown side-by-side within the same plot item (e.g. it has two Columns and one Row), there will be four pages in total.  
  
Note that you cannot enter a value greater than the Number of Pages field value (see below).

  * Number of Pages: read only; indicates the total number of individual chart pages available for display. This will be dependent on the number of charts, rows and columns that comprise the chart object.  
  
![](../Images/Chart_Hist_HistProp%202.gif)

  * Selectable: read only; defines whether the histogram chart is selectable or not.

Layout: this group contains a chart's layout settings; these control how many charts are displayed per page:

  * Rows: select a value to define how many rows are displayed per page. Used to display multiple-chart items.

  * Columns: select a value to define how many columns are displayed per page. Used to display multiple-chart items.

  * Gap: select a value (mm) defining the gap between the individual chart frames on a page; used in a multiple-frame layout.  

![note.gif \(1017 bytes\)](../Images/note.gif) |  If a value is set for either the Rows or Columns fields that generates a number of 'frames' that exceed the maximum number of charts, any unused frames will be left empty.  
---|---  

Appearance: this group contains general appearance settings:

  * Border: select [No](default) for no border; [Yes] to include a single-pixel border around the selected chart:  
  
![](../Images/Chart_Hist_HistProp%203.gif)

  * Visible: select [Yes](default) to make the chart visible; [No] to hide the chart.

  * Opaque: select [Yes](default) to make the chart opaque (i.e. background color set to white and not see-through), select [No] to set the background transparent ; generally used when charts are overlaid on other plots. The example below shows a chart overlaid on a plot of an open pit and topography wireframe - the chart on the left is transparent (Opaque='No'), that on the right is opaque:  
  
![](../Images/Chart_Hist_HistProp%204.gif)

Position: this group contains the settings for positioning and sizing a chart on a page:

  * X: select an X position (mm) for the top left corner of the chart (the default value is 25mm).

  * Y: select a Y position (mm) for the top left corner of the chart (the default value is 25mm).

  * Width: select a value (mm) for the width (horizontal extents) of the chart.

  * Height: select a value (mm) for the height (vertical extents) of the chart.  

![note.gif \(1017 bytes\)](../Images/note.gif) | 
    * The default values for the above settings allow a suitable margin for printing; when editing these values, make sure that a sufficient margin is left for printing and that the select page size is not exceeded.
    * Multiple individual charts can be placed on a single page and their positions (and sizes) customized using the Position settings.
    * The position and size of the chart can be set interactively using Page Layout Mode (Manage ribbon | Set to toggle this on or off)  
---|---  

## Laying out Multiple Charts on a Page

The Chart Properties dialog can be used to define the layout of multi-chart objects, showing them either as individual charts spread across many pages, or as multiple charts on one (or potentially more) pages.

By default, when you create a new chart sheet (or insert a chart as a plot item), a single chart is displayed per page. This chart will reflect the settings defined in the [Histogram](<Chart_Histogram.md>) or [Scatter Plot](<Chart_ScatterPlot.md>) dialogs.

The Chart Properties dialog offers the choice of creating multiple charts (representing multiple data series) or a single, compound chart showing all results on one sheet. A compound chart will, by definition, always be a single 'page', however, multiple charts are handled by a single chart 'object' in memory using independently accessible pages.

For example, if the Individual Charts option is selected in the Histogram dialog, and the Value/Key/Weight fields that have been selected give rise to four separate charts (for example, if one X Coordinate Value Field is selected, and one LITHKey Field containing four unique values), these charts will be created separately, and can be accessed individually using the [Charts](<Chart_Histogram_Charts.md>) tab. For this 4-chart object, setting the Columns to '2' and the Rows to '2' will permit all four charts to be displayed on one sheet, as shown below (the Pages property will automatically be set to '1'):

![](../Images/Chart_Hist_HistProp%205.gif)

If for this 4-chart object, Columns is set to '1' and Rows to '1' (the Pages property will automatically be set to '4'), only one chart will be displayed on the sheet. In the image below, only the selected chart is shown:

![](../Images/Chart_Hist_HistProp%206.gif)

In this configuration, the chart object is displaying one of several 'pages'.