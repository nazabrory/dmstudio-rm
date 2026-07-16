# BHCOUNT Process

To access this process:

  * Estimate ribbon **> > Validate >> Drillhole Count**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **BHCOUNT** and click **Run**.
  * Enter "BHCOUNT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/commandtable_B.md#BHCOUNT>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

This command counts the number of boreholes used to estimate each model cell. This information can then be used to assist in assigning a reserve category to the model cells.

The two input files, MODELIN and SAMPIN, must have been created by the grade estimation process [ESTIMA](<estima.md>): 

  * **MODELIN** \- the output model from ESTIMA.

  * **SAMPIN** \- the ouput sample file from ESTIMA.  
  
When running [ESTIMA](<estima.md>) to create these two files, the following options must have been specified:  

  1. **Key Field**   
This restricts the number of samples per key field, where the key field will usually be BHID. Although this option must have been selected when running ESTIMA, it need not actually affect the results. If you do not want to restrict the number of samples per key field, then select the maximum number to be greater than or equal to the maximum number of samples in the search volume. This will ensure that it has no effect. The reason for using the option is so that the key field (BHID) is copied to the sample output file.

  2. **Sample Output File**   
A sample output file must be created.

The input to **BHCOUNT** includes the following:

  1. Key Field (**KEY**)  
The same key field must be specified as for the corresponding ESTIMA run.

  2. Grade Value (**VALUE**)  
If multiple values of the VALUE_OU field were specified in the Estimation Parameter File for the ESTIMA run then there will be multiple values in the FIELD field of the SAMPIN file. However BHCOUNT can only process one value, which can be selected using the VALUE field. Note that this usage is different from normal field prompts as the input is a field value, not a field name. Therefore it cannot be selected from a dropdown list but must be entered manually. If the FIELD field in the SAMPIN file only contains one value then it does not have to be entered as it will be selected automatically. Note also that the field value is restricted to 24 characters. 

  3. Parent Parameter (**PARENT**)   
The same value of parameter PARENT that was used for the ESTIMA run must also be specified for the BHCOUNT run. Failure to do this will lead to incorrect values in the MODELOUT file. 

The output model from BHCOUNT will be the same as the input model, but with the extra field N-BHID.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
MODELIN |  Input model file. This file is the output MODEL file from ESTIMA |  Input |  Yes |  Block Model  
SAMPIN |  Input sample file. This file is the SAMPOUT file from ESTIMA. The run of ESTIMA which created the file must have used the following options: - the key field option was selected. - only one output grade field was created. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODELOUT |  Output |  Yes |  Block Model |  Output model file. This is the same as the input model, but with the extra field N-BHID.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY |  Name of the field containing the drillhole identification code. This is the field specified as the KEY field when running ESTIMA. This will usually be BHID, which is the default. |  SAMPIN |  Yes |  Any |  BHID  
  
## Example
    
    
    !BHCOUNT  &MODELIN(gradmod1), &SAMPIN(sampout),   
  
---  
      
    
     &MODELOUT(gradmod2), *KEY(BHID), VALUE(AU), @PARENT=1BHCOUNT - Calculate the number of BHIDs used to estimate each model   
      
    
     cell.  
      
    
    ... input validation.  
      
    
    - Key field BHID  
      
    
    - Value field AU  
      
    
    - Parent cell estimation (PARENT=1)  
      
    
    - Input model file GRADMOD1  
      
    
    - Input sample file SAMPOUT       
      
    
    - Output model file GRADMOD2  
      
    
    - The following zone field(s) have been identified:  
      
    
    ~ ROCKTYPE  
      
    
    ... processing data (this may take some time!)  
      
    
    ... sorting sample file.  
      
    
    ... counting by key field BHID.  
      
    
    ... sorting model file.  
      
    
    ... joining counted sample data to model.  
      
    
    ... resorting model file.  
      
    
    ... deleting temporary work files.  
      
    
    ... output model file GRADMOD2  
      
    
    contains 6250 records.  
      
    
    ... process complete.  
  
Related topics and activities

  * [ESTIMA Process](<estima.md>)

  * [ESTIMATE Process](<estimate.md>)