![](../Images/HeaderCell.gif) |  Adding and Removing Table Columns Adding and removing columns  
---|---  
  
# Adding and Removing Table Columns

A table may display all or some of the data in memory. Table columns can be duplicated so that the same data can be shown with different formats. Composited fields from other tables can also be added as well as fields which are computed by the program such as sample length or desurveyed sample coordinates.

Because a table is a representation of data in memory, removing a column does not delete it from any source file; it can be added to the table again later.

##  ![](../Images/StepByStep2.gif)

## To Add a Column to a Table

  1. Turn on the Table window display and click the Tables tab to make the window active.

  2. In the Tables window, right-click a table and select Format.

  3. In theColumnstab, clickAddby theColumns in Viewwindow to launch theColumn Wizard.

  4. If you have drillhole data loaded, choose whether you wish to add a Data Column or a System Field, and click Next.

Select Column Type |  To display |  Example  
---|---|---  
Data Column |  Downhole sample data from any data tables loaded into memory. |  Displaying any original data field e.g. grades and lithology codes from imported tables  
System Field |  Computed field values such as downhole depth, inclination, dip and coordinates of the desurveyed string . |  To display graphically how the azimuth of the hole string varies down a hole.  
  
  5. Select one or more fields that you wish to add using the same display style.

![note.gif \(1017 bytes\)](../Images/note.gif) | Fields can be selected from any table. For example, when adding columns to the lithology table, a grade field from the assays table can be selected, and a composited grade column is displayed i.e. the selected grade field is composited over the sample intervals (Depth From, Depth To) defined in the current table.   
---|---  
  
  6. If a composited field has been defined, select the Compositing Mode, Weighting Method and Compositing Parameters, and click Next.

  7. Select the display style to be applied to the new columns.

  8. In theColumn Wizard, click End.

## To Remove a Column from the Table View

  1. In the Tables window, select the tab of the table you wish to edit.

  2. Select the column to be removed by clicking the field name header.

  3. Using theManageribbon selectTable | Edit | Remove Column

![note.gif \(1017 bytes\)](../Images/note.gif) | Table columns can also be added, copied, removed, ordered, reset and formatted by right-clicking a table in the Tables window, and selecting Format.  
---|---  
![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Creating a new table type](<CreateTable.md>)[  
Changing the format of table columns](<FormatColumn.md>)