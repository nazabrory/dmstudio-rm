# GRADE Process

To access this process:

  * **Estimate** ribbon **> > Interpolate >> Standard >> Basic**.
  * Enter "GRADE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **GRADE** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_G.md#GRADE>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

Interpolate a single grade into a block model using basic interpolation methods:

  * Nearest Neighbour

The Nearest Neighbour interpolation method simply assigns to the subcell the grade of the nearest sample. The definition of 'nearest' takes into account the anisotropy and orientation of the search ellipsoid. The Inverse Power of Distance method also takes account of the anisotropy and orientation of the search volume when assigning weights to the samples.

  * Inverse Power of Distance

For Inverse Power of Distance and Ordinary Kriging you may record the number of samples which are used to make each estimate. This is done by specifying a **NUMSAM** field. 

  * Ordinary Kriging

If you select Ordinary Kriging then you must also define a one or two structure spherical model variogram. It is assumed that any anisotropy in the variogram ranges has the same orientation as the search volume, but the actual values of the ranges are independent of the dimensions of the search volume. For Ordinary Kriging you may also record the kriged variance of the estimate by specifying a **VARIANCE** field.

Note: Only one grade field can be interpolated at a time. **[COKRIG](<cokrig.md>)** should be used when multiple grade fields need to be interpolated at a time.

