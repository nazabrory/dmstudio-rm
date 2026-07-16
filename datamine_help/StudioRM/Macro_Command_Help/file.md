# FILE Macro Command

Detects the existence of a database file from within a menu or macro, and, optionally, the number of records in the file.

The format is:
    
    
    !FILE <var1>=<filename>,<var2>=recs

Where:

  * `<var1>` is a substitution variable.

  * `<filename>` is the name of the database file.

  * `<var2>` is a second substitution variable.

The variable `<var1>` will be set to 0 if the file does not exist, or there is a file read error, or the file has no read access for the current usercode. If the file exists, the Data Definition can be read, and read permission is granted, `<var1>` becomes 1.

The optional variable `<var2>` will be set to the number of records in the file. This will be zero if `<var1>` is zero.

Note: A message displays if the file does not exist, or read permission is denied, or there is a read error or any of the specified fields do not exist.

## Example

Check that the file `COLLARS` exists and set the variable `$recs#` to the number of records in the file:
    
    
    !FILE $exist#=COLLARS, $recs#=RECS  
  
---  
  
Note: The variable `RECS` is not checked; any name following the = is permitted. The structure is defined for consistency, and to allow future extension of the format.

## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
!FILE: SUBSTITUTION VARIABLE OR FILE NAME OR RECS MISSING or 8 CHARACTERS  <<<<listing of command line>>>> ERR 89 <<< (0) IN MACGET |  The command is malformed. Fatal; the macro or menu is cancelled. |  Check the command syntax.  
  
Related topics and activities:

  * [FIELD Macro Command](<field.md>)