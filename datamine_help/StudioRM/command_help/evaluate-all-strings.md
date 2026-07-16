# evaluate-all-strings ("eva")

See this command in the [**command table**.](<COMMAND%20TABLE_E.md#evaluate-all-strings>)

To access this command:

  * **Report** ribbon **> > Evaluate >> Strings >> All Strings**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "evaluate-all-strings"

  * Use the quick key combination "eva".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **evaluate-all-strings** and click **Run**.

## Command Overview

Evaluate all visible string overlay objects, against either a block model or drillholes, by projecting them perpendicular to the view plane. 

**Note** : the [evaluate-all-strings-plane](<evaluate-all-strings-plane.md>) command only differs from evaluate-all-strings in that the former projects perpendicularly to the mean plane of the loaded strings whilst the latter always uses the current view direction.

All strings are evaluated regardless of their selection status, although strings that are not displayed due to filtering will not be included in the analysis.

Strings can be in any position, and can be coplanar. This command, effectively, will run the [evaluate-1-string](<evaluate-1-string.md>) command multiple times in order to prepare results for either individual evaluation blocks, or a combined volume comprising all extruded strings.

Strings are internally extruded to form a 3D volume for analysis. This projection will take place orthogonally to the current section plane, and is unaffected by the current view direction or rotation.

If multiple strings exist, you can report evaluation results for each closed and projected string volume or as a combined result.

Evaluation results can be saved to a new object using the Save Results option on the **[Evaluation Results](<../COMMON/EvaluationDynamicTableViewDialog.md>)** screen. Data is saved as a results object (visible in the Loaded Data and Project Data control bars) and can be saved to a physical file. Any existing evaluation results of the same name are overwritten.

**Note** : evaluation results, specifically the fields listed in the output results table and which have been selected from the evaluated drillholes or block model, are not effected by the order in which data has been loaded.

This command displays the [Evaluation Settings](<../COMMON/EvaluationPropertiesDialog.md>) screen, followed by the [Evaluation Results](<../COMMON/EvaluationDynamicTableViewDialog.md>) screen.

Related topics and activities

  * [Evaluation Settings](<../COMMON/EvaluationPropertiesDialog.md>)

  * [Evaluation Results](<../COMMON/EvaluationDynamicTableViewDialog.md>)

  * [evaluate-1-string ("ev1")](<evaluate-1-string.md>)

  * [evaluate-2-strings ("ev2")](<evaluate-2-strings.md>)

  * [evaluate-all-strings-plane](<evaluate-all-strings-plane.md>)

  * [evaluate-current-wireframe](<evaluate-current-wireframe.md>)

  * [evaluate-display-legend-switch](<evaluate-display-legend-switch.md>)

  * [evaluate-set-of-wireframes](<evaluate-set-of-wireframes.md>)

  * [evaluate-wireframe](<evaluate-wireframe.md>)