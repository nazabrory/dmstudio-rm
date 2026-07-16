# link-selected-strings-point ("lmpp")

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#link-selected-strings-point>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "link-selected-strings-point"

  * Use the quick key combination "lmpp".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **link-selected-strings-point** and click **Run**.

## Description

Links strings to form a solid wireframe. The linking order is determined by the proximity of the centres of each string. In this respect, strings with the closest centres are linked.

**Note** : if duplicate strings exist within the selection, these are ignored, and the command window reports that a link has not been created.

### Using the 3D Solid linking method

If you have strings on adjacent sections that are to be linked together, and those strings cross each other when viewed in the direction of wireframing, then temporary vertices are inserted into the string and these temporary vertices are used when the wireframe is created. Since pairs of strings are wireframed at a time it is possible for these temporary vertices to be created for one pair of strings and not the other. In this situation a wireframe may be built which contains inconsistencies. 

Therefore, the 3D-Solid method is not suitable for use with the older linking commands if adjacent sections contain strings that cross each other in the direction of wireframing.

See [**3D Solid linking method**.](<../COMMON/3D%20Solid%20Linking%20Method.md>)

## How to Use

  1. In the Current Objects toolbar, select or create a new current wireframe object.

  2. Load and select at least two separate strings.

  3. Run the command. 

  4. Select a sting to start the linking sequence.

  5. Enter the Number of strings in group. This is the number of links the command will attempt to perform to create a single wireframe volume.

**Note** : the same screen is presented for both this link-selected-strings-point ("lmpp") and link-selected-strings-point ("lmpp") commands.

  6. Click OK.

Wireframe data is generated.

Related topics and activities

  * [link-selected-string-el-switch](<link-selected-string-el-switch.md>)

  * [link-selected-strings-attrib](<link-selected-strings-attrib.md>)

  * [link-selected-strings-plane ("lmpl")](<link-selected-strings-plane.md>)