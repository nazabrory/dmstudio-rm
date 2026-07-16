# PTCLD2WF Process  
  
To access this process:

  * Structure ribbon  >> Create >> Point Cloud Solid

See this process in the [Command Table ](<../command_help/COMMAND%20TABLE_P.md#PTCLD2WF>).

## Process Overview

**PTCLD2WF** reconstructs surface data files from input point cloud files.

A single input points file containing surveyed point data is expected. Point density and arrangement can be uniform or irregular. Points can optionally be declustered and, if normal calculation is required, these stages can be performed independently of surfacing or as one combined operation, depending on _@RUNMODE_.

The **[Point Reconstruction Console](<../COMMON/point-reconstruction-console.md>)** provides a workflow-based approach to setting up parameters for **PTCLD2WF**. It also offers automated file loading and scenario management and access to an additional reconstruction method (you can also record **PTCLD2WF** macros if one of the supported methods is selected). Unless you require a process for your point reconstruction project, it is a recommended alternative.

**PTCLD2WF** processing involves up to 3 phases, depending on the wireframe surfacing method chosen:

  1. Input points are declustered to decrease point density and encourage a more uniform point layout. 

  2. Input point data is appended with normal information, indicating the normal direction to be considered when specific surfacing methods are used. Not all methods require point normal calculation.

Normal data can also be extracted from the input points file if it is present.

  3. A surface is interpolated between points using a combination of surface method and appropriate parameters.

In all cases, the input file is a Datamine points file and the output files are a wireframe file pair.

Note: **PTCLD2WF** parameters can be dependent on other settings. For example, @DEPTH, @WIDTH, @SAMPNODE, @PTWEIGHT and @BOUNDTYP are only used if @WFMETHOD is 1 or 2. Similarly, if @WIDTH is greater than zero, @DEPTH is not used.  
  
Another example: if @WFMETHOD is not 1, @BOUNDTYP is not used.  

## Declustering Raw Point Cloud Data

Raw point cloud data can be denser than required for a suitable surface reconstruction.

Declustering options are:

  * Random point removal (**to achieve a target** _@SSDIST_**number of points** in the declustered output file). This is _@SSMETHOD_ =1. 

**Warning** : Depending on the arrangement of your input points, random declustering can have a significant (possibly adverse) effect on your output wireframe. Where input points are generally regularly spaced in a grid pattern, random declustering can be effective, whereas if the variability of point spacing is high throughout the data, random declustering may occasionally generate undesirable results. With this subsampling option, the output wireframe will not be reliably reproducible. In cases where data inputs are highly irregular, or a reproducible wireframe output is required, @SSMETHOD 2 or 3 is recommended.  

  * To **achieve a target** _@SSDIST_**distance** between points. This is _@SSMETHOD_ =2. Subsampling performed using this method is static, that is, it will always generate the same declustered point data, given the same input data. A higher value tends to produce smaller declustered data (= fewer points).

  * To **decluster to a specific octree depth** , again provided by _@SSDIST_). This is _@SSMETHOD_ =3. A higher value tends to produce larger declustered data (= more points). This is also a static declustering method.

See [DECLUST](<declust.md>).

## Computing Point Normals

Point normal computation relies on the following parameters: _@NNEIGHBS_ and _@RADIUS_. An explanation of these parameters can be found in the table further below.

Point normal computation is only required if _@WFMETHOD_ is either 1 or 2. Surface reconstruction will not complete if either method is specified and point normal data is not available. If @WFMETHOD is anything other than 1 or 2, all point normal computation parameters are ignored.

**Note** : The **Balanced** point reconstruction method available via the [**Point Reconstruction Console**](<../COMMON/point-reconstruction-console.md>) is not powered by the PTCLD2WF process and has its own surface calculation method with additional parameters.

Point normals can be computed for any input point data, either as an independent task (_@RUNMODE=2_) or as part of the full surface reconstruction process (_@RUNMODE=4_). Alternatively, if normal data is already available for the input point cloud, _*NORMALX_ , _*NORMALY_ and _*NORMALZ_ can be mapped beforehand.

**Note** : If normal attributes are specified but a run subsequently includes normal computation (e.g. _@RUNMODE_ is either 2 or 4), computed normals will be used in preference to mapped fields.

See [Point Reconstruction Methods and Tips](<../COMMON/point-reconstruction-methods.md>).

* * *

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input point cloud data file used to create the wireframe surface. |  Input |  Yes |  Points  
  
## Output Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
**POINTS** | Output file prefix for subsampled points and points with normals. A file containing subsampled points will have an _SS suffix. Points with normals will have a _SSNORM suffix. This must be specified if _@RUNMODE_ = 1,2 or 4. | Output |  Yes, if _@RUNMODE_ =1, 2 or 4. Otherwise, no. | Points  
**WIRETR** | Output surface wireframe triangle file. | Output | Yes | Wireframe Points  
WIREPT |  Output surface wireframe point file. | Output |  Yes |  Wireframe Triangles  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X / Y / Z |  Name of X/Y/Z coordinate field in *IN. |  IN |  Yes |  Numeric |  Undefined  
NORMAL X/Y/Z |  Name of X normal field in input file IN. Only used if _@RUNMODE_ = 3 (calculate surface) |  IN |  No |  Numeric |  Undefined  
**RED** |  Name of red colour field in input file IN. Only used if @WFMETHOD is 1 or 2. |  IN |  No |  Any |  Undefined  
**GREEN** |  Name of green colour field in input file IN. Only used if @WFMETHOD is 1 or 2. |  IN |  No |  Any |  Undefined  
BLUE |  Name of blue colour field in input file IN. Only used if @WFMETHOD is 1 or 2. |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
RUNMODE |  Specify the functions for the process to execute:

  1. Generate a file containing subsampled points. This file will be generated with an _SS suffix.
  2. Generate a file containing points with normals data. This file will be generated with an _SSNORM suffix. Normals data is not used if @WFMETHOD = 3, 4 or 5. 
  3. Reconstruct a wireframe surface using the selected @WFMETHOD and parameters.
  4. Run the whole surface reconstruction process, including subsampling, normals computation and surface generation.

