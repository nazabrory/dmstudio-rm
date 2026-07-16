![](../Images/HeaderCell.gif) |  Displaying Parameter Profiles Controlling the use of parameter profiles in section views  
---|---  
  
# Parameter surface profiles

3D objects with Z coordinates which define parameters other than the elevation, for example a surface model derived from soil sampling or gravimetric surveys, can be displayed inside a profile box. The Z coordinate of each parameter surface is scaled to fit the vertical axis of the profile box. Any number of 3D objects can be displayed in a single profile box, and more than one profile box can be inserted on the same page.

Profile boxes may be positioned anywhere on the page, either inside, outside or overlapping the data area. The horizontal position in the profile box is tied vertically to the corresponding horizontal position in the data area. The surface profiles are automatically updated whenever:

  * the profile box is moved or resized;

  * the data area is moved or resized;

  * the scale in the data area is changed;

  * the data area is panned horizontally;

  * the section is rotated or repositioned.

A profile box is a plot item, and so you must select theManageribbon andLayout | Layout Mode before you can insert, select or edit a profile box.

##  ![](../Images/StepByStep2.gif)

## To insert a new profile box

  1. Using theManageribbon, selectInsert | Profile from the Plots window.

  2. Select OK on the [Profile Plot Box](<profile_plot_dialog.md>) dialog.

  3. A new empty profile box is placed in the top left corner of the page. The profile box can be moved and resized by selecting with the pointer.

## To move and re-size a profile box

  1. In Page Layout mode, select the profile box with the pointer.

  2. Click-and-drag the profile box to another position on the page, or edit the X and Y values in the [Properties](<profile_plot_dialog.md>) window.

  3. To resize click-and-drag one of the re-sizing handles on the border of the box or edit the Width and Height values in the [Properties](<profile_plot_dialog.md>) window.

## To add a 3D object (surface) to a profile box

  1. In Page Layout mode, select the profile box with the pointer.

  2. Double-click on the new profile box to display the [Profile Plot Box](<profile_plot_dialog.md>) dialog.

  3. Choose the Data Objects tab. The 3D Objects available are displayed in the Objects and Fields box.

  4. Select the object you wish to add to the profile box and expand to show the object fields.

  5. Select the field name which defines the parameter modelled by this surface (Z coordinate) and choose the Add button to add the field/object to the Current Profiles box. More than one parameter may be displayed in a profile box.

  6. Click OK.

## To format the display of a profile box

  1. In Page Layout mode, select the profile box with the pointer.

  2. Double-click on the profile to display the [Profile Plot Box](<profile_plot_dialog.md>) dialog.

  3. Choose the [Profile Box Properties](<format%20profile%20box%20properties%20dialog.md>) tab to display the current format settings.

  4. Edit the format settings in the Border, Fill and Size boxes.

  5. Choose the Font button the change the current font style and size.

  6. Choose OK to close the dialog.

## To format the display of a profile trace

  1. In Page Layout mode, select the profile box with the pointer.

  2. Double-click on the profile to display the [Profile Plot Box](<profile_plot_dialog.md>) dialog.

  3. Choose the [Data Objects](<profile%20plot%20box%20dialog.md>) tab and select the parameter (field/object) from the Current Profiles box.

  4. Choose the Properties button adjacent to the Current Profiles box to display the format settings for the selected parameter.

  5. Edit the format settings in the Label, Trace and Limits boxes.

  6. Choose OK to return to the [Profile Plot Box](<profile_plot_dialog.md>) dialog and select another profile.

  7. Choose OK to close the dialog.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Displaying terrain profiles in section views](<DisplayTerrain.md>)