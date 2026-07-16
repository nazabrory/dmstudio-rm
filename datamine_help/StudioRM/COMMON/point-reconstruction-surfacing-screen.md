# Configure Surfacing

To access this panel:

  * Display the [Point Reconstruction Console](<point-reconstruction-console.md>) and select the **Configure Surfacing** panel. This panel is only accessible if an appropriate reconstruction method is chosen.

If surfacing point cloud data using a tesselation method such as **Watertight** or **Face Advance** , this panel is not accessible as no additional surfacing parameters are required.

If using the **Ball Pivot** method, this panel provides as single parameter field to define the radius of the sphere used to 'roll' across the point clouds and generate a surface. 

**Poisson** and **SSD** construction methods require identical input surfacing parameters. These parameters control how a surface is interpolated between points along an established trend (as implied by the point normals). How surface triangles are generated in this case depends on the resolution of a theoretical grid of cells in 3D space, the number of point samples that can contribute to the formation of surface data and the 'power' of each point with regards to its priority in establishing a surface location.

The **Balanced** method is similar to both Poisson and SSD methods, but takes a slight different approach to surface creation, although it also uses normal directional information to form the surface represented by the point cloud. In this method, a search radius is used to determine the overall orientation of surface data. You can also automatically close gaps in surface data using a threshold area. This method also provides control over performance vs. quality and the density of wireframe triangles in the output mesh.

See [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>) for further guidance on how each method uses surfacing parameters.

Activity Steps:

  1. Display the [Point Reconstruction Console](<point-reconstruction-console.md>).
  2. Create, load or import a scenario using the [Create Scenario](<point-reconstruction-create-scenario-screen.md>) panel.
  3. Choose a suitable reconstruction method using the [Define Scenario](<point-reconstruction-define-scenario-screen.md>) panel. Ensure **Subsample input points** is checked.
  4. If required, **[Subsample](<point-reconstruction-subsample-screen.md>)** the input point cloud.
  5. If required for the chosen reconstruction method, specify surface normal calculation parameters using the [Calculate Normals](<point-reconstruction-normals-screen.md>) panel.

  6. If using the Ball Pivot reconstruction method:

     1. Choose the **Ball radius** to use when surfacing. A higher value means a larger sphere and a more generalized surface. The inter-point distance displayed on the **[Define Scenario](<point-reconstruction-define-scenario-screen.md>)** panel can help choose a radius value; generally a radius value that is lower than half the mean inter-point distance can cause incomplete surface generation (the ball falls between the points).

  7. If using the Poisson or SSD reconstruction methods:

     1. Select how a 3D grid of cells is used to construct the surface wireframe. Each cell of the grid represents a wireframe surface vertex, so a tighter grid means more points. You can set the resolution of the grid either by setting a Tree depth (also known as an 'octree depth' and very similar to the **Cubic Subdivision** method used to **[subsample](<point-reconstruction-subsample-screen.md>)**) or by setting the **Smallest cell width** that is permitted.

        * If setting the **Tree depth** , choose the number of binary subdivisions are performed on the hull of all point data, with each subdivision increasing the granularity of the grid exponentially. A higher number gives a greater resolution but may be slower and use more system resources. 

**Tip** : Typically, a Tree depth value between 4 and 24 is expected.

        * If defining the **Smallest cell width** , enter a positive 2D distance to constrain the number of cuboid subdivisions applied to create the final 3D octree grid so that no cells with a plan width below that value are allowed. This is similar to the subsampling option **Point Distance** , but is instead used to generate the 3D grid 'canvas' from which a wireframe will be constructed.

     2. Choose the minimum number of samples points that should fall within an octree node (cell) whilst the grid is adapted to sampling density. For noise-free samples, **Number of samples per node** values in the range 1-5 can be used. For more noisy input data, larger values in the range 15-20 may be more effective to reduce noise across the data before surfacing.

     3. Set the **Point weight** for each point in the octree grid. This value denotes the importance of the location of points within the screened Poisson equation (used for both **Poisson** and **SSD** surface calculations). It can be considered as the 'power' of each data point within the calculated grid when calculating where surface data is positioned and oriented.

  8. Continue to the **[Calculate Outputs](<point-reconstruction-outputs-screen.md>)** panel.

To import or export data to transfer settings between projects and systems:

  * To export the current scenario's settings, click **Export Settings** and specify an .xml file name. This file can be shared with other point reconstruction users.

  * To import previously exported settings, click **Import Settings** and select a point reconstruction .xml file.

The **Point Reconstruction Console** settings update to reflect the imported information.

Related topics and activities

  * [Point Cloud Reconstruction](<point-reconstruction.md>)

  * [Point Reconstruction Console](<point-reconstruction-console.md>)

  * [Resolve Duplicate Scenario](<point-reconstruction-import-duplicate-scenario.md>)

  * [Create Scenario](<point-reconstruction-create-scenario-screen.md>)

  * [Define Scenario](<point-reconstruction-define-scenario-screen.md>)

  * [Subsample](<point-reconstruction-subsample-screen.md>)

  * [Calculate Normals](<point-reconstruction-normals-screen.md>)

  * [Calculate Outputs](<point-reconstruction-outputs-screen.md>)

  * [Point Reconstruction Methods and Tips](<point-reconstruction-methods.md>)

  * [PTCLD2WF Process](<../Process_Help_XML/ptcld2wf.md>)

  * [wireframe-create-from-points ("cwp")](<../command_help/wireframe-create-from-points.md>)