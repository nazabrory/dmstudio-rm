# SELEXY Process

To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Select in 2D Perimeters**.

  * Enter "SELEXY" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SELEXY** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SELEXY>).

## Process Overview

Selectively copy records for which X and Y co-ordinate values lie within a perimeter defined in a perimeter file.

If the parameter @**OUTSIDE** =1, then values outside the perimeter will be selected. A perimeter must consist of at least the standard explicit numeric fields **XP, YP, ZP, PVALUE** and **PTN**. It must contain more than 2 and less than 1500 points.

### Multiple perimeters

Multiple perimeters may be processed at once. The output file will contain records which are selected by any of the perimeters. If selection is inside perimeters (default) then the effect is that selected records will come from the union of all perimeters. If selection is outside perimeters, then records will be selected if they lie outside any one perimeter, even if they lie inside another.

There is a limit to the number of perimeters which may be processed at one time. Under no circumstances may more than 100 perimeters be processed; but this limit may be lower, depending on the implementation and the number of points in each perimeter. All perimeters are first read into the real part of Studio 3's virtual array. Each point occupies 2 words. The size of this array is usually 100,000 words for implementations. With these values, the maximum number of points is 50,000 for most implementations. Each perimeter is closed in the array, by addition of an extra point. Thus the number of perimeters that can be handled depends on the total number of points in the input file. Any perimeters that cannot fit in their entirety into the virtual array will be ignored with a warning.

Once the perimeters have been read in, **SELEXY** makes a single pass through the input file, examining each record against all perimeters. This is a very fast method of processing data, and ensures that the order of the output file is the same as the order of the input file.

**Note** : The X,Y fields in the &**IN** file are assumed to refer to the same co-ordinate system as the **XP,YP** fields in the &**PERIM** file.

### Single Perimeter

A single perimeter may be selected from a multi-perimeter file by setting the required **PVALUE** into optional parameter @**PERIM**.

### Flagging selected records

Selected records may be flagged by up to 4 words of information taken from the perimeter that selected them. These four words may be either 4 numeric fields, or a combination of alphanumeric and numeric fields up to 4 words long. These fields are identified as * **ATTRIB1** -* **ATTRIB4** ; they must exist in the perimeter file, and will be placed in the output file if they do not already exist. For example, the **PVALUE** field may be used to flag which perimeter the record was selected by. If a record should be selected by more than one perimeter, then the values will be taken from the last perimeter that selected the record.

The value of the * **ATTRIB** fields used in flagging will be that associated with the first point of the perimeter.

### In Place operations

The input and output files may be the same for in-place flagging of values. Retrieval criteria may also be used if required. There is however no point in in-place selection unless the input file contains a field that may be flagged to indicate selection. In-place updating is specified by setting the input and output files to the same names, and specifying at least one * **ATTRIB** field that exists in both the perimeter file and the input file. The **PVALUE** field is often used for this purpose. An error is generated if the *ATTRIB field does not exist already in the input file, as new fields cannot be added in-place.

## Input Files

  
Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file for selection. Must have explicit numeric fields X and Y. |  Input |  Yes |  Undefined  
PERIM |  Perimeter file to control selection. Must have perimeter points in clockwise order, with the perimeter closed. The fields required are **XP,YP,ZP,PTN** , and **PVALUE** (standard perimeter format). All perimeters in the file will be used, up to a maximum of 100, or the number that will fit into the real part of the virtual array (usually 100,000 for all except your application on the PC, where it is 10,000). Perimeters which do not fit will be ignored with a warning. May also contain fields **ATTRIB1** -**4** which can be carried across to the output file. The value of these fields at the first point is used. |  Input |  Yes |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file containing all records lying within (or optionally outside) the perimeter. The **OUT** file may be the same as the IN file for in-place operations, unless extra fields ( **ATTRIB1** -**4**) from the perimeter file are being added.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Field in **IN** file defining the X co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
Y |  Field in **IN** file defining the Y co-ordinate. |  IN |  Yes |  Numeric |  Undefined  
ATTRIB1 |  Field from the perimeter file to be placed into the output file for all records which are selected. Up to 4 words may be entered, which may be 4 numeric fields or a mixture of alphanumeric and numeric fields totalling 4 words. |  PERIM |  No |  Any |  Undefined  
ATTRIB2 |  Second field from the perimeter file to be placed into the output file for all records selected by the perimeter. |  PERIM |  No |  Any |  Undefined  
ATTRIB3 |  Third field from the perimeter file to be placed into the output file for all records selected by the perimeter. |  PERIM |  No |  Any |  Undefined  
ATTRIB4 |  Fourth field from the perimeter file to be placed into the output file for all records selected by the perimeter. |  PERIM |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
OUTSIDE |  |  Option |  Description  
---|---  
1 |  Copies records of a file which have X and Y co-ordinates lying outside the perimeter (0).  
No |  0 |  0,1 |  0,1  
PERIM |  Set to the required **PVALUE** field to select a particular perimeter from **PERIM**. If **PERIM** is not set, then all perimeters will be processed. |  No |  Undefined |  Undefined |  Undefined  
PRINT |  >=1 Display summary stats for each perimeter and DDs. |  No |  0 |  0,1 |  0,1  
  
