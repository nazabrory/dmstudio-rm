# PLOTPE Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTPE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTPE** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTPE>).

## Process Overview

Generate a plot file of perimeters.

All perimeters in the file are plotted; each perimeter is closed automatically onto its first point (unless @**NOCLOSE** =1). Perimeters may be annotated with their value contained in symbolic field * **AFIELD** (which by default has an actual name of **PVALUE**), by setting @**ANNOTATE** =1. The annotation is by the first point in each perimeter; the direction, size, and offset of the annotation from this point may be selected.

The perimeters are read from a file with the standard perimeter format; that is, the file must contain the explicit numeric fields **XP, YP, ZP, PTN, PVALUE**. All data points for one perimeter (identical value of **PVALUE**) should be together in the file, in point number (**PTN**) order; **PLOTPE** does not check this.

Typical use of the process is to plot a designed pit. However, because the @**NOCLOSE** =1 option is available to stop perimeters from being closed, it is possible to use **PLOTPE** to plot line segments, where each connected segment is defined by a different * **AFIELD** value and an unique **PVALUE**. Note that the * **AFIELD** field may be either alpha or numeric, so allowing text to be associated with each line segment if desired.

If the @**SYMSIZE** (symbol size) and @**SYMBOL** (symbol) parameters are set, it is possible to plot a user-defined symbol at each perimeter point. The default is no symbol (@**SYMSIZE** =0).

A special facility for crest representation is available. This facility is defined by the symbolic field * **SFIELD** , and by parameters @**SYLVALUE** and @**SYLSCALE**. All perimeters in which * **SFIELD** has a value equal to @SYLVALUE are plotted using the special slope crest representation at a size of @**SYLSCALE** millimetres. 

## Input Files

Name| Description| I/O Status| Required| Type  
---|---|---|---|---  
IN| Input perimeter file. Must contain the fields **XP, YP, ZP, PTN** and **PVALUE** (numeric, explicit).| Input| Yes| String  
PROTO| Plot prototype file. Must contain the fields **X, Y, S1, S2** and CODE (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit).| Input| Yes| Plot Prototype  
  
## Output Files

Name| I/O Status| Required| Type| Description  
---|---|---|---|---  
PLOT| Output| Yes| Plot| Output plot file.  
  
## Fields

Name| Description| Source| Required| Type| Default  
---|---|---|---|---|---  
AFIELD| Field used for annotation. Default is **PVALUE**.| IN| No| Any| Undefined  
SFIELD| Field used for crest symbol plotting.| IN| No| Numeric| Undefined  
XP| Field containing X coordinate.| IN| No| Numeric| Undefined  
YP| Field containing Y coordinate.| IN| No| Numeric| Undefined  
PCODE| The **PCODE** value will control the line code of each string. If used, it will override the **LINECODE** parameter.| IN| No| Numeric| Undefined  
SYMCODE| The **SYMCODE** value will control the symbol used on each string. If used, it will override the **SYMBOL** parameter.| IN| No| Numeric| Undefined  
PFILL| The **PFILL** value will control the filling of each string. If used, it will override the **FILLCODE** parameter.| IN| No| Numeric| Undefined  
  
## Parameters

Name| Description| Required| Default| Range| Values  
---|---|---|---|---|---  
LINECODE| | Option| Description  
---|---  
1| narrow line  
2| broad line  
3| dashed line  
4| dotted line  
5| long dash, short dash;  
6| dash dot  
7| dash dot dot  
8| zigzag line  
No| 1| 1,8| 1,2,3,4,5,6,7,8  
NOCLOSE| | Option| Description  
---|---  
0| joins the first and last points of the perimeter; =1 does not join the first and last points of the perimeter (0).  
No| 0| 0,1| 0,1  
SYMBOL| Plotted symbol at each point. Default (92). Point symbol number 

  * 91 : Circle (o) 
  * 92 : Cross (+) 
  * 93 : Cross (x) 
  * 94 : Triangle 
  * 95 : Box 
  * 96 : Diamond 
  * 97 : Star 

