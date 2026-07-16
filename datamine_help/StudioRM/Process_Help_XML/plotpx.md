# PLOTPX Process

Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTPX" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTPX** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTPX>).

## Process Overview

Enhanced perimeter plotting.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input perimeter file. Must contain the fields **XP, YP, ZP, PTN** and **PVALUE** (numeric, explicit). |  Input |  Yes |  String  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). |  Input |  Yes |  Plot Prototype  
IN2 |  Optional 2nd input perimeter file containing annotation and slope lines. Should contain std perimeter fields, plus an optional alpha field for annotation (max 40 chars) |  Input |  No |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
AFIELD |  Field used for perimeter annotation. Default is **PVALUE**. May be alpha up to 8 characters. |  IN |  No |  Any |  Undefined  
DASH |  Field used for dashing patterns [1-4]. (0) |  IN |  No |  Numeric |  0  
NOANNO |  Field used for to prevent annotation of a perimeter under a range of conditions: 0 = no effect 1 = no annotation at all on the perimeter 2 = no road annotion on the perimeter 3 = no annotation of the perimeter if annotation lines are present and it is not intersected. 4 = combination of 2 |  IN |  No |  Numeric |  Undefined  
AUXANNO |  Field used for free form annotation in IN2. |  IN2 |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ANNOTATE |  Type of annotation. (0) 

  * 0 = no annotation 
  * 1 = annotate perimeter ends
  * 2 = annotate perimeter centre 
  * 3 = inline perimeter annotation and/or use IN2 file to define annotation, slope intersections, and free form annotations.

|  No |  0 |  0,3 |  0,1,2,3  
LINECODE |  |  Option |  Description  
---|---  
1 |  narrow line; =2 broad line (1).  
No |  1 |  1,2 |  1,2  
NOCLOSE |  |  Option |  Description  
---|---  
0 |  joins the first and last points of the perimeter;  
1 |  does not join the first and last points of the perimeter (0).  
No |  0 |  0,1 |  0,1  
SYMBOL |  Plots the symbol specified at each perimeter point 91=o, 92=+, 93=x (92). |  No |  92 |  Undefined |  Undefined  
SYMSIZE |  Symbol size in millimetres (0). |  No |  0 |  Undefined |  Undefined  
AXOFFSET |  Offset on the X axis of annotation (0). |  No |  0 |  Undefined |  Undefined  
AYOFFSET |  Offset on the Y axis of annotation (0). |  No |  0 |  Undefined |  Undefined  
ANGLE |  Angle of annotation from the X axis (0). |  No |  0 |  -360, 360 |  Undefined  
NDP |  Number of decimal places in the annotation if the annotation field is numeric. |  No |  Undefined |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). 0 indicates use the colour field. Parameters specific to annotate |  No |  1 |  Undefined |  Undefined  
NOINTANN |  0 = annotate non intersected perimeters (1) 1 = Do not annotate non intersected perimeters |  No |  1 |  0,1 |  0,1  
CHARSMIN |  Minimum character size in millimetres (0.8). |  No |  0.8 |  Undefined |  Undefined  
INTERVAL |  Interval for perimeter annotation when no annotation lines, in mm. [default is 120] |  No |  Undefined |  Undefined |  Undefined  
ROADANN |  For annotate=3: (0) 0 = no annotation at road bends 1 = annotate contours at road bends, with line 2 = annotate contours at road bends, with cross |  No |  0 |  0,2 |  0,1,2  
SLOPEANN |  For annotate=3: (1) 1 = just plot slope lines 2 = plot slope lines 3 = plot lines 4 = plot lines, offsetting, |  No |  1 |  1,4 |  1,2,3,4  
SLOPECOL |  Colour of 'slope symbols', for annotate=3 (-1) -1 = same as default parameter 0 = use colour field if present >=1 = any other colour. Default is -1. |  No |  -1 |  -1,64 |  Undefined  
BENCHCOL |  Colour of bench RL's, for annotate=3 (-1) -1 = same as default parameter 0 = use colour field if present >=1 = any other colour. Default is -1. |  No |  -1 |  -1,64 |  Undefined  
FFANNCOL |  Colour of free form annotation, for annotate=3 -1 = same as default parameter 0 = use colour field if present >=1 = any other colour. Default is -1. (-1) |  No |  -1 |  -1,64 |  Undefined  
FFANNSZ |  default character size of free form annotation, for annotate=3 (-1) Remaining parameters |  No |  -1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined