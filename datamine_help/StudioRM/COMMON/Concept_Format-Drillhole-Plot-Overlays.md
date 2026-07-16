# Format Drillholes in Plot Projections

The distinction between [static and dynamic drillholes](<Drillhole%20Representation%20in%20Studio.md>) is important when applying overlay formatting; in-memory dynamic drillhole data will be listed as "Holes Overlay" in the Format Display overlays list, and can be formatted in the same way as a static (file-based) drillhole object. When a drillhole overlay (static or dynamic) is highlighted, the area on the right of the Format Display dialog will update to show a Style and Drillholes sub-tab.

It is important to resolve ambiguities when displaying block model intersections

Where the intersection of a block model and a plane is being displayed, an ambiguity can occur when the plane falls exactly on a cell boundary. This is caused by the fact that the two adjacent cells will intersect the plane at the same point, so it is not clear which should be used to dictate drawing attributes. To resolve this ambiguity, EwLib detects the case where a plane falls on a major cell boundary, and then offsets the plane by a small amount so that it falls into either one cell, or the other.

To control how this issue is handled, the **Model Intersection Plane Bias** option exists in the Format Display screen's **Overlays** tab, which allows control over whether the intersection plane is biased forwards (in the direction of the plane normal), or backwards. 

Note: The trivial offset amount is preset at 1E-6 in block coordinates (i.e 1E-6*block width/height/length, as appropriate). 

Related topics and activities:

  * [Format 2D Drillhole Overlays](<Format%20Drillholes.md>)

  * [Preview Downhole Columns in Plots](<Activity-Drillhole-Previewer.md>)

  * [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>)

  * [Plot Sheet Templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>)

  * [Format Display](<Format%20Overlays%20Dialog.md>)
  * [Format Display: Overlays](<format%20display%20dialog_overlays.md>)

  * [Format Column Display](<../VR_Help/DH_PropDialog_Columns_Format.md>)

  * [Desurvey Methods Introduction (Static/Dynamic)](<Drillhole%20Representation%20in%20Studio.md>)