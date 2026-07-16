# PLOTSI Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTSI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTSI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTSI>).

## Process Overview

Scatter plot of data with optional annotation of the selected data fields and plotting of symbols and icons.

The process combines the functionality of **[PLOTAN](<plotan.md>)** , **[PLOTDA](<plotda.md>)** , and **[PLOTVA](<plotva.md>)** , and interactive ICON plotting in **[PLTLAY](<pltlay.md>)**.

Plotting with predefined icons, allows control on location, scaling and rotation of the icons. Data related text that should be displayed with the icon can be included with the **PLOTSI** process.

Control is supplied by parameters from the command line, or through data values supplied as fields. The default field names are the same as the parameter names. Alternative field names can be supplied by using the parameter names as symbolic field names.

Where both the parameter and field names are supplied, the field value will have priority over the parameter, providing it is not absent or blank.

Normally the field values will be entered with **[AED](<aed.md>)** , expanded into the data files with **[ATTSET](<attset.md>)** , and supplied with standard default values from a menu system.

The standard field/parameter names accepted are outlined below. The presence of a field specific to each type of plotting will act as a trigger to indicate the user requirements. More than one type of plotting is possible within a single run.

##### Annotation:

FIELD  |  The field to be annotated  
---|---  
NDEC  |  Number of decimal places for annotation  
CHARSIZE  |  Character size  
ASPRATIO  |  Aspect ratio  
XOFFSET  |  Annotation offset from point in X  
YOFFSET  |  Annotation offset from point in Y  
ANGLE  |  Annotation angle from X axis  
A  |  Annotation Color  
  
##### Symbols:

SYMBOL  |  Plotted symbol  
---|---  
SYMSIZE  |  Symbol size  
S  |  Symbol Color  
  
##### Scaled symbols:

SFIELD  |  Field to select data, in preference to the value of FIELD.  
---|---  
SCUTMM  |  Maximum size for symbol in mm.  
SCUTVAL  |  Data value for maximum symbol size.  
  
For example:

SFIELD  |  SCUTVAL  |  SCUTMM  |  Symbol Size (mm)  
---|---|---|---  
4  |  16  |  20  |  5  
8  |  16  |  20  |  10  
>=16  |  16  |  20  |  20  
  
##### Icons:

IVALUE  |  Icon IVALUE to plot  
---|---  
IXOFFSET  |  Icon offset from point in X  
IYOFFSET  |  Icon offset from point in Y  
IANGLE  |  Rotation angle from X axis  
ISCALE  |  Scaling factor  
IASPRAT  |  Aspect ratio, width / ht.  
IROTREF  |  Position of icon origin relative to the icon size box: | 3 | 4 | 5  
---|---|---  
2 | 0 | 6  
1 | 8 | 7  
  
##### General:

LAYER  |  Plot layer; an extra field LAYER will be included in the plot file.  
---|---  
|  Plot entity color  
  
