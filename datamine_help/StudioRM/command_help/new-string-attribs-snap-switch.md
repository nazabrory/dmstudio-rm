# new-string-attribs-snap-switch ("asw")

See this command in the [**command table**.](<COMMAND%20TABLE_N.md#new-string-attribs-snap-switch>)

To access this command:

  * Digitize ribbon **> > Edit Modes >> Snap Point Attributes**.

  * Use the quick key combination "asw".

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "new-string-attribs-snap-switch".

  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **new-string-attribs-snap-switch** and click **Run**.

## Command Overview

This toggle controls how attributes are added to new strings which are interactively drawn in the 3D window.

This command toggles between the two following states:

  * Toggled ON (i.e. active) - when a new string is drawn (with or without snapping), attributes are automatically picked up from the closest string, when the first string point is defined, and applied to the new string.

  * Toggled OFF (i.e. inactive) - drawing a new string(s) will honour the attributes defined using the selected Attribute Field and associated Attribute Value parameters in the [Current Objects](<../COMMON/Current_Objects_Toolbar.md>) toolbar, even if the first point is snapped to another string.

Command steps:

  1. Run the command.

  2. Check the status of this toggle in the message section (far left) of the Status Bar:

     * when toggled ON, it should read 'New string gets attributes from snapped point'

     * when OFF, it should read 'New string gets currently set attributes'.

Related topics and activities

  * [new-string](<new-string.md>)