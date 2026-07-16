# Pictures folder menu

Each 3D window folder is used to configure the overlays for the currently active 3D window, access object-specific properties, and load or unload data.

Pictures are 3D objects, essentially points data with a reference to an image file. Displayed on a flat plane, oriented in any 3D direction, picture objects are useful references for further analysis and design. You can either use existing georeferencing data or configure your own at the point of loading using [Image Registration](<ImageRegistration_Dialog.md>).

See [Pictures Data Type](<Images%20Data%20Type.md>).

## Pictures Folder Menu

To access this menu:

  * Right-click the **Pictures** folder in the **Sheets** or **Project Data** control bar (if your product has one, and is configured to use default menus).

Note: Double-clicking the Pictures folder displays the [Data Import](<../COMMON/data%20import%20dialog.md>) screen, allowing you to select a file for import using one of the data source drivers provided.

Right-clicking the Pictures folder shows the following menu options:

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
  
## Pictures Overlay Menu

To access this menu:

  * Right-click an overlay item in the Pictures folder.

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
Data Object Manager | Display the [Data Object Manager](<../COMMON/Data%20Manager%20Dialog.md>), with the associated data object selected for further analysis.  
Apply Clipping |  By default, 3D window clipping will be applied to all object overlays once clipping is activated. You can choose to disable or apply clipping to any overlay independently using this toggle option. View clipping will only be applied to overlays that are 'clipping-enabled'. See [Clipping 3D Data](<Clipping-Data.md>).  
Look At |  Automatically positions the 'camera' to show the selected overlay. See [Look At](<vr_navigation_look_at.md>).  
Redraw | Refresh the view of the selected overlay (only) in the currently-active 3D view.  
Rename | Rename the target overlay.  
Delete [Overlay Name] | Delete the current overlay. If this is the last overlay of a loaded data object, you can optionally unload the data object as well.  
  
Related topics and activities

  * [Sheets 3D Folder](<SheetsOverview.md>)

  * [Pictures Data Type](<Images%20Data%20Type.md>)

  * [Pictures Properties](<Pictures%20Properties%20Dialog.md>)

  * [Image Registration](<ImageRegistration_Dialog.md>)

  * [Image Registration - Example 1](<Image%20Registration%20Worked%20Example.md>)

  * [Image Registration Example 2](<image%20registration%20worked%20example%202.md>)