# Attribute Naming Convention

Attributes (also known as fields, properties or columns) are an important component of your data; they can control the visual appearance of a loaded file, or can be contained 'silently' within any data object as a means of storing data values. They can be added to new files or objects, including geological data (tables, drillholes, sample points, geological string and wireframe models), as well as mine planning data (planning outlines, mine design strings and wireframes).

  * An attribute can be either Numeric or Alphanumeric.

  * A table must contain unique attribute names - no two fields can be identical in name.

Your product supports attribute names up to 24 characters in length.

To retain compatibility with older software versions, if running "Short field mode", you will only be able to generate attribute names up to 8 characters by default. You can swap from a "short field" to a "long field" system. Actually, in some cases, the attribute length may be further restricted, for example where a process automatically applies a prefix or suffix to a field name, so a shorter base name is required.

To swap from a swap from a "short field" to a "long field" system:

You can swap between attribute length modes using the **Help >> About** screen.

  1. Expand the Help menu (top right of the screen).

  2. Select **About...**.

  3. Click **Manage...**.

  4. Check or uncheck **Use Long Field Names**.

  5. **Close** your application (remember to save your project and data).

  6. Log out of Windows and back in (this is required in order to register system settings). 

Studio products now operate in the selected mode with the current login.

## Excessively Long Field Names - What Happens?

Your system adopts the following behaviour if a field name is detected that is longer than the permitted limit:

  * When data is written to a file, excessively long attributes are truncated.

    * Unless the file is saved in the legacy system, the longer field names will still exist within the table - but only the first 8 characters are displayed in the legacy system.

  * If truncation occurs and it introduces a duplicate field name, only the first field is preserved. Subsequent (identically-named) fields are removed.

  * Where data is imported, excessively long attributes are truncated.

  * In specific cases, such as DILUTMOD, a lower limit is required in order to accommodate automatically-generated (and prefixed) field names.

**Warning** : In general, if you are working in a mixed-application environment where both 'short field' and 'long field' systems are in active use and data is transferred between them, you should retain an 8-character limit for field names. If you adopt a longer field naming convention, you should consider your data bound to post-2018 releases of Studio products. If in doubt, contact your local Datamine representative for advice.

## Illegal Names

  * Restricted Datamine field names cannot be used.

  * If you attempt to add an attribute name that already exists in the selected object, a warning is displayed and the attribute will not be added.

##  Illegal Characters

  * Attributes must not start with the following characters: "*", "&", "@", "!", "?", "." or "_"

  * Attributes must not contain spaces, or the following characters: ",", "!", " :", "*", "&", "=", "()".

**Note** : The underscore character, "_" can be used instead of a space within an attribute but should not be used at the start of an attribute as this can cause process such as INPUTD or INPFIL to terminate early.

Related topics and activities

  * [Attributes](<Attributes.md>)

  * [Add Column Screen](<AddColumn_Dialog.md>)