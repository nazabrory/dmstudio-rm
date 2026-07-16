# ESTIMATE: Estimation

To access this screen:

  * Display the **ESTIMATE** screen and click through to the **Estimation** tab.

Define the method by which a grade estimation will be performed. This information will be stored in the [Grade Estimation Parameter File](<Grade%20Estimation%20Parameter%20File.md>).

It is possible to select different grades to estimate, using different methods and different parameters all in a single run of Estimate. The different combinations of grades, methods and parameters are controlled by adding estimation items to the Index list on the left, as required, and then editing the default values for each item.

This right-hand side of the dialog comprises the following sub-tabs containing collections of fields relating to a particular aspect of search volume definition.

  * Attributes Set up the general parameters for each estimation. 

  * Options Select the anisotropy method to be used during estimation. 

  * Indicator Estimation Select the mean grade method, output files, order relation correction and cutoff parameters if indicator estimation is to be performed. 

  * Summary Shows a summary of the Estimation Parameters file. 

### Index List

The **Estimation Types** list contains the following controls:

Estimation Types list Select existing estimations to edit or delete. Selection of an item updates the relevant fields on the tabs on the right hand side. The right-click menu gives a range of options:

  * Add Add a new estimation at the bottom of the list. The default estimation description for estimation number n is Estima Param N. It is recommended that you edit the description to make it meaningful for your data. You can do this by highlighting the estimation and selecting Edit Description from the right-click menu

  * Copy Copy the estimation parameters into the buffer, so they can be pasted.

  * Cut Copy the estimation parameters into the buffer, so they can be pasted, and delete the selected estimation.

  * Paste Replace the parameters of the selected estimation with the values in the Copy/Cut buffer.

  * Delete Delete the selected estimation.

  * Edit Description Edit the description of the selected estimation.

  * Reset all Estimation Parameters Erase all estimations, after confirmation.

  * Up Move the selected estimation up one place.

  * Down Move the selected estimation down one place.

  * Sort by Reference Number Reorder the current list. Note that the field used to define the reference number is contained in brackets after the menu item.

  * Annotate All Using Description Only the description will be displayed, not the number. Note that the field used to define the description is contained in brackets after the menu item.

Add Create a new search volume with default values, and add it to the end of the current list. This option is also available from the right-click menu.

Delete Delete the currently selected search volume item from memory. This option is also available from the right-click menu.

Reset Erase all search volumes, after confirmation. This option is also available from the right-click menu.

Import Import estimation parameters from an existing Estimation Parameter file. All sets of estimation parameters from the file will be imported. The imported estimations will retain their numbers unless they clash with an existing number. In that case the estimation being imported will be renumbered as the maximum existing estimation number plus 1. Note that estimation numbers are integers.

Export Save the current set of estimation parameters in an Estimation Parameter file. All parameters will be exported.

### Attributes Tab

The Attributes sub-tab is used to define the general parameters for the selected estimation:

