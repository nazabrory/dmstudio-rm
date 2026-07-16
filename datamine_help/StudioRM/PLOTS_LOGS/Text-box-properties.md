# Text Box Properties

To access this screen: 

  * Double-click the exterior border of a [text box](<TextBox.md>) on a plot sheet.

  * Right-click a text box plot item and select Properties.

Use this screen to set the formatting of a **[text box plot item](<TextBox.md>)**. 

Changes are applied automatically to the target plot item when changed. 

**Note** : Many of the formatting options below are also available on the **Text Box** ribbon, and via the **[Properties](<../COMMON/properties%20control%20bar%20overview.md>)** control bar.

General  
---  
Contents | The text that appears in the text box.  
Horizontal Alignment | The horizontal alignment of text within the text box cell.  
Word Wrapping | Choose if words wrap within the text box or not.  
Vertical Alignment | The vertical alignment of text within the text box cell.  
Sharing (see [Text Box Plot Items](<TextBox.md>))  
Share Properties |  Will any aspect of this text box be shared (linked with) the properties of another text box that shares the same ID?

  * _No_ All changes made to the target text box affect it only. Other text boxes are unaffected.
  * _Yes_ Share one or more aspects of this text box with other text boxes sharing the same ID.

  
Set ID | If **Share Properties** =_Yes_ , set the ID that will link other text boxes to this one.  
Horizontal Position | If **Share Properties** =_Yes_ , synchronize the horizontal position of this and all other text boxes sharing the same ID (providing they too are set to share properties).  
Vertical Position | As above, but shares the vertical position.  
Width | As above, but shares the width of the text box.  
Height | As above, but shares the height of the text box.  
Format | As above, but shares the visual formatting of the text box, including alignment.  
Contents | As above, but shares the textual content of the text box.  
Appearance  
Border | Choose the borders that will be displayed for the text box.  
Use parent colour | If _Yes_ , the system default colour (black) is used regardless of per-text box settings. If _No_ , the text box colour can be set.  
Colour | Set the colour of the borders and text of the text box  
Use parent font | If _Yes_ , per-text box settings applied are ignored in favour of the **[system default font](<../COMMON/Options_Plots.md>)**.  
Visible | Is the text box visible or not?  
Opaque | If _Yes_ , unfilled areas of the text box are opaque, otherwise data 'behind' the text box can be seen.  
Font  
Font | The font face, for example, Arial.  
Height | The height of the font in points.  
Bold | Make text elements **bold**.  
Underline | Make text elements _underlined_.  
Italic | Make text elements _italicized_.  
Position  
Width  | The overall width of the plot item.  
Height | The overall height of the plot item.  
X | The distance, in mm, from the left side of the plot item to the left side of the plot sheet.  
Y | The vertical distance from the top of the plot sheet to the top of the plot item.  
Rotation | The orientation of the text box in degrees, by default, 0.  
  
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

  * [Text Box Plot Items](<TextBox.md>)

  * [Text Box](<text%20box%20properties%20dialog.md>)

  * [Locatable Plot Items](<Locatable%20Plot%20Items.md>)

  * [Properties Control Bar](<../COMMON/properties%20control%20bar%20overview.md>)

  * [Drawing Order](<Format_Drawing_Order_Dialog.md>)