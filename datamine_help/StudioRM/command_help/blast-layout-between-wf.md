# blast-layout-between-wf ("blbw")

See this command in the [command table](<commandtable_B.md#blast-layout-between-wf>).

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "blast-layout-between-wf".

  * Use the quick key combination "blbw".

## Command Overview

Layout a blast pattern between wireframe limits to create a new set of drillholes. 

This method is applicable when you have two 3D surfaces between which you wish to layout a blast, for example the original topography and a geological surface that you wish to expose. The method is similar to the [blast-layout-from-wf](<blast-layout-from-wf.md>) command, although in this case two objects are being used to define the blast zone.

Command steps:

  1. Load a [blast patterns file](<../COMMON/filetype.md#Blast>).

  2. Load or create a closed string to indicate the outline perimeter. It is not essential that this line is projected onto the wireframe surface but the elevation of the blast outline string is used as a reference level from which the holes are projected and will affect their precise location.

  3. Run the command.

  4. If no string is selected, you are prompted to "Select perimeter to indicate blast"; select your blast outline string.

  5. Choose the start of the base line; find the left hand end of the longest segment of the string and snap to this point. When prompted to "Select second point of base line", snap to the other end of this segment and this line will now become the base line for the blast. This will provide the orientation for the blast holes.

  6. Fix a blast hole position: Click just inside the corner at the left hand end of the base line and click **OK** to confirm the co-ordinates.

  7. Select the loaded blast patterns file and enter a pattern number and click **OK**. You will now see the Hole Specification screen.

  8. Enter a Hole Prefix if desired and then click OK.

The pattern fills with vertical holes as shown below. 

  9. Save the holes and string if required as previously.

Related topics and activities

  * [add-attributes](<add-attributes.md>)
  * [blast patterns file](<../COMMON/filetype.md#Blast>)

  * move-blasthole-row

  * move-blasthole

  * blast-layout

  * [blast-layout-from-wf](<blast-layout-from-wf.md>)

  * [blast-layout-interactive](<blast-layout-interactive.md>)