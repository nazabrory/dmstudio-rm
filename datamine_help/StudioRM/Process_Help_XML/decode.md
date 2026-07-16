# DECODE Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Set Value >> Decode**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DECODE** and click **Run**.
  * Enter "DECODE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DECODE>).

## Process Overview

Decode a named field of the input file through a dictionary file, writing a new output file containing all the fields of the input file, plus the new decoded field, which is given the name supplied in symbolic field * **TEXT**.

A _dictionary file_ is a database file containing two fields; **CODE** and **TEXT**. Each may be either an alphanumeric or a numeric field. There should be only one value of each **CODE** field; if there are multiple values, then only the first one will be taken. The dictionary file must be sorted on the **CODE** field. If it is not, use the **[SORT](<sortx.md>)** process prior to using the **DECODE** process. The maximum length of the **CODE** field (if alphanumeric) is 40 characters, and the maximum length of the **TEXT** field (if alphanumeric) is 80 characters. The **CODE** field should match in type and length the field to be decoded.

The dictionary **CODE** field is matched against the field specified as symbolic field * **CODE**. If the value matches, then the * **TEXT** field in the output file will contain the value from the **TEXT** dictionary field. If the * **CODE** field is not matched, the * **TEXT** field is set to the * **CODE** field, as closely as field lengths permit. If the fields are different types (i.e. not both numeric or alphanumeric), then the * **TEXT** field is set to absent data (if numeric field) or blank (if alpha field).

Typical uses of the **DECODE** process are to convert geological coding to a text string, or to convert from one language to another. The method is, however, very general, and may be used for example to decode one set of numbers from another; for example, to set slope angles as a function of a numeric rock type.

The dictionary file is first read into your application's virtual array, and is searched using a binary chop search. This is why it must be sorted on the **CODE** field.

**Note** : the default value of the * **TEXT** field in the output file is set to the default value of the **TEXT** field in the dictionary. This can be used to advantage, for example when setting up slope angles in an orebody model from a rocktype code using a dictionary. The default value of the **TEXT** field (representing the SLOPE angle) should be set to the required default **SLOPE** field value.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be decoded. This contains the field **CODE** (real name specified below) which is translated through the dictionary file **DICT** matching with the **CODE** field, and writing the equivalent **TEXT** field from the dictionary to the output file as field **TEXT**. |  Input |  Yes |  Undefined  
DICT |  Dictionary file (fields **CODE** and **TEXT**). There should be only one occurrence of each **CODE** value. This file MUST be sorted on **CODE**. |  Input |  Yes |  Dictionary  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Decoded file. An exact copy of the input file with the decoded field **TEXT** added.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
CODE |  Field to be translated in input file. |  IN |  Yes |  Character |  Undefined  
TEXT |  Field holding translated text, on output file. |  OUT |  Yes |  Character |  Undefined  
  
## Examples
    
    
    !DECODE &IN(FILE1), &OUT(FILE2), &DICT(DICT), *CODE(ROCK),   
  
---  
      
    
             *TEXT(LITHOL)  
  
The 4-character alphanumeric field rock in file1 is decoded through the dictionary file dict, with the translation going into field lithol in file file2. The dictionary file contains two alphanumeric fields; CODE, with a 4-character rocktype classification code, and TEXT with an English description, which is placed into field lithol in file2.
    
    
    !DECODE &IN(MODEL), &OUT(MODEL1), &DICT(SLOPDICT),   
  
---  
      
    
             *CODE(ROCK), *TEXT(SLOPE)  
  
The orebody model file model has a numeric rocktype field **ROCK**. This is decoded through the slope angle dictionary slopdict to give a new slope angle field **SLOPE** in the output model file model1. The dictionary would contain the **CODE** and **TEXT** fields; the **CODE** field gives the possible values of **ROCK** (sorted in order of **ROCK**) and the **TEXT** field gives the associated **SLOPE** angles required. The default value of the dictionary **TEXT** field will become the default **SLOPE** angle to be used by **PITEVA** where there are no cells.

## Error and Warning Messages

Message |  Description  
---|---  
Error: unable to open or read from... |  Unable to access or read from the specified input file. Fatal; the process is exited without creating an output file.   
Error: Error during reading Dictionary... |  Empty input or dictionary file. Fatal; the process is exited without creating an output file. Fatal; the process is exited without creating an output file.  
Error: TEXT field already exists in input file... |  *TEXT field already exists in the input file or *CODE field name was not found in the input file. Fatal; the process is exited without creating an output file.  
Warning: CODE value has already been specified. Additional references will be ignored |  Code field already specified so duplicate references (following original) are ignored - non-fatal.  
Error: missing mandatory field |  A missing field, normally TEXT or CODE could not be found. Fatal; the process is exited without creating an output file.  
Error: Failed to open input file |  An input file could not be found at the specified location. Fatal; the process is exited without creating an output file.  
Error: Error during file copy |  An error occurred copying from the input to the output file. Fatal; the process is exited without creating an output file.  
Error: CODE field in input and output files differ in type |  The field definition for the CODE attribute in both input and output files is not identical (e.g. different type or implicit/explicit mismatch). Fatal; the process is exited without creating an output file.