![](../Images/HeaderCell.gif) |  Projection Properties Dialog An explanation of fields and properties  
---|---  
  
# Projection Properties

### To access this dialog:

  * Right-clicking a projection item in the Sheets control bar, selecting Properties.

This summary dialog shows the properties of the currently selected projection.

Two tabs exist within this dialog - Properties and Drawing Order. The former outlines each property of the projection object, and is editable. The latter describes the point at which the selected projection is drawn to the screen when data is drawn to the viewing area. For more information on draw ordering, see [Formatting the Drawing Order](<Format_Drawing_Order_Dialog.md>).

![](../Images/Tip.gif) |  With regards to the Plots window (and to a lesser extent, the Logs window), much of the hierarchical structure of a particular sheet can be stored in template form. This minimizes the effort required to generate a consistent look and feel across a range of presentation projects by automatically generating a standard arrangement of sheets, projections and, if required, data object overlays. [Find out more about Plot Templates...](<PLOTS_Plot%20Templates.md>)  
---|---  
  
Field Details:

The Projection Properties dialog contains the following fields:

View Direction Settings

Align with section: you can set this to [Yes] to force the view direction of the projection window to line up with that of the current section definition.

Azimuth: set the azimuth of the projection's view direction.

Dip: set the dip of the projection's view direction.

Share: share the selected projection's view direction with other projections on the sheet. To activate this facility, more than one projection (at least) will need to have a [Yes] value specified for this property. Then, whenever the view direction is changed for any one of those projections, the direction will be updated in all other qualifying view areas.

View Direction: set the view direction by selecting a predefined description from the drop-down list.

View Centre Settings

Share: share the selected projection's view center setting with other projections on the sheet. All projections with a [Yes] value - on the same sheet \- will be updated if the view center is changed in any of those sections.

Use section mid-point: if set to [Yes] the center point as currently established by the section definition will be used to center the data view.

X/Y/Z: specify the center point of the view in 3D space.

Appearance

Opaque: setting this option "Yes" will make the selected projection obscure any projections that fall 'behind' it. If set to "No", the background for the selected projection will be transparent, enabling the view of data that is behind it.

Section Mid-point Settings

Easting: in this situation easting refers to the eastward measured distance (or the x-coordinate) of the section.

Level: The horizontal openings on a working horizon in a mine; these levels are typically accessed from a shaft and/or decline system. Levels are generally established at regular intervals, 10s of metres apart.

Northing: northing refers to the northward measured distance (or the y-coordinate) of the data section.

Section Orientation Settings

Azimuth: the azimuth of the current data section. Note that this is independent of view direction.

Dip: the orientation of the section with respect to a dip angle.

Section Orientation: the orientation of a section is set initially when a new sheet is added (Insert | Sheet | ...), but you can change it here at any time; you can either select a predefined alignment using a description from the drop-down list, or set a custom Azimuth and Dip value. Note that these values are automatically populated if a predefined orientation is selected.

Section Definition Settings

Section Number: the index number for the section being viewed in the current projection. You can use the up and down spin arrows to adjust this setting and automatically update the view.

Share: share the section definition with other projections on the sheet. The section definition can be [Shared], in which case any other projection that has the same [Shared] value will be updated whenever the section definition changes in any qualify projection (for example, making the section 'corridor' wider in one will make it wider in all shared projections).

Conversely, if set to [Not Shared], the section definition will not be updated if other projections are subjected to a section definition change.

The additional settings in this drop-down menu are important; [Consecutive] is a method by which a projection is automatically assigned a unique section number, normally one higher than the highest thus recorded on the sheet. For example, if all projections were set to this value, they could be set to section definitions 1,2 and 3 (or 2,3 and 4 etc.) - subsequent alterations to section 1 would affect 2 and 3, but consecutive sections would still be shown.

(This is a useful way of showing sections either side of a selected central slice in multi-projection sheets)

Finally, [Locked] will do just that; if set to [Yes], it will prevent any changes to the current section definition for the selected section, regardless of any commands run from the menu or command bar. Note that it is also possible to lock other aspects of a projection.

Title: an automatically generated (and non-editable) name for the currently active section.

Sections Table Settings

Use section table: if a section definition file is to be used but is not already loaded, select [Yes] and you will be prompted for the location of a file. If a section definition file is already in use, this field will automatically read [Yes]; this loaded file can be disabled by selecting [No].

Section Clipping Settings

Apply Clipping: clip objects within the selected project at section limits.

Share: share the clipping settings of the current projection with all other entities; either within the current sheet or all sheets. Alternatively you elect not to share these settings.

Position Settings

Height: the height, in pixels, of the current projection window.

Width: the width, in pixels, of the current projection window.

X: the X coordinate of the origin of the plot item.

Y: the Y coordinate of the origin of the plot item.

General Settings

Linked: If active, the view will select and display the same data selection. If the view is not live the selected data may not be visible.

For example, when a selection a window is synchronized, the selected hole is displayed in the log view in the second window, and the selected interval is displayed. The log view changes to display the selected hole because the log view is Live (see below). The selected interval is displayed because the log view is Linked.

Linked views can be synchronized so that changes to one view are instantly reflected in the other(s). For more information on this, see [Synchronizing Linked Views](<Synchronizing%20Linked%20Views.md>).

Live: modify the view so selected data becomes visible (see above for more information).

Scale Settings

Locked: Lock the current scale and disable the Scale fields (see below).

Scale: you can change the data scale by selecting a preset scale ratio from the drop-down list, or entering your own scale.

Share: in a multi-sheet data window (Plots, Logs, Tables or Reports \- for an overview of how sheets, projections and overlays are handled in your application, see [View Hierarchy](<../COMMON/View%20Hierarchy.md>)) you can elect to make the scale of the current object available to all sheets (and corresponding projections and overlays), the current sheet (only sharing the data across the projections and overlays relevant to the current sheet) or not shared at all (meaning the object data will only be available to the current sheet/projection/overlay combination.

View Exaggeration Settings

X/Y/Z: you can alter the exaggeration (distortion) of the selected projection in X, Y and/or Z directions, using these fields. By default, data will not be exaggerated (that is, it will be represented in a 1:1:1 ratio, maintaining the aspect ratio of the original data).

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [The Drawing Order tab](<Format_Drawing_Order_Dialog.md>)