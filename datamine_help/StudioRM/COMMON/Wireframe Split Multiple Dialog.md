# Wireframe Split Multiple

To access this screen:

  * **Wireframe** ribbon **> > Plane >> Multiple Split**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-split-multiple"

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-split-multiple** and click **Run**.

Splits a selected wireframe object, or preselected wireframe triangle data, into several wireframes along the intersections with parallel, equally-spaced planes. Output strings inherit their colour from the original wireframe.

**Note** : This command supports [**flexible wireframe selection**](<Wireframe_Selection_Concept.md>).

To split a wireframe (potentially multiple times) using a section:

  1. Load the wireframe data to be sectioned. This can be open or closed.

  2. Define a section for cutting the wireframe. All sections are parallel to this one. See [3D Sections Menu](<../VR_Help/workspace_sections.md>).

  3. Run the **wireframe-split-multiple** command.

  4. Choose a loaded wireframe Object (the default is the current object) or selected wireframe triangle data (Selected triangles). You can select triangle data whilst the **Project to Plane** screen is displayed. See [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>).

**Note** : if choosing **Selected triangles** , only selected wireframe data is split. This can be useful to partially cut a wireframe multiple times, for example.

  5. Define the **Plane Orientation** of the 3D cutting section plane. The input wireframe is split at the intersection with the section.

     * Horizontalset the plane to be horizontal (i.e. both Azimuth and Inclination are 0 degrees).
     * North-Southset the plane to a vertical North-South orientation (i.e. Azimuth is 90 degrees and Inclination is -90 degrees).

     * East-Westset the plane to a vertical East-West orientation (i.e. Azimuth is 0 degrees and Inclination is -90 degrees).

     * 3D Sectionif any [sections have been defined in the active 3D window](<../VR_Help/workspace_sections.md>), one of them can be the 'origin' section from which other sections at equal spacing are derived.

Click to transfer the azimuth and dip of the section to the relevant fields. The _Default Section_ option is listed alongside any custom sections that exist for your project.

     * Azimuthset the azimuth of the section plane manually. 

Note: this field is automatically overwritten if any of the preset options are selected.

     * Inclinationset the inclination of the section plane manually.

Note: this field is automatically overwritten if any of the preset options are selected.

  6. Define the position of the section's center point using the **Plane Reference Point** values. Define **X** , **Y** and **Z**.

  7. Pick the **Spacing** between your sections. Wireframe data is split at the original section and at this distance above or below the section, throughout the data. Smaller values tend to produce more sectional splits.

  8. As an alternative to explicitly defining the plane orientation you can use one of the following automatic options:

     * Use View Planefix the plane as the current view plane in the currently active 3D window.

     * Pick Faceclick to select a wireframe face in the 3D window. 

The **Azimuth** and Inclination update to reflect the orientation of the picked face and the **Plane Reference Point** (see above) updates to the coordinates of the selected point. This option fully defines the plane in 3D space.

  9. Create **Output** data either within the Current object, an existing wireframe object (pick it from the list) or a new object (type a new name).

Multiple wireframe objects arise after splitting, so you can choose Multiple New Objects to generate multiple separate objects, with each containing one element of the output. Once enabled, you can either select the default prefix of "String Split:" or enter any prefix you like; objects are generated with the prefix and an ID, e.g. "String Split:1", "String Split:2" and so on.

Before you create the new objects, a message is displayed to indicate the number of objects that are created.

  10. Choose if you wish to cap the new data so that it forms closed solids (Cap Ends). If splitting an open wireframe, this setting has no effect.

     * If **Cap Ends** is **checked** , each resulting wireframe entity (after splitting) is closed.

     * If **Cap Ends** is **unchecked** , split wireframe entities will not be closed.

  11. Optionally, choose a **Split Column**. This is an attribute of the output wireframe that denotes which triangle belongs to which distinct 'split' (a numeric value is assigned, for example "0" and "1" for each side of the section. This can be useful if outputting to a single object.

  12. Click **OK** to generate your output.

Related topics and activities

  * [wireframe-split-multiple](<../command_help/wireframe-split-multiple.md>) (command)

  * [Wireframe Split](<Wireframe%20Split%20Dialog.md>)

  * [Wireframe Split by String](<Wireframe%20Split%20By%20String%20Dialog.md>)

  * [Wireframe Section](<Wireframe%20Section%20Dialog.md>)

  * [Wireframe Multiple Section ](<Wireframe%20Section%20Multiple%20Dialog.md>)

  * [Wireframe Multiple Section ](<Wireframe%20Section%20Multiple%20Dialog.md>)

  * [Hull to Strings](<hull%20to%20strings%20dialog.md>)

  * [Strings from Intersections](<Wireframe%20Strings%20From%20Intersections%20Dialog.md>)

  * [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>)