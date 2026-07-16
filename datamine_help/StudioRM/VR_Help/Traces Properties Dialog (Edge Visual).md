# Strings Properties: Lines

To access this screen:

  * Display the [String Properties](<Traces_Properties.md>) screen and select the **Lines** tab.

Control how the lines (edges) between points are drawn to the screen in the active 3D window. 

To configure the display of string data for the target overlay:

  1. Display the string data to be formatted in any 3D window.

  2. Display the **Lines** screen.

  3. Display Lines is enabled by default. You can hide the overlay by unchecking it, but this will disable all other controls on this screen.

  4. Choose the display **Type** :

     * 2D The width of lines remains the same, regardless of the viewing distance.

       * Specify the **Style** attributes associated with either 2D or 3D lines. If required, a legend/column pair must be specified individually for both line style and width. See [Legend Controls](<Legend-Pallete.md>).

       * Check **Guideline** to display a single-pixel-width line in addition to the primary string display.

     * 3D Lines have a three-dimensional appearance, and their size may vary depending on the viewing distance and direction.

       * Default Cylinder: the default 3D line style is used, which is a cylinder.

       * Imported Model: allows you to specify any 3D object by browsing to an external DirectX (.X) file. This is scaled to fit into each edge.

       * Check **Guideline** to display a single-pixel-width line in addition to the primary string display.

       * Transparent Textures Available if Imported Model is selected. The colour keying process is used to make a specified colour transparent; in this case, black (0,0,0). When this option is selected, black areas of the imported model are made completely transparent.

  5. Define the **Size** (=the width) of the string edges. 

Both 2D and 3D line styles can be sized and scaled by either a fixed amount, or based on their associated data attributes. For 2D lines, these control the width of the line in pixels on the screen. For 3D lines, they control the amount that the underlying 3D object is expanded in world space.

     * Define a **Legend** and **Column** to control string edge widths based on data values. If _< none>_ is selected for **Legend** , scaling is universal throughout the overlay.

     * Limit the Minimum and Maximum line width if required using **Constraints** options.

     * Define a **Scale** factor. This is multiplied by the base size value for the string, either as a fixed amount, or a factor applied to the data values in the selected **Column**.

  6. Define the string **Color**. See [Legend Controls](<Legend-Pallete.md>).

  7. For closed strings, you can flood the inside of the enclosed string by checking **Filled**. This has no effect on open strings

Note: If a legend is specified for colouring, the value in the legend for Fill Color is used, rather than the value for Line Color. 

     * For filled strings, adjust the **Opacity**.

     * For filled strings, if a texture legend is selected, adjust the **Legend Tile Size** to get the effect you want.

  8. By default, a single attribute is used for colouring, size and line style. Check Color by Edge to determine the colour, size and line style of each string edge based on its individual data attributes.

Related topics and activities

  * [String Properties: General](<String_Properties_Dialog_General.md>)

  * [String Properties: Symbols](<String_Properties_Dialog_VertexVisualTab.md>)

  * [Strings Properties: Labels](<StringProp_Labels.md>)

  * [Associated Files](<Associated%20Files%20Dialog.md>)

  * [Info Mode List](<Traces%20Properties%20Dialog%20\(Info%20Mode%20List\).md>)

  * [3D Display Templates](<3D_Templates.md>)