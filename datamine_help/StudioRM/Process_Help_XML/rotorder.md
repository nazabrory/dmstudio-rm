# ROTORDER Process

To access this process:

  * Enter "ROTORDER" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **ROTORDER** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#ROTORDER>).

## Process Overview

Converts rotation axes and angles to a specified rotation order. Can be used to update a file in place, and retrieval criteria are supported.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file containing axes and angles to be reordered. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file. If this is set to the same file as IN then the input file fields will be modified.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
ROTAXIS1 |  Field name for first rotation axis. |  IN |  Yes |  Any |  VAXIS1  
ROTAXIS2 |  Field name for second rotation axis. |  IN |  Yes |  Any |  VAXIS2  
ROTAXIS3 |  Field name for third rotation axis. |  IN |  Yes |  Any |  VAXIS3  
ANGLE1 |  Field name for first rotation angle. |  IN1 |  Yes |  Any |  VANGLE1  
ANGLE2 |  Field name for second rotation angle. |  IN1 |  Yes |  Any |  VANGLE2  
ANGLE3 |  Field name for third rotation angle. |  IN1 |  Yes |  Any |  VANGLE3  
  
## Parameters

Name |  Description |  Required |  Type |  Default  
---|---|---|---|---  
OUTAXIS1 |  First rotation axis. 1=X, 2=Y, 3=Z. The first rotation is by **ANGLE1** degrees clockwise around axis **AXIS1** , when viewed along the axis from positive values towards the origin. An axis value of 0 means no rotation. |  Yes |  Any |  3  
OUTAXIS2 |  Second rotation axis. 1=X, 2=Y, 3=Z. The second rotation is by **ANGLE2** degrees clockwise around axis **AXIS2** , when viewed along the axis from positive values towards the origin. An axis value of 0 means no rotation. |  Yes |  Any |  1  
OUTAXIS3 |  Third rotation axis. 1=X, 2=Y, 3=Z. The first rotation is by **ANGLE3** degrees clockwise around axis **AXIS3** , when viewed along the axis from positive values towards the origin. An axis value of 0 means no rotation. |  Yes |  Any |  3