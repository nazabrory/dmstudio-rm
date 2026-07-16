# ATTSET Process

To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ATTSET** and click **Run**.
  * Enter "ATTSET" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ATTSET>).

## Process Overview

Set the values of nominated attribute fields in a file based on the values of a given data field in the input file. Attribute values are defined relative to data ranges or by matching patterns.

The &**LEGEND** file can contain multiple attribute definitions. A legend name provides the key for each definition. Each legend may contain definitions for several data fields. For each data field, one or more attribute fields may be defined.

Each default field name in &**LEGEND** may be redefined on the command line via symbolic field names in the expected way. e.g. * **DATFLD1**(NORTH).

Where data and/or attribute fields are supplied in the legend definition file, the values specified on the command line must exist in the file.

Where the attribute field does not exist in the input file, but will be created in the output file, **ATTSET** will determine the type and length from the contents of the **ATTVALUE** field values.

To simplify the input and maintenance of the legend definition file, the specification of ranges does not differentiate between numeric and alphanumeric fields - all values are entered with alphanumeric fields. The following rules apply for the entry of range information to handle discrete, continuous and non-continuous data :-

The values entered in **DATMIN** , **DATMAX** and **DATEXP** must match the data type of the data field. Alphanumeric data entered into the **DATMIN** and **DATMAX** fields are handled like the existing retrieval criteria. Special numeric values Tr,Dl,+,- are recognized for numeric data.

Data entered into the **DATEXP** field is handled in the same way as the **PICREC** process. If full regular expressions are required, then **REGEXP** should precede the full regular expression.

If only **DATMIN** is defined, discrete values are assumed.

If some **DATMIN** or **DATMAX** values are missing an error will be reported. The standard upper and lower limit values for numeric and alphanumeric data should be used where no specific upper or lower bound is to be specified.

If both **DATMIN** and **DATMAX** are defined, DATMIN is inclusive on the lower bound, and non-inclusive on the upper bound. If DATMIN=DATMAX then a test for discrete values is assumed.

Overlapping ranges are not allowed. If, for example, a background color is to be set and a limited number of other ranges specified, then each interval must be specified.

During data entry in **[AED](<aed.md>)** or a similar input process, blank (space) field values can be left in the file, to eliminate the need to re-enter repeated field values. An additional process, **ATTCHK** is provided to fill in blank field values with the previous defined field value (in the column), and validate the content of the legend file.

**ATTSET** provides the functionality of multi-field **[SETVAL](<setval.md>)** or **[GENTRA](<gentra.md>)** but oriented to customized menu applications.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Overwritten |  Yes |  Undefined |  Input data file  
LEGEND |  Legend definition file. The following standard field names are expected: LEGEND A8 Legend key. DATFIELD A8 Data field in input file. DATMIN A12 Minimum value. DATMAX A12 Maximum value. DATEXP A40 Match regular expression. ATTFIELD A8 Attribute field name. ATTVALUE A12 Attribute field value. Alternate field names can be supplied to the process by specification through the symbolic field names. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file containing the additional attribute fields. May be the same as the input file but additional attribute fields will be ignored.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
DATFLD1 |  Optional data field. If no DATFIELD field is supplied, then DATFLD1 is used to specify the single required data field. Otherwise DATFLD1..5 can be used to select a subset of the data fields. |  IN |  No |  Undefined |  Undefined  
DATFLD2 |  Second optional data field from those listed in DATFLD. |  IN |  No |  Undefined |  Undefined  
DATFLD3 |  Third optional data field |  IN |  No |  Undefined |  Undefined  
DATFLD4 |  Fourth optional data field |  IN |  No |  Undefined |  Undefined  
DATFLD5 |  Fifth optional data field |  IN |  No |  Undefined |  Undefined  
ATTRIB1 |  First optional attribute field. If no ATTFIELD field is specified, then ATTRIB1 is used to specify the single required attribute field. Otherwise ATTRIB1..5 can be used to select a subset of the attribute fields. |  IN |  No |  Undefined |  Undefined  
ATTRIB2 |  Second optional attribute field from those listed in ATTFIELD. |  IN |  No |  Undefined |  Undefined  
ATTRIB3 |  Third optional attribute field |  IN |  No |  Undefined |  Undefined  
ATTRIB4 |  Fourth optional attribute field |  IN |  No |  Undefined |  Undefined  
ATTRIB5 |  Fifth optional attribute field |  IN |  No |  Undefined |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MODE |  Type of validation to be undertaken(0). |  Option |  Description  
---|---  
1 |  minimum value DATMIN used.  
2 |  minimum DATMIN and maximum DATMAX values used.  
3 |  matching expression used.  
No |  0 |  0,3 |  0,1,2,3  
INRANGE |  Type of in-place update (0). Where the attribute field exists in the input file, only those values satisfying the range or pattern will be updated if set to 1. All records are output. |  No |  0 |  0,1 |  0,1  
  
