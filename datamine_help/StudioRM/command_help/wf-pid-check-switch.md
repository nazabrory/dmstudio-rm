# wf-pid-check-switch ("twcd")

See this command in the [**command table**.](<COMMAND%20TABLE_W.md#wf-pid-check-switch>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "wf-pid-check-switch"

  * Use the quick key combination "twcd".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **wf-pid-check-switch** and click **Run**.

## Command Overview

Toggle the checking of duplicate points on or off during verify. 

During the [wireframe-verify](<wireframe-verify.md>) command adjacency and surface normal information is generated using triangle adjacency information. Triangles are considered adjacent if the PID point identifiers match. 

As a consequence, triangle vertices that have common coordinates but different point identifiers must be merged. Surfaces within a group can share vertices but groups do not have common vertices.

Note: The [set-tolerance](<set-tolerance.md>) command can be used to put a tolerance on duplicate point checking.

  

Related topics and activities:

  * [wireframe-verify ("wvf")](<wireframe-verify.md>)

  * [wf-boundary-line-switch ("twvb")](<wf-boundary-line-switch.md>)

  * [wf-convert-line-switch ("twcl")](<wf-convert-line-switch.md>)
  * [wf-intersect-line-switch ("twvi")](<wf-intersect-line-switch.md>)
  * [wf-merge-line-switch ("twvm")](<wf-merge-line-switch.md>)