# wireframe-surface-merge ("udt")

See this command in the [**command table**.](<COMMAND%20TABLE_W.md#wireframe-surface-merge>)

To access this screen:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "wireframe-surface-merge"

  * Use the quick key combination "udt".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **wireframe-surface-merge** and click **Run**.

## Command Overview

Perform a surface operation to update one wireframe DTM surface (or partial surface) with another. It is also known as the "Update DTM" or "Update Hull" command.

This function generates a new surface using the second wireframe data to update the surface elevation in preference to the first. The resultant surface area is the union of the first and the second wireframe surface, so there is no restriction that the second surface be bounded by the first.

The operation of the command can be likened to using a cookie cutter at the boundary of the second surface to cut out the first surface, and inserting the second surface into the first. Where there is a gap at the interface between the first and second surface, the gap is closed off with triangles, modelling the cut and fill relationship between the two surfaces.

Displays the **[Update DTM](<../COMMON/wireframe%20surface%20merge%20dialog.md>)** screen. 

Related topics and activities

  * [Update DTM](<../COMMON/wireframe%20surface%20merge%20dialog.md>) (screen)

  * [Volume between DTMs](<../COMMON/Wireframe%20Volume%20between%20intersecting%20DTMs.md>)

  * [Volume under Intersecting DTM](<../COMMON/Wireframe%20Volume%20under%20Intersecting%20DTM%20Dialog.md>)

  * [Wireframe Project to Plane](<../COMMON/Wireframe%20Project%20To%20Plane%20Dialog.md>)