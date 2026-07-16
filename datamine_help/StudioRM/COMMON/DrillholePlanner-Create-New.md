# Drillhole Planner: Create Holes

The [Drillhole Planner](<DrillholePlannerDialog.md>) is used to interactively plan exploration, infill and production drilling patterns.

Depending on how you design your new hole data, you can set up one or more constraints in advance.

You can also edit existing holes. See [Edit Planned Drillholes](<DrillholePlanner-Edit.md>) and [Drillhole Deviation Planning](<DrillholePlanner-Lift-Drift.md>).

To add one or more holes to the drilling plan:

  1. If required, load reference data into the primary 3D view. This could include a topography file, existing model, structural models (for example, implicitly modelled geological volumes or contact surfaces), for example.

  2. Ensure your snap settings are appropriate. For example, you may wish to snap collar points to the topography (you can also automatically snap drillhole start positions to a loaded surface using the tool later).

  3. Display the **Drillhole Planner**.

  4. Choose an existing Drillhole Table (a loaded drillhole data object).

Note: I if no drillhole object has been defined as the current drillhole object when the Drillhole Planner is launched, a new object is created ("New Drillholes") and automatically selected.

Note: You can create a new Drillholes object whilst the Drillhole Planner is displayed, using the [Current Object](<Current_Objects_Toolbar.md>) toolbar.

  5. If required, configure display settings for your drillhole object using Format. This displays the [Drillhole Properties](<../VR_Help/DH_PropDialog_General.md>) screen for the selected drillhole object.

  6. I if a geological or planning model is loaded, you can use it to code the current drillhole set automatically. Select the Attribute Model click Apply to all.

  7. Define a Hole Naming Convention. This is used for all generated drillholes.

     1. Define a Prefix. Define a prefix for each drillhole name. 

Note: This is only available if the **BHID** field in your Drillhole Table is alphanumeric. If **BHID** is numeric, no prefix can be applied.

     2. Define a Start Number. This follows the **Prefix** if **BHID** is alphanumeric or represents the number starting number for numeric IDs.

Note: **Start Number** increments by 1 each time a new hole is generated, but any ID can be edited afterwards. You cannot create a duplicate ID. In cases where duplication would occur, the first higher unused number found in the BHID numeric sequence is used instead.

  8. In the **Add New Hole** section, create holes interactively or as offsets from previous holes. 

The tools in this section are used to construct new hole data with in the current Drillhole Table. Holes will be added using the current Dip, Azimuth, HoleLength, SampleLength, StartDepth, Lift and Drift settings (see below).

See the preceding sections for more information on how to create new hole data.

  9. [Edit Planned Drillholes](<DrillholePlanner-Edit.md>). Also see [Drillhole Deviation Planning](<DrillholePlanner-Lift-Drift.md>).

  10. [Save Drillhole Tables](<DrillholePlannerSaveDialog.md>).

  11. Save your project and, if prompted, save your drillhole data to an external file.

Related topics and activities

  * [Drillhole Planner](<DrillholePlannerDialog.md>)

  * [Edit Planned Drillholes](<DrillholePlanner-Edit.md>)

  * [Drillhole Deviation Planning](<DrillholePlanner-Lift-Drift.md>)

    * [Add Multiple Deviations](<DrillholePlannerAddRowsDialog.md>)

  * [Advanced Drillhole Planner Settings](<DrillholePlannerAdvancedDialog.md>)

  * [Drillhole Planning](<Drillhole_Planning_Concept.md>)

  * [Save Drillhole Tables](<DrillholePlannerSaveDialog.md>)