## Example

An example macro is shown here, together with a listing of the results file. Two separate legends are defined with names ROCK-LEG and MAT-LEG. Each is applied in turn to data file ATTDATA, creating output files containing fields 1 and 2 respectively. Finally the two output files are joined together so that both color fields are in the same file.
    
    
    !START INPFIL To demonstrate the use of ATTCHK and ATTSET!REM -----------------------------------------------------------------  
  
---  
      
    
    !REM Load legend file; this contains 2 legends ROCK-LEG and MAT-LEG  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !INPFIL &OUT(legend)  
      
    
    Attset example  
      
    
    LEGEND A 8 Y -  
      
    
    DATFIELD A 8 Y -  
      
    
    DATMIN A 12 Y -  
      
    
    DATMAX A 12 Y -  
      
    
    DATEXP A 40 Y -  
      
    
    ATTFIELD A 8 Y -  
      
    
    ATTVALUE A 12 Y -  
      
    
    [  
      
    
    ok  
      
    
    ROCK-LEG,ROCK, 0, 1,,1,1  
      
    
    , , 1, 2,, ,2  
      
    
    , , 2,10,, ,1  
      
    
    MAT-LEG,MATERIAL,,,[Ww][Aa][Ss][Tt][Ee] ,2,1  
      
    
    , ,,,[Ll][Oo]-[Gg][Rr][Aa][Dd][Ee] , ,2  
      
    
    , ,,,[Hh][Ii]-[Gg][Rr][Aa][Dd][Ee] , ,3  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !REM Load test data  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !INPFIL &OUT(attdata)  
      
    
    Attset data for example  
      
    
    ROCK N Y 0  
      
    
    MATERIAL A 8 Y -  
      
    
    [  
      
    
    ok  
      
    
    1,WASTE  
      
    
    2,LO-GRADE  
      
    
    2,HI-GRADE  
      
    
    2,Lo-Grade  
      
    
    2,Hi-Grade  
      
    
    0,Waste  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !REM Verify legend file  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !ATTCHK &IN(legend),&OUT(legend2),&ERROR(legerror)  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !REM Set attribute data using ROCK-LEG  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !ATTSET &IN(attdata),&OUT(attdata2),&LEGEND(legend2),@MODE=0.0,  
      
    
    @INRANGE=0.0  
      
    
    ROCK-LEG  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !REM Set attribute data using MAT-LEG  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !ATTSET &IN(attdata),&OUT(attdata3),&LEGEND(legend2),@MODE=0.0,  
      
    
    @INRANGE=0.0  
      
    
    MAT-LEG  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !REM Join the two data sets back into a single file  
      
    
    !REM -----------------------------------------------------------------  
      
    
    !SPLAT &IN1(attdata2),&IN2(attdata3),&OUT(attdata4)  
      
    
    !END  
      
    
    The output file:  
      
    
    =====================================================================  
      
    
    FILENAME ATTDATA4 testxdir  
      
    
    FILE CREATED BY SYSTEM USING SPLAT ON 18/ 9/94  
      
    
    ---------------------------------------------------------------------  
      
    
    FILE CONTAINS 6 RECORDS EACH OF LENGTH 5  
      
    
    ---------------------------------------------------------------------  
      
    
    FIELD TYPE WORD.NO STORED START DEFAULT  
      
    
    ---------------------------------------------------------------------  
      
    
    ROCK N 1 Y 1 0.0  
      
    
    MATERIAL A 1 Y 2 -  
      
    
    MATERIAL A 2 Y 3  
      
    
    1 N 1 Y 4 -  
      
    
    2 N 1 Y 5 -  
      
    
    =====================================================================  
      
    
    =====================================================================  
      
    
    ROCK MATERIAL 1 2  
      
    
    =====================================================================  
      
    
    1.0 WASTE 2.0 1.0  
      
    
    2.0 LO-GRADE 1.0 2.0  
      
    
    2.0 HI-GRADE 1.0 3.0  
      
    
    2.0 Lo-Grade 1.0 2.0  
      
    
    2.0 Hi-Grade 1.0 3.0  
      
    
    0.0 Waste 1.0 1.0  
      
    
    6 RECORDS LISTED  
  
Related topics and activities

  * [AED Process](<aed.md>)

  * [ATTCHK Process](<attchk.md>)

  * [ GENTRA Process](<gentra.md>)

  * [SETVAL Process](<setval.md>)