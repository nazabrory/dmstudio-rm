# circle-by-three-points ("a3")

See this command in the [**command table**.](<_COMMAND%20TABLE_C.md#circle-by-three-points>)

To access this command:

  * **Digitize** ribbon **> > Tools >> Arc**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "check-link-selected-strings".

  * Use the quick key combination "clss".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **check-link-selected-strings** and click **Run**.

## Command Overview

Draws an arc defined by three points interactively in a **3D** window. The first two points define the end points of the arc, and the third is a point that the arc passes through.

  * If no strings object exists in memory, a new object is created when this command is run, displaying details of the new object immediately in the [Current Objects](<../COMMON/Current_Objects_Toolbar.md>) toolbar.

### Snapping to Data

This command supports both left- (freeform) and right-click snapping. How snapping is applied depends on which of the three points is snapped.

  * If you right-click (snap) to define the start point, the arc will start at the snapped elevation, regardless of the currently active 3D section definition. If your first point is snapped:
    * Selecting the 2nd point (the arc end) with a left click adds the final point of the arc on the currently active section, potentially creating a spiral incline or decline. The third point (left or right click) defines the arc circumference, maintaining the gradual change from start to end point (which will always be on-section).
    * Snapping the 2nd point ensures the arc spans between the two snapped points and could, potentially, be completely off-section. The third click (left or right click) defines the extent of the arc.

**Note** : This command supports **[command line coordinates](<../COMMON/Coordinates_Command%20Line.md>)**.

Command steps:

  1. Run the command.

  2. Click in a **3D** window to define the start point of the arc.

  3. Click to define the end point of the arc.

  4. Click to define the point on the circumference.

**Tip** : Left-click and drag the third point to dynamically resize the generated arc, or right-click and drag to snap dynamically to nearby data.

  5. Double-click or tap to cancel the command.

Related topics and activities

  * [circle-from-edge-to-edge](<circle-from-edge-to-edge.md>)

  * [circle-from-center-to-edge](<circle-from-center-to-edge.md>)

  * [circle-with-defined-radius](<circle-with-defined-radius.md>)