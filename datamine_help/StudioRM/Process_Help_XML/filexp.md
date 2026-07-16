# FILEXP Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Make Fields Explicit**.
  * Enter "FILCOM" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FILCOM** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FILEXP>).

## Process Overview

Copies any file within the database from the input file to the output file, expanding the file by turning all implicit fields into explicit fields.

The field value in every record will be the constant value of the old implicit field.

This process is used when it is necessary to give different values to a field in different records after the field was initially defined as implicit. In particular, files cannot be joined on implicit fields, and so FILEXP is used to turn all fields to explicit before a join takes place.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file.  
  
## Example
    
    
    !FILEXP    &IN(COMFILE),&OUT(FILE)  
  
---  
  
Related topics and activities

  * [FILCOM Process](<filcom.md>)