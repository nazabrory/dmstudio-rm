# WFEXPND Process

To access this process:

  * **Wireframe** ribbon **> > Process >> Wireframe Proceses >> Expand Wireframe**.

  * Enter "WFEXPND" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **WFEXPND** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_W.md#WFEXPND>).

## Process Overview

Create a copy of a wireframe, where each triangle has been moved outwards (or inwards) by a set distance.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
INTR |  Input wireframe triangle file. |  Input |  Yes |  Wireframe triangle  
INPT |  Input wireframe point file. |  Input |  Yes |  Wireframe points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUTTR |  Output |  Yes |  Wireframe triangle |  Output wireframe triangle file.  
OUTPT |  Output |  Yes |  Wireframe points |  Output wireframe point file..  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DISTANCE |  The distance required to move the triangles out by. A positive number will move them in the direction of each triangle normal (usually outwards for a verified closed wireframe, or upwards for a verified open wireframe). A negative distance will move the triangles in the opposite direction (e.g. to shrink a closed volume). |  Yes |  Undefined |  -, + |  Undefined  
TOLERANC |  A value which determines how closely the required distance must be met. This has most effect in the number of triangles added to approximate the path around sharp edges in the wireframe. A smaller tolerance will result in smoother curves but a bigger wireframe. A value of one tenth of the offset distance often provides a good balance between wireframe size and smoothness. |  Yes |  Undefined |  0.001, + |  Undefined  
SURFBLND |  Determines whether blends are created on the boundaries of open wireframes: 0 = don't blend boundaries, 1 = blend boundaries. |  No |  1 |  0,1 |  0,1  
  
## Example
    
    
    !WFEXPND &INTR(_vb_mintr),&INPT(_vb_minpt),  
  
---  
      
    
    &OUTTR(outtr),&OUTPT(outpt),  
      
    
    @DISTANCE=5.0,@TOLERANC=1.0,@SURFBLND=1.0  
  
Related topics and activities

  * [EXPNDMOD Process](<expndmod.md>)

  * [translate-wireframe ("trw")](<../command_help/translate-wireframe.md>)