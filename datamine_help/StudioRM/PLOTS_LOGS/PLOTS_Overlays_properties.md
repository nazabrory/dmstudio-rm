# Plot Overlays Properties

To access these properties:

  * In the **Sheets** or **Project Data** control bar, right-click a projection's **Overlays** folder and choose **Overlays Properties**.

  * Display the **[Properties](<../COMMON/properties%20control%20bar%20overview.md>)** control bar and, in the **Sheets** or **Project Data** control bar, click a projection's **Overlays** folder and choose **Overlays Properties**.

General properties for managing overlays in plot sheet projections can be found here.

Automatically add new 3D object overlays: choose what happens when new object data is created (as a result of loading or importing data within a project session. You can select:

  * None: leave the existing overlays plot item as it is, without adding the new object data default overlay(s). You can load them later if you want to.

  * 2D overlays: automatically add overlays of the legacy 2D type to the projection, once the data is loaded, providing the overlay group isn't locked (see below). See [Projection Overlay Types](<Projection%20Overlay%20Types.md>).

  * 3D overlays: add 3D overlays to a _3D Overlay Group_ and display them in the projection once data is loaded, providing the overlay group isn't locked (see below). See [3D Overlay Groups](<3D%20Overlay%20Concept.md>).

Remove empty overlays: 

  * If _Yes_ , overlays that don't contain 3D data (say, data has been unloaded) are automatically removed from the projection, providing the overlay group isn't locked (see below). 

  * If _No_ , empty overlays remain listed.

Share: 

  * Make the current overlay collection available to other projections within the current plot sheet (Within sheet).

  * Make overlays available to other sheets of the same project (Within document).

  * Ensure overlays are only available to their parent projection, meaning they can be duplicated within the projection, but nowhere else (Not shared).

**Note** : If overlays are locked (that is, the Lock Overlays context menu option for a projection is enabled, so that a padlock appears against the overlays icon), then no overlay is created if new data is loaded, regardless of the settings made above.

Related topics and activities

  * [Plot Overlays](<Plots-overlays.md>)

  * [Plots from 3D Data](<../COMMON/Plot%20Overlays%20From%20Type.md>)

  * [3D Overlay Groups](<3D%20Overlay%20Concept.md>)

  * [Projection Grid Options](<../COMMON/format%20grid%20dialog.md>)

  * [Projection Overlay Types](<Projection%20Overlay%20Types.md>)

  * [Properties Control Bar](<../COMMON/properties%20control%20bar%20overview.md>)