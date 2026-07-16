# auto-node-switch ("ans")

See this command in the [**command table**.](<_COMMAND%20TABLE_A.md#auto-node-switch>)

To access this command:

  * Home ribbon **> > Edit Modes >> Auto Node**.
  * **Digitize** ribbon **> > Edit Modes >> Auto Node**.
  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "auto-node-switch"

  * Use the quick key combination "ans".
  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **auto-node-switch** and click **Run**.

## Command Overview

Automatically create string vertices during digitizing with any string creation command, or command that adds string vertices interactively (new-string, insert-line-segment, extend-string, for example)

If enabled, string digitizing requires mouse, finger or stylus movement to automatically generate a string. If disabled, string nodes must be digitized independently either with a left or right mouse click, or by tapping the finger or stylus.

This command represents a switch: successive use will alternate between the enabled and disabled state. 

By default, this switch is off but commands may override this default setting, such as when sketching in Studio Mapper, for example.

**Note** : There's no need to set up snapping modes when digitizing data (say, a polygon feature) onto a wireframe map. The closest wireframe vertex or point is snapped.

Related topics and activities

  * [auto-snap-switch ("asn")](<auto-snap-switch.md>)