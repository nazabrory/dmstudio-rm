# PLOTVA Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLOTVA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLOTVA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLOTVA>).

## Process Overview

Generates a multi-value scatter plot file, where each data point is annotated by up to 10 fields centred on this point.

Individual character size, offsets, angle and decimal places must be specified interactively for each field.

The input file should contain just one entry for each location. If it contains more than one, then there will be multiple plots at that location.

### Entering Field Details

You need to enter the following information for each field to be plotted:

  * Field Name,
  * Character Size,
  * X Offset,
  * Y Offset,
  * Angle,
  * Number of Decimal Places.

Up to 10 fields can be specified terminating with a blank line or a comma in column 1. The data for each field must be specified on a single line separating data items with commas. When data entry is terminated the user is prompted to enter 0 to start plotting, 1 to add more fields or 2 to start data entry again.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. This must contain X and Y fields and at least one value field. |  Input |  Yes |  Undefined  
PROTO |  Plot prototype file. Must contain the fields **X, Y, S1, S2** and **CODE** (numeric, explicit) and **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** (numeric, implicit). If these last 6 values set in **PROTO** , then corresponding parameters need not be set. |  Input |  Yes |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field to be plotted along X axis. |  IN |  Yes |  Numeric |  Undefined  
Y |  Field to be plotted along Y axis. |  IN |  Yes |  Numeric |  Undefined  
SYMCODE |  The **SYMCODE** value will control the symbol used on each point. If used, it will override the **SYMBOL** parameter. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ANGLE |  Angle for symbol plotting in degrees from the X axis.(0) |  No |  0 |  Undefined |  Undefined  
SYMBOL |  Plotted symbol at each point. Default (92). Point symbol number 

  * 91 : Circle (o) 
  * 92 : Cross (+) 
  * 93 : Cross (x) 
  * 94 : Triangle 
  * 95 : Box 
  * 96 : Diamond 
  * 97 : Star 
  * 98 : Pie Segment. 

Can also be from the standard symbol set (codes 201 - 267) ( ) |  No |  92 |  91,267 |  Undefined  
SYMSIZE |  Symbol size in millimetres (3). Set to 0 for no symbol. |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the **PLOT** file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
XMIN |  Minimum value of X for plot. None of **XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE** need be set if this information is already in the prototype. |  No |  Undefined |  Undefined |  Undefined  
XMAX |  Maximum value of X for plot. |  No |  Undefined |  Undefined |  Undefined  
YMIN |  Minimum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
YMAX |  Maximum value of Y for plot. |  No |  Undefined |  Undefined |  Undefined  
XSCALE |  X scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Y scale in user data units per millimetre. |  No |  Undefined |  Undefined |  Undefined  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED |  The @**APPEND** parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES >>> NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @**APPEND** parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.  
>>> FATAL ERROR, BAD SCALE/RANGE COMBINATION(S) <<< >>> XMIN, XMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> YMIN, YMAX = nnnnnnnnnn.nn nnnnnnnnn.nn >>> XSCALE, YSCALE = nnnnnnnnnn.nn nnnnnnnnn.nn |  Either insufficient scale information had been entered (at least two of **XMIN, XMAX, XSCALE** or Y equivalents must be entered either from the prototype of from parameters) or the combination given of **XMIN, XMAX** , and **XSCALE** (or their Y equivalents) was impossible. Often caused by entering a null plot prototype and no parameters. Fatal; the process is exited.  
>>> INSUFFICIENT DATA. RE_ENTER THE LINE. <<< |  Insufficient annotation information has been entered. The user is prompted to re-enter the line of data.  
>>> ERROR IN FIELD NAME. RE-ENTER THE LINE. <<< |  An error has been detected in the field name entry. The user is prompted to re-enter the line of data.  
>>> FIELD ffffffff DOES NOT EXIST. RE-ENTER THE LINE. <<< |  The annotation field entered does not exist in the input data file. The user is prompted to re-enter the line of data.  
>>> ERROR - REPLY MUST BE 0, 1, 2 or ! |  The response to the question 'Is data entry correct?' must be 0, 1, 2 or !.