# Wireframe Section

To access this screen:

  * **Wireframe** ribbon **> > Plane >> Section**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-section"

  * Use the quick key combination "csl".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-section** and click **Run**.

Create a string where a defined plane intersects a wireframe object or preselected wireframe triangle data. Output strings inherit their colour from the original wireframe.

**Note** : This command supports [**flexible wireframe selection**](<Wireframe_Selection_Concept.md>).

To create a string at the intersection of a wireframe and a 3D section plane:

  1. Load the open wireframe data to be sectioned.

  2. Define a section that represents the plane to use to create a closed intersection string. See [3D Sections Menu](<../VR_Help/workspace_sections.md>).

  3. Run the **wireframe-section** command.

  4. Choose a loaded wireframe Object (the default is the current object) or selected wireframe triangle data (Selected triangles). You can select triangle data whilst the **Project to Plane** screen is displayed. See [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>).

**Note** : if choosing **Selected triangles** , string data is produced at the intersection of selected wireframe data and the section only.

  5. Define the **Plane Orientation** of the 3D plane:

     * Horizontalset the plane to be horizontal (i.e. both Azimuth and Inclination are 0 degrees).
     * North-Southset the plane to a vertical North-South orientation (i.e. Azimuth is 90 degrees and Inclination is -90 degrees).

     * East-Westset the plane to a vertical East-West orientation (i.e. Azimuth is 0 degrees and Inclination is -90 degrees).

     * 3D Sectionif any [sections have been defined in the active 3D window](<../VR_Help/workspace_sections.md>), these section planes can be used to generate section string data. 

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

  8. Output: you can output data either within the Current object, an existing wireframe object (pick it from the list) or a new object (type a new name).

  9. Click **OK**.

Output data is created and the projected wireframe volume displays.

Related topics and activities

  * [wireframe-section ("csl")](<../command_help/wireframe-section.md>) (command)

  * [Wireframe Multiple Section ](<Wireframe%20Section%20Multiple%20Dialog.md>)

  * [wireframe-section-multiple ("msl")](<../command_help/wireframe-section-multiple.md>)

  * [Hull to Strings](<hull%20to%20strings%20dialog.md>)

  * [Strings from Intersections](<Wireframe%20Strings%20From%20Intersections%20Dialog.md>)

  * [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>)