Can also be from the standard symbol set (codes 201 \- 267)( )| No| 92| 91,267| Undefined  
SYMSIZE| Symbol size in millimetres (0).| No| 0| Undefined| Undefined  
ANNOTATE| | Option| Description  
---|---  
0| no annotation;  
1| annotate at top;  
2| annotate at centre (0).  
No| 0| 0,2| 0,1,2  
AXOFFSET| Offset on the X axis of annotation (0).| No| 0| Undefined| Undefined  
AYOFFSET| Offset on the Y axis of annotation (0).| No| 0| Undefined| Undefined  
ANGLE| Angle of annotation from the X axis (0).| No| 0| -360,360| Undefined  
NDP| Number of decimal places in the annotation if the annotation field is numeric.| No| Undefined| Undefined| Undefined  
SYLVALUE| Value of **SFIELD** field for plotting of crest symbol.| No| Undefined| Undefined| Undefined  
SYLSCALE| Crest symbol line width in millimetres (3).| No| 3| Undefined| Undefined  
CHARSIZE| Character size in millimetres (3).| No| 3| Undefined| Undefined  
ASPRATIO| Aspect ratio, width / ht. for chars (0.9).| No| 0.9| Undefined| Undefined  
| Colour [as 'pen' number] for plot (1).| No| 1| Undefined| Undefined  
APPEND| Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0).| No| 0| 0,1| 0,1  
XMIN| Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype.| No| Undefined| Undefined| Undefined  
XMAX| Maximum value of X for plot.| No| Undefined| Undefined| Undefined  
YMIN| Minimum value of Y for plot.| No| Undefined| Undefined| Undefined  
YMAX| Maximum value of Y for plot.| No| Undefined| Undefined| Undefined  
XSCALE| X scale in user data units per millimetre.| No| Undefined| Undefined| Undefined  
YSCALE| Y scale in user data units per millimetre.| No| Undefined| Undefined| Undefined  
FILLCODE| Fill code for filling closed perimeters.| Option| Description  
---|---  
1 - 64| solid colour fill  
401 - 414| pattern fill  
3001 - 3030| hatch fill.  
No| Undefined| 1,3030| Undefined  
  
## Examples

### Example 1

Plot all perimeters from file perims. Each will be closed. There will be no annotation or symbols plotted:
    
    
    !PLOTPE   &IN(PERIMS),&PROTO(PLOTPROT),&PLOT(PERIMS.P),   
  
---  
      
    
    @XMIN=300,@XMAX=600,@YMIN=300,@YMAX=600  
  
### Example 2

A second plot with annotation on each perimeter and the symbol 'x' plotted at each point. The annotation is offset by 1 mm in Y from the point to allow space for the symbol, which is 2 mm high. The prototype used is the output from the previous plot, so there is no need to reset the data ranges **XMIN** ... **YMAX** :
    
    
    !PLOTPE   &IN(PERIMS),&PROTO(PERIMS.P),&PLOT(PERIMS1.P),@SYMBOL=93,  
  
---  
      
    
    @SYMSIZE=2,@ANNOTATE=1, @AYOFFSET=1,@=2,@CHARSIZE=2.5  
  
### Example 3

The line segments plotting facility is used. File **SEGDATA** contains a series of segments identified by fields **PVALUE** and **SEGNO**. Alphanumeric field **SEGNO** is used for the text annotation (* **AFIELD**) as defined by parameters @**ANNOTATE** , @**AXOFFSET** , @**AYOFFSET** , @**ANGLE** , @**CHARSIZE** and @**ASPRATIO**.
    
    
    !PLOTPE   &IN(SEGDATA),&PROTO(PROTOP),&PLOT(PLOTPE),  
  
---  
      
    
    *AFIELD(SEGNO),@LINECODE=1.0,@NOCLOSE=1.0, @SYMBOL=92.0,  
      
    
    @SYMSIZE=3.0,@ANNOTATE=2.0,@AXOFFSET=10.0,@AYOFFSET=-10.0,  
      
    
    @ANGLE=45.0, @CHARSIZE=3.0,@ASPRATIO=1.1,@=1.0,@APPEND=0.0  
  
### Example 4

The special crest plotting facility is used. When field **PTYPE** has a value of 3, the perimeter is plotted with crest symbols of 5 mm. The remaining perimeters are all plotted with narrow lines (@**LINECODE** =1) with points represented as a cross (@**SYMBOL** =92):
    
    
    !PLOTPE  &IN(PITPERS),&PROTO(PITPROT),&PLOT(PITPLOT),   
  
---  
      
    
             *SFIELD(PTYPE),@LINECODE=1.0,@NOCLOSE=0.0, @SYMBOL=92.0,@SYMSIZE=0.0,@ANNOTATE=0.0,   
      
    
             @AXOFFSET=0.0,@AYOFFSET=0.0,@ANGLE=0.0, @SYLVALUE=3.0,@SYLSCALE=5.0,@CHARSIZE=3.0,   
      
    
             @ASPRATIO=0.9,@=1.0,@APPEND=0.0  
  
## Error and Warning Messages

Message| Description  
---|---  
>>> ERR 411 <<< ( 0) IN TRANDP| The scale has been defined or calculated as zero. Fatal; the process is exited.  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE.>>> A NEW OUTPUT FILE WILL BE CREATED| The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES>>> NOT CONTAIN ALL THE REQUIRED FIELDS.>>> THE PLOT FILE WILL BE OVERWRITTEN.| The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<<>>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn>>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn>>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn| Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.  
>>> ERR 122 <<< ( fileno) IN PLOTPE>>> NOT A VALID PERIMETER FILE <<<| One or more of the fields **XP, YP, ZP, PTN** or **PVALUE** is missing in the input perimeter file. Fatal; the process is exited.  
>>> FIELD aaaaaaaa SPECIFIED FOR ANNOTATION DOES NOT EXIST IN FILE ffffffff.>>> PVALUE FIELD TAKEN AS DEFAULT.| The field entered for * **AFIELD** does not exist in the input perimeter file. The **PVALUE** field is taken for annotation and processing continues.