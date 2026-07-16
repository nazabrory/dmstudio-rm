# Points Properties: General

To access this screen:

  * **Sheets** or **Project Data** control bar **> > 3D Folder >> Points >> Right Click an Overlay >> Properties**.
  * Double click a points object overlay in the **Sheets** or **Project Data** control bar.
  * Double click a points object overlay in a 3D view.

Use this screen to general 3D visualization settings for loaded point data object overlays.

The Points Properties screen has the following tabs:

  * **General** Configure general 3D visualization settings for points, including animation sequence playback and clipping options. See below.
  * **Symbols** Set up the format of the point including its shape or model, size, rotation and colour. See [Points Properties: Symbols](<Point_PropDialog_Symbols.md>).
  * **Labels** Specify annotation for your plane object overlays. See [Planes Properties: Labels](<Planes_PropDialog_Labels.md>).
  * Associated files Review and launch any external data files associated with the current data object. See [Associated Files](<Associated%20Files%20Dialog.md>).
  * Info Mode List Control the attributes that are displayed for the data object when using **Dynamic Information Mode**. See [Info Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>).
  * Templates Apply, edit, define and delete 3D window formatting templates here. See [3D Display Templates](<3D_Templates.md>).

To configure general visualization settings for loaded point object overlays:

  1. Display the **Points Properties: General** screen.

  2. Review the Name of the overlay. You can also edit this.

  3. Review the **Source** of the overlay. This is the name of loaded data object represented by the overlay and is read-only.

  4. If you are planning to display a sequenced animation of data in the 3D view (see [Sequence Animations](<Sequencing.md>)), define the Sequence Column containing the numeric values that will control the playback. 

Once selected, the following options become available:

     * Forward Animate the data file according to the increasing value of the selected attribute column.

     * Single Frame Replace instead of adding to displayed view frames.

     * Reverse Select this option to play the sequencing animation in reverse (from the highest record to the lowest record value in the Sequence Column).

     * Anim. Rate This value represents the 'speed' at which the 'steps' are played. The most appropriate value depends on many factors, including the density of the data and how many 'steps' are in a particular animation.

     * Anim. Step This value determines the step size in the animation and equates to the number of records displayed or hidden for each frame. It is based on the values in the selected Sequence Column.

     * Loop Animation Check to replay your animation from the beginning once the final 'frame' has been displayed.

  5. Choose if 3D scene clipping affects the overlay using Apply Clipping.

     * If **checked** , global scene clipping settings apply to the overlay.

     * If **unchecked** , the picture object is rendered without clipping regardless of scene clipping settings.

  6. Click **OK** to apply the overlay settings to the object overlay.

Related topics and activities:

  * [Points Properties: Symbols](<Point_PropDialog_Symbols.md>)

  * [Points Properties: Labels](<Points_PropDialog_Labels.md>)

  * [Associated Files](<Associated%20Files%20Dialog.md>)

  * [Info Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>)

  * [3D Display Templates](<3D_Templates.md>)