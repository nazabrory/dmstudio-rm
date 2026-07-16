# Format Display

To access this screen:

  * In the Sheets or **Project Data** control bar, double-click a Grids overlay in a [2D plot sheet projection](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>).

  * Use the quick key combination "fdd" where a 3D-view-oriented projection is selected.

  * Use the quick key combination "fdd" where a 2D-axis-oriented projection is selected (and **Only display in 3D views** is set to _No_).

  * This screen is also displayed when various context-sensitive formatting commands are run throughout your application.

The Format Display screen is used to manage the display and formatting parameters for grids, object overlays, display templates, hull, section line; manage holes sets and overlay drawing order for the Plots window, and specifically, the formatting of 2D projection overlays.

Note: Settings applied here are exclusive to 2D plot projections shown in a 3D orientation and do not affect data shown in 3D plots projections, 2D projections oriented to an axis, or any 3D window.

Options are configured within tabs along the top of the screen, with additional tabs available on the Overlays tab, on the right of the screen.

The following tabs may be available, please select a link below for more information:

  * [Hole Set](<../PLOTS_LOGS/Format%20HoleSetDialog.md>)

  * [Grids](<format%20grid%20dialog.md>)

  * [Overlays](<format%20display%20dialog_overlays.md>)

  * [3D Rendering](<Format%20Display%20Dialog_3D%20Rendering.md>)

  * [Section Line Properties](<../PLOTS_LOGS/section%20line%20properties.md>)

  * [Hull Properties](<../PLOTS_LOGS/hull%20properties.md>)

  * [Drawing Order](<Drawing%20Order%20Dialog.md>)

This **Format Display** screen is used to control many aspects of how data is displayed, including the creating and management of [overlays](<View%20Hierarchy.md>). Overlays constitute fundamental building blocks of effective data display. 

The screen is also used for the creation of plot display [templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>). These powerful files are easily created using very similar tools and functions to those used in the application and editing of overlay settings.

## What is an Overlay?

In brief, an overlay dictates how a representation of an object is made. Each overlay dictates the color, linestyle, rendering method, annotation, symbol format, shading format and other display options. When defining an overlay you can either:

  * Define visual settings directly for an overlay, which is associated with a loaded data object. 

    * An object can have multiple overlays.

    * An overlay represents a collection of display settings.

  * Extract the settings from the current overlay to create a plot display template. See [Plot Sheet Templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>).

    * Templates can be used to transfer visual settings from one object to another of the same type.

Note: Templates created using the **Format Display** screen are referred to as "Plot Templates". These aren't applicable to 3D window overlays, where separate template facilities exist.

## Automatically Creating Overlays

Data display templates can be applied manually to objects as required, or they can be used to automatically create an overlay (or even multiple overlays) each time data of a particular type is loaded, using the Apply on Load feature. For example, you could load a drillhole data set which automatically created separate overlays to display downhole columns showing a histogram, a lithology bar, borehole ID annotation and so on. If you use a common data display format for more than one situation, this facility can save you a lot of display formatting time.

## Display Legends

Display legends are a useful way of applying conditional formatting to data overlays. In essence, a legend contains the information that dictates which data value(s) is assigned to which display property. Each legend interval (or 'bin') is dictated either as a unique value, a range or a filter expression.

Display legend information is output to a display template, if one is created, meaning you do not have to manually import or export .elg files to standardise on a display format across projects.

Wherever a data column value is found that matches a particular interval, that data is drawn using the assigned properties. For example, if a legend bin is defined as being a gold grade of 1-1.5 ppm and that particular legend item is set as being drawn in yellow, that particular range legend would be applied to the AU column using the Format Display dialog. Once set, the next time the data is redrawn, all data rows that carry an AU value between 1 and 1.5 is coloured in yellow.

### Handling Absent or Unmatched Data

All automatically-generated legends (that is, those created using the Legend Wizard) will contain a default bin that is assigned to absent values. Absent values are special values in data tables, normally associated with the character "-" (hyphen). This setting is determined by the Data Conversions dialog.

If absent data is interpreted, it is assigned a display format according to that automatically generated bin.

However, in some cases, no match can be made at all. For example, if a legend contains several bins extended from the value 1 through to, say, 3.5 inclusive, and data values are intercepted above 3.5, those values are regarded as 'unmatched'.

Unmatched data is drawn using which Fixed Color is currently assigned for the overlay. In the case of drillholes, this is the On-Section colour. Therefore, it is possible to set up the display format for all data rows that can be interpreted by a legend and also to determine what is shown when a value cannot be matched.

In short, unmatched data will use the Fixed Color for the overlay in context. Absent data values are indicated by the specific absent data conversion value, and should not be confused with unmatched data.

Note: You may have noticed inconsistent use of English and American spelling of the word "colour" throughout Studio products. We're aware of this and will be standardizing on the English spelling over time. The American format is typically legacy.

Related topics and activities:

  * [Formatting Object Overlays](<Formatting%203D%20Objects.md>)

  * [Views, sheets and overlays](<concept_views%20sheets%20overlays.md>)

  * [Plot Sheet Templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>)

  * [Format 2D Drillhole Overlays](<Format%20Drillholes.md>)