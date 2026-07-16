# set-snap-points-switch ("stpo")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#set-snap-points-switch>)

To access this command:

  * **Digitize** ribbon **> > Snap >> Snap to Points**.

  * Use the quick key combination "stpo".

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "set-snap-points-switch".

  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **set-snap-points-switch** and click **Run**.

## Command Overview

Sets snap mode to snap to object points.

Snapping is done to select points interactively using the right-mouse button. If you snap to a point the location of the cursor is set at the X Y and Z coordinates of that point. When using the left-mouse button (no snap), the cursor location, when placing a point, is set at the X Y and Z coordinate of the point on the view plane on which the cursor lies.

With point snapping activated, when the right-mouse button is used the cursor is set at the X Y and Z coordinate of the data point that is nearest to the cursor when the button is pressed. A data point is a point on a string or drill hole. Points available for snapping on drill holes are the sample end points and sample centre points. The sample ends are marked with tick marks and the centre points marked with circles.

**Tip** : The snapping mode can be changed while in the middle of executing another command, such as defining a string. For example, the first point on a new string could be set at (4000,2000,6000) using a grid snapping mode, and then other points on the string defined by snapping to other objects by toggling a points snap mode during digitizing.

Command steps:

  1. Run the command.

  2. Run the required, relevant design commands which would make use of this snap mode e.g. new-string.

Related topics and activities

  * [set-snap-grid-parameters ("gs")](<set-snap-grid-parameters.md>)

  * [set-snap-grid-switch ("stg")](<set-snap-grid-switch.md>)

  * [set-snap-lines-switch ("stl")](<set-snap-lines-switch.md>)

  * [set-snap-mode ("snm")](<set-snap-mode.md>)

  * [set-snap-none-switch ("sn0")](<set-snap-none-switch.md>)

  * [set-snap-surface-switch ("sts")](<set-snap-surface-switch.md>)