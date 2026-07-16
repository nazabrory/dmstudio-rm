# PEROPN Process

To access this process:

  * Enter "PEROPN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PEROPN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PEROPN>).

Open or close all perimeters in the input file.

Note: A perimeter is closed if the last point is equal to the first point. Otherwise, the perimeter is considered to be open.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PERIMIN |  Input perimeter file. File must contain the fields **XP, YP, ZP, PVALUE** and **PTN**. |  Input |  Yes |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOUT |  Output |  Yes |  String |  Output perimeter file. All fields are copied from the input file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CLOSE |  |  Option |  Description  
---|---  
(0) |  will remove last point of a perimeter if perimeter is closed.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !PEROPN &PERIMIN(PERS1),&PERIMOUT(PERS2),@CLOSE=1  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
MISSING PERIMETER FIELDS |  If the &**PERIMIN** file does not contain all 5 fields XP, YP, ZP, PVALUE and PTN the message `' will be displayed and the process will exit.