![](../Images/HeaderCell.gif) |  Formatting Downhole Columns Changing the way drillholes are displayed/interpreted  
---|---  
  
# Formatting downhole columns

Choose theManageribbon and selectFormat | Overlays to:

  * Add or remove downhole columns. 

  * Change the order of columns.

  * Change the display style of a selected column.

  * Overlap columns, e.g. line graph over text or structure over lithology, for greater presentational impact.

  * Change the width and scale of columns.

  * Change the alignment of text and axis direction of graphs.

  * Select a fixed color or a user defined color legend for text and lines.

  * Select a fixed color, color legend or pattern legend for graph, box and histogram fills.

Drillholes, Object Filters, Columns and Column Filters

Drillhole data objects are often coupled with 'downhole column' data to provide more information about the drillhole data. This could be in the form of a histogram, listed grade values, braces, bar charts etc. Downhole columns are formatted separately (using the [Format Column Display Dialog](<Format%20Column%20Display%20Dialog.md>)) from the actual drillhole data (which uses the [Traces as Holes](<format%20traces%20dialog.md>) dialog).

View Filtering can be applied to any object in memory, including drillholes, to control the data that is displayed at any one time. This is controlled by a filter expression which can be defined by various methods, including the [Data Object Manager](<../COMMON/Data%20Manager%20Dialog.md>) or, to specifically filter drillhole data, using the [filter-drillholes](<../command_help/filter-drillholes.md>) command.

Drillhole segments and downhole columns will always honor this object-level filter. If data does not pass the filter, neither it nor the associated downhole column data will be shown.

However, the situation is slightly more complex where a 'column-specific' filter exists. All downhole columns can be associated with their own filter (using the [Filter tab on the Format Columns dialog](<Format_Column_Filter_Dialog.md>)). In this case, an aspect of the downhole column will only be shown if it passes both the object-level and column-level filters. For example; if a drillhole object was filtered in the Data Object Manager to only show data above the X value 150, only column and drillhole data would be shown above the 150 position. If an AU column was set to show results only where the grade surpasses the 1.0 grade cut-off point, downhole column data would only be shown above 150 in X and where grade values exceed 1.0 ppm.

##  ![](../Images/StepByStep2.gif)

## To add a new column

  1. Choose the Manage ribbon and select Format | Overlays

  2. Choose the **Add** button adjacent to the **Columns in View** box to start the Column Wizard.
  3. Choose whether you wish to add a **Data Column** or a calculated **System Field** and select Next.  
  
**Select Column Type**| **To display**| **Example**  
---|---|---  
Data Column| All downhole sample data from all data tables e.g. grades and lithology codes.| Use this column type to display any of the original data fields from the imported tables.  
System Field| Computed field values like downhole depth, inclination, dip and coordinates of the desurveyed trace.| Use this column type to graph, say, how the azimuth of the hole trace varies downhole.  
  4. Select a **table** to define the sample interval for the column and select **Next**.  
  
**Note** that the table selected need not contain the fields you wish to display. For example, by choosing the lithology table here, and a grade field from the assays table in the next step, a **composited field** is created i.e. the selected grade field is composited over the sample intervals defined by the selected table.

  5. Select one or more **fields** you wish to add using the same display style.

  6. If a composited field has been defined (the selected _table_ does not contain the selected _fields_), select the **Compositing Mode** , **Weighting Method** and **Compositing Parameters** and choose Next.
  7. Finally select the **style** which you want to apply to the columns.
  8. Select **End** to add the columns to the **Columns in View** box.
  9. Select a column in the **Columns in View** box and choose the **Up** and **Down** buttons to change the plotting order.
  10. Choose **Apply** to view the changes or **OK** to close the dialog.

## To change the display style of a column

  1. Choose theManageribbon and selectFormat | Overlays

  2. Select the column name in the **Columns in View** box.
  3. Select the **Style Templates** tab dialog to display the current display style. The **Customized style** box indicates whether the default template style has been modified. Uncheck the Customized style box to reset the style to the original template settings.
  4. Select the column display style required from the **gallery** of pre-defined styles. Settings on the other style tabs will be modified according to the selected template.
  5. View and modify the style settings on the other tabs as required.
  6. Choose **Apply** to view the changes or **OK** to close the dialog.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Graph and Histogram styles](<LogColumnStyleGraph.md>)[  
Trace style](<LogColumnStyleTrace.md>)[  
Angle Style](<Modify%20Column%20Angle%20Style.md>)[  
Formatting drillhole traces](<FormatHoles.md>)