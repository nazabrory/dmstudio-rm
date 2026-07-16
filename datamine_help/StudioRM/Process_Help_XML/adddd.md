# ADDDD Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Add Fields**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ADDDD** and click **Run**.
  * Enter "ADDDD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ADDDD>).

## Process Overview

Adds extra fields to a file, requesting the field names and parameters interactively, in the same way as that used for entering a new Data Definition.

The default value is entered for all records of an explicit field.

**ADDDD** will also work on a file with just a Data Definition, e.g. a prototype.

Since **ADDDD** modifies the file description, it can be used for this purpose, with no addition of fields.

Implicit fields may be added in-place; i.e. the input file name can be the same as the output file name. For new explicit fields, the input file name must be different to the output.

A FORTRAN read format can be supplied at the File Description prompt of **ADDDD**. This format should be given within parenthesis and in standard FORTRAN format, for example (F10.3,2A4,5F9.3). Once this format is written into the _Data Definition_ of the file, it will be automatically detected and used by fixed format data input processes such as [INPUTW](<inputw.md>).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Overwritten |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output file. This may be the same as IN for in-place operation; in this mode, only implicit fields may be added. |  Output |  Yes |  Table  
  
## Notes

  * Clicking **OK** shows a prompt:

    
    
    >FILE DESCRIPTION>    Up to 60 characters.
    
    
    >FIELDNAME>    Name of the new field or ! to terminate.
    
    
    >TYPE A/N (N)>   A for alphanumeric, N for numeric
    
    
    >LENGTH (1)>    Length of the alphanumeric field. 
    
    
    >STORED (Y)>    Y for explicit, N for implicit
    
    
    >DEFAULT>    Default value.  Can be left blank
    
    
    >CONFIRM ? > enter OK, ok, YES, Y or y to end Data Definition

  * The ! character, entered at the **FIELDNAME** prompt, is generally used to terminate Data Definition entry.

**Note** : When running **ADDDD** in a macro, you must use the ] character to terminate the Data Definition entry. This will avoid the termination of the macro at that position.

  * If ! is entered at any prompt other than **FIELDNAME** then this will cancel the entry for the existing fieldname, and return control back to the **FIELDNAME** prompt.

  * **ADDDD** includes token parsing. This means that answers to successive interactive prompts can be entered on a single line separated by one or more spaces. For example, will give a numeric explicit field with a name of AU and a default value of 0:  
  
`FIELDNAME >AU N Y 0`

  * Default values for alpha fields require quotes if they contain imbedded blanks. Otherwise the process will treat the blank as a separator between the responses to successive interactive prompts.

  * Token parsing stops at 40 characters. Therefore the total number of characters on a line (including spaces) must not exceed 40. It also means that a default value of more than 40 characters cannot be entered using **ADDDD** (or [INPUTD](<inputd.md>) or [INPFIL](<inpfil.md>)). Longer default values should be entered using [DMEDIT](<dmedit.md>). [SETVAL](<setval.md>) can be used to propagate long alphanumeric strings through entire files.

  * Fields can be an alphanumeric or numeric, and are restricted to 24 characters. If you attempt to add a field name that already exists in the selected object, a warning will be displayed and it will not be added. Similarly, restricted Datamine field names cannot be used. 

  * Fields must not start with the following characters: "*", "&", "@", "!", "?", ".".

  * Fields must not contain spaces, or the following characters: ",", "!", " :", "*", "&", "=", "()".

## Examples

1\. Addition of one alphanumeric (ALPHA) and one numeric (NUMERIC) field.
    
    
    !ADDDD &IN(INFILE),&OUT(NEWFILE)  
  
---  
      
    
    INPUT DATA DESCRIPTION FOR FILE INFILE .FILE DESCRIPTION > Extended File  
      
    
    SUPPLY DETAILS OF FIELDS AS FOLLOWS-NEXT FIELDNAME > ALPHAFIELD 1 > ALPHA---------------------TYPE A/N(N)> ALENGTH (1)> 8     STORED? (Y)> Y DEFAULT >   
      
    
    NEXT FIELDNAME > NUMBERFIELD 2 > NUMBER---------------------TYPE A/N(N)> NSTORED? (Y)> YDEFAULT >  
      
    
    NEXT FIELDNAME >!END OF DDCONFIRM ? OK  
  
2\. Definition of a FORTRAN read format in the file description:
    
    
    !ADDDD &IN(INFILE),&OUT(NEWFILE)   
  
---  
      
    
    INPUT DATA DESCRIPTION FOR FILE INFILE .FILE DESCRIPTION > (F10.3,2A4,2F9.3,2A4,F6.0)  
      
    
    SUPPLY DETAILS OF FIELDS AS FOLLOWS-NEXT FIELDNAME > ALPHAFIELD 1 > ALPHA---------------------TYPE A/N(N)> ALENGTH (1)> 8STORED? (Y)> YDEFAULT >  
      
    
    NEXT FIELDNAME > NUMBERFIELD 2 > NUMBER---------------------TYPE A/N(N)> NSTORED? (Y)> YDEFAULT >  
      
    
    NEXT FIELDNAME > !END OF DDCONFIRM ? OK  
      
    
       
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> BLANK FIRST CHARACTER IN FIELDNAME \- ILLEGAL <<< |  Blank fieldnames are not permitted. If one is entered, the above error message will be given and the FIELDNAME > prompt repeated.  
>>> MAX FIELDS - DATA DEFINITION TERMINATED <<< |  The maximum number of words occupied by fields is 64. Each numeric field takes 1 word, and each set of 4 characters in an alphanumeric field also takes one word. If the maximum number of words is exceeded, the Data Definition entry will be terminated with the above message; any multi-word alphanumeric field being entered at this point may be incomplete.  
>>> FIELD NAME ALREADY EXISTS - IGNORED <<< |  The same fieldname cannot appear twice in a file; if it does, the process issues the error message above and returns to the FIELDNAME > prompt.  
>>> CANNOT ADD EXPLICIT FIELDS WHEN DOING IN-PLACE OPERATION - ILLEGAL <<< |  If an attempt is made to add explicit fields during an in-place update, the above message is displayed and the field is ignored.  
  
Related topics and activities

  * [Attribute Naming Convention](<../COMMON/Attribute_Naming_Convention.md>)
  * [INPUTC Process](<inputc.md>)
  * [INPUTD Process](<inputd.md>)
  * [INTEXT Process](<intext.md>)
  * [FILCOM Process](<filcom.md>)
  * [FILEXP Process](<filexp.md>)