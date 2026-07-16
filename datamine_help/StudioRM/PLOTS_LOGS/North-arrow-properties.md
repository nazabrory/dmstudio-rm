# North Arrow Properties  
  
To access this screen: 

  * Display the **Properties** control bar and click a north arrow in a plot sheet.

This screen is used to set the formatting of a **[north arrow plot item](<NorthArrow.md>)**. Changes are applied automatically to the target plot item when changed. 

**Note** : Many of the formatting options below are also available on the **North Arrow** ribbon.

Arrow  
---  
Visible |  Is the arrow visible or hidden?  
3D | Is the arrow component of the north arrow displayed in 'flat' 2D or oriented in 3D to align with the section's view direction?  
Colour | Set the colour of the arrow component.  
Bold | Choose if thick (Yes) or thin (No) lines are used for the arrow graphic.  
Size |  The size of the arrow in pixels.  
Aspect | Choose the aspect ratio of the arrow graphic. Values from 1-5 are accepted where 1= thinnest and 5 = widest. 3 is the default.  
Label  
3D | Is the label component of the north arrow displayed in 'flat' 2D or oriented in 3D?  
Colour | Set the colour of the label component.  
Font | The current font face of the arrow label.  
Caption | The text of the label.  
Keep Upright |  Choose if the label always appears upright.   
Offset |  The distance between the 'origin' of the arrow and the text to be displayed.   
Position  
X | The distance, in mm, from the left side of the plot item to the left side of the plot sheet.  
Y | The vertical distance from the top of the plot sheet to the top of the plot item.  
Width  | The overall width of the plot item.  
Height | The overall height of the plot item.  
Rotation | Not used - value changes have no effect on the plot item.  
Appearance  
Visible | Is the plot item visible (both components) or not?  
Opaque | Choose if the unfilled parts of the plot item are 'see through' or not.  
  
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

  * [North Arrow Plot Item](<NorthArrow.md>)

  * [Locatable Plot Items](<Locatable%20Plot%20Items.md>)

  * [Properties Control Bar](<../COMMON/properties%20control%20bar%20overview.md>)

  * [Drawing Order](<Format_Drawing_Order_Dialog.md>)