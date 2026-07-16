# Legend Box Properties  
  
To access this screen: 

  * Display the **Properties** control bar and click a legend box in a plot sheet.

This screen is used to set the formatting of a [symbol plot item](<Symbols.md>). Changes are applied automatically to the target plot item when changed. 

**Note** : Some of the formatting options below are also available on the **Legend Box** ribbon, and the **[Legend Box](<Legend_Box_Contents_Dialog.md>)** screen.

General  
---  
Legend | Choose a system, project or user legend to display on your plot sheet.  
Fixed Size | Not used.  
X | The distance, in mm, from the left side of the plot item to the left side of the plot sheet.  
Y | The vertical distance from the top of the plot sheet to the top of the plot item.  
Width  | The overall width of the plot item.  
Height | The overall height of the plot item.  
Rotation | The orientation of the legnd box in degrees, by default, 0.  
Appearance  
Border | Check to draw a border around the displayed legend box.  
Grid | Choose if the legend box is arranged within a visible table grid.  
Outside Width | The width of the border surrounding the legend box.  
Inside Width | The width of the boundaries of internal cell borders.  
Opaque | Check to prevent 'lower' plot items appearing through unfilled parts of the legend box (if the legend box is drawn after them - see [Drawing Order](<Format_Drawing_Order_Dialog.md>).  
Font  
Font | The font face, for example, Arial.  
Height | The height of the font in points.  
Bold | Make text elements **bold**.  
Underline | Make text elements _underlined_.  
Italic | Make text elements _italicized_.  
Minimum Height | The minimum height permitted for the legend box when resizing.  
  
For more information on the following settings, see [Locatable Plot Items](<Locatable%20Plot%20Items.md>).

Location  
---  
Has Location | Is this a locatable plot item or not?  
Location Type | Only displayed if **Has Location** = Yes, set if the location is represented by a fixed point in 3D space (_Point_) or as a 3D line intersecting with other projections in 3D space (_Line_).   
Plot Position | Determines how the plot item is positioned in relation to its associated location, either as a _Fixed_ or _Relative_ position.   
Show Connector | If the plot item is located, and this is set to "Yes", an arrow connects the plot item to the associated position on the current plot. If set to "No" the arrow is not displayed.  
Line Width | If a connector is displayed, this is the width of the arrow.  
Arrow Size | If a connector is displayed, this is the width of the arrow head.  
Line Colour | The colour of a connector line, if one is displayed.  
Location Point 1 (if Has Location = _Yes_)  
X/Y/Z | The absolute position of the locator point in 3D space, or the first point of the line if the **Location Type** = _Line_.  
Location Point 2  
X/Y/Z | If **Location Type** = _Line_ , the world coordinates of the end point of the location line in 3D space.   
  
Related topics and activities

  * [Legend Box Plot Items](<legendbox.md>)

  * [Legend Box](<Legend_Box_Contents_Dialog.md>)

  * [Locatable Plot Items](<Locatable%20Plot%20Items.md>)

  * [Properties Control Bar](<../COMMON/properties%20control%20bar%20overview.md>)

  * [Drawing Order](<Format_Drawing_Order_Dialog.md>)