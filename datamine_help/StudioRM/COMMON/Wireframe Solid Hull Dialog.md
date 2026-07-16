# Wireframe Solid Hull

To access this screen:

  * **Wireframe** ribbon **> > Boolean >> Solid Hull**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-solid-hull"

  * Use the quick key combination "soh".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-solid-hull** and click **Run**.

Generate the outer surface of overlapping solid wireframes. 

This performs the equivalent of a series of [wireframe-union](<Wireframe%20Union%20Dialog.md>) operations on pairs of wireframes until all the outer surfaces are combined into a single solid shape. Resolves any overlaps in the selected wireframe.

More than one wireframe surface must be present in the selected wireframe object, or selected triangle data, for this command to be used. All surfaces are combined into a single 3D hull object.

**Note** : This command supports [**flexible wireframe selection**](<Wireframe_Selection_Concept.md>).

To generate a single wireframe that encloses all selected wireframe data:

  1. Load the open wireframe data. This should either be multiple wireframe objects, or one object containing multiple volumes.

  2. Run the **wireframe-solid-hull** command.

  3. Choose a loaded wireframe Object (the default is the current object) or selected wireframe triangle data (Selected triangles). You can select triangle data whilst the **Project to Plane** screen is displayed. See [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>).

**Note** : if choosing **Selected triangles** , section string data is produced at the intersection of selected wireframe data and the section intervals only.

  4. Optionally, define a **Key field** that isolates individual wireframes within the input data. This data is copied to the output hull object.

  5. Create **Output** data either within the Current object, an existing wireframe object (pick it from the list) or a new object (type a new name).

  6. Click **OK**.

Related topics and activities

  * [wireframe-solid-hull ("soh")](<../command_help/wireframe-solid-hull.md>) (command)

  * [Wireframe Difference](<Wireframe%20Difference%20Dialog.md>)

  * [Wireframe Extract Separate](<Wireframe%20Extract%20Separate%20Dialog.md>)

  * [Wireframe Intersection](<Wireframe%20Intersection%20Dialog.md>)

  * [Wireframe Union](<Wireframe%20Union%20Dialog.md>)

  * [Strings from Intersections](<Wireframe%20Strings%20From%20Intersections%20Dialog.md>)

  * [Boolean operations](<boolean_operations.md>)

  * [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>)