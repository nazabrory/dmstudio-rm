# end-link-boundary ("elb")

See this command in the [**command table**.](<COMMAND%20TABLE_E.md#end-link-boundary>)

To access this command:

  * Explicit ribbon **> >**Create >> End Link >> End Link Boundary

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "end-link-boundary"

  * Use the quick key combination "elb".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **end-link-boundary** and click **Run**.

## Command Overview

Creates a wireframe link by closing an area defined by a perimeter and its associated boundary/bridge string(s).

In the example below, the bottom perimeter would be closed in three steps, using the end-link-boundary command, honouring the red boundary strings:

![](../Images/LinkBoundary1.gif)

  * If the perimeter contains no bridge strings this command behaves in the same way as the [end-link](<end-link.md>) command.

  * More than one bridge string may be connected to the perimeter.

  * A bridge string is a string that has both its first and last points connected to points on one of the two strings which are to be linked.

  * Bridge strings must have their end points snapped (point or line) to a perimeter.

  * It is not necessary to select the bridge string, as these are automatically detected during the linking process.

  * Bridge strings can contain any number of points and be fully three dimensional, but their end points must be connected to points on one of the selected strings. Crossovers of bridge strings should be avoided. The bridge strings themselves are not selected when running this command, they are automatically detected.

  * The links take their colour from the first string of each string-pair used for the linking.
  * Various settings can be used to control linking, see [Wireframe Linking Settings](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>).
  * Tag strings can be used to control linking, see [use-tag-switch](<use-tag-switch.md>).

Note: This command uses the **Maximum Segment Length** value (if greater than zero), as specified in **[Wireframe Linking Settings](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)** to limit the generated segment length of generated wireframe triangles.

Command steps:

  1. In the [Current Objects](<../COMMON/Current_Objects_Toolbar.md>) toolbar, select or create a new current wireframe object.

  2. Run the command.

  3. Following the prompts in the Status Bar or your cursor tooltips (if enabled) select the required end perimeter portion. Repeat for other end perimeter portions and click Cancel to exit the command.

  4. Link the remaining perimeters or strings using the related [link-boundary-to-line](<link-boundary-to-line.md>), [link-boundary](<link-boundary.md>) or any other relevant string linking commands.

Related topics and activities

  * [link-boundary](<link-boundary.md>)

  * [ link-boundary-to-line](<link-boundary-to-line.md>)

  * [ end-link](<end-link.md>)

  * [Wireframe Linking Settings](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)

  * [use-tag-switch](<use-tag-switch.md>)

  * [Current Objects](<../COMMON/Current_Objects_Toolbar.md>)