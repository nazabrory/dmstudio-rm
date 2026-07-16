# Evaluate Wireframe

To access this screen:

  * Run the [evaluate-wireframe](<../command_help/evaluate-wireframe.md>) command.

  * Run the [evaluate-current-wireframe](<../command_help/evaluate-current-wireframe.md>) command.

Generate evaluated grades and tonnes of a block model or drillhole data in relation to either a DTM or closed wireframe volume.

If evaluating with reference to a DTM, you must choose if the model above or below the surface is evaluation. Optionally, you can constrain evaluation to a reference level.

This screen is the first of two displayed during evaluation. Once settings are defined here, [Evaluation Results](<EvaluationDynamicTableViewDialog.md>) display and they can be saved to a data object (and subsequently saved to a physical file).

A comparison of the total volume of the cells within the wireframe and the volume of the wireframe is made. If the difference between these two figures is more than 2 percent of the volume of the cells a warning is given. An example of when this would occur is if all or part of the wireframe is outside the limits of the cell model.

If any cell contains an absent density value the default density is used. This default value is defined when the cell model file is opened. 

If absent grade values are found, then they are replaced by the average value for the grade for calculation purposes and a message is displayed in the Output window.

During evaluation, **BLOCKID** information is written to the wireframe data (the triangles file). This matches the same **BLOCKID** results data. Where a wireframe object comprises multiple volumes (and for **evaluate-wireframe** , multiple volumes are also selected), incremental ID values are applied and recorded in results. For example, an object containing multiple stope volumes is evaluated per volume, with a unique ID applied to data in both the wireframe file, and the results table.

It is necessary to write the wireframe to file at some stage before exiting your application in order to store this BLOCKID value in the current wireframe files. This is most easily done using the [write-wf-data](<../command_help/write-wf-data.md>) command.

### Evaluate a Wireframe Volume

To evaluate a wireframe volume against either block model or drillhole data:

  1. Display the [Project Settings: Mine Design](<Project%20Settings_Mine%20Design.md>) screen and choose to evaluate against either drillhole or block model data.

  2. Load or create and display a wireframe object.

  3. Load or create a block model or drillholes, at least some of which must be enclosed by the wireframe volume.

This data must be visible before evaluation.

  4. Run either the **evaluate-wireframe** or **evaluate-current-wireframe** commands.

The **Evaluate Wireframe** screen displays.

  5. If running the **evaluate-wireframe** command, pick the **Wireframe Object** that represents the evaluation volume.

  6. Set the wireframe **Type** to _Closed Volume_.

  7. Assign a Mining Block ID to the wireframe so it can be given a reference in the results file. If the evaluation is accepted the triangles in the wireframe files are given this ID value.

**Note** : it is advisable to restrict **BLOCKID** values to two decimal places.

  8. Enter a **Default Density**. This is used if a **DENSITY** field does not exist in the input model or drillholes, or it exists and absent values are found. By default, this is 1.

**Note** : Default Density persists between static evaluation commands, but can be adjusted in any of them, if appropriate.

  9. Click **OK** to display the [**Evaluation Results**](<EvaluationDynamicTableViewDialog.md>) screen.

### Evaluate a DTM

To evaluate a wireframe DTM against either block model or drillhole data:

  1. Display the [Project Settings: Mine Design](<Project%20Settings_Mine%20Design.md>) screen and choose to evaluate against either drillhole or block model data.

  2. Load or create and display a wireframe object.

  3. If not already done, make sure the wireframe data is [verified](<Wireframe%20Verify%20Dialog.md>).

  4. Load or create a block model or drillholes, at least some of which must be enclosed by the wireframe volume.

This data must be visible before evaluation.

  5. Run either the **evaluate-wireframe** or **evaluate-current-wireframe** commands.

  6. If running the **evaluate-wireframe** command, pick the **Wireframe Object** that represents the evaluation volume.

  7. Set the wireframe **Type** to _DTM_.

  8. Choose the data to evaluate in relation to the DTM:

     * Choose Volume Above DTM to consider only drillhole or model data above (that is, has a higher elevation than) the surface data. You can constrain this To a maximum elevation, although the default value is automatically calculated as the highest elevation of the surface.

     * Choose Volume Below DTM to consider only drillhole or model data below the surface. The lowest To value is calculated, but can be edited.

  9. Assign a Mining Block ID to the wireframe so it can be given a reference in the results file. If the evaluation is accepted the triangles in the wireframe files are given this ID value.

**Note** : it is advisable to restrict **BLOCKID** values to two decimal places.

  10. Enter a **Default Density**. This is used if a **DENSITY** field does not exist in the input model or drillholes, or it exists and absent values are found. By default, this is 1.

**Note** : Default Density persists between static evaluation commands, but can be adjusted in any of them, if appropriate.

  11. Click **OK** to display the [**Evaluation Results**](<EvaluationDynamicTableViewDialog.md>) screen.

Related topics and activities

* [evaluate-wireframe ("evw")](<../command_help/evaluate-wireframe.md>)

  * [evaluate-wireframe ("evw")](<../command_help/evaluate-wireframe.md>)

  * [evaluate-current-wireframe](<../command_help/evaluate-current-wireframe.md>)

  * [evaluate-set-of-wireframes](<../command_help/evaluate-set-of-wireframes.md>)

  * [evaluate-all-strings ("eva")](<../command_help/evaluate-all-strings.md>)

  * [Evaluation Results](<EvaluationDynamicTableViewDialog.md>)

  * [evaluate-1-string ("ev1")](<../command_help/evaluate-1-string.md>)

  * [evaluate-2-strings ("ev2")](<../command_help/evaluate-2-strings.md>)

  * [evaluate-display-legend-switch](<../command_help/evaluate-display-legend-switch.md>)