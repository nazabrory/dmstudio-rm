# simplify-string ("sps")

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#simplify-string>)

To access this command:

  * **Digitize** ribbon **> > Condition >>Condition >> Simplify String**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "simplify-string".

  * Use the quick key combination "sps".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **simplify-string** and click **Run**.

## Command Overview

Reduce the number of points on a string whilst attempting to retain a shape most representative of the pre-simplified version. Start and end points of the string are not adjusted with this command.

**Note** : this is similar, and can be used as an alternative to, the [condition-string ("cond")](<condition-string.md>) or [reduce-points ("red")](<reduce-points.md>) commands.

Command steps:

  1. Digitize or load string data.

  2. Optionally, select the string data to be simplified. If no data is preselected, you can selected it after the command starts.

  3. Run the command.

  4. On the **Simplify String** screen, enter a **Simplification Distance**. This is the chord length within which a single point is added. Smaller values lead to a higher number of remaining points.

  5. If no data was preselected, pick string data in any **3D** window.

String data is simplified.

  6. If string data was not preselected, click **Done** to complete the command.

Related topics and activities

  * [condition-string ("cond")](<condition-string.md>)

  * [smooth-string ("sms")](<smooth-string.md>)