|  Yes |  1 |  1,4 | 1,2,3,4  
SSMETHOD |  The method to use for subsampling.

  1. Random: SSDIST specifies number of target points to be saved and subsamples using random point removal. 
  2. Spatial: SSDIST specifes a target distance between points in the subsampled set.
  3. Octree: SSDIST Resamples a cloud by replacing all the points inside each cell of the octree (at a given level of subdivision) by their gravity center.

|  Yes if _@RUNMODE_ =1 or 4, otherwise no. |  2 |  1,3 |  1,2,3  
**SSDIST** |  A parameter controlling the extent to which subsampling is performed and depends on the chosen _@SSMETHOD_. 

  * Where _@SSMETHOD_ = 1, this value represents the target number of points after resampling. 
  * If _@SSMETHOD_ =2, this value represents the target inter-sample distance after subsampling. 
  * If _@SSMETHOD_ =3, _@SSDIST_ represents the remaining cell a the centre of gravity of the octree (the level of subdivision at which the process is applied is chosen to (roughly) match the expected number of output points).

| Yes if _@RUNMODE_ =2 or 4, otherwise no. | 0.5 | Undefined | Undefined  
**NNEIGHBS** | The number of neighbours used when orienting the normals using a spanning tree. Normals are not required if _@WFMETHOD_ is 3,4 or 5. |  No unless: _@RUNMODE_ =2 or; _@RUNMODE_ =4 and _@WFMETHOD_ = 1 or 2 | Undefined | Undefined | Undefined  
RADIUS |  Where @WFMETHOD = 1 or 2: the neighborhood radius used to compute normals. The bigger the radius, the more points will be used to compute the local surface model, resulting in generally smoother normals but also in a longer process time. A value of zero will allow the program to compute a radius value automatically, based on the mean average inter-point distance. Where @WFMETHOD = 4, this represents the radius of the sphere used to generate the surface by rolling across the input points.  Not used if @WFMETHOD Is 3 or 5. | Yes if @WFMETHOD = 1, 2 or 4 | Undefined | Undefined | Undefined  
**DEPTH** |  The octree depth to be used in surface construction. A higher number gives greater resolution but will be slower and use more memory. Should ideally be between 4 and 24. Values larger than 10 are likely to be process intensive. This parameter is ignored if WIDTH is specified as greater than zero.  Not considered if @WFMETHOD 3,4 or 5. | No | Undefined | Undefined | Undefined  
**WIDTH** |  This floating point value specifies the target width of the finest level octree cells used in surface reconstruction. If set to zero then DEPTH is used to control octree size.  Not considered if @WFMETHOD 3,4 or 5. | No | Undefined | Undefined | Undefined  
**WFMETHOD** |  The method to use to construct the wireframe surface from the set of points with oriented normals. 

  1. Reconstructs a surface by solving a Poisson system (solving a 3D Laplacian system with positional value constraints).
  2. Reconstructs a surface by solving for a Smooth Signed Distance function (solving a 3D bi-Laplacian system with positional value and gradient constraints). Can be moderately more accurate than Poisson option but may also take longer.
  3. Reconstructs a surface using a Delauney triangulation method and will generally produce a watertight volume.
  4. Reconstructs a surface using a Delauney triangulation method by simulation the path of a ball rolling across the input data. 
  5. Reconstructs a surface using a fast advancing front method. It can be useful for a rapidly generated initial data preview.

| Yes | 5 | 1,5 | 1,2,3,4,5  
**SAMPNODE** |  Number of samples per node during Reconstruction. This floating point value specifies the minimum number of sample points that should fall within an octree node as the octree construction is adapted to sampling density.  For noise-free samples, small values in the range [1.0 - 5.0] can be used.  For more noisy samples, larger values in the range [15.0 - 20.0] may be needed to provide a smoother, noise-reduced, reconstruction.  Only used if @WFMETHOD is 1 or 2. | No | Undefined | Undefined | Undefined  
**PTWEIGHT** | The importance that interpolation of the point samples is given in the formulation of the screened Poisson equation. This is a floating point number. Only used if @WFMETHOD is 1 or 2. | No | Undefined | Undefined | Undefined  
  
* * *

## Example
    
    
    !START M1  
  
---  
      
    
    # - Use !LOCDBOFF to look for files outside the local folder  
      
    
    # - Use local files by deleting the next line or use !LOCDBON  
      
    
    !LOCDBOFF  
      
    
    !PTCLD2WF &IN(pointcloudCMS1),  
      
    
    &POINTS(pointsout),  
      
    
    &WIRETR(comb1tr),  
      
    
    &WIREPT(comb1pt),*X(XPT),*Y(YPT),*Z(ZPT),@RUNMODE=1.0,  
      
    
    @SSMETHOD=3.0,@SSDIST=9.0,@MODEL=2.0,@NNEIGHBS=6.0,  
      
    
    @RADIUS=1.0,@DEPTH=12.0,@WIDTH=0.05,@WFMETHOD=2.0,  
      
    
    @SAMPNODE=6.0,@PTWEIGHT=10.0  
      
    
    !END