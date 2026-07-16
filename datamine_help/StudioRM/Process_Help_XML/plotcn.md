# PLOTCN Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTCN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTCN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTCN>).

## Introduction

Spline contouring in plan or orthogonal sections for point, wireframe or block model data.

Contours can be specified with the parameters **CMIN, CMAX, CINT, , CHARSZ, ANNOTATE, DENSITY, NDP, HILIGHT** and **HI**.

The data from the point, wireframe or model is triangulated and contoured on the nominated mesh interval. Additional smoothing and extrapolation can be applied prior to contouring. The contour strings can be output to a string file.

  * The scale parameters (@**XMIN** , @**XMAX** , @**YMIN** , @**YMAX** , @**XSCALE** , @**YSCALE**) are only optional if the scale or extents have been supplied through a plot prototype file.
  * When **PLOTCN** is run with @**SYSTEM** =2.0, the result is a "2d" string file with no notion of orientation, and is displayed in a plan view.

  * When **PLOTCN** is run with @**SYSTEM** =3.0, the "height" of the contours, (the Z-coordinate) gets the value of the field which is being contoured. For this reason contour strings will not match up in 3D space with the plane through the block model along which values were contoured. The contour strings could be processed using **[EXTRA](<extra.md>)** , in order to shift them into the required position in 3D space.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2, CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. Optional only if **APPEND** =1 |  Input |  No |  Plot Prototype  
POINT |  Input raw data point file. |  Input |  No |  Points  
WIRETR |  Input wireframe triangle file. |  Input |  No |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  No |  Wireframe Points  
MODEL |  Input model file. Must contain fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK** and **FIELD** field. |  Input |  No |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
STRING |  Output |  No |  String |  Optional output string file. If selected this file be written out as well as the plot file and will contain fields **XP, YP, ZP, PTN and PVALUE. The value of PVALUE** field is determined from the **PVALST** and **PVALINC** parameters.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X field in input point file. Only required if contouring raw data. |  POINT |  No |  Numeric |  Undefined  
Y |  Y field in input point file. Only required if contouring raw data. |  POINT |  No |  Numeric |  Undefined  
Z |  Z field in input point file. Only required if contouring raw data, and the **PLANE** parameter is supplied. |  POINT |  No |  Numeric |  Undefined  
FIELD |  Field to be contoured. Only required if contouring raw data or solid model. |  POINT, MODEL |  No |  Numeric |  Undefined  
SEAM |  Seam ID field. Only required if contouring solid model. |  MODEL |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PLANE |  Plane, 'XY', 'XZ' or 'YZ' through the data for projection of data onto a plane. |  No |  'XY' |  Undefined |  'XY', 'XZ', 'YZ'  
POSITION |  Position of the plane. For example if the XY plane is used a Z position is needed. Only required if neither **TOP** nor **BOTTOM** are specified. |  No |  Undefined |  Undefined |  Undefined  
TOP |  Value of FIELD for which top of seam contour required. Only required if neither **POSITION** nor **BOTTOM** appear. |  No |  Undefined |  Undefined |  Undefined  
BOTTOM |  Value of FIELD for which base of seam contour required. Only required if neither **POSITION** nor **TOP** appear. Both **TOP** and **BOTTOM** set for an isopach. |  No |  Undefined |  Undefined |  Undefined  
SYSTEM |  If set to 3 then perimeters in the **STRING** file are treated as true 3D. eg if the graphics display is showing a YZ plane then a perimeter in this plane should have YP and ZP varing with XP constant. The default is (2). Under the default system XP and YP vary and ZP is constant, whichever plane is displayed. |  No |  2 |  2,3 |  2,3  
GRIDINC |  Mesh interval in user data units (-). |  No |  - |  Undefined |  Undefined  
CMIN |  Minimum contour value in user data units. |  No |  Undefined |  Undefined |  Undefined  
CMAX |  Maximum contour value in user data units. |  No |  Undefined |  Undefined |  Undefined  
CINT |  Contour interval in user data units. |  No |  Undefined |  Undefined |  Undefined  
HILIGHT |  Highlight every Nth contour with HI. |  No |  Undefined |  Undefined |  Undefined  
HI |  Colour [as 'pen' number] for highlighting. |  No |  Undefined |  Undefined |  Undefined  
CHARSZ |  Character size in millimetres for contour annotation (3.5). |  No |  3.5 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
NDP |  Number of decimal places for annotation. |  No |  Undefined |  Undefined |  Undefined  
ANNOTATE |  Frequency of contour line annotation in millimetres (100). |  No |  100 |  Undefined |  Undefined  
DENSITY |  Maximum contour density in contour lines per millimetre. A default cutout is applied if not specified (0). |  No |  0 |  Undefined |  Undefined  
MAXLINK |  The maximum separation of points that will be joined by a triangle. By default a convex hull will be formed around all points (+). |  No |  + |  Undefined |  Undefined  
EXTRAP |  Distance to extrapolate the data before contouring in the plane of the contour (0). |  No |  0 |  Undefined |  Undefined  
GSMOOTH |  Smoothing factor to apply to the mesh data before contouring. A value between 0 and 1 will interpolate a result between the triangulated value at 0 and an inverse distance result for 1 (0). |  No |  0 |  Undefined |  Undefined  
POWER |  Interpolation power (2). |  No |  2 |  Undefined |  Undefined  
RADIUS |  Interpolation search radius (+). |  No |  + |  Undefined |  Undefined  
PVALST |  If STRING file requested, for the first string to be written **PVALUE** will be set to **PVALST**. For the following strings **PVALUE** is incremented by **PVALINC** (1.0). |  No |  1.0 |  Undefined |  Undefined  
PVALINC |  If **STRING** file requested, **PVALUE** value increment (1.0). |  No |  1.0 |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
PRINT |  >0 to display the contouring information. |  No |  0 |  0,1 |  0,1  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<<  
>>> XMIN, XMAX = -0.10E+31 0.10E+31  
>>> YMIN, YMAX = -0.10E+31 0.10E+31  
>>> XSCALE , YSCALE = -0.10E+31 -0.10E+31 |  Check the defined minimum, maximum and scale settings.  
>>> *FIELD not found for MODEL file <<< |  The specified field in * **FIELD** does not exist. Select an existing field name.