# set-snap-grid-switch ("stg")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#set-snap-grid-switch>)

To access this command:

  * **Home** ribbon **> > Snap >> Snap >> Snap To Grid.**

  * **Digitize** ribbon **> > Snap >> Snap to Grid**.

  * Use the quick key combination "stg".

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "set-snap-grid-switch".

  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **set-snap-grid-switch** and click **Run**.

## Command Overview

Set snap mode to snap to grids. 

If enabled, the right-mouse button is used the cursor is set at the X Y and Z coordinate of a grid point defined by the grid increment numbers. These can be changed by selecting them with the cursor and typing in a new value from the keyboard. The origin of the grid is initially at (0,0,0) but can also be reset. 

If the grid increment for an axis is set at zero no snapping is performed in that direction. Thus if the increments are X=10, Y=5 and Z=0, when the right-mouse button is used the cursor is set at coordinates such as (30,15,34.23) and (400,255,87.56), depending upon the current view plane settings.

Command steps:

  1. Run the command.

  2. Run the required, relevant design commands which would make use of this snap mode e.g. new-string.

Related topics and activities

  * [set-snap-grid-parameters ("gs")](<set-snap-grid-parameters.md>)

  * [set-snap-lines-switch ("stl")](<set-snap-lines-switch.md>)

  * [set-snap-mode ("snm")](<set-snap-mode.md>)

  * [set-snap-none-switch ("sn0")](<set-snap-none-switch.md>)

  * set-snap-grid-switch ("stg")

  * [set-snap-surface-switch ("sts")](<set-snap-surface-switch.md>)