# SETVAL Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Set Value**.

  * Enter "SETVAL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SETVAL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SETVAL>).

## Process Overview

Insert a value into a given field either during copying of a file or as an in-place operation.

If done during a copy, the field contains the given value in every record in the output file. If done in-place, retrieval criteria may be used if desired to allow insertion of the value into only some of the records of the file, thus provided a selective replacement capability.

If retrieval criteria are used during a file copy, where the &**OUT** file is not the same as the &**IN** file, then the output file will only contain those records that were selected from the input file using the retrieval criteria.

### Prompts

When the process is run, the following prompts appear in the **Command** toolbar:

  * >FIELD

The name of the field in the file for which a value will be set.

  * >VALUE

The value to be set into the given field name. If the value is alphanumeric, this must be an alphanumeric string (not in quotes). If the field is numeric, this must be a number.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file. If this is the same file as the input, then values will be set in place.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MULTIFLD |  Allow multiple field names to be specified if non-zero (0). Up to 20 fields can be supplied. The ! character should be entered to terminate multi-field entry. | No | 0 | 0,1 | 0,1  
  
## Examples

Set to absent data all those values of the field **Ag** , where X=35 and Au>.1<10.
    
    
    !SETVAL &IN(Assays),&OUT(Assays)  
  
---  
      
    
    FIELD >Ag  
      
    
    VALUE >-  
      
    
    X=35,Au>.1<10  
  
In this example, the &**IN** file is the same as the &**OUT** file, so replacement is in place.

### Example 2

Set multiple fields in each record of file **Assays** that satisfies the same criteria as example 1:
    
    
    !SETVAL X=35,Au>.1<10,&IN(Assays),&OUT(Assays),@MULTIFLD=1  
  
---  
      
    
    FIELD >Ag  
      
    
    VALUE >-  
      
    
    FIELD >Cu  
      
    
    VALUE >-  
      
    
    FIELD >Pb  
      
    
    VALUE >-  
      
    
    FIELD >!