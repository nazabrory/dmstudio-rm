# edit-model-cell-values ("ecv")

See this command in the [command table](<COMMAND%20TABLE_E.md#edit-model-cell-values>).

To access this command:

  * **Model** ribbon **> > Manipulate >> Edit Cells**.

  * **Digitize** ribbon **> > Attributes >> Add**.

  * Enter "edit-model-cell-values" into the **Command** toolbar and press <ENTER>

  * Use the quick key combination "ecv" with a 3D window active.

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **edit-model-cell-values** and click **Run**.

## Command Overview

Change attribute values of block model cells interactively. 

**Note** : This command only permits the update of one cell or subcell at a time.

This command displays the **[Edit Attributes](<../COMMON/edit%20attributes%20pick%20dialog.md>)** screen.

Command Steps:

  1. Load the block model to be edited and display a relevant aspect in any 3D window.

  2. Launch the **edit-model-cell-values** command.

The **Edit Block Model Cell Values** screen displays.

  3. If you wish to list all system attributes (these are used to define a data type within Studio products), check **Show system attributes** , otherwise system attributes will not appear in the **Attributes** table.

  4. For the attribute(s) you wish to change, select or type a _Value_ to be applied. Only values that are valid for the attribute type (numeric or alphanumeric) is permitted

     * Alternatively, you can **Pick** attributes from another loaded data object (of a suitable data type), as described below.
  5. Where a non-system legend has been applied to an object (as indicated by the **Legend** column), you can control which element(s) of the legend are displayed alongside the selected _Value_. This is controlled using the **Legend Value Indicator** tools:

     * Show Fill: If a COLOUR field exists, this option is irrelevant as the sample fill will always be displayed, even if this option is disabled. For non-standard legends, this will show a preview of the fill type associated with the value/legend combination.
     * Show Line: If a LSTYLE field exists, the option is ignored, as the line style preview will always be shown in the Value above. For non-standard legends, this will show a preview of the line style associated with the value/legend combination.
     * Show Symbol: If a SYMBOL field exists, the option is ignored, as the symbol preview will always be shown. For non-standard legends, this will show a preview of the symbol associated with the value/legend combination.
  6. To transfer an attribute value to the selected data from another 3D data item, use the **Pick** button. This method can be adopted to quickly transfer attributes and their values from one object to another. 

     1. Display the 3D data that contains the desired attribute(s) in at least one 3D window. 
     2. Select **Pick**.
     3. Left or right click an object to transfer its attributes to the table. 
     4. Adjust the attribute values to the ones you want for the selected data.
  7. Select the check boxes for attributes that you wish to update. Values for all "checked" attributes are updated on all selected data objects.

**Warning** : this will automatically add all attributes of the picked data that don't already exist in the selected object data, and this operation can't be undone.

Related Topics and Activities

  * [edit-attributes (command)](<edit-attributes.md>)
  * [edit-dh-attributes (command)](<edit-dh-attributes.md>)
  * [add-attributes (command)](<add-attributes.md>)
  * [Edit Data Attributes](<../COMMON/edit%20attributes%20pick%20dialog.md>)
  * [The Data Object Manager](<../COMMON/Data%20Manager%20Dialog.md>)
  * [Attribute Naming Conventions](<../COMMON/Attribute_Naming_Convention.md>)