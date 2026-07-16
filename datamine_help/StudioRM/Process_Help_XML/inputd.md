# INPUTD Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Create**.
  * Enter "INPUTD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **INPUTD** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#INPUTD>).

## Process Overview

Creates a file containing a Data Definition only. Such files may be used in subsequent data input and processing functions.

### Use of the ! Character

The ! character, entered at the FIELDNAME > prompt, normally is used to terminate Data Definition entry. Entered at any other prompt, the ! character has the effect of canceling the entry for the existing fieldname, and dropping control back to the FIELDNAME > prompt. 

Within a macro, the Data Definition cannot be terminated by the ! character, as this will terminate the [INPFML](<inpfml.md>) process; instead another special purpose character (such as [) may be used. 

### Prompts

When INPUTD is run, you are prompted for the following information in the Command toolbar:

  * > FILE DESCRIPTION >

Up to 24 character field 'name'. May be upper or lower case text, numbers, or special symbols. Internal blanks in field names should be avoided, and _ / . - used instead. Fields should not start with !, *, & or @, as such names will give rise to syntax problems under some circumstances.

  * > TYPE A/N (N) >

A for alphanumeric field, N or return for numeric field.

  * > LENGTH (1) >

Length in characters for alphanumeric fields only. Question omitted for numeric fields.

  * > STORED? (Y) >

Y or return for explicit fields, N for implicit (file constant) fields. Implicit fields are not supplied in data records.

  * > DEFAULT >

Default value to replace absent data (in processes which carry out this replacement). Just <return> for blank default value for alphanumeric and zero for numeric fields. For implicit fields the constant values must be entered.

The above is repeated for each field until ! entered for NEXT FIELDNAME. Then:

  * > CONFIRM? >

OK, ok, YES, Y or y to end DD.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  File to be created.  
  
## Example
    
    
    !INPUTD &OUT(ASSAYDD)INPUT DATA DESCRIPTION FOR FILE AssayDD .  
  
---  
      
    
    FILE DESCRIPTION >(2A4,2X,2F8.2,F6.2)<return>  
      
    
    Here a format is stored in the data definition for   
      
    
    use in the INPUTF process,   
      
    
    to load data from external files.  
      
    
    SUPPLY DETAILS OF FIELDS AS FOLLOWS-  
      
    
    NEXT   
      
    
    FIELDNAME     >    BHID    <return>  
      
    
    FIELD     1   >    BHID  
      
    
    ---------------------  
      
    
    TYPE A/N(N)   >    A       <return>  
      
    
    > LENGTH (1)    >    8       <return>  
      
    
    STORED? (Y)   >            <return>  
      
    
    > DEFAULT       >    DUMMY   <return>  
      
    
    BHID is an explicit alphanumeric field, 8 characters long, with a default   
      
    
     value of DUMMY.  
      
    
    NEXT  
      
    
    FIELDNAME     >    FROM    <return>  
      
    
    > FIELD     2   >    FROM  
      
    
    --------------------  
      
    
    TYPE A/N(N)   >            <return>  
      
    
    > STORED? (Y)   >            <return>  
      
    
    >DEFAULT       >            <return>  
      
    
    NEXT  
      
    
    FIELDNAME     >    TO      <return>  
      
    
    > FIELD 3       >    TO  
      
    
    ---------------------  
      
    
    TYPE A/N(N)   >            <return>  
      
    
    STORED? (Y)   >            <return>  
      
    
    >DEFAULT       >            <return>  
      
    
    FROM and TO are explicit numeric fields, with zero default values.  
      
    
    NEXT  
      
    
    FIELDNAME     >    %ASH    <return>  
      
    
    > FIELD     4   >    %ASH  
      
    
    ---------------------  
      
    
    TYPE A/N(N)   >            <return>  
      
    
    > STORED? (Y)   >            <return>  
      
    
    >DEFAULT       >            <return>  
      
    
    ASH is an explicit numeric field. Because the first character is a special   
      
    
     character (%) then the user is asked if the Data Definition is being terminated.   
      
    
     Because the answer is just<return>, which means NO, then the %ASH   
      
    
     name is accepted.NEXT  
      
    
    FIELDNAME     >    DENSITY   
      
    
     <return>  
      
    
    FIELD     5   >    DENSITY  
      
    
    ---------------------  
      
    
    TYPE A/N(N)   >            <return>  
      
    
    STORED? (Y)   >    n       <return>  
      
    
    DEFAULT       >    2.6     <return>  
      
    
    DENSITY is an implicit numeric field, with a value throughout the file   
      
    
     of 2.6.  
      
    
    NEXT  
      
    
    FIELDNAME     >    !       <return>  
      
    
    > END OF DD  
      
    
    CONFIRM ?     >    OK      <return>(Listing of Data Definition)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> BLANK FIRST CHARACTER IN FIELD NAME - ILLEGAL <<< |  Blank field names are not permitted. If one is entered, the FIELDNAME > prompt is given again.  
>>> FIELD NAME ALREADY EXISTS - IGNORED <<< |  The same field name cannot appear twice in a file; if it does, the FIELDNAME > prompt is given again.  
>>> MAX FIELDS - DATA DEFINITION TERMINATED <<< |  The maximum number of words occupied by fields is 64. Each numeric field takes 1 word, and each set of 4 characters in an alphanumeric field also takes one word. If the maximum number of words is exceeded, the Data Definition entry will automatically be terminated; any multi-word alphanumeric field being entered at this point may be incomplete.  
  
Related topics and activities

  * INPUTD Process

  * [INTEXT Process](<intext.md>)

  * [INPDDF Process](<inpddf.md>)

  * [INPFIL Process](<inpfil.md>)

  * [INPFML Process](<inpfml.md>)

  * [INPUTC Process](<inputc.md>)

  * [INPUTW Process](<inputw.md>)

  * [OUTPUT Process](<output.md>)