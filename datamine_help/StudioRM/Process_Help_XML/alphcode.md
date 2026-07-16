# ALPHCODE Process  
  
To access this process:

  * Enter "ALPHCODE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **ALPHCODE** and click **Run**.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#ALPHCODE>).

## Process Overview

Converts and back-converts an alpha numeric code to a numeric code.

IN must contain either:

  * an alphanumeric field to code with numeric values (optionally based on a dictionary), or;

  * a numeric code to be back-converted to an alpha equivalent based on a dictionary.

The conversion method is determined by the @**INVERSE** parameter.

When **INVERSE** =0

  * You can code from alpha to numeric without an input dictionary (**INDICT**), and output dictionary (**OUTDICT**) is optional.

  * You can code from alpha to numeric using an input dictionary. 

WHEN **INVERSE** =1

  * You can code from numeric to alpha with an input dictionary.

  * If no input dictionary is provided, the process will fail.

### Dictionary Files

Dictionary file data can be specified (optionally) to decode either input (**INDICT**) and output (**OUTDICT**) data, or both.

The input dictionary file contains equivalent alphanumeric and numeric value-pairs and should have the same format as an **OUTDICT** file, which is created when converting alpha to numeric values. * **FIELD** and * **NFIELD** must be present. This file may be used when @**INVERSE** =0 or @**INVERSE** =1. If this file is not present when @**INVERSE** =0, numeric coding is created and written to **OUTDICT** (if provided). This file is _required_ when @**INVERSE** =1. If **INDICT** and **OUTDICT** are both specified, **OUTDICT** is a copy of **INDICT**.

The output dictionary file is created when generating alpha values from numeric values (**INVERSE** =0). **OUTDICT** provides a record of the numeric values created that correspond to the input alpha values. It also contains a count of the number of records with each alpha value. If **INDICT** and **OUTDICT** are specified, **OUTDICT** is a copy of **INDICT**. The output dictionary is always optional.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  File containing alpha field to code with numeric values (optionally based on a dictionary); or a numeric code to be back-converted to an alpha equivilent based on a dictionary. |  Input |  Yes |  Table  
INDICT | Input dictionary file. See "Dictionary Files". | Input | Yes, if INVERSE=1, otherwise no. | Table  
  
## Output Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
OUT |  Output file containing fields in the input file plus a numeric field containing the alpha coded values. If file is back-converted, this contains the alpha equivilent for the numeric field. | Output |  Yes |  Table  
**OUTDICT** | Output dictionary file. See "Dictionary Files" | Output |  No |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
FIELD |  The alpha field to use to create corresponding numeric values. This field should either exist in IN or INDICT |  IN |  Yes |  Any |  Undefined  
NFIELD |  The numeric field containing the numeric values corresponding the alpha values in *FIELD. This should be a new field name or exist in INDICT |  IN |  Yes |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
INVERSE |  A flag to determine the type of conversion to perform: =0 : Convert input FIELD in IN file from Alpha to Numeric, using INDICT if supplied. =1 : Back-convert input FIELD in IN file from Numeric to Alpha using INDICT. |  Yes |  0 |  0,1 | 0,1  
  
## Examples
    
    
    !START test1  
  
---  
      
    
    !echo 1 Adds field NCODE to test1 (without output dictionary )  
      
    
    !echo --------------------------------  
      
    
    !ALPHCODE &IN(_vb_holes),  
      
    
    &OUT(test1),*FIELD(LITH),*NFIELD(NCODE),@INVERSE=0.0  
      
    
    !END  
      
    
       
      
    
    !START test2  
      
    
    !echo 2 Adds field NCODE to test1 (with output dictionary)  
      
    
    !echo --------------------------------  
      
    
    !ALPHCODE &IN(_vb_holes),  
      
    
    &OUT(test2),&OUTDICT(dict1),  
      
    
    *FIELD(LITH),*NFIELD(NCODE),@INVERSE=0.0  
      
    
    !END  
      
    
       
      
    
    !START test3  
      
    
    !echo 3  Attempts to code LITH from NCODE (without input dictionary )  
      
    
    !echo    This should fail  
      
    
    !echo --------------------------------  
      
    
    !ALPHCODE &IN(test2),  
      
    
    &OUT(test3),*FIELD(LITH),*NFIELD(NCODE),@INVERSE=1.0  
      
    
    !END  
      
    
       
      
    
    !START test4  
      
    
    !echo 4 Attempts to code LITH from NCODE (with input dictionary)  
      
    
    !echo --------------------------------  
      
    
    !ALPHCODE &IN(test2),  
      
    
    &INDICT(dict1),  
      
    
    &OUT(test4),*FIELD(LITH),*NFIELD(NCODE),@INVERSE=1.0  
      
    
    !END  
      
    
       
      
    
    !START test5  
      
    
    !echo 5 Add field NCODE (with input & outout dictionary)  
      
    
    !echo --------------------------------  
      
    
    !ALPHCODE &IN(_vb_holes),  
      
    
    &INDICT(dictionary),  
      
    
    &OUT(test5),  
      
    
    &OUTDICT(dict5),*FIELD(LITH),*NFIELD(NCODE),@INVERSE=0.0  
      
    
    !END  
      
    
       
      
    
    !START test6  
      
    
    !echo 6 Add field NCODE (with input dictionary)  
      
    
    !echo --------------------------------  
      
    
    !ALPHCODE &IN(_vb_holes),  
      
    
    &INDICT(dictionary),  
      
    
    &OUT(test6),*FIELD(LITH),*NFIELD(NCODE),@INVERSE=0.0  
      
    
    !END