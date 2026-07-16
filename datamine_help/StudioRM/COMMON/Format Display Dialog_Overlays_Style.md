# Format Display: Style

To access this screen:

  * Display the **[Format Display](<Format%20Overlays%20Dialog.md>)** screen, enable the **Overlays** view and click the **Style** tab.

Configure how [2D plot projection](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>) overlays are presented. This can either be by manual configuration or by applying a **[template](<Data%20Display%20Templates.md>)**. You can also use this screen to update an existing template.

Select an overlay or data display template from the Overlays list to show the current format settings. The settings of that overlay or template display on the right (under the **Style** tab). Settings are automatically stored with the target overlay or template when you **Apply** them (or click **OK** to dismiss the **Format Display** screen).

### Format an Overlay

In the following activity, the term "overlay" can refer either to an actual plot projection overlay or a template that can be applied to an overlay.

To configure the visual style of an overlay or template:

  1. Display the **Style** tab.

  2. Decide if the target overlay is visible or not using Visible. Invisible overlays do not appear in projections but can be redisplayed at any time.

  3. Choose the basic display format to use, with Display As options (not all options are available for all data types):

     * **Points** Display data vertices only.

     * **Labels Only** Display the overlay labels only, with no other 3D geometry in view. This can be useful if you have configured point data purely for the purpose of positioning annotation in a plot sheet, for example.

     * **Lines** Display only the edges of a string overlay. Not available for other data types.

     * **Faces** Display only the faces of a wireframe object.

     * **Blocks** Display a block model as cuboids.

     * **Arrows** Display arrows in place of drillhole segments and string edges to show the direction of data.

     * **Intersection** Display a block model or wireframe as an intersection with the currently active [section](<../PLOTS_LOGS/CustomSections.md>) plane.

     * **Drillholes** Display static drillhole data as a formatted downhole column.

  4. For block model and wireframe data, choose if **3D Rendering** mode should be active. This mode uses alternative rendering routines to provide additional visual formats (at the cost of performance).

**Note** : 3D Rendering mode is largely superseded by [3D projection](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>) formatting options. Consider creating a 3D projection instead.

If 3D Rendering mode is active, pick a **Shading** and Draw Mode. See [3D Rendering Options](<Format%20Display-3D-Rendering-Mode.md>).

Also see [3D Rendering Options](<Format%20Display-3D-Rendering-Mode.md>).

  5. For strings data, choose if Snap Points are displayed when digitizing 3D features.

  6. For block model data, choose how any ambiguity is resolved if a block model cell boundary lies exactly on an intersection plane. These options are only available if the **Display As** setting is _Intersection_.

You have the following options:

     * Shift the intersection plane **Backwards** by a tiny amount (1E-6*block width/height/length as appropriate) to ensure a clean intersection of model and section plane.

     * As above, but shift the section plane Forwards slightly.

     * Use the **Default** settings as specified by your [Data Options](<data%20options.md>). This setting is the same for all Studio applications on the current PC.

  7. To apply an existing **Template** to the overlay, select it and click **Apply Template**.

     * Check Apply to all overlays displaying [object name] to override the display of all overlays relating to the same data object. This is useful if you have multiple overlays of the same object and want to format them in the same way.

See [Format Display: Templates](<Data%20Display%20Templates.md>).

  8. To update an existing **Template** with the current overlay settings, select it and click **Update Template**. 

  9. Click **OK** or **Apply** to update the display of data in 2D plot projections of the active plot sheet.

Related topics and activities

  * [Format Display](<Format%20Overlays%20Dialog.md>)

  * [Format Display: Templates](<Data%20Display%20Templates.md>)

  * [Add a Display Template](<add_template_dialog.md>)

  * [Format Display: Color](<Format%20Display%20Dialog_Overlays_Color.md>)

  * [Format Display: Symbols](<format%20display%20dialog_overlays_symbols.md>)

  * [Format Display: Feature](<Format%20Display%20Dialog_Feature.md>)

  * [Format Display: Feature](<Format%20Display%20Dialog_Feature.md>)

  * [Format Display: Labels](<Format%20Display%20Dialog_Overlays_Labels.md>)

  * [Format Display: Advanced](<Format%20Display%20Dialog_Overlays_Advanced.md>)

  * [3D Rendering Options](<Format%20Display-3D-Rendering-Mode.md>)

  * [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>)

  * [Data Options](<data%20options.md>)