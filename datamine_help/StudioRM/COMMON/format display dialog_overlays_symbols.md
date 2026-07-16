# Format Display: Symbols

Note: These settings relate to the format of data object overlays in 2D plot projections. See [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>).

To access this screen:

  * Display for the [Format Display](<Format%20Overlays%20Dialog.md>) screen and select the **Symbols** tab.

Symbols are used during data display to highlight the terminal points of string data. Symbols can either be specified so that the same symbol will be used throughout, or symbols can be modified as regards size, rotation or shape according to a particular value in a database column. For example, to add a symbol representing the specific grade of mineral content at key positions along a drillhole sample, alternatively, symbols may simply be used to show the ends of line segments.

To configure symbols for plot projection overlays or downhole columns:

  1. Display the **Symbols** screen.

  2. Choose either a Fixed **Symbol** or using a symbol code in a data Column, matched to a symbol Legend. See [3D Symbols Library](<Symbol%20List.md>).

  3. Similarly, choose a Fixed symbol **Size** (in screen mm) or derive the size from a data Column and Legend.

  4. Choose the Rotation of your symbols. You can specify the alignment of a symbol, either globally, or via legend values.

     * Fixed Specify a rotation in degrees for all symbols.

     * Dip Choose a data Column containing dip values and (optionally) do the same for Dip Direction.

       * If checked, use Draw in 2D to determine is symbols are drawn as 'flat' shapes, regardless of the assigned dip and dip direction values.

Note: This can be useful when symbols with a given dip and dip direction are no longer visible from the current view direction.

     * Point Along Lines Ensure all symbols are aligned with along the line (pointing in the direction of the line). If unchecked, symbols will be displayed at the specified rotation regardless of the line direction.

  5. If you want to store your Labels formatting in the current display template, click Update Template. See [Data Display Templates](<Data%20Display%20Templates.md>).
  6. Click **OK**.
  7. Save your project.

Related topics and activities:

  * [Format Display](<Format%20Overlays%20Dialog.md>)

  * [Format Display: Style](<Format%20Display%20Dialog_Overlays_Style.md>)

  * [Format Display: Color](<Format%20Display%20Dialog_Overlays_Color.md>)

  * [Format Display: Feature](<Format%20Display%20Dialog_Feature.md>)

  * [Format Display: Advanced](<Format%20Display%20Dialog_Overlays_Advanced.md>)

  * [Data Display Templates](<Data%20Display%20Templates.md>)