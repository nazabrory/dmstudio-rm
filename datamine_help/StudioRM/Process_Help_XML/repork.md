# REPORK Process

To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **REPORK** and click **Run**.
  * Enter "REPORK" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#REPORK>).

## Process Overview

Legacy tabulating report generator with provision for separate keyfield sections.

This process allows printing of headers according to the key field values. The user may select fields for tabulation, for display below each key field header. 

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. |  Input |  Yes |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY1-25 |  Optional key fields |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LINES |  Number of lines per page of output. If negative will be double spaced. |  No |  Undefined |  Undefined |  Undefined  
NOFF |  If set to 1, suppresses form feeds. |  No |  0 |  0,1 |  0,1  
PRNTCOLS |  Required print width in columns . |  No |  132 |  Undefined |  Undefined  
HEDCENTR |  If set to 1, page heading to be centred. |  No |  0 |  0,1 |  0,1  
HEDSPACE |  Number of lines spacing required between the page headings, key block, and table headings. |  No |  Undefined |  Undefined |  Undefined  
COMPRESS |  Set to 1 for compressed print option (only for some printers. Uses DPL24C convention). |  No |  Undefined |  0,1 |  0,1  
MINDSPLY |  Set to 1 to suppress screen display of the full report tabulation (0). |  No |  0 |  0,1 |  0,1  
SYSFILE |  |  Option |  Description  
---|---  
1 |  to send report to a system file rather than the printer or print file. File name is requested.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !REPORK      &IN(HOLES),*KEY1(BHID),  
  
---  
      
    
    @LINES=60.0,@NOFF=1.0,@PRINTCOLS=132.0,  
      
    
    @HEDCENTR=1.0,@HEDSPACE=5.0,@MINDSPLY=0.0,  
      
    
    @SYSFILE=1.0  
  
The defined report is then sent to the system file REPORK.DAT.

## Error and Warning Messages

Message| Description  
---|---  
>>> YOU HAVE EXCEEDED THE MAXIMUM FORMAT SPECIFIER LENGTH OF 250 CHARACTERS. ONLY THOSE FIELDS CURRENTLY DEFINED ARE TO BE OUTPUT <<<| The maximum width of 250 characters was exceeded. Any additional field is ignored.  
>>> FORTRAN ERROR NUMBER = nnnnnn WRITING TO PRINTER| A system error occurred when writing the output to the line printer. Fatal; the process is exited.  
  
Related topics and activities

  * [REPORT Process](<report.md>)