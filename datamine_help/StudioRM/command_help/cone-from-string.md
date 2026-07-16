# cone-from-string ("cnfs")

See this command in the [**command table**.](<_COMMAND%20TABLE_C.md#cone-from-string>)

To access this command:

  *   * **Sample Analysis** ribbon **> > Edit Drillholes >> Cones >> Cones from String**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "cone-from-string"

  * Use the quick key combination "cnfs".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **cone-from-string** and click **Run**.

## Command Overview

Generate a wireframe cone from a string. Typically, this cone is used to assess the impact of production deviation from a plan, such as a planned drillhole direction or drive development. This can be useful to assess the potential proximity of development or drilling in relation to other important and known structural milestones such as a stope cavity or other developments.

Command steps:

  1. In the Current Objects toolbar, create a new wireframe object. See **[Current Objects Toolbar](<../COMMON/Current_Objects_Toolbar.md>)**.

  2. Run the command.

  3. In any 3D window, select a string.

  4. Using the [Generate Cones](<../COMMON/GenerateConesDialog.md>) screen, define the following parameters:

     * Deviation Per Unit Length enter the maximum expected drillhole deviation from plan here. Bigger values create shallower cones (with a greater potential deviation and an increased risk of proximity detection warnings.

     * Deviation Field an optional field in the drillhole object that denotes the deviation from plan (potentially per sample).

     * Start Radius the deviation from plan at the start of the hole. This can be regarded as the upper cone radius.

     * Minimum Segment Length. the minimum possible length of a cone segment from its neighbour. The average sample length is a reasonable guide for this.

     * Name Field if specified, this value is added to all wireframe cone segments.

  5. Click **OK**. 

A wireframe cone is created based on the above parameters, starting at the initial string vertex and deviating outwards along the length of the string.

The command completes automatically.

Related topics and activities

  * [cone-from-drillhole ("cnfd")](<cone-from-drillhole.md>)

  * [Generate Cones screen](<../COMMON/GenerateConesDialog.md>)