![](../Images/HeaderCell.gif) |  Table Contents An explanation of fields and properties  
---|---  
  
# Table Contents tab

### To access this dialog:

  * Double-click a Table plot item in the Plots window to display the Table dialog, Click the Contents tab.

This tab, part of the Table Properties dialog, is used to configure general properties for a Table plot item, including the data object/columns that are represented, and how they are displayed. Click Apply to update the current Table with edited properties.

Field Details:

The following fields are available on this dialog:

Table: select an in-memory table from which you wish to display values in your plot view.

Columns: once a Table is selected (see above) you are given the option to select each of the available fields for further formatting. For each of the buttons that lie to the right of the Columns list, operations are performed in context with the selected item. Note that only one column field can be modified at any one time.

Reset: resets the selected data column properties to the default values.

Insert: displays the Select Column dialog. From here, you can select any column that is currently part of the selected table's underlying database. You can duplicate existing columns if required, and format the duplicate entries entirely separately from the original.

Delete: remove the table column that is currently selected. This will not delete any data from the object's database; only the table view is affected by this command.

Format...: opens the [Format Table Column](<../COMMON/Format%20Display%20Dialog_Label%20Item%20Format.md>) dialog for the currently selected entry.

Up/Down: move the selected column either up the list (resulting it being displayed further to the left in the table view) or down the list (resulting in a shift to the right).

Title Row/Format: allows you to edit the title row of the table, using the [Cell Format](<cell%20format%20dialog.md>) dialog.

Font/Color: edit the font and/or color that is used to display table values.

Headings: allows you to edit any header rows associated with the table, using the [Cell Format](<cell%20format%20dialog.md>) dialog.

Data Rows: you can limit the number of data rows displayed by entering an integer here. By default, ten rows of data are shown, but this can be increased or decreased as required. Note that this is the number of rows from the initial row; it is not possible to decimate the rows and show every nth row, for example.

Frame: select the thickness of the outlying frame of the table, in points.

Grid: select the thickness of the cell borders within the selected table, in points.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Table Filters](<tablefiltersortdialog.md>)