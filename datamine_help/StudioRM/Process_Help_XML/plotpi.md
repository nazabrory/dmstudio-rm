# PLOTPI Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTPI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTPI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTPI>).

## Process Overview

Plot multiple numeric data variables as coloured sectors with the radii proportional to the respective variable value.

For each variable, you are prompted for the variable name, maximum value to be plotted, the radius (in mm) corresponding to that maximum value and the colour for the sector outline. The sectors are plotted in the order supplied by the user, in a clockwise direction from the vertical.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. |  Input |  Yes |  Undefined  
PROTO |  Plot prototype file. Must contain fields **X,Y,S1,S2,CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field to be plotted along X axis. |  IN |  Yes |  Numeric |  Undefined  
Y |  Field to be plotted along Y axis. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
EXPLODE |  Distance in mm used to separate the pie slices (0). | No | 0 | Undefined | Undefined  
APPEND |  Plot append flag.(0) If 1 then the new plot will be appended to the **PLOT** file if exists and is a valid plot file. | No | 0 | 0,1 | 0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. | No | Undefined | Undefined | Undefined  
XMAX |  Maximum value of X for plot. | No | Undefined | Undefined | Undefined  
YMIN |  Minimum value of Y for plot. | No | Undefined | Undefined | Undefined  
YMAX |  Maximum value of Y for plot. | No | Undefined | Undefined | Undefined  
XSCALE |  X scale in user data units per millimetre. | No | Undefined | Undefined | Undefined  
YSCALE |  Y scale in user data units per millimetre. | No | Undefined | Undefined | Undefined  
  
* * *

## Example

The following macro illustrates the use of PLOTPI:
    
    
    !START EXAMPLE Example of PLOTPI  
  
---  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !REM Create a simple data file; 3 records, 5 fields  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !INPFIL &OUT(data),@PRINT=0.0  
      
    
    Example data file  
      
    
    X N Y 0  
      
    
    Y N Y 0  
      
    
    AU N Y 0  
      
    
    AG N Y 0  
      
    
    CU N Y 0  
      
    
    ]  
      
    
    OK  
      
    
    50, 50,4.5,50,0.5  
      
    
    100,100,2.5,90,0.8  
      
    
    150, 75,7.5,30,1.0  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !REM Define plot prototype  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !PROTOP &OUT(PROTOP)  
      
    
    10  
      
    
    35  
      
    
    35  
      
    
    230  
      
    
    140  
      
    
    Y  
      
    
    1  
      
    
    1  
      
    
    0  
      
    
    230  
      
    
    0  
      
    
    140  
      
    
    OK  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !REM Create PI plot  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !PLOTPI&IN(DATA),&PROTO(PROTOP),&PLOT(PLOT1),*X(X),*Y(Y),  
      
    
    @EXPLODE=1.0,@APPEND=0.0  
      
    
    AU, 10,15,2  
      
    
    AG,100,15,4  
      
    
    CU, 1,15,6  
      
    
       
      
    
    0  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !REM Add a frame  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !PLOTFR &PROTO(PROTOP),&PLOT(PLOT1),@XINC=50,@YINC=50,@NDX=0,@NDY=0,  
      
    
    @IGRID=3,@=1,@APPEND=1,@CHARSIZE=5  
      
    
    Easting  
      
    
    Northing  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !REM Add a title  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !PLOTTI &PROTO(PROTOP),&PLOT(PLOT1),@CHARSIZE=7,@=1,@APPEND=1   
  
To display the plot:
    
    
    !REM ---------------------------------------------------------------  
  
---  
      
    
    !REM Display PI plot  
      
    
    !REM ---------------------------------------------------------------  
      
    
    !DISPLA &IN(PLOT1),@PAUSE=-1.0  
      
    
    !END  
      
    
    The interactive prompting is as follows:
    
    
    INTERACTIVE ENTRY OF PLOTTING DATA  
    ==================================  
    Please enter the following information :  
    Field Name , Maximum Value , Radius , Outline Colour  
    Separate data items with a comma, one field per line  
    Terminate data entry with a blank line or with a comma in column 1  
    You may enter up to a maximum of 10 fields  
      
    AU, 10,15,2  
    AG,100,15,4  
    CU, 1,15,6  
    DATA SUMMARY  
    ------------  
    Field Name MaxValue Radius Outline  
    1 AU 10.000 20.0 2  
    2 AG 100.000 20.0 4  
    3 CU 1.000 20.0 6  
      
    Is data entry correct ?  
    0 - to start plotting  
    1 - to add more fields  
    2 - to start again  
    0  
      
    >>> 18 RECORDS IN FILE PLOT1 <<<