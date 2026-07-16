# ESTIMATE: Search Volumes

To access this screen:

  * Display the [ESTIMATE](<EstimateDialog.md>) wizard and click through to the **Search Volumes** screen.

Define the search volume parameters to be used during grade estimation. Search volumes are defined on this screen, and selected for a particular estimation process on the [Estimation Types](<Estimate_Estimation.md>) tab.

One or more search volumes are defined using the Search Volume Parameter file. Each record in the file defines a separate search volume, and each search volume has a unique Search Volume Reference Number. This means that a search volume may be unique to an individual grade, or can be shared by two or more grades.

For more general information on Search Volumes, see [Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>), and [Grade Estimation Search Volume Parameter Files](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>).

The left side of this tab contains an indexed list of available search volumes. Volumes can be added, edited and deleted. The procedure for defining a search volume is described below.

  1. Define a new search volume with the Add button.

  2. Default values are set in all tabs, and can be edited.

  3. To edit an existing search volume click the search volume number / description in the Index area. The search volume number is always an integer, and will be equal to the maximum existing search volume number, plus 1. If there are no existing search volumes, then the first volume will be '1'.

This right-hand side of the dialog comprises four sub-tabs, containing collections of fields relating to a particular aspect of search volume definition:

  * Shape: used to define the geometry, axes and rotation of the search volume ellipsoid. 

  * Category: up to three search volumes can be defined; this tab is used to specify the parameters for primary, dynamic and tertiary volumes. 

  * Decluster: this tab is used to define the use of octants and key fields. 

  * Summary: shows a summary of the Search Volume Parameters file. 

### Index List

The search volume list contains the following controls:

Search Volume List Select existing search volume definitions in the list. Selection of an item updates the relevant fields on the tabs on the right-hand side (Shape, Category etc.). The right-click menu provides the following options:

  * Add Add a new search volume at the bottom of the list. The default search volume description for search volume number "N" is Search Volume N. It is recommended that you edit the description to make it meaningful for your data. You can do this by highlighting the search volume and selecting Edit Description from the right-click menu.

  * Copy Copy the search volume parameters into the buffer, so they can be pasted.

  * Cut Copy the search volume parameters into the buffer, so they can be pasted, and delete the selected volume.

  * Paste Replace the parameters of the selected volume with the values in the Copy/Cut buffer.

  * Delete Delete the selected search volume.

  * Edit Description Edit the description of the selected search volume.

  * Reset all Search Volumes Erase all search volumes, after confirmation.

  * Up Move the selected search volume up one place.

  * Down Move the selected search volume down one place.

  * Sort by Reference Number Reorder the current list. Note that the field used to define the reference number is contained in brackets after the menu item.

  * Annotate All Using Description Only the description will be displayed, not the number. Note that the field used to define the description is contained in brackets after the menu item.

  * Copy Variogram Parameters Copy the rotation parameters (angles and axes) from a variogram model defined in the Variogram Models tab to the selected search volume. Also the lengths of the axes of the search volume will be set equal to the ranges of the highest-numbered structure of the variogram model.

Add Add a new estimation parameter item. This is also available from the right-click menu (see above). This is also available from the right-click menu (see above).

Delete Delete an estimation parameter item. This is also available from the right-click menu (see above). This is also available from the right-click menu (see above).

Reset Erase all estimations, after confirmation. This is also available from the right-click menu (see above). This is also available from the right-click menu (see above).

Import Import search volumes from an existing [Search Volume Parameter](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>) file. All search volumes from the file will be imported. The imported search volumes will retain their numbers unless they clash with an existing number. In that case the volume being imported will be renumbered as the maximum existing search volume number plus 1. Note that search volume numbers are integers.

Export Save the current set of search volumes in a [Search Volume Parameter](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>) file. All search volumes will be exported.

### Shape Tab

