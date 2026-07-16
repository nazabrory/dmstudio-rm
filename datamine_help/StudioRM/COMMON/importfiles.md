# Import Project Files

To display this screen:

  * **Data** ribbon **> > Import >> Add to Project >> Add to Project (by driver)**.
  * **Project Files** control bar **> > Right-click the project icon >> Add >> Import Files**.

  * **Project Data** control bar **> > Right-click "Project" >> Add >> Import Files**.

The Import Files screen is shown as the final step in the [data import process](<Concept-Import.md>) and contains three tabs, each suited to a specific import-related purpose:

  * Files Define the names of the resulting data files to be added to the current project.

  * Fields Filter any non-essential incoming data on a field-by-field basis, and options for specifying the display legends to use to display the incoming data.

  * Rename Fields As Datamine file data columns are restricted to 24 characters in length, it may be necessary to shorten incoming field names to provide a smooth transitional process during import. All fields being imported that are over 24 characters in length will be automatically 'trimmed' (characters will be removed from the end of the field until 24 characters is achieved), and you can opt to rename any incoming field (this may be useful if the default output for one application is synonymous with a particular table field, for example).

The **Import Files** screen displays when you [Import Project Files by Driver](<importfiles-Driver.md>) and [Import Multiple Files to Project](<ImportMultipleFileOptions.md>).

Note: The mappings specified in the Rename Fields tab are applied whenever a file is saved to Datamine's native format, and not just when it is saved during important.

Note: For some file formats, you can import multiples files at once. See [Import Multiple Files to Project](<ImportMultipleFileOptions.md>).

To define file output settings:

  1. Display the **Import Files** screen.

  2. Define the Base file name. This is the prefix used to recognize the file after importation.

  3. On the **Files** tab, use **Save File Types** options to create one or more Datamine file types. Each selection results in an additional project file reference.

if you have specified a Base File Name, each enabled field description will be automatically generated, using the base name with one of following suffixes:

     * PT for points files

     * TR for triangle (wireframe) files

     * ST for string files

     * BM for block model files

  4. By default, Generated extended precision files is selected. We recommend you leave this selection as it is.

  5. The Description is shown in the **[Properties](<properties%20control%20bar%20overview.md>)** control bar if the file is subsequently selected in Studio. Edit this as required.

  6. Set the Location to store the converted Datamine file or files.

To define field mappings:

  1. Display the **Import Files** screen.

  2. Select the Import Fields tab.

  3. All files in the incoming file display. All are checked by default (=all are created in the imported file). Check or uncheck attributes to include or exclude them from the imported file(s).

  4. Choose a **COLOUR** field. This is automatically mapped to Datamine's colour codes and can be useful for default 3D window visualization.

     * Click **+** to automatically create a default colour legend for this field.

  5. Check Use legends to resolve colour values to display the Colour Legend list.

     1. Select a default visualization legend to use to display **COLOUR field** values.

     2. Display a **preview** of the legend.

     3. **Edit** the legend using the **Legends Manager**.

To rename fields during importation:

  1. Display the **Import Files** screen.

  2. Select the Rename Fields tab.

The left side of this tab is used to contain a list of conversion instructions. Any automatically (or previously added) instructions is shown in the following format:
         
         ORIGINAL NAME -> NEW NAME

NEW NAME should not be longer than 24 characters, and if a string greater than 24 characters is added, it will be automatically concatenated to 24 characters on import.

  3. Click **Add** to insert a new instruction.

     1. Enter the name of the original field name (From).

     2. Enter the name of the field name in the imported file (To).

  4. Renaming instructions are processed in order, with the uppermost renaming instructions processed first. **Raise** or Lower an item to change its processing order.

Note: Select an existing item and click **Edit** to modify it.

Related topics and activities

  * [Importing Data](<Concept-Import.md>)

  * [Import and Load Data](<Concept_Importing%20and%20Exporting%20Data.md>)

  * [Import Project Files by Driver](<importfiles-Driver.md>)

  * [Import Multiple Files to Project](<ImportMultipleFileOptions.md>)

  * [Load External Data](<Load-External-Data.md>)

  * [Load Multiple Files](<Load-Multiple-Files.md>)