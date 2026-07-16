# View Direction  
  
To access this screen:

  * Display the [**View Settings**](<../COMMON/Section%20Definition%20Dialog.md>) screen and click the **View Direction** tab.

You can change the view direction of a plot projection both interactively and by manually setting azimuth and dip values. This topic covers changing the direction via the **[View Settings](<../COMMON/Section%20Definition%20Dialog.md>)** screen.

Where a projection is not viewing data perpendicular (or perpendicular to a major axis) to its associated section (see [Sections and Projections](<alignviewwithsection.md>)), it is known as a "3D Projection", although this is just a convenient label as, in fact, all projections have a view direction, and that view direction can be set independently for each projection.

[![](../Images/Plots-example1.png)](<javascript:void\(0\);>)

A plot sheet showing a 3D projection (top left) and a projection with a view aligned perpendicularly to the defined section (top left)

To change the view direction (using the View Settings screen).

  1. Display a plot sheet with at least one [2D or 3D](<Projection%20Overlay%20Types.md>) projection.

  2. Select the projection (left click).

  3. Activate the **Plots (View)** ribbon and click **Set**.

The **[View Settings](<../COMMON/view%20settings%20direction%20dialog.md>)** screen displays, open at the **View Direction** tab.

  4. Set the **View Orientation** :

     * _Horizontal_ View 3D data orthogonally to the world axes (orient the view to look directly at the data from above). 

The **Azimuth** and **Dip** settings (see below) automatically adjust to 0 and 90 respectively if **View from** is set to _Above/Plan_. Otherwise the view is inverted.

     * _North-South_ View data along the from the North, towards the South. **Dip** becomes 270 and **Azimuth** becomes 0 if **View from** is set to _East_. Otherwise, the view swaps to the opposite line of sight.

     * _East-West_ As above, but view from East to West. **Dip** becomes 180 and **Azimuth** becomes 0 if View from is _North_ , or the opposite viewpoint if set to _South_.

     * 3dUse whatever **Dip** and **Azimuth** values you like, with **View from** set along any of the major axes of the section (_North East_ , _South East_ and so on).

**Note** : **Azimuth** and **Dip** values, regardless of how they are set, is relative to the world axes. You can align the view with the section, but this done using separate controls (see below).

  5. Choose the world coordinates that appear at the centre of the projection, using **Mid Point** XYZ settings.

  6. To align the view with the currently active section, use the Align to Section menu. See[Projection Properties](<projection%20properties.md>).

Other settings become unavailable if a preset section alignment is selected other than _No_.

  7. Click **Reset Mid Point** to revert view centre default settings.

  8. Choose how projection data updates during changes:

     * To update the projection as view settings change, check **Dynamic**.

     * To update the settings only on **OK** or **Apply** , uncheck **Dynamic**.

**Note** : You can also set the view direction in a plot using the **(Plots) View** ribbon commands (**View** group).

Related topics and activities

  * [View Settings](<../COMMON/Section%20Definition%20Dialog.md>)

    * [Section Definition](<CustomSections.md>)

    * View Direction

    * [Size/Scale](<../COMMON/view%20settings%20scale%20dialog.md>)

    * [Section Width Settings](<Plots-ViewSettings-SectionWidth.md>)

    * [Projection Exaggeration Settings](<Plots-ViewSettings-Exaggeration.md>)

  * [Sections and Projections](<alignviewwithsection.md>)

  * [Projection Overlay Types](<Projection%20Overlay%20Types.md>)

  * [Add a Sheet or Projection](<insertsection.md>)

  * [Section Definition](<CustomSections.md>)

  * [Clipping Plots Data](<ClipView.md>)

  * [Zoom, Scale & Pan](<Zooming.md>)

  * [Align Sections](<alignsection.md>)