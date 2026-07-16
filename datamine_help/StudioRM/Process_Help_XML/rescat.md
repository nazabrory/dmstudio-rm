# RESCAT Process

To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **RESCAT** and click **Run**.
  * Enter "RESCAT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#RESCAT>).

## Process Overview

Reserve Category Modeling.

To define reserve categories in terms of the distance of the nearest sample from the centre of a cell. All fields from the input model file are copied to the output model, and in addition 3 extra fields may be added:  

  * **VALUE** \- the value of the nearest sample.

  * **DISTANCE** \- the distance of the nearest sample from the cell centre.

  * **CATEGORY** \- a reserve category identifier.

If a field **CATEGORY** already exists in one of the input files then the **CATEGORY** field in the output **MODEL** file will be of the same type (A-alpha or N-numeric) If the field does not already exist then it will be created as an alpha field with a maximum of 4 characters.

Any combination of the 3 fields may be included controlled by the value of parameter **RESCAT**. The user is prompted to enter reserve category definitions interactively.

If RESCAT = 1,3,4 or 6 then you must define reserve categories in free format: >

  * Category

  * Minimum Distance

  * Maximum Distance

3 data items per line separated by commas. Terminate entry with a blank line or a comma in the first character position. If parameter **ELLIPSE** is non zero then the weighting parameters are prompted:

>DIP> |  Dip of Axis 1 (degrees down from horizontal).  
---|---  
>AZIMUTH> |  Azimuth of Axis 1 (degrees clockwise from Y).  
>AXIS 1 > |  Relative length of Axis 1.  
>AXIS 2 > |  Relative length of Axis 2.  
>AXIS 3 > |  Relative length of Axis 3.  
  
Note: AXIS 1 is in the Y direction, if unrotated. Distances along e.g. AXIS 2 will be multiplied by the ratio AXIS 2/AXIS 1.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Input prototype model. This may be just fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK**. May contain cells and sub-cells. |  Input |  Yes |  Block Model Prototype  
IN |  Input sample data (sorted on X). Must contain the fields **X , Y , Z , VALUE**. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODEL |  Output |  Yes |  Block Model |  Output model.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Value field. Even if the **VALUE** field is not copied to the output file a **VALUE** field is still required (as for any other model interpolation process). |  IN |  Yes |  Any |  Undefined  
X |  Name of X field in **IN** sample file. |  IN |  Yes |  Numeric |  Undefined  
Y |  Name of Y field in **IN** sample file. |  IN |  Yes |  Numeric |  Undefined  
Z |  Name of Z field in **IN** sample file. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
RADIUS |  Search radius.[Maximum Value] |  Yes |  Undefined |  Undefined |  Undefined  
RESCAT |  Reserve category parameter controlling fields in the output model. |  No |  1 |  Undefined |  Undefined  
ELLIPSE |  Ellipsoid weighting parameter. If set to 1 then the user will be prompted to enter distance weighting parameters. |  No |  0 |  0,1 |  0,1  
XSUBCELL |  No. of sub-cells/cell in X. |  No |  1 |  Undefined |  Undefined  
YSUBCELL |  No. of sub-cells/cell in Y. |  No |  1 |  Undefined |  Undefined  
ZSUBCELL |  No. of sub-cells/cell in Z. Above three parameters only used if input prototype does not already contain cells. |  No |  1 |  Undefined |  Undefined  
PRINT |  >=1 Display co-ordinates and interpolated values. |  No |  Undefined |  0,1 |  0,1