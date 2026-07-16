# insert-curve ("ics")

See this command in the [**command table**.](<COMMAND%20TABLE_I.md#insert-curve>)

To access this command:

  * **Digitize** ribbon **> > Edit >> Replace with Curve**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "insert-curve"

  * Use the quick key combination "ics".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **insert-curve** and click **Run**.

## Command Overview

Quickly generate smooth string curves based on preceding and following edge orientations, by selecting two control points. This command can be used to modify existing open or closed string data.

All attributes on the original string is copied to any new vertices added during curve generation.

For closed strings, points should be selected in a clockwise screen direction. The angle of the string segment that precedes the first point is continued to create the first modifier line and the segment following the second point will is to create the second modifier line.

Command steps:

  1. Display the string data to be modified in any 3D window.
  2. Activate the command.
  3. Select the first point for the curve on any string (right-click snapping options are supported).
  4. Select the last point for the curve on the same string.  

  5. Use the two modifier control strings to adjust the position, extent and direction of the curve.
  6. Click **Done** to update the string and insert the new points to honor the required curve.

Related topics and activities

  * [insert-line ("ils")](<insert-line.md>)

  * [insert-near-points](<insert-near-points.md>)

  * [insert-points-mode ("ipo")](<insert-points-mode.md>)

  * [insert-segment-intersect ("isgi")](<insert-segment-intersect.md>)