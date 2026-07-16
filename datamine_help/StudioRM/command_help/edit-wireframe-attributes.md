# edit-wireframe-attributes ("ewa")

See this command in the [command table](<COMMAND%20TABLE_E.md#edit-wireframe-attributes>).

To access this command:

  * **Edit** ribbon >> **Attributes >> Edit >> Edit Wireframes**

  * **Explicit** ribbon **> > Edit >> Attributes**.

  *   *   * Enter "edit-wireframe-attributes" into the **Command** toolbar and press <ENTER>

  *   * Use the quick key combination "ewa" with a 3D window active.

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **edit-wireframe-attributes** and click **Run**.

## Command Overview

Change attribute values of wireframes. Data can either be selected before or after running the command. Separate (but similar) dialogs are used to edit the attributes of **[drillholes](<edit-dh-attributes.md>)** and [block models](<edit-model-cell-values.md>).

Data from multiple data objects can be edited simultaneously if required, although only data of the same type supported by this command can be changed. 

This command displays the **[Edit Attributes](<../COMMON/edit%20attributes%20pick%20dialog.md>)** dialog.

Command Steps:

  1. Define appropriate data selection options (to ensure you can select the data, or part of the data that you need to edit).

  2. Either select your data and then run the **edit-attributes** command or vice versa. It doesn't matter which order is used.

The attributes table updates to show all unique attributes of all selected data items, plus a corresponding Value. 

     * If **Get value drop-down options from** is set to _Legend_ , a **Legend** column appears in the **Attributes** table, containing all legends available to the current project (system, user and project).

     * If **Get value drop-down options from** is set to _Selected Items_ , no **Legend** column appears in the attributes table, containing all legends available to the current project (system, user and project).

**Tip** : You can also set attribute value(s) by picking existing 3D data. This is explained in more detail below.

  3. If you wish to list all system attributes (these are used to define a data type within Studio products), check **Show system attributes** , otherwise system attributes will not appear in the **Attributes** table.

  4. If you plan to edit attribute values of multiple objects, you can choose how numeric values are displayed:

     * If Show averages is checked, the **Value** column will show the mean average of all numeric data values of the target attribute. Alphanumeric values will be listed as "Multiple". An example value will also be shown.

     * If **Show averages** is unchecked, all **Value** entries will be listed as "Multiple", along with an example value.

  5. For the attribute(s) you wish to change, select or type a _Value_ to be applied. Only values that are valid for the attribute type (numeric or alphanumeric) will be permitted

     * Alternatively, you can **Pick** attributes from another loaded data object (of a suitable data type) to transfer those attributes into the table, as described below.
  6. Where a non-system legend has been applied to an object (as indicated by the **Legend** column), you can control which element(s) of the legend are displayed alongside the selected _Value_. This is controlled using the **Legend Value Indicator** tools:

     * Show Fill: If a COLOUR field exists, this option is irrelevant as the sample fill will always be displayed, even if this option is disabled. For non-standard legends, this will show a preview of the fill type associated with the value/legend combination.
     * Show Line: If a LSTYLE field exists, the option will be ignored, as the line style preview will always be shown in the Value above. For non-standard legends, this will show a preview of the line style associated with the value/legend combination.
     * Show Symbol: If a SYMBOL field exists, the option will be ignored, as the symbol preview will always be shown. For non-standard legends, this will show a preview of the symbol associated with the value/legend combination.
  7. To transfer an attribute value to the selected data from another 3D data item, use the **Pick** button. This method can be adopted to quickly transfer attributes and their values from one object to another. 

     1. Display the 3D data that contains the desired attribute(s) in at least one 3D window. 
     2. Select **Pick**.
     3. Left or right click an object to transfer its attributes to the table. 
     4. Adjust the attribute values to the ones you want for the selected data.
  8. Select the check boxes for attributes that you wish to update. Values for all "checked" attributes will be updated on all selected data objects.

**Warning** : this will automatically add all attributes of the picked data that don't already exist in the selected object data, and this operation can't be undone.

Related Topics and Activities

  * [edit-attributes (command)](<edit-attributes.md>)
  * [edit-dh-attributes (command)](<edit-dh-attributes.md>)
  * [add-attributes (command)](<add-attributes.md>)
  * [Edit Data Attributes](<../COMMON/edit%20attributes%20pick%20dialog.md>)
  * [The Data Object Manager](<../COMMON/Data%20Manager%20Dialog.md>)
  * [Attribute Naming Conventions](<../COMMON/Attribute_Naming_Convention.md>)
  * [Edit Model Cell Values](<edit-model-cell-values.md>)