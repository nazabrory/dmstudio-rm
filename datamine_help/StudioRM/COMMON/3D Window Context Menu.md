# 3D Window Context Menu

To access this screen:

  * Right-click any empty part of a **3D** window.

Each 3D window's context menu can be used to quickly access and run recently used commands and commonly-used 3D data manipulation commands.

To repeat a previous command:

  1. Right-click an empty part of any **3D** window

  2. The 5 most recently accessed commands are shown in **Recent Commands**.

  3. Either select one of the 'top 5' or click More.. to display **Recent Commands**.

     1. Review the presented list to choose from any of commands run in the current or previous sessions.

To save 3D data using the context menu:

You can use the 3D window context menu to save loaded 3D object data in its current state.

  1. Right-click an empty part of any **3D** window

  2. Expand **Save** to display a list of 3D data types.

     1. Only data types that are currently loaded are accessible. 

     2. If data was originally loaded from a source file, it will automatically be saved without prompts.

     3. If new object data has been created in the current project session, you are asked for a file name.

To load 3D data using the context menu:

  1. Right-click an empty part of any **3D** window.

  2. Expand Load to reveal further options:

     1. Pick a data type currently available as a Datamine file, then select an existing project file to load it.

     2. Pick a file **External** to your project and then load it and add it to your project at the same time.

     3. Pick a file in a non-Datamine format, and import it using **Data Source Drivers**.

     4. Connect to a database or Fusion workspace.

     5. Display the **[Data Load Wizard](<new_document_wizard.md>)** to load data files from one or more sources.

To access data selection options:

Sometimes, it can be useful to focus data selection so that only desired data types are picked by the cursor.

  1. Right-click an empty part of any **3D** window.

  2. Expand **Data Selection**.

  3. Pick a data type to swap all loaded data of that type from 'selectable' to 'unselectable' mode.

To view each data types selection setting, activate the **Home** ribbon and expand the **Select >> Default** menu.

You can also select or deselect all loaded points. strings or drillholes.

To create new data objects:

  1. Right-click an empty part of any **3D** window.

  2. Expand **Define New Data**.

  3. Choose to create a new _Points_ , _Strings_ , _Ellipsoid_ or _Drillholes_ object.

**Tip** : to create other data type objects, use the **[Current Objects](<Current_Objects_Toolbar.md>)** toolbar.

To remove loaded data from memory:

You can unload data using the context menu:

  1. Right-click an empty part of any **3D** window.

  2. Expand **Erase**.

  3. Pick the data type to unload. 

     * For any selection starting with "All", all data of the selected data type is erased.

     * Otherwise, you are prompted to select 3D data to erase interactively. Only data of the selected type is erased.

To set up data snapping:

Data snapping is useful for making data line up in the 3D view.

  1. Right-click an empty part of any **3D** window.

  2. Expand **Data Snapping**

     1. Set up object-specific snapping with **[Object Snap Settings](<SnapSettings.md>)**.

     2. Toggle snap switches using **[set-snap-points-switch](<../command_help/set-snap-points-switch.md>)** , **[set-snap-lines-switch](<../command_help/set-snap-lines-switch.md>)** , [set-snap-grid-switch](<../command_help/set-snap-grid-switch.md>) or **[set-snap-surface-switch.](<../command_help/set-snap-surface-switch.md>)**

     3. Toggle snapping mode to a particular data type.

Related topics and activities

  * [Data Load Wizard](<new_document_wizard.md>)

  * [Current Objects](<Current_Objects_Toolbar.md>)

  * [Object Snap Settings](<SnapSettings.md>)