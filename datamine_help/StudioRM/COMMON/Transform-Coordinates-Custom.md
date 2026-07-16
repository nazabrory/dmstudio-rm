# Custom Coordinate Transformation

To access the Transform Coordinates screen:

  * **Data** ribbon **> > Transform >> Geographic**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "transform-coordinates"

  * Use the quick key combination "tco".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **transform-coordinates** and click **Run**.

Transform a spatial data file's coordinates from one system to another using your own conversion logic.

A transformation instruction is defined using one or more control point pairs, representing 3D coordinate positions in both a **Source** and **Target** world. Transformations can include as many control points as you need to define the 3D transition, and you can even pick control points in 3D using any available 3D window.

Once control points have been set, **Calculate Transformation** to determine the translation, scale and rotation parameters, which can be saved for later use.

Typically, transformations of this type are used to transform data between unknown and known coordinate references, where there are known destination points for data.

**Note** : you can also transform data between two **[standard](<Transform-Coordinates-Standard.md>)** coordinate systems, and can even **[automate](<Transform-Coordinates-Automation.md>)** the standard transformation function.

To set up a custom coordinate transformation:

  1. Define input and output files. See [Transform Coordinates](<Transform_Coordinates_Dialog.md>).

  2. Select the **Custom** tab.

  3. If relevant, load untransformed and reference data into a 3D window and display it, if this helps to define the target or destination coordinate spaces.

  4. In the **Control Points** table, define a control point representing a landmark for the untransformed source data. You can do this by either entering **X** , **Y** and **Z** coordinate values yourself, or using the pick button to choose a position in a **3D** window.

**Tip** : right click to snap to loaded data, or left click to select a position on the currently active 3D section.

Defined points display in **3D**. **Source** points are shown in **green** and, by default, with a numeric index. You can change the **Label** shown on screen by adding your own.

  5. Using the same approach, define a **Target** 3D point. Again, you can either set the position manually or pick 3D points.

**Target** points display in **red** and carry the same **Label** as the **Source**.

Note: at this point, a 2D transformation can be derived. Clicking **Calculate Transformation** at this point updates the **Transformation** table below to show the translation in **X** and **Y** (no scaling or rotation occurs).

  6. Add more control points if transformation in 3 dimensions is required.

  7. Click **Calculate Transformation** to update the table below.

  8. Review the **Transformation** table and adjust the transformation parameters if you need to:

     * **Translation X/Y/Z** enter the translation distance in each major axis between **Source** and **Target** coordinate systems.

     * **Scale Factor X/Y/Z** enter the exaggeration factor applied during transformation, along each axis. This factor essentially controls the modification of the data geometry to accommodate transformation between control points.

     * **Axis 1/2/3** data may rotate during transformation. The **Axis** represents the major axis around which the **Angle** (degrees) rotation is applied (see below).

     * **Angle** for each major axis, define the rotation applied during transformation. 

  9. **Save** your transformation matrix as an external .xml file if you plan to share it with others, or other projects. Once saved, a transformation file can be **Load** ed to automatically transfer the settings to the Transformation group. This will also restore any control points that were saved.

**Note** : you can also **Restore** previous settings made in a previous session.

  10. Click **OK** to transform your Input file based on custom transformation settings.

Related topics and activities

  * [Transform Coordinates](<Transform_Coordinates_Dialog.md>)

  * [Standard Coordinate Transformation](<Transform-Coordinates-Standard.md>)

  * [Coordinate Systems](<Coordinate%20Systems%20Concept.md>)

  * [Coordinate System Selection](<CRSBrowserDlg.md>)

  * [Transform Coordinates Automation](<Transform-Coordinates-Automation.md>)