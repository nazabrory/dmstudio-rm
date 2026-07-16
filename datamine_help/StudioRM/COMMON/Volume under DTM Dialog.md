# Volume under DTM

To access this screen:

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-under-surface"

  * Use the quick key combination "wus".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-under-surface** and click **Run**.

Create a closed wireframe which surrounds the volume underneath the "Upper DTM" and above the "Lower DTM". 

The [wireframe-under-surface("wus")](<../command_help/wireframe-under-surface.md>) command checks that surfaces are fully intersecting. If not, a vertical sheet is added where a full intersection isn't possible, projecting upwards or downwards to the intersection with the opposing surface. As such, output volumes from this command are always watertight.

Each DTM is automatically extended (temporarily) if required in order to guarantee an intersection. This additional overhead affects the performance of the operation compared to its partner command [wireframe-under-surface-intersecting](<../command_help/wireframe-under-surface-intersecting.md>) which is quicker for the same data but assumes a clean intersection of surfaces is already in place. If you're confident a full intersection exists, this command is the one to use instead.

Once your objects have been selected (using the drop-down lists or picker tools), click OK to generate a volume.

**Note** : This command supports [**flexible wireframe selection**](<Wireframe_Selection_Concept.md>).

To create a volume between an upper and lower DTM, forcing an intersection if required:

  1. Load the wireframe data to intersect. This can be open or closed.

  2. Run the **wireframe-under-surface** command.

  3. Choose a loaded wireframe **Object** for the **Upper DTM** (the default is the current wireframe object) or selected wireframe triangle data (Selected triangles). You can select triangle data whilst the **Volume Between DTMs** screen is displayed. See [Selecting Wireframe Data](<Wireframe_Selection_Concept.md>).

**Note** : if choosing **Selected triangles** , only selected wireframe data is used to generate an enclosed volume.

  4. Choose the data to use for the **Lower DTM**. As above, **Object** data or **Selected triangles** can be used. 

  5. Create **Output** data either within the Current object, an existing wireframe object (pick it from the list) or a new object (type a new name).

  6. Click **OK**.

Related topics and activities

  * [wireframe-under-surface("wus")](<../command_help/wireframe-under-surface.md>) (command)

  * [Volume under Intersecting DTM](<Wireframe%20Volume%20under%20Intersecting%20DTM%20Dialog.md>) (with no intersection check)

  * [Volume between DTMs](<Wireframe%20Volume%20between%20intersecting%20DTMs.md>)

  * [Update DTM](<wireframe%20surface%20merge%20dialog.md>)

  * [Wireframe Project to Plane](<Wireframe%20Project%20To%20Plane%20Dialog.md>)