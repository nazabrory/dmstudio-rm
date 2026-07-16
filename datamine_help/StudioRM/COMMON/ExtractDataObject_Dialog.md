# Extract Data Object

To access this screen:

  * **Data** ribbon **> > Objects >> Extract**.

  * Using the [Data Object Manager](<Data%20Manager%20Dialog.md>), select Extract from Object.

  * In the [Loaded Data](<Loaded%20Data%20Control%20Bar.md>) control bar, right click any object and select Extract.

  * In the [Sheets](<Sheets%20Control%20Bar%20Overview.md>) control bar, right click any object and select Extract.

Get information held within currently loaded data objects, and create new objects based on the values contained within a selected field.

Warning: This process creates new objects based on the unique values of a selected field, so there can be a potentially large number of new objects created during this process.

Create extracted objects by either specifying a field within the object's database, meaning all unique values found will be used as a basis for creating a new object, or you can use filter expressions to declare how the original object data is to be used during extraction.

Note: Block models and drillholes can't be processed with this function. Use this function on point, string and wireframe data only.

## Example

The simple wireframe object below is comprised of three linked strings:

![](../Images/ExtractObject1.gif)

Running Extract Object and selecting the **LINK** field to act as the extraction key (two link values are present in the database to representing the linking meshes between each of the the three lines), results in the following message:

![](../Images/ExtractObject2.gif)

Selecting Yes shows a series of two alternating progress bars (Apply Filter and Copy File). Two new object files are created. You can see their descriptions in the Loaded Data, **Sheets** or **Project Data** control bar.

![](../Images/ExtractObject3.gif)

The description is formed from the original filename(s) combination, followed by the details of the field used to split the original file, and the value of the field in the new file.

Use the visibility controls in the Project Data control bar to see the independent structures extracted from the parent object. For example:

![](../Images/ExtractObject4.gif)

and;

![](../Images/ExtractObject5.gif)

To extract structures from a loaded 3D object:

  1. Review the **Object Name**. This is the name of the data object from which data is extracted. It can't be edited.

  2. Choose an **Extraction Method**.

     * Choose **Extract by Field** to select a field from the list. All unique values found within the selected object's database result in new object creation.

     * Choose **Extract Using Filter** to either enter a filter expression manually, or use one of the following options (availability depends on the object type selected):

       * Select By Group Select a data group from the using the cursor. A filter expression will be created based on the selection.

       * Select By Surface Select a surface using the cursor. A filter expression will be created based on the selection.

       * Select By Attribute Select an attribute using the cursor. A filter expression will be created based on the selection.

       * Custom Activates the Filter Wizard button.

       * Filter Wizard Opens the [Data Expression Builder](<ExpressionWizardDialog.md>) to build filter expressions.

Note: Filter expressions are accepted after a cursory check of syntax, however, if a filter expression is valid (in that it contains syntax in the correct structure) but is intended for filtering data fields that do not exist in the incoming file, the file is loaded without filtering. For example, if you elect to filter a wireframe model based on, say, an **XP** field, but this field does not exist in the loaded file - the entire contents of the file will be loaded. In other words, filtering will not be performed.

Related topics and activities

  * [Data Object Manager](<Data%20Manager%20Dialog.md>)

  * [Data Expression Builder](<ExpressionWizardDialog.md>)