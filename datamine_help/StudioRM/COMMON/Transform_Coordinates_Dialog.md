# Transform Coordinates

To access this screen:

  * **Data** ribbon **> > Transform >> Geographic**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "transform-coordinates"

  * Use the quick key combination "tco".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **transform-coordinates** and click **Run**.

Transform a spatial data file's coordinates from one system to another using industry-standard coordinate systems, or your own conversion logic.

The **Transform Coordinates** console handles numerous types of coordinate representations, including cartographic and geodetic transformations. 

Before coordinate transformation is performed, the input file and parameters are checked, and if the transformation cannot be completed with the specified inputs, a message displays indicating failure. This may be due to coordinate system not being recognised, or coordinates not being compatible with the coordinate systems selected.

You can also **[automate](<Transform-Coordinates-Automation.md>)** this command.

**Tip** : click **Restore** to reinstate settings used in a previous coordinate transformation.

To configure coordinate transformation:

  1. Choose your input **Filename**. Use the browse button to pick any file on disk and click **Save**.

If coordinate fields are detected in the file, they are listed automatically in the coordinate fields below.

  2. If the automatically-assigned coordinate fields for **X Column** , **Y Column** and **Z Column** are inaccurate, pick alternatives. All numeric fields detected in the input file are listed.

  3. Choose your output **Filename** location and name using the file browser provided.

**Note** : the input file is copied to the output file, with the values in the specific X,Y and Z columns replaced by the transformed equivalent.

  4. Define parameters for either:

     * A **Standard** transformation, by picking Well Known Text (WKT) keys for the **Source Coordinate System** and **Target Coordinate System**. 

See [Standard Coordinate Transformation](<Transform-Coordinates-Standard.md>).

     * A **Custom** transformation, using your own logic to transform data according to defined transitions between control points.

See [Custom Coordinate Transformation](<Transform-Coordinates-Custom.md>).

  5. Click **OK** to generate your **Output File** containing transformed coordinate fields.

Related topics and activities

  * [Standard Coordinate Transformation](<Transform-Coordinates-Standard.md>)

  * [Custom Coordinate Transformation](<Transform-Coordinates-Custom.md>)

  * [Coordinate Systems](<Coordinate%20Systems%20Concept.md>)

  * [Coordinate System Selection](<CRSBrowserDlg.md>)

  * [Transform Coordinates Automation](<Transform-Coordinates-Automation.md>)