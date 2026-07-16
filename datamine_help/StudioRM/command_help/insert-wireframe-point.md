# insert-wireframe-point ("iwp")

See this command in the [**command table**.](<COMMAND%20TABLE_I.md#insert-wireframe-point>)

To access this command:

  * **Explicit** ribbon **Create >> Insert Point**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "insert-wireframe-point"

  * Use the quick key combination "iwp".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **insert-wireframe-point** and click **Run**.

## Command Oveview

Interactive command for inserting points in a wireframe and automatically generating the associated wireframe triangles.

New triangles are created between the new point and the vertices of the selected triangle.

The vertices of the selected triangle are highlighted, for example:

![](../Images/InsertWireframePoint1.gif)   

Click again, inside the selected triangle to position the new point dynamically with the mouse, for example:

![](../Images/InsertWireframePoint2.gif)

Command steps:

  1. In the Current Objects toolbar, set the required current wireframe.

  2. Run the command.

  3. Select the reference wireframe triangle (on or within the boundary of an existing wireframe triangle).

  4. Select (left or right-click) the location for the new wireframe point so that the resultant triangles do not create crossovers.

  5. Repeat steps 3 and 4 until all required points have been inserted.

  6. Click Cancel.

  7. Click where you wish to locate the point.

Related topics and activities

  * [copy-wireframe](<copy-wireframe.md>)

  * [ translate-wireframe](<translate-wireframe.md>)

  * [ move-wireframe](<move-wireframe.md>)

  * [move-wireframe-point](<move-wireframe-point.md>)