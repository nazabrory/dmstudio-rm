# ACCMLT Process

To access this process:

  * Sample Analysis ribbon **> > Statistics >> Statistics Processes >> Accumulate on Keyfields**.
  * Enter "ACCMLT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **ACCMLT** and click **Run**.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ACCMLT>).

## Process Overview

**ACCMLT** accumulates values for constant values of keyfields.

For example, if a file contained the fields **YEAR** , **MINE** , **CuProdn** , **AuProdn** then subtotals of **CuProdn** and **AuProdn** for each value of **YEAR** over all values of **MINE** could be produced.

The output is a new file containing the keyfields and the totals. The format is identical to the input file, except that all alphanumeric fields are eliminated, unless they form part of the keyfields.

The total keyfield value must be no more than 5 words long. 

Important: the input file should be sorted on the keyfields beforehand. If it is not, then totals will be for each set of sequential keyfields with the same value in the file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
  
## Output Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
OUT |  Output sub-total file. | Output |  Yes |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY1 |  Keyfield 1 for totalling. |  IN |  No |  Any |  Undefined  
KEY2 |  Keyfield 2. |  IN |  No |  Any |  Undefined  
KEY3 |  Keyfield 3. |  IN |  No |  Any |  Undefined  
KEY4 |  Keyfield 4. |  IN |  No |  Any |  Undefined  
KEY5 |  Keyfield 5. |  IN |  No |  Any |  Undefined  
KEY6 |  Keyfield 6. |  IN |  No |  Any |  Undefined  
KEY7 |  Keyfield 7. |  IN |  No |  Any |  Undefined  
KEY8 |  Keyfield 8. |  IN |  No |  Any |  Undefined  
KEY9 |  Keyfield 9. |  IN |  No |  Any |  Undefined  
KEY10 |  Keyfield 10. |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ALLRECS |  Accumulation flag (0). If set to 1 then all records will be copied to the output file showing the cumulative totals. |  No |  0 |  0,1 | 0,1  
UNSORTED |  Unsorted flag. Default (0). |  **Option** |  **Description**  
---|---  
0 |  \- An accumulated total is written to the OUT file every time the keyfield[s] changes. Hence, if the IN file is sorted on the keyfield[s] there will be 1 entry in OUT for each keyfield[s] value. If IN is not sorted on the keyfield[s], there may be multiple entries for the same keyfield[s] value in the OUT file.  
1 |  \- The accumulation is over all records with the same keyfield[s] value. Hence there will only be 1 entry in OUT for each keyfield[s] value, irrespective of whether the IN file is sorted or not. N.B. If UNSORTED=1, the cumulative totals option ALLRECS cannot be used. The process will automatically set ALLRECS to 0 if UNSORTED=1.  
No |  0 |  0,1 |  0,1  
  
## Error and Warning Messages

**Message** |  Description  
---|---  
>>> NO NUMERIC FIELDS TO ACCUMULATE |  ACCMLT accumulates all numeric fields which are not part of the key, but there were none. Fatal; the process is exited.  
>>> WARNING - VALUE OF FIELD nnnnnnnn TOO LARGE >>> ON RECORD NUMBER mmmmmmmm \- IGNORED |  A value greater than or equal to TOP was found. Warning; the record is ignored.  
>>> ERR 47 <<< ( 0) IN FNDKEY |  Warning; none of the specified key fields exist in the input files. Accumulation is carried out over all records.  
>>> KEYFIELD aaaaaaaa MISSING FROM FILE ffffffff |  A warning message that is produced if @PRINT >=1. The keyfield is ignored and processing continues.