# Define Custom Zones

To access this screen:

  * Using the [Advanced Estimation](<Multivariate_Introduction.md>) wizard, select Define Custom Zones from the left-hand menu system. 

Note: This panel requires that at least one zone has been [defined](<Multivariate_Select_Samples.md>) for your estimation scenario.

This panel is used to define custom zones for soft boundary analysis. Zone combinations selected in the Select zones table are generated based on the unique attribute value (or combinations of values) found in the selected Zone 1 and Zone 2 fields on the [Select Samples](<Multivariate_Select_Samples.md>) screen.

If the geostatistical characteristics of two or more zones are similar it may be beneficial for estimation to include samples from other zones. This is particularly useful if some zones have few samples. Defining soft boundaries allows the estimation in a model zone to use samples from more than one sample zone. For example, samples in zones 2, 4 and 6 are used for estimating model cells in model zone 2; samples in zones 4 and 6 for cells in zone 4, and samples in zones 2 and 6 for cells in zone 6. In this situation the zone boundaries are defined as Soft boundaries.

Soft boundaries are modelled by defining custom sample zones comprising two or more sample zone values. The custom zone is then selected when defining the samples to use to estimate a model zone.

You can select any of the sample zones listed on the left and combine them into a single Custom zone. This can then be assigned to a particular Model Zone using the [Define Estimations](<Multivariate_Define_Estimations.md>) screen, as part of setting up soft boundary estimation.

For example, if both Zone 1 and Zone 2 attributes were chosen, where Zone 1 contains values 1, 2 and 3 and Zone 2 contains values A and B, the following combinations are generated:

  * `1/A, 2/A, 3/A, 1/B, 2/B, 3/B`

You can then assign any of these combinations to a custom zone. For example, `1/A` and `2/B`.

If only one zone field is specified on the Select Samples panel, the unique values of that zone (including absent, if absent zone values exist) are listed.

Once a custom zone has been defined, the [Bivariate Statistics](<Bivariate_Statistics.md>) screen can be used to generate zone statistics.

### Hard and Soft Boundary Estimation

In many estimation studies there will be a 1:1 match between the zone in which the model cell is located and the zone in which the samples are located. Only samples in zone N are used to estimate model cells in zone N. These zone boundaries are defined as Hard boundaries. 

If the geostatistical characteristics of two or more zones are similar it may be beneficial for estimation to include samples from other zones. This is particularly useful if some zones have few samples. Defining soft boundaries allows the estimation to use samples from more than one zone. For example, samples in zones 2, 4 and 6 are used for estimating model cells in zone 2; samples in zones 4 and 6 for cells in zone 4, and samples in zones 2 and 6 for cells in zone 6. In this situation the zone boundaries are defined as Soft boundaries.

Soft boundaries are modelled by defining Custom zones of two or more sample zones. Each custom zone is then assigned to a model zone when the estimations are defined using the [Define Estimations](<Multivariate_Define_Estimations.md>) screen.

### Zone Information in Output Files

If hard or soft boundaries are defined and you choose to output a **SAMPOUT** file (containing information about which samples contribute to a block estimation), the following fields in that file can help you understand more about how zonal control has been applied to the estimation. The following fields are included in the **SAMPOUT** file for this purpose:

I_{Zone} |  The {Zone} from which the sample originates (the input zone).  
---|---  
O_{Zone} |  The {Zone} that the sample affects (the output zone).  
O_IJK |  the IJK value of the block model.  
  
Similarly, the output model will contain a **COUNTFLD** field, the value of which will be defined by the Zone Parameter (**ZPAR**) file. There will be one column for each zone combination configured in the model and, if set up using the **Advanced Estimation** wizard, will be set in the format `{Zone1}/{Zone2}_N`. 

