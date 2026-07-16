# IPDNPG Process

To access this process:

  * Enter "IPDNPG" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **IPDNPG** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#IPDNPG>).

## Process Overview

Interpolate grades into block model cells using non-parametric methods.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Prototype model. Must contain at least the fields XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK. May contain cells and sub-cells. |  Input |  Yes |  Block Model Prototype  
IN |  Input sample data (sorted on X). Must contain the fields X , Y , Z , VALUE. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODEL |  Output |  Yes |  Block Model |  Output interpolated model.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Name of sample X field. |  IN |  Yes |  Numeric |  X  
Y |  Name of sample Y field. |  IN |  Yes |  Numeric |  Y  
Z |  Name of sample Z field. |  IN |  Yes |  Numeric |  Z  
VALUE |  Name of field to be interpolated. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
TYPE |  (1) Type of interpolation to be used :- |  Option |  Description  
---|---  
1 |  Moving mode  
2 |  Moving median  
3 |  Varying quantile  
4 |  Angle-weighted varying quantile  
Yes |  1 |  1,4 |  1,2,3,4  
RADIUS |  Search radius [mean cell dimension]. |  No |  Undefined |  Undefined |  Undefined  
MINNOP |  Minimum number of samples (5). |  No |  5 |  Undefined |  Undefined  
MAXNOP |  Maximum number of samples (1000). |  No |  1000 |  Undefined |  Undefined  
XSUBCELL |  No. of sub-cells/cell in X (1). |  No |  1 |  Undefined |  Undefined  
YSUBCELL |  No. of sub-cells/cell in Y (1). |  No |  1 |  Undefined |  Undefined  
ZSUBCELL |  No. of sub-cells/cell in Z (1). Above three parameters only used if input prototype does not already contain cells. |  No |  1 |  Undefined |  Undefined  
PRINT |  >=2 Display co-ordinates and interpolated values. |  No |  0 |  0,2 |  0,2