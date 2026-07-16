# RECCOP Process

To access this command:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **RECCOP** and click **Run**.
  * Enter "RECCOP" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#RECCOP>).

## Process Overview

Copy a group of records from one file to another.

The records passing the retrieval criteria (if any) are numbered and those satisfying the record number range **RECMIN** to **RECMAX** are copied. 

**Note** : The test on **RECMIN** and **RECMAX** is applied in the same manner as retrieval criteria limits.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
RECMIN |  Mininim record number (1). |  No |  1 |  Undefined |  Undefined  
RECMAX |  Maximum record number (+). |  No |  + |  Undefined |  Undefined