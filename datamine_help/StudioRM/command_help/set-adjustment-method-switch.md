# set-adjustment-method-switch ("am")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#set-adjustment-method-switch>)

To access this command:

  * Model ribbon **> >**Manipulate >> Adjust to Ore >> Adjustment Method

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "set-adjustment-method-switch"

  * Use the quick key combination "am".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** dialog, locate **set-adjustment-method-switch** and click **Run**.

## Command Overview

Toggle between using the cut-off grade or legend items methods when using the [adjust-string-in-ore](<adjust-string-in-ore.md>) command.

If the cut-off option (default) is selected, a value for the cut-off grade needs to be set using the [set-adjustment-cut-off](<set-adjustment-cut-off.md>) command. This needs to correspond with the currently defined [evaluation legend](<../COMMON/Project%20Settings_Mine%20Design.md>) field. If the legend items option is selected, then the defined evaluation legend items are used to define ore and non-ore categories. The latter is used in conjunction with the [set-ore-categories](<set-ore-categories.md>) command, to define whether each legend item (category) is classified as ore or non-ore (waste).

  * Cut-off grade: This method uses a defined cut-off grade and adjustment step size to control the adjustment of the ore outline. The cut-off grade is set using the command [set-adjustment-cut-off](<set-adjustment-cut-off.md>); the default value for the cut-off grade is absent (-).

The field used to define ore is the block model data column currently colored by a legend, as defined in the 3D properties screen for the loaded model. Once set, the same value is used until it is changed. 

If the adjustment is attempted with an absent cut-off grade, the message "The current cut off grade value cannot be used for adjustment" displays.  

  * Legend Items: This method uses the evaluation legend items (categories) in combination with the specified Ore/Non-Ore prompts and the defined step adjustment size, to control the adjustment of the ore outline. The evaluation legend is defined in the Project Settings dialog, [Mine Design tab](<../COMMON/Project%20Settings_Mine%20Design.md>).

The block model is coloured using this legend as defined in the 3D properties screen for the loaded model. These categories are initialised and defined by the Ore/Non-Ore prompts, using the command [set-ore-categories](<set-ore-categories.md>). 

The default for each category is ore. If this Legend Items method is being used to do guide the adjustment the value of the cut-off grade ([set-adjustment-cut-off](<set-adjustment-cut-off.md>)) and the currently shaded field become irrelevant.

Command Steps:

  1. Run the command.

  2. Check the message in the Status Bar:

     * "Using CUT OFF grade to define ore"

     * "Using LEGEND ITEMS to define ore"

  3. Click Cancel to accept the current switch state.

  4. Repeat steps 1 to 3 to change the switch state.

Related topics and activities

  * [adjust-string-in-ore](<adjust-string-in-ore.md>)

  * [set-adjustment-cut-off](<set-adjustment-cut-off.md>)

  * [set-step-distance](<set-step-distance.md>)

  * [set-ore-categories](<set-ore-categories.md>)

  * [Mine Design tab](<../COMMON/Project%20Settings_Mine%20Design.md>)