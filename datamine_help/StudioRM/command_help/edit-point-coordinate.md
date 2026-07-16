# edit-point-coordinate ("epc")

See this command in the [**command table**](<COMMAND%20TABLE_E.md#edit-point-coordinate>).

To access this command:

  * **Digitize** ribbon **> > Edit >> Move Points >> Edit Coordinate**.
  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "edit-point-coordinate"
  * Use the quick key combination "epc".
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **edit-point-coordinate** and click **Run**.

## Command Overview

Edit the coordinates of the selected point or string vertex. 

The following constraints should be considered when using this command:

  * When only points are selected, only the selected points can be edited.
  * If multiple points are selected, answering "No" to the "Move all selected points?" question moves a single point.
  * When moving selected points, the point originally picked moves to the required coordinates, with other points displaced by the same amount.
  * If both string and point data is selected, string data is affected only. String data edits will always take precedence over selected point data.

Command Steps:

  1. Launch the **edit-point-coordinate** command.
  2. Select one or more points or vertices to edit, using any available **3D** window.

The **Enter New Coordinate Screen** displays.

  3. Edit the **X** , **Y** and **Z** values as required.
  4. Click **OK** to update the loaded data object in the **3D** view.
  5. If multiple data points were selected, a "Move all selected points" prompt displays:
     * Select **Yes** to move all selected points or vertices to the 3D location indicated by the coordinate fields displayed.
     * Select **No** to update only the first selected point or vertex.

Related Topics and Activities

  * [Coordinate Systems](<../COMMON/Coordinate%20Systems%20Concept.md>)
  * [Digitizing using Command Line Coordinates](<../COMMON/Coordinates_Command%20Line.md>)
  * [move-points-mode ("mpo")](<move-points-mode.md>)