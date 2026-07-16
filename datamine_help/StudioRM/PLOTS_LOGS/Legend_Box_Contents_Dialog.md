# Legend Box

To access this screen:

  * Double click a [legend box plot item](<legendbox.md>) on a plot sheet.

  * Right click a legend box plot item and select **Legend Box Properties**.

The **Legend Box** screen is used to define the contents, layout and style properties for a [legend box plot item](<legendbox.md>). Typically, a legend box outlines the visual display legend for data within a projection, although it can also be useful to denote the structure of an evaluation legend for the purposes of reporting reserves.

The following tabs are shown:

  * Legend Box ContentsChoose a legend and configure its appearance. See below.
  * Drawing OrderUsed to determine at which point in the screen drawing process the current item is drawn to the screen. See [Drawing Order](<Format_Drawing_Order_Dialog.md>).

**Note** : Whilst legend boxes can be inserted into a plot sheet or projection, they aren't linked to 3D data, as their context is the legend, which can be created using the [Legends Manager](<../COMMON/FormatLegendsDialog.md>)'s array of tools.

### Legend Box Properties

The following settings can be applied to legend boxes using the **Legend Box** screen:

Legend Box Contents Tab  
---  
Legend | Choose a system, project or user legend to display on your plot sheet.  
Columns | Define the number of columns to be displayed in the legend box.  
Rows |  Choose which intervals of the legend to display. By default, Rows is equal to the number of legend intervals for the selected legend.  Reducing this number means later legend item intervals are not displayed.  
Show | 

  * FillCheck to display the fill colour for each legend interval, as defined using the **Legends Manager**.
  * LinestylesCheck to display the linestyle associated with each legend interval.
  * SymbolsCheck to display the symbol of each legend interval.

  
Grid | 

  * **Spacing** Define the spacing (pts) between adjacent legend items.
  * Draw LinesCheck to include grid lines between the displayed legend items.

  
Include Title Row |  Check to include a legend box title row (the default is the selected legend's name).  
Opaque | Check to prevent 'lower' plot items appearing through unfilled parts of the legend box (if the legend box is drawn after them - see [Drawing Order](<Format_Drawing_Order_Dialog.md>).  
Border | Check to draw a border around the displayed legend box.  
Colour | Choose the legend box border colour.  
Font | Choose the font used for text elements of the legend box.  
  
Note: These and other properties can be adjusted using the **[Properties](<Legend-box-properties.md>)** control bar.

Related topics and activities

  * [Legend Box Plot Items](<legendbox.md>)

  * [Legend Box Properties](<Legend-box-properties.md>)

  * [Plot Items](<LogPlotitems.md>)
  * [Plot Item Library](<plotitemlibrary.md>)

  * [Drawing Order](<Format_Drawing_Order_Dialog.md>)