Estimation Method (Nearest Neighbour, Inverse Power....) Select a radio button to define the general estimation method. The available estimation types are:

  * [Nearest Neighbour](<Grade%20Estimation%20Nearest%20Neighbour.md>): select this option to perform a Nearest Neighbour grade estimation.

  * [Inverse Power of Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>): select this option to perform an IPD grade estimation. The [Dynamic Anisotropy](<Dynamic%20Anisotropy%20-%20Introduction.md>) option requires angle fields to be interpolated into the block model. This is selected using the [Angle Data](<Dynamic%20Anisotropy%20-%20Interpolating%20Angles.md>) check box.

  * [Ordinary Kriging](<Grade%20Estimation%20Kriging.md>): select this option to perform an Ordinary Kriging grade estimation. You have the additional option of selecting log kriging.

  * [Simple Kriging](<Grade%20Estimation%20Kriging.md>): select this option to perform an Simple Kriging grade estimation. You have the additional option of selecting log kriging.

  * [Sichel's T Estimator](<Grade%20Estimation%20Sichels%20T%20Estimator.md>): select this option to use Sichel's T Estimator method.

  * [F-value](<Grade%20Estimation%20F%20Value.md>): use the average value of the variogram in the cell.

  * [Lagrange multiplier](<Grade%20Estimation%20Lagrange%20Multiplier.md>): use the Lagrange multiplier calculated when solving the Ordinary Kriging matrix.

(Select a link above for more information on each method, or for general information about the available methods, see [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)).

Indicator Estimation If Indicator Estimation (IE) is selected, then it applies to all estimates.

  * You cannot mix IE with any non-indicator methods

  * For IE, you must define an estimate in the Index panel for each cutoff. 

  * If zone control is being performed, you must define an estimate for each cutoff and each zone value. The cutoffs may vary between zones. 

All the indicator parameters are defined on the Indicator Estimation tab, which is greyed-out unless Indicator Estimation is selected here. Selecting this option ensures that the INDEST process will be accessed during estimation.

Data Fields Select the sample and model grade field files (or select the Same as Sample check box to define one file name for both purposes). For more information on Data Fields, see [VALUE_IN and VALUE_OU](<Grade%20Estimation%20Methods.md#VALUE_IN>).

Model Fields Define the secondary fields required (Number of Samples, Variance, Transformed Distance, Search Volume). For more information on secondary fields, see [Grade Estimation Secondary Fields](<Grade%20Estimation%20Methods.md#Secondary>).

Search and Variogram Definition Each list in this section contains all currently defined search volumes and variogram model definitions (defined on the respective tab of the Estimate screen). Depending on your selection of estimation method (see above), you may not have access to the Variogram Model list. For more information on these parameters, see [Grade Estimation Parameter File](<Grade%20Estimation%20Parameter%20File.md>).

Zone Field Values If one or two zone control fields have been specified on the [Files](<Estimate_Files.md>) tab, a different set of estimation parameters can be assigned to each zone value (one zone control field), or combination of zone values (two zone control fields). For more information on zonal control, see [Grade Estimation Zonal Control](<Grade%20Estimation%20Methods.md#Zonal>).

### Options Tab

Define additional parameters for the selected estimation. The fields shown will depend on the Estimation Method selected on the Attributes tab (see above), however, the list below represents an exhaustive tally of all possible fields for all methods, with an indication of the methods each field is associated with.

  * Anisotropy method Select either Search Ellipse, Isotropic or User Defined options. For more information on anisotropy methods, see [Grade Estimation Nearest Neighbour](<Grade%20Estimation%20Nearest%20Neighbour.md>).

**Note** : This is available for _Nearest Neighbour_ or _Inverse Power of Distance_ methods only.

  * Distance Weighting Select distance weighting options (for more information on these fields, see [Grade Estimation Inverse Power of Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>):

Note: These options are only available for the _Inverse Power of Distance_ method.

    * Include offset distance Select this check box to specify a Distance (see below).
    * Distance If a sample lies exactly on a discretised point, then it will be at zero distance from that point and will get 100% of the weight. This can lead to a biased estimate, particularly if there is only one discretised point and there are other samples lying within the cell. However, this can be avoided by specifying a positive value for the field Distance.

    * Power Select a value to define the power of distance for IPD weighting.

  * Weighting Fields Define the length and density weighting fields using the supplied drop-down lists. For more information, refer to [IPD Length and Density Weighting](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md#Length>).

Note: Only available for the _Inverse Power of Distance_ method.

  * Negative Kriging Weights Select the Reset Negative Weights to zero with this option. For more information on handling negative weights, see [Grade Estimation Negative Kriging Weights](<Grade%20Estimation%20Kriging.md#Negative>).

Note: Only available for the _Ordinary Kriging_ (with or without log option), _Simple Kriging_ (with or without log option) methods.

  * Local Mean Value For Simple Kriging, you can elect to either calculate the local mean value as the arithmetic mean of all samples lying in the search volume (Calculate Mean), or provide a field description from which it can be derived from the model (Use Model Field, and select a Local Mean Field).

Note: Only available for the _Simple Kriging_ method.

  * Log Kriging Settings Select your log kriging option from either Rendu's Approximation or General Case. For more information on log kriging, refer to [Grade Estimation Lognormal Kriging](<Grade%20Estimation%20Kriging.md#Lognormal>).

Note: Only available for the _Ordinary Kriging_ (with log option) and _Simple Kriging_ (with log option) methods.

  * Additive Constant Specify an additive constant for _Sichel's T Estimator_ method. This will be added to the Grade Estimation Parameter file as the **ADDCON** field. You should be aware, however, that this field is also used by the IPD method, but in a different context.

### Indicator Estimation Tab

Note: The Indicator Estimation tab is disabled unless Indicator Estimation was selected on the Attributes tab (see above).

  * Mean Grade Method The calculation of the grade above each cutoff requires that the average grade between each successive pair of cutoffs be specified. The following options are available:

    * Average of lower and upper cutoffs Average of minimum and maximum cutoff values. The grade above the highest cutoff is calculated as the highest cutoff plus half the difference between the highest and second highest cutoffs.
    * Average from sample file for all cutoff intervals Select this option to ensure that the mean grade is calculated by the **INDEST** process from the grades of the samples in the IN file, for all cutoff intervals.

    * Average from sample file; median value for samples above top cutoff Select this option to use a median average above the top cutoff value.

    * Manual Entry Values are specified by the user, using the BINGRADE and ABVGRADE fields in the ESTPARM file. The BINGRADE field contains the grade below the cutoff and the ABVGRADE field the grade above the cutoff. The ABVGRADE field is therefore only used for the top bin, and can be entered into the Manual Entry: Average grade above top cutoff field (see below).

Note: Although the option appears on the Indicator Estimation tab for every estimate, your selection applies to all estimates.

  * Output Files: two optional output files may be defined:

    * Average grade for each cutoff interval This output file contains cutoff grade ranges and average grade used for each range. It will include zone field(s), if any, plus the following fields: 

BIN  | Bin name for cutoffs.  
---|---  
LO_CUT | Lower cutoff grade.  
UP_CUT | Upper cutoff grade.  
NSAMPLES | Number of samples in the input file lying within the bin.  
BINGRADE | Bin grade used for indicator estimation. This is dependent on the **Mean Grade Method**.  
SAMPMEAN | Mean grade of samples in the input file lying within the bin  
    * Indicator values for each cutoff The output indicator file is a copy of the sample input IN file, but also includes the 0/1 indicator values for each cutoff.

  * Include "Probability Above" and "Grade Above"... Check to ensure these fields are included in the output Grade model.

  * Order Relation Correction One of the main drawbacks of the indicator estimation method is the "Order Relation" Problem. This will occur if the proportion of the sub-cell above cutoff n is estimated to be less than the proportion above cutoff `n+1`. for example, `if PRAB(n) < PRAB(n+1)`. Three options are available to correct for this:

    * Downwards
    * Upwards

    * Average of Downwards and Upwards

**Note** : The final option is recommended.

  * Cutoff Data The following options exist for defining the cutoff (indicator) grade:

    * Upper cutoff grade for current interval The cutoff (or indicator) grade must be specified for each estimation.
    * Mean grade between current and previous cutoffs You must also define the mean grade between the current and previous cutoff for each estimation. Although, this option appears for every estimate, your selection applies to all estimates.

    * Manual Entry: Average grade above top cutoff: if Manual Entry has been selected for the Mean Grade Method (see above), this option allows you to define the mean grade for the top bin manually.

### Summary Tab

The Summary tab shows a tabular view of the data columns and values found within the current Estimation Parameter File. For more details on these fields, see [Grade Estimation Parameter File](<Grade%20Estimation%20Parameter%20File.md>).

You can also:

  * Restore Restore the settings added prior to the last Run of the screen. This will restore all settings on all screens.

  * Clear Reset all fields on all screens to their default values.

  * Previous/Next Move backwards or forwards one screen in the order of Estimate screens

  * Run Run the current grade estimation.

  * Cancel Cancel the ESTIMATE process without running an estimation.

Related topics and activities

  * [ESTIMATE: Unfolding](<Estimate_Unfolding.md>)

  * [ESTIMATE: Search Volumes](<Estimate_Search.md>)

  * [ESTIMATE: Variogram Models](<Estimate_Variogram.md>)

  * [ESTIMATE: Files](<Estimate_Files.md>)

  * [ESTIMATE: Controls](<estimate_controls.md>)

  * [ESTIMATE: Preview](<Estimate_Preview.md>)

  * [Introduction to Grade Estimation and Interpolation](<Advanced%20Estimation%20Validation.md>)

  * [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)

  * [Grade Estimation Key Fields](<Grade%20Estimation%20Key%20Fields.md>)

  * [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)

  * [Grade Estimation Output and Results](<Grade%20Estimation%20Output%20and%20Results.md>)