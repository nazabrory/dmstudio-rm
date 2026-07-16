# FIELD Macro Command

Detects the existence of a database file and sets up substitution variables to the values of fields in the file, for a particular record. Default values of fields may also be found.

The format for this macro command is:
    
    
    !FIELD <var1>=<filename>,<var2>=N,<var3>=<field1>,<var4>..

Where:

  * `<var1>` is a substitution variable. The variable is set to 0 if the file does not exist, or there is a file read error, or the file has no read access, or if any of the specified fields do not exist. If the file exists, the Data Definition can be read, read permission is granted, and all fields exist, `<var1>` becomes 1.

  * `<filename>` is the name of the database file.

  * `N` is the number of the record in the database file.

  * `<var2>` is a second substitution variable. This should be set to the value of the particular record required. A value of 0 will give field default values, while + or a value greater than the maximum number of records in the file will give the last record in the file.

  * `<field1>` nominates the name of the field to examine. Substitution variables will be set based on the value found in `<field1>`, and the state of the file `<filename>`.

  * `<var3>` is a third substitution variable.

  * and so on.

Multiple pairs in the form <varA>=<fieldA>, <varB>=<fieldB>, ... can be supplied to extract more than one value in a single field call. The list may be extended onto as many lines as necessary; continuation is implied by ending the previous line with a comma.

Note: The command may extend over more than one line by ending the previous line with a comma.

A message displays if a file does not exist, or read permission is denied, or there is a read error or any of the specified fields do not exist.

## Examples

Find the hole name of the 1000th sample in an assay file. The variable "$hole#" is used to return this value; "$exists#" will be set to 1 if the file ASSAYS is found; "$records#" will be set to the total number of samples in the file:
    
    
     !FIELD $exists#=ASSAYS,$records#=1000,$hole#=BHID  
  
---  
  
Extract the data area limits (mm) from a plot file. These values are usually stored as implicit fields in the plot file header:
    
    
    !FIELD $found#=PLOT.P,$recs#=0,$xorig#=XORIG, $yorig#=YORIG,   
  
---  
      
    
     $xrt#=XRT, $ytp#=YTP  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> !FIELD: ILLEGAL FORMAT <<< >>> ERR 90 <<< (0) IN SOFFIE <listing of command line> |  The command is malformed. Fatal; the macro or menu is cancelled. |  Check the command syntax.  
  
Related topics and activities:

  * [FILE](<file.md>)