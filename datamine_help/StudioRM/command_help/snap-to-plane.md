# snap-to-plane ("stpl")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#snap-to-plane>)

To access this command:

  * Use the quick key combination "stpl".

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "snap-to-plane".

  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **snap-to-plane** and click **Run**.

## Command Overview

Note: Don't confuse this command with one of the plane data type snapping commands (such as [snap-to-plane-data-switch ("stpp")](<snap-to-plane-data-switch.md>), for example. In this context, the 'plane' is actually a 3D window section definition, used for clipping and digitizing, not a planes object type.

Move the current view plane to a parallel plane through a point. 

This can be really useful to align a cross-sectional plane for clipping, for example, when viewing a model slice passing through a particular drillhole segment, or to see how hanging wall points align with an implicit model.

Command steps:

  1. Display reference data in a **3D** window.

  2. Run the command.

  3. Select (left click) any data point (make sure your [data selection settings](<../COMMON/Selecting3DDataInteractively.md>) are set up first).

The current section plane position snaps to the clicked point.

Note: The existing section orientation (dip and azimuth) doesn't change. To change this, you'll need to edit [Section Properties](<../VR_Help/Section%20Properties%20Dialog.md>).

Related topics and activities:

  * [3D Sections](<../VR_Help/Sections.md>)

  * [Section Properties](<../VR_Help/Section%20Properties%20Dialog.md>)