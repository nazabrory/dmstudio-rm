# PLOTDA Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTDA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTDA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTDA>).

## Process Overview

Generate a scatter plot file, where each data point is annotated with a symbol centered on the point.

The input file should contain just one entry for each location. If it contains more than one, then there will be multiple plots at that location.

Unlike [PLOTAN](<plotan.md>), where the value of a third field is plotted at the point, and therefore there must be this third field, **PLOTDA** can be used to provide pure X-Y plots without a third field. However, if required, the size of the symbol chosen may be varied according to the value of a third field.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. |  Input |  Yes |  Undefined  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot File |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field to be plotted along X axis. |  IN |  Yes |  Numeric |  Undefined  
Y |  Field to be plotted along Y axis. |  IN |  Yes |  Numeric |  Undefined  
VALUE |  Field to be used for defining symbol size. |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
VMAX |  **VALUE** value for 2.5 millimetre diameter symbol (2.5). |  No |  2.5 |  Undefined |  Undefined  
SYMBOL |  Plotted symbol at point. Default (91). Point symbol number 91 : Circle 92 : Cross [+] 93 : Cross [x] 94 : Triangle 95 : Box 96 : Diamond 97 : Star [ ] 98 : Pie Segment 112 : Hexagon |  No |  91 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !PLOTDA &IN(ASSAYS),&PROTO(PLOTPROT),&PLOT(SCATPLOT),   
  
---  
      
    
    @XMIN=0,@XMAX=10,@YMIN=0,@YMAX=15,   
      
    
    *X(CU),*Y(AU),*VALUE(DEPTH), @VMAX=100  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.