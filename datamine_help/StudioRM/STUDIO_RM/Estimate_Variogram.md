# ESTIMATE: Variogram Models

To access this screen:

  * Display the [ESTIMATE](<EstimateDialog.md>) wizard and click through to the **Variogram Models** screen.

Define individual variogram models for the purpose of grade estimation. A variogram model consists of a nugget variance, and up to nine individual structures.

Variogram models are defined on this screen, and selected for a particular estimation process on the [Estimation Types](<Estimate_Estimation.md>) tab (depending on the estimation method selected).

The individual models γi(h) can be spherical, power, exponential, gaussian or De Wijsian. If [kriging](<Grade%20Estimation%20Kriging.md>) is selected as an estimation method, then you must specify the variogram parameters using the Variogram Model Parameter file.

This tab consists of an indexed list of variogram models on the left side, and a series of sub-tabs on the right side. Variograms can be added, edited and deleted.

The procedure for defining a search volume is described below.

  1. Define a new variogram with the Add button. 

  2. Default values are set in all the tabs, and can be edited.

  3. To edit an existing variogram, click the variogram number / description in the Index area. The variogram number is always an integer, and will be set equal to the maximum existing variogram number plus 1. If there are no existing variograms, then the first volume will be '1'.

This right-hand side of the dialog comprises three tabs containing collections of fields relating to a particular aspect of variogram definition:

  * Rotation: define the orientation of the range ellipsoid. 

  * Structures: define the structures found within the variogram model. 

  * Summary: shows a summary of the Variogram Model Parameters file. 

### Index List

The **Variogram Model** list contains the following controls:

Variogram Model list Select existing variogram model definitions from the list. Selection of an item updates the relevant fields on the tabs on the right-hand side. The right-click menu provides the following options.

  * Add Add a new variogram model at the bottom of the list. The default variogram model description for variogram model number "N" is Variogram Model N. It is recommended that you edit the description to make it meaningful for your data. You can do this by highlighting the variogram model and selecting Edit Description from the right-click menu. 

  * Copy Copy the variogram model parameters into the buffer, so they can be pasted.

  * Cut Copy the variogram model parameters into the buffer, so they can be pasted, and delete the selected model.

  * Paste Replace the parameters of the selected model with the values in the Copy/Cut buffer.

  * Delete Delete the selected variogram model.

  * Edit Description Edit the description of the selected variogram model.

  * Reset all Variogram Models Erase all variogram models.

  * Up Move the selected variogram model up one place.

  * Down Move the selected variogram model down one place.

  * Sort by Reference Number Reorder the current list. Note that the field used to define the reference number is contained in brackets after the menu item.

  * Annotate All Using DescriptionOnly the description will be displayed, not the number. Note that the field used to define the description is contained in brackets after the menu item.

  * Copy Search Parameters Copy the rotation parameters (angles and axes) from a search volume defined in the Search Volumes tab to the selected variogram model. Also the ranges of the variogram model will be set equal to the lengths of the axes of search volume.

Add Create a new search volume with default values, and add it to the end of the current list. This is also available from the right-click menu (see above).

Delete Delete the currently selected search volume item from memory. This is also available from the right-click menu (see above).

Reset Erase all search volumes, after confirmation. This is also available from the right-click menu (see above).

Import Import variogram models from an existing Variogram Model Parameter file. All variogram models from the file will be imported. The imported variogram models will retain their numbers unless they clash with an existing number. In that case the model being imported will be renumbered as the maximum existing variogram model number plus 1. Note that variogram model numbers are integers.

Export Save the current set of variogram models in a Variogram Model Parameter file. All variogram models will be exported.

### Rotation Tab

The Rotation tab is used to define the orientation of the range ellipsoid.

  * The variogram ellipsoid is used to define any parameter which is not isotropic, the most common example being the range of the spherical model. The variogram ellipsoid is defined using fields **First** , **Second** and Third, in an identical manner to the search ellipsoid, described in the [Search Volume](<Estimate_Search.md>) section.

  * The default values specify no rotation. Therefore; if the variogram ellipsoid is to have the same orientation as the search ellipsoid, then the fields First, Second and Third must be the same as fields **First** , **Second** and Third on the Search Volumes tab.

  * Both rotation and axis can be specified for any axis (although all fields are optional, default values will be used if nothing else is specified).

  * You can specify the rotational axes manually by clearing the Use Axis Defaults check box and selecting the **First** , **Second** and Third axis from the drop-down list.

### Structures Tab:

Define the structures relevant to the current variogram model.

  * Nugget Value Enter the Nugget Variance in this field.

  * Spherical/Non-spherical/All models Control the description of the parameters in the structures table below. If all structures are spherical, then the Spherical models radio button should be selected, and the descriptions will refer to Ranges and Variance.

If none of the structures is spherical, then select Non-spherical models or All models and the descriptions of the parameters will be more generic.

If a model has a mixture of spherical and non-spherical structures, and the Spherical models field is selected, then only spherical structures will be displayed. If a model has a mixture of spherical and non-spherical structures, and the Non-spherical models button is selected, then only non-spherical structures will be displayed.

  * New/Edit/Delete To add a new structure to a model click New. To edit an existing structure, highlight the required structure and click Edit. To delete an existing structure, highlight the required structure and click Delete. The contents of the screen will vary depending on the type of structure being created or edited. If either Edit or New is selected, the Edit Structure screen is shown.  
  
The contents of the Edit Structure screen depend on the current selection of the Model Type drop-down list. The following table shows you the settings that can be made for each type:

Model Type |  Option 1 |  Option 2 |  Option 3 |  Option 4  
---|---|---|---|---  
Spherical |  Range in X |  Range in Y |  Range in Z |  Spatial Variance  
Power |  X Direction Power |  Y Direction Power |  Z Direction Power |  Slope  
Exponential |  1/3 Range in X |  1/3 Range in Y |  1/3 Range in Z |  Spatial Variance  
Gaussian |  Distance in X |  Distance in Y |  Distance in Z |  Spatial Variance  
De Wijsian |  Parameter C in X |  Parameter C in X |  Parameter C in X |  Not Used  

For more information on variogram structures, see [Grade Estimation Variograms](<Grade%20Estimation%20Variograms.md>).

### Summary Tab

View the contents of the current Variogram Model Parameter file. The Summary tab can also be used to edit the values of the fields contained within the Variogram Model Parameter file; highlight a value and edit it.

You can also:

  * Restore Restore the settings added prior to the last Run of the screen. This will restore all settings on all screens.

  * Clear Reset all fields on all screens to their default values.

  * Previous/Next Move backwards or forwards one screen in the order of Estimate screens

  * Run Run the current grade estimation.

  * Cancel Cancel the ESTIMATE process without running an estimation.

  

Related topics and activities

  * [ESTIMATE Wizard](<EstimateDialog.md>)