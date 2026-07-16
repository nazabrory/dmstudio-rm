# evaluate-set-of-wireframes

See this command in the [**command table**.](<COMMAND%20TABLE_E.md#evaluate-set-of-wireframes>)

To access this command:

  * **Report** ribbon **> > Evaluate >> Wireframes >> Set of Wireframes**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "evaluate-set-of-wireframes"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **evaluate-set-of-wireframes** and click **Run**.

## Command Overview

Evaluate a set of wireframes separating each one by specification of a key field.

If evaluating with reference to DTM data, you must choose if the model or drillhole data above or below the surface is evaluated. Optionally, you can constrain evaluation to a reference level.

This screen is the first of two displayed during evaluation. Once settings are defined here, [Evaluation Results](<../COMMON/EvaluationDynamicTableViewDialog.md>) display and they can be saved to a data object (and subsequently saved to a physical file).

A comparison of the total volume of the cells within the wireframe and the volume of the wireframe is made. If the difference between these two figures is more than 2 percent of the volume of the cells a warning is given. An example of when this would occur is if all or part of the wireframe is outside the limits of the cell model.

If any cell contains an absent density value the default density is used. This default value is defined when the cell model file is opened. 

If absent grade values are found, then they are replaced by the average value for the grade for calculation purposes and a message is displayed in the Output window.

During evaluation, **BLOCKID** information is written to the wireframe data (the triangles file). This matches the same **BLOCKID** results data. Where a wireframe object comprises multiple volumes (and for **evaluate-wireframe** , multiple volumes are also selected), incremental ID values are applied and recorded in results. For example, an object containing multiple stope volumes is evaluated per volume, with a unique ID applied to data in both the wireframe file, and the results table.

It is necessary to write the wireframe to file at some stage before exiting your application in order to store this BLOCKID value in the current wireframe files. This is most easily done using the [write-wf-data](<write-wf-data.md>) command.

Command steps:

  1. Display the [Project Settings: Mine Design](<../COMMON/Project%20Settings_Mine%20Design.md>) screen and choose to evaluate against either drillhole or block model data.

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

  9. Click **OK** to display the [**Evaluation Results**](<../COMMON/EvaluationDynamicTableViewDialog.md>) screen.

Related topics and activities

  * [Evaluate Wireframe](<../COMMON/Evaluate%20Wireframe%20Dialog.md>)

  * [evaluate-current-wireframe](<evaluate-current-wireframe.md>)

  * [Evaluation Results](<../COMMON/EvaluationDynamicTableViewDialog.md>)

  * [evaluate-all-strings ("eva")](<evaluate-all-strings.md>)

  * [evaluate-1-string ("ev1")](<evaluate-1-string.md>)

  * [evaluate-2-strings ("ev2")](<evaluate-2-strings.md>)

  * [evaluate-display-legend-switch](<evaluate-display-legend-switch.md>)