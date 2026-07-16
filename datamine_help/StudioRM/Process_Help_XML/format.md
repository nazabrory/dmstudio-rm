# FORMAT Process  
  
To access this process:

  * Enter "FORMAT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FORMAT** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FORMAT>).

## Process Overview

Generate a tabulated report for output to the screen or to a system file.

Reports consist of 3 regions :-

  * **Header text** Text at the top of every page.
  * **Data columns** Field values listed vertically.
  * **Footer text** Text at bottom of every page.

Header and footer text can contain a number of tokens (in carets ^ ^), these are replaced with special values as the report is generated. The fields to use for data columns can be specified interactively or from a report definition file.

Substitution strings (e.g. $DATE#) may be included in header and footer lines. The expression ^page^ will print the incremental page number in the header or footer.  
  
Special DATAMINE characters -, +, tr(TR) are honored in printed report. Any numeric out of format range is printed as a '*'. Any character strings exceeding the format range are truncated to the right.

### Interactive Parameters

Once initial parameters are specified and the process is launched, you'll need to specify the following using the Command Line

##### SYSFILE

Only displayed if **SYSFILE** =1. Specifies name of system file to create. Max 56 characters.

##### REPORT NAME

Only displayed if **REPDEF** is supplied, and is the name of report definition to use. If entered, only definition records with a matching **REPNAME** are used. If blank, all records are used.

##### HEADING

Prompts for lines of text to use as report heading lines (max 9 lines). Specify heading lines as follows:

  * HDn[,{LHS=ccc|CTR=ccc|RHS=ccc| JL|JC|JR}];headingtext:

Where:

  * n = Heading line number (1 to 9);

  * LHS|CTR|RHS=ccc = Horizontal position for left, centre or right of <heading text>, respectively;

  * JL,JC,JR = Justify left, centre or right of <heading text>, respectively;

  * ':' = Heading text terminator. If not present, last non blank character used as terminator inclusively. Text can contain embedded ':';

Heading lines must be entered sequentially starting at 1. Part lines can be specified by supplying multiple entries with the same line number. Part lines are assembled in the order supplied. If no position specifiers are supplied, partial lines are concatenated.

Heading text can contain the following special replacement tokens:

  * ^PAGE^ = Current report page number.

  * ^DATE^ = System date at report start.

  * ^TIME^ = System time at report start.

  * ^LINE{,char(s)}^ = Specifies that a line of char(s) should be drawn across the report. One (or more) optional chars can be supplied to define the pattern to draw for the line. Default is blanks.

  * ^KFIELD{ ,WIDTH{,NDP}}^ =Specify a field name to be used as a Key for grouping page(s) of report records. Token is replaced with current value of KFIELD. WIDTH is optional for all fields. NDP can be supplied for numeric fields, but only if WIDTH has been supplied. Max of 10 separate ^xxFIELD^ tokens may be used. A change in the value of any ^KFIELD^ will trigger a break.

  * ^#DFIELD{,WIDTH{,NDP}}^ =Specify a field name that contains Data to be displayed. WIDTH,NDP operate in the same way as for ^KFIELD^. A change in the value of ^#DFIELD^ does not trigger a break.

The value of **DFIELD** in the 'current' record is always used for the displayed data value (in headers, the first record on the page contains the data displayed). In footers, the last record on the page contains the data displayed. Heading input is terminated with a blank line. A blank line is always required, even if there are no heading lines.

##### FOOTING

Prompts for lines of text to use as report footing lines. Specify footing lines as follows :
    
    
    FTn[,{LHS=ccc|CTR=ccc|RHS=ccc| JL|JC|JR}];footingtext:

Footing lines are supplied in exactly the same way as heading lines and can contain replacement tokens. Footing input is terminated with a blank line. A blank line is always required, even if there are no footing lines.

##### FIELD

The name of a field to be printed in a column down the report. A "format" for this field will then be prompted for. If REPDEF has also been supplied, any fields nominated here will be displayed to the right of those columns specified in REPDEF.

**Note** : **FIELD** /**FORMAT** (see below) interaction continues until terminated with a blank line. A blank line is always required, even if there are no entries.

##### FORMAT

Display format to use for this FIELD. Valid format types are:

  * Numeric (Real)[iX,]Fw.d[,jX] 

  * Numeric (Integer)[iX,]Iw[,jX] 

  * Alpha (character)[iX,]Aw[,jX]

Where:

  * i = number of leading blanks

  * w = total output width of field

  * d = number of decimal places

  * j = number of trailing blanks

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input data file containing fields to display in the report body. |  Input |  Yes |  Undefined  
REPDEF |  Optional report definition file. Must contain the following fields :- 

  * **REPNAME** A8 Report name key. 
  * **FIELD** A8 Output data field name. 
  * **INDEX** N Field output order. 
  * **WIDTH** N Output field width in char. 
  * **NDP** N Decimal places for N,0=int. 
  * **WRAPCHAR** A4 [Y|N] wrap wide alphas. 
  * **HT1** A12 FIELD header text, line 1. 
  * **HT2** A12 FIELD header text, line 2. 
  * **HT3** A12 FIELD header text, line 3. 
  * **FT1** A12 FIELD footer text, line 1. 
  * **FT2** A12 FIELD footer text, line 2. 
  * **FT3** A12 FIELD footer text, line 3. 

If **REPDEF** specified, a **REPNAME** key value identifying the report definition to use will be requested at the start of the interactive input stage. |  Input |  No |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
LHMARGIN |  Start character column for report. (1) All report output is located relative to this position on the screen/paper. |  No |  1 |  Undefined |  Undefined  
RHMARGIN |  End character column for report. (79) |  No |  79 |  Undefined |  Undefined  
LINES |  Number of lines per page of output. (20) = 0 Continuous output, no paging. >= 1 Output 'N' lines of Header+Footer+ Data text per report page. |  No |  20 |  Undefined |  Undefined  
HDSEP |  Horizontal separator to use between header text and the data columns. (3) Only applies to fields specified with the optional **REPDEF** file. |  Option |  Description  
---|---  
0 |  No separator.  
1 |  Output a blank line above data.  
2 |  Output a dashed line above data.  
3 |  Output a solid line above data.  
No |  3 |  0,3 |  0,1,2,3  
FTSEP |  Horizontal separator to use between the data columns and the footer text. (3) Only applies to fields specified with the optional **REPDEF** file. |  Option |  Description  
---|---  
0 |  No separator.  
1 |  Output a blank line below data.  
2 |  Output a dashed line below data.  
3 |  Output a solid line below data.  
No |  3 |  0,3 |  0,1,2,3  
GUTTER |  Number of spaces between adjacent data field columns in output report. (1) Only applies to fields specified with the optional **REPDEF** file. |  Option |  Description  
---|---  
0 |  Data columns abut each other. >= 1: Insert 'N' spaces between columns.  
No |  1 |  Undefined |  Undefined  
KEYBREAK |  Action to take when any of the optional header/footer key fields specified with the ^ **FIELD** ^ token q.v. change. (-1) |  Option |  Description  
---|---  
-1 |  Output the footer and start a new page when any ^ **FIELD** ^ changes. >= 0 Output the footer, then advance 'N' lines on the same page. If no room on that page for next header+footer and at least 1 data line, then start a new page.  
No |  -1 |  Undefined |  Undefined  
NOFF |  Form-feed character output. (0) |  Option |  Description  
---|---  
0 |  Output a form-feed for new page.  
1 |  Suppress form-feed output.  
No |  0 |  0,1 |  0,1  
DOUBLE |  Line spacing for data column records.(0) |  Option |  Description  
---|---  
0 |  No spaces between data lines.  
1 |  Inserts a blank line below each data line. i.e. "Double spaced"  
No |  0 |  0,1 |  0,1  
SYSFILE |  System file output control. (0) |  Option |  Description  
---|---  
0 |  No system file output.  
1 |  Report is output to a system file. If SYSFILE=1 , an output name will be requested during the interactive input.  
No |  0 |  0,1 |  0,1  
PRINT |  Screen output control for report. (1) |  Option |  Description  
---|---  
-1 |  Will stop screen output. >= 0: Report will appear on the screen.  
No |  1 |  -1,1 |  -1,0,1  
PAUSE |  Display control for screen paging. (-1) Only used for screen output **PRINT** >=0. = -1 Wait until user presses RETURN before displaying next page. |  Option |  Description  
---|---  
0 |  Display all pages without pause. >= 1: Pause for 'N' seconds, then automatically display next page.  
No |  -1 |  Undefined |  Undefined  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> INVALID MARGINS SET <<< |  The margins specified by the @LHMARGIN and/or @RHMARGIN parameters are incorrect. These parameters are ignored and the default values are assumed.  
>>> INVALID HEADING IDENTIFICATION <<< |  The heading number supplied is incorrect or out of sequence. Fatal; the process is exited.  
>>> INVALID HEADING INPUT FORMAT <<< |  The heading format supplied is incorrect. Fatal, the process is exited.  
>>> INVALID FOOTING IDENTIFICATION <<< |  The footing number supplied is incorrect or out of sequence. Fatal; the process is exited.  
>>> INVALID FOOTING INPUT FORMAT <<< |  The footing format supplied is incorrect. Fatal; the process is exited.  
>>> FIELD fieldname NOT IN FILE <<< |  The field name supplied does not exist in the input file. The name supplied is ignored and the file name prompt is repeated.  
>>> INVALID FORMAT - format |  The format supplied is not a valid FORTRAN format. The input is ignored and the format prompt is repeated.  
>>> OUTPUT nnn CHARACTERS - MAX ALLOWED mmm <<< |  The maximum output width, as determined by parameters @RHMARGIN and @LHMARGIN, was exceeded. Fatal; the process is exited.  
>>> FORTRAN ERROR NUMBER = nnn WRITING TO PRINTER |  A system error occurred when sending output to the line printer. Fatal; the process is exited.