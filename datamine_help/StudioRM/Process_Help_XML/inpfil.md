# INPFIL Process

To access this process:

  * **Data** ribbon **> > Transfer >> Text >> Input new DD and CSV Data**.
  * Enter "INPFIL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **INPFIL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_I.md#INPFIL>).

## Process Overview

Creates a file and enters free format data into it. Free format data is separated by commas.

The data may come either from the keyboard, or from a system file external to the database.

**INPFIL** acts like a combination of [INPUTD](<inputd.md>) & [INDATA](<indata.md>). Records may not start with the character !. This is because the ! symbol acts as the end-of-data character. Thus macro files should not be read in with INPFIL; use [INPUTC](<inputc.md>) instead.

**Note** : within a macro, the Data Definition cannot be terminated by the ! character, as this will terminate the **INPFIL** process; instead another special purpose character (such as [) may be used. 

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  File to be created.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
PRINT |  >=1 to display each record (0). |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !INPFIL &OUT(NEWDATA)  
  
---  
      
    
    INPUT DATA DESCRIPTION FOR FILE newdata .  
      
    
    FILE DESCRIPTION  > New Assay Data <return>  
      
    
    SUPPLY DETAILS OF FIELDS AS FOLLOWS -  
      
    
    NEXT  
      
    
    FIELDNAME     >    BHID<return>  
      
    
    FIELD     1   >    BHID  
      
    
    ---------------------  
      
    
    TYPE A/N(N)   > A <return>  
      
    
    LENGTH (1)    > 8 <return>  
      
    
    STORED? (Y)   >   <return>  
      
    
    DEFAULT       >   <return>  
      
    
    NEXT  
      
    
    FIELDNAME     > FROM <return>  
      
    
    FIELD     2   > FROM  
      
    
    ---------------------  
      
    
    TYPE A/N(N)   >   <return>  
      
    
    STORED? (Y)   >   <return>  
      
    
    DEFAULT       >   <return>  
      
    
    NEXT  
      
    
    FIELDNAME     > TO<return>  
      
    
    FIELD     3   > TO  
      
    
    ---------------------  
      
    
    TYPE A/N(N)   >   <return>  
      
    
    STORED? (Y)   >   <return>  
      
    
    DEFAULT       >   <return>  
      
    
    NEXT  
      
    
    FIELDNAME     > Cu<return>  
      
    
    FIELD     4   > Cu  
      
    
    ---------------------  
      
    
    TYPE A/N(N)   >   <return>  
      
    
    STORED? (Y)   >   <return>  
      
    
    DEFAULT       >   <return>  
      
    
    NEXT  
      
    
    FIELDNAME     > ! <return>  
      
    
    END OF DD  
      
    
    CONFIRM   ?   OK  <return>  
      
    
    SYSFILE><return>  
      
    
    DATA     >BH0001,0,12,0,0<return>  
      
    
    DATA     >BH0001,12,14,0.5,0.1<return>  
      
    
    DATA     >BH0001,14,16.3,1.2,0.53<return>  
      
    
    DATA     >!<return>  
      
    
       
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> SYSTEM FILE DOES NOT EXIST <<< |  The named file does not exist. Fatal; the process is exited.  
>>> NOT A NUMBER <<<  
>>> ERR 57 <<< (numbposn) IN STRDCD |  An illegal DATAMINE number has been entered. Warning; the record is ignored.  
  
Related topics and activities

  * INPFIL Process

  * [INTEXT Process](<intext.md>)

  * [INPDDF Process](<inpddf.md>)

  * [INPFML Process](<inpfml.md>)

  * [INPUTC Process](<inputc.md>)

  * [INPUTD Process](<inputd.md>)

  * [INPUTW Process](<inputw.md>)

  * [OUTPUT Process](<output.md>)