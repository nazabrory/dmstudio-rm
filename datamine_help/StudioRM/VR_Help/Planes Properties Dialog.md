# Plane Properties

To access this screen:

  * **Sheets** or **Project Data** control bar **> > 3D Folder >> Planes >> Right Click an Overlay >> Properties**.
  * Double click a planes object overlay in the **Sheets** or **Project Data** control bar.
  * Double click a planes object overlay in a 3D view.

Planes are oriented 2-dimensional shapes that depict a particular dip or dip direction. They are commonly used in geological structure analysis and, in particular, the assessment of potential failure domains at the face, and joint space analysis.

Note: Planes are, in practice, a point in space with information about orientation. Their database looks similar to a point object for this reason.

Planes are commonly generated from strings (using the **Convert to Planes** context menu option in the **Sheets** or **Project Data** control bar). For each string, an average plane is calculated which best fits all the points in the string (open or closed). The plane is oriented around its line of true dip, and extents calculated to just fit the source string.

The **General** tab of the **Planes Properties** screen allows you to format an existing plane, using one of these tabs:

  * **General** Configure general visual formatting for the plane such as shape, colour and opacity. See below.
  * **Labels** Specify annotation for your plane object overlays. See [Planes Properties: Labels](<Planes_PropDialog_Labels.md>).
  * Associated files Review and launch any external data files associated with the current data object. See [Associated Files](<Associated%20Files%20Dialog.md>).
  * Info Mode List Control the attributes that are displayed for the data object when using **Dynamic Information Mode**. See [Info Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>).
  * Templates Apply, edit, define and delete 3D window formatting templates here. See [3D Display Templates](<3D_Templates.md>).

To configure general 3D display properties for a plane object overlay:

  1. Display the **Planes Properties: General** screen.

  2. Review the Name of the overlay. You can also edit this.

  3. Review the **Source** of the overlay. This is the name of loaded data object represented by the overlay and is read-only.

  4. By default, planes are shown as circular discs, but you can change the **Display Type** to _Rectangles_.

  5. Choose the **Color** of the planes using the [Legend Controls](<Legend-Pallete.md>).

  6. Set the Opacity of the overlay. By default, it is fully opaque (100%). Use the slider to adjust this. By default, a plane is 50% opaque.

  7. Choose if 3D scene clipping affects the overlay using Apply Clipping.

     * If **checked** , global scene clipping settings apply to the overlay.

     * If **unchecked** , the picture object is rendered without clipping regardless of scene clipping settings.

  8. Click **OK** to apply the overlay settings to the object overlay.

Related topics and activities:

  * [The Planes folder](<Sheets_Planes.md>)

  * [Creating Planes](<Creating%20Planes.md>)

  * [Associated Files](<Associated%20Files%20Dialog.md>)

  * [Info Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>)

  * [3D Display Templates](<3D_Templates.md>)