To define or edit custom zones for estimation:

  1. Display the **Advanced Estimation** wizard.

  2. First, select one or more of the sample zones listed on the left (**Select zones**). These are the zones that will be considered when assessing sample values as part of estimation.

  3. Click Add Zoneto create a **Custom zone** representing the currently selected zones on the left. The **Custom zone** name is a concatenated string of all selected zones.

**Tip** : You can call a **Custom zone** anything you want by selecting it and clicking **Rename**.

  4. Select a custom zone to update the list on the left to show which sample zones make up that custom zone (highlighted by a selected check box). You can change custom zone assignments by editing the check boxes on the left and clicking **Update**.

  5. If there is a Custom zone you no longer need, you can **Delete** it. 

If this custom zone is already assigned to a model zone on the [Define Estimation](<Multivariate_Define_Estimations.md>) screen(**Soft Boundary Setup**), that assignment will be automatically removed and, for that model zone, a hard boundary estimation will be performed instead.

**Note** : You can remove all custom zones using **Clear list**. This cannot be undone.

  6. The **Custom Zone Sample Summary** table at the bottom of the panel displays statistics of all defined custom zones.

  7. To assess custom zones further, you can generate statistics for them using the [Bivariate Statistics](<Bivariate_Statistics.md>) screen, where they are listed alongside standard zones (or zone combinations).

**Note** : Advanced Estimation is part of the Studio RM toolset. Additional licensing modules aren't required.

### Custom Zone Sample Summary

The summary table displays the following columns:

  * Custom Zone Sample Summary This command group contains a table showing, for each distinct zone.

  * Zone Custom zone identifier(s) for each combination of zone values. If two zone fields have been selected then the zone values will be separated by the / symbol. The bottom row will be shown as zone All, giving statistics over all zones or in the case where no zones have been selected.

  * Samples The total number of samples for the specified zone(s).

  * 2D Will state "Yes" if , for each zone, the z-span of all the coordinates in the zone is close to zero. It will show "No" if this isn't the case, and the data will be treated as 3D.

  * No of Holes If a Hole ID field has been selected above, this column contains the number of holes for which zone values have been detected.

  * Range dist The span of the data hull enclosing all samples. This distance is normally greater than the maximum distance between any samples (unless the hull has a sample exactly at the opposing corners).

  * Mean length: The average sample length, calculated as TO - FROM

  * **Absent lengths:** The number of samples with an absent data FROM or TO value.

  * Calculate distance statistics Statistics are normally calculated when a new Samples file is specified, but you can use this button to calculate the following additional statistics for the samples file:

    * Max dist The maximum distance between samples, per zone (if one or more zones is specified).

    * Mean dist The average distance between samples, optionally per-zone.

    * Min dist The closest distance between sample pairs, optionally per-zone.

Related topics and activities

  * [Advanced Estimation Introduction](<Multivariate_Introduction.md>)
  * [Scenario Setup](<Multivariate_Scenario_Setup.md>)

  * [Select Samples](<Multivariate_Select_Samples.md>)

  * [Unfolding](<Multivariate_Unfold.md>)

  * [Bivariate Statistics](<Bivariate_Statistics.md>)

  * [Investigate Anisotropy](<Multivariate_Investigate_Anisotropy.md>)

  * [Create Variograms](<Multivariate_Create_Variograms.md>)

  * [Fit Models](<Multivariate_Fit_Models.md>)

  * [KNA: Select Locations](<Multivariate_KNA_SelectLocations.md>)

  * [KNA: Optimize](<Multivariate_KNA_Optimize.md>)

  * [Select Prototype](<Multivariate_Select_Prototype.md>)

  * [Parameters](<Multivariate_Import_Parameters.md>)

  * [Define an Estimation](<Multivariate_Define_Estimations.md>)

  * [Review Variograms](<Multivariate_Confirm_Variograms.md>)

  * [Define Search Volumes](<Multivariate_Select_Search_Volumes.md>)

  * [Run Estimations](<Multivariate_Run_Estimation.md>)