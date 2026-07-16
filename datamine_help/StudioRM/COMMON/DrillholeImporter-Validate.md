# Validate Imported Drillhole Tables

To access this screen:

  * **[Import drillhole data](<DrillholeImporter-Import.md>)** tables into **Drillhole Importer** and select the **Validate** tab.

This screen, part of the Drillhole Importer console, is used to:

  * Define drillhole data validation rules
  * Display validation errors, warnings and information for all the imported tables.
  * Correct errors in imported data and record the status of each correction. 
  * If possible, automatically apply a "quick fix for easily-resolvable errors.
  * Export a list of validation errors as a table.

Here's a **[list of validation errors and their associated statuses](<DrillholeImporter-Errors.md>)**.

Errors are split up by table, for example, _Collar_ , _Survey_ and so on. These tabs match the folder names on the **[Import Tables](<DrillholeImporter-Import.md>)** screen. All tables within each folder are validated as if they were a single table. The numbers on the tabs tell you how many validation results have been highlighted for each table. A star indicates if any of the outstanding validations (errors or warnings) still need to be resolved.

Validation settings are stored in the current **[scenario](<DrillholeImporter-Import.md>)**. When you export a scenario, these settings are also transferred to the destination system, ensuring a consistent validation approach between team members.

There are three ways to fix validation errors:

  * Automatically, if possible, by applying rule-based 'quick fixes'. You can define these rules.
  * You can manually 'quick fix' a validation, that is, apply the current validation rule set to the selected error. One or more errors can be selected before a fix is applied.

**Tip** : use keyboard shortcuts such as SHIFT to select multiple contiguous records and CTRL to add any records to the selected set.

  * You can manually edit the table values of conflicting or erroneous values until they are suitable for desurveying.

**Note** : Drillhole Importer table columns can be dynamically resized.

By default, when you apply fixes, any previously listed errors (resolved by subsequent changes) remain in the grid, but appear in light grey with a "Resolved" status. You can toggle the display of fixed entries by checking or unchecking **Show Committed Errors**.

To define validation rules (do this first if you haven't already):

  1. Complete the **[import of drillhole database tables](<DrillholeImporter-Import.md>)**.
  2. Display the **Validate** screen.
  3. Select **Rules...**

The **Edit Rules** screen displays.

  4. Define the distance tolerance below which a collar is deemed to be a **duplicate** of another, using **Collars - Duplicate collar location <**. Any collar within the stipulated distance (in a straight line in 3D space) will be considered duplicate and will be reported as a validation failure ("Duplicate Collar Location").
  5. To **validate the position of imported collars** in relation to a surface topography file:
     1. Check **Collars Topography** (if unchecked, no validation is performed of collar position).
     2. Enter a **Tolerance** distance. _Collars_ beyond this distance from the topography file (in a vertical direction) will fail validation and will need to be fixed before continuing.
  6. Decide if gaps between sample records are reported. Check **Downhole - Sample interval gaps** to highlight gappy data, or uncheck to ignore.
  7. Report unexpected dip changes in the _Surveys_ input file using **Survey - Large dip curvature change >**. Set the change of dip in degrees over (per) a nominated distance, e.g. a change of 15 degrees per 10 meters.
  8. Similarly, choose what constitutes an **unexpected change in bearing** over a given distance using **Survey - Large bearing curvature change >**.
  9. In the **Fixes** group, choose how automated fixes ('quick fixes') are applied, if triggered:
     * **Collar end of hole longer than interval** : If a drillhole EOH location is detected that doesn't align with the terminal drillhole interval's "TO" position, choose what happens:
       * If **checked** , an attempt is made to automatically adjust the drillhole data object in memory to align the collars EOH value with the drillhole interval "TO" position. This can achieved either by changing the collar's EOH position (**Reset collar EOH length**) or by editing the interval (**Reset interval TO**).
       * If unchecked, no quick fixes are applied.
  10. Click **OK** to update the validation rules and refresh your data with the new rules in place.

Note: Validation rules are saved with your project, so a project save is also advisable.

To perform validation on imported data tables:

  1. Complete the **[import of drillhole database tables](<DrillholeImporter-Import.md>)**.
  2. Display the **Validate** screen.
  3. Define your validation rules (see "To define validation rules", above).
  4. Click **Validate**.

For each imported table, validation results display. 

  5. If validation errors have occurred, they appear on the respective tab on the left of the screen.

Validation errors are categorised as errors, warnings or information. This is reflected in the **Status** column.

     * **Errors** must be fixed before proceeding to the desurveying stage. **Status** displays as a red cross.
     * **Warnings** should be reviewed and ideally fixed, but you can continue to desurveying, although unexpected output may occur. **Status** also displays as a red cross.
     * **Information** is to alert you to a particular situation, but no action is required, or can be taken. **Status** displays as a an "i" symbol. An example of this could be where assay table contains a BHID with no downhole records.
     * **Resolved** validation errors not yet committed to the loaded data objects (see below) are shown as a green tick.

The Record number indicates the data row at which the error was detected. 

The **BHID** represents the unique drillhole identifier with which the error is associated.

A **Validation description** provides information about what has gone wrong. This could be "Duplicate collar location", "No Downhole Records" and so on. Text in green is for information only, but may highlight an area of concern. Orange text represents a warning, and red text is a fatal error that will prohibit desurveying later on.

The **Action** column describes the action to be taken when the next **Commit** is performed.

  6. Select one or more validation errors and resolve it. 

**Tip** : use keyboard shortcuts such as SHIFT to select multiple contiguous records and CTRL to add any records to the selected set.

The validation resolution table on the right updates to show the fields relevant to the validation failure. For example, if a duplicate collar position has been detected (which may be normal, say, for fan drilling), the **XYZ** fields of the duplicate holes, along with their **BHID** display. In this example, you could edit the coordinates displayed for each hole or choose to ignore one of the duplicates by unchecking **Keep**.

  7. To automatically apply an obvious fix to the selected error, use **Quick Fix**. This will only be valid for certain types of validation failure. Quick-fixing will attempt to resolve the error according to the current validation rule constraints.

  8. Review and resolve each validation error as appropriate until all errors on all tabs have been considered (even if you choose to ignore them) and, if required, data value fixes committed.

**Tip** : Use **Previous** and **Next** to cycle through the errors displayed in each table.

  9. To remove a previous data edit, use **Undo** to reinstate the drillhole data as it was last committed.
  10. Click **Commit** to update the current drillhole data objects. This will not change physical files.
  11. Check Show committed records to display committed changes in the validations table above. Uncheck to hide these records, displaying only unattended validation items.

Related topics and activities

  * [Drillhole Importer](<DrillholeImporter-screen.md>)
  * [Import and Map Data](<DrillholeImporter-Import.md>)
  * [Drillhole Validation Errors](<DrillholeImporter-Errors.md>)
  * [Desurvey Validated Drillhole Data](<DrillholeImporter-Desurvey.md>)