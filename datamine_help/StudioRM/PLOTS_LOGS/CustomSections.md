# Section Definition  
  
To access this screen:

  * Display the [**View Settings**](<../COMMON/Section%20Definition%20Dialog.md>) screen and click the **Section Definition** tab.

Sections are used in plots for the following reasons:

  * To orient a view direction relative to a section (for example, orthogonal).

  * To see where a 3D plane at a known location and orientation intersects 3D data.

There are several ways to access section properties to edit them. The example activity below uses the **Section Definition** screen, but you can also edit sections using the **Projection (Section)** ribbon, visible when you click a projection in a plot sheet.

Another way to edit sections is to modify them using **Sheets** or **Project Data** control bar options. See [3D Sections](<../VR_Help/Sections.md>). Sections created in the 3D window can be accessed for use in plots.

You can also edit the active section of a projection using the projection's properties. See [Sections and Projections](<alignviewwithsection.md>).

**Note** : To create a section definition table, use 3D window functions. See [3D Sections](<../VR_Help/Sections.md>).

Activity steps:

  1. Ensure [Page Layout Mode](<PageLayoutMode.md>) is not active.

  2. Right-click a projection and select **View Settings**.

The **View Settings** screen displays.

  3. Select the **Section Definition** tab.

  4. Set the general orientation of the section (the current settings display here):

     * Choose a preset (**Horizontal** , North-South or **East-West**) orientation, or;

     * Enter an Azimuth and **Dip** value for a custom orientation that doesn't align with a major world axis.

  5. Choose the **Mid-Point** of the section. This determines where the centre of the section plane lies in world coordinates. Enter **X** , Y and Z values.

  6. Choose the section **Width**. This determines how **[clipping](<ClipView.md>)** is applied, and the extent of movement when the **Next** and **Previous** buttons are used on the **Plots (View)** ribbon.

  7. To adjust the position of the Mid Point, use the Position arrows to shift the section plane in a direction orthogonal to itself. For example, a horizontal plane shifts the Z coordinate.

  8. Toggle **Apply Clipping** to control if data clipping is applied to data projections that use this section.

  9. Decide how data updates in the plot sheet following changes to the section:

     * If **Dynamic** is **checked** , projection data that uses the target section updates instantly to show a new data direction, or section position.

     * If **Dynamic** is **unchecked** , projection updates only occur when **OK** or **Apply** is clicked.

  10. Click **OK** to dismiss the **Section Definition** screen and return to the plot sheet.

Related topics and activities

  * [View Settings](<../COMMON/Section%20Definition%20Dialog.md>)

    * Section Definition

    * [View Rotation Settings](<Plots-ViewSettings-Rotate.md>)

    * [Size/Scale](<../COMMON/view%20settings%20scale%20dialog.md>)

    * [Section Width Settings](<Plots-ViewSettings-SectionWidth.md>)

    * [Projection Exaggeration Settings](<Plots-ViewSettings-Exaggeration.md>)

  * [Sections and Projections](<alignviewwithsection.md>)

  * [Projection Overlay Types](<Projection%20Overlay%20Types.md>)

  * [Add a Sheet or Projection](<insertsection.md>)

  * Section Definition

  * [Clipping Plots Data](<ClipView.md>)

  * [Zoom, Scale & Pan](<Zooming.md>)

  * [Align Sections](<alignsection.md>)