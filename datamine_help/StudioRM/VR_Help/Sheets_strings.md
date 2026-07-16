# 3D Strings Menus

Each 3D window folder is used to configure the overlays for the currently active 3D window, access object-specific properties, and load or unload data.

String data is, simply, connected points. The points are _vertices_ and the connecting straight lines are _edges_.

The **Strings** folder of the **Sheets** and (if your product has one) **Project Data** control bars is slightly different to most of the others in that a third menu level is available. This is because a string object can contain one more string "traces". A trace is a separate string formed from connected vertices, and can be open or closed. Where multiple traces exist in the same object (for example, contour strings of a topography, or pit limit strings to control slope angles), the menu system extends to a deeper level, where each trace can be seen.

Note: There's no limit to the number of traces a string object can contain, but the menu system only displays the first 500 traces.

## Strings Folder Menu

To access this menu:

  * Right-click the **Strings** folder in the **Sheets** or **Project Data** control bar (if your product has one, and is configured to use default menus).

Note: Double-clicking the Strings folder displays the [Data Import](<../COMMON/data%20import%20dialog.md>) screen, allowing you to select a file for import using one of the data source drivers provided.

Right-clicking the Strings folder shows the following menu options:

Load | Display the [Import Data](<../COMMON/data%20import%20dialog.md>) screen, to be used for the import of an external file. Note that once a file of this type has been loaded into the currently-active 3D window, it is added to your project. You can import the same data more than once, to create multiple instances of that object, if required.  
---|---  
New |  Add new data to your active 3D scene interactively. Select this option and digitize points in your view. Points must be digitized onto a plane, section or wireframe surface. **Note** : This option is unavailable for Drillhole data.  
Create from Loaded Data |  Display the [3D Objects](<3d_objects.md>) screen, allowing you to select an object in the current project for display in the active 3D window.  
Clip All | Apply current view clipping to all overlays of the selected type. See [Clipping 3D Data](<Clipping-Data.md>).  
Clip None | All overlays in the target folder will ignore view clipping settings (show them completely) if selected.  
Show All | Show all overlays in the target folder.  
Transparent All | (Wireframe and block model data only) Render all wireframe overlays at 50% opacity.  
Hide All | Hide all overlays in the target folder.  
Unload All |  Unload all overlays and associated data objects within the selected folder.  Note: This does not delete physical files.  
Redraw All |  Redraw the view of all items in the target folder.  
Shininess | (Wireframe data only) Render all wireframe overlays so that they are shiny or dull.  
Apply Filter |  Apply a previously saved **Quick Filter** to all overlays of the selected data type.  See **[Quick Filters](<../COMMON/Quick%20Filter%20Dialog.md>)**.  
Delete All |  Remove all displayed overlays of the selected data type.  **Note** : This does not unload data object(s) or delete physical files.  
  
## Strings Overlay Menu

To access this menu:

  * Right-click an overlay item in the Strings folder.

Save | Save the current overlay's data object without further prompts. For this option to be available, you will need to have already saved the associated object in memory to a file at least once.  
---|---  
Data |  This option cascades the following sub-menu:

  * Reload...: Rreload the selected object into memory using new load/import settings.
  * Refresh...: Refresh the selected object into memory using its associated data load and import settings.
  * Save As...: Save the selected new 3D object to the project file or a new Datamine file. Displays the Save New 3D Object screen.
  * Export...: Export the selected object to a Datamine or non-Datamine file, using the [Data Export](<../COMMON/ExportTable.md>) screen.
  * To Excel...: Export the selected object's table and open it in MS Excel. This provides an quick means of exporting data to *.xls format. Warning: Microsoft Excel only supports a finite number of data rows, therefore, this option is not suitable for large data sets that have more data rows than the permitted maximum.
  * Unload...: Unload the selected object data from memory. **Note** : This does not remove the file from the project (i.e. it remains listed in the **Project Files** control bar), nor does it remove the file from disk.

  
