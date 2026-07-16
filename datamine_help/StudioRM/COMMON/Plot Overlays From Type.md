# Plots from 3D Data

To access this screen:

  * **3D View** ribbon **> > Save To >> Plot View**.

  * **Report** ribbon **> > Present >> Plot View**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "create-plot-view".

  * Use the quick key combination "cpv".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **create-plot-view** and click **Run**.

One useful way to add reference data to a plot is to generate a section based on the contents of the active 3D window. The **Create Plot View** command does just that.

Once generated, your plot is displayed in the Plot window as a tab along the bottom of the screen with the default name "From 3D" (this can be changed by right-clicking the sheet tab and selecting Rename).

There are two types of plot projection that can be created. Select from either:

  * 2D OverlaysPlot projections generated as 2D overlays are the legacy method but can still be useful for generating CAD-style reports. These projections are supported by legacy plot management controls.

  * 3D Overlays: a 3D plot projection emulates the 3D view more closely and uses the same overlay formatting functions and view controls. Formatting settings, where possible, are preserved between the 3D and Plots 3D sheet views, including 3D object formatting properties, view direction and clipping.

Click OK to generate a plot sheet and plot projection. The initial view in the generated plot sheet will be as seen in the 3D window.

Regardless of the type of overlays you have chosen to create, an attempt will be made to retain 3D window overlay formatting wherever possible, and also view information such as direction and clipping. See [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>).  

Activity steps:

  1. Display data in any 3D view. This is how data should appear in the plot sheet so set an appropriate view orientation.

  2. Run the command.

  3. On the Copy From screen, **Select the view to copy from**. All 3D windows are listed.

  4. Select the type of overlays to create. See [Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>).

  5. Click **OK**.

A new plot sheet is created and the Plots window displays.

The new sheet contains a single (full-page) projection representing the current view of the 3D window. 

Related topics and activities

  * [Sections and Projections](<../PLOTS_LOGS/alignviewwithsection.md>)

  * [Plot Overlays](<../PLOTS_LOGS/Plots-overlays.md>)

  * [Plot Overlays Properties](<../PLOTS_LOGS/PLOTS_Overlays_properties.md>)

  * [create-plot-view ("cpv")](<../command_help/create-plot-view.md>) (command)

  * [Plot Projection Overlay Types](<../PLOTS_LOGS/Projection%20Overlay%20Types.md>)

  * [3D Overlay Groups](<../PLOTS_LOGS/3D%20Overlay%20Concept.md>)

  * [The Plots Window](<Window_PLOTS_Overview.md>)

  * [The View Hierarchy](<View%20Hierarchy.md>)