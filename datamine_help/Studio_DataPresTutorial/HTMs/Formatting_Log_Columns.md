![](../HeaderCell.jpg) |  Formatting Log Columns Formatting the log sheet data columns.  
---|---  
  
# Overview

In this portion of the tutorial you are going to format the log sheet data columns. Formatting log column data includes setting the following (where relevant) for each data column displayed in the log sheet:

  * Style Templates \- select a data display style e.g. Text, Bars, Line Graph, Histogram, Trace, Angles

  * Graph \- if relevant, define data minimum, maximum and scale settings

  * Color \- define fixed color or legend color and fill options

  * Text \- set text display style, format, font size and color options

  * Alignment \- define vertical and horizontal alignment options

  * Border \- select cell border positions and color options

  * Width/Margins \- set column width, margin and margin color options

  * Axes \- define axes labels position, lines and label interval

  * Filter \- define optional data filtering

## Prerequisites

Required:

  * Opened and saved a copy of the project file Data Presentation Tutorial.StartPoint.dmproj \- see exercises under the [Opening and Saving Projects](<Opening%20and%20Saving%20Projects.md>) page.

  * Inserted a new VB2675 Log sheet - see exercises on the [Opening, Copying and Inserting Log Sheets](<Opening_Copying_and_Inserting_Log_Sheets.md>) page.

  * Selected the hole VB2737 in the newly inserted log sheet - see exercise on the [Selecting Drillholes](<selecting_drillholes.md>) page.

Recommended:

  * Modified the log View settings for the VB2737 Log sheet - see exercise on the [Modifying Log View Settings](<Modifying_Log_View_Settings.md>) page.

  * Displayed the relevant Columns in the VB2737 Log sheet - see exercise on the [Displaying Log Sheet Column Data](<Displaying_Log_Sheet_Column_Data.md>) page.

  * Formatted the Hole Log Frame in the VB2737 Log sheet - see exercise on the [Formatting the Hole Log Frame](<formatting_the_hole_log_frame.md>) page.

  * Formatted the Log Header, Column Titles and Footer in the VB2737 Log sheet - see exercise on the [Formatting the Log Header, Column Titles and Footer](<formatting_the_hole_log_header_and_footer.md>) page.

## Exercise: Formatting Log Columns

In this exercise, you are going to modify the columns' formats in the VB2737 log sheet. This includes modifying the following:

  * Depth At and Elevation columns text font
  * NLITH column text and color
  * LITH column style and text
  * DENSITY column axes labels
  * AU column display style and color
  * CU column display style and color
  * ZONE column display style and margins

**Modifying the Depth At and Elevation Columns Text Format**

  1. Select the Logs window.

  2. Select the VB2737 log sheet tab.

  3. Left-click anywhere within the Log View to show the surrounding frame as a dotted line, then right click to select  Hole Log Frame (VB2737) Properties Select _L og_ | _H_ ole... .

  4. In the Log View Properties dialog, select the Columns tab.

  5. In the Columns in View pane, select [Depth At].

  6. In the Style Templates subtab, check that the style is set to [Ticks with annotation].
  7. In the Text sub-tab, Font Size group, clear the Use Defaults check box, select the font size [6] pts.
  8. In the Number Format group, select the Decimal Places check box and select [1].
  9. In the Color group, select the Fixed Color option, select the color [Black].
  10. In the Alignment sub-tab, clear the Use Default Alignment check box, select the Horizontal option [Centre].
  11. In the Log View Properties dialog, click Apply (do not close the dialog).
  12. In the VB2737 log sheet, check that the Depth At column text has been modified, as shown below:  
  
![](../Images/Plot17.jpg)  
  

  13. Repeat steps 4 to 11 for the Elevation column, using the same style, alignment, font size, number of decimal places and color.
  14. In the VB2737 log sheet, check that the Elevation column text has been modified, as shown below:  
  
![](../Images/Plot18.jpg)

