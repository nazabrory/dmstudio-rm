# AED Process

To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **AED** and click **Run**.
  * Enter "AED" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#AED1>).

## Process Overview

File editor for creation, validation and modification of files.

Files may be set-up or validated using an optional definition file. This file may itself first be set-up in **AED** , or an existing definition file may be used, initially modified by the editor if required. Data may be entered by typing in the individual records or existing system files may be read in. In addition, character format files may be output. Any existing database file may be entered, and records may be inserted, modified or deleted. New records may be added under control of validation criteria set up in the definition file.

AED operates by displaying on the screen a series of 'pads', which provide a 'view' of part of the file. Each 'pad' consists of an 'information' line, a line displaying the field names, a data area of 14 records, and an Input and a Message line. Cursor movement is controlled by the usual cursor control keys or by entry of special characters on the input line. Extensive editing functions are provided by a set of sub-commands which are also entered on the input line. These sub-commands are described below.

**Note** : The Datamine **Table Editor** offers a more interactive approach to modifying Datamine (,dm) binary files.

## Automatic Creation of Definition File

If the input file does not exist, and no definition file was entered, then a definition file will be created as the initial stage of editing. Values are entered into it in exactly the same way as for any other file. The definition file is created to allow you to set up all the field names, types, lengths etc. that you require in the file you will be entering. The definition file also allows you to set up field maxima and minima and permitted values for validation.

Names/meanings of fields are given on next help screen. On exit (/E command) then the definition file will be saved as "name".%, where "name" is the name of the input file, and a file data definition will be created from the definition file for the user to enter data into.

If the user exits the editor using Quit (/Q) or Output (/O) then the definition file will be lost and AED abandoned.

The definition fields are:-

FIELD  |  The field name required (up to 24 characters)  
---|---  
TYPE  |  A (alphanumeric) or N (Numeric) only.  
LENGTH  |  In characters of the field: 4 for numeric.  
STORED  |  Y (Yes, for explicit) or N (No, implicit).  
FORM  |  Reserved for format; not currently used.  
FMIN  |  Minimum permitted value (numeric fields).  
FMAX  |  Maximum permitted value (numeric fields).  
INCR  |  Control on field values, appended records: \- Field will initially be set to default 0 Field will be same as preceding record +n Numeric field will be incremented by n.  
VALUES  |  If one entry only: a default value. If more than one, separated by commas, a full set of permitted values for the field.  
  
## Sub-commands.

These apply to all files, including the definition file. All commands are followed by <return>.

/A  |  Set current field blank  
---|---  
/B  |  Move the cursor to the bottom of the file. Its position in the current field is maintained  
/C/name/  |  Change the name of the current field to 'name'. If an attempt is made to change the name of the current field to a field name that already exists in the file, the following message appears on the Message line _'Field name already exists'_ and no change is made  
/n,mD  |  Delete lines n to m inclusive. If no record range is specified, the current record is deleted  
/E  |  End editor automatically saving the file  
/F/field/  |  Set the edit field to 'field'; i.e. only values of one that particular field may be edited  
/F  |  Unset the edit field  
/nG  |  Move cursor to line n. Its position in the current field is maintained  
/nI  |  Insert record(s) before line n. If no line is specified, insertion takes place before the current record. The initial field values will all be the default values  
/n,mL  |  List lines n to m inclusive. If no line range is specified the current record is listed  
/N  |  Append a new line to the end of the file  
/O  |  Output the file being created, validated or modified as a character system file and exit from the editor. Note that any modifications made will not be saved to the Datamine file  
/n,mP  |  Send records n to m to the printer  
/Q  |  Quit without saving.  
/R  |  Read from a system file. These can be entered when creating a new file, or when entering new records when using either /I or /N commands  
/n,mS/string/  |  Search for string' between records n and m  
/n,mS/string/string2/  |  Replace 'string' by 'string2' between records n and m  
/T  |  Move cursor to the top of the file. Its position in the current field is maintained  
/U  |  Undo all modifications currently on screen.  
/V/value/  |  Change field default value of the current field  
/n,mY  |  Validate records n to m according to the validation criteria specified in the definition file  
/Z  |  Show the Data Definition of the file  
//char  |  Replace '/' by 'char'  
  
Sub-commands **/N** and **/I** enter you into Insert mode; **/** terminates Insert mode.

**n,m** are line numbers: **-** for first, **+** for last. If line numbers are not specified then the current line is assumed.

In addition to the usual cursor movement keys, the following characters may be used to control cursor movement:

. |  Forward one field |  , |  Backwards one field  
---|---|---|---  
.. |  Forward one pad |  ,, |  Backwards one pad  
> |  Forward one record |  < |  Backwards one record  
>> |  Forward one page |  << |  Backwards one page  
<return> |  Moves forward one field |  |   
  
**?** provides Help on sub-commands and **??** shows permitted field values.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Overwritten |  Yes |  Table |  Input file to be edited. If this file does not exist, it will be created: first a definition file will be created (named "name".%) into which you enter the required fields, validation info, etc. Then the definition file is written out and used to define the IN file, into which you enter data.  
DEFN |  Overwritten |  No |  Undefined |  Definition file. Must contain the following fields:- FIELD, TYPE, LENGTH, STORED, FORM, FMIN, FMAX, INCR, VALUES. If neither the input file nor the definition file exist, both will be created. If the input file does not exist, but a definition file is entered, then the input file will be created from the definition file. Whenever a definition file exists, it may be used for validation. If both the input and the validation file exist, then input file entries will be validated against the definition file.  
APPHLP |  Input file containing application specific help information that will be included in the help display. An alphanumeric field named APPHLP will be expected, with a maximum of 56 characters displayed. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Table |  Edited output file. If this is not specified, then the input file will be overwritten.  
  
## Example
    
    
    AED &IN(ASSAYS)>>> FILE ASSAYS DOES NOT EXIST>>> ERR 9 <<< (********) IN GETDDINeither input nor definition file exists:Creating definition file ASSAYS %  
  
---  
  
## Error and Warning Messages

**Message** |  Description  
---|---  
Not a number |  Indicates that an attempt has been made to enter non-numeric data for a numeric field.  
>>> FILE ffffffff DOES NOT EXIST |  Either the input or definition file does not exist.  
>>> ERR 9 <<< (********) IN GETDDI |  Either the input or definition file does not exist.