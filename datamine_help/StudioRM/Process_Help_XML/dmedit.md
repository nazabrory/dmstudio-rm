# DMEDIT Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Basic File Edit**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DMEDIT** and click **Run**.
  * Enter "DMEDIT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DMEDIT>).

## Process Overview

Edits a file in-place, that is, without creating a new copy.

The edit functions are selected by entering a single character command. Where required, commands prompt for extra information. The functions available are:

> F List all field names.  
> C Change a field name.  
> L List a line or lines of data.  
> D Delete a line or lines of data.  
> R Replace a data item over 1 or more lines.  
> S Search for a given data item.  
> H Provide help.  
> V Change default value of a field.  
> P Change last page/record.  
> E Exit from editor.

Thus the editor permits certain changes to the file Data Definition as well as to the data contained within the file. The C, R, S and V commands all work on fields, which are specified by the user. They may work on either numeric or alphanumeric fields; the type is detected by the editor. Only explicit (stored) fields may be edited. Attempts to edit implicit fields will produce an error message, causing the command to be abandoned.

**Note** : you can also use the **Table Editor** utility to modify files.

### Guidelines

  * Line Numbers are integers, entered in response to the **FROM** and **TO** prompts.

  * The **TO** number must be greater than or equal to the **FROM**.

  * If **FROM** is greater than the last line, the message is produced and the command abandoned:
        
        >>> PAST END OF FILE <<<

  * If **FROM** is entered as 0, the current line (last one searched, listed etc) is used.

If **TO** is entered as 0, a single line is assumed. If **TO** is given beyond the end of file, it will be set to the last record.

  * Errors in entering **FROM** and **TO** will cause the command to be abandoned.

  * Alphanumeric values are not enclosed in quotes ('). If they are shorter than the field length, they will be blank padded. If they are longer, they will be truncated.

  * Page/Record numbers are calculated as follows: run the edit process with parameter @**DEBUG** =1. This will display the required values **NPST** (start page number for data) and **NLRP** (number of logical records/page). Locate the last line in the file containing good data (**NLASTL**). Then:-
        
        NLASTP = NPST + (NLASTL-1)*NLRP + 1  
        NLASTR = NLASTL - (NLASTP-NPST)*NLRP

  * **DMEDIT** should not be used on an index file. If it is, the actual index file will be edited, not the files referred to. It is usually better to re-create the index.
  * Deleted records are still maintained in the file after editing, although they are not accessible. They may be removed by use of the **COPY** process.
  * **DMEDIT** may not be used to insert records. This may be done by use of the **EXTEND** process on a file with line numbers ([COPYNR](<copynr.md>) process), followed by [SORT](<sortx.md>) on the **RECORDNO** field.
  * **DMEDIT** may be aborted without change to the file by typing "!" in response to the "EDIT >" prompt.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be edited. |  Input |  Yes |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  Send a complete record of the edit session to the printer or print file if **ECHO** =1 , PRINT=2. |  No |  0 |  0,2 |  0,1,2  
  
## Example
    
    
    !DMEDIT &IN(ASSAYS)  
  
---  
      
    
    >>> EDITING FILE ASSAYS <<<  
      
    
    =============================  
      
    
    (Listing of available commands)  
      
    
    EDIT > L<return>  
      
    
    >>> LIST LINES  
      
    
    FROM > 1<return>  
      
    
    TO > 3<return>  
      
    
    1>>BH0001 0.000000 12.000000 0.000000 0.000000  
      
    
    2>>BH0001 12.000000 14.000000 0.500000 0.100000  
      
    
    3>>BH0001 14.000000 16.300000 1.200000 0.530000  
      
    
    EDIT > R<return>  
      
    
    >>> REPLACE DATA  
      
    
    FIELD > Cu<return>  
      
    
    THIS IS A NUMERIC FIELD  
      
    
    VALUE > 0.3<return>  
      
    
    FROM > 1<return>  
      
    
    TO > 1<return>  
      
    
    EDIT > L<return>  
      
    
    >>> LIST LINES  
      
    
    FROM > 1<return>  
      
    
    TO > 3<return>  
      
    
    1>>BH0001 0.000000 12.000000 0.300000 0.000000  
      
    
    2>>BH0001 12.000000 14.000000 0.500000 0.100000  
      
    
    3>>BH0001 14.000000 16.300000 1.200000 0.530000  
      
    
    EDIT > D<return>  
      
    
    >>> DELETE LINES  
      
    
    FROM > 2<return>  
      
    
    TO > 2<return>  
      
    
    CONFIRM ? OK<return>  
      
    
    EDIT > L<return>  
      
    
    >>> LIST LINES  
      
    
    FROM > 1<return>  
      
    
    TO > 3<return>  
      
    
    1>>BH0001 0.000000 12.000000 0.300000 0.000000  
      
    
    3>>BH0001 14.000000 16.300000 1.200000 0.530000  
      
    
    EDIT > E<return>  
      
    
    >>> >>> EDIT COMPLETED <<< <<<  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ILLEGAL COMMAND <<< |  Only C, D, E, F, H, L, P, R, S and V are valid commands.  
>>> FIELD NOT FOUND IN FILE <<< |  Field name requested in the C, R, S or V command does not exist in the file being edited.  
>>> FIELD ALREADY EXISTS <<< |  The new field name specified in the C command is already in the file.  
>>> FIELD IS IMPLICIT - CANNOT BE EDITED <<< |  Only explicit fields can be edited.  
>>> ILLEGAL LINE NUMBER <<< |  An illegal line number has been specified in the D, L, R, S or V command.  
  
Related topics and activities

  * [AED Process](<aed.md>)