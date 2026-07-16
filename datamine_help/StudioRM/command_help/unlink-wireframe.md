# unlink-wireframe ("uw")

See this command in the [**command table**.](<COMMAND%20TABLE_U.md#unlink-wireframe>)

To access this command:

  * **Explicit** ribbon **> > Create >> Unlink Wireframe**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "unlink-wireframe"

  * Use the quick key combination "uw".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **unlink-wireframe** and click **Run**.

## Command Overview

Remove all wireframe links with a shared LINK attribute value.

All previously-selected data is unselected once this command is run. Target data must contain a LINK attribute.

Command steps:

  1. Load and display the wireframe data to be modified.
  2. Run the command
  3. Pick a loaded wireframe object. 

All the triangles with the same LINK value become selected and a message displays asking for confirmation of the deletion.

     * Confirming deletes the highlighted triangles (which is supported by undo and redo).
     * Declining deselects the triangles without unlinking them.

Related topics and activities

  * [unlink-triangle](<unlink-triangle.md>)

  * [erase-all-wireframes](<erase-all-wireframes.md>)

  * [erase-wireframe ("erw")](<erase-wireframe.md>)

  * [erase-wireframes](<erase-wireframes.md>)