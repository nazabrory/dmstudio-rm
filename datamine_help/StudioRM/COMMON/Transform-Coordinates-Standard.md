# Standard Coordinate Transformation

To access the Transform Coordinates screen:

  * **Data** ribbon **> > Transform >> Geographic**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "transform-coordinates"

  * Use the quick key combination "tco".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **transform-coordinates** and click **Run**.

Transform a spatial data file's coordinates from one system to another using industry-standard coordinate systems, using the [Transform Coordinates](<Transform_Coordinates_Dialog.md>) screen.

**Note** : you can also define a custom transformation.

The **Transform Coordinates** screen handles numerous types of coordinate representations, including cartographic and geodetic transformations. You can also **[automate](<Transform-Coordinates-Automation.md>)** this function and set up a **[custom](<Transform-Coordinates-Custom.md>)** transformation.

If spatial data coordinates are being transformed for the first time, and you are unsure of what **Target Coordinate System** to use so that the data is displayed in its expected orientation, remember that your application uses a general XYZ cartesian coordinate system where:

  * X coordinates increase towards the East

  * Y coordinates increase towards the North

  * Z coordinates increase upwards.

Before coordinate transformation is performed, the input file and parameters are checked, and if the transformation cannot be completed with the specified inputs, a message displays indicating failure. This may be due to coordinate system not being recognised, or coordinates not being compatible with the coordinate systems selected.

**Tip** : click **Restore** to reinstate settings used in a previous coordinate transformation.

To perform a standard coordinate transformation:

  1. Define input and output files. See [Transform Coordinates](<Transform_Coordinates_Dialog.md>).

  2. Select the **Standard** tab.

  3. For the **Source Coordinate System** , you can either:

     * Pick a **Key** using the browse button to display the [Coordinate System Selection](<CoordinateSystemSelection_Dialog.md>) screen. 

**Note** : the following Well Known Text (WKT) Keys are support by your application: G, ESRI, IGNF, OGC.

     * Enable **WKT** to define the coordinate system using a Well Known Text transformation string. 

**Tip** : edit a standard **Key** by selecting it first, then selecting the **WKT** option to modify the prepared text. This can help to ensure the correct syntax is used.

  4. Choose your **Target Coordinate System** using either **Key** or **WKT** options.

  5. Click **OK** to transform your **Input File** data to the **Output File**. 

Related topics and activities

  * [Transform Coordinates](<Transform_Coordinates_Dialog.md>)

  * [Custom Coordinate Transformation](<Transform-Coordinates-Custom.md>)

  * [Coordinate Systems](<Coordinate%20Systems%20Concept.md>)

  * [Coordinate System Selection](<CRSBrowserDlg.md>)

  * [Transform Coordinates Automation](<Transform-Coordinates-Automation.md>)