The following fields are available on this tab:

  * Ellipsoidal/Rectangular Define the basic shape of your search volume here. For more information on search volume geometry, see [Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>).

  * X, Y, Z Axis Define the extent of each 3D axis here. The lengths of the axes of the ellipsoid are defined using fields SDIST1, SDIST2 and SDIST3. Initially SDIST1 is along the X-axis, SDIST2 along the Y-axis and SDIST3 along the Z-axis. For more information, refer to [Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>).

  * Shape Rotation One, two or three rotations may then be defined. For each rotation, it is necessary to define both the rotation angle, the axis about which the rotation is applied, and optionally a field representing dynamic angle information in the case of a dynamic anisotropy study.

The rotation angle is measured in a clockwise direction when viewed along the positive axis towards the origin. A negative rotation angle means an anti-clockwise rotation. For more information on rotation angles of search volumes, see [Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>).

If the [Dynamic Anisotropy](<Dynamic%20Anisotropy%20-%20Introduction.md>) option is required, then one or more of the [Dynamic Angle](<Dynamic%20Anisotropy%20-%20Estimating%20Grade.md#search>) fields must be selected from the picklist which include fields from the input prototype model file.

### Category Tab

For each search volume, a minimum and maximum number of samples can be defined. If there are more than the maximum number of samples within a search volume, then the nearest maximum number of samples is selected. "Nearest" is defined in terms of a transformed distance, depending on the search volume.

The search ellipse is shrunk concentrically, until only the maximum number of samples lie within it.

The following groups of fields are available on this tab, and are used to define the parameters required for dynamic search volumes.

  * Primary Search Volume Specify the Minimum and Maximum number of samples for the first dynamic search volume.

  * Second Search Volume

  * Third Search Volume

For more information on dynamic search volumes, see [Grade Estimation Dynamic Search Volumes](<Grade%20Estimation%20Dynamic%20Search%20Volumes.md>)

### Decluster Tab

Generally, samples are not evenly distributed around the cell being estimated, but are clustered together. Using the "search volume shrinking method" described previously, this may lead to samples in one area having an undue influence on the grade of the cell. This problem is avoided by dividing the search volume into octants, and ensuring that a minimum number of octants have samples in them.

The Decluster tab contains the following fields, used to define octants, and associated key fields.

  * Octants Check Use Octants define octant details:

    * Minimum number to be filled: the minimum number of octants to be filled before a cell will be estimated.

    * Minimum number of samples in an octant: the minimum number of samples in an octant before it is considered to be filled.

    * Maximum number of samples in an octant: the maximum number of samples in an octant, to be used for estimation. If there are more than the maximum number of samples in an octant, the samples nearest to the cell centre are selected, using the transformed distance of the shrinking ellipsoid method.

For more information on using the octant method, see [Grade Estimation Octants](<Grade%20Estimation%20Octants.md>).

  * Sample Key Field: if each record in the sample data file is identified by a key field, then the number of samples per key field value can be restricted. The most obvious use of this feature is to prevent samples from a single hole having an overpowering influence on the estimated grade of a cell.

    * Key Field: displays the key field to be used (default: BHID).
    * Maximum number of samples: define the maximum number of samples with the same key field value.

### Summary Tab

This tab displays the current values held within the parameters file for the currently-active volume. For more information, see [Grade Estimation Search Volume Parameter File](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>). 

You can also:

  * Restore Restore the settings added prior to the last Run of the screen. This will restore all settings on all screens.

  * Clear Reset all fields on all screens to their default values.

  * Previous/Next Move backwards or forwards one screen in the order of Estimate screens

  * Run Run the current grade estimation.

  * Cancel Cancel the ESTIMATE process without running an estimation.

Related topics and activities

  * [Estimate Dialog - Files](<Estimate_Files.md>)

  * [Estimate Dialog - Unfolding](<Estimate_Unfolding.md>)

  * [Estimate Dialog - Variogram Models](<Estimate_Variogram.md>)

  * [Estimate Dialog - Estimation Types](<Estimate_Estimation.md>)

  * [Estimate Dialog - Controls](<estimate_controls.md>)

  * [Estimate Dialog - Preview](<Estimate_Preview.md>)

  * [Grade Estimation Introduction](<Grade%20Estimate%20Overview.md>)

  * [Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>)

  * [Grade Estimation Search Volume Parameter File](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>)

  * [Grade Estimation Octants](<Grade%20Estimation%20Octants.md>)