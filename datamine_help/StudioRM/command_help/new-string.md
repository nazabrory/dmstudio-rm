# new-string ("ns")

See this command in the [**command table**.](<COMMAND%20TABLE_N.md#new-string>)

To access this command:

  * **Home** ribbon **> > Edit >> New String.**

  * **Digitize** ribbon **> > Create >> String**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "new-string".

  * Use the quick key combination "ns".

  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **new-string** and click **Run**.

## Command Overview

Digitize new string data interactively (digitizes) in any 3D or Task data window. Digitizing can be completed across multiple windows, or even sections of the same split 3D window, which allows digitizing to be performed, potentially, in 3D by snapping.

**Note** : This command supports **[command line coordinates](<../COMMON/Coordinates_Command%20Line.md>)**.

Typically, a left click or tap of the stylus adds a string point (although if **[Auto Node](<auto-node-switch.md>)** is enabled, points are added quickly to simulate sketching).

This command is supported by undo and redo. If undoing or redoing whilst the command is active (you'll see a **Done** button in the top left of the screen if so), you can undo or redo individual points. Once the command is completed, the entire string or strings are undone or redone as a single unit.

If no strings object exists in memory, a new object is created when this command is run. The object is called "New Strings" but this can be changed.

Digitizing mode continues until either another command is run, or **Done** is clicked, or you press ESC.

Tip: Whilst digitizing, you can complete the digitizing operation by double-clicking or double-tapping the final string vertex position. You can also complete the digitizing operation by closing the string.

## Advanced Digitizing Controls

Disabled by default, this command is supported by advanced digitizing controls. Enable advanced controls using **Project Settings >> [Points and Strings](<../COMMON/Project%20Settings_Points%20and%20Strings.md>)** and check Display advanced digitizing controls. Once active you can constrain your digitizing behaviour to manage the length, gradient and azimuth of subsequent string segments. 

See [Advanced String Design](<../COMMON/advanced_string_design.md>).

**Note** : As a project setting, you must save your project to preserve this digitising mode between project sessions. The screen popup remembers its previous position.

Related topics and activities

  * [new-points](<new-points.md>)

  * [create-new-strings-object ("cns")](<create-new-strings-object.md>)

  * [3D Design](<../VR_Help/Designing_in_VR.md>)

  * [Digitizing in 3D](<../VR_Help/Digitizing_In_VR.md>)

  * [Command Line Coordinates](<../COMMON/Coordinates_Command%20Line.md>)

  * [Project a String ](<../VR_Help/Strings_Fitting%20a%20string%20to%20a%20surface.md>)

  * [auto-node-switch ("ans")](<auto-node-switch.md>)

  * [auto-snap-switch ("asn")](<auto-snap-switch.md>)