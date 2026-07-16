# new-sketch

See this command in the [**command table**.](<COMMAND%20TABLE_N.md#new-sketch>)

To access this command:

  * Digitize ribbon >> Edit Modes >> Auto Node.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "new-sketch"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **new-sketch** and click **Run**.

## Command Overview

Digitize new string data in sketch mode, where nodes are added automatically, based on cursor/stylus/finger movement. This behaviour is enforced regardless of the current [Auto Node](<auto-node-switch.md>) switch settings.

A sketch is drawn as a strings data type, using the current strings object formatting. If no strings object exists, one is created.

This command supports undo and redo functions. 

Note: This command does not support right-click (or equivalent) snapping but does honour the current [Auto Snap](<auto-snap-switch.md>) setting.

Activity steps:

  1. Run the command.

  2. Start sketching in any 3D view. Cursor/finger/stylus movement will create a free-form sketch line.

  3. Click Done to complete the sketching operation or just double-click (left or right) to finish (see below).

Tip: Whilst digitizing, you can complete the digitizing operation by double-clicking or double-tapping the final string vertex position. You can also complete the digitizing operation by closing the string.

Related topics and activities

  * [auto-node-switch](<auto-node-switch.md>)

  * [auto-snap-switch](<auto-snap-switch.md>)

  * [new-string ("ns")](<new-string.md>)