The value used in the process will be selected in the following order of priority (if supplied and not storing absent data):

  * parameter value

  * default value for the field

  * field value

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. |  Input |  Yes |  Undefined  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
ICON |  Input icon file. An icon is a small number of plot file records that describe some feature or symbol. The icon file may contain a number of icons. In addition to the normal plot file records, the icon file will contain the explicit fields **IVALUE, ITEXT, IXSIZE** and **IYSIZE**. |  Input |  No |  Plot  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field to specify distance along X axis for plotting symbol(s). |  IN |  Yes |  Numeric |  Undefined  
Y |  Field to specify distance along Y axis for plotting symbol(s). |  IN |  Yes |  Numeric |  Undefined  
LAYER |  Plot layer |  IN |  No |  Any |  Undefined  
|  Colour |  IN |  No |  Numeric |  Undefined  
FIELD |  Field to be annotated, or plotted |  IN |  No |  Any |  Undefined  
NDEC |  Decimal places for annotation. |  IN |  No |  Numeric |  Undefined  
CHARSIZE |  Character size in millimetres. |  IN |  No |  Numeric |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars. |  IN |  No |  Numeric |  Undefined  
XOFFSET |  Annotation offset from point in X in mm. |  IN |  No |  Numeric |  Undefined  
YOFFSET |  Annotation offset from point in Y in mm. |  IN |  No |  Numeric |  Undefined  
ANGLE |  Annotation angle from X axis. |  IN |  No |  Numeric |  Undefined  
A |  Annotation colour for plot. |  IN |  No |  Numeric |  Undefined  
SYMBOL |  Plotted symbol. 91=o, 92=+, 93=x. |  IN |  No |  Numeric |  Undefined  
SYMSIZE |  Symbol size in millimetres. 0=none. |  IN |  No |  Numeric |  Undefined  
S |  Symbol colour for plot. |  IN |  No |  Numeric |  Undefined  
SFIELD |  Field to determine symbol size. |  IN |  No |  Numeric |  Undefined  
SCUTMM |  Maximum size for symbol in mm. |  IN |  No |  Numeric |  Undefined  
SCUTVAL |  Data value for maximum symbol size. |  IN |  No |  Numeric |  Undefined  
IVALUE |  Icon **IVALUE** to plot at X,Y. |  ICON |  No |  Any |  Undefined  
IROTREF |  Position of icon origin. 0..9 |  ICON |  No |  Numeric |  Undefined  
IANGLE |  Rotation angle from X axis. |  ICON |  No |  Numeric |  Undefined  
IXOFFSET |  Icon X offset from point in millimetres. |  ICON |  No |  Numeric |  Undefined  
IYOFFSET |  Icon Y offset from point in millimetres. |  ICON |  No |  Numeric |  Undefined  
ISCALE |  Scaling factor. |  ICON |  No |  Numeric |  Undefined  
IASPRAT |  Aspect ratio, width / ht. for icons. |  ICON |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
NDEC |  Decimal places for annotation. |  No |  Undefined |  Undefined |  Undefined  
CHARSIZE |  Character size in millimetres. |  No |  Undefined |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars. |  No |  Undefined |  Undefined |  Undefined  
XOFFSET |  Annotation offset from point in X in mm. |  No |  Undefined |  Undefined |  Undefined  
YOFFSET |  Annotation offset from point in Y in mm. |  No |  Undefined |  Undefined |  Undefined  
ANGLE |  Annotation angle from X axis. |  No |  Undefined |  -360, 360 |  Undefined  
A |  Annotation colour for plot. |  No |  Undefined |  Undefined |  Undefined  
SYMBOL |  Plotted symbol. 91=o, 92=+, 93=x. |  No |  Undefined |  Undefined |  Undefined  
SYMSIZE |  Symbol size in millimetres. 0=none |  No |  Undefined |  Undefined |  Undefined  
S |  Symbol colour for plot. |  No |  Undefined |  Undefined |  Undefined  
SCUTMM |  Maximum size for symbol in mm. |  No |  Undefined |  Undefined |  Undefined  
SCUTVAL |  Data value for maximum symbol size. |  No |  Undefined |  Undefined |  Undefined  
IVALUE |  Icon IVALUE to plot at X,Y. |  No |  Undefined |  Undefined |  Undefined  
IROTREF |  Position of icon origin. 0..9 |  No |  Undefined |  0,9 |  0,1,2,3,4,5,6,7,8,9  
IANGLE |  Rotation angle from X axis. |  No |  Undefined |  -360, 360 |  Undefined  
IXOFFSET |  Icon X offset from point in millimetres. |  No |  Undefined |  Undefined |  Undefined  
IYOFFSET |  Icon Y offset from point in millimetres. |  No |  Undefined |  Undefined |  Undefined  
ISCALE |  Scaling factor. |  No |  Undefined |  Undefined |  Undefined  
IASPRAT |  Aspect ratio, width / ht. for icons. |  No |  Undefined |  Undefined |  Undefined  
LAYER |  Plot layer |  No |  Undefined |  Undefined |  Undefined  
|  Colour |  No |  Undefined |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Examples

### Example 1

The following macro illustrates plotting symbols and annotation:
    
    
    !START EXAMPLE PLOTSI Example 1 - symbol and annotation  
  
---  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !REM Create a simple data file; 4 records  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !INPFIL &OUT(DATA)  
      
    
    Example data file  
      
    
    X N Y 0  
      
    
    Y N Y 0  
      
    
    VALUE1 N Y 0  
      
    
    CHARSIZE N Y 0  
      
    
    XOFFSET N Y 0  
      
    
    YOFFSET N Y 0  
      
    
    ANGLE N Y 0  
      
    
    A N Y 0  
      
    
    SYMBOL N Y 0  
      
    
    SYMSIZE N Y 0  
      
    
    S N Y 0  
      
    
    ]  
      
    
    OK  
      
    
    50, 50, 1, 4, -2, -2, 0, 1, 91, 20, 5  
      
    
    100, 100, 2, 8, -4, 4, 90, 2, 94, 30, 6  
      
    
    150, 50, 3, 12, 6, 6, 180, 3, 95, 40, 7  
      
    
    200, 100, 4, 16, 8, -8, 270, 4, 96, 50, 8  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !REM Define plot prototype  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !PROTOP &OUT(PROTOP)  
      
    
    1 # Define plot size explicitly in mm  
      
    
    320 # Paper size in X  
      
    
    220 # Paper size in Y  
      
    
    35 # X origin  
      
    
    35 # Y origin  
      
    
    250 # Plot size in X  
      
    
    150 # Plot size in Y  
      
    
    Y # Yes - define scaling  
      
    
    1 # X scale  
      
    
    1 # Y scale  
      
    
    0 # X minimum  
      
    
    250 # X maximum  
      
    
    0 # Y minimum  
      
    
    150 # Y maximum  
      
    
    OK # All values are ok  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !REM Create PLOTSI plot  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !PLOTSI &IN(DATA),&PROTO(PROTOP),&PLOT(PLOTSI1.P),*X(X),*Y(Y),  
      
    
    *FIELD(VALUE1),@NDEC=0,@ASPRATIO=0.9  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !REM Add a frame  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !PLOTFR &PROTO(PROTOP),&PLOT(PLOTSI1.P),@XINC=50,@YINC=50,@NDX=0,  
      
    
    @NDY=0,@IGRID=3,@=1,@APPEND=1,@CHARSIZE=5  
      
    
    X  
      
    
    Y  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !REM Add a title  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !PLOTTI &PROTO(PROTOP),&PLOT(PLOTSI1.P),@CHARSIZE=6,@=1,@APPEND=1  
      
    
    PLOTSI Example 1 - Annotation and Symbols  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !REM Display PI plot  
      
    
    !REM ------------------------------------------------------------------  
      
    
    !DISPLA &IN(PLOTSI1.P),@PAUSE=-1.0  
      
    
    !END