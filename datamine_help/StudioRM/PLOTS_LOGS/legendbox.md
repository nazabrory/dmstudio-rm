# Legend Box Plot Items

A legend box is a special type of title block used to display the contents of a colour fill, pattern, line style or symbol legend. A legend box can be customized by changing its legend contents, size, number and size of rows and columns, and the legend title and border.

**Note** : This plot item can be drawn before or after other plot items, say to ensure it is shown on top of another one, using the **Drawing Order** tab. See [Drawing Order](<Format_Drawing_Order_Dialog.md>).

A legend box can be added to either the sheet or projection level of a plot sheet. See [The Plots Window](<../COMMON/Window_PLOTS_Overview.md>). Whilst Legend Boxes can be inserted into a plot sheet or projection, they aren't linked to 3D data, as their context is the legend, which can be created using the [Legends Manager](<../COMMON/FormatLegendsDialog.md>)'s array of tools.

## Plot Item Ribbons

Highlighting a plot item anywhere on a plot displays a dedicated ribbon containing various options for resizing, formatting and managing the contents of the target. All commonly-used properties can be accessed here and is generally the most convenient option for configuring plot items.

The options that appear depend on what you select. For example, selecting a [Title Box](<TitleBlock.md>) plot item displays a ribbon to let you manage the arrangement of cells within it, whilst selecting a **[North Arrow](<NorthArrow.md>)** item displays a different set of controls to determine the arrow's appearance:

[![](../Images/Plots_TitleBox-ribbon.png)](<javascript:void\(0\);>)

The Title Box ribbon

[![](../Images/PLots_NorthArrow-ribbon.png)](<javascript:void\(0\);>)

The North Arrow ribbon

**Note** : To return to more general plot management functions, activate the **Manage** ribbon. Plot item ribbons only display for as long as the plot item is selected.

**Note** : Deselect a plot item by holding <CTRL> and left clicking it.

### Add a Legend Box Plot Item

To add a legend box plot item to a plot sheet:

  1. Display the plot sheet to receive the new symbol.

  2. Click into the plot sheet (anywhere).

  3. **Manage** ribbon **> > Insert >> Plot Item**.

The **[Plot Item Library](<plotitemlibrary.md>)** displays.

  4. Select _Legend Box_ and click **OK**.

An empty legend box displays.

  5. Double-click the new legend box.

The **[Legend Box](<Symbol_Properties_Dialog.md>)** screen displays.

  6. Define the legend box's properties. See **[Legend Box Screen](<Legend_Box_Contents_Dialog.md>)**.

  7. Choose the drawing order for the plot item. See [Drawing Order](<Format_Drawing_Order_Dialog.md>).

  8. Click **OK**.

The legend box updates to reflect the latest settings.

### Edit Legend Box

To edit the general properties of an existing legend box:

  1. Double-click an existing legend box on a plot sheet.

The [Legend Box](<Legend_Box_Contents_Dialog.md>) screen displays.

  2. Edit the legend general properties and click **OK**. See [Legend Box Screen](<Legend_Box_Contents_Dialog.md>).

  3. Click **OK**.

The legend box updates.

  4. To change the height of the legend box, right click it and select **Legend Box >> Row Height** and choose the new height.

The legend box updates.

**Note** : You can also resize the legend box by enabling **Page Layout** mode (see below).

  5. To remove the final legend item from the displayed list, right click the legend box and select **Legend Box >> Delete Row**.

The final legend interval is removed from the display.

**Note** : This does not affect the legend, only the contents of the legend box.

  6. To add a new row to the end of the legend, right click the legend box and select **Legend Box >> Append Row**.

A legend interval is added to the end of the list. If an existing legend interval exists, it is displayed, otherwise, a blank row is added. For example, if your selected legend contains 8 intervals and you add nine rows, the ninth row is blank.

To change the columns used to display the legend box:

  1. Right click a legend box.

  2. Expand the **Legend Box** menu.

  3. To change the number of columns over which the legend box displays, choose either **Insert Column** or **Delete Column**. 

The legend box table updates and reorganizes itself to show the new column count.

**Note** : The size of text in each cell is automatically set by the program based on the maximum font size. For the best results, choose the font size that best suits the largest cell, typically the title in the first row, and the program will auto-size the text in the other, smaller cells.

### Move or Resize a Plot Item

To move or resize an existing plot item:

  1. Select the Manage ribbon and enable **Page Layout Mode**.

  2. Click to select the plot item. 

Resize boxes appear around the plot item.

  3. Ensure the **Lock** toggle on the plot item's ribbon is not active. If it is, deactivate it. If the **Lock** toggle is active, the height and width (and rotation) cannot be changed.

  4. To resize the plot item (and if supported, proportionally resize contents) drag one of the control points to a new position.

**Tip** : To retain the original aspect ratio of the plot item during resizing, hold down **CTRL**.

  5. To move the plot item, position the mouse inside the plot item until the cursor changes to a four-way arrow. Then, left-click and drag the plot item to a new position on the sheet.

**Note** : If a plot item is parented to another item, it can still be repositioned outside the boundary of its parent. For example, a title box associated with a projection can be positioned anywhere on the plot sheet, even outside the projection.

**Tip** : When moving a plot item, it will attempt to 'snap' to nearby objects. Override this behaviour by holding down SHIFT.

### Rotate a Plot Item

Plot items that display a green rotation symbol after selection can be rotated. 

To rotate a plot item:

  1. Select the Manage ribbon and enable **Layout Mode**.

  2. Ensure the **Lock** toggle on the plot item's ribbon is not active. If it is, deactivate it. If the **Lock** toggle is active, the height and width (and rotation) cannot be changed.

  3. Left click to select a plot item.

The resize and rotate controls display, for example:

![](../Images/RotatingPlotItems.gif)

  4. Left click and drag the green rotate control.

  5. Release the left mouse button to redraw the control at the new orientation.

**Tip** : Small plot item resize handles can blend into each other. **[Zoom in](<Zooming.md>)** to see each resizer more clearly.

Related topics and activities

  * [Legend Box Screen](<Legend_Box_Contents_Dialog.md>)

  * [Legend Box Properties](<Legend-box-properties.md>)
  * [Plot Items](<LogPlotitems.md>)

  * [Plot Item Library](<plotitemlibrary.md>)

  * [Drawing Order](<Format_Drawing_Order_Dialog.md>)