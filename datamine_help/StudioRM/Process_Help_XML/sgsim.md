# SGSIM Process  
  
To access this process:

  * **Simulate** ribbon **> > Conditional Simulation >> Sequential Gaussian**.
  * Enter "SGIM" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SGSIM** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SGSIM>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

Create a regular grid of conditionally-simulated points using sequential gaussian simulation.

Multiple realizations (simulations) can be generated in a single run of the process. The main inputs are:

  * A sample data file (X,Y,Z and grade field), and the corresponding variogram model.
  * The definition of the output grid of points.

There is a choice of kriging methods:

  * simple kriging.

  * ordinary kriging.

  * simple kriging with a locally varying mean.

  * kriging with an external drift.

  * collocated cokriging with one secondary grade.

The outputs are:

  * A points file (**XPT** , **YPT** , **ZPT** , grade and realization number) containing the simulated points.

  * A block model file. This contains the same information as the points file, except that each realization is a separate field in the model. It provides an alternative way of viewing the results.

  * Output file for the transformation table. This contains the grade field **GRADE** from the **IN** sample file, and the field **TRANDATA** , giving the transformed value. The file is sorted by **GRADE**.

  * Output statistics table giving statistics for the input sample data, and the output simulated values.

A statistical analysis of the simulated points can then be carried out with process [CSMODEL](<csmodel.md>). The [CSMODEL](<csmodel.md>) process also includes the option to average simulated points over a parent cell. The process is based on the GSLIB code for sequential gaussian simulation (sgsim).

**Note** : For details of this method refer to the following resource: GSLIB. Geostatistical Software Library and User's Guide by Clayton V.Deutsch and Andre G.Journel, published by Oxford University Press, Second Edition, 1998\. ISBN 0-19-510015-8.

There are some differences between Datamine and GSLIB conventions. However, unless otherwise stated, Datamine conventions are used here. Where required these are converted to GSLIB conventions by the process.

### Define the Grid

The grid of points can be defined in one of three ways:

  1. By specifying an empty prototype model, and parameters **XPPPC** , **YPPPC** , **ZPPPC**. A set of points is created for every parent cell where the number of points per parent cell is defined by the parameters **XPPPC** , **YPPPC** , **ZPPPC**. In effect the parameters define the subcell splitting where each simulated point corresponds to a subcell centre.

  2. By specifying a prototype model containing cells and subcells, and parameters **XPPPC** , **YPPPC** , **ZPPPC**. This is similar to option 1 except that points are only created for those parent cells that contain one or more subcells. A full set of points is always created for each parent cell.

  3. By specifying the parameters **XMIN** , **XSIZE** , **NX** , **YMIN** , **YSIZE** , **NY** , **ZMIN** , **ZSIZE** , **NZ**. Note that **XMIN** defines the location of the point with the minimum X value ie the centre of the corresponding subcell, not the model origin. **XSIZE** defines the spacing between grid points and **NX** defines the total number of grid points. The parameters **XPPPC** , **YPPPC** , **ZPPPC** then define the number of points per parent cell in the output model containing the simulated points. The values of all 12 parameters are stored as implicit fields in the output **POINTS** file, so that they can be accessed by subsequent processes (eg **CSMODEL**).

A simulated value is calculated for each grid point. If there is insufficient data within the search volume then an absent data value is assigned.

### Input Sample File &IN

The input sample data file includes the coordinate fields **X** , **Y** , **Z** and the grade field **GRADE**. The **GRADE** field may contain either the original sample values or the normal score values, depending on parameter **TRANTYPE**. Normal score values can be calculated using process **NSCORE**. 

The IN file may also include a declustering weights field **DCWGT** and a secondary field **SECFLD1**. The declustering weights are used to adjust the sample histogram. The contents of the secondary field depend on the value of parameter **KTYPE**.

### Input Variogram Parameter File &VMODPARM

The input variogram model should be for the normal scores. ie the sample data should have been normalized (process **[NSCORE](<nscore.md>)**) before the variogram was calculated.

