# Plot Overlays

Overlays are representations of 3D data. A data object can be represented by one or more overlays.

In a basic sense, data represents the form of something, whilst its overlay describes how it is displayed. You can represent the same object in different ways, and this can be useful to ensure your audience understands what they are looking at.

The relationship between views, projections and overlays is covered in [The View Hierarchy](<../COMMON/View%20Hierarchy.md>). It can be useful to generate projections from **[3D window data](<../COMMON/Plot%20Overlays%20From%20Type.md>)** , either as a **[2D or 3D](<Projection%20Overlay%20Types.md>)** overlay group, but you can also add overlays to an existing plot sheet projection at any time.

To add an overlay independently to an existing projection:

  1. Expand the **Sheets** or **Project Data** control bar's **Plots** folder.

  2. Expand the folder with the name of the plot sheet containing your projection.

The plot sheet displays.

  3. Expand the projection menu. This reveals an **Overlays** folder, and the target projection is selected.

  4. Right-click the **Overlays** folder and choose **Insert...**

The [Plot Item Library](<plotitemlibrary.md>) displays. This version of the PIL shows only items that have an associated data overlay.

  5. Choose the type of data to add to the projection:

     * If the data is of the faces (wireframe), blocks (block model), lines (strings) or points type:

       1. Pick an appropriate item in the PIL.

The **Add Overlay** screen displays.

       2. Choose the overlay to add. If nothing appears, there is no data of the corresponding type currently loaded (**Cancel** , load the data and try again).

     * To add an overlay to support the display of other data, choose from:

       * **Grid** An overlay showing grid intervals. Projections can display multiple grids.

       * **Hull** Display an overlay that highlights the outer border(s) of the projection.

       * Section LineIf viewing a 3D projection, it can be useful to highlight the position of the active section.

Once selected, a **Properties** screen appears to configure the new overlay item.

     * Alternatively, pick the **3D Object Overlay Wizard** item, then:

       1. Choose the overlay to add using the **Add Overlay** screen.

       2. From the PIL, choose which type of overlay you are adding (the contents of this screen depend on the data overlay you picked previously).

A 3D data overlay is added to the projection.

**Note** : You can also access the **3D Object Overlay Wizard** screen from the **Manage** ribbon (**Insert >> Overlay**).