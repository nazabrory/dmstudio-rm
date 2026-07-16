# OUTPUT Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Text Utilities >> Datamine File to Text**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **OUTPUT** and click **Run**.
  * Enter "OUTPUT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_O.md#OUTPUT>).

## Process Overview

Output a database file to a system character format file.

The file includes a special version of the Data Definition in front of it. This is used by the [INPDDF](<inpddf.md>) process to re-read the file back into a database. The format of the file produced is described in the INPDDF documentation. For interfacing with other systems, this Data Definition can be suppressed by setting the @**NODD** parameter to '1'.

The accuracy of the numeric values output is maintained, as far as possible, using a format which changes automatically with the magnitude of the number. It is therefore possible to output numbers spanning the whole range between the lowest and highest system values.

By default, all fields are output; however, the required fields, and the order in which they are output, can be chosen using the optional fields F1 \- Fn. This is helpful if the output file would otherwise be too wide for the system to handle correctly. The maximum permitted width of an output system file is 240 characters, except when exporting to CSV using the faster method described below.

If the database file name is a catalogue file (consisting of a series of file names with a field name of '**FILENAM** \- note the prefixed apostrophe), then first the catalogue file is output from the database file &**IN** , and then each file in turn, which is referenced in the catalogue file, is output. The name of each external system file generated will match that of the database file name.

Note: The following message is displayed when using OUTPUT with a catalogue file input: >>> OPERATING ON A CATALOGUE FILE INPUT <<<

### Exporting to CSV

A faster export method, described below, is invoked whenever the@CSVparameter is set to '1' and a catalog file isnotspecified.

The following additional parameters can be set:

  * @**DPLACE** \- set the number of decimal places used in the output data - for example "@DPLACE = 2" outputs up to 2 decimal places. The default of -1 indicates that the best representation for the magnitude of the data is used.

  * @**IMPLICIT** \- if "@IMPLICIT=1", and no required fields have been defined, all table fields are output, including implicit fields. The default is '0'.

When called from a script or macro, more than 25 required output fields can be defined using F1-Fnfields. These must be defined consecutively, and without gaps for example, F1,F2,F4 would not be allowed, and reading would stop afterF2.

If required output fields are defined, and a FIELDLST file is specified, then fields from the FIELDLST file are added to the end of those specified using the F1 \- Fn output fields.

In order to reduce the size of the output file, any trailing zeros (after the decimal point) and trailing spaces after text are automatically trimmed.

The maximum permitted width of 240 characters is not applicable when using this export method.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Database file to be output. If IN is a catalogue file, then all files in the catalogue are output. |  Input |  Yes |  Table  
FIELDLST |  File used to supply selected fields. |  Input |  No |  Undefined  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  Optional first output field. None specified means "all". |  IN |  No |  Numeric |  Undefined  
F2-25 |  Optional output fields. |  IN |  No |  Numeric |  Undefined  
FIELDNAM |  Field in FIELDLST to identify selected fields. |  FIELDLST |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CSV |  |  Option |  Description  
---|---  
1 |  Output in comma separated format (0).  
No |  0 |  0,1 |  0,1  
NODD |  |  Option |  Description  
---|---  
1 |  Suppress output of Data Definition (0).  
No |  0 |  0,1 |  0,1  
DPLACE |  Exporting to CSV only: specify the maximum number of decimal places to export. |  Option |  Description  
---|---  
-1 |  Use the best representation for the magnitude of the data.  
0 |  Export 0 decimal places  
1 |  Export 1 decimal place.  
2 |  Export 2 decimal places  
3 |  Export 3 decimal places  
4 |  Export 4 decimal places  
5 |  Export 5 decimal places  
No |  -1 |  -1,5 |  -1,0,1,2,3,4,5  
IMPLICIT |  Exporting to CSV only: if no output fields are specified, allows you to either export explicit fields only, or explicit and implicit fields. |  Option |  Description  
---|---  
0 |  All explicit fields are exported.  
1 |  All fields are exported, including implicit fields.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !OUTPUT &IN(DBFILE)  
  
---  
      
    
    SYSFILE>\DATAMINE\SYSTEM\ALPHADAT.DAT<RETURN>  
  
## Error and Warning Messages

**Message** |  Description  
---|---  
>>> FILE <name>  
>>> EXISTS ALREADY <<<  
>>> PRESS <RETURN> TO CONTINUE OR ! TO TERMINATE <<< |  To overwrite the existing system file, press <return>. This message is not produced in a macro - the existing file would be overwritten.  
>>> NO FIELDS TO OUTPUT |  None of the fields specified for output have been found. Fatal; the process is exited. If errors are detected in outputting files under catalogue control (such as database file does not exist), then the next file in the catalogue is attempted.  
Error: Error opening or reading from FIELDLST filefile_name\- the named FIELDLST file could not be opened. |  Faster CSV export method only: the process will continue as though the relevant fields had not been requested.  
Error: Missing requested field:field_name. |  Faster CSV export method only: a requested output field could not be found in the input file.  
Error: No requested fields have been found. Process aborted. |  Faster CSV export method only: none of the requested fields could be found.  
Error: Failed to open input file:file_name. |  Faster CSV export method only: unspecified problem opening or reading from the input file.  
Error: Could not create an instance of DmTable. |  Faster CSV export method only: an internal error occurred during Datamine file access.  
Error: Could not create an instance of DmSchema. |  Faster CSV export method only: an internal error occurred during Datamine file access.  
  
Related topics and activities

  * OUTPUT Process

  * [INTEXT Process](<intext.md>)

  * [INPDDF Process](<inpddf.md>)

  * [INPFIL Process](<inpfil.md>)

  * [INPFML Process](<inpfml.md>)

  * [INPUTC Process](<inputc.md>)

  * [INPUTD Process](<inputd.md>)

  * [INPUTW Process](<inputw.md>)