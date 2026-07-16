![](../Images/HeaderCell.gif) |  Drillhole Validation Validating the data comprising a drillhole object  
---|---  
  
# Validating drillhole data

Drillhole data files are automatically validated when they are first imported.

Validation information is reported in the **Validation** column of the report for each imported table.

To run the validation tests again:

  1. Using the Command control bar type "validation-report" and press <ENTER>

The following table shows you how data is validated within the drillhole object:  

**Data type** |  **Tests applied** |  **If status is** |  **Then action taken is**  
---|---|---|---  
Collars |  missing holes |  holes missing |  report  
|  existence of desurvey fields |  all exist |  desurvey  
Surveys |  missing holes |  holes missing |  report  
|  existence of desurvey fields |  all exist |  desurvey  
Traces |  missing holes |  false |  report  
Assays |  missing holes |  holes missing |  report  
|  gaps |  gaps exist |  report  
|  overlaps |  overlaps exist |  report  
|  hole length |  length exceeds trace |  extend  
Lithology |  missing holes |  holes missing |  report  
|  gaps |  gaps exist |  report  
|  overlaps |  overlaps exist |  report  
|  hole length |  length exceeds trace |  extend  
Interval log |  missing holes |  holes missing |  report  
|  gaps |  gaps exist |  report  
|  overlaps |  overlaps exist |  report  
|  hole length |  length exceeds trace |  extend  
Depth log |  missing holes |  holes missing |  report  
|  gaps |  gaps exist |  report  
|  overlaps |  overlaps exist |  report  
|  hole length |  length exceeds trace |  extend  
  
## Correcting errors

When errors are detected in the drillhole data tables, the recommended method of correcting errors is to

  1. Activate theViewribbon and selectWindow | Activate | Reports

  2. Use the **Page Setup** , **Print Setup** and **Print** commands from the Project button menu to print the validation report. You can also copy and paste text selected in the report view to another text editor using the **Edit** menu commands.
  3. In your application, choose Projectbutton |SaveorSave As to save the current document.
  4. Choose Projectbutton**|****Close**.
  5. Edit the external data source files.
  6. Choose Projectbutton**| Open** and select the document name from the list of recent files.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Defining and building drillholes](<../COMMON/LoadingDynamicDrillholeData.md>)[  
Handling special values in imported files](<SpecialValues.md>)[  
Editing tables](<Edittable.md>)[  
Printing reports and plots](<aboutprinting.md>)