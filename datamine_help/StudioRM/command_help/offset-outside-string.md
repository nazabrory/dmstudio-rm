# offset-outside-string ("oos")

See this command in the [**command table**.](<COMMAND%20TABLE_O.md#offset-outside-string>)

To access this command:

  * **Digitize** ribbon **> > Tools >> Offset >> Expand**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "offset-outside-string"

  * Use the quick key combination "oos".

  * Open the **[Find Command](<../COMMON/findcommand.md>)** screen, locate "**offset-outside-string** " and click **Run**.

## Command Overview

Creates a new string/perimeter inside the selected string/perimeter, in the plane of the current view plane, by expanding the selected string/perimeter by the specified distance.

This command can either work with preselected data or without (in which case, a string must be selected when the command is activated.

The specified offset is applied perpendicular to each segment of the string.

#### Switches Affecting Offsets

  * If a rosettes file is currently loaded and use-rosettes-switch is toggled ON, the expansion distance is derived from the berm width value(s) in the **ROSBWID** field of the rosette file.

  * If a suitable block model is loaded and the [use-modelfile-switch](<use-modelfile-switch.md>) is toggled ON, the expansion distance is derived from the berm width value(s) in the **BERMWDTH** field of the block model file.

Command steps

  1. Select the required string(s) or perimeter(s).

  2. Run the command.

  3. Enter the **Expansion Distance**.

  4. Click **OK**.

The string offset is applied.

Related topics and activities

  * [offset-string ("exp")](<offset-string.md>)

  * [offset-inside-string ("ois")](<offset-inside-string.md>)

  * [project-string-at-angle](<project-string-at-angle.md>)

  * [use-modelfile-switch](<use-modelfile-switch.md>)

  * se-rosettes-switch