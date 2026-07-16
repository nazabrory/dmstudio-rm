# Unfolding

To access this screen:

  * In the [**Advanced Estimation**](<Multivariate_Dialogs_Overview.md>) wizard, select **Unfolding**.

**UNFOLD** is a grade estimation technique where folded orebodies are unfolded to reduce structural complexity. When an orebody is folded in the world coordinate space (WCS), spatial relationships are reduced which means that traditional linear estimation techniques may not do a good job at grade estimation (because mineralization occurred before the rock was folded).

The [**UNFOLD Wizard**](<UnfoldWizard.md>) can optionally generate a parameters file that can be used in the [**Advanced Estimation**](<Multivariate_Introduction.md>) (AE) wizard, to automatically set unfolding settings for an estimation run.

**Note** : The **Unfolding** screen of the AE wizard is only accessible if Show unfolding parameters is checked on the **[Select Samples](<Multivariate_Select_Samples.md>)** screen.

You can use the **Unfolding** screen to import an existing **Unfolding parameters file** (using the **Select Samples** screen) and apply it. Then, edit the settings on this screen.

**Note** : Unfolding parameters can be exported using the **[Parameters](<Multivariate_Import_Parameters.md>)** screen.

To update or create unfolding parameters for cokriging:

  1. Review or browse for unfolding strings. These define the hanging wall and footwall of the zone for unfolding and are typically defined using the **UNFOLD Wizard**). See [Create Unfolding Strings](<Unfold_HWFW.md>).

  2. Where possible, the following key attributes are detected in the strings file:

     * **Section identifier** Section strings represent the folds in the orebody. These are added at regular intervals by the **UNFOLD** wizard.

     * Boundary (HW/FW) idthe attribute defining the hangingwall and footwall data.

     * Within section tagWithin section tag field, for example, _WSTAG_. This is a numeric field in the selected **Strings file** , defining the stratigraphical links between hangingwall and footwall points on strings within the same section.

     * Between section tagBetween section tag field, for example, _BSTAG_. This is a numeric field defining the stratigraphical links between 2 points on strings on adjacent sections with the same boundary. 

  3. Choose how links between unfolding strings are generated:

     * Within section and Between section tagsWithin section links are defined by the **Within section tag** field. Between section links are defined by the **Between section tag** field.

     * Do not use any tagsWithin-section links and between-section links are defined automatically without considering other tag string data.

  4. Choose the **Plane** of the structural interpretations defined in the input unfolding strings file.

     * **Vertical section** Vertical sectional interpretation.

     * Horizontal planeInterpretation in plan.

  5. Define the **Tolerance** in the calculation of the UCSA coordinate expressed as a proportion of the UCSA width.

  6. Choose the UCSB origin tag number. This is the number of points which define the origin surface from which the UCSB coordinate is measured. If not specified, the surface is created from the first points on each of the hangingwall and footwall strings.

  7. Set the Hangingwall boundary value. This is the value of the **Boundary (HW/FW) id** in the string file that defines the hangingwall of the unit. Similarly, set the Footwall boundary value.

  8. Define the type of **UCSA** coordinate (across strike) written to the unfolded data file.

     * Normalised (between 0 and 1)

     * Adjusted (normalised * av. length)

     * True length

     * World X coordinate

     * World Y coordinate

     * World Z coordinate

  9. Set the type of **UCSB** and **UCSC** coordinates to be created using the same options as above.

  10. Choose which data to review after unfolding:

     * Unfolded stringsload the unfolded string data into the 3D view after generation.

     * Unfolded samplesload the unfolded samples into the 3D view after generation.

Click **Run and Display** to run the **UNFOLD** process and generate unfolded data for estimation.

Review the **Valid strings and samples** results, where the number of unfolded strings and samples are displayed. 

Related topics and activities

  * [Advanced Estimation Introduction](<Multivariate_Introduction.md>)
  * [Scenario Setup](<Multivariate_Scenario_Setup.md>)

  * [Select Samples](<Multivariate_Select_Samples.md>)

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