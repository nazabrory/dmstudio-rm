# break-string ("bs")

See this command in the [**command table**.](<commandtable_B.md#break-string>)

To access this command:

  * **Digitize** ribbon **> > Tools >> Break**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "break-string"

  * Use the quick key combination "bs".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **break-string** and click **Run**.

## Command Overview

Breaks a string at a selected point. Any string can be broken at any point.

All string fragments created with this command stay within the original object. If custom attributes exist on the string being broken, both resulting segments contain the custom attributes. **COLOUR** , **LSTYLE** and **SYMBOL** attributes also transfer to the created string segments.

Command steps:

  1. (Optionally) select string data in a **3D** view.
  2. Run the command.

The message area of the **Status** bar prompt shows either "...BREAK point on ANY string" if there no selected string, or "...BREAK point on SELECTED string" if there is already a selected string.

  2. Select the break point, and a new string vertex is added at the cursor position. The shape of the string is unchanged. You can also use right-click snapping to pick a point. See [Snapping Settings](<../COMMON/SnapSettings.md>).

  3. Complete the command by double-clicking or tapping anywhere in a **3D** window.

Related topics and activities

  * [break-strings](<break-strings.md>)

  * [break-string-with-string](<break-string-with-string.md>)