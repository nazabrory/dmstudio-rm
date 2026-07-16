# wireframe-verify ("wvf")

See this command in the [**command table**.](<COMMAND%20TABLE_W.md#wireframe-verify>)

  * **Wireframe** ribbon **> > Fix >> Verify**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "wireframe-verify"

  * Use the quick key combination "wvf".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **wireframe-verify** and click **Run**.

## Command Overview

Triangulate the chosen wireframe and attempt to produce consistent normals. If there are shared edges, the normals generated may not be correct.

The main purpose of verification is to create manifold surfaces from the wireframe. 

In order to do this, Verifylooks for the highest, non-vertical triangle in the selection, and alters its normal so that it is pointing upwards. It then looks at all adjacent triangles, and ensures that their normals are consistent with that face. The process then continues from these faces, until no more are unassigned, or adjacent triangles are found. If all triangles have been assigned, the process is complete, otherwise the Surface Number is incremented, and the process starts again with the highest, non-assigned, non-vertical triangle.

Displays the **[Verify Wireframe](<../COMMON/Wireframe%20Verify%20Dialog.md>)** screen. 

Related topics and activities

  * [Verify Wireframe Data](<../COMMON/Wireframe%20Verify%20Dialog.md>) (screen)

  * [Verify Wireframe: Examples](<../COMMON/Wireframe%20Verify%20Examples.md>)

  * [Clean Wireframe](<../COMMON/Wireframe%20Clean%20Dialog.md>)