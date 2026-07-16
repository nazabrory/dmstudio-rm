# end-link-selected-strings

See this command in the [**command table**.](<COMMAND%20TABLE_E.md#end-link-selected-strings>)

To access this command:

  * Explicit ribbon **> >**Create >> End Link >> End Link Selected

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "end-link-selected-strings"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **end-link-selected-strings** and click **Run**.

## Command Overview

Create a wireframe mesh from a closed string object in memory, using Delauney triangulation.

**Note** : this command is affected by the **Maximum Segment Length** setting in your [Project Settings](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>).

Command steps:

  1. Select a closed string to become a wireframe mesh.

  2. Run the command.

  3. Enter an (optional) attribute to define the linking sequence. An attempt is made to find matching values in the select attribute, with a link being formed only between points bearing coincident data.

Related topics and activities

  * [end-link ("eli")](<end-link.md>)

  * [end-link-boundary ("elb")](<end-link-boundary.md>)

  * [link-strings ("ls")](<link-strings.md>)

  *   * [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)