# set-default-density

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#set-default-density>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "set-default-density"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **set-default-density** and click **Run**.

## Command Overview

Set the rock or material 'default' density for the project. 

This is used in the absence of a **DENSITY** field or where absent density values ('-') are encountered when evaluating block model or drillhole data.

This setting is _not_ used by the command-line evaluation commands shown below:

  * evaluate-1-string
  * evaluate-2-strings
  * evaluate-all-strings
  * evaluate-all-strings-plane
  * evaluate-wireframe
  * evaluate-set-of-wireframes

For the above commands, a custom default density value is provided as part of the command.

Command steps:

  1. Run the command.

  2. Enter a Default Density for evaluation.

  3. Click OK.