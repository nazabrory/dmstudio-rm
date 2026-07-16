![](../Images/HeaderCell.gif) |  Table Filter Expression Dialog An explanation of fields and properties  
---|---  
  
# Table Filter Expression Dialog

This dialog is displayed when a filter expression is being added to a table sheet, or an existing filter expression is being edited (using the [Format Table Display](<tablefiltersortdialog.md>) dialog).

Filter expressions can be a statement, or series of logical statements, used to control which data qualifies for inclusion in the current table. You can restrict rows based on a comparison of a database properties with a value (only show rows where an AU value is less than 2.5, for example), a comparison of two or more properties (e.g. only show rows where a copper grade is less than a grade cut-off value) or where the contents of a table cell can be matched to a pattern using regular expressions.

For more information on logical expressions and filtering.

Field Details:

The following fields are available:

Expression: this editable field contains the logical expression to be applied to the table.

Expression Builder: Launches the Data Expression Builder dialog, an interface for producing simple and complex logical expressions.

Filter Enabled: select this checkbox to make the filter active (i.e. it will be applied with other active filters in the list shown in the [Format Table Display](<tablefiltersortdialog.md>) dialog). Clear this check box to make the specified filter expression inactive without removing it from the list, so can be reactivated later if required).

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Format Table Display Dialog](<tablefiltersortdialog.md>)