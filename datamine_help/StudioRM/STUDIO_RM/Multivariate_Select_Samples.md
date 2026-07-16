# Select Samples

To access this screen:

  * In the [**Advanced Estimation**](<Multivariate_Dialogs_Overview.md>) wizard, click **Select Samples**.

Define the sample files and fields for estimation.

This screen is divided into two key areas:

  * Input Samplesselect the input sample file or, if you need to unfold data for estimation, an unfolding parameters file. 

By default, coordinate fields are auto-detected, but you can set them yourself if fields aren't recognized.

Once an unfolding parameters or sample file is selected, choose one or more grade fields for the estimation and zone fields if zonal control is applied (with either hard or soft boundary rules). 

See [UNFOLD in Advanced Estimation](<Unfold-advanced-estimation.md>).  

  * Sample Summary:once you have defined your fields, a summary table displays with basic statistics such as the number of samples and distances between samples.

### Sample Summary Statistics

When samples, at least one estimation variable and (optionally) zones are defined, the **Sample Summary** table shows summary statistics:

  * **Zone** If one or two zones are specified, the statistics relating to either a zone, or a zone combination are listed on separate table rows. If two zone fields have been selected then the zone values will be separated by the / symbol. The bottom row is shown as zone All, giving statistics over all zones or in the case where no zones have been selected.
  * **2D** This shows "Yes" if , for each zone, the z-span of all the coordinates in the zone is close to zero. It shows "No" if this isn't the case, and the data will be treated as 3D.
  * No of HolesIf a **Hole ID** field has been selected, this column contains the number of holes for which zone values have been detected.
  * Range distThe span of the data hull enclosing all samples. This distance is normally greater than the maximum distance between any samples (unless the hull has a sample exactly at the opposing corners).

  * Mean lengthThe average sample length.

  * **Absent lengths** The number of samples with an absent data **FROM** or **TO** value.

You can also Calculate distance statistics, which can take a few minutes to calculate for large data files (hence they aren't calculated by default):

  * Max distThe maximum distance between samples, per zone (if one or more zones is specified).

  * Mean distThe average distance between samples, optionally per-zone.

  * Min distThe closest distance between sample pairs, optionally per-zone.

### Select Samples Activities

The following activities assume the **Advanced Estimation** wizard is displayed, and that **[a scenario has been configured](<Multivariate_Scenario_Setup.md>)** , and is active.

To specify input sample data for an estimation study (no unfolding):

  1. Browse for a **Samples file**. This will be a desurveyed drillholes or sample points file in either .dm or .dmx format.

The grade/variable list below populates with the file's numeric fields, and if possible, the coordinate fields are selected below. A **Hole ID** field and **FROM** and **TO** fields are also automatically picked if they are recognized.

  2. Review the **Select grade/variables fields** list and check any grade or variable that will contribute to the estimation. 
  3. Check that the **X** , **Y** and **Z** fields represent the coordinates of the samples. If not, select them.
  4. If you plan to estimate using zonal control (possibly with soft boundary support), select **Zone 1** and (for multi-zone combinations) Zone 2.
  5. Review and confirm the **Hole ID** , **From** and **To** fields. These denote independent holes and interval break points, so make sure they are set to the right fields.
  6. Review the **Sample Summary** statistics. 
  7. Optionally, **Calculate distance statistics**.

To specify input sample data for an estimation study (with unfolding):

  1. Check **Use Unfolding**.
  2. Browse for a **Unfolding parameters file**. This is typically output from the **[UNFOLD](<../Process_Help_XML/unfold.md>)** process but can also be exported from a previous session of the AE wizard. See [UNFOLD in Advanced Estimation](<Unfold-advanced-estimation.md>).

The samples file, if it can be derived from the unfolding parameters file, is automatically set.

The grade/variable list below populates with the file's numeric fields, and if possible, the unfolded coordinate fields are selected below. A **Hole ID** field and **FROM** and **TO** fields are also automatically picked if they are recognized.

  3. If you intend to adjust unfolding parameters, unfold data and save a parameters file, check **Show Unfolding Parameters**.

     1. Activate the **Unfolding** screen. 

     2. Adjust or set unfolding parameters. See [Unfolding](<Multivariate_Unfold.md>).

     3. Click **Run and Display**.

     4. Activate the **Parameters** screen and check **Export**.

     5. Browse for a location and specify a name for your **Unfolding parameters** file.

     6. Return to the **Select Samples** screen and select the updated file.

  4. Review the **Select grade/variables fields** list and check any grade or variable that will contribute to the estimation. 
  5. Check that the **X** , **Y** and **Z** fields represent the coordinates of the samples. If not, select them.
  6. If you plan to estimate using zonal control (possibly with soft boundary support), select **Zone 1** and (for multi-zone combinations) Zone 2.
  7. Review and confirm the **Hole ID** , **From** and **To** fields. These denote independent holes and interval break points, so make sure they are set to the right fields.
  8. Review the **Sample Summary** statistics. 
  9. Optionally, **Calculate distance statistics**.

Related topics and activities

  * [Advanced Estimation Introduction](<Multivariate_Introduction.md>)
  * [Scenario Setup](<Multivariate_Scenario_Setup.md>)

  * [Unfolding](<Multivariate_Unfold.md>)

    * [UNFOLD in Advanced Estimation](<Unfold-advanced-estimation.md>)

    * [UNFOLD Parameters](<Unfold-parameters.md>)

  * [Define Custom Zones](<Define_Zones.md>)

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