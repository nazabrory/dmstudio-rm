# circle-from-edge-to-edge ("cee")

See this command in the [**command table**.](<_COMMAND%20TABLE_C.md#circle-from-edge-to-edge>)

To access this command:

  * **Digitize** ribbon **> > Create >> Arc >> Circle by Edges**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "circle-by-edges"

  * Use the quick key combination "cee".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **circle-by-edges** and click **Run**.

## Command Overview

Draws a circle with a diameter set by two points defined interactively in a **3D** window.

  * If no strings object exists in memory, a new object is created when this command is run, displaying details of the new object immediately in the Current Objects toolbar.

  * Right-click for snap; left-click for placing points without snapping.

  * If snapping is active, points may be snapped using the right mouse button.

**Tip** : This command can be completed by double-clicking (or tapping) anywhere in a 3D window.

**Note** : This command supports **[command line coordinates](<../COMMON/Coordinates_Command%20Line.md>)**.

### Selecting data and snapping

  * Using the left-mouse button for both the 1st and 2nd clicks will always align the resulting string with the currently active section.

  * Left-clicking the first point, then using right-click to snap to an off-section point will still scale the string, but the resulting string will always be coincident with the section plane.

  * Right-clicking a point off-section then left-clicking or right-clicking a second point will produce a string that will align with the current section's azimuth and dip, but without changing the elevation of the first point; the square will be positioned at the elevation of the first point, and following the direction of the section.

**Tip** : change the colour of the string you are creating whilst the command is active. You can even access the [String Properties](<../VR_Help/Traces_Properties.md>) screen to make further edits to the legend, symbols etc. without having to close the command.

Command steps:

Command steps:

  1. Run the command.

  2. Select your snap and data selection settings. See [Selecting 3D Data Interactively](<../COMMON/Selecting3DDataInteractively.md>).

  3. In the Current Objects toolbar, select the current object or create a new one. See [Set the current object](<../COMMON/Current_Objects_Toolbar.md>).

  4. In the Current Objects toolbar, choose an Attribute Field and Attribute Value. See [Set current object attributes](<../COMMON/Current_Objects_Toolbar.md>).

  5. Click to define the first diameter circumference point of the circle.

  6. Click to define the second diameter circumference point of the circle.

  7. If required, click or click-and-drag to move the previously placed second edge point.

The circle grows and shrinks dynamically.

  8. Click Cancel to complete the creation of the circle.

Related topics and activities

  * [circle-from-center-to-edge](<circle-from-center-to-edge.md>)

  * [ circle-with-defined-radius](<circle-with-defined-radius.md>)

  * [ circle-by-three-points](<circle-by-three-points.md>)