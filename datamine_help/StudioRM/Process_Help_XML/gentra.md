#  GENTRA Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Set Value >> Alpha to Numeric.**

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **GENTRA** and click **Run**.

  * Enter "GENTRA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_G.md#GENTRA>).

## Process Overview

General field transformation. Fields are transformed using one or more standard **GENTRA** transformation functions, field (data column) names and constants.

**Note** : See the process [EXTRA](<extra.md>) and the Datamine Table Editor for an alternative, more modern means of manipulating Datamine files.

### Notes about GENTRA

  * Most of the GENTRA functions require that the results of a function are saved to a new field.

  * OLDFIELD indicates the name of an existing field

  * NEWFIELD indicates the name of a new field

  * After END the prompt is:-  
>CONFIRM ? > OK, ok, YES, yes, Y or y to carry out transformations.

  * If the ERA (Erase) command is used, the field which has been erased cannot be re-created in the same pass through GENTRA. Removal of multiple fields can be typed as a single line response as follows:  
ERA FIELD1;ERA FIELD2; .......

  * Help information is available by typing HELP as the response to a prompt for a transformation:  
TRAN >HELP  
>>> TRANSFORMATION SUB-COMMANDS <<<  
<listing of all transformations>  
>>> CONDITIONAL SUB-COMMANDS <<<  
<listing of all conditional operators>

  * The DECA command converts an alpha field to a numeric (similar to the ALFNUM process). All characters are removed except + - 0 1 2 3 4 5 6 7 8 9 . and if possible it will interpret a real number. Otherwise NEWFIELD is set to missing value. Blank also becomes missing value ("-"). In some cases an alpha field may contain a number of occurrences of embedded numbers. The "nth" occurrence may be selected.

  * The ENCA command encodes part or all of an alpha field into selected positions of another alpha field. Character positions START_TO to END_TO in NEWFIELD are updated using characters from START to END in OLDFIELD. END is automatically calculated as the minimum of the length of OLDFIELD and START + (END_TO - START_TO).

  * The ENCN command encodes a numeric field into selected positions of an alpha field. Character positions START_TO to END_TO are updated using a formatted real number taken from a numeric field (OLDFIELD). The format is controlled by the available character positions (START_TO to END_TO) and a specified number of decimal places (NDP). If NDP is zero then the decimal point is omitted. Numbers are not converted to E format. If a number overflows the available character positions it is encoded as "*". Missing values become blanks. Character positions in NEWFIELD are automatically padded with leading zeros.

  * The ENCS command encodes part or all of a literal string into selected positions of an alpha field. This is the same as ENCA except that NEWFIELD is updated from a literal string (STRING) instead of another alpha field. STRING must be enclosed in single quotes if it contains blanks or colons. The quotes will be stripped off. Any characters within START_TO to END_TO not set from OLDFIELD or STRING will be padded to blanks.

  * For ENCA, ENCN, ENCS the following rules apply:

    * If NEWFIELD does not exist it will be created with length = int ((END_TO-1)/4)+

    * If END_TO is greater than the current field length of NEWFIELD and the GENTRA is not "in-place", then the length of NEWFIELD is automatically increased to length = int ((END_TO-1)/4+1.

    * If the GENTRA is "in-place", then the length of NEWFIELD will not be increased and END_TO will be set to length = min (END_TO,length) and the following warning given: "END_TO greater than field length

  * Two or more commands can be entered on the same line, separated by a semi-colan. This is particularly useful in macros where tests are being applied, as it will make the commands more readable. For example:

LTC OLDFIELD CONSTANT; ADD NEWFIELD OLDFIELD OLDFIELD2

However, it should be noted that there is a maximum of 40 characters on a line.

### GENTRA Functions and Syntax

GENTRA Function |  Description |  Function Syntax  
---|---|---  
ADD |  Add two fields together |  ADD NEWFIELD OLDFIELD OLDFIELD2  
ADDC |  Add a constant to OLDFIELD |  ADDC NEWFIELD OLDFIELD CONSTANT  
SUB |  Subtract OLDFIELD2 from OLDFIELD |  SUB NEWFIELD OLDFIELD OLDFIELD2  
SUBC |  Subtract CONSTANT from OLDFIELD |  SUBC NEWFIELD OLDFIELD CONSTANT  
MUL |  Multiply two fields together |  MUL NEWFIELD OLDFIELD OLDFIELD2  
MULC |  Multiply an existing field by a CONSTANT |  MULC NEWFIELD OLDFIELD CONSTANT  
DIV |  Divide OLDFIELD by OLDFIELD2 |  DIV NEWFIELD OLDFIELD OLDFIELD2  
DIVC |  Divide OLDFIELD by CONSTANT |  DIVC NEWFIELD OLDFIELD CONSTANT  
MOD |  The modulus of OLDFIELD and OLDFIELD2 |  MOD NEWFIELD OLDFIELD OLDFIELD2  
MODC |  The modulus of OLDFIELD and CONSTANT |  MODC NEWFIELD OLDFIELD CONSTANT  
SQRT |  Square root of OLDFIELD |  SQRT NEWFIELD OLDFIELD  
EXP |  Exponent of OLDFIELD of OLDFIELD |  EXP NEWFIELD OLDFIELD  
LOG |  Logarithm to the base 10 of OLDFIELD |  LOG NEWFIELD OLDFIELD  
LOGE |  Logarithm to the base e of OLDFIELD |  LOGE NEWFIELD OLDFIELD  
LOGN |  Logarithm to the base e of OLDFIELD |  LOGN NEWFIELD OLDFIELD  
RAIS |  Raise OLDFIELD to the power CONSTANT |  RAIS NEWFIELD OLDFIELD CONSTANT  
INT |  Truncate OLDFIELD to the nearest integer |  INT NEWFIELD OLDFIELD  
MAX |  Maximum of OLDFIELD and OLDFIELD2 |  MAX NEWFIELD OLDFIELD OLDFIELD2  
MIN |  Minimum of OLDFIELD and OLDFIELD2 |  MIN NEWFIELD OLDFIELD OLDFIELD2  
END |  End of function/transformation definition |  END  
SIN |  Sine of OLDFIELD (degrees) |  SIN NEWFIELD OLDFIELD  
COS |  Cosine of OLDFIELD (degrees) |  COS NEWFIELD OLDFIELD  
TAN |  Tangent of OLDFIELD (degrees) |  TAN NEWFIELD OLDFIELD  
CANC |  Cancel all transformations |  CANC  
QUIT |  Exit without transforming |  QUIT  
PREV |  Copy value from OLDFIELD's previous record |  PREV NEWFIELD OLDFIELD  
THIS |  Copy value from OLDFIELD's current record |  THIS NEWFIELD OLDFIELD  
NEXT |  Copy value from OLDFIELD's next record |  NEXT NEWFIELD OLDFIELD  
SETC |  Seta new field to a constant value |  SETC NEWFIELD CONSTANT  
ERA |  Erase an OLDFIELD |  ERA OLDFIELD  
ASIN |  Arcsine of OLDFIELD |  ASIN NEWFIELD OLDFIELD  
ACOS |  Arccosine of OLDFIELD |  ACOS NEWFIELD OLDFIELD  
ATAN |  Arctangent of OLDFIELD |  ATAN NEWFIELD OLDFIELD  
ABS |  Absolute (positive) value of OLDFIELD |  ABS NEWFIELD OLDFIELD  
PHI |  Inverse normal distribution function of OLDFIELD |  PHI NEWFIELD OLDFIELD  
LT |  Test if OLDFIELD less than OLDFIELD2 and execute next command if true |  LT OLDFIELD OLDFIELD2  
LE |  Test if OLDFIELD less than or equal to OLDFIELD2 and execute next command if true |  LE OLDFIELD OLDFIELD2  
EQ |  Test if OLDFIELD equal to OLDFIELD2 and execute next command if true |  EQ OLDFIELD OLDFIELD2  
GE |  Test if OLDFIELD greater than or equal to OLDFIELD2 and execute next command if true |  GE OLDFIELD OLDFIELD2  
GT |  Test if OLDFIELD greater than OLDFIELD2 and execute next command if true |  GT OLDFIELD OLDFIELD2  
NE |  Test if OLDFIELD not equal to OLDFIELD2 and execute next command if true |  NE OLDFIELD OLDFIELD2  
LTC |  Test if OLDFIELD less than CONSTANT and execute next command if true |  LTC OLDFIELD CONSTANT  
LEC |  Test if OLDFIELD less than or equal to CONSTANT and execute next command if true |  LEC OLDFIELD CONSTANT  
EQC |  Test if OLDFIELD equal to CONSTANT and execute next command if true |  EQC OLDFIELD CONSTANT  
GEC |  Test if OLDFIELD greater than or equal to CONSTANT and execute next command if true |  GEC OLDFIELD CONSTANT  
GTC |  Test if OLDFIELD greater than CONSTANT and execute next command if true |  GTC OLDFIELD CONSTANT  
NEC |  Test if OLDFIELD not equal to CONSTANT and execute next command if true |  NEC OLDFIELD CONSTANT  
DECA |  Convert the OCCURRENC embedded number in alpha OLDFIELD to numeric NEWFIELD |  DECA NEWFIELD OLDFIELD OCCURRENC  
ENCA |  Encode alpha OLDFIELD beginning at position START to alpha NEWFIELD from position START_TO to position END_TO |  ENCA NEWFIELD START_TO END_TO OLDFIELD START  
ENCN |  Encode numeric OLDFIELD using NDP decimal places to alpha NEWFIELD from position START_TO to position END_TO |  ENCN NEWFIELD START_TO END_TO OLDFIELD NDP  
ENCF |  Encode numeric OLDFIELD using internal Datamine floating point conversion into alpha NEWFIELD |  ENCF NEWFIELD OLDFIELD  
ENCS |  Encode literal string STRING beginning at position START to alpha NEWFIELD from position START_TO to position END_TO |  ENCS NEWFIELD START_TO END_TO STRING START  
IDXC |  Return the starting location of the literal STRING within alpha OLDFIELD to numeric NEWFIELD. If not found, 0 is returned |  IDXC NEWFIELD OLDFIELD STRING  
INDX |  Return the starting location of the alpha OLDFIELD 2 within alpha OLDFIELD to numeric NEWFIELD. If not found, 0 is returned |  INDX NEWFIELD OLDFIELD OLDFIELD 2  
LENG |  Return the number of characters in alpha OLDFIELD up to the last non-blank, to numeric NEWFIELD |  LENG NEWFIELD OLDFIELD  
SUBS |  Return the substring of alpha OLDFIELD that begins at position FROM and is at most LENGTH characters to the last non-blank. The substring is inserted into NEWFIELD, starting at position DESTINATION. FROM,LENGTH and DESTINATION are numeric fields |  SUBS NEWFIELD OLDFIELD FROM LENGTH DESTINATION  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file.  
  
## Example
    
    
    !GENTRA &IN(OLDFILE),&OUT(NEWFILE)1. Add a two character prefix to a numeric sample number.  
  
---  
      
    
    >ENCS SAMPLEID 1 2 JU 1  
      
    
    >ENCN SAMPLEID 3 8 SAMPLE 0  
      
    
    =====================  
      
    
    SAMPLEID       SAMPLE  
      
    
    =====================  
      
    
    JUJ002168     2168.0  
      
    
    JU000003         3.0  
      
    
    JU458221    458221.0  
      
    
    2. Split an alpha BHID into its alpha prefix and numeric portion.  
      
    
    >DECA BHIDN BHID 1  
      
    
    >ENCA BHIDA 1 2 BHID 1  
      
    
    ==============================  
      
    
    BHID         BHIDN     BHIDA  
      
    
    ==============================  
      
    
    SN082371   82371.0       SN  
      
    
    FP900734  900734.0       FP  
      
    
    JU000451     451.0       JU  
      
    
    3. 'THIS' operation for multi-word alpha field.  
      
    
    >ENCA FIELDB 1 8 FIELDA 1  
      
    
    4. 'SETC' operation for multi-word alpha field.  
      
    
    >ENCS TEXT 1 20 'DEFAULT VALUE' 1  
      
    
    5. Round numeric field to 3 decimal places.  
      
    
    >ENCN TEMP 1 12 VALUE 3  
      
    
    >DECA VALUE TEMP 1  
      
    
    6. Decode an alpha field of the form "yy/mm/dd" into 3 separate numbers.  
      
    
    >DECA YEAR DATE 1  
      
    
    >DECA MONTH DATE 2  
      
    
    >DECA DAY DATE 3  
      
    
    =========================================  
      
    
    DATE         YEAR     MONTH     DAY  
      
    
    =========================================  
      
    
    90/09/13     90.0      9.0     13.0  
      
    
    90/10/01     90.0     10.0      1.0  
      
    
    90/12/21     90.0     12.0     21.0  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ILLEGAL OPERATION CODE <<< |  An illegal transformation has been specified. Warning; the next transformation is requested.  
>>> FIELD aaaaaaaa DOES NOT EXIST |  The specified field name is not in the file and has not been created. Warning; the next transformation is requested.  
>>> BAD NUMBER, PLEASE RE-TYPE COMMAND |  A number specified for a constant is invalid. Warning; the user must re-enter the transformation required.  
>>> ILLEGAL ALPHANUMERIC FIELD <<< >>> ERR 42 <<< ( n) IN READOP |  An alphanumeric field was specified; GENTRA works on numeric fields. Warning; the next transformation is requested.  
>>> CANNOT RE-USE AN ERASED FIELD <<< |  Use a different field name. Warning; the next transformation is requested.  
>>> WARNING - ONLY nn MORE TRAN COMMANDS ALLOWED <<< |  Warning message displayed after 145 transformations have been entered.  
OPERATION aaaa INVALID OPERAND nnnnnnnnn.nn ABSENT DATA SUBSTITUTED |  Square root of a negative number or logarithm of a value less than 'TRACE' has been specified. Warning; the new field is given a value of absent data and the next transformation requested.  
>>> GENTRAN ABANDONED. NO FILES CHANGED. <<< |  QUIT or ! has been entered in response to the request for a transformation, or the number of transformations entered has exceeded 300. The process is exited.  
>>> NO TRANSFORMATION(S) REQUESTED BEFORE END <<< >>> GENTRAN ABANDONED. NO FILES CHANGED. <<< |  END has been entered as the first response to the request for a transformation. The process is exited.  
  
Related topics and activities

  * [EXTRA Process](<extra.md>)