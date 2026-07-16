# extend-string ("ext")

See this command in the [**command table**.](<COMMAND%20TABLE_E.md#extend-string>)

To access this command:

  * Digitize ribbon >> Design >> Tools >> Extend.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "extend-string"

  * Use the quick key combination "ext".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **extend-string** and click **Run**.

## Command Overview

Extends a string by adding new points to its end point. Additional string points are added interactively or using the **[command line coordinate entry system](<../COMMON/Coordinates_Command%20Line.md>)**. You can also perform a combination of interactive and command line entries, which could be useful to maintain a required gradient or target 3D location.

  * Left-click to place a point without snapping, and right-click to snap to data.

  * Data selection and snapping honours the current data selection and snap settings.

  * The string is only extended from the last point \- the end of the string.

  * To extend the string from the other end, use [reverse-string](<reverse-string.md>) (to reverse the string point order) before running this command.

## Advanced Digitizing Controls

Disabled by default, this command is supported by advanced digitizing controls. Enable advanced controls using **Project Settings >> [Points and Strings](<../COMMON/Project%20Settings_Points%20and%20Strings.md>)** and check Display advanced digitizing controls. Once active you can constrain your digitizing behaviour to manage the length, gradient and azimuth of subsequent string segments. 

See [Advanced String Design](<../COMMON/advanced_string_design.md>).

**Note** : As a project setting, you must save your project to preserve this digitising mode between project sessions. The screen popup remembers its previous position.

Command steps:

  1. Run the command.

  2. Select the string to be extended.

  3. Digitize additional points or add command line coordinates.

Related topics and activities

  * [extend-segment-virtual-intersect ("esv")](<extend-segment-virtual-intersect.md>)

  * [extend-string-to-string](<extend-string-to-string.md>)

  * [reverse-string](<reverse-string.md>)

  * [Advanced String Design](<../COMMON/advanced_string_design.md>)