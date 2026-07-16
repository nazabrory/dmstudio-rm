# Reconstruct Wireframe from Points

### To access this command:

  * **Explicit** ribbon **> > Automatic >> From Points**.

  * Using the **[command line](<Command_Toolbar.md>)** , enter "wireframe-create-from-points"

  * Use the quick key combination "cwp".

  * Display the **[Find Command](<findcommand.md>)** screen, locate **wireframe-create-from-points** and click **Run**.

Reconstruct wireframe volumes implied by point cloud data. Typically, this data comes from field data capture devices such as drones and cavity monitoring systems and has been converted to the Datamine format.

**Note** : this command is intended to reconstruct wireframe volumes, although it can also be used to produce partly open structures, such as a drive finger, for example.

The **Point Cloud Reconstruction** console provides everything you need to define your input data, how to interpret it and ultimately generate a wireframe volume output.

There are many methods available to surface point data, and your choice of method is determined by the nature of your input data, your appetite for accuracy and the requirements for your output wireframes, and typically, how they will used in downstream processes. For example, if you are generating a volume for grade and tonnage evaluation, you will want it to be 'watertight', whereas if you are generating visual reference data for a field or development report, this may not be necessary.

A scenario-based approach is used, meaning you can set up one or more surfacing scenarios to accommodate multiple domains or operating situations. Scenarios are saved with the project but can also be exported for use in other projects. 

Commonly, it is the data capture device that determines some (or all) surfacing requirements. Where a consistent capture device is used, with similarly regular point cloud generation settings (supported by a standard data cleanup workflow), a scenario can relate to a particular operational configuration. That said, point cloud reconstruction is also sensitive to data density, implied geometry and what 'trends' are exhibited by the data. A scan of multiple development drives in a box and pillar arrangement will contain multiple trends, and will probably be more easily surfacable with a tessellation technique instead of a probabilistic Gaussian approach, for example.

Point reconstruction can be an iterative process; fine-tuning surfacing parameters to gradually improve the result. The scenario approach means that a previously successful run can be used as a good starting point for another project based on similar inputs.

See [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>).

## Point Reconstruction Methods  

The Point Cloud Reconstruction console asks you to choose your surfacing method at the start of the scenario. Whilst it's impossible to specify with certainty the ideal method for all input data conditions, some are more adept in certain situations. 

For more information on the available methods, see [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>).

For more information on the Point Reconstruction Console, including activities and further examples, see [Point Cloud Reconstruction](<point-reconstruction.md>).

Related topics and activities

  * [Point Cloud Reconstruction](<point-reconstruction.md>)

  * [Point Reconstruction Console](<point-reconstruction-console.md>)

  * [Create Scenario](<point-reconstruction-create-scenario-screen.md>)

  * [Define Scenario](<point-reconstruction-define-scenario-screen.md>)

  * [Subsample](<point-reconstruction-subsample-screen.md>)

  * [Calculate Normals](<point-reconstruction-normals-screen.md>)

  * [Calculate Outputs](<point-reconstruction-outputs-screen.md>)

  * [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>)