# Add an Attribute to an Object

Add a data attribute to a loaded data object. 

Attributes can either be **[numeric, alphanumeric or calculated](<Attributes.md>)**. Alphanumeric attributes are constrained to a length limit (where length is measured in number of characters). This limit will depend on the **[mode](<Attribute_Naming_Convention.md>)** of your system. 

**Note** : In the context of object or table data, "column", "field" and "attribute" have the same meaning. "Attribute" is used throughout Studio documentation.

Activity Steps

  1. Display the **Add Column** screen:
     * In the [Loaded Data](<Loaded%20Data%20Control%20Bar.md>) control bar, right-click an object and select Add Column.
     * Run [add-attributes](<../command_help/add-attributes.md>). 
     * In a 3D or Plots window, use the quick keys "nat".

     * Activate the Edit ribbon and select Attributes >> Edit Attributes.

  2. Select an **Object** to append. If you right-clicked an object to display the **Add Column** dialog, that object is listed automatically.

  3. Decide which **Type** of attribute is appropriate:

     * _Numeric_ attributes store number values or an absent indicator ("-").

     * _Alphanumeric_ attributes store any data value and are considered text, not numbers. An absent indicator ("-") is also supported.

     * _Calculated_ attributes will store automatically generated values, such as an open string's _Length_ , or a closed string's _Area_.

Note: _Calculated_ string attributes are stored with fixed, reserved names. They are prefixed with an underscore, e.g. "_AREA". All entries in this list other than _Numeric_ and _Alphanumeric_ are calculated attribute types. See [Attributes](<Attributes.md>).  

  4. Enter an attribute **Name** , up to a **[maximum length limit](<Attribute_Naming_Convention.md>)**.

  5. For _Alphanumeric_ attributes, specify a **Length**. This is the maximum number of characters the attribute can store.

  6. Set a **Default Value** which is used in place of empty records. This is commonly a hyphen ("-") representing absent data, but can be any value the attribute supports.

**Important** : Numeric data expressed as "-" is not the same as zero. Zero is a measured quantity and can influence the results of application calculations in a different way to absent data, where the record is considered to be missing.

Related Information and Activities

  * [Attribute Naming Convention](<Attribute_Naming_Convention.md>)

  * [add-attributes command](<../command_help/add-attributes.md>)

  * [Attribute Manager](<Attribute_Manager.md>)

  * [Edit Attributes](<edit%20attributes%20pick%20dialog.md>)