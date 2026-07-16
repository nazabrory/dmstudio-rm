# link-single-outline ("l1")

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#link-single-outline>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "link-single-outline"

  * Use the quick key combination "l1".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **link-single-outline** and click **Run**.

## Description

Create wireframe from an outline string and supplied height.

This command will typically be used to create a wireframe model of underground survey data. This survey data will typically have been surveyed or digitised and then interpolated for the correct elevations, to create a completely three-dimensional floor or roof string for each drive. You are asked to identify the outline string, along with the drive height and a drive wireframe model is created based on this string and another string formed by projection. 

  * If a **positive** height is put in, it will effectively be creating a roof string. 

  * If a **negative** height is supplied, it is used for creating a floor string below. If a cell model has been opened, the drive is fully evaluated against it. The newly-created wireframe data will join any other currently available wireframe data.

### Using the 3D Solid linking method

If you have strings on adjacent sections that are to be linked together, and those strings cross each other when viewed in the direction of wireframing, then temporary vertices are inserted into the string and these temporary vertices are used when the wireframe is created. Since pairs of strings are wireframed at a time it is possible for these temporary vertices to be created for one pair of strings and not the other. In this situation a wireframe may be built which contains inconsistencies. 

Therefore, the 3D-Solid method is not suitable for use with the older linking commands if adjacent sections contain strings that cross each other in the direction of wireframing.

See [**3D Solid linking method**.](<../COMMON/3D%20Solid%20Linking%20Method.md>)

## How to use

  1. In the Current Objects toolbar, select or create a new current wireframe object.

  2. Load and select a single closed string.

  3. Run the command.

Wireframe data is generated.

Related topics and activities

  * [link-selected-outlines](<link-selected-outlines.md>)

  * [link-selected-strings-attrib ("lma")](<link-selected-strings-attrib.md>)

  * [link-selected-strings-plane ("lmpl")](<link-selected-strings-plane.md>)

  * [link-selected-strings-point ("lmpp")](<link-selected-strings-point.md>)

  * [create-drive ("cdr")](<create-drive.md>)