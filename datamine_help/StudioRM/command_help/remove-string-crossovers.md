# remove-string-crossovers ("tcr")

See this command in the [**command table**](<COMMAND%20TABLE_R.md#remove-string-crossovers>).

To access this command:

  * **Digitize** ribbon **> > Condition >> Condition >> Trim Crossovers**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "remove-string-crossovers"

  * Use the quick key combination "tcr".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **remove-string-crossovers** and click **Run**.

## Command Overview

Remove string crossovers in the current view plane.

Select a segment on part of the string that is to be retained. Any crossovers (closed-over loops) in the string are eliminated, by removing those string vertices on the loop formed by each crossover. A new point is created at the original intersection point of each former loop.

**Note** : A "crossover" occurs if, along the line of sight, string data intersects itself. As such, this command is sensitive to the orientation of the current view plane.

Command steps:

  1. Run the command.

  2. Select a string.

The string is trimmed to a single perimeter with no crossed lines in the current view plane.

Related topics and activities

  * [smooth-string](<smooth-string.md>)

  * [converge-segments](<converge-segments.md>)

  * [condition-string](<condition-string.md>)

  * remove-string-crossovers

  * [resolve-string-points ("resp")](<resolve-string-points.md>)

  * [insert-near-points ("inp")](<insert-near-points.md>)