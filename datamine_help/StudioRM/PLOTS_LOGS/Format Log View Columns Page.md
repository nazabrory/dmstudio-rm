# Format Log Columns  
  
To access this screen:

  * Display the [Log View Properties](<Log-View-Properties.md>) screen and select the **Columns** tab.

Define downhole columns that sit alongside either strip log information or a loaded drillhole object. 

This screen differs from the **Format Downhole** screen in that this log sheet-specific instance contains a list of attributes that can be used to define [log sheet](<../COMMON/Window%20Overview_%20Logs.md>) formatting, whereas in the 3D window equivalent, an attribute is selected from a static or dynamic drillhole object beforehand. Otherwise the functionality is very similar.

Note: The other difference is that a log sheet can only display information for a [dynamic](<../COMMON/Drillhole%20Representation%20in%20Studio.md#dynamic>) drillhole, whereas the **Format Downhole** screen can be used to configure formatting for both [static](<../COMMON/Drillhole%20Representation%20in%20Studio.md#static>) and dynamic drillhole types.

###  Formatting Styles

The following display styles are available for 3D downhole columns. Access them via the Style menu at the top of the **Format Downhole Column** screen:

Style |  Description |  Example |  More Information |  Property Help  
---|---|---|---|---  
Text |  Textual attribute values (numeric or alphanumeric, displayed down the hole). |  ![](../Images/DHColumns_Text.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Text.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Bars with Annotation |  Coloured (filled) bars and text overlay |  ![](../Images/DHColumns_BarsWithAnnotation_110x110.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Text.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Bars |  Coloured (filled) bars |  ![](../Images/DH_Bars_111x104.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Text.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Braces with Annotation |  Text annotation with brace style connector. |  ![](../Images/DH_BracesWithAnnotation_111x111.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Text.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Ticks with Annotation |  Text annotation with tick style connector.  |  ![](../Images/DH_TicksWithAnnotation_110x97.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Text.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Arrows with Annotation |  Text annotation with arrows style connector.  |  ![](../Images/DH_ArrowsWithAnnotation_111x89.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Text.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Line Graph |  Unfilled line graph for Text annotation with brace style connector.  values |  ![](../Images/DH_LineGraph_112x104.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Graphs.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Graph/Color](<Format_Column_Graph_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Histogram |  Unfilled histogram for numeric values |  ![](../Images/DH_Histogram_111x103.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Graphs.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Graph/Color](<Format_Column_Graph_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Filled Histogram |  Filled histogram for numeric values |  ![](../Images/DH_FilledHistogram_111x101.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Graphs.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Graph/Color](<Format_Column_Graph_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Trace |  Show parallel trace using any attribute legend or color |  ![](../Images/DH_Trace_113x100.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Trace.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Trace](<Format%20Column%20Trace%20Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
Angles |  Show numeric values as angles (higher numbers show more severe angle deviation from hole) |  ![](../Images/DH_Angles_113x81.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Angles.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
External Image File |  Show predefined images per hole or interval alongside the sample |  ![](../Images/DH_Images_113x92.jpg) |  [Click here](<../COMMON/Downhole_Columns_Format_Images.md>) |  [Alignment](<Format_Column_Alignment_Dialog.md>) [Border/Color](<Format_Column_Borders_Dialog.md>) [Filter](<Format_Column_Filter_Dialog.md>) [Image](<../VR_Help/DH_PropDialog_Columns_Image.md>) * [Text](<Format_Column_Text_Dialog.md>) [Width/Margins](<format_column_margins_dialog.md>)  
  
* See [Adding Images to your Drillhole Display](<../COMMON/Downhole_Columns_Format_Images.md>) for instructions on how to configure downhole images for loaded drillhole data.

## Format Log Columns

  1. Display the **Columns** screen.

  2. Using the Columns in View list, select an attribute to format.

  3. Format the column using one of the available options:

     * Up/Down Adjust the position of the highlighted column in the Columns in View list (see above). If your data column is set to Overlap previous column, it will always overlap the column immediately above it in the list. Columns are drawn in a left-right order on the sheet (corresponding to up-down in the Columns in View list) so reordering here can be used to change the position of the log column on the sheet.

     * Delete Remove the column selected in the Columns in View list.

     * Add Add a new column to the log sheet, using the [Column Wizard](<addlogcolumn.md>).

     * Copy Add a copy of the selected column. Each copy is added to the bottom of the Columns in View list, but can be reordered (see above).

     * Rename Rename a log sheet column. If the [Column Names Row](<column%20titles%20dialog.md>) is used in log sheet formatting (for example, the title), the column width is automatically adjust to accommodate it 

     * Reset Reset the log sheet to show only the default columns.

     * Font Use the Font screen to set the font style.

Related topics and activities:

  * [Adding and removing log columns](<addlogcolumn.md>)

  * [Formatting log columns](<FormatLogColumn.md>)

    * [Alignment](<Format_Column_Alignment_Dialog.md>)

    * [Border/Color](<Format_Column_Borders_Dialog.md>)

    * [Filter](<Format_Column_Filter_Dialog.md>)

    * [Graph/Color](<Format_Column_Graph_Dialog.md>)

    * [Text](<Format_Column_Text_Dialog.md>)

    * [Width/Margins](<format_column_margins_dialog.md>)

    * [Trace](<Format%20Column%20Trace%20Dialog.md>)

  * [Formatting header and footer](<FormatHeader.md>)

  * [Format Downhole Dialog](<../VR_Help/DH_PropDialog_Columns_Format.md>)