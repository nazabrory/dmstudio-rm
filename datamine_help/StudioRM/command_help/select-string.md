# select-string

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#select-string>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "select-string".

  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **select-string** and click **Run**.

## Command Overview

Note: Don't confuse this command with **[select-string-data-switch](<select-string-data-switch.md>)** and similar commands. These set the selection mode for strings, either to allow strings to be selected or not. In comparison, **select-string** is a command that activates string picking mode.

Select or deselect a string for further operations. Whilst this command mode is active, only string data (open or closed) can be selected in a 3D window.

This command selects a "preferred" string for certain subsequent actions. For example, the [insert-points-mode](<insert-points-mode.md>) command will only add points to a selected string. The string is selected with the cursor by pointing to it. Once a string has been selected in this way, then subsequent commands needing a selected string will use the one chosen without requesting selection. To cancel a selection, this command is also used, followed immediately by another command.

  * Strings can be added to the already selected string data by holding down <CTRL> during selection. Reselecting an already selected string will deselect it.

  * The mouse can either be clicked to select a single string, or clicked and dragged to define a selection box. Whether strings are selected by the defined box depends upon whether strings are set to be selected if all inside the box, or partly inside the box. This is controlled from the Data Selection area on the [Points and Strings](<../COMMON/Project%20Settings_Points%20and%20Strings.md>) tab of the [Project Settings](<../COMMON/ProjectSettings.md>) screen.

Related topics and activities:

  * [select-string-data-off](<select-string-data-off.md>)

  * [select-string-data-on](<select-string-data-on.md>)

  * [select-string-data-switch](<select-string-data-switch.md>)

  * [select-string-depth](<select-string-depth.md>)