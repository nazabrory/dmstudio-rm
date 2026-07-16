# JOIN Process  
  
To access this process:

  * **Data** ribbon >> **Data Tools** >> **Relational** >> **Join**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **JOIN** and click **Run**.
  * Enter "JOIN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_J.md#JOIN>).

## Process Overview

Performs a relational join, subset join, weave or subset weave of two input files into an output file. The type of join required is controlled by the values of the optional parameters @**SUBSETR** AND @SUBSETF.

This process belongs to a group of four similar ones within the Datamine process collection; JOIN, SUBJOI, WEAVE and SUBWVE. Each provides a different outcome, as described by the following diagram:

  
[![](../Images/JOIN_SUBJOIN_WEAVE_SUBWEAVE.jpg)](<javascript:void\(0\);>)

By default, with @SUBSETR=0 and @SUBSETF=0, JOIN writes out all records and all fields from both input files. Records are compared on the specified keyfields, and if a match is found, the two records are combined into one on the output file. If both files have identical Data Definitions then the record from the second input file is the one written out. Thus in this case the second file updates the first. If no match is found then records are written out with absent data codes for the missing fields.

  * With @SUBSETR=1 and @SUBSETF=0, a relational subset join is carried out. See process [SUBJOI](<subjoi.md>) for further details.

  * With @SUBSETR=0 and @SUBSETF=1, a relational weave is carried out. See process [WEAVE](<weave.md>) for further details.

  * With @SUBSETR=1 and @SUBSETF=1, a relational subset weave is carried out. See process [SUBWVE](<subwve.md>) for further details.

At least one keyfield must be specified and must appear in both input files as an explicit field. The keyfield may be up to 5 words long, and support is provided for up to 30 fields. If a field is specified which does not exist in both input files, it is ignored, providing at least one field matches.

Both input files must be sorted in the order of the key fields before they can be joined. If this is not the case, the process will exit with an error message.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  First file to be updated (sorted on required keyfields). |  Input |  Yes |  Table  
IN2 |  Second file (update file) (sorted on required keyfields). |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY1 to 30 |  Keyfields for matching. Up to 30 keyfields can be specified. |  IN1, IN2 |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SUBSETR |  Controls whether all records or a subset are written to the output file. If set to (0) all records are written. |  No |  0 |  0,1 |  0,1  
SUBSETF |  Controls whether all fields or a subset is written to the output file. If set to (0) all fields are written. With SUBSETR and SUBSETF set to 0 JOIN writes out all records and all fields from both input files. With SUBSETR=1 and SUBSETF=0 a relational subset join is carried out. With SUBSETR=0 and SUBSETF=1 a relational weave is carried out. With SUBSETR=1 and SUBSETF=1 a relational subset weave is carried out. |  No |  0 |  0,1 |  0,1  
CARTJOIN |  If set to (0) and if no keyfields are specified the process will terminate with an error. If set to 1 the full Cartesian product is produced and written to the output file. No keyfields should be specified to produce the Cartesian product. |  No |  0 |  0,1 |  0,1  
KEYTOL |  KEYTOL is the tolerance value used to test whether numeric key values are equal. It must be greater than or equal to zero. It replaces the previous heuristic comparison method.  If KEYTOL is set to a negative value then zero is used.  In a macro KEYTOL can be set to absent using -. "@KEYTOL=-" This will revert to legacy behaviour and use a heuristic comparison in relational commands and zero in sort.  |  No |  0.00001 |  0,+ |  Undefined  
PRINT |  >=1 Display messages on Data definitions. Default is (0) |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !JOIN     &IN1(ASSAYS),&IN2(COLLARS.S),&OUT(HOLES),*KEY1(BHID)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> INPUT FILE nn NOT SORTED ON KEY FIELD(S) >>> POSITION IN FILE 1 IS nnnnnnnn >>> POSITION IN FILE 2 IS nnnnnnnn |  Fatal; the process is exited. The position numbers are the record numbers reached in each file.  
>>> FILE ffffffff CANNOT BE USED AS BOTH <<< >>> INPUT AND OUTPUT BY THIS PROCESS <<< >>> ERR 130 <<< ( fileno) IN JOIN |  Either the first or second input file has the same name as the output file. Fatal; the process is exited.  
>>> ERR 47 <<< ( 0) IN FNDKEY |  Warning; none of the specified key fields exist in the input files. The full Cartesian product is produced and written to the output file.  
>>> KEYFIELD aaaaaaaa MISSING FROM FILE ffffffff |  A warning message that is produced if @**PRINT** >=1. The keyfield is ignored and processing continues.  
  
Related topics and activities

  * [SUBJOI](<subjoi.md>)

  * [WEAVE](<weave.md>)

  * [SUBWVE](<subwve.md>)