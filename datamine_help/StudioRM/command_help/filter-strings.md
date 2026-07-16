# filter-strings ("fs")

See this command in the [**command table**.](<COMMAND%20TABLE_F.md#filter-strings>)

To access this command:

  * **Format** ribbon **> > Filter >> Strings**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "filter-strings"

  * Use the quick key combination "fs".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **filter-strings** and click **Run**.

## Command Overview

Filter all visible strings overlays.

This command makes it possible to selectively display and work with strings using a filter expression. As soon as the command is invoked any previously set string filters is removed.

It is advisable not to use coordinate data in the expressions but to use attribute fields. If any one point in a string fails to pass, then this string is "turned off".

Existing filters can be removed by running this command without any filters. The [redraw-display](<redraw-display.md>) command will display all the data.

For more information on filtering data, click [here](<../COMMON/Filtering_Data.md>).

Command steps:

  1. Run the command.

The [Expression Builder](<../COMMON/Expression%20Builder%20Dialog.md>) displays.

  2. Enter or construct a valid filter expression. See [Filtering Data](<../COMMON/Filtering_Data.md>).

  3. Click OK.

Related topics and activities:

  * [Expression Builder](<../COMMON/Expression%20Builder%20Dialog.md>)

  * [Logical Expressions](<../COMMON/logical%20expressions.md>)

  * [Filtering Data](<../COMMON/Filtering_Data.md>)