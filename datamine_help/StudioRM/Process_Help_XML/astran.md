# ASTRAN Process

To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ASTRAN** and click **Run**.
  * Enter "ASTRAN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ASTRAN>).

## Process Overview

This process reads one or more ASCII sample assay files in SIF format and updates a DATAMINE database file by matching sample numbers. Up to 10 grade fields may be updated from each file.

**ASTRAN** expects to find a file **ASTRAN.LST** containing a list of SIF files to be processed. This file may be prepared by an operating system pre-processing script. Any files that have all records matched are renamed.

SIF files that do not have all their samples matched will be rewritten with a flag 'MATCHED: date' at the end of any matched records. On subsequent runs these previously matched records may be ignored or rematched according to the value of the @**UPDATE** parameter.

A database file &**XREF** is used to cross reference assay names as they appear in the SIF files (**ASSNAM**) and the database field name (**ELEMENT**). Multiple values of **ASSNAM** may be referenced to a field. This file also has a units field which specifies the units of the assay as stored in the database. Assays in the SIF file will be converted to match these units. Only one value of units should appear in &**XREF** for each value of **ELEMENT**.

Example of &**XREF** :
    
    
    =======================  
    ELEMENT UNITS ASSNAM  
    =======================  
    AU1 ppm Au  
    AU2 ppm Au(R)  
    AU2 ppm Au(R)  
    SULPHUR % S

A 2 valued DATAMINE environment variable **ASTRAN_COMMAND** is used by **ASTRAN**.

The first value is an operating system command or script to be run to pre-process the ASCII files and produce the ASTRAN.LST file.

The second value gives the format of the command to be used to rename a fully matched file. Each individual file name will be substituted for the $1.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input database file.  
  
This file must contain a sample identifier field. The default name for this field is SAMPLEID.  
  
It may be either Numeric or Alphanumeric. In addition, the IN file will contain a number of other fields: the names of elements and compounds to be matched with fields in the assay data files. It may also contain fields which are not matched such as BHID, FROM, TO, etc. |  Input |  Yes |  Table  
XREF |  Required assay name cross-reference file. This file is used to link the names of assay fields in the database file to fields in the assay transfer {SIF} file. It is also used to convert results from the assay file to database units. Required fields in the XREF file are:

  * ELEMENT -- name of field in the IN file. Alphanumeric; two words.
  * UNITS -- units stored in the IN file for the current field. Alphanumeric; one word. Allowable units are: '%' -- per cent. ppm -- parts per million. ppb -- parts per billion.
  * ASSNAM -- name of field in assay transfer file. Alphanumeric; two words. There must be at least one record for each assay field in the IN file. There must be one record for each alias of a given assay field. An assay transfer file may not reference an assay field more than once for a given job.

|  Input |  Yes |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
SAMPLEID |  Optional name of sample identifier field in the IN file. Only required if the name of sample identifier field is not "SAMPLEID". |  IN |  No |  Any |  SAMPLEID  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SPREFIX |  Optional parameter to specify number of prefix characters. If "SAMPLEID" is numeric, this must be 0 if specified, otherwise it must be less than 11. (2) |  No |  2 |  0,11 |  0,1,2,3,4,5,6,7,8,9,10,11  
SDIGITS |  Optional parameter to specify number of digits to form numeric portion of "SAMPLEID". If "SAMPLEID" is numeric then SDIGIT must lie between 1 and 6. If "SAMPLEID" is alpha- numeric, SDIGIT must lie between 0 and 16. (6) |  No |  6 |  0,16 |  0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16  
MAXERRS |  Maximum number of errors that will be tolerated before processing is aborted. |  No |  Undefined |  Undefined |  Undefined  
UPDATE |  Controls treatment of previously updated samples. |  Option |  Description  
---|---  
(0) |  Ignore previously updated samples.  
1 |  Check previously updated samples but only update if the assay field has a missing value.  
2 |  As 1 but overwrite any value in the assay field.  
No |  0 |  0,2 |  0,1,2  
  
## Example

The following line would appear in one of the DATAMINE environment files.
    
    
    ASTRAN_COMMAND = 'ls -c eg* > ASTRAN.LST',  
  
---  
      
    
    'mv $1 matched/$1.M'  
      
    
    SIF: As required by ASTRAN.  
  
ASTRAN expects the SIF file to comprise ASCII records of no more than 124 characters. These include 6 lines of leader followed by any number of data records containing sample number and up to 10 assays. Blank lines may precede the header.

### Line 1 of Header

where

JOB - Job code terminated by a comma.

n - Number of sample records.

m - Number of samples not recorded.

c - Number of assay columns present.

The last 3 fields may be separated by a number of spaces.

### Line 2 of Header

COL

1 - 20 ignored

21 - 26 6 digit date in format ddmmyy

27 - 107 up to 10 fields 24 characters wide with left justified assay name.

### Line 3 of Header

COL  
1 - 26 ignored  
20 - 107 up to 10 fields 24 characters wide containing units. One of %, ppm, ppb, PPM, PPB.  
Line 4-6 of Header  
3 lines ignored.

### Line 7 - End of File

COL

1 - 10 sample alpha code.

11 - 26 sample numeric code.

27 - 107 up to 10 fields 24 characters wide containing assay results.

**Note** : For data fields:   
  
All blank becomes missing value.  
7 spaces L becomes trace.  
7 spaces - becomes missing value.

