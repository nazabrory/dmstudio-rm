# Enter Condition String Parameters

To access this screen:

  * Using the **[command line](<Command_Toolbar.md>)** , enter "condition-string"

  * Use the quick key combination "cond".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **condition-string** and click **Run**.

This screen is the user interface displayed when running the [condition-string](<../command_help/condition-string.md>) command.

Choose how many string segments comprise a selected string.

The selected string is formatted so that the specified number of segments (chords) are applied, and can be used to smooth a string, for example. 

To condition a string:

  1. Run the command.

  2. Select a string.

The **Enter Condition String Parameters** screen displays.

**Tip** : preselect string data to automatically display the parameters screen. You can preselect one or more strings.

  3. Enter the **Maximum Chord Length**. This is the maximum permitted length of any string segment (in metric or imperial units, depending on your [Project Options](<data%20options.md>)). This length will not be exceeded when conditioning a string, even for a straight line segment on the original data that exceeds this value.

  4. Enter the **Minimum Chord Length**. This is the minimum permitted string chord length. String segments will not be created below this value, regardless of the severity of curvature on the original data.

  5. Enter the **Minimum Angle**. This is the minimum convergent angle between subsequent string chords here. Lower values will produce strings with shallower internal string segment angles.

  6. Click **OK**.

The selected string data is conditioned based on the supplied parameters.

Related topics and activities

  * [Conditioning String Data](<Conditioning%20Strings.md>)

  * [condition-string ("cond")](<../command_help/condition-string.md>)

  * [smooth-string ("sms")](<../command_help/smooth-string.md>)