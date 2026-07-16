# PLOTTR Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTTR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTTR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTTR>).

## Process Overview

Generates a plan projection of the linkages in a wireframe model.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRETR |  Input wireframe triangle file. |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  Yes |  Wireframe Points  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LINECODE |  Line Type to be used to join each point. Line Types: 

  * 1 : Solid line 
  * 2 : Bold line 
  * 3 : Dashed line 
  * 4 : Dotted line 
  * 5 : Dot-Dash line

|  No |  1 |  1,5 |  1,2,3,4,5  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, assuming it exists and is a proper plot file (0). |  No |  0 |  0,1 |  0,1  
SYMBOL |  Plotted symbol at each point. Default (92). Point symbol number 

  * 91 : Circle (o) 
  * 92 : Cross (+) 
  * 93 : Cross (x) 
  * 94 : Triangle 
  * 95 : Box 
  * 96 : Diamond 
  * 97 : Star ( ) 
  * 98 : Pie Segment

|  No |  92 |  91,98 |  Undefined  
SYMSIZE |  Symbol size in millimetres (5). 0 for no symbol. |  No |  5 |  Undefined |  Undefined  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !PLOTTR &WIREPT(ZON2PT),&WIRETR(ZON2TR),&PROTO(ZON2WPRT),   
  
---  
      
    
     &PLOT(WZON2PLT)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED. |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> ERR 121 <<< ( n) IN PLOTTR |  An error has occurred when reading the input point or triangle file, for example, one or more of the essential fields in the file is absent or of the wrong type. Fatal; the process is exited.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX,** and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.