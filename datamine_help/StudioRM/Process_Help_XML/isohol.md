# ISOHOL Process  
  
To access this process:

  * Enter "ISOHOL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **ISOHOL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#ISOHOL>).

## Process Overview

Create a plot file showing an isometric view of drillholes, from a user-defined viewpoint, described by rotation and elevation angles.

**ISOHOL** clarifies the relationship between drillholes and their ore intersections. Colour may be used for individual samples, if there is a field * **VALUE** in the input file containing the colour number for each sample. Each drillhole may be displayed with a bar chart, annotation or curve representing the values of fields in the file. Two displays per drillhole are possible; these may be two bar charts, two sets of annotation, two sets of curves, or one of each.

The input drillhole file is in standard sample format, as output for example by the [DESURV](<desurv.md>) process. The file must be sorted on **BHID** and **FROM**.

Note: Scaling is fully automatic in this process.

Process Prompts

This is an interactive process and prompts appear on the command line once it is launched:
    
    
    > HOLE ID LABELING; CHARACTER SIZE IN MM 
    > Enter required height; default is 4mm
    
    
    > ANGLE IN DEGREES CLOCKWISE FROM PROJECTED 
     LINE OF FIRST SAMPLE IN EACH HOLE >
    
    
    Supply angle; 180 is vertically upwards   
    
    
    > HOW MANY FIELDS TO PLOT FOR EACH SAMPLE 
     (0, 1 or 2)?  >  
    
    
    Enter 0, 1 or 2.  
    
    
    > SCALING FOR R.BAR OR ANNOTATION FIELD 
    > Enter field name
    
    
    > ANNOTATE (A) OR BARPLOT (B) OR NONE (N)?> 
       
    
    
    Enter A, B or N (the default is A)
    
    
    If A is entered and the field is numeric 
     then:   
    
    
    > HOW MANY DECIMAL PLACES? >   
    
    
    Enter 0 - 4 (the default is 0)
    
    
    If B is entered then:   
    
    
    > MAX BAR LENGTH IN MM? 
    
    
    > Enter maximum bar length
    
    
    > DATA VALUE CORRESPONDING TO THIS LENGTH? 
    > Enter maximum data value.  Largest values 
     will be truncated and smaller ones scaled.   
    
    
     If 2 fields are to be plotted, the above 
     prompts are repeated for the second field.   
    
    
     If either one or two annotation responses 
     (A) given then:   
    
    
    > CHARACTER SIZE IN MM? >   
    
    
    Enter required character size (default is 
     2 mm).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input drillhole data file. Must contain fields BHID,X,Y,Z,LENGTH,A0,B0, + VALUE field. |  Input |  Yes |  Drillhole  
PROTO |  Plot prototype file. Must contain the fields X, Y, S1, S2, CODE (numeric, explicit) and XMIN, XMAX, YMIN, YMAX, XSCALE, YSCALE (numeric, implicit). Without a plot prototype, PXMIN ,.... PZMAX define the region to be mapped to the screen. |  Input |  No |  Plot Prototype  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Field containing colour codes. |  IN |  No |  Numeric |  Undefined  
BHID |  Drillhole identifier field (if not BHID). |  IN |  No |  Any |  BHID  
X |  Name of X field (if not X). |  IN |  No |  Numeric |  X  
Y |  Name of Y field (if not Y). |  IN |  No |  Numeric |  Y  
Z |  Name of Z field (if not Z). |  IN |  No |  Numeric |  Z  
LENGTH |  Name of LENGTH field (if not LENGTH). |  IN |  No |  Numeric |  LENGTH  
A0 |  Name of A0 field (if not A0). |  IN |  No |  Numeric |  A0  
B0 |  Name of B0 field (if not B0). |  IN |  No |  Numeric |  B0  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PXMIN |  X value of left-hand side of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PXMAX |  X value of right-hand side of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PYMIN |  Y value of front of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PYMAX |  Y value of back of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PZMIN |  Z value of bottom of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PZMAX |  Z value of top of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
VERTEXAG |  Vertical exaggeration required. |  Yes |  Undefined |  Undefined |  Undefined  
ROTATE |  The rotation angle in degrees horizontally of the viewpoint, clockwise from the model Y axis (45). |  Yes |  45 |  0,360 |  Undefined  
ELEVATE |  The rotation angle in degrees vertically of the viewpoint, upwards from model X-Y plane (45). |  Yes |  45 |  -90,90 |  Undefined  
CHARSIZE |  Character size in millimetres (3). |  No |  3 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
APPEND |  Plot append flag. If set to 1 then the new plot will be appended to the PLOT file, if it exists and is a valid plot file (0). |  No |  0 |  0,1 |  0,1  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 121 <<< ( n) IN ISOHOL |  One or more of the essential fields BHID, X, Y, Z, LENGTH, A0 or B0 is absent or of wrong type. Fatal; the process is exited.  
>>> CANNOT APPEND TO NON-EXISTENT OUTPUT FILE. >>> A NEW OUTPUT FILE WILL BE CREATED. |  The @APPEND parameter has been set to 1, but the specified plot file does not exist. A new file will be created to contain the new plot being produced.  
>>> ERROR - CANNOT APPEND TO PLOT FILE AS IT DOES NOT CONTAIN ALL THE REQUIRED FIELDS. >>> THE PLOT FILE WILL BE OVERWRITTEN. |  The @APPEND parameter has been set to 1, the specified plot file exists but is invalid. The existing plot file will be overwritten by the new plot being produced.