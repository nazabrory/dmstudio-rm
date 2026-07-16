# ENGLOG Process  
  
To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ENGLOG** and click **Run**.
  * Enter "ENGLOG" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#ENGLOG>)](<../command_help/COMMAND%20TABLE_E.md#ENGLOG>).

## Process Overview

The process takes as input a file containing coded drillhole logs, and translates them through a dictionary file into readable English equivalents in a report format.

It can also take input from a second file containing remarks, and join this information at the appropriate downhole distance to the output report. The report can be sent to the printer, to a system file, and to the screen.

Report contents are typically:

>SYSFILE> |  Name of system file for output report. This prompt is only given if SYSFILE=1.  
---|---  
>HEADING > |  Prompts for heading lines. Format of heading line input: HDn[,COL=ccc|,JL|,JC|,JR];heading text : where n = heading number (1 to 9); ccc = start column; JL,JC,JR = justify left, centre and right, respectively. : = heading text terminator if not present, last non blank character used as terminator inclusively.  Heading lines must be entered sequentially starting at 1. Partial heading lines (i.e two lines with the same heading number) should be entered from left to right. Unless overriding options are used, heading text for partial heading lines will be concatenated. Heading input must be terminated with a blank line. A blank line is required even if there are noheading lines.  
>FOOTING > |  Prompts for footing lines. Format of footing line input: HDn[,COL = ccc][,JL|JC|JR];footing text : where n = footing number (1 to 9); ccc= start column; JL,JC,JR = justify left, centre and right, respectively. : = footing text terminator if not present, last non blank character used as terminator inclusively.  Footing lines must be entered sequentially starting at 1. Partial footing lines (i.e two lines with the same footing number) should be entered from left to right. Unless overriding options are used, footing text for partial footing lines will be concatenated. Footing input must be terminated with a blank line. A blank line is required even if there are no footing lines.  
>FIELD> |  Name of the field to be printed. Enter blank line to terminate entry of field names.  
>FORMAT> |  FORTRAN format specification for the field, including any leading or trailing blanks.  
>ENGLISH_FIELD> |  Enter the name of the first English field [as defined in the IN file DD] which is to be decoded through the DICT file or transposed directly to the output report. Terminate with a blank line.  
>FIELD> |  Name of the field to be printed. Enter blank line to terminate entry of field names.  
>ENGLISH_TYPE> |  Enter the value of the TYPE field in the DICT file which matches the ENGLISH_FIELD. If this is left blank then the field value will be transposed directly to the output report.  
>PRECEDENT> |  Enter a string of text of up to 30 characters which will precede the English field. This may be left blank.  
>ANTECEDENT> |  Enter a string of text of up to 30 characters which will follow the English field. This may be left blank.  
>FORMAT> |  If the English field is to be transposed rather than decoded then the format for the output report must be defined. This should be an A format for alpha fields or F or I for numerics.  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  The input data file containing the coded log. This must contain at least the BHID and FROM fields. All fields which are to be decoded [the English fields] must be of the same type [alpha or numeric] and the same length [if alpha]. |  Input |  Yes |  Undefined  
DICT |  The dictionary file containing the translated codes. It must contain the 3 fields TYPE, CODE and TEXT. |  Input |  No |  Undefined  
REMARKS |  The remarks file contains the three fields BHID, FROM and TEXT, and should be sorted on BHID and FROM. The TEXT field is multi- character alpha. |  Input |  No |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LHMARGIN |  Start column for printing (1). |  No |  1 |  1,79 |  Undefined  
RHMARGIN |  End column for printing (79). |  No |  79 |  1,79 |  Undefined  
LINES |  Number of lines per page of output (0). 0 - no paging. |  No |  0 |  Undefined |  Undefined  
NOFF |  |  Option |  Description  
---|---  
(0) |  Show form feeds.  
1 |  Suppresses form feeds.  
No |  0 |  0,1 |  0,1  
DOUBLE |  |  Option |  Description  
---|---  
(0) |  Single spacing [default];  
1 |  Double spacing.  
No |  0 |  0,1 |  0,1  
SYSFILE |  |  Option |  Description  
---|---  
(0) |  Send report to print file.  
1 |  Send report to a system file rather than the print file. The file name is requested interactively.  
No |  0 |  0,1 |  0,1  
ENG_MARG |  The number of spaces left as a margin on the lefthand side of the output report before the decoded text is written. Default is (0). |  No |  0 |  Undefined |  Undefined  
ENG_LENG |  The number of characters per line for the translated text part of the output report. This does not include the spaces defined by ENG_MARG.(79) |  No |  79 |  1,79 |  Undefined  
PRECDENT |  This parameter controls the output of the precedent. The precedent itself is defined interactively. Note that this parameter affects the printing of antecedents in the same way. |  Option |  Description  
---|---  
0 |  If there is no code in the IN file [ie if it is blank for an alpha field or '-' for numeric] then the precedent is not included in the report. (0)  
1 |  The precedent [if it has been defined] will always appear in the output report, even if the coded field to which it applies is absent data.  
No |  0 |  0,1 |  0,1  
NOCOMMA |  This parameter controls the output of a comma following each ENGLISH_FIELD . |  Option |  Description  
---|---  
0 |  a comma will be printed after each field, unless an antecedent has been specified (0)  
1 |  there will be no automatic printing of commas. If required, they must be specified as antecedents.  
No |  0 |  0,1 |  0,1  
NONL |  This parameter controls the output of a new-line following each drillhole interval. |  Option |  Description  
---|---  
0 |  a new-line will be output after each interval. (0)  
1 |  a new-line will not be output after each interval.  
No |  0 |  0,1 |  0,1  
SHOWCODE |  This parameter controls the output of codes if no english translation is given. |  Option |  Description  
---|---  
0 |  the code is ignored, i.e. treated as absent. (0)  
1 |  the code is printed without translation  
Yes |  0 |  0,1 |  0,1  
PRINT |  Display control: (0) =-1 : Suppress output. =0 : Display output. |  No |  0 |  -1,0 |  -1,0