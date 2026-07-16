# wf-boundary-line-switch ("twvb")

See this command in the [**command table**.](<COMMAND%20TABLE_W.md#wf-boundary-line-switch>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "wf-boundary-line-switch"

  * Use the quick key combination "twvb".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **wf-boundary-line-switch** and click **Run**.

## Command Overview

Toggle the display of wireframe open edges on or off during [wireframe verification](<wireframe-verify.md>).

This command alternates your system between the following states:

  * Allow open edges, or boundaries of a wireframe, to be displayed during [**wireframe-verify**](<wireframe-verify.md>), and to be output as strings [wf-convert-line-switch](<wf-convert-line-switch.md>) is active. 

  * Don't check for or display open edges as string data.

Note: The [wireframe-verify](<wireframe-verify.md>) command generates the adjacency information for the wireframe. Each triangle has **PID** values _PID1_ , _PID2_ and _PID3_. The adjacent triangle number for the edge from _PID1_ to _PID2_ is stored in _TRE1ADJ_. If there is no adjacent triangle, the adjacency value is zero.

Related topics and activities:

  * [wireframe-verify ("wvf")](<wireframe-verify.md>)

  * [wf-convert-line-switch ("twcl")](<wf-convert-line-switch.md>)
  * [wf-intersect-line-switch ("twvi")](<wf-intersect-line-switch.md>)
  * [wf-merge-line-switch ("twvm")](<wf-merge-line-switch.md>)
  * wf-boundary-line-switch ("twvb")