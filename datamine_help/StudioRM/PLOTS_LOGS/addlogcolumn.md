![](../Images/HeaderCell.gif) |  Adding and Removing Downhole Columns How to add and remove downhole data columns  
---|---  
  
# Adding and Removing Downhole Columns

You can add any column from any table. Columns can be duplicated so that different formats can be applied to display the same column data. You can also add composited fields, as well as fields which are computed by the application, such as sample length or desurveyed sample coordinates.

![](../Images/StepByStep2.gif)

## Adding a new column

  1. In the Logs window, click a table to select it.

  2. Right-click and select Properties.

  3. In the Log View Properties dialog, select theColumnstab.

  4. By theColumns in Viewwindow, clickAddto launch theColumn Wizard.

  5. In the Column Wizard, choose to add either a **Data Column** , a calculated **System Field** or an Axis Column, and click **Next**.  
  
  
**Select Column Type**| **To display**| **Example**  
---|---|---  
Data Column| All downhole sample data from all data tables e.g. grades and lithology codes.| Use this column type to display any of the original data fields from the imported tables.  
System Field| Computed field values like downhole depth, inclination, dip and coordinates of the desurveyed trace.| Use this column type to graph, say, how the azimuth of the hole trace varies downhole.  
Axis Column| Downhole axis fields.| Depth, Elevation, Easting and Northing.  
  6. In theColumn Wizard, click **Next**.  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| If you selected Axis Columnas a column type, you will be prompted to specify the axis column, as well as anAutomaticorFixeddepth interval. After specifying these details, theColumn Wizardis closed by clickingEnd.  
---|---  
  7. If you selected Data ColumnorSystem Fieldin the previous screen, select a **table** to define the sample interval for the column and click **Next**.  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The selected table does not have to contain the fields you wish to display: for example, by choosing the lithology table here, and a grade field from the assays table in the next step, a **composited field** is created in which the selected grade field is composited over the sample intervals defined by the selected table.  
---|---  
  8. Select one or more **fields** you wish to add using the same display style.

  9. If a composited field has been defined (the selected _table_ does not contain the selected _fields_), select the **Compositing Mode** , **Weighting Method** and **Compositing Parameters** and choose **Next**.

  10. Select the **style** which you want to apply to the columns.

  11. Select **End** to add the columns to the Log View Properties dialog, **Columns in View** box.

  12. **In the Log View Propertiesdialog, click Apply** to view the changes, or **OK** to close the dialog.

## Deleting a Column

  1. In the Logs window, click a table to select it.

  2. Right-click and select Properties.

  3. In the Log View Properties dialog, select theColumnstab.

  4. In theColumns in Viewwindow, select a column and clickDelete.

  5. In the Log View Properties dialog, select **Apply** to view the changes, or **OK** to close the dialog.

## Changing the Order of Columns

  1. In the Logs window, click a table to select it.

  2. Right-click and select Properties.

  3. In the Log View Properties dialog, select theColumnstab.

  4. In the Columns in View box, select a column, and use the **Up** and **Down** buttons to change the position in which it is displayed.
  5. In the Log View Properties dialog, select **Apply** to view the changes, or **OK** to close the dialog.

## Copying a Column

  1. In the Logs window, click a table to select it.

  2. Right-click and select Properties.

  3. In the Log View Properties dialog, select theColumnstab.

  4. In the Columns in View box, select a column and click **Copy**. A copy of the selected column is added to the end of the list.
  5. Choose **Apply** to view the changes or **OK** to close the dialog.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Formatting columns](<FormatLogColumn.md>)[  
Formatting headers and footers](<FormatHeader.md>)[  
Removing and formatting tables and column title rows](<FormatLogViewTitle.md>)