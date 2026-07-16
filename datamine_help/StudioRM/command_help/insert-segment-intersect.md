# insert-segment-intersect ("isgi")

See this command in the [**command table**.](<COMMAND%20TABLE_I.md#insert-segment-intersect>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "insert-segment-intersect"

  * Use the quick key combination "isgi"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **insert-segment-intersect.htm** and click **Run**.

## Command Overview

Adds a new string vertex where another projected string segment would intersect it. The segment used for determining an intersection position can belong to the same or a different string object.

This command is unaffected by the current view direction or section plane, although strings must intersect cleanly (if strings are at different elevations, for example, intersection may not be possible). 

The direction of the initial selected segment is extended virtually to intersect with a second string segment.

Command Steps:

  1. Display string data in the **3D** window.

  2. Run the command.

  3. Select the string segment to receive the additional vertex.

  4. Select the string segment to be used to determine the intersection vertex position on the first segment.

If a string intersection is found, a new point is added to the first picked string segment.

  5. Click **Done** to complete the command.

Related topics and activities

  * [insert-at-intersections](<insert-at-intersections.md>)

  * [insert-point-segment-center](<insert-point-segment-center.md>)

  * [insert-points-mode](<insert-points-mode.md>)