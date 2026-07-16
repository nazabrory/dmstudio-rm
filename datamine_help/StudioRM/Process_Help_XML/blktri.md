# BLKTRI Process  
  
To access this process:

  * Model ribbon **> > Data From Model >> Perimeters**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **BLKTRI** and click **Run**.
  * Enter "BLKTRI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/commandtable_B.md#BLKTRI>).

## Process Overview

Converts block model(s) to wireframe surfaces(s).

Although it does not support a keyfield option, the [MODTRI](<modtri.md>) process is quicker to execute than the **BLKTRI** process. Also, **MODTRI** is able to process larger models than **BLKTRI**.

Another option is to make use of the Isosurfaces wireframe function, resulting in surface shapes representing real surfaces - although note that the output from **BLKTRI** and Isosurface generation may not be identical due to the calculation methods used.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. Must contain fields XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, and IJK. If it is a Rotated Model then it must also include the fields X0, Y0, Z0, ANGLE1, ANGLE2, ANGLE3, ROTAXIS1, ROTAXIS2, and ROTAXIS3. |  Input |  Yes |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
WIRETR |  Output |  Yes |  Wireframe Triangle |  Output wireframe triangle file.  
WIREPT |  Output |  Yes |  Wireframe Points |  Output wireframe point file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
CLASS |  Field in block model defining multiple zones or seams. |  IN |  No |  Any |  Undefined  
MODCOL |  A numeric field to be used to allocate (an integer) wireframe colour. It is assumed that colour is related to CLASS. If colour varies within a CLASS then the colour corresponding to the first occurrence of each CLASS will be used. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PLANE |  Plane for interpretation of solid or seam orientation. Values are: 0 - solid model, so plane not required. 1 - XY plane (plan) 2 - XZ plane (East-West section) 3 - YZ plane (North-South section) |  Yes |  0 |  0,3 |  0,1,2,3  
XSUBCELL |  Cell division in X direction. |  Yes |  1 |  1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
YSUBCELL |  Cell division in Y direction. |  Yes |  1 |  1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
ZSUBCELL |  Cell division in Z direction. | Yes | 1 | 1,20 |  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  
ORDER |  If non-zero then the process treats values of the CLASS field as an ordered numeric sequence, and infers intermediate values to generate a sequence of wireframe seam surfaces. A value of -1 indicates that the numeric sequence increases in value with depth, and +1 a decrease with depth. |  No |  0 |  -1,1 |  -1,0,1  
SURFACE |  This parameter is used to specify which wireframe surfaces are created: 1 - outer surface (Solid model only) 2 - inner surface (Solid model only) 3 - outer and inner surfaces (Solid model only) 4 - bottom surface 5 -top surface 6 - both bottom and top surfaces All options apply to a solid model (PLANE=0), but only 4,5 and 6 apply to seams (PLANE=1,2,3). |  Yes |  3 |  1,6 |  1,2,3,4,5,6  
COLOUR |  Colour for output wireframe. Only used if a colour field is not specified for MODCOL. |  No |  1 |  Undefined |  Undefined  
  
## Example
    
    
    !BLKTRI &IN(_vb_modopt),&WIRETR(wf_top_tr),  
  
---  
      
    
    &WIREPT(wf_top_pt),@PLANE(1),@XSUBCELL(1),   
      
    
       
      
    
     @YSUBCELL(1), @ZSUBCELL(1),@SURFACE(4),@COLOUR(1)  
      
    
    >>>    5452 Records in File ... wf_top_tr.dm <<<  
      
    
    >>>    5606 Records in File ... wf_top_pt.dm <<<  
      
    
    >>> BLKTRI   Complete <<<  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> Error: @PLANE and @SURFACE values inconsistent <<< |  BLKTRI requires the @PLANE (projection plane orientation) and @SURFACE (surface type to be created) parameters to be consistent, e.g. if @SURFACE is set to 4, 5 or 6 then @PLANE needs to be set to 1, 2 or 3 if. Fatal; the process is exited. |  Check that the @PLANE parameter is consistent with the defined @SURFACE parameter.