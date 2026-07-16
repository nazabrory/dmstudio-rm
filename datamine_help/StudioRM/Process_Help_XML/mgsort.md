# MGSORT Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Tables >> Sort**.

  * Enter "MDTRAN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MDTRAN** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MGSORT>).

## Process Overview

Sort a Datamine (.dm, .dmx) file into ascending or descending order of keyfields. Ascending order is the default; descending order is specified by setting the optional parameter @**ORDER** =2.

At least one keyfield must be specified and must appear as an explicit field. For alphanumeric fields, the collating sequence is the standard Datamine-specific sort sequence for text. The fields are sorted in the order in which they are specified. If a specified keyfield is not in the file, it is ignored. A warning message is given if @**PRINT** >=1.

**Note** : SORTX and MGSORT are identical, although separate process names have been retained and **SORTX** still accessible for legacy macro purposes.

Where sufficient memory exists, the table is sorted entirely within memory. However, if the memory required exceeds that available, the table is sorted in separate 'chunks', each temporarily stored to disk and then merged together for the final write. The maximum number of records that can be sorted is therefore limited only by available disk space.

This process includes the KEYSFRST option which, by default, maintains legacy behavior by reordering key fields in the output file so that KEY1 becomes the first field, KEY2 the second field, and so on. If you specify that key fields are not reordered, then the order of fields in the OUT and IN file will be identical.

This process allows you to determine how the sort is performed with regards to duplicate key field values, using the **ROWORDER** parameter.

Note: Although the order of fields in a file does not affect subsequent processing, it makes it more difficult to review the file using Datamine's Table Editor. For example, a borehole file which is sorted by BHID, FROM and TO is more difficult to manually validate if these fields are not adjacent.

## Sorting Text Values

## Notes

The SORTX and MGSORT processes honour the standard Datamine-specific sort sequence for text, shown below.
    
    
    AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789+-*/.,;:=?!@$%&()_'"<>[]

Note: A space is considered to be _before_ "A".

For macros and script operation, any number of KEYn fields can be defined (the previous limit of ten has been removed). Key fields must be specified in consecutive order, and without gaps: for example, adding KEY1, KEY2 and KEY4 are not allowed, and the reading of keyfields stop after KEY2.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File to be sorted. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Sorted file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY1-10 |  Keyfields for sorting . |  IN |  Yes |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ORDER |  |  Option |  Description  
---|---  
1 |  For ascending order  
2 |  For descending order (1).  
No |  1 |  1,2 | 1,2  
KEYSFRST |  |  Option |  Description  
---|---  
0 |  output fields in the same order as the input table  
1 |  output key fields first  
No |  1 |  0,1 |  0,1  
ROWORDER |  |  Option |  Description  
---|---  
0 |  Rows which contain duplicate key field values could be in any order (faster)  
1 |  Rows which contain duplicate key field values will be in the input file order (slower) (1)  
No |  1 |  0,1 |  0,1  
KEYTOL |  **KEYTOL** is the tolerance value used to test whether numeric key values are equal. It must be greater than or equal to zero. It replaces the previous heuristic comparison method.  If **KEYTOL** is set to a negative value then zero is used.  In a macro **KEYTOL** can be set to absent using -. "@**KEYTOL** =-" This will revert to legacy behaviour and use a heuristic comparison in relational commands and zero in sort.  |  No |  0.00001 |  0,+ |  Undefined  
  
## Example
    
    
    !MGSORT &IN(MODEL), &OUT(SMODEL), *KEY1(IJK),   
  
---  
      
    
               
      
    
    *KEY2(XC), *KEY3(YC), *KEY4(ZC)  
  
## Error and Warning Messages

Message |  Description  
---|---  
Warning: Keyfield: field_name is implicit and will be ignored. |  An implicit keyfield was provided. Since all values within it are identical, the keyfield is ignored.  
Warning: Missing keyfield. |  A requested keyfield could not be found in the file. The keyfield will be ignored.  
Error: No valid keyfields have been found. Process aborted. |  There were no valid keyfields to sort on. Keyfields may not have been specified, were not found in the file, or were implicit.  
Error: Failed to open input file. |  The required input file could not be found, or could not be opened for reading. The file may not exist, be open in another application, or you may not have access rights to the file.  
Error: Unable to create DmFile read buffer! |  An unspecified error (possibly memory related) when reading the input file.  
Error: Unable to open temporary chunk file file_name. |  An unspecified error when creating a temporary file - possibly due to a shortage of disk space.  
Error: Error writing to temporary chunk file file_name. |  An unspecified error when writing to a temporary file - may be followed by a description of the problem, if available.  
Error: Error whilst writing data to file_name. |  An unspecified error when writing to the output file - may be followed by a description of the problem, if available.  
Error: Could not create file_name. |  An unspecified error when creating the output file - may be followed by a description of the problem, if available. The output file may be open in another application, or you may not have access rights to overwrite or create it.  
Error: Could not create an instance of DmTable. |  An internal error when accessing the Datamine file.  
Error: Could not create an instance of DmSchema. |  An internal error when accessing the Datamine file.