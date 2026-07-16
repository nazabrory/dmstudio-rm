# link-quad

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#link-quad>)

To access this command:

  * Explicit ribbon >> Create >> Link >> Link Quad
  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "link-quad"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **link-quad** and click **Run**.

## Command Overview

Create a wireframe link using points on the selected segments of two strings.

This command provides an alternative control over linking to the [tagging method](<../COMMON/Wireframe_Tag_Strings.md>) and allows you to build up a complete link between strings in stages.

### Using the 3D Solid linking method

If you have strings on adjacent sections that are to be linked together, and those strings cross each other when viewed in the direction of wireframing, then temporary vertices are inserted into the string and these temporary vertices are used when the wireframe is created. Since pairs of strings are wireframed at a time it is possible for these temporary vertices to be created for one pair of strings and not the other. In this situation a wireframe may be built which contains inconsistencies. 

Therefore, the 3D-Solid method is not suitable for use with the older linking commands if adjacent sections contain strings that cross each other in the direction of wireframing.

See [**3D Solid linking method**.](<../COMMON/3D%20Solid%20Linking%20Method.md>)

Command steps:

  1. In the Current Objects toolbar, select or create a new current wireframe object.

  2. Run the command.

  3. Indicate the FIRST point on the FIRST string.

  4. Indicate the SECOND point on the FIRST string.

  5. Pick the string segment to link.

The string segment is highlighted.

  6. Select FIRST point of NEXT segment to link to the selected segment.

  7. Indicate the SECOND point of the NEXT segment.

  8. Pick the string segment to link.

  9. Click Finish.

Quad wireframe data is generated.

Related topics and activities

  * [link-strings ("ls")](<link-strings.md>)

  * [link-boundary ("lbo")](<link-boundary.md>)

  * [link-multiple-strings ("lms")](<link-multiple-strings.md>)

  * [link-outline-pair ("l2")](<link-outline-pair.md>)

  * [link-outline-pair-attribute ("l3o")](<link-outline-pair-attribute.md>)

  * [Wireframe Tag Strings](<../COMMON/Wireframe_Tag_Strings.md>)