# Drillhole Validation Errors

**[Drillhole Importer](<DrillholeImporter-screen.md>)** displays validation errors for each imported table. 

Errors are split up by table e.g. Collar, Survey and any other folder. These tabs match the folder names on the **[Import Tables](<DrillholeImporter-Import.md>)** screen. All tables within each folder validated as if they were one table. The numbers on the tabs tell you how many validations have been identified for each table. A star indicates if any of the outstanding validations (errors or warnings) still need to be resolved.

The following table summarizes the errors that can be produced by **Drillhole Importer** , and other supporting information.

**Quick Fix** indicates the behaviour performed if an attempt is made to quick fix the error. Manual Fix indicates the expected interactive behaviour to resolve the issue manually, via the **Validate** screen.

See [Validate Imported Drillhole Tables](<DrillholeImporter-Validate.md>). 

Table | Error | Description | Status | Result | Quick Fix | Manual Fix  
---|---|---|---|---|---|---  
Collar | Duplicate collar ID | Two or more collars with same BHID | Error | Display duplicate collar records. Check to remove one of the records. Allow user to edit record. | Use first record | Pick which record to use or manually edit.  
Collar | Duplicate collar location | Two or more collars with collar location within textbox distance | Warning | Display duplicate collar records. Check to ignore one of the records. Allow user to edit record.  | \-  | Pick to ignore records or manually edit.   
Collar | Invalid collar record | Error in fields BHID, XCOLLAR, YCOLLAR, ZCOLLAR | Warning | Display erroneous collar record. Checkbox to ignore and allow user to edit record.  | Ignore hole | Manually edit or ignore hole.   
Collar | Missing collar record | Records found for other tables, but no associated collar | Warning | Checkbox displayed to insert record, where collar record can be manually captured. | Ignore hole | Insert missing collar record  
Collar | Collar Topography Error | The collar position in the imported file is beyond the distance threshold set for the specified **Collars Topography** (as set in **Validation Rules**). | Error | Checkbox displayed to either keep or ignore the collar. If kept, the Z value of the collar can be edited to be within the threshold allowed. The actual deviation from collar to topography is shown in the **Z (delta)** column. | - | Either disable the collar or manually edit the collar's Z value.  
Survey | Duplicate Survey depth | Two records at same AT | Error | Display both survey records. Checkboxes for ignore. Allow user to edit records. | Use first record | Pick which record to use or manually edit.  
Survey | Dip out of range | Outside of -90 to 90 | Error | Display one record prior and one record after erroneous survey record. Checkbox to ignore faulty record or manually edit. | Ignore record | Pick a record to ignore  
Survey | Azimuth out of range | Outside of 0 to 360 | Error | Display one record prior and one record after erroneous survey record. Checkbox to ignore or manually edit.  | Ignore record | Pick a record to ignore  
Survey | Missing survey records | Found a collar record but no downhole survey | Info | Display collar record. Allow user to edit (in particular to insert a dip and azimuth field into the collar table.) If this edit is made, change setting on desurvey page to enable Include survey direction from collar table and notify user through a bubble alert that this setting was changed.  | - | Specify dip and azimuth for the collar record, which gets used with At=0.  
Survey | Missing collar record | Survey records found without a collar | Info | Checkbox displayed to insert record, where collar record can be manually captured. | - | Insert record  
Survey | Survey beyond EOH depth | Last survey TO is longer than end of hole | Error | Display collar record and final record of survey. Allow user to edit record.  | Reset EOH depth to last survey AT | -  
Survey | Large dip curvature | Adjacent records change by more than permitted amount | Warning | Display one record prior and one record after erroneous survey record. Checkbox to ignore or manually edit. | Ignore record | Pick a record to ignore  
Survey | Large azimuth curvature | Adjacent records change by more than permitted amount | Warning | Display one record prior and one record after erroneous survey record. Checkbox to ignore or manually edit. | Ignore record | Pick a record to ignore  
Downhole (Interval and Point) | Missing collar record | Records found without a collar table | Info | Checkbox displayed to insert record, where collar record can be manually captured. | - | Insert record  
Downhole (Interval and Point) | Overlapping samples | Downhole sample FROM and TO overlap; or depth From > To.Or Matching AT values. | Warning | Show erroneous downhole records, and allow for manual edits. Checkbox to ignore rows. | Attempt to correct (for duplicate FROM and TO). Ignore record if all fields are identical or one value has blank entries for all. | Edit records as required  
Downhole (Interval and Point) | Samples out of range | Downhole records (AT, FROM or TO) found deeper than hole length.Checks for AT, FROM or TO <0 or absent/invalid. | Error | Display collar record and final record of downhole. Allow user to edit record. Check for any absent or negative values. | Reset EOH depth to last sample TO or AT | -  
Downhole (Interval and Point) | No downhole records | No downhole records for collar record | Info | Nothing required | - | -  
Downhole (Interval only) | Sample interval gaps | Gaps in downhole record greater than allowed | Warning | Show record above and below gap. Option to insert record (i.e. insert record to fill in the gap i.e. BHID, FROM TO values are inserted matching previous and next records) and manually edit.  | Ignore record | Insert record to fill gaps.  
All tables | Field type check | Checks that all field types (Alpha or Numeric) are consistent between tables | Info | Checks any fields which occur in two or more tables (e.g. BHID will always be checked) has a consistent field type. | Convert numeric fields to alpha | -  
  
Related topics and activities

  * [Drillhole Importer](<DrillholeImporter-screen.md>)
  * [Validate Imported Drillhole Tables](<DrillholeImporter-Validate.md>)