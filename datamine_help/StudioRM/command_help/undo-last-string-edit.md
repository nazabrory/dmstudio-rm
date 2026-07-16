# undo-last-string-edit ("ule")

See this command in the [**command table**.](<COMMAND%20TABLE_U.md#undo-last-string-edit>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "undo-last-string-edit"

  * Use the quick key combination "ule".

  * Launch the **[Find Command](<../COMMON/findcommand.md>)** screen and locate "undo-last-string-edit", then click **Run**.

## Command Overview

Undo the last modification made during string editing. Only loaded string data can be affected when running this command (compared to the [undo-last-edit (<CTRL>+Z)](<undo-last-edit.md>) which edits the last action performed on any loaded data type).

This command will undo the effect of the very last string editing operation. For pure modifications to strings, such as those made during [delete-points-mode](<delete-points-mode.md>), the string is redrawn as it was before the last point was deleted. For commands where new strings are created, such as [copy-string](<copy-string.md>), use of undoing will delete the newly created string.

**Note** : This command will not undo actions performed by the [clip-inside-perimeter](<clip-inside-perimeter.md>) or [clip-outside-perimeter](<clip-outside-perimeter.md>) commands:

Related topics and activities

  * [undo-last-edit (<CTRL>+Z)](<undo-last-edit.md>)

  * [dtm-undo-last-link ("uld")](<dtm-undo-last-link.md>)