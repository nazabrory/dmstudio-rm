# assign-attributes-by-selection-order ("abso")

See this command in the [**command table**.](<_COMMAND%20TABLE_A.md#attributes-from-perimeters>)

To access this command:

  * **Data** ribbon **> > Attributes >> By Selection Order**.

  * **Digitize** ribbon **> > Attributes >> By Selection Order**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "assign-attributes-by-selection-order"

  * Use the quick key combination "abso".
  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **assign-attributes-by-selection-order** and click **Run**.

## Command Overview

This command displays the [Assign Attributes by Selection Order](<../COMMON/AssignAttributesBySelectionOrder.md>) screen to attribute loaded string, drillhole or wireframe data based on either the order of manual data selection or the location and direction of a loaded string.

[![](../Images/AttributesBySelectionOrder2.png)](<javascript:void\(0\);>)

Stope volume attribute values added due to their presence in relation to a loaded string (shown in orange with arrows)

It can be useful to define a series of sequenced labels along a string or set of points. For example, assigning a stope index to wireframe volumes along the direction of development, assigning a blasthole row ID throughout a blast pattern and so on. A sequential index can also be useful to create spatial indices that can be used for dependency creation, control / guide schedule sequencing, mapping different areas of the reserve or mine and many other uses.

Command steps:

  1. Load the data you wish to attribute and ensure it is visible in a **3D** window.

  2. Ensure you data selection settings are configured to allow selection of data in a 3D window. See [Selecting 3D Data Interactively](<../COMMON/Selecting3DDataInteractively.md>).

  3. Load the target points, strings, drillholes or wireframe data to receive the new attribute values.

  4. Run the **assign-attributes-by-selection-order** command.

The **Assign Attributes by Selection Order** screen displays. 

  5. Fill out the fields on this screen as described here: [Assign Attributes by Selection Order](<../COMMON/AssignAttributesBySelectionOrder.md>).

  6. Click **Apply** to update the target data and dismiss the **Assign Attributes by Selection Order** screen.  

Related topics and activities

  * [Assign Attributes by Selection Order](<../COMMON/AssignAttributesBySelectionOrder.md>)

  * [attributes-from-perimeters ("afp")](<attributes-from-perimeters.md>)

  * [edit-attributes ("eat")](<edit-attributes.md>)

  * [edit-dh-attributes ("ed")](<edit-dh-attributes.md>)

  * [edit-wireframe-attributes ("ewa")](<edit-wireframe-attributes.md>)

  * [Selecting 3D Data Interactively](<../COMMON/Selecting3DDataInteractively.md>)