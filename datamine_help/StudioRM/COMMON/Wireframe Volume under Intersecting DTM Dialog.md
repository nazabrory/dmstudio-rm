# Volume under Intersecting DTM

To access this screen:

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-under-surface-intersecting"

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-under-surface-intersecting** and click **Run**.

Create a closed wireframe which surrounds the volume underneath the "Upper DTM" and above the "Lower DTM". The DTMs must intersect.

This command assumes that surfaces are fully intersecting (i.e. the intersection line is fully closed) as no checks are made to assess this. This makes it a rapid command to use when you have high confidence that input objects intersect each other fully. If not, unexpected results may occur. If you would like to check if your surfaces are fully-intersecting first, and extend surfaces if required, use [wireframe-under-surface](<../command_help/wireframe-under-surface.md>) instead.

Once your objects have been selected (using the drop-down lists or picker tools), click OK to generate a volume.

The order of upper and lower DTM is important for this command; **Upper DTM** must be above **Lower DTM** in at least one area for a volume to be created.

**Note** : This command supports [**flexible wireframe selection**](<Wireframe_Selection_Concept.md>).

To create a volume between an upper and lower DTM:

  1. Load the wireframe data to intersect. This can be open or closed.

  2. Run the **wireframe-under-surface-intersecting** command.

  3. Choose a loaded wireframe **Object** for the **Upper DTM** (the default is the current wireframe object) or selected wireframe triangle data (Selected triangles). You can select triangle data whilst the **Volume Between DTMs** screen is displayed. See [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>).

**Note** : if choosing **Selected triangles** , only selected wireframe data is used to generate an enclosed volume.

  4. Choose the data to use for the **Lower DTM**. As above, **Object** data or **Selected triangles** can be used. 

  5. Create **Output** data either within the Current object, an existing wireframe object (pick it from the list) or a new object (type a new name).

  6. Click **OK**.

Related topics and activities

  * [wireframe-under-surface-intersecting ("wus")](<../command_help/wireframe-under-surface-intersecting.md>) (command)

  * [Volume under DTM](<Volume%20under%20DTM%20Dialog.md>) (with intersection check)

  * [Volume between DTMs](<Wireframe%20Volume%20between%20intersecting%20DTMs.md>)

  * [Update DTM](<wireframe%20surface%20merge%20dialog.md>)

  * [Wireframe Project to Plane](<Wireframe%20Project%20To%20Plane%20Dialog.md>)