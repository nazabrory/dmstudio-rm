# blast-layout-from-wf ("blwf")

See this command in the [command table](<commandtable_B.md#blast-layout-from-wf>).

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "blast-layout-from-wf".

  * Use the quick key combination "blfw".

## Command Overview

Layout a blast from a surveyed wireframe surface.

This method should be used when you have a surveyed surface from which you wish to layout a blast, for example the original topography or a pit bench surface.

## How to Use

  1. Load a [blast patterns file](<../COMMON/filetype.md#Blast>).

  2. Load a wireframe surface, and a closed string indicating the blast perimeter. It is not essential that this line is projected onto the wireframe surface but the elevation of the blast outline string is used as a reference level from which the holes are projected and will affect their precise location.

  3. Run the command.

  4. If no string is selected, you are prompted to "Select perimeter to indicate blast"; select your blast outline string.

  5. You are prompted to "Select first point of base line"; choose the left hand end of the longest segment of the string and snap to this point. When prompted to "Select second point of base line", snap to the other end of this segment and this line will now become the base line for the blast. This will provide the orientation for the blast holes.

  6. You are prompted to "Fix a blast hole position", click just inside the corner at the left hand end of the base line and click OK to confirm the co-ordinates. 

  7. Select the active blast patterns file and enter a pattern number and click OK. 

  8. You will now see the Hole Specification screen.

  9. Enter a **Hole Prefix** if desired and set the **Target Elevation** as required, then click OK.

The pattern fills with vertical holes.

Related topics and activities

  * [add-attributes](<add-attributes.md>)
  * [blast patterns file](<../COMMON/filetype.md#Blast>)

  * move-blasthole-row

  * move-blasthole

  * blast-layout

  * [blast-layout-between-wf ("blbw")](<blast-layout-between-wf.md>)

  * [blast-layout-interactive](<blast-layout-interactive.md>)