# MODTRI Process  
  
To access this process:

  * Enter "MODTRI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MODTRI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MODTRI>).

## Process Overview

Convert the visible faces of a sub-cell block model to wireframe surfaces. The block model is interpreted as a solid model.

Note: This process is much faster than the **[BLKTRI](<blktri.md>)** process and will work better on larger models.

When using the @**PTTOL** parameter to detect duplicate wireframe output points the process will be slower

The @**ORIGIN** parameter can be used with more complex sub celled models to help resolve producing unverifiable wireframes.

If the block model is a standard rotated block model then the additional fields **X0, Y0, Z0, ANGLE1, ANGLE2, ANGLE3, ROTAXIS1, ROTAXIS2,** and **ROTAXIS3** are used to calculate the wireframe position.

The standard wireframe GROUP, SURFACE, adjacency and orientation data is output to the wireframe files. Normals for void surfaces will face inwards and can be used in Studio 3 evaluation processes to automatically exclude the evaluation of the void volume.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. Must contain fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ** , and **IJK**. If it is a Rotated Model then it must also include the fields **X0, Y0, Z0, ANGLE1, ANGLE2, ANGLE3, ROTAXIS1, ROTAXIS2** , and **ROTAXIS3**. |  Input |  Yes |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
WIRETR |  Output wireframe triangle file. |  Output |  Yes |  Wireframe Triangle  
WIREPT |  Output wireframe point file. |  Output |  Yes |  Wireframe Points  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ORIGIN |  Origin coordinates. Values are: 0 - retain original coordinates. 1 - use coordinates relative to the model origin. 2 - use the central coordinates of model cells as the new origin |  No |  0 |  0,2 |  0,1,2  
PTTOL |  Check for duplicates in output wireframe coordinates |  No |  0 |  0,1 |  0,1  
  
## Example

Wireframe a single zone from a grade sub-cell model.
    
    
    !GENTRA &IN(MODEL),&OUT(TEMP)  
  
---  
      
    
    SETC ZONE 0  
      
    
    GTC CU 1; SETC ZONE 1  
      
    
    GTC CU 3; SETC ZONE 3  
      
    
    GTC CU 5; SETC ZONE 5  
      
    
    END  
      
    
    OK  
      
    
    !MODTRI &IN(TEMP),&WIREPT(WIREPT),&WIRETR(WIRETR),ZONE=   
      
    
     3  
  
Related topics and activities

  * [BLKTRI Process](<blktri.md>)