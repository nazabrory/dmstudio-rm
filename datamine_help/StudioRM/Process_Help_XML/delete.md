# DELETE Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Delete**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DELETE** and click **Run**.
  * Enter "DELETE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DELETE>).

## Process Overview

Deletes the physical file associated with the symbolic &IN name from disk.

**Warning** : this process deletes physical Datamine files and cannot be undone. Be careful if running this command interactively, and particularly so if via a macro as part of batch process.

If the input file is a catalogue file then all files within the catalogue can be deleted, depending on the value of the optional parameter @**CONFIRM**. If the input is a catalogue file and @**CONFIRM** =0, the user is warned that operation is on catalogue file input and must confirm that deletion of all files in the catalogue is required, before this takes place. If the input is a catalogue file and @CONFIRM= 1, the user is again warned that operation is on catalogue file input, but in this case must confirm deletion of each file in the catalogue individually, before this takes place.

A catalogue file itself may be deleted by either overwriting it with another file before deletion; or by using the [DMEDIT](<dmedit.md>) process to change the name of the field from 'FILENAM to anything else.

The following **Output** window messages display on successful completion of files:
    
    
    >>> nnnnnnnn RECORDS IN FILE filename  
    >>> FILE filename DELETED OK

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be deleted. If IN is a catalogue file, then all the files in the catalogue will be deleted if confirmed. |  Input |  Yes |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CONFIRM |  |  Option |  Description  
---|---  
1; |  If **IN** is a catalogue file, then a request for confirmation will be issued for each file in the catalogue. If IN is a individual database file, then confirmation that the file is to be deleted is requested. Default: (0). >>> OPERATING ON A CATALOGUE FILE INPUT <<< >>> ARE YOU SURE YOU WISH TO DELETE ALL FILES <<< >>> PRESS <RETURN> TO CONTINUE (OR ! TO TERMINATE) >  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !DELETE &IN(FILE)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> SECURITY VIOLATION ON FILE nnnnnnnn |  If the file has been specified (SECURI process) to be No Access, (i.e. no read or write permitted), a message will be produced; the file will not be deleted.  
>>> SECURITY VIOLATION - OUTPUT FILE WRITE PROTECTED <<< |  The file is read only and the file will not be deleted. In either case use !SECURI to change the security access to read/write and then delete the file.  
  
Related topics and activities

  * DELETE Process