**Modifying the NLITH column Text and Color formats**

  1. In the Columns in View pane, select [NLITH].
  2. In the Style Templates sub-tab, select [Bars].
  3. In the Text sub-tab, tick the Show Text checkbox.
  4. In the Font Size group, clear the Use Defaults check box, select the font size [8] pts.
  5. In the Color group, select the Fixed Color option, select the color [Black].
  6. In the Border/Color sub-tab, Fill group, select the Fill check box.
  7. Select the Color using legend option, select the Column [Lithology$_vb_lithology.NLITH], click Use Default Legend.  
  
![note.gif \(1017 bytes\)](../images/note.gif)| When selecting columns in the Column dropdown and legends in the Legend dropdown, use the relevant keyboard letters A-Z to step through the menu items.  
---|---  
  8. In the Log View Properties dialog, click Apply (do not close the dialog).
  9. In the VB2737 log sheet, check that the modified NLITH column is formatted as shown below:  
  
![](../Images/Plot19.jpg)

**Modifying the LITH column Style and Text formats**

  1. In the Columns in View pane, select [LITH].
  2. In the Style Templates sub-tab, select [Text offset to prevent overlaps].
  3. If the message dialog 'Warning. Format will be reset...' is displayed, click Yes.
  4. In the Text subtab, Font Size group, clear the Use Defaults checkbox, select the font size [6] pts.
  5. In the Color group, select the Fixed Color option, select the color [Black].
  6. In the Log View Properties dialog, click Apply (do not close the dialog).
  7. In the VB2737 log sheet, check that the modified LITH column is formatted, as shown below:  
  
![](../Images/Plot20.jpg)

**Setting the DENSITY column Axes Labels**

  1. In the Columns in View pane, select [DENSITY].
  2. In the Axes sub-tab, Label Axes group, select the Top check box.
  3. In the Axis Label Interval group, clear the Automatic checkbox and select the interval [1].
  4. In the Log View Properties dialog, click Apply (do not close the dialog).
  5. In the VB2737 log sheet, check that the modified DENSITY column is formatted, as shown below:  
  
![](../Images/Plot21.jpg)

**Modifying the AU column Style and Text formats**

  1. In the Columnsin View pane, select [AU].
  2. In the Style Templates sub-tab, select [Filled Histogram].
  3. In the Graph/Color sub-tab, Color group, select the option Color Using Legend, select the Column [Assays$_vb_assays.AU], click Use Default Legend.
  4. Click Show Legend.
  5. View the legend preview in the Legend dialog, close it.  
  
![](../Images/dp_Formatting%20Log%20Columns%206.jpg)  
  
![note.gif \(1017 bytes\)](../images/note.gif)| Legends can be created and customized using the Format ribbon's Format Legends commandFormat |Legends.... For more information on legends, please see the Help documentation, the Geological Modeling and Underground Design tutorials.  
---|---  
  6. Back in the Log View Properties dialog, Axes sub-tab, Label Axes group, select the Top checkbox.
  7. In the Axis Label Interval group, clear the Automatic check box, select the interval [5].
  8. In the Log View Properties dialog, click Apply (do not close the dialog).
  9. In the VB2737 log sheet, check that the modified AU column is formatted, as shown below:  
  
![](../Images/Plot22.jpg)

**Modifying the CU column Style and Text formats**

  1. In the Columns in View pane, select [CU].
  2. In the Style Templates subtab, select [Line Graph].
  3. If the message dialog 'Warning. Format will be reset...' is displayed, click Yes.
  4. In the Graph/Color sub-tab, Color group, select the Color Using Legend option, select the Column [Assays$_vb_assays.CU], click Use Default Legend.
  5. In the Axes sub-tab, Label Axes group, select the Top option, select the Vertical Lines option.
  6. In the Axis Label Interval group, clear the Automatic checkbox, select the interval [5].
  7. In the Log View Properties dialog, click Apply (do not close the dialog).
  8. In the VB2737 log sheet, check that the modified CU column is formatted, as shown below:  
  
![](../Images/Plot23.jpg)

  

![](../Images/NextExercise.gif)[Proceed to the next topic](<Inserting_Log_Sheet_Plot_Items.md>)