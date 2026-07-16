# set-adjustment-cut-off ("scu")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#set-adjustment-cut-off>)

To access this command:

  * Model ribbon **> >**Manipulate >> Adjust to Ore >> Set Cut-Off

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "set-adjustment-cut-off"

  * Use the quick key combination "scu".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **set-adjustment-cut-off** and click **Run**.

## Command Overview

Set grade field and cut-off grade for adjusting a string to an ore boundary using a block model.

This command sets the cut-off to be used when adjusting a string to an ore outline using the [adjust-string-in-ore](<adjust-string-in-ore.md>) command. The initial value for the grade field is blank and the cut-off value is absent (-). The default value is the last value that was entered. 

The block model field used for adjustment is the field currently defined by the selected [evaluation legend](<../COMMON/Project%20Settings_Mine%20Design.md>). If this is changed with the assign-fill-codes command it is likely that the cut-off will need to be changed as well. If the string adjustment is being done using filter definitions of ore then the cut-off value is irrelevant.

For more information on this command, see [adjust-string-in-ore](<adjust-string-in-ore.md>).

Command Steps:

  1. Run the command.

  2. In the Cutoff Grade screen, define the grade field and cut-off grade.

  3. Click OK.

Related topics and activities

  * [adjust-string-in-ore](<adjust-string-in-ore.md>)

  * [set-adjustment-method-switch ("am")](<set-adjustment-method-switch.md>)

  * [set-ore-categories ("soc")](<set-ore-categories.md>)

  * [set-step-distance](<set-step-distance.md>)

  * [set-ore-categories](<set-ore-categories.md>)

  * [Mine Design tab](<../COMMON/Project%20Settings_Mine%20Design.md>)