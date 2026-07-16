# INPUTC Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Text Utilities >> Input Text Data**.
  * Enter "INPFIL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **INPFIL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#INPUTC>).

## Process Overview

Creates a text file of standard form, with 80 characters per record. The Data Definition is set up automatically to contain a single alphanumeric field of length 20 words (80 characters) with the fieldname T.

The data may optionally be read from a system file external to the database. This is useful to set up character files e.g. macros \- which have been created outside a database.

Blank lines within the external file are loaded (as far as the record count is concerned) but are ignored in all processing, as blank is absent data within a text field. 

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  File to be created.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  >=1 to display each record (0). |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !INPUTC &OUT(MACRO1)SYSFILE><return>  
  
---  
      
    
    TEXT >!start mymac<return>  
      
    
    TEXT >!list &in($1)<return>  
      
    
    TEXT >!end<return>  
      
    
    TEXT >!!<return>  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited.   
  
Related topics and activities

  * INPUTC Process

  * [INTEXT Process](<intext.md>)

  * [INPDDF Process](<inpddf.md>)

  * [INPFIL Process](<inpfil.md>)

  * [INPFML Process](<inpfml.md>)

  * [INPUTD Process](<inputd.md>)

  * [INPUTW Process](<inputw.md>)

  * [OUTPUT Process](<output.md>)