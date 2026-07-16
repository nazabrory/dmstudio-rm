# edit-hole-attribute

See this command in the [command table](<COMMAND%20TABLE_E.md#edit-hole-attribute>).

To access this command:

  *   *   * Enter "edit-hole-attribute" into the **Command** toolbar and press <ENTER>

Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **edit-hole-attribute** and click **Run**.

## Command Overview

Edit the properties of a drillhole data column. This command is unusual in that the command name requires a field to be added as a suffix. For example, if you wish to edit the LITH attribute value of a loaded drillhole, the command required is "edit-hole-attribute-LITH".

**Note** : running this command without a field suffix will result in a message indicating the command is unrecognised.

Command Steps:

  1. Load static drillhole data.
  2. Launch the edit-hole attribute command with a field name as an extension, e.g. "edit-hole-attribute-ZONE". 

Note: The specified field name must be present on the current drillhole object

  3. Pick a point on the loaded drillhole object

  4. Enter the new attribute value to be applied at the selected location.
  5. Click **OK**.

The loaded drillhole object is updated to reflect the new attribute value assignment.

Related Topics and Activities

  * [edit-dh-attributes](<edit-dh-attributes.md>)