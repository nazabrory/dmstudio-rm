# square-from-edge-to-edge ("see")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#square-from-edge-to-edge>)

To access this command:

  * **Digitize** ribbon **> > Create >> Rectangle >> Square by Edges**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "square-from-edge-to-edge"

  * Use the quick key combination "see".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **square-from-edge-to-edge** and click **Run**.

## Command Overview

Draws a square by defining a point on two opposite edges. 

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

  4. Click to define the mid point of one edge of the square.

  5. Click to define a point on the opposite edge of the square, to define its height and width.

**Tip** : To adjust the size of the square, click-and-drag to move the second point.

  6. Click Done to complete the creation of the square.

Related topics and activities

  * [rectangle-from-center-to-corner ("rcec")](<rectangle-from-center-to-corner.md>)

  * [rectangle-from-corner-to-corner ("rcce")](<rectangle-from-corner-to-corner.md>)

  * [square-from-center-to-corner ("stc")](<square-from-center-to-corner.md>)

  * [square-from-corner-to-corner](<square-from-corner-to-corner.md>)

  * [square-from-center-to-edge ("sce")](<square-from-center-to-edge.md>)

  * [create-planar-rectangle("crct")](<create-planar-rectangle.md>)