The Co and Ci values are normalized automatically by the process ie they are divided by (Co + ΣCi) so that the sill is 1.

The three rotations defining the orientation of the ellipsoid of ranges must be in the order:

  1. Around the Z axis (azimuth rotation)
  2. Around the X axis (dip rotation)
  3. Around the Y axis (plunge rotation)

Therefore, in the input variogram model parameter file (VMODPARM) the values of the VAXIS fields must be:

  * VAXIS1 = 3 (Z)
  * VAXIS2 = 1 (X)
  * VAXIS3 = 2 (Y)

**Note** : The **[ROTORDER](<rotorder.md>)** process can be used to convert to the 3 (**Z**), 1 (**X**), 2 (**Y**) rotation angle convention.

### Input Secondary File &SECFILE

The input secondary file is required if the Kriging Type (@**KTYPE**) = 2, 3 or 4. Its content depends on the value of @**KTYPE** as follows:

2\. the locally varying mean for Simple Kriging  
3\. the drift variable when kriging with an external drift  
4\. the secondary grade for Collocated Cokriging

The secondary file must be a block model file with a cell or subcell and data value for each point to be simulated. The secondary field must not include absent data values.  
  
If the grid of simulated points is defined by the &**PROTO** file and the file does not contain any records then the &**SECFILE** file should have the same model parameters (**XMORIG** , **XINC** , **NX** , etc) as the &**PROTO** file and should have subcells as defined by parameters by **XPPPC** , **YPPPC** , **ZPPPC** , at every possible location.  
  
If the &**PROTO** file contains records then the &**SECFILE** file must still have the same model parameters and subcells defined by parameters **XPPPC** , **YPPPC** , **ZPPPC** . However the subcells must only cover a 3D rectangular volume as defined by the minimum and maximum parent cell in each of the X, Y and Z directions.  
  
If the grid of simulated points is defined by parameters **XMIN** , **XSIZE** , **NX** etc then the &**SECFILE** model must include a cell or subcell, and data value, at every grid location. The model parameters do not matter as long as there is a cell or subcell at all grid points.

#### Search Volume

As for the variogram parameters, the three rotations for the search volume must be in the order around Z, around X, then around Y.

### Output Points File POINTS

The output points file contains the simulated points, sorted on **XPT** , **YPT** , **ZPT**. As well as the coordinate fields **XPT** , **YPT** , **ZPT** the file will contain the simulated value **GRADE** and field **SIMNUM** giving the simulation (realization) number. This is an integer, starting at 1, with a maximum of **NSIM**.

The file also contains 12 implicit field whose default values define the regular grid of simulated points, which are stored in terms of the equivalent block model. These fields will be used subsequently by the [CSMODEL](<csmodel.md>) process for averaging points into block values and creating block models.

Field | Stored | Description  
---|---|---  
XPT |  Yes |  X coordinate of simulated point  
YPT |  Yes |  Y coordinate of simulated point  
ZPT |  Yes |  Z coordinate of simulated point  
SIMNUM |  Yes |  Realization number  
{grade} |  Yes |  Simulated value  
XPPPC |  No |  Number of points per parent cell in the X direction  
YPPPC |  No |  Number of points per parent cell in the Y direction  
ZPPPC |  No |  Number of points per parent cell in the Z direction  
XMORIG1 |  No |  X origin of model  
YMORIG1 |  No |  Y origin of model  
ZMORIG1 |  No |  Z origin of model  
XINC1 |  No |  Parent cell size in the X direction  
YINC1 |  No |  Parent cell size in the Y direction  
ZINC1 |  No |  Parent cell size in the Z direction  
NX1 |  No |  Number of parent cells in the X direction  
NY1 |  No |  Number of parent cells in the Y direction  
NZ1 |  No |  Number of parent cells in the Z direction  
  
**Note** : The XMORIG1, YMORIG1, and ZMORIG1 field values define the origin of the block model. These are different from the XMIN, YMIN, and ZMIN parameters which define the minimum coordinates of a subcell.

