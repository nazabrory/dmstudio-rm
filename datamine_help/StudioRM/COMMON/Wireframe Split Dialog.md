# Wireframe Split

To access this screen:

  * **Wireframe** ribbon **> > Plane >> Split**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-split"

  * Use the quick key combination "spli".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-split** and click **Run**.

Splits a wireframe or selected triangle data into two parts using a section plane. Data is created either as a wireframe object or to multiple objects. 

This is the user interface for the [wireframe-split ("spli")](<../command_help/wireframe-split.md>) command.

To split a wireframe (once) using a section:

  1. Load the wireframe data to be sectioned. This can be open or closed.

  2. Define a section for cutting the wireframe. See [3D Sections Menu](<../VR_Help/workspace_sections.md>).

  3. Run the **wireframe-split** command.

  4. Choose a loaded wireframe Object (the default is the current object) or selected wireframe triangle data (Selected triangles). You can select triangle data whilst the **Project to Plane** screen is displayed. See [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>).

**Note** : if choosing **Selected triangles** , only selected wireframe data is split. This can be useful to partially cut a wireframe, for example.

  5. Define the **Plane Orientation** of the 3D cutting section plane. The input wireframe is split at the intersection with the section.

     * Horizontalset the plane to be horizontal (i.e. both Azimuth and Inclination are 0 degrees).
     * North-Southset the plane to a vertical North-South orientation (i.e. Azimuth is 90 degrees and Inclination is -90 degrees).

     * East-Westset the plane to a vertical East-West orientation (i.e. Azimuth is 0 degrees and Inclination is -90 degrees).

     * 3D Sectionif any [sections have been defined in the active 3D window](<../VR_Help/workspace_sections.md>), these section planes can be used to control the projection angle of the cutting string.

Click to transfer the azimuth and dip of the section to the relevant fields. The _Default Section_ option is listed alongside any custom sections that exist for your project.

     * Azimuthset the azimuth of the section plane manually. 

Note: this field is automatically overwritten if any of the preset options are selected.

     * Inclinationset the inclination of the section plane manually.

Note: this field is automatically overwritten if any of the preset options are selected.

  6. Define the position of the section's center point using the **Plane Reference Point** values. Define **X** , **Y** and **Z**.

  7. As an alternative to explicitly defining the plane orientation you can use one of the following automatic options:

     * Use View Planefix the plane as the current view plane in the currently active 3D window.

     * Pick Faceclick to select a wireframe face in the 3D window. 

The **Azimuth** and Inclination update to reflect the orientation of the picked face and the **Plane Reference Point** (see above) updates to the coordinates of the selected point. This option fully defines the plane in 3D space.

  8. Create **Output** data either within the Current object, an existing wireframe object (pick it from the list) or a new object (type a new name).

Multiple wireframe objects arise after splitting, so you can choose Multiple New Objects to generate multiple separate objects, with each containing one element of the output. Once enabled, you can either select the default prefix of "String Split:" or enter any prefix you like; objects are generated with the prefix and an ID, e.g. "String Split:1", "String Split:2" and so on.

Before you create the new objects, a message is displayed to indicate the number of objects that will be created.

  9. Choose if you wish to cap the new data so that it forms closed solids (Cap Ends). If splitting an open wireframe, this setting has no effect.

     * If **Cap Ends** is **checked** , each resulting wireframe entity (after splitting) is closed.

     * If **Cap Ends** is **unchecked** , split wireframe entities will not be closed.

  10. Optionally, choose a **Split Column**. This is an attribute of the output wireframe that denotes which triangle belongs to which distinct 'split' (a numeric value is assigned, for example "0" and "1" for each side of the section. This can be useful if outputting to a single object.

  11. Click **OK** to generate your output.

Related topics and activities

  * [wireframe-split ("spli")](<../command_help/wireframe-split.md>) (command)

  * [Wireframe Split by String](<Wireframe%20Split%20By%20String%20Dialog.md>)

  * [Wireframe Section](<Wireframe%20Section%20Dialog.md>)

  * [Wireframe Multiple Section ](<Wireframe%20Section%20Multiple%20Dialog.md>)

  * [Wireframe Multiple Section ](<Wireframe%20Section%20Multiple%20Dialog.md>)

  * [Hull to Strings](<hull%20to%20strings%20dialog.md>)

  * [Strings from Intersections](<Wireframe%20Strings%20From%20Intersections%20Dialog.md>)

  * [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>)