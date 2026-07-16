# PLTLAY Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLTLAY" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLTLAY** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLTLAY>).

## Process Overview

Interactive graphics plot editing and layout process.

There are a number of line, box, circle and text generation sub-commands available in **PLTLAY** in addition to icon storage and retrieval of selected plotted entities. 

Additional data overlay plotting functions are available in the **PLTLAY** process. However, in addition to the normal plot file fields the plot file must also contain the implicit fields **XCENTRE, YCENTRE, ZCENTRE, SAZI** and **SDIP**. The default values of these fields, together with the default values of **XMIN, XMAX, YMIN** and **YMAX** fields completely define the position, orientation and size of the viewing plane that will be used in the **PLTLAY** process. 

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Plot prototype. |  Input |  No |  Plot Prototype  
ICON |  Icon file. An icon is a small number of plot file records that describe some feature that is commonly required on mine plans, e.g. mine shafts. This input/output icon file may contain a number of user-defined icons. In addition to the normal plot file fields, the icon file will contain the explicit fields **IVALUE, ITEXT, IXSIZE** and **IYSIZE**. |  Overwritten |  No |  Plot  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file. This file will contain all of the plot data that has been generated during the current operation of **PLTLAY**.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ASIZE |  Type of A size paper, for initial plot size if no prototype file supplied. (0) |  No |  0 |  Undefined |  Undefined  
XSCALE |  Initial X plot scale factor if no prototype file supplied.  For example, enter 1000 for a scale of 1:1000. Note that user data units of metres are assumed; if metres are not the unit, then the scale must be multiplied by factor f, where f=no. of metres in 1 user data unit [e.g. 0.3048 for feet]. |  No |  Undefined |  Undefined |  Undefined  
YSCALE |  Initial Y plot scale factor if no prototype file supplied. |  No |  Undefined |  Undefined |  Undefined  
UNIT |  This parameter indicates the type of data that will be brought into the process. The default is metric (0) and a unit value of 1 indicates user units of imperial feet. |  No |  0 |  0,1 |  0,1  
APPEND |  If an input plot prototype file has been supplied, any plot records in this file may automatically copied to the final output plot file by setting this parameter to 1.(1) |  No |  1 |  0,1 |  0,1