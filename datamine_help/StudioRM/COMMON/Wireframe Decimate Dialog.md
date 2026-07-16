# Decimate Wireframe

To access this screen

  * **Wireframe** ribbon **> > Operations >> Decimate**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-decimate"

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-decimate** and click **Run**.

Simplify a wireframe by reducing the number of edge and wireframe faces. 

See [Wireframe Decimation](<Wireframe%20Decimation%20Guidelines.md>).

To decimate a loaded wireframe object (open or closed volume):

  1. Define a **Wireframe Name** by typing, selecting or interactively picking a loaded wireframe object.

The number of faces detected in the selected object displays as **Face Count**.

**Note** : you cannot decimate part of an object, only entire objects.

  2. Choose a **Decimation Method** :

     * **Quadratic Decimation** the default setting and suitable for the majority of use cases, this is a relatively quick decimation method but has the potential to slightly change the wireframe geometry.

     * **Measured Decimation** a slower method but more likely to retain the precise geometry of the original wireframe.

  3. Set Reduction Targets (which controls the extent of decimation):

     1. Enable and define a Reduce By target. This simplifies the wireframe until the requested percentage reduction has been achieved although note that this target may not be reached precisely, depending on the input data provided.

     2. Check **Maximum Error** to ensure the reduction process continues until the removal of candidate vertices would produce a greater error than that specified (in world data units). In other words, this is a tolerance which limits the distance by which a face can move when a point is deleted.

**Note** : lower values may lead to increased processing times, but may be necessary where the dimensions of a design element (such as a drive finger) are relatively small.

  4. Use **Feature Preservation Weighting** options to determine what constitutes an import feature of the input wireframe and control how (or if) those features are preserved during decimation. This facility could be used to preserve bench boundaries, for example.

     1. Enter a **Feature Edge Weight** for features defined by the corresponding (following) Feature Edge Angle setting. A value of zero indicates that data qualifying as a feature has no importance and will probably be lost during decimation. Increasing this number means that those edges become increasingly less preferable for removable by the decimation algorithm. Choosing a large number (say, 99999) will ensure that detected edges are preserved, but may slow down processing, or prevent the algorithm from reaching its target reduction.

     2. Decide what is classed as a feature using the **Feature Edge Angle** limit. Angles sharper than the specified limit are treated as features and are preserved according to other weighting options.

     3. Choose how open edges are decimated, by setting a **Boundary Edge Weight**. This setting effectively determines how rigidly the outer edge (or other open edges) are preserved during decimation.

  5. Choose how you want to **Output** your data, either as an In-place update (the selected wireframe is adjusted) or as a New Object (in which case, a default object name is created, starting with a "Decimated:" prefix.

**Warning** : in-place object updates cannot be undone.

  6. Click **OK** to decimate the target wireframe.

Related topics and activities

  * [Wireframe Decimation](<Wireframe%20Decimation%20Guidelines.md>)

  * **[wireframe-decimate](<../command_help/wireframe-decimate.md>)** (command)

  * [Clean Wireframe](<Wireframe%20Clean%20Dialog.md>)

  * [Verify Wireframe](<Wireframe%20Verify%20Dialog.md>)