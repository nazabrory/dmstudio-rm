# PLOTCX Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTCX" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTCX** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTCX>).

## Process Overview

Spline contouring in plan, orthogonal sections or a rotated section plane with point, wireframe or block model data.

Contours can be specified in four ways:

  1. In the simplest case contours are specified with the parameters **CMIN, CMAX, CINT, CHARSZ, NDP, HILIGHT** and **HI**. The remaining methods are specified with a **CONTOUR** control file:

  2. Specify individual contour values with the **CVALUE** field.

  3. Specify a sequence of contour values and replicate the contour values by adding the difference between the smallest and largest contour values to each contour in turn. This method can be applied to contouring data on a logarithmic annotation interval.

  4. Specify major and minor contour intervals such that all contour intervals are multiples of the smallest interval.

Data in the CINT field can be bounded by values in the **CMIN** and **CMAX** parameters. Additional control on contour display is available with the use of optional fields **C, LINECODE, CHARSZ, NDP, ANNOTATE** and **DENSITY** fields. These controls can be specified for individual contours, and groups of contours.

Further parameters are supplied to control the interpretation of the contour specification. **FREQ** requests that the distribution of the contoured data be analyzed to plot contours at the frequency intervals requested. **LOG** requests a logarithmic transformation of the data before applying the contour specification.

The data to be contoured can be handled in 3 ways:

  1. Plotting in the XY plane using data limits supplied by the plot prototype. This case is applied to point data with the **X , Y** and **VALUE** fields specified, or wireframe data where the elevation ZP is contoured. The **PLANE** parameter should not be supplied, or three dimensional coordinates will be expected in the input point file.

  2. Projection of point data, wireframes, or sampling of models in one of the three orthogonal directions using the plot prototype to define the data limits in the nominated view.

  3. Projection of data onto a plane defined by a section definition, using the clipping parameters **DPLUS** and **DMINUS** for point or wireframe data. The distance of the points from the plane is contoured unless a field is specified with **FIELD**. Models are intersected with the section plane and the intersected block values contoured.  
A grid can be overplotted in the section plane.

The data from the point, wireframe or model is triangulated and contoured on the nominated mesh interval, with optional control on the location of the mesh origin. For model data, the mesh origin and size should be based on the model data definition.

The process will accept a model which has been defined using the Rotated Model option in [PROTOM](<protom.md>). A message will be displayed to show that the model has been identified as a Rotated Model.

Note: Additional smoothing and extrapolation can be applied prior to contouring.

The contour strings can be output to a string file. The contours generated can be clipped to a bounding perimeter.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2, CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. Optional only if **APPEND** =1 |  Input |  No |  Plot Prototype  
SECTION |  Optional section definition file. |  Input |  No |  Section Definition  
BOUND |  Optional bounding perimeter. No contours will produced outside this perimeter. Must contain fields **XP, YP, ZP, PTN** and **PVALUE**. This file must contain only one perimeter, must be clockwise and must not be closed. |  Input |  No |  String  
POINT |  Input raw data point file. |  Input |  No |  Points  
WIRETR |  Input wireframe triangle file. |  Input |  No |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  No |  Wireframe Points  
MODEL |  Input model file. Must contain fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK** and **FIELD**. If it is a Rotated Model then it must also include the fields **X0, Y0, Z0, ANGLE1, ANGLE2, ANGLE3, ROTAXIS1, ROTAXIS2** , and **ROTAXIS3**. |  Input |  No |  Block Model  
CONTOUR |  Input file containing one or more of the following fields to specify control over contour output: 

  * **CVALUE** Individual contour values. 
  * **CINT** Contour interval. C Contour colour value. 
  * **LINECODE** Contour linecode 1001 and so on.
  * **CHARSZ** Annotation character size. 
  * **NDP** Number of decimal places. 
  * **ANNOTATE** Frequency of contour line annotation in millimetres. 
  * **DENSITY** Maximum contour density in lines per millimetre. The contour specification will be interpreted in logarithmic values if **NLOG** >0 and frequency percentages if **FREQ** >0.0.

