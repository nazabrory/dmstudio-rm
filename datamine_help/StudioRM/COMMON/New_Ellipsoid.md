# New Ellipsoid

To access this screen: 

  * Implicit ribbon **> > Ellipsoid >> New**.
  * **Data** ribbon **> > Objects >> New >> Ellipsoid**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "new-ellipsoid"

  * Use the quick key combination "nel".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **new-ellipsoid** and click **Run**.

This dialog is launched by the [new-ellipsoid](<../command_help/new-ellipsoid.md>) command is used to create one or more search ellipsoids, for inclusion within a new or existing [ellipsoids object](<../VR_Help/Ellipsoids_Overview.md>).

If you wish to store your ellipsoid definitions within an existing ellipsoids object, you can select it first. Otherwise, you can create a new ellipsoids object automatically. Alternatively, use the [Current Object](<Current_Objects_Toolbar.md>) toolbar to generate a new, empty ellipsoid object before you start.

Then, you can define your ellipsoid centroid position by either specifying values in the relevant coordinate fields, or you can pick a position on the currently active 3D section. Define the size and orientation of your ellipsoid, then click Add to add it to the currently specified ellipsoids object (an object can contain one or more ellipsoid definitions).  

To create a new ellipsoid object:

  1. Display the **New Ellipsoid** screen.

  2. Select an existing Ellipsoid object or enter a new description to create a new object. All ellipsoid objects that are currently loaded will be displayed in the list.

  3. To retrieve the properties of an existing ellipsoid (say, to create a modified copy), select the Copy from loaded ellipsoid pick button and then an ellipsoid in view in any 3D window. The properties of the ellipsoid (see below) then display on screen.

  4. Define the **Position** of the ellipsoid by entering **XYZ** coordinates. You can also use the picker button to select a 3D location in the current 3D view.

  5. Define the Size. Enter a Length for the major, semi-major and minor axes of the ellipsoid. This determines the overall size of your ellipsoid.

  6. Define the **Rotation** of the ellipsoid; enter the Azimuth, Dip and Roll of the new ellipsoid. You can specify the axis for each angle independently using Axis 1, Axis 2 and Axis 3.

  7. **Add** the new ellipsoid definition to the current ellipsoids object.

Related topics and activities

  * [Ellipsoids Overview](<../VR_Help/Ellipsoids_Overview.md>)

  * [The Ellipsoids Folder (Sheets)](<../VR_Help/Sheets_Ellipsoids.md>)

  * [new-ellipsoid](<../command_help/new-ellipsoid.md>)

  * [ellipsoids object](<../VR_Help/Ellipsoids_Overview.md>)