If sample number has ** in cols 11-12 samples treated as not received.
    
    
    !ASTRAN &IN(ASSAY),&XREF(XREF),@SPREFIX=2.0,@SDIGITS=   
  
---  
      
    
     6.0,@MAXERR=100,@UPDATE=0  
      
    
    ASTRAN TIME >16:19: 3  
      
    
    ASSAY FILE: eg12345  
      
    
    JOB: EG 12345  
      
    
    ASSAY FILE: eg67890  
      
    
    JOB: EG 67890  
      
    
    >>> MERGING SAMPLE RECORDS <<<  
      
    
    >>> 7 RECORDS PROCESSED : TIME 16:19: 5 <<<  
      
    
    LISTING OF UNMERGED SAMPLES  
      
    
    FILE: eg67890  
      
    
    JOB: EG 67890 DATE: 230490  
      
    
    LINE SAMPLE  
      
    
    9 X 071717  
      
    
    >>> UPDATING FILE eg67890  
      
    
    The SIF file eg67890 has been partly matched and would now look like:  
      
    
    EG 67890, 4SAM 0SNR 2COL  
      
    
    AV630 250590 Au Au(R)  
      
    
    DATA STORE UNITS ppm ppm  
      
    
    LLD s in STORE UNITS 0.01 0.01  
      
    
    CO FILE ORIGINATED FROM THECO  
      
    
    X 71715 1.25 0.29 MATCHED: 27/ 4/90  
      
    
    X 71716 2.07 0.10 MATCHED: 27/ 4/90  
      
    
    X 71717 1.10 1.00  
      
    
    X 71719 2.04  
  
  

## Error and Warning Messages

Message | Description  
---|---  
CANNOT OPEN SAMPLE DATABASE FILE  
CANNOT OPEN CROSS REFERENCE FILE |  Check input files.  
"SAMPLEID" MUST BE AN EXPLICIT FIELD  
INVALID LENGTH FOR "SAMPLEID" FIELD  
"SAMPLEID" FIELD IS MISSING  
CORRUPT "SAMPLEID" FIELD |  Check SAMPLEID field.  
"SAMPLEID" FIELD TOO LONG |  SAMPLEID field is longer than 10 characters.  
INVALID VALUE FOR @SPREFIX |  @SPREFIX <0 or >10  
@SPREFIX INCOMPATIBLE WITH *SAMPLEID |  @SPREFIX is too large.  
INVALID VALUE FOR @SDIGITS |  @SDIGITS <0 or >16.  
*SAMPLEID SIZE CONFLICT |  SAMPLEID field is not compatible with parameters.  
@SPREFIX MUST BE ZERO IF *SAMPLEID IS NUMERIC |  AMPLEID in numeric and @SPREFIX>0.  
@SDIGITS MUST BE LESS THAN 7 |  @SDIGITS >6.  
REQUIRED FIELDS MISSING FROM &XREF FILE  
ERROR READING &XREF FILE |  Check &XREF file.  
FIELD MUST BE NUMERIC |  A field specified in &XREF is not numeric in &IN.  
INVALID UNITS IN &XREF FILE |  Units must be one of %, PPM or PPB.  
INCONSISTENT UNITS IN &XREF FILE |  More than one value of UNITS for an ELEMENT in &XREF.  
ASSAY NAME CONFLICT IN &XREF FILE |  An ASSNAM is cross referenced to more than 1 ELEMENT.  
TOO MANY RECORDS IN &XREF FILE |  More than 100 records.  
ERROR ENCOUNTERED WHILE RUNNING PRE-PROCESSOR |  The pre-processor command or script returned an error condition.  
CANNOT OPEN "ASTRAN.LST" |  This file has not been created or is already opened.  
CANNOT OPEN ASSAY FILE  
ASSAY FILE IS EMPTY |  Check database ASSAY file.  
LINE 1 OF HEADER RECORD INVALID  
LINE 2 OF HEADER RECORDS MISSING  
INVALID ASSAY DATE  
LINE 3 OF HEADER RECORDS MISSING  
LINE 4 OF HEADER RECORDS MISSING  
LINE 5 OF HEADER RECORDS MISSING  
LINE 6 OF HEADER RECORDS MISSING |  Assay file does not conform to SIF.  
INVALID ASSAY NAMES |  Assay name from SIF sample file not found in &XREF.  
INVALID ASSAY UNITS |  Units in SIF sample file not one of %, PPM or PPB.  
UNEXPECTED END OF FILE |  Number of sample records in the SIF file does match the value in line 1 of the header.  
TOO MANY "SAMPLES NOT RECEIVED" |  The number of bad records does not match the value given in line 1 of the header.  
INVALID SAMPLE DIGITS  |  A sample number in the SIF file has more than @SDIGITS digits.  
INVALID ASSAY VALUE |  An assay value in the SIF file is not numeric.  
THERE ARE NO ASSAY FILES |  No files listed in ASTRAN.LST  
ERROR READING SAMPLE DATABASE FILE  
DUPLICATE SAMPLE ASSAY  
DUPLICATE SAMPLE ON DATABASE |  A sample in the SIF file has already been matched into the database and has been matched again.  
ERROR ENCOUNTERED WHILE RENAMING FILE |  The system rename for a fully match file did not work. Check the ASTRAN_COMMAND environment variable.