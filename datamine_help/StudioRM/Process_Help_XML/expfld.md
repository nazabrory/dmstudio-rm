# EXPFLD Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Expand File**.

  * Enter "EXPFLD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#ESTIMATE>)](<../command_help/COMMAND%20TABLE_E.md#EXPFLD>).

## Process Overview

Copy a file, while expanding the number of records so that a record is output for given increments of a start field until an end field value is reached.

A typical use is where there are properties defined over a range of sample numbers, and these are to be combined with other data entered for each sample. For example, suppose the file contains the following fields:-
    
    
    BHID    FROMNO   TONO    DENSITY

where the **DENSITY** is defined for the range of sample numbers in **FROMNO** and **TONO**. EXPFLD could be used to expand this into a new file containing the fields:-
    
    
    BHID Sample DENSITY

This file contains a record of the **DENSITY** for each sample number, and as such may be combined with other files in this format.

The records output are for values of * **START** , * **START** +@**INCRMENT** , * **START** +2*@**INCRMENT** , and so on, until the value of * **END** for the input record is reached. This means that @**INCRMENT** must never be zero, or an infinite number of records lie between the values.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file containing numeric explicit fields **START** and **END** defining the range. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file containing extra records between the given ranges, the actual value being held in field NEWFIELD.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
START |  Name of field giving the start of the range. |  IN |  Yes |  Numeric |  Undefined  
END |  Name of field giving the end of the range. |  IN |  Yes |  Numeric |  Undefined  
NEWFIELD |  Name of field in output file containing the value for the record within the range. |  OUT |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
INCRMENT |  Increment to be applied to **START** within range. | Yes | Undefined | Undefined | Undefined  
  
## Example
    
    
    !EXPFLD &IN(COMDEN),&OUT(SAMDEN),*START(FROMNO),  
  
---  
      
    
    *END(TONO),*NEWFIELD(SAMPLE),@INCRMENT=1  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> WARNING - RECORD nnnnnn HAS START nnnnnn.nn GT END nnnnnn.nn <<<  
>>> ERR 131 <<< (recordno) IN EXPFLD |  Warning; illegal record. The record is output unchanged.  
>>> FIELD DOES NOT EXIST <<<  
>>> ERR 131 <<< ( fileno) IN EXPFLD |  Either the *START or the *END field does not exist in the input file. Fatal; the process is exited.  
>>> FIELD NOT NUMERIC <<<  
>>> ERR 132 <<< ( fileno) IN EXPFLD |  Either the *START or the *END field was alphanumeric. Fatal; the process is exited.