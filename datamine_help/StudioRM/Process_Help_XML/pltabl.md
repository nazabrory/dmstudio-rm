# PLTABL Process  
  
Note: This legacy plotting process is no longer supported or developed. It is included here for legacy macro support only. For interactive plot creation and editing functions, with template and automation support, consider the [Plots](<../COMMON/Window_PLOTS_Overview.md>) window tools.

To access this process:

  * Enter "PLTABL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PLTABL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PLTABL>).

## Process Overview

Generate a tabulated report on the plotter.

Output selected fields from a file as a plotted table with headings, and user definable field formats. The input is similar to [REPORT](<report.md>).

### Prompts

`>SYSFILE>` External file name (max 56 chars).

`>HALFLINE> `Prompts for ten half-lines of 60-column width as a heading to the report.

`>FIELD> `Name of the field to be printed.

`>FORMAT> `FORTRAN format specification for the field, including any leading or trailing blanks.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PLOT |  Output |  Yes |  Plot |  Output plot file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LINES |  Number of lines per page of output. If negative will be double spaced. |  No |  Undefined |  Undefined |  Undefined  
NOFF |  If set to 1, suppresses form feeds (0). |  No |  0 |  0,1 |  0,1  
SYSFILE |  |  Option |  Description  
---|---  
1 |  to send report to a system file rather than the printer or print file (0). File name is requested:  
No |  0 |  0,1 |  0,1