### Output Model File &MODEL

The output block model file contains the simulated points. This is the same data as the **POINTS** file, but in block model format. If multiple realizations have been selected (**NSIM** greater than 1) then the field name for each realization will be **SIM1** , **SIM2** , **SIM3** , etc.

If the grid of simulated points is defined by the **PROTO** file then the **MODEL** file will have the same model parameters (**XMORIG** , **XINC** , **NX** , and so on); otherwise the model parameters will be based on parameters **XMIN** , **XSIZE** , **NX** , and so on. Note that **XMIN** is the X coordinate of the location of the point with the minimum X value and so is half a cell displaced from the model origin.

Field |  Stored |  Description  
---|---|---  
IJK |  Yes |  IJK index  
XC |  Yes |  X coordinate of centre of parent cell  
YC |  Yes |  Y coordinate of centre of parent cell  
ZC |  Yes |  Z coordinate of centre of parent cell  
SIM1 |  Yes |  1st simulated value  
SIM2 |  Yes |  2nd simulated value  
.... |  .... |  ....  
SIMn |  Yes |  nth simulated value  
XINC |  Yes |  Parent cell size in the X direction  
YINC |  Yes |  Parent cell size in the Y direction  
ZINC |  Yes |  Parent cell size in the Z direction  
XMORIG |  No |  X origin of model  
YMORIG |  No |  Y origin of model  
ZMORIG |  No |  Z origin of model  
NX |  No |  Number of parent cells in the X direction  
NY |  No |  Number of parent cells in the Y direction  
NZ |  No |  Number of parent cells in the Z direction  
  
### Program Limits

Maximum number of: |  Value  
---|---  
Samples in input IN file |  500,000  
Simulated points in X direction |  See "Maximum number of points, below"  
Simulated points in Y direction |  See below  
Simulated points in Z direction |  See below  
Points in X direction in covariance table |  71  
Points in Y direction in covariance table |  71  
Points in Z direction in covariance table |  21  
Superblock nodes in X direction |  21  
Superblock nodes in Y direction |  21  
Superblock nodes in Z direction |  11  
Previously simulated nodes to use |  48  
Data for one simulation |  48  
Variogram structures |  4  
Characters in full path name of the project file |  256  
Realizations in the output model |  200  
  
##### Maximum Number of Points

If the 3D grid of points is defined by parameters **NX** , **NY** and **NZ** and **NSIM** is the number of simulations then the maximum number of simulated points is:
    
    
    NX*NY*NZ*NSIM <= 2,000,000,000. 

If the 3D grid of points is defined by the input prototype model **PROTO** then the corresponding limit is:
    
    
     NX*XPPPC * NY*YPPPC * NZ*ZPPPC * NSIM <= 2,000,000,000

where NX is the number of parent cells in X in the **PROTO** model and **XPPPC** is the parameter defining the number of points per parent cell in X, etc. Whether or not the **PROTO** model includes cells does not affect the calculation.

### Command Prompt Window

The Command Prompt window is opened during the processing and contains progress information for the run of the sgsim executable. You can left click the mouse in the window to stop it scrolling, and then right click to start it again. The window is closed automatically when the sgsim executable finishes.

### System Files

_sgsdbg.txt |  Debug output. Contents depend on the value of the DBGLEVEL parameter  
---|---  
_sgslog.txt |  Log file. Only useful if there is a problem.  
_sgs_*.txt |  Temporary system files. These will be deleted if the process terminates cleanly.   
_sp*.dm |  Temporary Datamine files. These will be deleted if the process terminates cleanly.  
  
