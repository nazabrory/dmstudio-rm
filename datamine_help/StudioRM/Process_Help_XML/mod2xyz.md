# MOD2XYZ Process

To access this process:

  * **Model** ribbon **> > Manipulate >> Model to XYZ**.

  * Enter "MOD2XYZ" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MOD2XYZ** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MOD2XYZ>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

Assign field values from a block model to any file containing XYZ coordinate fields.

This can be useful for:

  * assigning a rocktype value from a block model to a drillhole file
  * assigning an interpolated grade from a block model to a drillhole file so that it can be compared with the actual sample value. In this case the field in one of the files must be renamed first before the process is run. 
  * assigning a value from a model to wireframe triangles. In order to achieve this the [COGTRI](<cogtri.md>) command should be run first to calculate the centre point of each triangle. Then the output file from **COGTRI** becomes the input file to **MOD2XYZ**.

The IN1 file is a standard block model file with one or more attribute fields. The IN2 file must include at least the three coordinate fields. The IN2 coordinate points are superimposed over the model cells and the selected field values (*F1, *F2, etc) are copied from the model cell to the sample point. The OUT file includes the same fields as the IN2 file plus the selected fields *F1, *F2, etc. If a sample point does not lie within a model cell then its field values, *F1, *F2, etc, will be set to absent data.

**Note** : This process supports **[retrieval criteria](<../COMMON/Retrieval_Criteria_Overview.md>)**.

## Input Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
IN1 |  Input |  Yes |  Block Model |  Input model containing fields F1, F2, etc.  
IN2 |  Input |  Yes |  Undefined |  Input file containing fields X, Y and Z  
  
### Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Copy of IN2 file with extra fields F1, F2, etc from input model file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  X coordinate field in IN2 file. |  IN2 |  Yes |  Numeric |  Undefined  
Y |  Y coordinate field in IN2 file. |  IN2 |  Yes |  Numeric |  Undefined  
Z |  Z coordinate field in IN2 file. |  IN2 |  Yes |  Numeric |  Undefined  
F1 |  1st field in IN1 model to be copied to the OUT file. |  IN1 |  Yes |  Numeric |  Undefined  
F2 |  2nd field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
F3 |  3rd field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
F4 |  4th field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
F5 |  5th field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
F6 |  6th field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
F7 |  7th field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
F8 |  8th field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
F9 |  9th field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
F10 |  10th field in IN1 model to be copied to the OUT file. |  IN1 |  No |  Numeric |  Undefined  
  
## Example
    
    
    !MOD2XYZ &IN1(MODELB2),&IN2(SAMPLEB),  
  
---  
      
    
    &OUT(SAMPLEB2),*X(XPT),*Y(YPT),*Z(ZPT),   
      
    
    *F1(ZONE),*F2(ROCK)  
  
Related topics and activities

  * [COGTRI Process](<cogtri.md>)