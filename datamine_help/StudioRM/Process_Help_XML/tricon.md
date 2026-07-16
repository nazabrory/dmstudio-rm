# TRICON Process  
  
To access this process:

  * Enter "TRICON" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **TRICON** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TRICON>).

## Process Overview

Generates contours directly from irregularly scattered data points or from a triangulated digital terrain model.

Contours are either simple unsmoothed straight-lines interpolated within the triangles, or are smoothed using the parametric quadratic Overhauser curve with linear blending function. The contours produced are annotated in either case.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Optional input data file. Must contain fields **X** , **Y** , **VALUE**. |  Input |  No |  Undefined  
WIREPT |  Optional input wireframe point file. |  Input |  No |  Wireframe Points  
WIRETR |  Optional input wireframe triangle file. |  Input |  No |  Wireframe Triangle  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2, CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. If no plot prototype file, then **XMIN, XMAX, YMIN, YMAX** taken from the model file on **IN**. |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X co-ordinate field in input file. |  IN |  No |  Numeric |  Undefined  
Y |  Y co-ordinate field in input file. |  IN |  No |  Numeric |  Undefined  
VALUE |  Field to be contoured. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VMIN |  Minimum contour value. |  Yes |  Undefined |  Undefined |  Undefined  
VMAX |  Maximum contour value. |  Yes |  Undefined |  Undefined |  Undefined  
CINT |  Contour interval. |  Yes |  Undefined |  Undefined |  Undefined  
DMAX |  Maximum separation of points to be joined. |  No |  Undefined |  Undefined |  Undefined  
SURFACE |  Optional surface identifier. +1 for upper surface, -1 for lower surface (+1). |  No |  +1 |  -1, 1 |  -1, 1  
OPTIMISE |  Linear or quadratic contour tracing; =0 linear; =1 quadratic (0). |  No |  0 |  0,1 |  0,1  
BOUNDARY |  |  Option |  Description  
---|---  
0 |  no boundary plotted; =1 boundary of data area plotted.  
No |  Undefined |  0,1 |  0,1  
DUPELIM |  Set to 1 to allow elimination of duplicate points (0). |  No |  0 |  0,1 |  0,1  
TOL |  Tolerance distance below which points are considered to be duplicated (0.00001). |  No |  0.00001 |  Undefined |  Undefined  
NDP |  Number of decimal places for annotation (0). |  No |  0 |  Undefined |  Undefined  
CHARSIZE |  Character size in millimeters (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimeter. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimeter. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !TRICON    &WIREPT(TOPOPT),&WIRETR(TOPOTR),&PROTO(TOPOPROT),          
  
---  
      
    
    &PLOT(TOPOCONT),@VMIN=150,@VMAX=250,@CINT=5,          
      
    
    @DUPELIM=1  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>>YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>>XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or **Y** equivalents must be entered either from the prototype of from parameters) or the combination given of XMI**N, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.  
>>>CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>>A NEW OUTPUT FILE WILL BE CREATED. |  The @APPEND parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>>ERROR \- CANNOT APPEND TO PLOT FILE AS IT DOES >>>NOT CONTAIN ALL THE REQUIRED FIELDS. >>>THE PLOT FILE WILL BE OVERWRITTEN. |  The @APPEND parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> ERR 121 <<< ( n) IN TRICON |  An error has occurred when reading the input raw data, point or triangle file. Fatal; the process is exited.  
>>>TRIANGLE FILE DEFINED, BUT >>>NO ASSOCIATED POINT FILE |  Fatal; the process is exited.  
>>>POINT FILE DEFINED, BUT >>>NO ASSOCIATED TRIANGLE FILE |  Fatal; the process is exited.  
>>>FIELD aaaaaaaa MISSING FROM POINT FILE |  One of the essential fields **XP, YP, ZP** or **PID** is missing from the input wireframe point file. Fatal; the process is exited.  
>>>FIELD aaaaaaaa MISSING FROM TRIANGLE FILE |  One of the essential fields **PID1, PID2, PID3, TRIANGLE** or **SID** is missing from the input wireframe triangle file. Fatal; the process is exited.