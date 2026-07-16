# move-plane ("mpl")

See this command in the [command table.](<COMMAND%20TABLE_M.md#move-plane>)

  * View ribbon **> > Move >> Move**
  * Enter "move-plane" into the **[Command](<../COMMON/Command_Toolbar.md>)** toolbar and press <ENTER>.

  * Use the quick key combination "mbl" whilst a 3D view is active.

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **move-plane** and click **Run**

## Command Overview

Moves the currently active section a specified distance. Positive values will move the plane forward along a directional orthogonal to the plane and negative values will move the plane backwards.

The distance moved is specified using the popup screen, where a positive distance moves the plane forward and negative in the reverse direction. The default movement distance can be set using the **View** ribbon's **Move** field.

**Note** : The movement distance specified during this command is different to the one applied when using [move-plane-forward ("mpf")](<move-plane-forward.md>) and [move-plane-backward ("mpb")](<move-plane-backward.md>) commands, which uses the current section width instead.

Command Steps:

  1. Run the **move-plane** command.

The **Move Plane** screen displays.

  2. Enter the **Distance to move plane** as either a negative or positive value (depending on whether movement backward or forward is required.
  3. Click **OK**.

The currently active section is shifted forward or backwards by the specified distance. The orientation of the section or view plane is not altered.

Related Topics and Activities

  * [move-plane-backward](<move-plane-backward.md>)
  * [move-plane-forward](<move-plane-forward.md>)