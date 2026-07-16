# Project Settings: Mine Design

To access this screen:

  * On the Project Settings screen, select the **Mine Design** tab.

Specify how underground design drive strings are created and used, and reserves evaluation is performed, in your application. 

To define drive linking settings when using drive design commands:

  1. Display the **Mine Design** screen.

  2. Choose whether or not to **Keep cross section strings** :

The [link-complete-drive](<../command_help/link-complete-drive.md>) or link-drive-ends commands create cross-sectional perimeters at each point along the drive control string, and are used to make a wireframe model of that drive. This toggle controls whether or not these cross- sectional perimeters are left resident in memory.

     * If **checked** , cross-sectional perimeters remain loaded after the wireframe is generated.

     * If **unchecked** , these perimeters are automatically unloaded after the design command completes.

  3. Choose whether to **Generate wall strings** or not:

During use of the [link-complete-drive](<../command_help/link-complete-drive.md>) or link-drive-ends commands, left, right and centreline-roof strings may be created in addition to the wireframe model of the underground drive. These strings can be useful for design and layout purposes. 

     * If **checked** , wall strings remain loaded after drive generation, together with the original drive control string.

     * If **unchecked** , wall strings are automatically unloaded after drive generation.

  4. Choose whether to **Evaluate drive against model** or not:

     * If **checked** , and a block model is loaded, the [link-complete-drive](<../command_help/link-complete-drive.md>) or link-drive-ends commands include evaluating the generated wireframe model of the drive against the block model, using any current grade category filters. 

     * If **unchecked** , evaluation results are not generated when drive linking.

**Note** : regardless of the status of this control, the overall drive volume and tonnage is always written to the drive statistics file.

  5. Pick a colour for the **Cross section** , **Roof string** and **Wall string**.

  6. Click **Ramp segment length** to display the **Ramp Segment Length** screen and enter a value.

To configure how evaluation is performed during drive linking:

  1. Display the **Mine Design** screen.

  2. Toggle the use of a block model during evaluations with the **Evaluate Block Model** option.

If the use of the cell model in evaluations is enabled, the evaluation commands use the open cell model as the data source. Either this or **Evaluate Drillholes** (see below) can be checked, not both.

  3. Alternatively, choose **Evaluate Drillholes** to turn on the use of drillholes in evaluations. This means evaluation commands use the (filtered) drillholes as the data source. You can either select this option or Evaluate Block Model (see above).

**Note** : to evaluate drillhles, static desurveyed drillholes must be loaded. 

  4. Choose if full cell (block model) or segment (drillhole) evaluation is performed, using the **Full cell/segment evaluation** toggle.

     * If **checked** , evaluations against block models are done using full cell evaluation, and full segments if drillhole evaluation is being performed.

For models, cells are considered to be wholly inside or outside the wireframe. If a cell has more than 50 percent of its volume inside the wireframe it is treated as being included and all its volume is evaluated. 

If drillhole evaluation is performed, a segment is considered to be inside the wireframe if at least half the segment length is enclosed.

     * If **unchecked** , evaluation is performed using partial cell or segment data.

  5. **Evaluations are always performed using legends**. 

The evaluation legend that is used can either be the legend being used for the display (**Use Display Legend** is **checked**), or another legend can be picked from the list provided.

Related topics and activities

  * [Project Settings](<ProjectSettings.md>)

  * [link-complete-drive](<../command_help/link-complete-drive.md>)

  * link-drive-ends

  * [Drillhole Representation](<Drillhole%20Representation%20in%20Studio.md>)