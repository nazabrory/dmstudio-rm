# CONTST Process  
  
To access this process:

  * **Model** ribbon **> > Data from Model >> Contours**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CONTST** and click **Run**.
  * Enter "CONTST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CONTST>).

## Proces Overview

Generate contours from a block model and stores them in three dimensional format into a string file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. Must contain fields XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK + FIELD field. |  Input |  Yes |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  String |  Output string file, containing fields XP,YP,ZP, PTN,PVALUE,P.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
FIELD |  Field to be contoured. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VMIN |  Minimum contour value. |  Yes |  Undefined |  Undefined |  Undefined  
VMAX |  Maximum contour value. |  Yes |  Undefined |  Undefined |  Undefined  
CINT |  Contour interval. |  Yes |  Undefined |  Undefined |  Undefined  
GRIDINT |  Grid interval for contouring. |  Yes |  Undefined |  Undefined |  Undefined  
PLANE |  Plane, 'XY', 'XZ' or 'YZ' through the model. Default is the XY plane. |  No |  'XY' |  Undefined |  'XY', 'XZ','YZ'  
POSITION |  Position of the plane. For example if the XY plane is used a Z position is needed. Only required if neither TOP nor BOTTOM are specified. |  No |  Undefined |  Undefined |  Undefined  
TOP |  Value of FIELD for which top of seam contour required. Only required if neither POSITION nor BOTTOM appear. |  No |  Undefined |  Undefined |  Undefined  
BOTTOM |  Value of FIELD for which base of seam contour required. Only required if neither POSITION nor TOP appear. |  No |  Undefined |  Undefined |  Undefined  
SMPASS |  Number of smoothing passes required (1). |  No |  1 |  Undefined |  Undefined  
SMFACTOR |  Smoothing factor in the range 0 [minimum smoothing] to 1 [maximum smoothing] (0.5). |  No |  0.5 |  0,1 |  Undefined  
SMTHRESH |  Smoothing threshold used for operations of types 3,6, and 7 only (0.0). |  No |  0.0 |  Undefined |  Undefined  
OPTYPE |  Smoothing operation type (4) selected from:- |  Option |  Description  
---|---  
1 |  Laplacian (non-directional 2nd partial derivative) function on surface - used as an indicator of curvature, for example for identification of discontinuities.  
2 |  Sq root of sum of 1st partial derivatives, a measure of the surface gradient.  
3 |  Adaptive noise reduction for smoothing in areas where difference between adjacent grid values exceeds THRESH.  
4 |  Local 5-point mean for smoothing.  
5 |  Local 5-point standard deviation.  
6 |  Lower thresholding - replace all values below THRESH by the THRESH value.  
7 |  Upper thresholding - replace all values above THRESH by the THRESH value.  
8 |  Minkowski dilatation - extend grid outward by one element using local average value.  
No |  4 |  1,8 |  1,2,3,4,5,6,7,8  
HILIGHT |  Highlight every Nth contour with different colour. |  No |  Undefined |  Undefined |  Undefined  
HICOLOUR |  Colour for highlighting (2). |  No |  2 |  1,64 |  Undefined  
COLOUR |  Default colour for plot (1). |  No |  1 |  1,64 |  Undefined  
  
## Example
    
    
    !CONTST    &IN(FEMODEL), &OUT(FESTRS),*FIELD(Fe), @POSITION=-45,   
  
---  
      
    
             @VMIN= 30, @VMAX=80, @CINT=5, @GRIDINT=10, @HILIGHT=5, @HI=4,   
      
    
             @OPTYPE= 6