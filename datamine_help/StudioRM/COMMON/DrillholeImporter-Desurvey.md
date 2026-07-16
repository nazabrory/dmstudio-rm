# Desurvey Validated Drillhole Data

To access this screen:

  * [Validate Imported Drillhole Tables](<DrillholeImporter-Validate.md>) and select the **Desurvey** tab.

This screen, part of the **[Drillhole Importer](<DrillholeImporter-screen.md>)** console, is used to desurvey validated drillhole component data files (collars, assays, surveys etc.).

Validation isn't mandatory, and desurveying can be run against the imported data files without validation, or with existing validation errors. Results in this situation, however, can be unpredictable so it is recommended that you review each validation failure.

Various options are available to control the desurveying process (which is actually running **[HOLES3D](<../Process_Help_XML/holes3d.md>)**). 

**Note** : Whilst a typical drillhole importation scenario includes a Survey file, one is optional. If you decide to desurvey without a survey database, all data is assumed to be vertical, and this is highlighted when you actually desurvey the validated input data on the **Desurvey** screen.

You can update an existing drillhole file with new desurveyed information or create a new file. Once desurveying is complete, a summary displays, which can be exported.

**Note** : Drillhole Importer table columns can be resized.

To desurvey validated component drillhole tables into a static drillhole file:

  1. Complete the **[data import](<DrillholeImporter-Import.md>)** and **[validation](<DrillholeImporter-Validate.md>)** stages of **Drillhole Importer** and display the **Desurvey** screen.
  2. By default, alphanumeric field widths are set to the width of the widest value. To override this and set a new field width, check the appropriate attribute(s) and set a new **Width**.
  3. Select the Drillholes object to host the newly desurveyed data. By default, data is saved to an object called "-new_drilholes-" but you can change this to any name you like.
  4. Specify how the desurveying is performed, using desurveying **Options**.
     * Choose the Desurvey method:

       * Select Radius of curvature to use a curved-hole interpretation using spherical arcs when creating drillholes.

       * Choose Straight line segment to assign a given direction to a length of hole both above and below each sample measurement, half-way to the next higher or lower measurement. This method still does not account for the real curvature of the hole.

See [Drillhole Representation](<Drillhole%20Representation%20in%20Studio.md>).

     * Decide if you want to Add samples for each survey record. When a hole sample is desurveyed the survey data (azimuth and dip) of the sample is used to locate the sample centre point in space. A desurveyed drillhole file contains a set of samples each with a calculated center point in XYZ world space.
       * Sometimes raw drillhole data tables to be desurveyed may contain more than one survey record within one sample, each with different azimuth and dips. Since a sample is by definition a straight line its location in space cannot be calculated using more than one survey record. If **checked** , desurveying will automatically divide up samples where more than one survey records lie within a sample.

The samples are split in half until only one survey record lies within each sample. Therefore many samples may be created. This will cause extra samples to be created so that no sample contains more than one survey record within its FROM and TO values. For no extra samples to be created this option should be unchecked..

       * If **unchecked** and a sample does contain more than one survey record not all survey records will be taken into account. Traditionally this has been resolved by first compositing the samples to reduce their lengths. 

     * Choose whether to **Include survey direction from collar table** , that is, to include dip and azimuth data from the collars table in the desurveying process.

     * Choose whether to Include sample end coordinates:

       * **Check** to include the X, Y and Z coordinates of the start and end of each sample in the desurveyed output file. Fields XSTART, YSTART, ZSTART, XEND, YEND and ZEND are created in the output file.

       * **Uncheck** to not output coordinate fields to the desurveyed file.

     * Choose the dip convention for the hole using **Positive dip down**.

       * If **checked** , positive dip values will represent downward dipping, down the hole. This is the default setting.

       * If **unchecked** dip values will represent an upwards dip.

     * Choose whether to **Fill absent intervals**.

       * If **checked** , the output file will include a record for every missing FROM / TO interval in the input sample files. The grades will all be set to absent data.

       * If **unchecked** the output file will not include FROM / TO intervals that were missing from the input sample files.

     * Click **OK** to return to the **Drillhole Importer** screen.

  5. Decide if existing drillhole data in the selected object is retained, using Retain existing drillholes. If checked, existing data is appended, otherwise a new data object is generated.
  6. Choose how a legend is applied to the generated drillhole data:

     * If Use default template for setting drillhole colour legend is **checked** , the default 3D template for the drillhole data type in your project is used to manage which legend is used for colouring in the 3D window(s).

     * If Use default template for setting drillhole colour legend is **unchecked** , pick an attribute from the **Colour Legend** list. The attributes listed here are those where the **Create Legend** option was checked on the **[Import](<DrillholeImporter-Import.md>)** screen. The selected attribute determines the colour legend for the generated drillholes.

**Note** : the **Use default template for setting drillhole colour legend** option is only available if a default template has been assigned to the [Drillholes](<Drillhole%20Representation%20in%20Studio.md>) data type. You do this using the **[Drillholes Properties](<../VR_Help/3D_Templates.md>)** screen (**Templates** tab).

  7. Click **Generate Drillholes** to perform desurveying using the HOLES3D process.

An **Import summary** displays on the right. If errors occurred during desurveying, they are listed here. 

Related topics and activities

  * [Drillhole Importer](<DrillholeImporter-screen.md>)
  * [Import and Map Data](<DrillholeImporter-Import.md>)
  * [Validate Imported Drillhole Tables](<DrillholeImporter-Validate.md>)
  * [Drillhole Validation Errors](<DrillholeImporter-Errors.md>)
  * [3D Display Templates](<../VR_Help/3D_Templates.md>)
  * [Drillhole Representation](<Drillhole%20Representation%20in%20Studio.md>)