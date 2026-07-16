# PICTED Process  
  
To access this process:

  * Enter "PICTED" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PICTED** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PICTED>).

## Process Overview

Interactive display and manipulation of Datamine plot files to produce composite plots.

PICTED allows different plot files to be displayed concurrently, and permits rescaling and positioning of individual plots. The composite picture created in this way may be saved to an output *.dm format plot file.

### Process Options

On running the process, the following options are displayed:

  1. SET PLOT DIMENSIONS IN MM

  2. DISPLAY A FILE (AND ADD TO ACTIVE LIST)

  3. SET/CHANGE OFFSETS/SCALES

  4. REMOVE FILE FROM ACTIVE LIST

  5. SAVE DISPLAY INTO NEW PLOT FILE

  6. REFRESH DISPLAY

  7. HARDCOPY CURRENT DISPLAY

  8. EXIT

Each of the above options generates subsidiary interactions:

  1. For SET PLOT DIMENSIONS IN MM:

    
    
    CURRENT PLOT DIMENSIONS ARE : X = XXX.XX, Y = YYY.YY
    
    
    >>> SET NOMINAL PLOT SIZE IN MM>
    
    
    X > Supply X plot dimension.
    
    
    Y > Supply Y plot dimension.
    
    
    FILE > Supply plot file name.
    
    
    >>> EXPAND (>1) OR REDUCE (<1) FACTOR >
    
    
    X > Supply X scaling factor.
    
    
    Y > Supply Y scaling factor.
    
    
    >>> X AND Y OFFSETS IN MM --
    
    
    X > Supply X offset from picture origin for the local origin of
    
    
    the current plot file.
    
    
    Y > Supply Y offset from picture origin for the local origin of
    
    
    the current plot file.
    
    
    SET OR CHANGE SCALES AND OFFSETS
    
    
    >>> N FILES ACTIVE ---
    
    
    >>>================================================
    
    
    >>> FILENAME FILE LIMITS SCALED BY OFFSETS
    
    
    >>> X Y X Y X Y
    
    
    >>>================================================
    
    
    >>> xxxxxxxx nn.n nn.n nn.n nn.n nn.n nn.n

  2. For DISPLAY A FILE (AND ADD TO ACTIVE LIST):

The Project Browser is displayed in order to select the required plot file.

  3. For SET/CHANGE OFFSETS/SCALES:

Scales and offsets are prompted for, as for option 2.

  4. For REMOVE FILE FROM ACTIVE LIST:

The Project Browser dialog is displayed in order to select the required plot file.
    
    
    REMOVE FILE FROM ACTIVE LIST
    
    
    >>> CURRENTLY ACTIVE FILES ARE --
    
    
    >>> xxxxxxxx
    
    
    >>> yyyyyyyy

  5. For SAVE DISPLAY INTO NEW PLOT FILE:

The Project Browser is displayed in order to define the required output plot file location and name.

  6. For REFRESH DISPLAY:

The Graphics widow display is cleared and regenerated from the plot files in the active list.

  7. For HARDCOPY CURRENT DISPLAY:

This function is not available.

  8. For EXIT

The **PICTED** process is terminated.