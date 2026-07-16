# Planes folder menu

Each 3D window folder is used to configure the overlays for the currently active 3D window, access object-specific properties, and load or unload data.

Points data objects and overlays are listed in the Points folder. The folder, and items within it, are supported by context menus.

Planes are added to this folder either by importing an external planes file, loading a [Planes object](<../COMMON/filetype.md#planes>) from the current project, or by generating a plane from either an open or closed string. Your application can use strings digitised onto wireframes to specify key planes, for example for joint space analysis. As part of this, a variety of tools and visualisation methods are available to help with their generation and interpretation.

See [Planes Properties](<Planes%20Properties%20Dialog.md>).

An existing planes file can be imported using the data source drivers, by either right-clicking the root level of this folder and selecting Import, or you can (re)import a plane object already in memory by selecting Import from Project. Note that the imported file must contain the minimum required fields for a [plane definition file](<../COMMON/filetype.md#planes>).

## Planes Folder Menu

To access this menu:

  * Right-click the **Planes** folder in the **Sheets** or **Project Data** control bar (if your product has one, and is configured to use default menus).

Note: Double-clicking the Planes folder displays the [Data Import](<../COMMON/data%20import%20dialog.md>) screen, allowing you to select a file for import using one of the data source drivers provided.

Right-clicking the Planes folder shows the following menu options:

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
  
## Planes Overlay Menu

To access this menu:

  * Right-click an overlay item in the Planes folder.

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
Quick Legend or  
New Legend | Creates a numeric legend using the [Quick Legend](<../COMMON/Quick_Legend_Dialog.md>) screen, or create a new legend using the **Legends Manager**.  
---|---  
Display Legend | Preview the legend associated with the 3Doverlay.  
Legend Column | Select any data field within the parent object from which the overlay was created. Once selected, the currently associated legend will be applied to the new column. Note that the fixed colour will be used for any unmatched data.  
Rename | Rename the target overlay.  
Delete [Overlay Name] | Delete the current overlay. If this is the last overlay of a loaded data object, you can optionally unload the data object as well.  
  
Related topics and activities

  * [3D Planes](<Creating%20Planes.md>)

  * [Sheets 3D Folder](<SheetsOverview.md>)

  * [Datamine File Descriptions](<../COMMON/filetype.md>)