# TERPLT Process  
  
To access this process:

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, select **TERPLT** and click **Run**.
  * Enter "TERPLT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TERPLT>).

## Process Overview

Generate a ternary (triangular) diagram plot , with optional output of a table of the data values.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  First input field of ternary plot (top apex). |  IN |  Yes |  Numeric |  Undefined  
F2 |  Second input field of ternary plot (bottom left). |  IN |  Yes |  Numeric |  Undefined  
F3 |  Third input field of ternary plot (bottom right). |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PLOT |  |  Option |  Description  
---|---  
1 |  output of ternary plot to printer or print file (0).  
No |  0 |  0,1 |  0,1  
PRINT |  |  Option |  Description  
---|---  
1 |  output of data values to printer or print file (0).  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !TERPLT    &IN(SEDREG),*F1(PB),*F2(ZN),*F3(CU),@PLOT=1,@PRINT=1  
  
---