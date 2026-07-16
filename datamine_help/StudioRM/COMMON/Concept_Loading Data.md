# Loading Data

There are several ways to load data into Studio application memory. These include:

  * **Drag and drop** drag a supported file into any 3D window. See [Drag-and-drop](<Drag-and-drop_in_Studio_3.md>).

  * Load using the **Project Files** or **Project Data** control bars (drag and drop also supported).

  * Using **Data** ribbon >> **Load** options.

  * Data loaded as part of another command or tools in Studio.

  * Automating data loading via script.

You can load native (Datamine DM or DMX) or 3rd party file formats using Datamine's extensive Data Source Drivers facility. The steps you need to take to load in particular file formats are often unique to the data formats (as they all need special instructions to convert them to the Datamine format).

You can load in a single file, or multiple files at once. Both are supported when dragging and dropping data, but you can also achieve the same using one of these methods:

  * [Load External Data](<Load-External-Data.md>)

  * [Load Multiple Files](<Load-Multiple-Files.md>)

There are also specific tools to handle the loading of data:

  * [MineScape Block Model Generator](<MinescapeBlockModelGen.md>)

  * [Gemcom Model Import](<Gemcom%20Model%20Import.md>)

Note: You can also import files to the project without loading data into memory. See [Importing Data](<Concept-Import.md>).

## Reloading & Refreshing Data

The important point to remember with **reloading** is that data is [reloaded](<Data%20Reload%20Dialog.md>) from the original source - for example, if an AutoCad is imported using the Data Source Drivers, and a Datamine file is created, the link between the Datamine file and the original source is maintained. In this situation, when data is reloaded, the Datamine file is reloaded into your application in whichever state it was last left when last [refreshed](<Data%20Refresh%20Dialog.md>), hence, if the original source data file (AutoCad) has changed, these changes will not be reflected in the associated Datamine file.

**Refreshing** data is slightly different; when data is refreshed, the original data source is accessed (the non-Datamine file). Then, the associated Datamine file is updated in line with the original source using the Data Source Drivers, and then loaded into your application. This process ensures that the data viewed is synonymous with the non-Datamine format file.