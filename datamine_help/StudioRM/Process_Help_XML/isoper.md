# ISOPER Process  
  
To access this process:

  * Enter "ISOPER" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **ISOPER** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#ISOPER>).

## Process Overview

Create an isometric view of perimeters and strings.

Note: Scaling is fully automatic in this process.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Prototype plot file. Only the plot area data is used. Any scaling and data ranges (XMIN, XMAX etc ) are ignored. |  Input |  Yes |  Plot Prototype  
PERIMIN |  Perimeter input file |  Input |  Yes |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PXMIN |  X value of left-hand side of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PXMAX |  X value of right-hand side of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PYMIN |  Y value of front of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PYMAX |  Y value of back of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PZMIN |  Z value of bottom of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
PZMAX |  Z value of top of region to be plotted. |  Yes |  Undefined |  Undefined |  Undefined  
ROTATE |  The rotation angle in degrees horizontally of the viewpoint, clockwise from the data Y axis (45). |  No |  45 |  0,360 |  Undefined  
ELEVATE |  The rotation angle in degrees vertically of the viewpoint, upwards from data X-Y plane (45). |  No |  45 |  -90,90 |  Undefined  
CHARSIZE |  Character size in millimetres (4). |  No |  4 |  Undefined |  Undefined  
ASPRATIO |  Aspect ratio, width / ht. for chars (0.9). |  No |  0.9 |  Undefined |  Undefined  
|  Colour [as 'pen' number] for plot (1). |  No |  1 |  Undefined |  Undefined  
  
## Example

The following example demonstrates the use of **ISOPER** to produce isometric plots of pit design and section perimeters.

The process [SURTRI](<surtri.md>) is used to build a Digital Terrain Model of the original design perimeters and [WIREPE](<wirepe.md>) is then used to create the pit sections.  
  
Plot the design perimeters:
    
    
    !ISOPER  &PROTO(PROTO),   
  
---  
      
    
             &PERIMIN(PITDESN), &PLOT(PLOT1),  
      
    
    @PXMIN=14000, @PXMAX=15000,   
      
    
             @PYMIN=60000, @PYMAX=61000,   
      
    
    @PZMIN=-50, @PZMAX=150, @ROTATE=25,   
      
    
             @ELEVATE=45  
      
    
    Build a DTM of the design  perimeters:  
      
    
    !SURTRI  &WIREPT(PT),   
      
    
             &WIRETR(TR), &PERIMIN(PITDESN)  
      
    
    Generate pit section perimeters:  
      
    
    !WIREPE   &WIREPT(PT), &WIRETR(TR), &PERIMOUT(PITSECN),   
      
    
             @YINCR=20  
      
    
    2  
      
    
    14000  
      
    
    60000  
      
    
    15000  
      
    
    60000  
      
    
    -50  
      
    
    150  
      
    
    Y  
      
    
    Plot the pit section perimeters:  
      
    
    !ISOPER  &PROTO(PROTO),   
      
    
             &PERIMIN(PITSECN), &PLOT(PLOT2),   
      
    
    @PXMIN=14000,@PXMAX=15000,   
      
    
             @PYMIN=6000, @PYMAX=61000,   
      
    
    @PZMIN= -50,@PZMAX=150,@ROTATE=25,   
      
    
             @ELEVATE=45.  
      
    
       
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> MISSING FILES <<< |  One or more of the input files do not exist. Fatal; the process is exited.  
>>> ATTEMPT TO OPEN PERIMETER FILE <<< |  The input perimeter file can not be read by the process (e.g. it does not exist). Fatal; the process is exited.  
>>> ATTEMPT TO OPEN PROTO FILE <<< |  The plot prototype file can not be read by the process (e.g. it does not exist). Fatal; the process is exited.  
>>> ATTEMPT TO CALL PLINIT <<< |  An error occurred when initiating the graphics environment (e.g. it has failed to open the output plot file or it has failed to open the screen device). Fatal; the process is exited.  
>>> ATTEMPT TO COPY DATA DEFINITION <<< |  An error occurred when copying the data definition from the input prototype file to the output plot file (e.g. disk full). Fatal; the process is exited.  
>>> MISSING PERIMETER FIELDS <<< |  One or more of the essential perimeter fields are missing (e.g. the file specified is not a perimeter file). Fatal; the process is exited.  
>>> MISSING ISOMETRIC PARAMETERS <<< |  One or more of the compulsory isometric parameters are missing (e.g. ISOPER is running within a macro). Fatal; the process is exited.  
>>> INVALID PLOT COORDINATES <<< |  One or more of the compulsory plot coordinates are missing, incorrect or inconsistent (e.g. @XMIN > @XMAX). Fatal; the process is exited.  
>>> NO MORE ROOM FOR PLOT FILE FIELDS <<< |  The maximum number of 64 fields in a file has been exceeded. Fatal; the process is exited.  
>>> ATTEMPT TO WRITE PLOT DATA DEFINITION <<< |  An error occurred when writing the data definition of the output plot file (e.g. disk full). Fatal; the process is exited.  
>>> ATTEMPT TO READ PERIMETER FILE <<< |  An error occurred when reading in the perimeter file (e.g. it has corrupted or invalid data). Fatal; the process is exited.