# wf-merge-line-switch ("twvm")

See this command in the [**command table**.](<COMMAND%20TABLE_W.md#wf-merge-line-switch>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "wf-merge-line-switch"

  * Use the quick key combination "twvm".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **wf-merge-line-switch** and click **Run**.

## Command Overview

Toggle the display of wireframe shared edges on or off during wireframe verification.

After wireframe data has been merged (or intersected) with the wireframe- merge command, the shared edges between the intersected surfaces are identified with an adjacency value of -1 (stored in the fields **TRE1ADJ** , **TRE2ADJ** , **TRE3ADJ**). Each surface component that is bounded by other intersecting surfaces is assigned a new surface number and can then be independently manipulated.

This toggle allows the shared edges, or merge lines to be displayed during the [wireframe-verify](<wireframe-verify.md>), and to be output as strings if the wf- convert-line-switch toggle is on. The strings cannot be created without the display toggle set on.

Related topics and activities:

  * [wireframe-verify ("wvf")](<wireframe-verify.md>)

  * [wf-boundary-line-switch ("twvb")](<wf-boundary-line-switch.md>)

  * [wf-convert-line-switch ("twcl")](<wf-convert-line-switch.md>)
  * [wf-intersect-line-switch ("twvi")](<wf-intersect-line-switch.md>)
  * wf-merge-line-switch ("twvm")