# gaussian-wireframe-from-points

See this command in the [**command table**](<COMMAND%20TABLE_G.md#gaussian-wireframe-from-points>).

To access this command:

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **gaussian-wireframe-from-points** and click **Run**.

  * Enter "gaussian-wireframe-from-points" into the [**Command Line.**](<../COMMON/Command_Toolbar.md>)

## Command Overview

Generate a wireframe from a point cloud data file in memory. This method is an alternate method to the one used by Studio's implicit modelling commands although may provide good results for some input data configurations.

**Note** : Although this command can be used to generate either volume or DTM surfaces, it is primarily design to generate the former. For a more focussed DTM generation command, see [dtm-create](<dtm-create.md>).

Input data will typically be scan data from aerial or underground equipment (CMS or drones) and should already be in memory as an object before you use the command. Import options are available using your Data Source Drivers, one of which is dedicated to point data import - PDAL.

Scan data can include a high number of sample points. Subsampling is recommended to improve performance of surfacing and downstream processes (modelling, reserves reporting etc.). How much or how little of your raw data is imported is determined by what you wish to achieve, the nature of the object(s) being reconstructed, hardware limitations and other contributing factors. If you decide to subsample, you will need to set the target points number that you wish to achieve (the raw number is also displayed).

Subsampling can be performed either by using a regular grid, or a declustering approach to remove more data from dense clusters of data.

Note: If duplicate points are detected in the input points file, only one of the points is added to the point cloud object.

Command Steps:

  1. Specify the input object
  2. (Optionally) subsample/decluster the incoming points to create a dataset for surfacing.
  3. Specify surfacing parameters to control continuity, hole removal, output resolution and other qualities.
  4. Create the wireframe.

Related topics and activities

  * [Point Cloud Reconstruction](<../COMMON/point-reconstruction.md>)

  * [Point Reconstruction Console](<../COMMON/point-reconstruction-console.md>)

  * [PTCLD2WF Process](<../Process_Help_XML/ptcld2wf.md>)