# Import and Load Data

Your application can **[load or import data](<Concept_Loading%20Data.md>)** in a variety of formats, including Datamine's proprietary formats. Imported and loaded data are shown in the **[Project Files](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)** control bar.

There are advantages to using Datamine files, particularly for block models where an 'on-disk' mechanism allows data to be partly loaded and processed without straining your system. Datamine files can also be specified when running **[processes](<Studio%203%20Commands%20and%20Processes.md>)**.

Data can also be loaded by other methods, including automatically as part of a managed process. You can find out more about this in the corresponding help files.

**Note** : You can also **[reload and refresh data](<Concept_Loading%20Data.md>)**.

To load one or more Datamine files (drag and drop method):

The quickest way to load a Datamine file is to drag and drop it into a 3D window:

  1. Locate the file (or files) you wish to load using your operating system's browser.

  2. Left-click or tap and drag selected file(s) into any 3D window.  

You can load 3D and non-visual files in this way. 3D data is displayed (if the 3D view settings permit it) in all available 3D windows using default formatting.  

Data is loaded and file references are added to the project. 

  3. **Save** your project. 

To load a Datamine file (menu method):

You can also load Datamine files using the menu system. Only one file at a time can be loaded using this method.

  1. Activate the **Data** ribbon and expand the **Datamine** menu.

  2. Select the data type you wish to load.

  3. Using the file browser, locate and **Open** your file.  
  
The target file is loaded.

  4. **Save** your project. 

To import a single file (any format) and load it into memory in one operation:

All file formats, including Datamine files, can be imported using Data Source Drivers:

  1. Activate the **Data** ribbon and expand the **External** menu.

  2. Use the **[Data Import](<data%20import%20dialog.md>)** screen to pick a **Driver Category** and **Data Type**.  

You can view driver-related information by clicking **Driver Help** after selecting a category.

  3. Complete the import details as shown in the screens that follow. These are driver-specific and you can find out more about them by pressing F1 as each screen is displayed. Typically, you specify:

     * Attribute fields to import.

     * Driver-specific details, such as a **LAYER** field for **CAD** data, for example.

     * For ASCII text imports, if a header row exists, or if data is delimited.

  4. Once import details are completed, data is loaded into memory. If the data contains 3D geometry, a default overlay is created and displayed in 3D windows.  

  5. **Save** your project. 

To import a file (any format) and add it to the project without loading:

You can also import data purely to add a project file reference. If you don't need to use your imported data right away, or if the file is large, this can be useful option.

  1. Activate the **Data** ribbon and select **Import >> Add to Project >> Add to Project (by driver)**.

  2. Use the **[Data Import](<data%20import%20dialog.md>)** screen to pick a **Driver Category** and **Data Type**.  

You can view driver-related information by clicking **Driver Help** after selecting a category.

  3. Complete the import details as shown in the screens that follow. These are driver-specific and you can find out more about them by pressing F1 as each screen is displayed. Typically, you specify:

     * Attribute fields to import.

     * Driver-specific details, such as a **LAYER** field for **CAD** data, for example.

     * For ASCII text imports, if a header row exists, or if data is delimited.

  4. Once import screens have been completed, a file reference is added to your project. You can see this reference in the **[**Project Files**](<Concept_Project%20Files%20Control%20Bar%20Overview.md>)** control bar. Data is not loaded into memory.

  5. **Save** your project. 

To filter data during loading or importing single files:

You may not want all of your data file to be loaded. Studio applications allow you to specify a filter during import or loading, to extract only the relevant data items. This can help to reduce RAM usage and improve system performance.

  1. Hold down CTRL.

  2. Drag and drop a file or files from either the **Project Files** control bar or your operating system into a 3D window.

  3. In the Datamine Data Import dialog, select the **Data Fields** you wish to import.

  4. Some data types require specific field mapping to import correctly. This can be **Coordinate Fields** or **Control Fields** and are specific to each data type. Automatic mapping is performed if possible.

  5. If you want to use a **Filter** expression to further refine your import, add one. **[Filtering data](<Filtering_Data.md>)** can ensure you only import the data you need.

  6. Click **OK** to load your data into memory.

  7. **Save** your project. 

To import multiple files to the project (without loading them):

  * See [Import Multiple Files to Project](<ImportMultipleFileOptions.md>).

To load multiple files into memory:

  * See [Import Project Files by Driver](<importfiles-Driver.md>).

Related Information and Activities

  * [Loading Data](<Concept_Loading%20Data.md>)
  * [Load External Data](<Load-External-Data.md>)
  * [Load Multiple Files](<Load-Multiple-Files.md>)
  * [Loading and Saving Filtered Data](<Filtering_Data.md>)
  * [Drag-and-drop](<Drag-and-drop_in_Studio_3.md>)
  * [Loading Dynamic Drillhole Data](<LoadingDynamicDrillholeData.md>)
  * [Unload Data](<Unloading%20Data.md>)
  * [Importing Data](<Concept-Import.md>)
  * [Import Project Files by Driver](<importfiles-Driver.md>)
  * [Import Multiple Files to Project](<ImportMultipleFileOptions.md>)
  * Data Management Screens
    * [Project Browser](<ProjectBrowser.md>)
    * [Data Import Screen](<data%20import%20dialog.md>)
    * [ Data Export Screen](<ExportTable.md>)