# Format Downhole Columns in 2D Plots

You can specify the visual formatting settings for a static or dynamic drillholes overlay in **[Plot](<Window_PLOTS_Overview.md>)** window [2D projections](<../PLOTS_LOGS/alignviewwithsection.md>).

Note: This activity is not relevant to formatting 3D window overlays, nor drillhole overlays rendered in 3D plot projections. See [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>). For information on formatting 3D window downhole columns, see [Drillhole Properties: Columns](<../VR_Help/DH_PropDialog_Columns.md>).

To add downhole columns to a DYNAMIC drillhole overlay:

  1. Display the Format Display screen

  2. Select a dynamic drillhole overlay.

  3. Select the Drillholes tab. See [Format Drillholes in Plot Projections](<Concept_Format-Drillhole-Plot-Overlays.md>).

  4. Click Insert.

The [Column Wizard](<../PLOTS_LOGS/columnwizard.md>) displays.

  5. Choose the type of column to add:

     * Select Data Column if you are displaying columns that relate to data attribute values (such as grade, rock type and so on).

     * Select System Field if you want to present calculated hole information such as vertical thickness, for example.

  6. Click Next to display the **Select the table** screen.

  7. Pick the drillhole data object you plan to enhance and click Next.

  8. On the Select the fields screen, select the data description that represents the values you wish to represent.

  9. Click OK to launch the [Format Column](<../VR_Help/DH_PropDialog_Columns_Format.md>) screen, where you can set the Alignment, Border, Width/Margins, Filter, Template, Graph/Color or Text settings. See [Format Overlay or Column](<../VR_Help/DH_PropDialog_Columns_Format.md>).

Note: This screen is identical to the one displayed for 3D window downhole column formatting.

  10. Click OK to add the downhole column to the drillhole trace - the preview is automatically updated.

  11. Use the Previewer to fine tune the relative position of the column to the drillhole.

  12. Click **OK** or **Apply** to update the target drillhole object overlay in the 2D projection.

To add Downhole Columns to a STATIC drillhole overlay:

  1. Display the Format Display screen

  2. Select a static drillhole overlay.

  3. Select the Drillholes tab. See [Format Drillholes in Plot Projections](<Concept_Format-Drillhole-Plot-Overlays.md>).

  4. Click Insert.

The **Select Column** screen displays.

  5. Select a data attribute containing values to present (you can select a numeric or alphanumeric field).

  6. Click OK to launch the [Format Column](<../VR_Help/DH_PropDialog_Columns_Format.md>) screen, where you can set the Alignment, Border, Width/Margins, Filter, Template, Graph/Color or Text settings. See [Format Overlay or Column](<../VR_Help/DH_PropDialog_Columns_Format.md>).

  7. Click OK to add the downhole column to the drillhole trace - the preview will be automatically updated.

To change the appearance of an existing downhole column (any type):

  1. Display the Format Display screen

  2. Select a static drillhole overlay.

  3. Select the Drillholes tab. See [Format Drillholes in Plot Projections](<Concept_Format-Drillhole-Plot-Overlays.md>).

  4. Use the Previewer to select the column indicator in the preview pane so it is highlighted.

  5. Click Format

Tip: You can also double-click the column indicator or right-click the column and select Format from the context menu.

  6. Click OK to launch the [Format Column](<../VR_Help/DH_PropDialog_Columns_Format.md>) screen, where you can set the Alignment, Border, Width/Margins, Filter, Template, Graph/Color or Text settings. See [Format Overlay or Column](<../VR_Help/DH_PropDialog_Columns_Format.md>).

  7. Click OK to add the downhole column to the drillhole trace - the preview is automatically updated.

  8. Use the Previewer to fine tune the relative position of the column to the drillhole.

  9. Click **OK** or **Apply** to update the target drillhole object overlay in the 2D projection.

To manage the layout of existing downhole columns:

  1. Display a plot sheet with at least one 2D projection containing drillhole overlay data.

  2. Display the [Format Display](<Format%20Overlays%20Dialog.md>) screen.

  3. In the **Overlay Objects** group, select a drillhole object overlay.

  4. Select the **Drillholes** tab.

  5. Choose if you want to display both drillhole and columns, using Display drillhole traces. 

     * If **checked** , the drillhole trace (the underlying string that represents the geometry of the drillhole) is drawn with downhole columns. 

If **unchecked** , the drillhole trace is not drawn (although any downhole columns will use the positional data to derive their correct positions).

  6. Similarly, use **Display drillhole columns** to control if columns are displayed or not.

Tip: Unchecking this option retains existing downhole column settings, so can be a useful way of temporarily switching the columns off.

  7. Check Auto arrange to position columns automatically at an equal distance on either side of the downhole trace. If unchecked, column positions retain custom positions.

  8. Check Snap to columns to snap the column positions to key areas during drag-and-drop, allowing for easier positioning of columns. If unchecked, positioning is unconstrained.

  9. Use the **Drillhole Previewer** to fine-tune the positions of each downhole column as well as inserting and formatting the columns. See [Preview Downhole Columns in Plots](<Activity-Drillhole-Previewer.md>).

  10. Optionally, store your formatting information to a plot template. See [Plot Sheet Templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>).

  11. Click **OK** to update the display of the drillhole data in the current plot projection.

  12. Save your project.

Related topics and activities:

  * [Format Drillholes in Plot Projections](<Concept_Format-Drillhole-Plot-Overlays.md>)

  * [Preview Downhole Columns in Plots](<Activity-Drillhole-Previewer.md>)

  * [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>)

  * [Plot Sheet Templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>)

  * [Format Display](<Format%20Overlays%20Dialog.md>)
  * [Format Display: Overlays](<format%20display%20dialog_overlays.md>)

  * [Format Column Display](<../VR_Help/DH_PropDialog_Columns_Format.md>)

  * [Desurvey Methods Introduction (Static/Dynamic)](<Drillhole%20Representation%20in%20Studio.md>)