For any method, you must specify an [input prototype block model](<../COMMON/filetype.md#BlockMod>), and an input sample data file. If the input prototype model contains cells and subcells then values are interpolated into the existing cell structure. If the prototype model is empty then cells and subcells are created if there are sufficient samples within the search volume.  
  
For kriging, a search volume is defined by a 3D ellipsoid which is centered on each subcell of the model in turn, and is used to select the samples for interpolating that subcell. You must define the lengths for the three axes of the ellipsoid, which may be different if you want an anisotropic volume. If you want a spherical search volume then set all three axes equal to the radius of the required sphere. You may orientate the search ellipsoid by specifying three sets of rotation angles and axes. The definition of the rotation angles and axes is described in section 3 of the Grade Estimation User Guide.  
  
You may select to use the zone control option by specifying a **ZONE** field. This will restrict the samples that are used for making the estimate to have the same **ZONE** value as the prototype model subcell. For example if both the prototype model and sample data files include a numeric rocktype field **ROCK** , then specifying **ZONE**(ROCK) will ensure that subcells which are rocktype N will be estimated using samples which are rocktype N.

The samples from the input sample file &**IN** can be weighted by specifying a **LENGTH** field.

**Note** : It frequently happens that samples are not evenly distributed around the subcell being estimated, but are clustered together. One way of minimizing this problem is to divide the search volume into octants and ensure that a minimum number of octants have samples in them. This is defined using the **MINOCT** , **MINPEROC** and **MAXPEROC** parameters.

### Input Files

**Name** |  **I/O Status** |  **Required** |  **Type** |  **Description**  
---|---|---|---|---  
PROTO |  Input |  Yes |  Block Model prototype |  Input prototype model. This must contain at least the fields **XC** , **YC** , **ZC** , **XINC** , **YINC** , **ZINC** , **XMORIG** , **YMORIG** , **ZMORIG** , **NX** , **NY** , **NZ** , **IJK**.  If the file contains cells and subcells, then these cells and subcells will be copied to the output model with the new grade field added. If the file does not contain cells and subcells then they will be created if there is sufficient data within the search ellipsoid.  
IN |  Input |  Yes |  Drillhole |  Input sample data. This must contain the X, Y and Z coordinates of each sample and the grade field (**VALUE**) to be estimated. This will usually be a drillhole file, but can be any file containing the four required fields  
  
### Output Files

**Name** |  **I/O Status** |  **Required** |  **Type** |  **Description**  
---|---|---|---|---  
MODEL |  Output |  Yes |  Block Model |  Output interpolated model. This will include all the fields in the input prototype model plus the estimated grade field (**VALUE**). In addition the number of samples field (**NUMSAM**) and the variance field (**VARIANCE**) will be included if they have been specified  
  
## Fields

**Name** |  **Description** |  **Source** |  **Required** |  **Type** |  **Default**  
---|---|---|---|---|---  
X |  Name of the field containing the X coordinate of the sample. |  IN |  Yes |  Numeric |  X  
Y |  Name of the field containing the Y coordinate of the sample. |  IN |  Yes |  Numeric |  Y  
Z |  Name of the field containing the Z coordinate of the sample. |  IN |  Yes |  Numeric |  Z  
VALUE |  Name of the field containing the grade to be estimated. |  IN |  Yes |  Any |  Undefined  
NUMSAM |  Name of the field to be created in the output **MODEL** file which is used to record the number of samples used for estimating each cell. If a field name is not specified the number of samples used will not be recorded. |  MODEL |  No |  Numeric |  Undefined  
VARIANCE |  Name of the field to be created in the output **MODEL** file which is used to record the kriged variance of the estimate of eachcell. This can only be used if Ordinary Kriging (IMETHOD=3) has been selected. If a field name is not specified then the variance will not be reorded. |  MODEL |  No |  Numeric |  Undefined  
ZONE |  Name of the zonal interpolation field. The field may be numeric or up to 20 character alphanumeric. The field must exist in both the **PROTO** and IN files. If it is specified then cells in each **ZONE** will be interpolated using only samples with the same **ZONE** value. |  PROTO, IN |  No |  Any |  Undefined  
LENGTH |  Name of the field used for length weighting of samples. This is only used if the Inverse Power of Distance interpolation method is selected (**IMETHOD** =2). |  MODEL |  No |  Numeric |  LENGTH  
  
## Parameters

**Name** |  **Description** |  **Required** |  **Default** |  **Range** |  **Values**  
---|---|---|---|---|---  
SDIST1 |  Length of the search ellipsoid axis in the X direction. |  No |  100 |  0.00001,+ |  Undefined  
SDIST2 |  Length of the search ellipsoid axis in the Y direction. . |  No |  100 |  0.00001,+ |  Undefined  
SDIST3 |  Length of the search ellipsoid axis in the Z direction. . |  No |  100 |  0.00001,+ |  Undefined  
SANGLE1 |  First rotation angle (in degrees) for the search ellipsoid. The rotation is around the axis defined by **SAXIS1**. |  No |  0 |  -360,360 |  Undefined  
SAXIS1 |  Coordinate axis about which rotation **SANGLE1** is applied. Specify 1 for the X axis, 2 for the Y axis, or 3 for the Z axis. |  No |  3 |  1,3 |  1,2,3  
SANGLE2 |  Second rotation angle (in degrees) for the search ellipsoid. The rotation is around the axis defined by **SAXIS2**. |  No |  0 |  -360,360 |  Undefined  
SAXIS2 |  Coordinate axis about which rotation **SANGLE2** is applied. Specify 1 for the X axis, 2 for the Y axis, or 3 for the Z axis. |  No |  1 |  1,3 |  1,2,3  
SANGLE3 |  Third rotation angle (in degrees) for the search ellipsoid. The rotation is around the axis defined by **SAXIS3**. |  No |  0 |  -360,360 |  Undefined  
SAXIS3 |  Coordinate axis about which rotation **SANGLE3** is applied. Specify 1 for the X axis, 2 for the Y axis, or 3 for the Z axis. |  No |  3 |  1,3 |  1,2,3  
MINNUM |  Minimum number of samples which must lie within the search ellipsoid in order for the model subcell to be estimated. If there are less than the minimum number and the input **PROTO** model contains cells, then an absent data value will be assigned to the grade field in the output model file **MODEL** If there are less than the minimum, but the input **PROTO** model does not contain any cells, then a cell will not be created in the output model file **MODEL**. |  No |  3 |  1,1400 |  Undefined  
MAXNUM |  Maximum number of samples to be used for estimating the grade of a model cell. If more than the maximum number lie within the search ellipsoid, then the search ellipsoid is shrunk concentrically until just **MAXNUM** samples remain. The maximum number cannot exceed 1400. |  No |  20 |  1,1400 |  Undefined  
MINOCT |  The minimum number of octants to be filled before a subcell will be interpolated. If it is set to zero then octant search will not be used. |  No |  0 |  0,8 |  0,1,2,3,4,5,6,7,8  
MINPEROC |  The minimum number of samples in an octant before it is considered to be filled. |  No |  1 |  0,1400 |  Undefined  
MAXPEROC |  The maximum number of samples in an octant, to be used for interpolation. If there are more than the maximum number in any octant, then the samples closest to subcell centre are selected. If set to zero there is no limit on the number of samples. |  No |  0 |  0,1400 |  Undefined  
IMETHOD |  Interpolation method: 1: Nearest Neighbour 2: Inverse Power of Distance 3: Ordinary Kriging with a one or two structure spherical variogram model . |  No |  2 |  1,3 |  1,2,3  
POWER |  Weighting power if Inverse Power of Distance is selected (**IMETHOD** =2). |  No |  2 |  Undefined |  Undefined  
NSTRUCT |  Number of structures in the variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3). |  No |  1 |  1,2 |  1,2  
NUGGET |  Nugget variance of spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3). |  No |  0 |  0,+ |  Undefined  
ST1VAR |  Spatial variance (ie C value) of the first structure of the spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3). |  No |  1 |  0.000001,+ |  Undefined  
ST1RANG1 |  Variogram range (ie A value) in the X direction of the first structure of the spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3). |  No |  100 |  0.000001,+ |  Undefined  
ST1RANG2 |  Variogram range (ie A value) in the Y direction of the first structure of the spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3). |  No |  100 |  0.000001,+ |  Undefined  
ST1RANG3 |  Variogram range (ie A value) in the Z direction of the first structure of the spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3). |  No |  100 |  0.000001,+ |  Undefined  
ST2VAR |  Spatial variance (ie C value) of the second structure of the spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3) and two structures have been specified (**NSTRUCT** =2). |  No |  1 |  0.000001,+ |  Undefined  
ST2RANG1 |  Variogram range (ie A value) in the X direction of the second structure of the spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3) and two structures have been specified (**NSTRUCT** =2). |  No |  100 |  0.000001,+ |  Undefined  
ST2RANG2 |  Variogram range (ie A value) in the Y direction of the second structure of the spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3) and two structures have been specified (**NSTRUCT** =2). |  No |  100 |  0.000001,+ |  Undefined  
ST2RANG3 |  Variogram range (ie A value) in the Z direction of the second structure of the spherical variogram model. This parameter is only used if Ordinary Kriging is selected (**IMETHOD** =3) and two structures have been specified (**NSTRUCT** =2). |  No |  100 |  0.000001,+ |  Undefined  
PARENT |  Flag to control parent cell estimation: 0: estimate a grade for each individual subcell. 1: estimate a grade for the parent cell and assign that grade to all subcells lying within the parent cell. |  No |  0 |  0,1 |  0,1  
XPOINTS |  Number of discretisation points in the X direction. Discretisation points are used to simulate each cell or subcell for the purpose of grade estimation.  They are only used for Inverse Power of Distance (**IMETHOD** =2) and Ordinary Kriging (**IMETHOD** =3) estimation methods.  If Inverse Power of Distance is used then **XPOINTS** , **YPOINTS** and **ZPOINTS** may all be 1, and so the subcell is represented by a single point at its centre. If Ordinary Kriging is used then the total number of discretisation points (**XPOINTS** x **YPOINTS** x **ZPOINTS**) must be greater than or equal to 2. |  No |  3 |  1,6 |  1,2,3,4,5,6  
YPOINTS |  Number of discretisation points in the Y direction. Discretisation points are used to simulate each cell or subcell for the purpose of grade estimation.  They are only used for Inverse Power of Distance (**IMETHOD** =2) and Ordinary Kriging (**IMETHOD** =3) estimation methods. If Inverse Power of Distance is used then **XPOINTS** , **YPOINTS** and **ZPOINTS** may all be 1, and so the subcell is represented by a single point at its centre. If Ordinary Kriging is used then the total number of discretisation points (**XPOINTS** x **YPOINTS** x **ZPOINTS**) must be greater than or equal to 2. |  No |  3 |  1,6 |  1,2,3,4,5,6  
ZPOINTS |  Number of discretisation points in the Z direction. |  No |  3 |  1,6 |  1,2,3,4,5,6  
XSUBCELL |  Number of subcells per parent cell to be created in the X direction. This only applies if there are no cells in the input prototype model PROTO, and therefore cells (and subcells) are created by the GRADEprocess. |  No |  1 |  1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
YSUBCELL |  Number of subcells per parent cell to be created in the Y direction.  |  No |  1 |  1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
ZSUBCELL |  Number of subcells per parent cell to be created in the Z direction.  |  No |  1 |  1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
PRINT |  Display control: 0: minimum output including progress message. 1: as 0 plus details of input parameters. 2: as 1 plus display of each cell value. |  No |  0 |  0,2 |  0,1,2  
  
