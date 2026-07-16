# drive-evaluation-switch ("tde")

See this command in the [**command table**.](<COMMAND%20TABLE_D.md#drive-evaluation-switch>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "drillhole-to-string".

  * Use the quick key combination "tde".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **drillhole-to-string** and click **Run**.

## Command Overview

Toggles on or off the evaluation of drive wireframes when created using the [link-complete-drive](<link-complete-drive.md>) or link-drive-ends commands.

  * If the drive-evaluation-switch is ON then when the drive is generated, the generated wireframe is evaluated against the loaded block model, using any current grade category filter. If no model file is open, a simple volume calculation is done. In each case, the overall drive volume and tonnage is written to a statistics file.

  * If this switch is OFF, no evaluation is performed.

Related topics and activities

  * [link-complete-drive](<link-complete-drive.md>)

  * link-drive-ends

  * [evaluate-wireframe ("evw")](<evaluate-wireframe.md>)