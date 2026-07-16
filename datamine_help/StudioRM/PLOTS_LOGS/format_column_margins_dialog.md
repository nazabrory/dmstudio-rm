![](../Images/HeaderCell.gif) |  Downhole Formatting: Width/Margins Setting the dimensions and padding of downhole formatting  
---|---  
  
# Overlay Formatting: Width/Margins

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

The Width/Margins menu is used to set up padding/margin for your downhole columns. This can be useful if you wish to push your downhole formatting away from the sample or the opposite and can also impact how graphs and other items are drawn. You can also use this to change one of the "... with Annotation" styles from one type to another, and to apply prefix and/or suffix symbols.

Margins are represented in the Drillhole Properties \- [Columns](<../VR_Help/DH_PropDialog_Columns.md>) tab as unfilled areas, e.g.:  
  
![](../Images/DrillholePrev2.jpg)

[More about margins...  
](<../VR_Help/DH_PropDialog_Columns.md>)

![note.gif \(1017 bytes\)](../Images/note.gif) |  The settings described here apply to the currently active 3D window and all linked external windows. [Independent](<../COMMON/Independent_3D_Windows.md>) windows will be unaffected.  
---|---  
  
#  ![](../Images/StepByStep2.gif)

  1. Set the Width excluding margins in millimeters. You should set this width first, before setting margins. If no margins are specified, you will not see a Width including margins field.

  2. If required, set the width of Left Margin and Right Margin and select a Width and a Style. The column width is automatically adjusted. The combined value of margins \+ un-margined distance is shown in the Width including margins read-only field. 

     * Adjusting the Width excluding margins will only update the Width including margins read-only field.

     * Adjusting the Left or Right margin value will maintain the Width including margins value, but will adjust the Width excluding margins value accordingly.

     * If you attempt to set a margin that cannot be fitted into the Width excluding margins, the alternate margin will be adjusted to accommodate.

  3. To apply prefix or suffix symbols within your left and/or right margin (a margin must be above zero to use one), use the Style drop-down list to select arrows, braces, lines, ticks or other combinations.

  4. Select a Margins Color or select the Same color as contents check box.

  5. Choose Apply to view changes.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [3D Formatting: the Columns Tab](<../VR_Help/DH_PropDialog_Columns.md>)   
[3D Formatting: the Format Downhole dialog](<../VR_Help/DH_PropDialog_Columns_Format.md>) [Modify Angle template Style](<Modify%20Column%20Angle%20Style.md>)[  
Modify Graph template style](<LogColumnStyleGraph.md>)   
[Modify Trace template style](<../COMMON/Downhole_Columns_Format_Trace.md>) [Formatting columns (Tables)](<FormatColumn.md>)[  
Formatting columns (Section) (Plots)](<FormatHoleColumn.md>)[  
Formatting columns (Logs)](<FormatLogColumn.md>)