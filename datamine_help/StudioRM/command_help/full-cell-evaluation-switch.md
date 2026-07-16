# full-cell-evaluation-switch ("fce")

See this command in the [**command table**.](<COMMAND%20TABLE_F.md#full-cell-evaluation-switch>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "full-cell-evaluation-switch"

  * Use the quick key combination "fce".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **full-cell-evaluation-switch** and click **Run**.

## Command Overview

Turn on or off full cell evaluation of a block model.

If this toggle is on then evaluations against block models are done using full cell evaluation. That is cells are considered to be wholly inside or outside the wireframe.

If the switch is set, then the centroid of the subcell is checked to see whether it is inside the wireframe. If the centroid is inside, then 100% of the subcell volume is used for the evaluation; if the centroid is outside then 0% of the subcell volume is used. Leaving this option unchecked means that the true volume of the subcell within the wireframe will calculated and used for the evaluation. Full cell evaluation is faster, but less accurate.

Related topics and activities

  * [evaluate-1-string](<evaluate-1-string.md>)

  * [evaluate-2-strings](<evaluate-2-strings.md>)

  * [evaluate-wireframe](<evaluate-wireframe.md>)