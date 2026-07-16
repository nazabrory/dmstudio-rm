# ONERR Macro Command

Transfers control to a specified label in the menu or macro if a fatal error occurs.

`!ONERR` works in a similar fashion to the !**[HOLD](<hold.md>)** command, except that transfer is made to the specified label rather than to the next command in the macro if a fatal error is found. 

The format is:
    
    
    !ONERR    GOTOXXXX  
  
---  
  
Where:

  * `XXXX `is a label in the macro (can be up to 16 characters long). 

The label may be separated from the [GOTO](<goto.md>) for ease of reading. Once the `!ONERR` command has been given, it remains in force until cancelled. This may be done by use of the `!NOHOLD` command.

Note: The label is not checked until a fatal error occurs and an attempt is made to take the transfer.

## Example

The following example is used to set up an error trap for a macro:
    
    
    !START 1  
  
---  
      
    
    !ONERR goto <label> # set the error trap  
      
    
    <statements1>       # main body of macro  
      
    
    !<label>:REM        # error handling subroutine  
      
    
    <statements2>       # error handling messages and commands  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> INCORRECT LABEL XXXX IN GOTOXXXX OR XXX NOT FOUND <<< <listing of command line> >>> ERR 75 <<< ( recordno) IN MACGET  
|  Either the label was too long (>4 characters) or was not found in the menu or macro. Fatal; the menu or macro is abandoned. recordno is the record number in the menu or macro (from !START). |  Check label length and name.  
  
Related topics and activities:

  * [HOLD Macro Command](<hold.md>)

  * [GOTO Macro Command](<goto.md>)