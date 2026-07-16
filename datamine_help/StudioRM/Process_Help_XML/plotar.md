# PLOTAR Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTAR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTAR** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTAR>).

## Process Overview

Generate a scatter plot file, where each data point is annotated with an arrow symbol plotted relative to the X,Y data point.

The input file should contain just one entry for each location. If it contains more than one, then there will be multiple plots at that location.

The length and direction of the arrows plotted are specified by the values of *LENFLD and *AZIFLD in the input data file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. Must contain the fields defined by parameters **XFLD, YFLD, LENFLD** and **AZIFLD**. |  Input |  Yes |  Undefined  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2, CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last six values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot File |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
XFLD |  Field to be plotted along X axis. |  IN |  Yes |  Numeric |  Undefined  
YFLD |  Field to be plotted along Y axis. |  IN |  Yes |  Numeric |  Undefined  
LENFLD |  Field controlling arrow length. |  IN |  Yes |  Numeric |  Undefined  
AZIFLD |  Field controlling arrow direction in degrees clockwise from north. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ASCALE |  Scale for **LENFLD** in data units per plotted millimetre. |  Yes |  Undefined |  Undefined | Undefined  
DRAWHEAD |  Controls plotting of arrow head, 0 - No Arrow Head to be plotted. 1 - Arrow Head to be plotted. Default: (0) |  No |  0 |  0,1 |  0,1  
POSITION |  Position at which arrow is plotted relative to point X Y: |  Option |  Description  
---|---  
1 |  \- Plot Arrow Head at position [X,Y].  
2 |  \- Plot Arrow Tail at position [X,Y].  
3 - Centre Arrow at position [X,Y]. Default |  (3)  
No |  3 |  1,3 |  1,2,3  
HEADSIZE |  Length in millimetres of arrow head. Default: (3.0) |  No |  3.0 |  Undefined |  Undefined  
HEADANGL |  Angle in degrees between left and right lines of arrow head. Default: (90) |  No |  90 |  1,90 |  Undefined  
CHARSIZE |  Character size in millimeters. Default: (4) |  No |  4 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / hieght for characters. Default: (0.9) |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot. Default: (1) |  No |  1 |  1,64 |  Undefined  
XMIN |  Minimum value of X for plot. Not required if the values **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** are already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. Not required if the values **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** are already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. Not required if the values **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** are already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. Not required if the values **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** are already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimeter. Not required if the values **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** are already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimeter. Not required if the values **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** are already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !PLOTAR  &IN(SEDREG),&PROTO(REGPROT),&PLOT(SEDREGA.P),  
  
---  
      
    
    *XFLD(EAST), *YFLD(NORTH),*LENFLD(CU),*AZIFLD(BRNG),@ASCALE=50,   
      
    
    @DRAWHEAD=1,@POSITION=3,@HEADANGL=60  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX, and XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.  
>>> Invalid Arrow Position Ind. <<< |  The @**POSITION** parameter must have a value of 1, 2 or 3.