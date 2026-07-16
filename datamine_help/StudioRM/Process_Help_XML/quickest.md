# QUICKEST Process  
  
To access this process:

  * **Model** ribbon **> > Estimate >> Interpolate**.

  * Enter "MODTRA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MODTRA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_Q.md#QUICKEST>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

The **QUICKEST** process interpolates grades into a block model using basic calculations. It supports processes requiring precursory interpolation methods, such as IsoShell generation. It can also be called independently from the command line.

## Input Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PROTO |  Input |  Yes |  Block_Model_File |  Input model prototype. This is a standard block model file containing the 13 compulsory fields. It may also contain the rotated model fields. If it includes cells then it must be sorted on IJK.  
IN |  Input |  Yes |  Table |  Input sample data. This must contain X,Y and Z fields and at least one grade field.  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
**MODEL** |  Output |  Yes |  Block Model File |  Output model containing estimated grades, variance etc.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X coordinate of sample data in IN file. If not specified, then X is assumed. If the unfolding option is used, then the X coordinate must be set to the unfolded UCSA coordinate. |  IN |  Yes |  Numeric |  X  
Y |  Y coordinate of sample data in IN file. If not specified, then Y is assumed. If the unfolding option is used, then the Y coordinate must be set to the unfolded UCSB coordinate. |  IN |  Yes |  Numeric |  Y  
Z |  Z coordinate of sample data in IN file. If not specified, then Z is assumed. If the unfolding option is used, then the Z coordinate must be set to the unfolded UCSC coordinate. |  IN |  Yes |  Numeric |  Z  
VALUE | Name of the field containing the grade to be estimated | IN | Yes | Alphanumeric | Undefined  
NUMSAM | Name of the field to be created in the output MODEL file which is used to record the number of samples used for estimating each cell. If a field name is not specified the number of samples used will not be recorded. | - | No | Alphanumeric | Undefined  
ZONE | Name of the zonal interpolation field. The field may be numeric or up to 20 character alphanumeric. The field must exist in both the PROTO and IN files. If it is specified then cells in each ZONE will be interpolated using only samples with the same ZONE value. | - | No | Alphanumeric | Undefined  
LENGTH | Name of the field used for length weighting of samples. This is only used if the Inverse Power of Distance interpolation method is selected (IMETHOD=2). | - | No | Alphanumeric | Undefined  
  
## Parameters

  
Name |  Description |  Required |  Default |  Range |  Values  
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
IMETHOD |  Interpolation method: 1: Nearest Neighbour 2: Inverse Power of Distance |  No |  2 |  1,2 |  1,2  
POWER |  Weighting power if Inverse Power of Distance is selected (IMETHOD=2). |  No |  2 |  Undefined |  Undefined  
XPOINTS |  Number of discretisation points in the X direction. Discretisation points are used to simulate each cell or subcell for the purpose of grade estimation. They are only used for the Inverse Power of Distance (**IMETHOD** =2) estimation methods If Inverse Power of Distance is used then **XPOINTS, YPOINTS** and **ZPOINTS** may all be 1, and so the subcell is represented by a single point at its centre. |  No |  3 |  1,6 |  1,2,3,4,5,6  
YPOINTS |  Number of discretisation points in the Y direction. Discretisation points are used to simulate each cell or subcell for the purpose of grade estimation. They are only used for the Inverse Power of Distance (**IMETHOD** =2) estimation methods If Inverse Power of Distance is used then **XPOINTS, YPOINTS** and **ZPOINTS** may all be 1, and so the subcell is represented by a single point at its centre. |  No |  3 |  1,6 |  1,2,3,4,5,6  
ZPOINTS |  Number of discretisation points in the Z direction. Discretisation points are used to simulate each cell or subcell for the purpose of grade estimation. They are only used for the Inverse Power of Distance (**IMETHOD** =2) estimation methods If Inverse Power of Distance is used then **XPOINTS, YPOINTS** and **ZPOINTS** may all be 1, and so the subcell is represented by a single point at its centre. |  No |  3 |  1,6 |  1,2,3,4,5,6  
XSUBCELL |  Number of subcells per parent cell to be created in the X direction. This only applies if there are no cells in the input prototype model **PROTO** , and therefore cells (and subcells) are created by the **GRADE** process. |  No |  1 |  1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
YSUBCELL |  Number of subcells per parent cell to be created in the Y direction. This only applies if there are no cells in the input prototype model **PROTO** , and therefore cells (and subcells) are created by the **GRADE** process. |  No |  1 |  1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
ZSUBCELL |  Number of subcells per parent cell to be created in the Z direction. This only applies if there are no cells in the input prototype model **PROTO** , and therefore cells (and subcells) are created by the **GRADE** process. |  No |  1 |  1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
PRINT |  Display control: 0: minimum output including progress message. 1: as 0 plus details of input parameters. 2: as 1 plus display of each cell value. |  No |  0 |  0,2 |  0,1,2  
  
Related topics and activities

  * [GRADE Process](<grade.md>)