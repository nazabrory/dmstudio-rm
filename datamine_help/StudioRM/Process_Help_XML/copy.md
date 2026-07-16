# COPY Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Copy Files**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **COPY** and click **Run**.
  * Enter "COPY" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#COPY>).

## Process Overview

Copy a file.

No check is made for the existence of the specified output file, which therefore can be overwritten.

If retrieval criteria are in force, the output file only contains those records which match the criteria. If an index file is copied, the output file contains the joined set of files accessed by the index; it is not itself an index.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file.  
  
## Example

The following example copies a file using a retrieval criteria of 'COPPER>0.5' i.e. all records which have a value of greater than and equal to 0.5 in the field COPPER are copied:
    
    
    !COPY &IN(FILE1), &OUT(FILE2), COPPER>0.5  
  
---