# VALIDA Process  
  
To access this process:

  * Enter "VALIDA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **VALIDA** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_V.md#VALIDA>).

## Process Overview

Validate fields against each other in a Datamine file.

Commands are entered interactively to specify the nature of the required tests.

The main test commands are:

TEST FFFFFFFF.op.GGGGGGGG  |  Checks the relationship between field names **FFFFFFFF** and **GGGGGGGG**.  
---|---  
UNLS FFFFFFFF.op.GGGGGGGG  |  If all **UNLS** criteria are satisfied, then all **TEST** criteria are ignored for the current record.  
  
If any test fails, the entire record is failed, and will not be written to the output file unless the **PASS** command has been given.

It is important that the described format for the **TEST** and **UNLS** commands is kept to, in particular that the **FFFFFFFF** and **GGGGGGGG** field names are entered as 8 characters, blank padded to the right if required, and the operators are 4 characters long (for example, .EQ.). There is a maximum of 20 commands permitted.

The validation commands are prompted for:
    
    
    > TEST FFFFFFFF.op.GGGGGGGG

Test field **FFFFFFFF** (entered as 8 characters, blank padded if necessary) against field **GGGGGGGG**. The permissible operators .op. are .GE.,.EQ.,.LE.,.NE. If **FFFFFFFF** i s the same as **GGGGGGGG** then the test is on the same field between the previous and the current record; otherwise the test is on different fields in the same record. There may be a number of different **TEST** criteria specified. The record will only pass if it passes all TEST criteria.
    
    
    > UNLS FFFFFFFF.op.GGGGGGGG

If all the given **UNLS** relationships between field **FFFFFFFF** and field **GGGGGGGG** are true, then the **TEST** criteria will not be carried out, and the record will pass. The format for and meaning of the components of the **UNLS** command are exactly the same as for the **TEST** command.
    
    
    >MESS Display message on failed tests.
    
    
    >PASS Write failed records to &OUT.
    
    
    >FAIL Do not write failed records (default).
    
    
    >LAST End of commands.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be validated. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  File containing validated records.  
  
## Example
    
    
    !VALIDA   
  
---  
      
    
     &IN(ASSAYS),&OUT(VASSAYS)  
      
    
    TEST   
      
    
    FROM .GE.FROM  
      
    
    TEST   
      
    
    TO .GE.FROM  
      
    
    MESS  
      
    
    LAST  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> VALIDATION COMMAND "AAAA" NOT RECOGNISED <<< >>> FIELD "FFFFFFFF" NOT RECOGNISED <<< >>> OPERATION ".op." UNKNOWN <<< |  Each command is decoded and validated as it is read in. If any errors are found, the command is ignored with one of these error messages.