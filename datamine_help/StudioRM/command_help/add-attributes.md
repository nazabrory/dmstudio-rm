# add-attributes ("nat")

See this command in the [**command table**.](<_COMMAND%20TABLE_A.md#add-attributes>)

To access this command:

  * Data ribbon >> Attributes >> Add

  * **Digitize** ribbon **> > Attributes >> Add**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter `add-attributes`

  * Use the quick key combination "nat"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate _add-attributes_ and click **Run**.

## Command Overview

Add a new attribute (column) to an object in memory.

**Note** : Modern Studio applications permit attribute names up to 24 characters in most cases. There are exceptions, such as where an attribute name is automatically prefixed or suffixed by another function, for example. See [**Attribute Naming Conventions**](<../COMMON/Attribute_Naming_Convention.md>). Older versions of Studio products were limited to attribute names up to 8 characters.

## About Attributes

Attributes can be an alphanumeric or numeric, and are restricted to 24 characters in most cases (restrictions exist for specific processes - detailed in individual help files).

If you attempt to add an attribute name that already exists in the selected object, a warning will be displayed and it will not be added. Similarly, restricted Datamine attribute names cannot be used. 

  * Attributes must not start with the following characters: "*", "&", "@", "!", "?", ".".

  * Attributes must not contain spaces, or the following characters: ",", "!", " :", "*", "&", "=", "()".

## Default Attribute Values

When adding attributes, you must specify a default value. This will be used in the absence of other data values. You can choose any default value you like, providing it is of an appropriate type.

  * **Alphanumeric attributes** : the 'default default' is a hyphen, a special character indicating absent data. You can choose any other value, numeric or otherwise to be the default value.

  * **Numeric attributes** : default values can be any numeric value, but can also be a hyphen, representing absent numeric data. Note that this is not the same as zero. 

Command Steps:

  1. Running the command opens the [Add Column ](<../COMMON/AddColumn_Dialog.md>)screen.

**Note:** This screen can also be accessed from the context menu of the **Loaded Data** control bar: right-click a loaded data object, and select **Add Column**. 

  2. Select the Object in memory to be modified. 

Note: If you launched this screen from the Loaded Data control bar, only the selected object is listed.

  3. Complete the following fields as required:

     * **Name**

     * **Type**

     * **Default Value** (see "Default Values")

     * **Length** (alphanumeric attributes only)

       * Column lengths must be specified as a multiple of 4 

## Script Support

The `AddColumn` method on the `ObjectData.Schema` class can be accessed via the `IDmOverlay` interface.  
  
The format for scripting this command is:  
  
IDmOverlay->ObjectData.Schema.AddColumn

Related topics and activities

  * [Attribute Naming Convention](<../COMMON/Attribute_Naming_Convention.md>)

  * [Manage Object Attributes](<../COMMON/Attribute_Manager.md>)

  * [edit-attributes ("eat")](<edit-attributes.md>)

  * [edit-dh-attributes ("ed")](<edit-dh-attributes.md>)

  * [edit-wireframe-attributes ("ewa")](<edit-wireframe-attributes.md>)

  * [File Types](<../COMMON/filetype.md>)