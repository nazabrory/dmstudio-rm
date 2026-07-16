# set-field-output-status

See this command in the [**command table**.](<COMMAND%20TABLE_S.md#set-field-output-status>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "set-field-output-status"

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **set-field-output-status** and click **Run**.

## Command Overview

Write an attribute field to a file type. The format for this command is:
    
    
    set-field-output-status(FLDNAME ncode)    

where `FLDNAME` is the attribute field name and `ncode` is a bitwise integer defining the filetype to write to. The integers and field types are:

Integer |  File Type  
---|---  
1 |  Points  
2 |  Strings  
4 |  Holes  
8 |  Wireframes  
16 |  Results  
  
Valid `ncode` values are, for multiple file types, compound values. For example, to write an attribute field to NO file types you would use:
    
    
    set-field-output-status(FLDNAME, 0)

As another example, to write an attribute field to points and results:
    
    
    set-field-output-status(FLDNAME, 18)   

The latter example will write to points and results file types because 2 + 16 = 18