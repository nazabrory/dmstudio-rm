# use-modelfile-switch ("tum")

See this command in the [**command table**.](<COMMAND%20TABLE_U.md#use-modelfile-switch>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "use-modelfile-switch".

  * Use the quick key combination "tum".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **use-modelfile-switch** and click **Run**.

## Command Overview

Note: Load a block model before running this command.

Toggle the use of the loaded model slope angle and berm width values when projecting or offsetting strings.

If this mode is active, the face angle for string projection at a point is derived from the value in the cell model **SLOPE** field. This value will take preference over rosettes and the default value. If the value is absent it is ignored. 

Note: It is not possible to turn the use of the **SLOPE** field on if there is no cell model file or if the cell model file contains no SLOPE field. The initial setting is off.

The other required field is **BERMWDTH**. Current berm width settings is ignored, superseded by the **BERMWDTH** specifications, allowing different berm widths for different areas in a pit.

This toggle is generally used when running open pit design commands but can also be used with more general string offsetting commands.

Related topics and activities:

  * Open Pit Design

  * [project-string-at-angle](<project-string-at-angle.md>)

  * [offset-string](<offset-string.md>)

  * [offset-inside-string](<offset-inside-string.md>)

  * [offset-outside-string](<offset-outside-string.md>)

  * use-rosettes-switch