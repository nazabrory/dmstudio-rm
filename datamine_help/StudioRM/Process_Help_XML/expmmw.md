# EXPMMW Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Expand Mining Perimeters**.

  * Enter "EXPMMW" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#ESTIMATE>)](<../command_help/COMMAND%20TABLE_E.md#EXPMMW>).

## Process Overview

This process expands a set of planar perimeters according to a user defined minimum mining width (MMW). This will allow perimeters which describe geological or grade boundaries to be expanded into a mineable entity.

The perimeters must be planar, but not necessarily in one of the orthogonal planes. 

The process first calculates the plane of each perimeter, and transforms the coordinates into that plane; the perimeter is then tested against the MMW constraint and adjusted as necessary; finally the expanded perimeter is transformed back into its original plane. The test against MMW is done by first calculating the centre line of the perimeter. 

A minimum perimeter is created based on this centre line with the MMW being measured perpendicular to the line. Each side of the minimum perimeter is then 0.5 x MMW from the centre line. The original perimeter is then tested against the minimum perimeter and is adjusted, if necessary, to ensure that no part of it lies within the minimum perimeter. 

The expanded perimeter is then written to the output file. All perimeters will automatically be checked for crossovers and consecutive duplicate points Duplicate points will be removed. Malformed perimeters will be reported, but they will not be processed or included in the output file. Input perimeters may be either open or closed. Output perimeters will be closed. It is not possible to define an algorithm which will deal with every shape and size of perimeter. Therefore it has been implemented as a two pass process, controlled by parameter **MODE**. 

User interaction is required between the passes to check and if necessary edit the strings. Pass 1 (**MODE** =1) takes as input the original perimeters from the **PERIMIN** file and creates the **PERIMOUT** file containing the original perimeters, the centre line strings and the expanded perimeters. The strings in this file can then be checked interactively in the graphics window.

If **EXPMMW** has not produced a satisfactory expanded perimeter then the centre line string should be edited appropriately. Two extra fields will be created in the **PERIMOUT** file:

**PTYPE** \- the perimeter type field. This expects values:

  * 0 \- the original perimeter

  * 1 \- centre line string

  * 2 \- expanded perimeter

**PORIG** \- this field contains the **PVALUE** of the original perimeter.

If the **PERIMIN** file contains a field then these values will be carried through to the **PERIMOUT** file. The value of will be incremented by 1 for centre lines and by 2 for expanded perimeters. If the **PERIMIN** file does not contain a field, then a field will be created in the output file. The of each original perimeter will be assigned a value of 1, 2 for centre lines and 3 for the expanded perimeters. Editing the centre line strings in the graphics window will usually only involve small changes to the centre line strings near the intersection with the original perimeters.

Pass 2 through process **EXPMMW** takes as input a file containing both the original perimeters and the centre lines. Fields **PTYPE** and **PORIG** are required in the **PERIMIN** file. In practice it is probably best for the PERIMIN file to contain all perimeters even if the centre line did not require editing. In this way all the expanded perimeters are kept in the same file.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PERIMIN |  The input perimeter file. If **MODE** =1 then the fields required are **XP** ,**YP** ,**ZP** , **PTN** and **PVALUE** ie standard perimeter format. Any other fields in this file will not be copied to the output file. All valid perimeters in the file will be used.  If **MODE** =2 or 3 then it must also contain **PTYPE** and **PORIG** fields. In addition the file must be sorted on the keyfields **PORIG** , **PTYPE** and **PTN**. |  Input |  Yes |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOUT |  Output |  Yes |  String |  The output perimeter file containing the expanded perimeters. It may also contain a copy of the original perimeters and the centre line strings depending on the value of parameter **MODE**. The file will contain the standard perimter fields **XP** ,**YP** ,**ZP** ,**PTN** and **PVALUE** plus ,**PTYPE** and **PORIG**. Malformed input perimeters will be reported but not processed. In place processing is not permitted ie **PERIMIN** and **PERIMOUT** must be different files.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MMW |  The minimum mining width, measured perpendicular to the centre line of the perimeter. Any point on the expanded perimeter will be at least 0.5 x **MMW** from the centre line. |  Yes |  Undefined |  Undefined |  Undefined  
PINC |  Numeric increment for **PVALUE** s for centre line string and adjusted perimeter as written to the **PERIMOUT** file. If the **PVALUE** of the input perimeter is P then its centre line string will have a **PVALUE** of P+PINC and the expanded perimeter will have a **PVALUE** of P+2xPINC. The default value is (0.1). |  No |  0.1 |  Undefined |  Undefined  
MODE |  This parameter defines the contents of both the **PERIMIN** and **PERIMOUT** files. It has values: |  Option |  Description  
---|---  
1 |  **PERIMIN** : original perimeters  **PERIMOUT** : original perimeters centre lines expanded perimeters.  
2 |  **PERIMIN** : original perimeters centre lines  **PERIMOUT** : original perimeters centre lines expanded perimeters.  
3 |  **PERIMIN** : original perimeters centre lines  **PERIMOUT** : expanded perimeters For pass 1 MODE must be set to 1. For pass 2 **MODE** must be either 2 or 3. The default value of **MODE** is (1).  
No |  1 |  1,3 |  1,2,3  
NODIAG |  This parameter specifies whether the centre line of a square perimeter should be the diagonal or the length. It has values: |  Option |  Description  
---|---  
1 |  Centreline can be the diagonal  
2 |  Centreline will not be the diagonal  
No |  1 |  1,2 |  1,2