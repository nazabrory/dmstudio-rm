# INPFML Process

To access this process:

  * **Data** ribbon **> > Transfer >> Text >> Input DD and Fixed Format Data**.
  * Enter "INPFML" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **INPFML** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#INPFML>).

## Process Overview

Creates a file and enters data of fixed format into it. The data may come either from the keyboard, or from a system file external to the database; the system file records must be no longer than 80 characters.

The data format may come either from the file description, entered when the Data Definition is requested, or from the format line.

1\.  |  INPFML may be considered as a combination of [INPUTD](<inputd.md>). Incorrect data records (i.e. not matching the specified format statement) will be ignored, with a message to the display.  
---|---  
|  |   
2. |  Records may not start with !. This is because the ! symbol acts as the end-of-data character.  
|  |   
3. |  Macro files, in which each command starts with !, are best entered through [INPUTC](<inputc.md>).  
|  |   
4. |  Within a macro, the Data Definition cannot be terminated by the ! character, as this will terminate the **INPFML** process; instead another special purpose character (such as [) may be used.  
|  |   
5. |  The user is prompted for the following information  
|  >FILE DESCRIPTION > |  Up to 60 character text file description, or a FORTRAN format in brackets, defining the format of data to be read in (e.g. by the INPUTF or INPUTW processes). Order of fields is that in the DD and the type of each field must match that in the DD. Character data must be in A4 units (e.g. 3A4,A2), numbers in E, F or G format (e.g. 3F12.0), integers as F format (e.g. F6.0) and X for spaces. Maximum length of format statement is 80 characters, including the enclosing brackets, and maximum length of data record to which format applies is also 80 characters.  
|  > NEXT FIELDNAME > |  Up to 24 character field 'name'. May be upper or lower case text, numbers, or special symbols. Internal blanks in field names should be avoided, and _ / . - used instead. Fields should not start with !, *, & or @, as such names will give rise to syntax problems under some circumstances.  
|  > TYPE A/N (N) > |  A for alphanumeric field, N or return for numeric field.  
|  > LENGTH (1) > |  Length in characters for alphanumeric fields only. Question omitted for numeric fields.  
|  > STORED? (Y) > |  Y or return for explicit fields, N for implicit (file constant) fields. Implicit fields are not supplied in data records.  
|  > DEFAULT > |  Default value to replace absent data (in processes which carry out this replacement). Just <return> for blank default value for alphanumeric and zero for numeric fields. For implicit fields the constant values must be entered.  
|  The above is repeated for each field until ! entered for NEXT FIELDNAME. Then:  
|  > CONFIRM? > |  OK, ok, YES, Y or y to end DD.  
|  > SYSFILE > |  External system file name from which the formatted data is to be read, or return for entry from the keyboard. Format of the system file name is system specific, with a maximum of 56 characters allowed, including pathnames.  
|  > FORMAT > |  FORTRAN format in brackets, defining the format of data records to be read. Order of fields is that in the DD and the type of each field must match that in the DD. Character data must be in A4 units (e.g. 3A4,A2), numbers in E, F or G format (e.g. 3F12.0), integers as F format (e.g. F6.0) and X for spaces. Maximum length of format statement is 80 characters, including the enclosing brackets, and maximum length of data record to which format applies is also 80 characters. If format is already in the FILE DESCRIPTION, then enter just return.  
|  > DATA > |  If no SYSFILE, data lines in defined format. ! terminates.  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  File to be created.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  >=1 to display each record (0). | No | 0 | 0,1 | 0,1  
  
## Example
    
    
    !INPFML   
  
---  
      
    
     &OUT(NEWDATA)INPUT   
      
    
     DATA DESCRIPTION FOR FILE newdata .  
      
    
    FILE   
      
    
     DESCRIPTION > New Assay Data<return>  
      
    
    SUPPLY   
      
    
     DETAILS OF FIELDS AS FOLLOWS -  
      
    
    NEXT  
      
    
    FIELDNAME   
      
    
     > BHID<return>  
      
    
    FIELD   
      
    
     1 > BHID  
      
    
    ---------------------  
      
    
    TYPE   
      
    
     A/N(N)> A<return>  
      
    
    LENGTH   
      
    
     (1)> 8<return>  
      
    
    STORED?   
      
    
     (Y)> <return>  
      
    
    DEFAULT   
      
    
     > <return>  
      
    
    NEXT  
      
    
    FIELDNAME   
      
    
     > FROM<return>  
      
    
    FIELD   
      
    
     2 > FROM  
      
    
    ---------------------  
      
    
    TYPE   
      
    
     A/N(N)> <return>  
      
    
    STORED?   
      
    
     (Y)> <return>  
      
    
    DEFAULT   
      
    
     > <return>  
      
    
    NEXT  
      
    
    FIELDNAME   
      
    
     > TO<return>  
      
    
    FIELD   
      
    
     3 > TO  
      
    
    ---------------------  
      
    
    TYPE   
      
    
     A/N(N)> <return>  
      
    
    STORED?   
      
    
     (Y)> <return>  
      
    
    DEFAULT   
      
    
     > <return>  
      
    
    NEXT  
      
    
    FIELDNAME   
      
    
     > Cu<return>  
      
    
    FIELD   
      
    
     4 > Cu  
      
    
    ---------------------  
      
    
    TYPE   
      
    
     A/N(N)> <return>  
      
    
    STORED?   
      
    
     (Y)> <return>  
      
    
    DEFAULT   
      
    
     ><return>  
      
    
    NEXT  
      
    
    FIELDNAME   
      
    
     > !<return>  
      
    
    END   
      
    
     OF DD  
      
    
    CONFIRM   
      
    
     ? OK<return>  
      
    
    SYSFILE>   
      
    
     data.dat<return>  
      
    
    FORMAT   
      
    
     > (2A4,F7.2,F7.2,F8.3)<return>  
  
## Error and Warning Messages

Message | Description  
---|---  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited.  
>>> FORMAT CONVERSION ERROR <<< (listing of record) >>> ERR 80 <<< ( 0) IN FMTDCD |  The given record did not match the format entered. Warning; the record is ignored.  
>>> ERR 94 <<< (charposn) IN INPFMT >>> ERROR IN FORMAT AT CHARACTER POSITION nnn FORMAT<<< >>> (listing of format) |  The format was illegal. Only A, E, F, G and X descriptors are allowed. Fatal; the process is exited.  
  
Related topics and activities

  * INPFML Process

  * [INTEXT Process](<intext.md>)

  * [INPDDF Process](<inpddf.md>)

  * [INPFIL Process](<inpfil.md>)

  * [INPUTC Process](<inputc.md>)

  * [INPUTD Process](<inputd.md>)

  * [INPUTW Process](<inputw.md>)

  * [OUTPUT Process](<output.md>)