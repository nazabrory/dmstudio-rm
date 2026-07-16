# MineScape Block Model Generator

To access this screen:

  * **Data** ribbon **> > External >> Minescape Block Model**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "minescape-to-blockmodel"

  * Use the quick key combination "msk".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **minescape-to-blockmodel** and click **Run**.

Import one or more MineScape Stratmodels and convert them to strata block models in Studio. Models selected for import are combined into a single strata model.

The individual models should be created from the same prototype model and have the same sub-cell grid. 

### Overlapping Data

By default, non-overlapping cells and sub-cells are added directly to the final block model, but you can disable this behaviour if you want.

If enabled, where partially overlapping cells in Z are detected, subdivision is performed to remove overlaps. Where completely overlapping cells between models are detected, the cell from the last imported model (that is, the model lowest in the list) is added to the final compound model.

If Resolve overlapping seams is unchecked, the output consolidated model will contain overlapping subcells (one for each overlapping seam object).

To import and convert MineScape prism models to a single, compound Datamine block model:

  1. Ensure you have one or more MineScape prism models (.csv) available on disk.

  2. Open the **MineScape Block Model Generator**.

  3. Use the **Minescape Folder** browser to locate the folder in which your prism models are stored.

All individual prism model files display in the table below.

  4. Review the files table below, displaying the **File** name and **Seam** name for each file. 

**Note** : the **Seam** is the text after the final underscore of the file name, and is used The value from this column is used to populate a **SEAM** attribute in the generated block model.

  5. For each file you wish to import and convert to a single model, ensure the first column is **checked**. Unchecked data is not imported.

  6. Choose the **Number of Subcells** in the **X** and **Y** directions. You can choose between 1-10 for each direction.

**Note** : values greater than 20 are not permitted.

  7. Select the **Weight Column** , used to host weighted average values in the final model.

  8. Click **Create Block Model**.

For each listed file, a progress bar displays. The name of the file being processed appears in the title. Files are process in the top-bottom order as listed in the table.

  9. Review the imported, compound block model in a 3D window.

Related topics and activities

  * [Loading Data](<Concept_Loading%20Data.md>)

  * [Import and Load Data](<Concept_Importing%20and%20Exporting%20Data.md>)