# FILCOM Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Make Fields Implicit**.
  * Enter "FILCOM" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FILCOM** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FILCOM>).

## Process Overview

Copies any file within the database from the input file to the output file, but compressing the file by turning all those fields with a constant value throughout the file into implicit fields.

This is of particular use for simple text files, such as those established by the [INPUTC](<inputc.md>) process - where the alphanumeric field may have been defined in the Data Definition as 80 characters long, but the longest record is only 20 characters. In such alphanumeric fields, compression will be in multiples of 4 characters.

**Note** : Retrieval criteria are ignored by this process.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file.  
  
## Example
    
    
    !FILCOM    &IN(FILE1),&OUT(COMFILE1)  
  
---  
  
Related topics and activities

  * [INPUTC Process](<inputc.md>)

  * [FILEXP Process](<filexp.md>)