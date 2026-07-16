# Calculate Geotechnical Attributes

To access this screen:

  *   *   * Using the **[command line](<Command_Toolbar.md>)** , enter "calculate-geotechnical-attributes"

  *   * Use the quick key combination "cga".

  *   * Display the **[Find Command](<findcommand.md>)** screen, locate **calculate-geotechnical-attributes** and click **Run**.

Use this screen to calculate the average joint spacing, fracture frequency and the Rock Quality Designation (RQD) of selected plane data. The primary purpose of this assessment is to determine, for loaded **[plane](<Studio%203%20Planes%20Overview.md>)** data, the properties of a potential failure domain and guard against structurally risky fieldwork.

To calculate geotechnical attributes of loaded plane data:

  1. Using the **Selected Objects** list, pick one or more loaded plane objects representing structural contacts.

**Note** : Previously selected plane objects will already show checked boxes, whilst if an object has only part of its planes selected, a grey check box is shown instead.

Click **All** or **None** to select or deselect all listed plane objects.

  2. Use the Group by Field list to pick an attribute to act as a key field value when calculating results, or select _None_ to calculate geotechnical attributes across all selected planes. 

**Note** : If you select a key field, it must be present in all selected plane objects.

  3. Define the **Output** results you need to create, using the following options:

     * Output window: Check to display the calculated results in the [Output](<Output%20Control%20Bar%20Overview.md>) control bar.

     * Histogram: Check to create a histogram chart sheet in the Plots window. See [Creating and Editing Histograms](<../PLOTS_LOGS/Chart_Histogram.md>).

     * Output to Point Data Object: Check to output a points data object and enable the following options:

       * **Current Object** or New Object: Output to the current points object or create new object. If no points object exists, either option creates one.

       * **Column Mapping** : Choose the name of the output points data attribute that will store particular geotechnical results:

         * **Average Spacing** : The average fracture spacing throughout the selected data.

         * Fracture Frequency: Record the fracture frequency (the number of fractures occurring within a unit length) within this attribute.

         * **RQD** : Record the Rock Quality Designation within this attribute. RQD is the degree of jointing or fracture in a rock mass measured as a percentage.

Related topics and activities

  * [calculate-geotechnical-attributes](<../command_help/calculate-geotechnical-attributes.md>) (command)

  * [calculate-structural-orientation](<../command_help/calculate-structural-orientations.md>) (command)