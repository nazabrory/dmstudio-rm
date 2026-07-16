# wf-intersect-line-switch ("twvi")

See this command in the [**command table**.](<COMMAND%20TABLE_W.md#wf-intersect-line-switch>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "wf-intersect-line-switch"

  * Use the quick key combination "twvi".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **wf-intersect-line-switch** and click **Run**.

## Command Overview

Toggle the display of crossovers between wireframe surfaces during verify.

The [wireframe-verify](<wireframe-verify.md>) command can be used to check for wireframe surfaces that intersect themselves, or intersect other surfaces. This toggle controls whether these lines of intersection are displayed. The lines can also be output as strings if the [wf-convert-line-switch](<wf-convert-line-switch.md>) toggle is on. The strings cannot be created without the display toggle set on.

Note: With this command, triangles are not split at the intersection. If this is required the [wireframe-extract-separate](<wireframe-extract-separate.md>) command should be used. The wf- intersections command can also be used to generate intersection strings for all currently displayed wireframe data, independent of group and surface selection.

Related topics and activities:

  * [wireframe-verify ("wvf")](<wireframe-verify.md>)

  * [wf-boundary-line-switch ("twvb")](<wf-boundary-line-switch.md>)

  * [wf-convert-line-switch ("twcl")](<wf-convert-line-switch.md>)
  * [wf-merge-line-switch ("twvm")](<wf-merge-line-switch.md>)
  * wf-intersect-line-switch ("twvi")