Copy Data From | Append the selected object with data from another object of the same type using the [Select Objects to Copy From](<../COMMON/CopyDataFromDialog.md>) screen.  
Extract | Derive information held within currently loaded data objects, and create new objects based on the values contained within a selected field. Displays the [Extract Data Object](<../COMMON/ExtractDataObject_Dialog.md>) screen.  
Add Column | Add a new attribute to the data object to which the overlay relates, using the [Add Column](<../COMMON/AddColumn_Dialog.md>) screen.  
Make Current Object | To assign the data object associated with the selected overlay as the "current object", select this item - subsequent interactive 3D editing will be performed with respect to the current object. See [Current Objects](<../COMMON/Concept_Current_Object.md>).  
Select All | Select all object overlays of this type.  
Deselect All | Deselect all object overlays of this type  
Data Object Manager | Display the [Data Object Manager](<../COMMON/Data%20Manager%20Dialog.md>), with the associated data object selected for further analysis.  
Apply Clipping |  By default, 3D window clipping will be applied to all object overlays once clipping is activated. You can choose to disable or apply clipping to any overlay independently using this toggle option. View clipping will only be applied to overlays that are 'clipping-enabled'. See [Clipping 3D Data](<Clipping-Data.md>).  
Link to DTS |  Displays the [Change Column](<SetEPSColumnDialog.md>) screen. This is used to define an attribute that forms the basis for a schedule animation in Datamine Task Scheduler (this could be a pushback number or activity date, for example). You can only select a numeric data attribute. Not available if no DTS project is connected. See [DTS Synchronization Options](<../COMMON/EPS%20Sync%20Options%20Dialog.md>).  
[Overlay Name] Properties | Display the 3D properties screen associated with the target overlay. See [Viewing Data](<../COMMON/Interface_Viewing%20Data.md>)  
Use Template | Apply a display template to the overlay. This option only appears if at lease one template for the target object type exists.  
  
Copy | Create an identical copy of the overlay in the same folder.  
Look At |  Automatically positions the 'camera' to show the selected overlay. See [Look At](<vr_navigation_look_at.md>). Note: String overlays have an option to **Look at Individual String** using the [Select String/Drillhole](<select_string_or_drillhole_dialog.md>) screen. Similarly, drillholes have an additional **Look at Individual Drillhole** option.  
Show Labels | (Drillholes only) Toggle on or off the display of drillhole labels in the 3D view.  
Redraw | Refresh the view of the selected overlay (only) in the currently-active 3D view.  
Sequence Controls |  (Points and string overlays) Display the **Sequence Controls** toolbar to animate the target overlay according to its **Sequence Column**. See [Sequence Control](<Sequence%20Control%20Dialog.md>).  
New String |  Digitize a new string in a 3D window. Note: Click **Done** when you've finished.  
---|---  
Project to   
Wireframe or  
Section |  Project all vertices of the overlay's data object along the line of sight to intercept with a 3D section or wireframe surface, if possible. Note: Data that cannot be projected is left unchanged.  
Convert to Planes | Convert the data of the target overlay to a **Planes** object, assuming the best fit plane through each string trace to form planes. See [3D Planes](<Creating%20Planes.md>).  
Quick Legend or  
New Legend | Creates a numeric legend using the [Quick Legend](<../COMMON/Quick_Legend_Dialog.md>) screen, or create a new legend using the **Legends Manager**.  
---|---  
Display Legend | Preview the legend associated with the 3Doverlay.  
Legend Column | Select any data field within the parent object from which the overlay was created. Once selected, the currently associated legend will be applied to the new column. Note that the fixed colour will be used for any unmatched data.  
Rename | Rename the target overlay.  
Delete [Overlay Name] | Delete the current overlay. If this is the last overlay of a loaded data object, you can optionally unload the data object as well.  
  
## String Trace Menu

To access this menu:

  * Right-click a trace of a string data object overlay.

[Trace Number] Properties |  Display the **Trace Properties** screen to insert or delete trace vertices. See [Trace Properties (Vertices)](<Trace%20Properties%20Dialog%20\(Vertices\).md>).  
---|---  
Look At | Orient the camera of the active 3D window to look directly at the selected trace. See [Look At](<vr_navigation_look_at.md>).  
Add Vertices |  Add more points to the target trace by digitizing them in 3D. This affects all overlays associated with the object data. Note: Click **Done** when you've finished.  
Delete Last   
Vertex | Remove the most recently digitized vertex from the data object. This affects all overlays associated with the object data.  
Project to   
Wireframe or  
Section |  Project all trace points along the line of sight to intercept with a 3D section or wireframe surface, if possible. Note: Data that cannot be projected is left unchanged.  
Delete | Delete the trace from the string object.  
  
Related topics and activities

  * [Sheets 3D Folder](<SheetsOverview.md>)

  * [String Properties](<Traces_Properties.md>)

  * [Digitize and Edit](<Strings_Digitize%20and%20Edit.md>)

  * [Project Strings and Points](<../COMMON/ProjectStringsPoints_Dialog.md>)