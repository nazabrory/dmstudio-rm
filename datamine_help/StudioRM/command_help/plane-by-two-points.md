# plane-by-two-points ("2")

See this command in the [**command table**.](<COMMAND%20TABLE_P.md#plane-by-two-points>)

To access this command:

  * **3D View** ribbon **> > Sections >> 2 Points**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "plane-by-two-points"

  * Use the quick key combination "2".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **plane-by-two-points** and click **Run**.

## Command Overview

Position and orient the target section so that its central axis aligns with a line defined by two points. The rotation around that line is specified explicitly as either horizontal, perpendicular or vertical.

This command will create a new section plane and, if selected, automatically orient the view so that it is orthogonal to the new plane.

**Tip** : right-clicking to snap section end points to other data can be useful to ensure the section intersects 3D overlays at an appropriate position, such as an collar and EOH position on a drillhole, or to orient a section along an underground drive plan and so on.

**Note** : there are separate commands available to define the 3D view _direction_. These options are similar to defining a section ([1 point](<view-by-one-point.md>), [2 points](<view-by-two-points.md>), [3 points](<view-by-three-points.md>)) but in each case, no section definition changes, only the direction from which data is viewed in the target 3D window. See also [Viewing Data](<../COMMON/Interface_Viewing%20Data.md>) and [3D Sections](<../VR_Help/Sections.md>).

Command steps:

  1. Orient your 3D view so appropriate data is clearly visible.

  2. Run the command.

  3. Following the prompt, select (snapping is allowed) the first reference point in the window.

  4. Following the prompt, select (snapping is allowed) the second reference point in the window.

The **Orientation** screen displays.

  5. Select a view orientation in relation to the 2 anchor points (essentially, choose the third axis):

     * **Horizontal** orient the plane to have zero azimuth and inclination.

     * **Vertical** orient the section vertically (an inclination of -90). The azimuth is determined by your digitized points.

     * **Perpendicular** orient the section to be perpendicular to the digitized points.

  6. Decide if you want to automatically align the view orthogonally to the new section orientation:

     * If Align view to section is **checked** , the target 3D window view automatically orients so that the view direction is perpendicular to the section plane (that is, looking directly at it).

     * If Align view to section is **unchecked** , the view direction does not change when the section definition updates.

  7. Click **OK**.

The current section is updated, and if you chose to do so, the view direction is automatically oriented to be orthogonal to the section.

Related topics and activities

  * Navigation Toolbar

  * [plane-by-one-point ("1")](<plane-by-one-point.md>)

  * [plane-by-three-points ("3")](<plane-by-three-points.md>)

  * [3D Sections](<../VR_Help/Sections.md>)

  * [Section Locking](<../COMMON/Section_Locking.md>)

  * [3D Section Widgets](<../COMMON/Section_Widgets.md>)

  * [view-by-one-point ("v1")](<view-by-one-point.md>)