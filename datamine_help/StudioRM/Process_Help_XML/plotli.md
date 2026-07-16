# PLOTLI Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTLI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTLI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTLI>).

## Process Overview

Generate a line plot file.

The line type may be chosen by optional parameter. Currently available are broad or narrow. All points are connected in the order in which they appear in the file by the chosen line type.

**PLOTLI** may be used to plot a perimeter from a perimeter file. In this case the optional parameter @**CLOSE** =1 is specified to close the perimeter plot. If multiple perimeters exist in the perimeter file, then the required one should be selected by retrieval criteria, e.g. **PVALUE** =3.

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
X |  Line X co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
Y |  Line Y co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LINECODE |  Line Type to be used to join each point. Default (1). Line Types: |  Option |  Description  
---|---  
1 |  Solid line  
2 |  Bold line  
3 |  Dashed line  
4 |  Dotted line  
5 |  Dot-Dash line  
No | 1 | 1,5 | 1,2,3,4,5  
CLOSE |  |  Option |  Description  
---|---  
1 |  joins the first and last points [for perimeters].  
No |  0 |  0,1 |  0,1  
SYMBOL |  Plotted symbol at each point.  Point symbol number 91 : Circle (o) 

  * 92 : Cross (+) 
  * 93 : Cross (x) 
  * 94 : Triangle 95 : Box 
  * 96 : Diamond 
  * 97 : Star ( ) 
  * 98 : Pie Segment

|  No |  92 |  91,98 |  91,92,93,94,95,96,97,98  
SYMSIZE |  Symbol size in millimetres (3). Set to 0 for no symbol. |  No |  3 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Examples

### Example 1

The following example shows plotting of a variogram file:
    
    
    !PLOTLI   &IN(VGRAM),&PROTO(PLOTPROT),&PLOT(VGRMPLOT),   
  
---  
      
    
    @XMIN=0,@XMAX=25,@YMIN=0,@YMAX=2.5, *X(LAG),*Y(V.GRAM),@=3  
  
### Example 2

An example of plotting a single perimeter from a perimeter file:
    
    
    !PLOTLI   &IN(PERIMS),&PROTO(PLOTPROT),&PLOT(PERIM2.P),  
  
---  
      
    
    @XMIN=200, @XMAX=1000,@YMIN=500,@YMAX=1300,  
      
    
    *X(XP),*Y(YP),@CLOSE=1, PVALUE=2  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 411 <<< ( 0) IN TRANDP |  The scale has been defined or calculated as zero. Fatal; the process is exited.#12;>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE.  
>>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.