All files matching the template _sgs_*.txt and _sp*.dm will be deleted as the process terminates. Therefore you should not use any of these file names.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input sample data file. This must include the coordinate fields X , Y , Z and the grade field GRADE . It may also include the declustering weights field DCWGT and the secondary field SECFLD1 . If an IN |  Input |  No |  Table  
VMODPARM |  Variogram model parameter file. Each record in this file defines a variogram model type and its parameters. |  Input |  Yes |  Variogram - Model  
PROTO |  Input prototype model file to define the regular grid for the simulated points. If the PROTO file contains records then simulated points are created for all parent cells that contain at least one subcell. If the PROTO file does not contain any records then simulated points are created for all parent cells. The number of simulated points per parent cell is defined by the parameters XPPPC , YPPPC , ZPPPC . If the file is not specified then the grid is defined by the parameters XMIN , XSIZE , NX etc. |  Input |  No |  Block Model Prototype  
REFDIST |  Input reference distribution to define required transformation. As well as specifying the file, parameter TRANTYPE must be set to 2. The file must include the field REFGRADE , to define the reference distribution, and may also include the field REFWGT to define declustering weights. |  Input |  No |  Table  
SECFILE |  Secondary file, required if KTYPE = 2,3 or 4. This contains the locally varying mean ( KTYPE =2), the external drift variable ( KTYPE =3) or the secondary variable for collocated cokriging ( KTYPE =4). This must be a block model file with a cell or subcell (and data value) at each simulated point. - if the grid of simulated points is defined by the PROTO file and the file does not contain any records then the SECFILE file should have the same model parameters (XMORIG, XINC, NX, etc) as the PROTO file and should have subcells as defined by parameters XPPPC , YPPPC , ZPPPC at every possible location. - if the PROTO file contains records then the SECFILE file must still have the same model parameters and subcells defined by parameters XPPPC , YPPPC , ZPPPC . However the subcells need only cover a 3D rectangular volume as defined by the minimum and maximum parent cell in each of the X, Y and Z directions. - if the grid of simulated points is defined by parameters XMIN , XSIZE , NX etc then the SECFILE model must include a cell or subcell, and data value, at every grid location. The model parameters do not matter as long as there is a cell or subcell at all grid points. |  Input |  No |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
POINTS |  Output |  Yes |  Point Data |  Output points file containing simulated points. As well as the coordinate fields XPT, YPT, ZPT the file will contain the simulated value GRADE and field SIMNUM giving the simulation (realization) number. This is an integer, starting at 1, with a maximum of NSIM .  
MODEL |  Output |  No |  Block Model |  Output block model file containing simulated points. This contains the same data as the POINTS file, but in block model format. If multiple realizations have been selected ( NSIM greater than 1) then the field name for each realization will be SIM1, SIM2, SIM3, etc. A maximum of 44 realizations are allowed in the MODEL file in the single precision version of your project, or 200 in the double precision version. If the grid of simulated points is defined by the PROTO file then the MODEL file will have the same model parameters (XMORIG, XINC, NX, etc); otherwise the model parameters will be based on parameters XMIN , XSIZE , NX etc.  
TRANDIST |  Output |  No |  Table |  Output file for the transformation table. This will contain the grade field GRADE from the IN sample file and the field TRANDATA giving the transformed value. The file will be sorted by GRADE .  
STAT_TBL |  Output |  No |  Table |  Output statistics table giving statistics for the input sample data and the output simulated values.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X coordinate of the GRADE field in the IN sample file. |  IN |  Yes |  Numeric |  X  
Y |  Y coordinate of the GRADE field in the IN sample file. |  IN |  Yes |  Numeric |  Y  
Z |  Z coordinate of the GRADE field in the IN sample file. |  IN |  Yes |  Numeric |  Z  
GRADE |  Field in the IN sample file defining the grade to be simulated. This may contain either the original sample values or the normal score values, depending on parameter TRANTYPE . |  IN |  Yes |  Numeric |  Undefined  
DCWGT |  Optional declustering weights field in the IN sample file. |  IN |  No |  Numeric |  Undefined  
SECFLD1 |  Optional secondary field in the IN sample file. The contents of this field depend on the value of parameter KTYPE . |  IN |  No |  Numeric |  Undefined  
SECFLD2 |  Field in secondary file SECFILE . This is required if KTYPE = 2,3 or 4. The field contains the locally varying mean ( KTYPE =2), the external drift variable ( KTYPE =3) or the secondary variable for collocated cokriging ( KTYPE =4) . If @KTYPE=4 *SECFLD2 must be untransformed. |  SECFILE |  No |  Numeric |  Undefined  
REFGRADE |  Reference grade field, defining the reference distribution, in the REFDIST file. |  REFDIST |  No |  Numeric |  Undefined  
REFWGT |  Optional reference weight field, defining declustering weights, in the REFDIST file. |  REFDIST |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MINGRADE |  Minimum GRADE value input from the IN sample file. Values less than the minimum are ignored. |  No |  0 |  Undefined |  Undefined  
MAXGRADE |  Maximum GRADE value input from the IN sample file. Values greater than the maximum are ignored. |  No |  Undefined |  Undefined |  Undefined  
TRANTYPE |  Transform data option: 0 = no transformation; the field GRADE in the IN sample file is assumed to have a standard normal distribution, and the simulated value GRADE in the output POINTS file will also be untransformed. 1 = transform the GRADE values using the standard normal distribution. 2 = transform the GRADE values using the distribution defined in the input file REFDIST . |  No |  1 |  0,2 |  0,1,2  
MINSIMGR |  Minimum simulated grade value. This is used to restrict values in the back-transformation process. |  No |  0 |  Undefined |  Undefined  
MAXSIMGR |  Maximum simulated grade value. This is used to restrict values in the back-transformation process. |  No |  999999 |  Undefined |  Undefined  
LOTAIL |  Back-transformation method in the lower tail of the distribution to a minimum grade of MINSIMGR . 1 = Linear interpolation. 2 = Power model interpolation. The power used is defined by LOPAR . |  No |  1 |  1,2 |  1,2  
LOPAR |  Power parameter used in back-transformation of grades in the lower tail of the distribution to a minimum of MINSIMGR . LOTAIL must be set to 2. |  No |  1 |  0,+ |  Undefined  
UPTAIL |  Back-transformation method in the upper tail of the distribution to a maximum grade of MAXSIMGR . 1 = Linear interpolation. 2 = Power model interpolation. The power used is defined by UPPAR . 4 = Hyperbolic model extrapolation using power parameter defined by UPPAR . |  No |  1 |  1,4 |  1,2,4  
UPPAR |  Power parameter used in back-transformation of grades in the upper tail of the distribution to a maximum of MAXSIMGR . UPTAIL must be set to 2 or 4. |  No |  1 |  0,+ |  Undefined  
NSIM |  Number of realizations to generate. If a MODEL file has been selected then the maximum number of realizations is 44 for the single precision version of Datamine Studio packages or 200 for the double precision version. If a MODEL file has not been selected then there is no limit on the maximum number of realizations. |  No |  1 |  1,+ |  Undefined  
XPPPC |  The number of simulated points per parent cell to be created in the X direction in the output MODEL file. This corresponds to the number of subcells per parent cell in the X direction. The value of parameter XPPPC is also stored as the default value of implicit field XPPPC in the output POINTS file so that it can be accessed by subsequent processes eg CSMODEL. |  No |  1 |  Undefined |  Undefined  
YPPPC |  The number of simulated points per parent cell to be created in theY direction in the output MODEL file. This corresponds to the number of subcells per parent cell in the Y direction. The value of parameter YPPPC is also stored as the default value of implicit field YPPPC in the output POINTS file so that it can be accessed by subsequent processes eg CSMODEL. |  No |  1 |  Undefined |  Undefined  
ZPPPC |  The number of simulated points per parent cell to be created in the Z direction in the output MODEL file. This corresponds to the number of subcells per parent cell in the Z direction. The value of parameter ZPPPC is also stored as the default value of implicit field ZPPPC in the output POINTS file so that it can be accessed by subsequent processes eg CSMODEL. |  No |  1 |  Undefined |  Undefined  
XMIN |  Minimum X coordinate of the regular grid of simulated points created in the output POINTS and MODEL files. If a PROTO file is specified this parameter is ignored. |  No |  1 |  Undefined |  Undefined  
YMIN |  Minimum Y coordinate of the regular grid of simulated points created in the output POINTS and MODEL files. If a PROTO file is specified this parameter is ignored. |  No |  1 |  Undefined |  Undefined  
ZMIN |  Minimum Z coordinate of the regular grid of simulated points created in the output POINTS and MODEL files. If a PROTO file is specified this parameter is ignored. |  No |  1 |  Undefined |  Undefined  
XSIZE |  Spacing between simulated points in the X direction. If a PROTO file is specified this parameter is ignored. |  No |  1 |  Undefined |  Undefined  
YSIZE |  Spacing between simulated points in the Y direction. If a PROTO file is specified this parameter is ignored. |  No |  1 |  Undefined |  Undefined  
ZSIZE |  Spacing between simulated points in the Z direction. If a PROTO file is specified this parameter is ignored. |  No |  1 |  Undefined |  Undefined  
NX |  Number of simulated points in the X direction. If a PROTO file is specified this parameter is ignored. |  No |  10 |  1,+ |  Undefined  
NY |  Number of simulated points in the Y direction. If a PROTO file is specified this parameter is ignored. |  No |  10 |  1,+ |  Undefined  
NZ |  Number of simulated points in the Z direction. If a PROTO file is specified this parameter is ignored. |  No |  10 |  1,+ |  Undefined  
SEED |  Random number seed. This should be a large odd integer. If the same seed is used for multiple runs then the same set of simulated grades will be created. |  No |  |  1,+ |  Undefined  
MINDATPT |  The minimum number of original data to be used to simulate a grid node. If there are fewer than MINDATPT data points the node is not simulated. |  No |  1 |  1,+ |  Undefined  
MAXDATPT |  The maximum number of original data to be used to simulate a grid node. If there are more than MAXDATPT data points the nearest points are selected. |  No |  12 |  1,48 |  Undefined  
MAXSIMPT |  The maximum number of previously simulated nodes to use for the simulation of another node. |  No |  12 |  1,48 |  Undefined  
SSTRAT |  Search strategy: 0 = data and previously simulated grid nodes are searched separately. Data are searched with a super block search and previously simulated nodes with a spiral search. 1 = data are relocated to grid nodes and a spiral search is used. MINDATPT and MAXDATPT are not then considered. |  No |  0 |  0,1 |  0,1  
MULTGRID |  Search strategy for previously simulated nodes: 0 = spiral search if greater than or equal to 1 then MULTGRID defines the number of grids for a multiple grid simulation. |  No |  0 |  |  0,9 Value: 0,1,2,3,4,5,6,7,8,9  
MAXPEROC |  Maximum number of original data points per octant. If set to zero then octant search is not used. If octant search is used then MAXDATPT is ignored. |  No |  0 |  0,+ |  Undefined  
SDIST1 |  Search distance in the X direction. This may be a rotated X direction if parameters SANGLE1 , SANGLE2 or SANGLE3 are non zero. |  No |  50 |  Undefined |  Undefined  
SDIST2 |  Search distance in the Y direction. This may be a rotated Y direction if parameters SANGLE1 , SANGLE2 or SANGLE3 are non zero. |  No |  50 |  Undefined |  Undefined  
SDIST3 |  Search distance in the Z direction. This may be a rotated Z direction if parameters SANGLE1 , SANGLE2 or SANGLE3 are non zero. |  No |  50 |  Undefined |  Undefined  
SANGLE1 |  First rotation angle for search ellipsoid. The rotation must be around the Z axis. |  No |  0 |  -360,360 |  Undefined  
SANGLE2 |  Second rotation angle for search ellipsoid. The rotation must be around the X axis. |  No |  0 |  -360,360 |  Undefined  
SANGLE3 |  Third rotation angle for search ellipsoid. The rotation must be around the Y axis. |  No |  0 |  -360,360 |  Undefined  
KTYPE |  Kriging type: 0 = simple kriging 1 = ordinary kriging 2 = simple kriging with a locally varying mean where the mean is defined by field SECFLD2 in file SECFILE . 3 = kriging with an external drift where the drift is defined by field SECFLD2 in file SECFILE . 4 = collocated cokriging with one secondary grade defined by field SECFLD2 in file SECFILE . |  No |  0 |  0,4 |  0,1,2,3,4  
VMODNUM |  Variogram model number in VMODPARM file. |  No |  1 |  |  Undefined  
CORCOEFF |  Correlation coefficient used for collocated kriging (ie when KTYPE = 4). |  No |  0 |  |  Undefined  
VARRED |  Variance reduction factor used for collocated kriging (ie when KTYPE = 4) . |  No |  1 |  Undefined |  Undefined  
RECTGRID |  Rectangular grid flag. This only applies if there are cells in the input PROTO model. |  Option |  Description  
---|---  
0 |  Simulated points will only be output where the points lie within a parent cell as defined by the PROTO model.  
1 |  Simulated points will be output at all locations inside the 3D rectangular volume enclosing the PROTO cells. This is essential if the output model file is to be used as the secondary file for a subsequent run of SGSIM with KTYPE=4 for cosimulation.  
No |  0 |  0,1 |  0,1  
DBGLEVEL |  Debug level. Controls the amount of debug information written to the debug file _sgsdbg.txt. 0 is the minimum and 3 the maximum. |  No |  0 |  0,3 |  0,1,2,3  
  
