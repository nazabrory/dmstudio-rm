# cg-points ("cgp")

See this command in the [**command table**.](<_COMMAND%20TABLE_C.md#cg-points>)

To access this command:

  * **Digitize** ribbon **> > Tools >> More >> Create Center Points**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "cg-points".

  * Use the quick key combination "cgp".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **cg-points** and click **Run**.

## Command Overview

Creates a COG (center of gravity) point for all selected perimeters (closed strings). The new point(s) inherit the attributes of the parent perimeter string(s).

This command cannot be used with open strings.

Command steps:

  1. Select the perimeter(s) from which center points are required.

  2. Run the command.

A new points object is created if one does not already exist, or data is added to the current points object. Each target string generates a COG point.

**Note** : COLOUR, LSTYLE and SYMBOL attributes are also copied from the perimeters to the points.

Related topics and activities

  * [close-string](<close-string.md>)