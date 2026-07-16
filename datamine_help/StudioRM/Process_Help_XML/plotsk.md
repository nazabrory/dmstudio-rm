# PLOTSK Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTSK" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTSK** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTSK>).

## Process Overview

Kidd Creek annotated section plot through drillholes.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input drillhole file, in standard sample format. If there is a field in this file, then the given colour number will be applied to each sample trace or barplot. |  Input |  Yes |  Drillhole  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Sample centre X co-ordinate. |  IN |  Yes |  Numeric |  X  
Y |  Sample centre Y co-ordinate. |  IN |  Yes |  Numeric |  Y  
Z |  Sample centre Z co-ordinate (elevation). |  IN |  Yes |  Numeric |  Z  
LENGTH |  Sample length. |  IN |  Yes |  Numeric |  LENGTH  
A0 |  Sample bearing. |  IN |  Yes |  Numeric |  A0  
B0 |  Sample dip. |  IN |  Yes |  Numeric |  B0  
BHID |  Drillhole identifier. |  IN |  Yes |  Numeric |  BHID  
FROM |  Downhole distance to sample top. |  IN |  Yes |  Numeric |  FROM  
TO |  Downhole distance to sample bottom. |  IN |  Yes |  Numeric |  TO  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
X1 |  X co-ordinate of section line start. |  Yes |  Undefined |  Undefined |  Undefined  
Y1 |  Y co-ordinate of section line start. |  Yes |  Undefined |  Undefined |  Undefined  
X2 |  X co-ordinate of section line end. |  Yes |  Undefined |  Undefined |  Undefined  
Y2 |  Y co-ordinate of section line end. |  Yes |  Undefined |  Undefined |  Undefined  
DISTANCE |  Maximum projection distance to section. drillhole intervals are clipped at the boundaries of the spatial window defined by the section line (**X1,Y1**) to (**X2,Y2**), the vertical coordinates from **YMIN** to **YMAX** and the thickness **DISTANCE** on both sides of the section line. |  Yes |  X1,Y1 |  Undefined |  Undefined  
NDP |  Number of decimal places for grade values. |  Yes |  Undefined |  Undefined |  Undefined  
ANGLE |  Angle for drillhole id, 0=horizontal, -90=vertically upwards, -= at angle of first sample (-). |  No |  - |  Undefined |  Undefined  
DHD |  Plot downhole distances at given interval (0). |  No |  0 |  Undefined |  Undefined  
XOFFSET |  Annotation offset in mm. to the right of sample centre at rt. angles to sample (0). |  No |  0 |  Undefined |  Undefined  
YOFFSET |  Annotation offset in mm. up from sample centre along sample (0). |  No |  0 |  Undefined |  Undefined  
LINECODE |  Line Type to be used to join each point. Default (1). Line Types: 1 : Solid line 2 : Bold line 3 : Dashed line 4 : Dotted line 5 : Dot-Dash line |  No |  1 |  1,5 |  1,2,3,4,5  
NOTICK |  |  Option |  Description  
---|---  
1 |  Suppress sample tick marks. (0).  
No |  0 |  0,1 |  0,1  
NOANNOT |  |  Option |  Description  
---|---  
1 |  Suppress BHID annotation (0).  
No |  0 |  0,1 |  0,1  
ANBOTHOL |  |  Option |  Description  
---|---  
1 |  BHID annotation at bottom of hole (0).  
No |  0 |  0,1 |  0,1  
DTRWIDTH |  Double trace width in mm. when the trace is in the section, 0 = single trace. (0). |  No |  0 |  Undefined |  Undefined  
PPSYMBOL |  Symbol at section plane Pierce Point (92). |  No |  92 |  Undefined |  Undefined  
PPSYMSIZ |  Pierce Point symbol size in mm. 0= no symbol (0). |  No |  0 |  Undefined |  Undefined  
ENEXDHD |  Annotate down the hole distance and distance from the section line at entry and exit. section entry and exit. (0) (0) = No annotation. 1 = Annotation. Distance from the secton line is positive on the side away from the viewer. -1 = Annotation. Distance from the section line is negative on the side away from the viewer. |  No |  0 |  -1,1 |  -1, 0, 1  
LINCOLFQ |  Trace colour in section far quarter. (14) |  No |  14 |  Undefined |  Undefined  
LINCOLCH |  Trace colour in section centre half. (14) |  No |  14 |  Undefined |  Undefined  
LINCOLCQ |  Trace colour in section close quarter. (14) |  No |  14 |  Undefined |  Undefined  
DTRTYPFQ |  Double trace line type when the trace is in the far quarter of the section.  1= Solid line.  2= Broad solid line.  3= Long dash 3 mm. dash, 3 mm. intervals.  4= Dots, 1 dot per mm. |  No |  4 |  1,4 |  1,2,3,4  
DTRTYPCH |  Double trace line type when the trace is in the central half of the section.  1= Solid line.  2= Broad solid line.  3= Long dash 3 mm. dash, 3 mm. intervals.  4= Dots, 1 dot per mm. |  No |  1 |  1,4 |  1,2,3,4  
DTRTYPCQ |  Double trace line type when the trace is in the closest quarter of the section. 1= Solid line.  2= Broad solid line.  3= Long dash 3 mm. dash, 3 mm. intervals.  4= Dots, 1 dot per mm. |  No |  3 |  1,4 |  1,2,3,4  
ANTICKM |  Tick marks to delineate annotations. These are single sided ticks, with a length equal to **XOFFSET**. 1= ticks, 0= no ticks. (1) |  No |  1 |  0,1 |  0,1  
VERBOSE |  0= Annotate only when the value changes. 1= Annotate all intervals even if the value of contiguous intervals is similar. (0) |  No |  0 |  0,1 |  0,1  
CHARSIZE |  Character size in millimetres (4). |  No |  4 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (14). |  No |  14 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot [Suggest 0]. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot [Suggest section length as defined by **X1** , **Y1** , **X2** , **Y2**]. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot [Lowest Z value]. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot [Highest Z value]. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined