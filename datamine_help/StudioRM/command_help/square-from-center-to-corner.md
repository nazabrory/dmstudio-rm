# square-from-center-to-corner ("stc")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#square-from-center-to-corner>)

To access this command:

  * **Digitize** ribbon **> > Create >> Rectangle >> Square by Center and Corner**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "square-from-center-to-corner"

  * Use the quick key combination "stc".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **square-from-center-to-corner** and click **Run**.

## Command Overview

Draw a square with a centre point and a corner point. Points can be digitized into any 3D window. 

**Tip** : If you're after a rectangle of known dimensions, consider snapping to a grid with this command, or use [create-planar-rectangle("crct")](<create-planar-rectangle.md>).

**Note** : This command supports **[command line coordinates](<../COMMON/Coordinates_Command%20Line.md>)**.

### Selecting data and snapping

  * Using the left-mouse button for both the 1st and 2nd clicks will always align the resulting string with the currently active section.

  * Left-clicking the first point, then using right-click to snap to an off-section point will still scale the string, but the resulting string will always be coincident with the section plane.

  * Right-clicking a point off-section then left-clicking or right-clicking a second point will produce a string that will align with the current section's azimuth and dip, but without changing the elevation of the first point; the square will be positioned at the elevation of the first point, and following the direction of the section.

**Tip** : change the colour of the string you are creating whilst the command is active. You can even access the [String Properties](<../VR_Help/Traces_Properties.md>) screen to make further edits to the legend, symbols etc. without having to close the command.

Command steps:

  1. Select the required snap and data selection settings using the Home ribbon.

  2. Run the command.

  3. Using the Current Objects toolbar, select the current string object or create a new one. See [Current Objects](<../COMMON/Current_Objects_Toolbar.md>).

  4. Click to define the a corner point of the square.

  5. Click to define the opposite corner point of the square.

**Tip** : To adjust the size of the square, click-and-drag to move a corner point.

  6. Click Done to complete the creation of the square.

Related topics and activities

  * [rectangle-from-center-to-corner ("rcec")](<rectangle-from-center-to-corner.md>)

  * [rectangle-from-corner-to-corner ("rcce")](<rectangle-from-corner-to-corner.md>)

  * [square-from-center-to-edge](<square-from-center-to-edge.md>)

  * [square-from-corner-to-corner](<square-from-corner-to-corner.md>)

  * [square-from-edge-to-edge](<square-from-edge-to-edge.md>)

  * [create-planar-rectangle("crct")](<create-planar-rectangle.md>)