## Example

The file of drillholes 'BOREHOLE' is selected by a set of perimeters defining leases. The borehole file has EASTING and NORTHING co-ordinates. The lease perimeter file 'LEASES' contains lease numbers as its PVALUE field, and has a set of colours ( field) which are passed through to the output file 'MYHOLES' of selected data, so that each hole is flagged by lease number and colour.
    
    
    !SELEXY &IN(BOREHOLE),&PERIM(LEASES),&OUT(MYHOLES),  
  
---  
      
    
    *X(EASTING),*Y(NORTHING),*ATTRIB1(PVALUE),*ATTRIB2()  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
>>> WARNING - LESS THAN 3 POINTS IN PERIMETER nnnnnnn.nn |  The listed number is the PVALUE. The perimeter is ignored. |  Edit or remove perimeters with 3 or less points.  
>>> WARNING - TOO MANY PERIMETERS - ONLY FIRST nnn TAKEN <<< >>> LAST PERIMETER PVALUE TAKEN = nnnnnnn.nn |  Too many perimeters in perimeter file. Only the first nnn perimeters are used, subsequent perimeters are ignored. Processing continues with the taken perimeters. |  Reduce number of perimeters.  
>>> ERROR - TOO MANY POINTS (>1500) IN PERIMETER PVALUE nnnnnnn.nn <<< >>> ERR 130 <<< ( 1500) IN PRRDRV |  A perimeter has more than 1500 points (including the closure point). Fatal; the process is exited. |  Condition the perimeters and reduce the number of points per perimeter.  
>>> ERROR - NO PERIMETERS FOUND <<< >>> ERR 131 <<< ( 0) IN PRRDRV |  No perimeters in perimeter file. Fatal; the process is exited. |  Select a perimeter file which contains perimeters.  
>>> ERROR IN READING PERIMETER FILE <<< |  This usually means database corruption or a hardware error. Fatal; the process is exited. |  Check the perimeter file.  
>>> CANNOT ADD FIELDS FROM PERIMETER FILE WHEN UPDATING IN-PLACE <<< >>> ERR 132 <<< ( 0) IN SELEXY |  In-place updating specified, but one or more of the *ATTRIB1-4 fields entered did not already exist in the input file. Fatal; the process is exited. |  Check that the fields exist.  
>>> ATTRIBUTE FIELD aaaaaaaa NOT IN PERIMETER FILE <<< >>> ERR 133 <<< ( n) IN SELEXY |  One or more fields *ATTRIB1-4 (n=1-4) was not in the &PERIM file. Fatal; the process is exited. |  Check that the fields exist.  
>>> FIELD aaaaaaaa IN PERIMETER FILE IS NOT NUMERIC <<< ERR 134 <<< >>> ( n) IN SELEXY |  One or more of fields XP, YP, ZP, PTN, PVALUE (n=1-5) was not numeric in the &PERIM file. Fatal; the process is exited |  Check that the fields XP, YP, ZP, PTN, PVALUE in the perimeter file are numeric.  
>>> MISSING ESSENTIAL FIELD aaaaaaaa IN PERIMETER FILE <<< >>> ERR 135 <<< ( n) IN SELEXY |  One or more of fields XP, YP, ZP, PTN, PVALUE (n=1-5) was not in the &PERIM file. Fatal; the process is exited. |  Check that the fields XP, YP, ZP, PTN, PVALUE exist in the perimeter file.  
>>> X OR Y FIELD NOT FOUND IN FILE OR NOT NUMERIC <<< >>> ERR 136 <<< ( 0) IN SELEXY |  The *X or *Y fields were not found in the &IN file or were alphanumeric. Fatal; the process is exited. |  Check that the *X or *Y fields exist and that they are numeric.  
  
Related topics and activities

  * [SELPER Process](<selper.md>)