## Example
    
    
    !SGSIM  &IN(sample1),&VMODPARM(vpar1),&POINTS(simpts1),&MODEL(simmod1),  
  
---  
      
    
     &TRANDIST(trandis1),*X(XPT),*Y(YPT),*Z(ZPT),*GRADE(AU),  
      
    
     @MINGRADE=0.0,@MAXGRADE=999.0,@TRANTYPE=1.0,@MINSIMGR=0.0,  
      
    
     @MAXSIMGR=20.0,@LOTAIL=1.0,@LOPAR=1.0,@UPTAIL=1.0,  
      
    
     @UPPAR=1.0,@NSIM=5.0,@XMIN=8640.0,@YMIN=3360.0,  
      
    
     @ZMIN=160.0,@XSIZE=5.0,@YSIZE=5.0,@ZSIZE=5.0,@NX=22.0,  
      
    
     @NY=20.0,@NZ=18.0,@SEED=69069.0,@MINDATPT=1.0,@MAXDATPT=12.0,  
      
    
     @MAXSIMPT=12.0,@SSTRAT=0.0,@MULTGRID=0.0,@MAXPEROC=0.0,  
      
    
     @SDIST1=17.0,@SDIST2=43.0,@SDIST3=15.0,@SANGLE1=20.0,  
      
    
     @SANGLE2=30.0,@SANGLE3=0.0,@KTYPE=0.0,@VMODNUM=1.0,  
      
    
     @CORCOEFF=0.0,@VARRED=1.0,@DBGLEVEL=0.0  
  
## Error and Warning Messages

Message |  Description  
---|---  
ERROR: nn characters in Project path name. Maximum = 48 |  The number of characters in the path name of the project folder exceeds 48 characters. Reduce the path name to 48 or less characters in length.  
  
Copyright Notice

The command SGSIM is based on the GSLIB program SGSIM. 

Copyright (C) 1996, The Board of Trustees of the Leland Stanford   
Junior University. All rights reserved.   
  
The programs in GSLIB are distributed in the hope that they will be   
useful, but WITHOUT ANY WARRANTY. No author or distributor accepts   
responsibility to anyone for the consequences of using them or for   
whether they serve any particular purpose or work at all, unless he   
says so in writing. Everyone is granted permission to copy, modify   
and redistribute the programs in GSLIB, but only under the condition  
that this notice and the above copyright notice remain intact.