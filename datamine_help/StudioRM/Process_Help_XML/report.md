# REPORT Process

To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **REPORT** and click **Run**.
  * Enter "REPORT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#REPORT>).

## Process Overview

Legacy process to generate a tabulation to your own format requirements, providing up to 5 header lines per page, at up to 120 columns print width.

Formats available are 'A' for alpha fields and 'F', 'E, or 'I' for numeric fields, using the normal FORTRAN format conventions. Spaces may be included using the nX specification either before or after fields. Reports are displayed on the screen, and can be sent to the printer or print file, or alternatively a character system file.

Data is output using ordinary FORTRAN format conversions, so any illegal values or numbers out of range will be trapped by FORTRAN and handled in the normal method for the particular computer being used. Only in the case of I format output of numeric fields will your application check the size of the data value, and substitute a - or + for a printed number if the value is respectively too small or too large.

  * >SYSFILE> External file name (max 56 chars)

  * >HALFLINE> Prompts for ten half-lines of 60-column width as a heading to the report.

  * >FIELD> Name of the field to be printed.

  * >FORMAT> FORTRAN format specification for the fieldm including any leading or trailing blanks.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file. |  Input |  Yes |  Table  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LINES |  Number of lines per page of output. If negative will be double spaced. |  No |  Undefined |  Undefined |  Undefined  
NOFF |  If set to 1, suppresses form feeds. |  No |  0 |  0,1 |  0,1  
SYSFILE |  |  Option |  Description  
---|---  
1 |  to send report to a system file rather than the printer or print file. File name is requested:  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !REPORT &IN (datafile)  
  
---  
      
    
    HALFLINE>  
      
    
    HALFLINE>  
      
    
    HALFLINE> BHID Au  
      
    
    HALFLINE>  
      
    
    ....  
      
    
    FIELD> BHID  
      
    
    FORMAT>4X,A4,A2  
      
    
    FIELD> Au  
      
    
    FORMAT>2X,F4.1  
      
    
    FIELD> (blank)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> YOU HAVE EXCEEDED THE MAXIMUM FORMAT SPECIFIER LENGTH  
OF 250 CHARACTERS. ONLY THOSE FIELDS CURRENTLY DEFINED ARE TO BE OUTPUT <<< |  Warning; the maximum length of 250 characters for the record format specifier has been exceeded. Only those fields defined up to this point will be output.  
  
Related topics and activities

  * [REPORK Process](<repork.md>)