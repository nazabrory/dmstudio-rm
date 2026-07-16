# Plots Window Menus  
  
The [Plots](<../COMMON/Window_PLOTS_Overview.md>) window features a context-menu system to perform operations on window items using a right-click menu. 

In general, there are two different menu types:

  * With [Page Layout](<PageLayoutMode.md>) mode activatedConfigure individual plot items, including projections of data. 

  * With **Page Layout** mode deactivatedConfigure plot items providing the layout of the plot is unaffected. In this mode, you can also set general sheet-level properties.

## Page Layout Mode Active

If **Page Layout** mode is active, the contents of a right-click menu depends on what you target (for example, if a _Clip Art_ plot item is selected, you can rotate and flip it, whereas if a _Projection_ is selected, you can scale and pan the underlying data and view, amongst other things. 

In this mode, you can make changes that affect the layout of the sheet and format its components.

### Plot Sheet Menu

Right-clicking the border of a plot sheet shows the highest-level context menu:

[Sheet Name] Properties | Format the [Page Size](<page%20size%20dialog.md>) and [Drawing Order](<Format_Drawing_Order_Dialog.md>) of items within the current sheet.  
---|---  
Insert | Displays the [Plot Item Library](<plotitemlibrary.md>), featuring the full set of possibly plot items, including new projections.  
Copy from [3D window] |  Copy the current plot sheet to the clipboard.  **Note** : To paste a copied plot sheet, right-click the top-level **Plots** item in the **Sheets** or **Project Data** control bar and select **Paste**.  
Paste [Plot Item] |  If a plot item has been copied to the clipboard it can be pasted, if the target plot component supports it. For example, you can copy a text box from any plot sheet and paste it at the sheet or projection level of another sheet, but you can only paste a scale bar into a projection (as a 3D data context is required).  
Wizard... | Open the Plot (or Log) Section Wizard to define the top level settings   
Redraw Dynamically | If **checked** , data views are automatically redrawn after formatting and other changes. If **unchecked** , updates must be triggered manually.  
Zoom | Access various options to change the magnification of the plot sheet. This does not change data values.  
Layout Mode | Disable **[Page Layout](<PageLayoutMode.md>)** mode.  
  
### Projection Menu

The following menu appears if a 2D or 3D projection is right clicked and **Page Layout** mode is active. See [Projection Overlay Types](<Projection%20Overlay%20Types.md>).

3D Projection  
---  
Copy From  
3D View | Create a plot sheet projection based on the current view direction of the primary 3D window.  
3D Section | Create a plot sheet projection based on the currently active section definition. See [Sections and Projections](<alignviewwithsection.md>).  
Copy To  
3D View | Copy the view direction of the target projection to the primary 3D window, updating its view.  
View Settings... | Display the **View Settings** screen to edit the view direction, section definition and other projection-related settings. See [View Direction](<../COMMON/view%20settings%20direction%20dialog.md>)  
Scale  
Automatic | Fit all data into the projection. It's a bit like "zoom all" in the 3D window. Not available if the scale is locked (see below).  
Increase/Decrease | Increase or decrease the current scale by a fixed amount. Not available if the scale is locked.  
Custom | Set the scale of the target projection using the **[View Scale Properties](<viewscaleproperties.md>)** screen. Not available if the scale is locked.  
Area... | Define an area to zoom using a rectangle. Not available if the scale is locked.  
Lock | Toggle scale locking. If active, the scale cannot be changed interactively, otherwise, the other options above are available.  
Pan  
Left/Right/Up/Down | Pan the view in the selected direction, without changing the scale or view direction.  
With Cursor | Use the cursor to digitize a 2-point line, where the first point is the location to move, and the second point is the destination.  
Set Center | Click once to define the data that appears in the centre of the projection. This is similar to a middle mouse wheel 'click' in the 3D window.  
Exaggeration  
None | Remove any exaggeration applied to the projection.  
Set | Set the exaggeration (axis scaling) in the projection, along any major axis, using the [Set Exaggeration](<sectionviewrecorddialog.md>) screen.  
Direction  
Plan | Define the view direction of the projection to a plan view. This does not affect section definitions.  
North-South View | Define the view direction of the projection to a north-south view.  
East-West View | Define the view direction of the projection to an east-west view.  
Align with Section | Align the current view direction with the active section, viewing data orthogonally to that section.  
Flip | Flip the current view by 180. Essentially, this inverts the current view.  
Custom... | Change the **Dip** and **Azimuth** of the current view direction. See [View Direction](<viewdirectionproperties.md>).  
Section  
Orientation  
North-South | Change the currently active section definition orientation to north-south.  
East-West | Change the currently active section definition orientation to east-west.  
Horizontal | Change the currently active section definition orientation to plan.  
Settings... | Display the **[Section Definition](<../COMMON/Section%20Definition%20Dialog.md>)** screen to edit the current section properties.  
Next/Previous | Move to the next or previous section. If a single section is defined, the section is shifted by the section width, otherwise the next section in the Section Definition Table is activated. See [Sections and Projections](<alignviewwithsection.md>).  
Wider/Narrower | Make the current section corridor wider or narrower.  
Set Width... | Set the width of the section using the **[Section Width](<../COMMON/Section%20Definition%20Dialog.md>)** screen.  
Apply Clipping | Toggle the use of **[clipping](<ClipView.md>)** around the active section.  
Use Table | Choose if a Section Definition Table is used (it must be loaded). Pick the name of the loaded section table object. If no table is loaded, you are asked if you want to load one.  
Table Properties... |  If a Section Definition Table is loaded (see above) use the Properties screen to map fields and view summary information. Note: To define sections for the Section Definition Table, see [3D Sections](<../VR_Help/Sections.md>).  
Set as Active Section | Use the currently active section as the section master. Defining a section master allows you to create multiple views in plan, transverse and 3D all using the same section definition. See [Master Sections](<MasterSection.md>).  
Use Active Section | Apply the currently active section master, or set the current section to the master if there isn't one. See [Master Sections](<MasterSection.md>).  
3D Projection Properties... | Display the [3D Projection](<projection%20properties.md>) screen to edit the properties of the current section, including many of those listed here.  
Select... |  Select one of the components of the current plot sheet. The items listed here vary according to what your plot sheet contains, but in general mimics the items shown in the **Plots >> [Projection Name]>> Overlays** menu of the **Sheets** or **Project Data** control bars. Selecting an item highlights it and updates related screen controls (ribbon, Properties control bar and so on).  
Insert... | Add a plot item to the target projection using the **[Plot Item Library](<plotitemlibrary.md>)**.  
Copy [Projection Name] |  Copy the current projection to the clipboard. **Note** : A copied projection can be pasted by right-clicking the **Plots** folder icon in the **Sheets** or **Project Data** control bars.  
Paste Format | Substitute all of the properties of the copied plot item with the one selected for pasting.  
Move  | Move the projection with the cursor.  
Resize | Resize the projection dynamically. Move the mouse to resize a rectangle and click to resize.  
Opaque | If _Yes_ , a projection will fully obscure any items drawn before it, according to the plot sheet [drawing order](<Format_Drawing_Order_Dialog.md>). If _No_ , unfilled areas are transparent.  
Bring to Front | Draw the target projection last in the drawing order.  
Send to Back | Draw the target projection first in the drawing order.  
Wizard... | Display the **[Projection Wizard](<Projection_Wizard_Dialog.md>)** to allow the current projection to be updated.  
Reset | Reset the projection to default settings.  
Delete 3D Projection |  Delete the projection. **Warning** : This cannot be undone.  
Redraw Dynamically | If **checked** , data views are automatically redrawn after formatting and other changes. If **unchecked** , updates must be triggered manually.  
Zoom | Access various options to change the magnification of the plot sheet. This does not change data values.  
Layout Mode | Disable **[Page Layout](<PageLayoutMode.md>)** mode.  
  
## Page Layout Mode Inctive

If **Page Layout** mode is not active, different menus appear. In this mode, you cannot make changes that affect the layout of the sheet and format its components, hence the list of options is shorter than when the mode is active.

The following menu structure appears for any plot component, including both 2D and 3D projection types (see [Projection Overlay Types](<Projection%20Overlay%20Types.md>)):

Insert  
---  
Locatable Plot Item  
At a Point | Only available if a projection is selected. Add a plot item with a 3D data point location. See [Locatable Plot Items](<Locatable%20Plot%20Items.md>).  
Along a Line | Only available if a projection is selected. Add a plot item at the intersection of a 3D line with the target plot sheet. See [Locatable Plot Items](<Locatable%20Plot%20Items.md>).  
Outline | Add an outline feature to the current projection. Double click to complete and then configure using the **[Insert Outline](<insertoutlinedialog.md>)** wizard.  
3D Line | Add a 3D line feature to the projection. Double click to complete and then configure using the **[Insert Line](<InsertLineDialog.md>)** wizard.  
Text Annotation | Select and click a point in the projection, then add freeform text annotation to your projection using the **[Text Annotation](<text%20annotation%20dialog.md>)** screen.  
Dimension Overlay | Add a string to your plot that displays each string segment length. Digitize at least two points and double-click to finish. Dimension values are then applied.  
Geological Feature  
Lithology Outline | Add a lithology outline geological feature to your plot.  
Stratum | Add a stratum feature to your plot.  
Ore Zone Boundary | Add an ore zone boundary feature to your plot.   
Vein | Add a vein feature to your plot.  
Reef | Add a reef feature to your plot.  
Polygon Feature | Add a generic polygon feature to your plot. See [Geological Features - Outlines](<annotationboundaries.md>).  
Linear Feature | Add a generic line feature to your plot. See [Geological Features - Strings](<annotationlines.md>).  
Fault | Add a fault feature to your plot.  
Contact | Add a contact surface indicator feature to your plot.  
Redraw Dynamically | If Yes, the target projection updates as properties are changed. If no, the plot must be redrawn to see changes.  
Zoom | Choose a zoom level for your plot. This doesn't affect data values, only your view of data.  
Layout Mode | Toggle the use of **[Page Layout](<PageLayoutMode.md>)** mode.  
Measure | Select and click 2 points in the projection. The distance between the points appears in the **[Status](<../COMMON/Interface_Status%20Bars.md>)** bar.  
Format Display |  Use the [Format Display](<../COMMON/Format%20Overlays%20Dialog.md>) screens to edit any 2D projection elements, such as geological features and 2D overlays.  **Note** : To format 3D overlays, use the **Sheets** or **Project Data** control bar menus (**Plots >> Projection >> 3D Projection >> 3D Overlay Group** and double-click the 3D object overlay you want to modify.  
[Item Name] Properties | Display the **[Projection](<projection%20properties.md>)** properties screen.  
View Settings... | Display the **View Settings** screen to edit the view direction, section definition and other projection-related settings. See [View Direction](<../COMMON/view%20settings%20direction%20dialog.md>)  
  
Related topics and activities

  * [Projection Overlay Types](<Projection%20Overlay%20Types.md>)

  * [Plots from 3D Data](<../COMMON/Plot%20Overlays%20From%20Type.md>)

  * [The View Hierarchy](<../COMMON/View%20Hierarchy.md>)

  * [Page Layout Mode](<PageLayoutMode.md>)

  * [Drawing Order](<Format_Drawing_Order_Dialog.md>)

  * [Sections and Projections](<alignviewwithsection.md>)

  * [3D Overlay Groups](<3D%20Overlay%20Concept.md>)

  * [Projection Properties](<projection%20properties.md>)

  * [Projection Wizard](<Projection_Wizard_Dialog.md>)

  * [Format Display](<../COMMON/Format%20Overlays%20Dialog.md>)

  * [View Settings](<../COMMON/Section%20Definition%20Dialog.md>)