# RANK Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics Processes >> Generate Rank Orders**.

  * Enter "RANK" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **RANK** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#RANK>).

## Process Overview

Ranks values of a given numeric or alphanumeric field in a file.

Output fields created are as follows:

  * **RANK** Rank order (integer) of the specified field.

  * **CUMPROP** Proportion value, computed as `(RANK-0.5)/NDATA` where **NDATA** is the number of data records used.

  * **PHI** The standard normal deviate, computed as the PHI (or Z) transform of the **CUMPROP** value. PHI is centred on zero and has values in the range -3.5 to +3.5 for small data sets.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Numeric or up to 4-character alpha field to be ranked. |  IN |  Yes |  Any |  Undefined  
RANK |  New field to be created in output file, to contain rank order values. |  OUT |  Yes |  Undefined |  Undefined  
CUMPROP |  New field to be created in output file, to contain cumulative frequency values of field **RANK** [values of **CUMPROP** lie between 0 and 1]. |  OUT |  Yes |  Numeric |  Undefined  
PHI |  New field to be created in output file, to contain PHI [inverse normal distribution] transform of field **CUMPROP** [values of PHI lie between -3.5 and +3.5]. |  OUT |  Yes |  Numeric |  Undefined  
  
## Example
    
    
    !RANK  &IN(SEDREG),&OUT(SRANK),*VALUE(AU),*RANK(ORDER),*CUMPROP(AUCF),*PHI(AUPHI)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 120 <<< ( fileno) IN ffffffff |  Input file ffffffff read error. Fatal; the process is exited.  
>>> ERR 121 <<< ( fileno) IN RANK |  File read error. Fatal; the process is exited.  
>>> ERR 122 <<< ( fileno) IN RANK |  No numeric fields in file, or fields specified were not numeric. Fatal; the process is exited.