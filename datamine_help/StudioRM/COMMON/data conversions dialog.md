# Data Conversions

To access this screen:

  * Right-click the topmost icon in the [Loaded Data](<Loaded%20Data%20Control%20Bar.md>) control bar (showing the project name) and select Set Conversions.

  * In the [Loaded Data](<Loaded%20Data%20Control%20Bar.md>) control bar, right-click a loaded data object's attribute and select **Set Conversions**.

  * In the **[Data Object Manager](<Data%20Manager%20Dialog.md>)** , right-click a loaded data object's attribute and select **Set Conversions**.

The **Data Conversions** screen is used to determine how these values are handled when encountered in your application. You can opt to specify conversions on a table-by-table (and column-by-column) basis, or you can apply data conversion settings to all columns within a table.

The data conversion instructions are saved in the project and applied to the target table attribute values whenever the project is opened.

Imported data tables may contain special values to signify absent, not recorded, trace or below detection limit values. For example, an assay value of _-1_ in the **Ag** field might signify "not recorded" and a value of _-9_ in the **Fe** field might signify "below detection limit". 

As another example, absent data values encountered in a composite are statistically ignored when calculating the weighted or dominant text value of the composite. If all samples in the composite have absent values, the composite value is also absent. When using the Specific gravity Weighting method, if an S.G. value is absent then the weighting method automatically reverts to standard length weighting.

Absent data values can be selectively converted to zero or other values by using Set Conversions settings. The converted value is used in the calculation of the composite value. 

Also, you may use special values in assay fields to signify when a sample assay is not assayed, or shows a trace, or is below the detection limit. These might typically be shown in an assays table with negative assay values, for example, you might use '-1' for absent data or not assayed, '-9' for trace and '-99' for data that is below detection.

When the assays file is imported, these special values can be converted using the Set Conversions routine. For example, you might convert "below detection" in the Au field to 0.005 g/t, and "below detection" in the Fe field to 5 ppm, and "not assayed" in all fields to zero.

To set data conversion requirements (Loaded Data control bar method):

Use this activity to set data conversions for all loaded data objects. See further below for object attribute-specific conversions.

  1. Load the data for which you wish to determine data conversion parameters. These can be visible or non-visible data.

  2. Right-click the top-level project icon in theLoaded Datacontrol bar and select Set Conversions

The **Data Conversions** screen displays.

  3. Select the Table and Column , or check Apply to All Columns to enforce the same data conversion logic for all attributes of the selected object.

  4. Define the special Data Value (the value actually found in the object) you wish to convert.

  5. Type what you want your data value to be Converted To, or select one of the special value symbols by clicking the down arrow: 

Symbol |  Value |  Description  
---|---|---  
? |  absent |  value unknown or not recorded  
>0 |  trace |  small positive value  
< |  detection limit |  below measurement tolerance  
- |  bottom |  very large negative number  
+ |  top |  very large positive number  
  6. Click Add.

  7. Click OK.

Related topics and activities

  * [Data Object Manager](<Data%20Manager%20Dialog.md>)

  * [Loaded Data Control Bar](<Loaded%20Data%20Control%20Bar.md>)