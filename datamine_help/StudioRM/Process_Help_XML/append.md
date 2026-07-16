# APPEND Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> Relational >> Append**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **APPEND** and click **Run**.
  * Enter "APPEND" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#APPEND>).

## Process Overview

Append two or more files together.

The Data Definitions (DDs) of the files do not have to be the same; if they are not, then a superset APPEND takes place. APPEND may be in-place if the DDs of all the files are identical.

Both input files are optional. The operation is:-

  1. If neither input file is defined, then APPEND will prompt for all files to be appended together. The first file specified defines the DD; all subsequent files must have an identical DD to or a subset of the first.
  2. If only &IN1 or &IN2 is defined, then APPEND will copy the file to the output. If the input file is a catalogue file, then APPEND will append all the files in the catalogue into the output file. Only files with the same DD (or a subset of the DD) as the first file will be appended.
  3. If both &IN1 and &IN2 files are specified, then the second file will be appended to the first. If &IN1 is a catalogue file, then all files specified in &IN1 will first be appended, followed by &IN2; or all files specified in &IN2, if &IN2 is a catalogue file. The output file DD will be a superset join of the two first file DDs, and all files on either input which match the DD (or have a subset of it) will be appended together. However if @PROTODD=1, then the first file in &IN1 will be taken as the definitive DD, and only files with this DD (or a subset of it) on either input will be appended together. This enables the first input to be used as a prototype for appending from a general catalogue.

In-place appending, where the output file is equal to &IN1, is allowed in the trivial case where two input files (not catalogues) are to be appended. In this case no retrieval criteria are permitted and both files must have identical DDs (or subset of &IN1). The output file can never be the same as &IN2.

If the optional parameter @SEQUENCE is set to 1, then a field 'FILENAME' is added to the output file. This field will contain the name of the file from which each record was appended. If @SEQUENCE is set to 2, then a field 'SEQUENCE' is added with a sequential file number (1,2,...) in it. If @SEQUENCE is set to greater than 2, then both fields are added. If APPEND is carried out in-place, then @SEQUENCE is ignored and a warning message displayed.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Input file 1. This may be a catalogue file. Omit for file prompting. Enter a prototype DD (and set PROTODD=1) for selection from a catalogue. Otherwise the DD of the first file will be combined with the first IN2 file (if any) for the output file DD, and only files matching (or a subset of) this DD will be appended. |  Input |  No |  Table  
IN2 |  Input file 2. This may be a catalogue file. Omit for file prompting. Enter a catalogue file (and set PROTODD=1) for selection from this catalogue using the prototype on IN1. Otherwise the DD of the first file will be combined with the first IN1 entry (if any) for the output file DD, and only files matching (or a subset of) this DD will be appended. IN2 files are appended after IN1 files. |  Input |  No |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file = file 1 for in place append, if IN1 nor IN2 are NOT catalogue files, both are defined, and have identical DDs. If SEQUENCE is set, then the output file will contain extra fields FILENAME (A,8) or SEQUENCE (N) or both.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SEQUENCE |  |  Option |  Description  
---|---  
1, |  add field FILENAME [A,8] into output file containing filenames of each input file.  
2, |  add field SEQUENCE [N] into output file containing a file sequence no. [1,2,...] for each file appended.  
3, |  add both FILENAME and SEQUENCE fields.  
No |  0 |  0,3 |  0,1,2,3  
PROTODD |  |  Option |  Description  
---|---  
1, |  Use the file on IN1 as a prototype for selection of files from a catalogue on IN2 to be appended. Ignored unless both IN1 and IN2 specified.  
No |  0 |  0,1 |  0,1  
PRINT |  |  Option |  Description  
---|---  
1, |  Show the output file DD after all files have been appended. If neither IN1 nor IN2 are specified, then the file names to be appended are prompted for:- Enter DATAMINE file name required, or <return> for default, or ] to end.  
No |  0 |  0,1 |  0,1  
  
## Example

In place append; both input files must have identical DDs:
    
    
    !APPEND &IN1(FILE1),&IN2(FILE2),&OUT(FILE1)  
  
---  
  
When only the output file (&OUT) is specified, the following displays:
    
    
    !APPEND &OUT(FILE4)  
  
---  
      
    
    Enter DATAMINE file name required or <return> for default, or ] to end.  
      
    
    FILE NAME [ ] > FILE1  
      
    
    File 1 name FILE1 from second input: 42 records appended.  
      
    
    Enter DATAMINE file name required or <return> for default, or ] to end.  
      
    
    FILE NAME [FILE1 ] > FILE2  
      
    
    File 2 name FILE2 from second input: 35 records appended.  
      
    
    Enter DATAMINE file name required or <return> for default, or ] to end.  
      
    
    FILE NAME [FILE2 ] > FILE3  
      
    
    File 3 name FILE3 from second input: 25 records appended.  
      
    
    Enter DATAMINE file name required or <return> for default, or ] to end.  
      
    
    FILE NAME [FILE3 ] > ]>>> 102 RECORDS IN FILE FILE4 <<<  
  
## Error and Warning Messages

Message| Description  
---|---  
*** Error - Output file same as input file 2.  
>>> ERR 121 <<< ( fileno) IN APPEND| The output file must not have the same name as the second input file. Fatal; the process is exited.  
*** Error - Retrieval Criteria set; cannot append in place.  
>>> ERR 122 <<< ( fileno) IN APPEND| The output file name has the same name as the first input file for an in-place append, but a retrieval criteria was set. Retrieval criteria may not be set for an in-place append. Either specify a different output file, or append in-place and then copy the output file under retrieval criteria. Fatal; the process is exited.  
*** Error - Different DDs; cannot append in-place.  
>>> ERR 123 <<< ( fileno) IN APPEND| The output file name has the same name as the first input file for an in-place append, but the DDs of the first and second input files are different. Fatal; the process is exited.  
*** Error - Cannot append in-place with catalogue files.  
>>> ERR 124 <<< ( fileno) IN APPEND| The output file name has the same name as the first input file for an in-place append, but both the first and second input files are catalogue files. Fatal; the process is exited.  
*** Warning - @SEQUENCE parameter cannot be used with in-place append.| Optional parameter @SEQUENCE is ignored when doing in-place append.  
*** Warning - File AAAAAAAA has different DD to previous file - skipped.| The DD of the specified file of one the input catalogue files does not match the required DD and it is skipped.