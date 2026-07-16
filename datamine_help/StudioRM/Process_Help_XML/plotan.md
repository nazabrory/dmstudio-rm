# PLOTAN Process

Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTAN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTAN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTAN>).

## Process Overview

**PLOTAN** is a general purpose scatter plot process, which may be used for such purposes as drillhole location maps, bench maps, and composite intersections with benches, as well as conventional scatter plots.

The input file should contain just one entry for each location. If it contains more than one, then there will be multiple plots at that location.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. |  Input |  Yes |  Undefined  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field to be plotted along X axis. |  IN |  Yes |  Numeric |  X  
Y |  Field to be plotted along Y axis. |  IN |  Yes |  Numeric |  Y  
VALUE |  Field for annotation. |  IN |  Yes |  Any |  Undefined  
CHARSZ |  Field to determine character size of annotation. If present it overrides the value of the **CHARSIZE** parameter. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
NDEC |  Decimal places for annotation. |  Yes |  Undefined |  Undefined |  Undefined  
XOFFSET |  Annotation offset from point in X in millimetres. |  Yes |  Undefined |  Undefined |  Undefined  
YOFFSET |  Annotation offset from point in Y in millimetres. |  Yes |  Undefined |  Undefined |  Undefined  
ANGLE |  Annotation angle from X axis. |  Yes |  0 |  0, 360 |  Undefined  
SYMBOL |  Plotted symbol at each point. Default (92). Point symbol number 91 : Circle (o) 92 : Cross (+) 93 : Cross (x) 94 : Triangle 95 : Box 96 : Diamond 97 : Star ( ) 98 : Pie Segment 112 : Hexagon |  No |  92 |  Undefined |  Undefined  
SYMSIZE |  Symbol size in millimetres (5). 0 for no symbol. |  No |  5 |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  1,64 |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !PLOTAN &IN(BCOLLS), &PROTO(PLOTPROT), &PLOT(BLOCPLOT), @XMIN=300,   
  
---  
      
    
    @XMAX=600, @YMIN=300, @YMAX=600, *X(XCOORD), *Y(YCOORD), *VALUE  
      
    
    (BHID),@NDEC=0, @XOFFSET=1, @YOFFSET=1, @ANGLE=0, @CHARSIZE=2.5, @=3  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 411 <<< ( 0) IN TRANDP |  The scale has been defined or calculated as zero. Fatal; the process is exited.  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX, and XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.