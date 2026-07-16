# insert-offsets

See this command in the [**command table**.](<COMMAND%20TABLE_I.md#insert-offsets>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "insert-offsets"

  * Use the quick key combination "iof".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **insert-offsets** and click **Run**.

## Command Overview

Insert a series of strings within a closed boundary according to minimum separation/distance parameters. 

Strings are projected perpendicularly to the selected centre line string segment that they intersect.

This command requires at least one closed string and another string (open or closed) to be loaded. The second string must intersect the closed boundary string.

Command steps:

  1. Run the command

  2. Select the string from which you wish to project perpendicular strings.

  3. Enter a distance between offsets. This is the 'gap' between projected strings that you require.

If the selected centre line string is straight (e.g. comprised of two nodes), the gap between projected strings and neighbouring strings are constant along their length.

Where a multi-segment string is selected, the gap between projected strings is onlyhonoured at the point of the newly projected string and intersection.

  4. Enter a minimum % separation distance and click OK.

Related topics and activities

  * [offset-outside-string ("oos")](<offset-outside-string.md>)

  * [offset-inside-string ("ois")](<offset-inside-string.md>)

  * [translate-point](<translate-string.md>)