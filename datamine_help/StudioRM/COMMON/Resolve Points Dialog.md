# Resolve Points

To access this screen:

  * **Digitize** ribbon **> > Condition >> Condition >> Resolve String Points**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "resolve-string-points"

  * Use the quick key combination "resp".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **resolve-string-points** and click **Run**.

Make points from one string coincident with those of another string if they are under a defined separation distance.

A possible use for this screen is to remove digitizing errors from abutting perimeters (such as geological outlines) ensuring that points match exactly. 

Another use is to produce an overall perimeter 'skin' around several intersecting perimeters. In this case a perimeter for resolution must be defined around the outside, conditioned so that it contains many points, then this command can be used with an arbitrarily large tolerance distance using the "+" character.

Activity steps:

  1. Run the command

The Resolve Strings screen displays

  2. Enter a **Tolerance Distance**.

  3. Click **OK**.

  4. Select the string containing points to resolve. 

Any points on this string that lie within the tolerance distance of any points on any other string are moved to coincide with the "other" string point(s). If no points are found within the tolerance distance, the string is unchanged.

Related topics and activities:

  * [resolve-string-points ("resp")](<../command_help/resolve-string-points.md>)