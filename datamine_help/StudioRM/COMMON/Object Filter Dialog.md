# Object Filter

To access this screen:

  * Drag and drop and file from your **[Project Files](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)** control bar into any active 3D window whilst holding CTRL.

  * Drag and drop and file from your operating system into any active 3D window whilst holding CTRL.

When loading a Datamine file, choose which aspects are loaded. This is commonly called "load filtering".

The contents and title of this screen vary according to the [type of file](<filetype.md>) being loaded, although the overall structure and layout is the same.

The top section of the window shows a File Description and reports the following:

  * The name and full system path of the incoming file.

  * The number of records that make up the underlying database table.

  * The type of object that the incoming data was originally created from.

To filter the data that is loaded:

  1. Display the **Object Filter** screen.

  2. Check or uncheck **Data Fields**. Only checked fields are present in the loaded data object. 

  3. Files containing geometry include Coordinate Fields. These fields must be mapped to **X** , Y and Z coordinates.

  4. If you are loading a strings data file, the following additional settings must be made:

     * PVALUE  The **PVALUE** represents the individual string to which a vertex belongs. Select a field from the drop-down list to determine the data column used to form point-string relationships. As with coordinate fields, standard database descriptions such as _PVALUE_ are automatically applied if they exist within the data to be loaded.

     * PTN Each string contains a series of points and vertices; this value is stored as a sequence of numbers, the standard name for this index in Datamine string files is PTN. However, you can choose another field.

  5. Filter incoming data by clicking Expression Builder to display the [Expression Builder](<ExpressionWizardDialog.md>) screen. Alternatively, enter a filter expression directly into the Filter field.

Related topics and activities

  * [The Project Files Control Bar](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)

  * [Expression Builder](<Expression%20Builder%20Dialog.md>)