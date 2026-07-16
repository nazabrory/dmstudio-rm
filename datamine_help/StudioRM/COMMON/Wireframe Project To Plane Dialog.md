# Wireframe Project to Plane

To access this screen:

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-surface-project"

  * Use the quick key combination "pdv".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-surface-project** and click **Run**.

Project an open wireframe or selected triangles representing a Digital Terrain Model (DTM), onto a defined plane, perpendicular to that plane. Projecting a DTM to a plane always produces a closed object. 

The **Project to Plane** screen is the user interface for the **[wireframe-surface-project](<../command_help/wireframe-surface-project.md>)** command.

Input data must have no overlapping faces when viewed along the direction of the plane normal. This is not checked before the operation, but any intersecting faces in the projected object are reported.

**Note** : This command supports [**flexible wireframe selection**](<Wireframe_Selection_Concept.md>).

To project an open wireframe onto a planar surface:

  1. Load the open wireframe data to be projected.

  2. Define a section that represents the plane to use for projection. See [3D Sections Menu](<../VR_Help/workspace_sections.md>).

  3. Run the **wireframe-surface-project** command.

  4. Choose a loaded wireframe Object (the default is the current object) or selected wireframe triangle data (Selected triangles). You can select triangle data whilst the **Project to Plane** screen is displayed. See [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>).

  5. Define the **Plane Orientation** of the 3D plane to which the DTM is projected:

     * Horizontalset the plane to be horizontal (i.e. both Azimuth and Inclination are 0 degrees).
     * North-Southset the plane to a vertical North-South orientation (i.e. Azimuth is 90 degrees and Inclination is -90 degrees).

     * East-Westset the plane to a vertical East-West orientation (i.e. Azimuth is 0 degrees and Inclination is -90 degrees).

     * 3D Sectionif any [sections have been defined in the active 3D window](<../VR_Help/workspace_sections.md>), these section planes can be used as the target for projection. Click this button to transfer the azimuth and dip of the section to the relevant fields. The _Default Section_ option is listed alongside any custom sections that exist for your project.

     * Azimuthset the azimuth of the plane manually. 

Note: this field is automatically overwritten if any of the preset options are selected.

     * Inclinationset the inclination of the plane manually.

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

  * [wireframe-surface-project ("pdv")](<../command_help/wireframe-surface-project.md>) (command)

  * [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>)