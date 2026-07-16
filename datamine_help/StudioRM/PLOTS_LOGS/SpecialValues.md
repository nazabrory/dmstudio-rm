![](../Images/HeaderCell.gif) |  Special Values Handling special values in data files  
---|---  
  
# Special values

Imported data tables may contain special values to signify absent, not recorded, trace or below detection limit values. For example, an assay value of -1 in the Ag field might signify "not recorded" and a value of -9 in the Fe field might signify "below detection limit".

##  ![](../Images/StepByStep2.gif)

## To set conversions

  1. Import the table.

  2. Choose Data | Set Conversions display the Data Conversions dialog.

  3. In the Column box, select the Table and Column name, or check the Apply to All Columns option.

  4. In the Value box, type the special value you wish to convert in the Data Value box.

  5. Type the value you wish to convert to in the Convert To box, or select one of the special value symbols by clicking the down arrow button:

Symbol |  Value |  Description  
---|---|---  
? |  absent |  Value unknown or not recorded  
>0 |  trace |  Small positive value  
< |  detection limit |  Below measurement tolerance  
- |  bottom |  Very large negative number  
+ |  top |  Very large positive number  
  
  6. Choose the Add button.

  7. Repeat steps 3 to 6 for each value conversion required in each field in each table.

  8. Choose OK to apply conversions.

The data conversions are saved in the document and applied to the imported tables whenever the document is opened. 

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Drillhole data validation](<validatedata.md>)