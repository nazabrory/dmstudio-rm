# Scale Object

To access this screen:

  * **Explicit** ribbon **> > Edit >> Scale**.

  * Enter "scale-wireframe" into the **Command** toolbar and press <ENTER>

  * Display the **[Find Command](<findcommand.md>)** screen, locate **scale-wireframe** and click **Run**.

Interactive command to scale wireframe data on one or more axis directions. 

This command scales data about a point which can be the wireframe center or its centroid, or any user-defined point.

This command can be used to scale entire wireframe objects or partial wireframe data including selected triangles. Where part of a wireframe object is scaled, Studio will attempt to retain links, preserving the integrity of surrounding data. For example, if part of a volume is scaled, the result will remain as a closed volume.

**Note** : This command supports [**flexible wireframe selection**](<Wireframe_Selection_Concept.md>).

Command steps:

  1. Select the wireframe that your wish to scale. See [Wireframe Data Selection](<selecting_wireframes.md>).

  2. Run the command. The Scale Object screen displays.

  3. Enter the Scale By values that you wish to apply to the wireframe in X, Y and Z directions.

  4. Select the point that the wireframe will rotate about, or use the picking tool to specify a point.

  5. Click Scale. This will scale the selected wireframe data as specified.

Related topics and activities

  * [scale-wireframe](<../command_help/scale-wireframe.md>)

  * [Selecting Wireframes](<selecting_wireframes.md>)