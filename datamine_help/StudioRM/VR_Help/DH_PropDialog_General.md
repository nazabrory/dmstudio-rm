# Drillhole Properties: General

To access this screen:

  1. In the Drillholes folder in the Sheets or **Project Data** control bars, right-click a drillholes file and select Properties. The **General** screen is shown by default.

  2. Double-click a drillhole overlay in any 3D window. The **General** screen is shown by default.

  3. In the Drillholes Properties screen, select the General tab.

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

Define the name, sequence column, clipping and sequence options for selected drillholes. 

The settings described here apply to a target 3D overlay. Updating its settings affects the view of that **[overlay](<../COMMON/concept_views%20sheets%20overlays.md>)** in the associated 3D window(s), including all linked external windows. [Independent](<../COMMON/Independent_3D_Windows.md>) 3D windows are unaffected.

To configure the visual formatting of the target drillhole object overlay:

  1. Review the **Name** of the drillhole overlay. This name represents the overlay only, and changing it will not change the underlying object or data file name.

**Tip** : use a naming convention that represents your data _overlay_ , not data _object_. See [Windows, Sheets, Projections and Overlays](<../COMMON/concept_views%20sheets%20overlays.md>).

**Note** : you can also change an overlay name by right-clicking an overlay in the **Sheets** or **Project Data** control bar and selecting **Rename**.

  2. Check the **Source** of the overlay. This is the name of the data object that your overlay is presenting.

  3. If you plan to use the **Sequence Controls** tool bar to animate your drillhole data according to the value of a particular numeric attribute, select one from the **Sequence Column** list. See [Sequence Control](<Sequence%20Control%20Dialog.md>). These settings also affect how an animation is played back in the 3D window.

Once a **Sequence Column** has been picked, you have further options over how 3D window animation is performed:

     * **Forwards** play the sequencing animation in a forwards direction; that is, from the lowest to the highest value for **Sequence Column**.

     * **Single Frame** select this option to display each frame of the animation individually. A non-zero value must be defined in the Anim. Step box.

     * **Reverse** select this option to play the sequencing animation in reverse; that is, from the highest to the lowest value for **Sequence Column**.

     * **Independent Sequence** if selected, allows you to change the animation rate and step values, and specify whether to loop or annotate the animation.

     * **Anim. Rate** the speed of the animation measured in sequence units per second. Sequence units are the units associated with the **Sequence Column** value. For example, if the unit of "weeks" is associated with a selected value, the animation is played at a rate of weeks per second.

     * **Anim. Step** this value determines the step size in the animation. A value of 0 (default) allows the animation to change continuously without fixed steps. Where the values associated with the **Sequence Column** vary in specific steps, for example in integers, the value specified for Anim Step can enforce the same behavior in the animation; for example, it can be set to 1 to only display integer values.

     * **Loop** check to replay the animation from the beginning after the final 'frame' is shown. If unchecked, the animation plays once only.

     * Annotateselect the column containing values to annotate your animation. These values display in the 3D window and update for each frame during playback.

     * Show Annotationif selected, then values for the column selected in the Annotate list are shown with the animation.

     * Configureallows you to configure the font, position and text parameters for the annotation using the [Sequence Annotation Overlay](<SequenceAnnotationOverlay_Dialog.md>) screen.

  4. Choose if clipping is applied to the target overlay:

     * If **Apply clipping** is **checked** , the target overlay responds to 3D window data clipping changes (front, back, outside and so on).

     * If **Apply clipping** is **unchecked** , clipping instructions are ignored and the target overlay is displayed fully, regardless of other clipping settings.

  5. Click **Apply** to update the current 3D window view(s) and leave the properties screen visible, or **OK** to apply settings and dismiss the properties screen.

Related topics and activities

  * [Drillholes: Style](<DHPropDialog_Segments.md>)

  * [Drillholes Properties: Symbols](<Drillholes%20Properties%20Dialog%20\(Symbol%20Visual\).md>)

  * [Drillholes Properties: Labels](<DH_PropDialog_Labels.md>)

  * [Drillhole Properties: Columns](<DH_PropDialog_Columns.md>)

  * [Drillholes Properties: Segments](<DHPropDialog_Segments.md>)

  * [Drillholes Properties: Associated Files](<Associated%20Files%20Dialog.md>)

  * [Drillhole Properties: Info Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>)

  * [3D Display Templates](<3D_Templates.md>)

  * [3D Window Templates](<../COMMON/3D_Window_Templates.md>)