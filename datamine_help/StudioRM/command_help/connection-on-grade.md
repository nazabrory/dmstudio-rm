# connection-on-grade ("cog")

See this command in the [**command table**.](<_COMMAND%20TABLE_C.md#connection-on-grade>)

To access this command:

  * **Digitize** ribbon **> > Condition >> Condition >> Connect on Gradient**

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "connection-on-grade"

  * Use the quick key combination "cog".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **connection-on-grade** and click **Run**.

## Command Overview

Generates a connection string between a 3D point and any points on a string which produce a predesignated angle, if possible.

Command steps:

  1. Load your landmark point and string data. The point data represents the start of the connection string to be created, and the loaded string the destination. 

  2. Run the **connection-on-grade** command.

  3. Specify the gradient of the new connecting string in degrees, to be formed between the initial point and the selected string, by entering a numeric (positive or negative) numeric value into the **Gradient of Strings (degrees)** field.

  4. Click **OK**.

A connection string is formed between the original point and destination string if such a connection is possible.

The units and up/down convention can be modified with the [set-gradient-convention](<set-gradient-convention.md>) command.

Related topics and activities

  * [set-gradient-convention](<set-gradient-convention.md>)

  * [adjust-to-gradient ("atg")](<adjust-to-gradient.md>)

  * [fit-elevation ("fe")](<fit-elevation.md>)