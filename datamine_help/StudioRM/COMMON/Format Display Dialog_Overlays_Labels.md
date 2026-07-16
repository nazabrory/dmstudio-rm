# Format Display: Labels

Note: These settings relate to the format of data object overlays in 2D plot projections. See [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>).

To access this screen:

  * Display for the [Format Display](<Format%20Overlays%20Dialog.md>) screen and select the **Labels** tab.

Labels are used to annotate labels in the **Plots** window and when formatting downhole columns. Labels are assigned to key points on an objects geometry (line segment ends, wireframe triangle junctions and so on). 

Tip: You can display one or more labels for each overlay. All defined overlays display in the order shown in the **Labels** list.

Note: Settings are per-overlay. Select an overlay using the list on the left.

To configure Plot projection or downhole column labels:

  1. Display the **Labels** screen.
  2. Select the overlay to be labelled using the Overlays list on the left.
  3. Select the label to be defined using the **Labels** list, or add a New label (each object can have more than one label set). 

  4. Note: You can also Delete existing label configurations.

  5. Click Reset and use the [Reset Labels](<Format%20Display%20Dialog_Reset%20Labels.md>) screen to choose an attribute within the data object containing values to be displayed as annotation. Also use this screen to define how many columns and rows of information appears when multiple labels are added.
  6. Select the **Labels** screen's Style tab and click the label attribute to display the Format screen.
  7. Define the new label's visual format. See [Format Overlay or Column](<../VR_Help/DH_PropDialog_Columns_Format.md>). 
  8. Click **OK** to return to the **Labels** screen.
  9. Back on the Format Display screen, select the Contents tab.

Note: The **Contents** screen shows all available labels in a grid, the size of which is determined by the **Reset Labels** screen. You can edit the attribute that appears in any position using the matrix of lists provided. 

  10. Define the Row height (mm) and Column width (mm) for the table that hosts your labels.
  11. If Include field names in the annotation is checked, each value is prefixed with the selected attribute name, otherwise only the value for each data point appears.
  12. If Clip lines and arrows behind annotation is checked, the tabular labels information obscures data behind it, otherwise projection data displays with the annotation.
  13. Set up the [Font](<format%20display%20dialog_font.md>) and [Position](<format%20display%20dialog_annotation%20position.md>) of the label.
  14. If you want to store your Labels formatting in the current display template, click Update Template. See [Data Display Templates](<Data%20Display%20Templates.md>).
  15. Click **OK**.
  16. Save your project.

Related topics and activities:

  * [Reset Labels](<Format%20Display%20Dialog_Reset%20Labels.md>)

  * [Formatting Object Overlays](<Formatting%203D%20Objects.md>)

  * [Annotation Position](<format%20display%20dialog_annotation%20position.md>)

  * [Format Overlays](<format%20display%20dialog_overlays.md>)