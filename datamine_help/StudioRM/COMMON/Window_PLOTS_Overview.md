# The Plots Window

The Plots window with its comprehensive suite of data source drivers, can use data from a huge variety of sources and bring it all together into a single model showing all the characteristics and properties you choose, and in whatever format you select to maximize the presentational impact.

This lets you produce representations of your operational data in sections, plans and 3D views and provides peerless possibilities for pictorial core logging. 

The Plots window allows you to:

  * Import drillhole data with many formats, from different sources, including: text, SQL/ODBC database tables, spreadsheets and other third party formats.

  * Verify the data then combine and process it to create drillhole traces indexed to multiple tables for downhole intervals and Depth logs.

  * View, format and print the downhole data tables in tabulated sheets.

  * Plot drillhole traces and indexed sample data values in plan, section or any three-dimensional view desired. A complete family of sections can be defined from a single section definition using a single dialog.

  * View the same section in multiple views controlled by a section master.

  * Plot all downhole data as scaled drillhole log sheets. A wide selection of presentation styles are available including text, line graphs, histograms and bars with optional color fill and pattern fill.

  * Embed plot projections containing either 2D or 3D overlay representations. See [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>).

  * Graphically interrogate and composite the drillhole data in table, section, 3D or log views. All views can be linked dynamically so that samples selected in any one view are selected in all linked views.

  * Draw interpretations directly onto section plots then save them as 3D polygons which can be exported.

  * Select and save ore zone intersections which can then be displayed in section and log plots, reported and exported.

  * Insert smart plot items like text boxes, coordinate grids, scale bars, tables and title blocks which automatically adjust as you change the position, orientation and scale of plot sheets.

  * Insert parameter profiles which dynamically re-intersect the surface model as the section is rotated or re-positioned.

  * Import and format other 3D objects from CAD drawings and other 3D data sources using the Data Source Drivers.

  * Select different paper sheet sizes, orientations, margins and scales for each view type, all within the same document.

  * Use Page Layout mode to display and edit interactively page borders, sheet margins, plot frames, coordinate grids, plot items and parameter profiles. See [Page Layout Mode](<../PLOTS_LOGS/PageLayoutMode.md>).

  * Use templates to automate repetitive plot and log view layout projects and maintain consistency across presentation projects.

**Tip** : If a 2D or 3D projection is selected and [Page Layout Mode](<../PLOTS_LOGS/PageLayoutMode.md>) is _not_ active, pressing "za" on the keyboard is a useful quick key to automatically zoom the data within the target projection to fit it within the boundaries of the projection. A similar quick key combination exists in the 3D windows.

**Tip** : Use "za" to maximize the view of any selected projection.

**Tip** : Use the mouse wheel to zoom either the selected page (if no projection is selected) or the contents of a projection. The view will always zoom around the position of the cursor.

## Plot Sheets

The top of the data structure in the Plots window is inhabited by "sheets".

Each plot sheet is a container for other plot components, which can be:

  * One or more plot sections or projections.

  * Data object overlays

  * Plot items

  * Geological features

  * Log sheets

There's a hierarchy to this stuff. [The View Hierarchy](<View%20Hierarchy.md>) covers this in detail, but in summary; a sheet contains projections which can contain plot items, geological features and log sheets. The relationships between plot items determine how they react to changes. For example, if a scale bar is linked to a projection (which it must be), and the scale of the projection changes, so does the scale bar. However, a text box is a standalone item that remains the same regardless of other changes.

## Plot Sections & Projections

Sections are a plane that define a slice of 3D data. The slice orientation and position is determined by a _section definition_. In fact, the section or sections can also be viewed in the 3D window, where they don't have to be orthogonal to the screen. See [Sections and Projections](<../PLOTS_LOGS/alignviewwithsection.md>).

Projections are a view of data, and controlled by the section., which can be created from within the Plots window by inserting a new projection into an existing sheet, or by creating a new sheet with a single, default projection (such as a plan view of loaded data, for example). Projections are also created when generating plot sheets from the 3D window using the **[create-plot-view](<../command_help/create-plot-view.md>)** command. In these cases, the section required to define the projection is created automatically, but can be adjusted.

Plot sections are described as a section _definition_ , and are always viewed orthogonally to that section in the Plots window. This differs from the 3D window in which the active section can be viewed from any angle. See [The View Hierarchy](<View%20Hierarchy.md>).

There are two basic types of plot projection: 2D (also known as "static sections" or "static projections") and 3D (also "dynamic sections" or "dynamic projections"). Whilst they serve a similar purpose - to display 3D data on a plot sheet - they have different visual properties and formatting options. See [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>). 

A plot projection can contain one or more data overlays (see below) and can be associated with one or more plot items (also below). To confuse matters, a projection actually _is_ a plot item, just one with extensive data presentation options.

## Plot Overlays

When 3D data (say, from the 3D window) is represented in a plot sheet, its visual formatting is controlled by an overlay. The same data object can have one or more overlays in a projection (say, you may want to show a surface topography as a series of points and as surfaces, or you can generate multiple overlays for a block model and swap between them to show different legend colouring.

The Overlays 'parent' object of a plot also has its own properties, See [Plot Overlays Properties](<../PLOTS_LOGS/PLOTS_Overlays_properties.md>).

Depending on whether the projection is of the 2D or 3D type, different formatting options are available. 2D projections represent the legacy projection type, but provide useful ways of visualizing design data, whereas a 3D projection contains overlays that can be formatted using the same 3D properties screens as you see in the **3D** window.

## Plot Items

A plot item is any isolated data object of a plot sheet. There are lots of plot items available and each have their own properties. Plot items can either be associated with data objects, or can be standalone. They can even be external files such as Excel worksheets and other data views hosted by non-Datamine services and applications (see [Inserting External Documents into Plot Sheets](<../PLOTS_LOGS/Inserting%20OLE%20Objects.md>)).

A projection (a view of loaded 3D data) is also a plot item, as is a north arrow. 

Plot items, once selected, can provide context menu items. You can select any plot item or toggle its selection status using the <CTRL> \+ click key combination.

See **[Plot Items](<../PLOTS_LOGS/LogPlotitems.md>)** and [Plot Item Library](<../PLOTS_LOGS/plotitemlibrary.md>).

## Plots Window Menus

The Plots window features a context-menu system to allow you to perform specific operations on window items . The menu that appears depends on your current [Page Layout Mode](<../PLOTS_LOGS/PageLayoutMode.md>).

For more information on Plots window context menus, see [Plot Window Menus](<../PLOTS_LOGS/Plot%20Window%20Menus.md>).

## Scaling Plots Data 

The Plots window has a suite of scaling functions that you can use to ensure that the data is presented as you want it.

Scale is represented in the Plots window as a ratio, for example '1:1000'. To specify a scale, use the Plot View ribbon's drop-down Scale menu.

## Plot Templates

A PLot Sheet Template (often more simply called a "plot template") is a file (.dmtpl) which stores information about the layout and data used by a single sheet. It remembers the layout and formatting of all your plot items, and also remembers which data and legends were used by those plot items.

Once you have created a sheet template, you can use it to create a sheet in any project as many times as you wish, thus avoiding the hassle of re-creating new sheets from scratch.

**Note** : With regards to the Plots window (and to a lesser extent, the Logs window), much of the hierarchical structure of a particular sheet can be stored in template form. This minimizes the effort required to generate a consistent look and feel across a range of presentation projects by automatically generating a standard arrangement of sheets, projections and, if required, data object overlays.

See [Plot Sheet Templates](<../PLOTS_LOGS/PLOTS_Plot%20Templates.md>).