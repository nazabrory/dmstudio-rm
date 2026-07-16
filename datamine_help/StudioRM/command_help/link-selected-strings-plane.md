# link-selected-strings-plane ("lmpl")

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#link-selected-strings-plane>)

To access this command:

  * Explicit ribbon **> >**Create >> Link Multiple
  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "link-selected-strings-plane"

  * Use the quick key combination "lmpl".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **link-selected-strings-plane** and click **Run**.

## Command Overview

Links selected strings to form a solid wireframe, after sorting by plane which determines the linking order. A number of strings (specified) are grouped together. If fewer than two strings are selected when the command is run, you are prompted to select more.

The Number of strings in group value is used to specify the number of strings that are linked together before another end link is performed. If this is left blank, all strings are linked together and the two strings at each end of the sorted strings are end linked.

End-linking occurs depending on the state of the [link-selected-string-el-switch](<link-selected-string-el-switch.md>) status.  
  
The same type of control applies to the [link-selected-strings-attrib](<link-selected-strings-attrib.md>) command as well as the link-selected-strings-plane command. In the former the strings linking order is determined by the attribute value specified. The link-selected-strings-plane command sorts strings by the planes in which they lie.

Note: This command uses the **Maximum Segment Length** value (if greater than zero), as specified in **[Wireframe Linking Settings](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)** to limit the generated segment length of generated wireframe triangles.

### Using the 3D Solid linking method

If you have strings on adjacent sections that are to be linked together, and those strings cross each other when viewed in the direction of wireframing, then temporary vertices are inserted into the string and these temporary vertices are used when the wireframe is created. Since pairs of strings are wireframed at a time it is possible for these temporary vertices to be created for one pair of strings and not the other. In this situation a wireframe may be built which contains inconsistencies. 

Therefore, the 3D-Solid method is not suitable for use with the older linking commands if adjacent sections contain strings that cross each other in the direction of wireframing.

See [**3D Solid linking method**.](<../COMMON/3D%20Solid%20Linking%20Method.md>)

Command steps:

  1. In the [Current Objects](<../COMMON/Current_Objects_Toolbar.md>) toolbar, select or create a new current wireframe object.

  2. Run the command.

  3. Enter the Number of strings in group. This is the number of links the command will attempt to perform to create a single wireframe volume.

**Note** : the same screen is presented for both this link-selected-strings-plane ("lmpl") and [link-selected-strings-point ("lmpp")](<link-selected-strings-point.md>) commands.

  4. Click OK.

Wireframe data is generated.

Related topics and activities

  * [link-selected-string-el-switch](<link-selected-string-el-switch.md>)

  * [ link-selected-strings-attrib](<link-selected-strings-attrib.md>)

  * [ link-selected-strings-point](<link-selected-strings-point.md>)