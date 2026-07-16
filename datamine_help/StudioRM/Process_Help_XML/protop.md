# PROTOP Process

Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PROTOP" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PROTOP** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PROTOP>)

## Process Overview

To create a prototype plot file with defined plot and data area shape/size, and optionally data ranges and scaling factors.

**PROTOP** is the first process to be used before plotting starts. It defines the prototype that will subsequently be used by plot processes. The main parts defined are the plot region (the total true size of the plot) and, within this, the data area, into which most plot processes will place plotted data. Sizes are defined in millimeters, and may be measured from existing plots, so that any in-house standard plot shape and size may be duplicated.

Within the data area, it is also possible to specify data ranges and/or scales if required. Thus a plot prototype could be set up for, for example, a series of bench plans. However, ranges and scales may be defined later, if required, during the plot process itself.

#### Scaling

Scales are defined separately in the X and Y directions, as data units per plotted millimeter. Thus, if the data units are meters, then an X SCALE (or Y SCALE) of 1 will give one meter per plotted millimeter, or a scale of 1:1000. An X SCALE of 2 will give 1:2000, and so on. If the data units are feet, then an X SCALE of 3.28084 will give 3.28084 feet per plotted millimeter (i.e. a scale of 1:1000).

#### Data Ranges and Scales

The user may define three values for X and Y defining the scale (X SCALE), and minimum and maximum data values (X MIN and X MAX). Any two out of these three must be defined, and the remaining value is then calculated. However, if all three are defined, then they must be consistent; the data range must map into the defined data area at the given scale. The process checks for this. Note that if the minimum and maximum are defined, then these are mapped into the data area, and can give rise to different scales in X and Y; to ensure the same scale in X and Y, it is better to give a data minimum or maximum and the required scale.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Plot Prototype |  Plot prototype file to be created.