|  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
STRING |  Output |  No |  String |  Optional output string file. If selected this file be written out as well as the plot file and will contain fields **XP, YP, ZP, PTN** and **PVALUE**. The value of **PVALUE** field is determined from the **PVALST** and **PVALIN** parameters.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X field in input point file. Only required if contouring raw data. |  POINT |  No |  Numeric |  Undefined  
Y |  Y field in input point file. Only required if contouring raw data. |  POINT |  No |  Numeric |  Undefined  
Z |  Z field in input point file. Only required if contouring raw data, and either the **PLANE** parameter or a section definition file is supplied. |  POINT |  No |  Numeric |  Undefined  
FIELD |  Field to be contoured. Required for contouring raw data or solid model. Optional for contouring a wireframe. |  Undefined |  No |  Undefined |  Undefined  
SEAM |  Seam ID field. Only required if contouring solid model. |  MODEL |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PLANE |  Plane, 'XY', 'XZ' or 'YZ' through the data for projection of data onto a plane. |  No |  'XY' |  Undefined |  'XY', 'XZ', 'YZ'  
POSITION |  Position of the plane. For example if the XY plane is used a Z position is needed. Only required if neither **TOP** nor **BOTTOM** are specified. |  No |  Undefined |  Undefined |  Undefined  
TOP |  Value of **FIELD** for which top of seam contour required. Only required if neither **POSITION** nor **BOTTOM** appear. |  No |  Undefined |  Undefined |  Undefined  
BOTTOM |  Value of FIELD for which base of seam contour required. Only required if neither **POSITION** nor **TOP** appear. Both **TOP** and **BOTTOM** set for an isopach. |  No |  Undefined |  Undefined |  Undefined  
TYPE |  Force the interpretation of the command line and contour specification file data: - derived from the parameters/files supplied |  Option |  Description  
---|---  
0 |  command line parameters  
1 |  contour values from **CVALUE** field  
2 |  contour values from **CVALUE** field with repetition in cycles  
3 |  major/minor contour intervals from **CINT** field.  
No |  0 |  0,3 |  0,1,2,3  
LOG |  Logarithmic conversion of data to be contoured to base 10 [1] or base e [2], with the contour specification interpreted in logarithmic values. Default is no conversion (0). |  No |  0 |  0,2 |  0,1,2  
FREQ |  Convert the data to be contoured to a frequency distribution, apply the specified contour values as percentages, and annotate the raw data values (0). |  No |  0 |  0,1 |  0,1  
SYSTEM |  If set to 3 then perimeters in the BOUND and STRING files are treated as true 3D. eg if the graphics display is showing a YZ plane then a perimeter in this plane should have **YP** and **ZP** varing with **XP** constant. The default is (2). Under the default system **XP** and **YP** vary and **ZP** is constant, whichever plane is displayed. |  No |  2 |  2,3 |  2,3  
SECTION |  Force the specification of a section definition if non-zero (0). The definition can also be selected from the section definition file, if supplied. |  No |  0 |  0,1 |  0,1  
DPLUS |  The search distance measured in the increasing direction from the section definition plane. |  No |  Undefined |  Undefined |  Undefined  
DMINUS |  The search distance measured in the decreasing direction from the section definition plane. |  No |  Undefined |  Undefined |  Undefined  
XGORIG |  Grid origin of mesh in user data units on the horizontal plotted axis. If a section definition is specified, then supply the true X coordinate (-). |  No |  - |  Undefined |  Undefined  
YGORIG |  Grid origin of mesh in user data units on the vertical plotted axis. If a section definition is specified, then supply the true Y coordinate (-). |  No |  - |  Undefined |  Undefined  
ZGORIG |  Grid origin of mesh in user data units in the true Z coordinate for a section definition (-). |  No |  - |  Undefined |  Undefined  
GRIDHINC |  Grid interval of mesh in user data units on the horizontal plotted axis (-). |  No |  - |  Undefined |  Undefined  
GRIDVINC |  Grid interval of mesh in user data units on the vertical plotted axis (-). |  No |  - |  Undefined |  Undefined  
GRIDINC |  Alternate specification of regular mesh interval in user data units (-). |  No |  - |  Undefined |  Undefined  
NOX |  Maximum number of mesh intervals on the horizontal plotted axis (-). |  No |  - |  Undefined |  Undefined  
NOY |  Maximum number of mesh intervals on the vertical plotted axis (-). |  No |  - |  Undefined |  Undefined  
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
CSMOOTH |  Smoothing factor to apply in contour generation by controlling the maximum step size in a mesh interval. A value of 0.1 will produce a smooth contour, 0.5 will produce a coarse contour. Use one of 0.1, 0.25 0.5 (0.1). |  No |  0.1 |  Undefined |  Undefined  
MAXLINK |  The maximum separation of points that will be joined by a triangle. By default a convex hull will be formed around all points (+). |  No |  + |  Undefined |  Undefined  
CELLSAMP |  The number of intervals to sample cells to approximate the subcell variation for orthogonal plane contouring of models (1). |  No |  1 |  Undefined |  Undefined  
EXTRAP |  Distance to extrapolate the data before contouring in the plane of the contour (0). |  No |  0 |  Undefined |  Undefined  
GSMOOTH |  Smoothing factor to apply to the mesh data before contouring. A value between 0 and 1 will interpolate a result between the triangulated value at 0 and an inverse distance result for 1 (0). |  No |  0 |  0,1 |  Undefined  
POWER |  Interpolation power (2). |  No |  2 |  Undefined |  Undefined  
RADIUS |  Interpolation search radius (+). |  No |  + |  Undefined |  Undefined  
B |  Colour for plotting boundary outline (-). |  No |  - |  Undefined |  Undefined  
BCODE |  Linecode for plotting boundary outline (1001). |  No |  1001 |  Undefined |  Undefined  
PVALST |  If **STRING** file requested, for the first string to be written **PVALUE** will be set to **PVALST**. For the following strings **PVALUE** is incremented by **PVALINC** (1.0). |  No |  1.0 |  Undefined |  Undefined  
PVALINC |  If **STRING** file requested, **PVALUE** value increment (1.0). |  No |  1.0 |  Undefined |  Undefined  
GRCOLR |  Preferred grid colour where a grid is to be plotted for a specified section definition (-). |  No |  - |  Undefined |  Undefined  
XGRIDINT |  X grid interval, 0 no X grid (0). |  No |  0 |  Undefined |  Undefined  
YGRIDINT |  Y grid interval, 0 no Y grid (0). |  No |  0 |  Undefined |  Undefined  
ZGRIDINT |  Z grid interval, 0 no Z grid (0). |  No |  0 |  Undefined |  Undefined  
XGRIDNDP |  X grid number of decimal places (0). |  No |  0 |  Undefined |  Undefined  
YGRIDNDP |  Y grid number of decimal places (0). |  No |  0 |  Undefined |  Undefined  
ZGRIDNDP |  Z grid number of decimal places (0). |  No |  0 |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. If specified here or in **PROTO** this value will override section limits. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. If specified here or in **PROTO** this value will override section limits. |  No |  Undefined |  Undefined |  Undefined  
VERTEXAG |  Controls vertical exaggeration when a section definition file is included. This must be set to allow different scales. The default is forced equal scales (1). If the input model is a Rotated Model then the process will always set **VERTEXAG** to 1 and display a warning message. = 0 allows different scales for both axes determined by **XSCALE** and **YSCALE** if provided or else by filling the data area to the section limits. > 0 sets value of **XSCALE** /**YSCALE**. |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
PRINT |  >0 to display contouring information. 1 contour control file 2 mesh values |  No |  Undefined |  Undefined |  Undefined