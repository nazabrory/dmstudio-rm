# plane-by-one-point ("1")

See this command in the [**command table**.](<COMMAND%20TABLE_P.md#plane-by-one-point>)

To access this command:

  * **3D View** ribbon **> > Sections >> 1 Point**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "plane-by-one-point"

  * Use the quick key combination "1".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **plane-by-one-point** and click **Run**.

## Command Overview

Set the view plane location and orientation in any 3D window based on a selected point and specified orientation.

The current section plane updates in response to this command, and you can optionally orient the view to an orthogonal focus automatically after the section definition updates. 

As one point can only define the section centre point, it is necessary to provide additional information about the alignment of the section. Once a centre point is digitized (either by left clicking to nominate a point on the current section or right-clicking to snap to other data points).

**Tip** : right-clicking to snap the section centre point to other data can be useful to ensure the section intersects 3D overlays at an appropriate position, such as an interval on a drillhole, or a landmark wireframe position and so on.

**Note** : there are separate commands available to define the 3D view _direction_. These options are similar to defining a section ([1 point](<view-by-one-point.md>), [2 points](<view-by-two-points.md>), [3 points](<view-by-three-points.md>)) but in each case, no section definition changes, only the direction from which data is viewed in the target 3D window. See also [Viewing Data](<../COMMON/Interface_Viewing%20Data.md>) and [3D Sections](<../VR_Help/Sections.md>).

Command steps:

  1. Orient your 3D view so appropriate data is clearly visible.

  2. Run the command.

  3. Following the prompt, select (snapping is allowed) any point in any 3D window.

The Plane By One Point screen displays.

  4. Select section **Orientation** :

     * **Horizontal** orient the plane to have zero azimuth and inclination.

     * North-Southorient the plane orthogonally to the north-south world axis. This equates to an azimuth of 90 and an inclination of -90.

     * East-Westorient the section to the east-west axis with an azimuth of zero and an inclination of -90.

     * Align to Vieworient the section orthogonally to the current view direction. 

  5. Decide if you want to automatically align the view orthogonally to the new section orientation:

     * If Align view to section is **checked** , the target 3D window view automatically orients so that the view direction is perpendicular to the section plane (that is, looking directly at it).

     * If Align view to section is **unchecked** , the view direction does not change when the section definition updates.

  6. Click **OK**.

The new section definition is applied in the target 3D window.

Related topics and activities

  * Navigation Toolbar

  * [plane-by-two-points ("2")](<plane-by-two-points.md>)

  * [plane-by-three-points ("3")](<plane-by-three-points.md>)

  * [3D Sections](<../VR_Help/Sections.md>)

  * [Section Locking](<../COMMON/Section_Locking.md>)

  * [3D Section Widgets](<../COMMON/Section_Widgets.md>)

  * [view-by-one-point ("v1")](<view-by-one-point.md>)