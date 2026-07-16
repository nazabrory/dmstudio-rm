# unlink-triangle ("utr")

See this command in the [**command table**.](<COMMAND%20TABLE_U.md#unlink-triangle>)

To access this command:

  * **Explicit** ribbon **> > Create >> Unlink Triangle**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "unlink-triangle"

  * Use the quick key combination "utr".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **unlink-triangle** and click **Run**.

## Command Overview

Interactively erase wireframe triangle data from the current wireframe.

Running this command deselects previously selected wireframe triangles.

  * This will erase data from the wireframe in memory; these modifications are only written to file when the [write-wf-data](<write-wf-data.md>) command is run or the object is saved on exit from Studio.

  * The target wireframe is not re-meshed to compensate for absent data.

  * The [wireframe-verify](<wireframe-verify.md>) command should used to update the wireframe adjacency information after edits to wireframe triangles have been made.

Command Steps:

  1. In the [Current Objects](<../COMMON/Current_Objects_Toolbar.md>) toolbar, select the wireframe data to modify.

  2. Run the command.

  3. Click within the boundary of the required wireframe triangle.

  4. Confirm the deletion.

  5. Repeat steps 3 and 4 until all required triangles have been deleted.

  6. Click Done.

Related topics and activities

  * [unlink-wireframe ("uw")](<unlink-wireframe.md>)

  * [erase-all-wireframes](<erase-all-wireframes.md>)

  * [erase-wireframe ("erw")](<erase-wireframe.md>)

  * [erase-wireframes](<erase-wireframes.md>)