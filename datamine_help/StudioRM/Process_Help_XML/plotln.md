# PLOTLN Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTLN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTLN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTLN>).

## Process Overview

Generates a line plot file from line segments. A line segment is identified by 4 fields * **X1** ,* **Y1** (the line start) and * **X2** ,* **Y2** (the line end).

The line type may be chosen by optional parameter, either broad or narrow. All points are connected in the order in which they appear in the file by the chosen line type.

Note: An empty plot file may be generated if the specified fields do not exist, or the line segments do not lie within the plot region.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. |  Input |  Yes |  Undefined  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X1 |  Line segment start X co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
Y1 |  Line segment start Y co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
X2 |  Line segment end X co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
Y2 |  Line segment end Y co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LINECODE |  Line type to be used to join each point. Default (1). Line Types: |  Option |  Description  
---|---  
1 |  Solid line  
2 |  Bold line  
3 |  Dashed line  
4 |  Dotted line  
5 |  Dot-Dash line  
No |  1 |  1,5 |  1,2,3,4,5  
SYMBOL |  Plotted symbol at each point.  Point symbol 

  * 91 : Circle (o) 
  * 92 : Cross (+) 
  * 93 : Cross (x) 
  * 94 : Triangle 
  * 95 : Box 
  * 96 : Diamond 
  * 97 : Star ( ) 
  * 98 : Pie Segment

|  No |  92 |  91,98 |  91,92,93,94,95,96,97,98  
SYMSIZE |  Symbol size in millimetres (3). Set to 0 for no symbol. |  No |  3 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !PLOTLN    &IN(LINESEGS),&PROTO(PLOTPROT),&PLOT(LINESEG.P),   
  
---  
      
    
    @XMIN=5000,@XMAX=10000,@YMIN=3000,@YMAX=8000,   
      
    
    *X1(XSTART),*Y1(YSTART),*X2(XEND),*Y2(YEND), @=3  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 411 <<< ( 0) IN TRANDP |  The scale has been defined or calculated as zero. Fatal; the process is exited.  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.