# cone-from-drillhole ("cnfd")

See this command in the [**command table**.](<_COMMAND%20TABLE_C.md#cone-from-drillhole>)

To access this command:

  * **Sample Analysis** ribbon **> > Edit Drillholes >> Cones >> Cones from Drillholes**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "cone-from-drillhole"

  * Use the quick key combination "cnfd".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **cone-from-drillhole** and click **Run**.

## Command Overview

Generate a wireframe cone from a drillhole.

Command steps:

  1. In the Current Objects toolbar, create a new wireframe object. See **[Current Objects Toolbar](<../COMMON/Current_Objects_Toolbar.md>)**.

  2. Run the command.

  3. In any 3D window, select a drillhole.

  4. Using the [Generate Cones](<../COMMON/GenerateConesDialog.md>) screen, define the following parameters:

     * Deviation Field an optional field in the drillhole object that denotes the deviation from plan (potentially per sample).

     * Start Radius the deviation from plan at the start of the hole. This can be regarded as the upper cone radius.

     * Minimum Segment Length. the minimum possible length of a cone segment from its neighbour. The average sample length is a reasonable guide for this.

     * Name Field if specified, this value is added to all wireframe cone segments.

  5. Click **OK**. 

A wireframe cone is created based on the above parameters, starting at the drillhole collar and deviating outwards towards the end-of-hole.

The command completes automatically.

Related topics and activities

  * [cone-from-string](<cone-from-string.md>)

  * [Generate Cones screen](<../COMMON/GenerateConesDialog.md>)