## Example
    
    
    !GRADE    &PROTO(rockmod),&IN(samples),&MODEL(grademod),*X(XPT),*Y(YPT),          *Z(ZPT),*VALUE(AU),*LENGTH(LENGTH),@SDIST1=100.0,  
  
---  
      
    
              @SDIST2=100.0,@SDIST3=100.0,@SANGLE1=0.0,@SAXIS1=3.0,  
      
    
              @SANGLE2=0.0,@SAXIS2=1.0,@SANGLE3=0.0,@SAXIS3=3.0,  
      
    
              @MINNUM=3.0,@MAXNUM=20.0,@MINOCT=0.0,@MINPEROC=1.0,  
      
    
              @MAXPEROC=0.0,@IMETHOD=2.0,@POWER=2.0,@NSTRUCT=1.0,  
      
    
              @NUGGET=0.0,@ST1VAR=1.0,@ST1RANG1=100.0,@ST1RANG2=100.0,  
      
    
              @ST1RANG3=100.0,@ST2VAR=1.0,@ST2RANG1=100.0,@ST2RANG2=100.0,  
      
    
              @ST2RANG3=100.0,@PARENT=0.0,@XPOINTS=3.0,@YPOINTS=3.0,  
      
    
              @ZPOINTS=3.0,@XSUBCELL=1.0,@YSUBCELL=1.0,@ZSUBCELL=1.0  
  
Related topics and activities

  * [ESTIMA Process](<estima.md>)

  * [ESTIMATE Process](<estimate.md>)

  * [COKRIG Process](<cokrig.md>)