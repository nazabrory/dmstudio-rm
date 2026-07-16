# new-points ("npo")

See this command in the [**command table**.](<COMMAND%20TABLE_N.md#new-points>)

To access this command:

  * **Home** ribbon **> > Edit >> New Point.**

  * **Digitize** ribbon **> > Create >> Point**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "new-points"

  * Use the quick key combination "npo".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **new-points** and click **Run**.

## Command Overview

Digitize new point data interactively (digitizes) in any 3D or Task data window. Digitizing can be completed across multiple windows, or even sections of the same split 3D window, which allows digitizing to be performed, potentially, in 3D by snapping.

Typically, a left click or tap of the stylus adds a point.

This command is supported by undo and redo. If undoing or redoing whilst the command is active (you'll see a **Done** button in the top left of the screen if so), you can undo or redo individual points. Once the command is completed, all points digitized in the command session are undone or redone as a single unit.

If no points object exists in memory, a new object is created when this command is run. The object is called "New Points" but this can be changed.

Digitizing mode continues until either another command is run, or **Done** is clicked, or you press ESC.

**Note** : This command supports **[command line coordinates](<../COMMON/Coordinates_Command%20Line.md>)**.

Related topics and activities

  * [new-string ("ns")](<new-string.md>)

  * [create-new-points-object ("cnp")](<create-new-points-object.md>)