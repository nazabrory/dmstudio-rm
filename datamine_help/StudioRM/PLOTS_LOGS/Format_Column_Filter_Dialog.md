![](../Images/HeaderCell.gif) |  Downhole Formatting: Filter Filtering how much downhole formatting is applied  
---|---  
  
# Overlay Formatting: Filter

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

The information in this article is relevant to both the Log View Properties \- [Columns](<Format%20Column%20Display%20Dialog.md>) tab and the [Format Downhole](<../VR_Help/DH_PropDialog_Columns_Format.md>) dialog (3D window formatting).

In either case, you access this screen by selecting the [Alignment] menu option, which is relevant to the following downhole formatting styles:

  * [Text](<../COMMON/Downhole_Columns_Format_Text.md>)
  * [Bars with Annotation](<../COMMON/Downhole_Columns_Format_Text.md>)
  * [Bars](<../COMMON/Downhole_Columns_Format_Text.md>)
  * [Braces with Annotation](<../COMMON/Downhole_Columns_Format_Text.md>)
  * [Ticks with Annotation](<../COMMON/Downhole_Columns_Format_Text.md>)
  * [Arrows with Annotation](<../COMMON/Downhole_Columns_Format_Text.md>)
  * [Line Graph](<../COMMON/Downhole_Columns_Format_Graphs.md>)
  * [Histogram](<../COMMON/Downhole_Columns_Format_Graphs.md>)
  * [Filled Histogram](<../COMMON/Downhole_Columns_Format_Graphs.md>)
  * [Trace](<../COMMON/Downhole_Columns_Format_Trace.md>)
  * [Angles](<../COMMON/Downhole_Columns_Format_Angles.md>)
  * [External Image File](<../COMMON/Downhole_Columns_Format_Images.md>)

The Filter menu allows you to set a filter that will be applied (only) to your downhole formatting. See "Drillholes, Object Filters, Columns and Column Filters", below, for more information.

![note.gif \(1017 bytes\)](../Images/note.gif) |  The settings described here apply to the currently active 3D window and all linked external windows. [Independent](<../COMMON/Independent_3D_Windows.md>) windows will be unaffected.  
---|---  
  
#  ![](../Images/StepByStep2.gif)

# Filter

  1. Enable the Filter check box to activate the filtering controls.

  2. Press the [Expression builder](<../expression%20builder.md>) button to enable the filter to be generated, or enter an expression directly into the editable field.

  3. Choose Apply to view changes.

### Drillholes, Object Filters, Columns and Column Filters

Drillhole data objects are often coupled with 'downhole column' data to provide more information about the drillhole data. This could be in the form of a histogram, listed grade values, braces, bar charts etc. Downhole columns are formatted separately (using this Format Column screen) from the actual 3D drillhole data (using the [Drillholes Folder](<../VR_Help/Sheets_Drillholes.md>)).

View filtering can be applied to any object in memory, including drillholes, to control the data that is displayed at any one time. This is controlled by a filter expression which can be defined by various methods, including the [Data Object Manager](<../COMMON/Data%20Manager%20Dialog.md>) or, to specifically filter drillhole data, using the [filter-drillholes](<../command_help/filter-drillholes.md>) command. Drillhole segments and downhole columns will always honour this object-level filter. If data does not pass the filter, neither it nor the associated downhole column data will be shown.

However, the situation is slightly more complex where a 'column' filter exists; all downhole columns can be associated with their own filter. In this case, 3D downhole formatting (the downhole 'column' will only be shown if it passes both the object-level and column-level filters. 

For example; if a drillhole object was filtered in the Data Object Manager to only show data where X>150, only column and drillhole data would be shown above the 150 position. If an AU downhole column was set to show results only where AU>1.0, downhole column data would only be shown grade values exceed 1.0 ppm and only for unfiltered data (above 150 in X).

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [3D Formatting: the Columns Tab](<../VR_Help/DH_PropDialog_Columns.md>)   
[3D Formatting: the Format Downhole dialog](<../VR_Help/DH_PropDialog_Columns_Format.md>) [Modify Angle template Style](<Modify%20Column%20Angle%20Style.md>)[  
Modify Graph template style](<LogColumnStyleGraph.md>)   
[Modify Trace template style](<../COMMON/Downhole_Columns_Format_Trace.md>) [Expression Builder Dialog](<../expression%20builder.md>) [Formatting columns (Tables)](<FormatColumn.md>)[  
Formatting columns (Section) (Plots)](<FormatHoleColumn.md>)[  
Formatting columns (Logs)](<FormatLogColumn.md>)