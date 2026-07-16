# APTOTRUE Process  
  
To access this process:

  * **Model** ribbon **> > Dynamic Anisotropy >> Dips**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **APTOTRUE** and click **Run**.
  * Enter "APTOTRUE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#APTOTRUE>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

**APTOTRUE** is designed to be used in conjunction with processes [ANISOANG](<anisoang.md>) and [ESTIMA](<estima.md>) when the apparent dip angle and the true dip direction angle have been interpolated into a model and the true dip angle is required in order to use the Dynamic Anisotropy option to estimate grades. In fact the input file can be any type of file, so long as it contains the apparent dip and true dip direction fields.

The process takes as input the file IN containing fields **APDIP** (apparent dip) and **TRDIPDIR** (true dip direction) and parameter **APDIPDIR** (apparent dip direction) and calculates the **TRDIP** (true dip) field which is written to file **OUT**. Parameter **APDIPDIR** is the azimuth of the sections corresponding to the apparent dip field. 

## Input Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
IN |  Input |  Yes |  Undefined |  Input file containing the true dip direction and the apparent dip angle fields.  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file containing all the fields in the input file plus the true dip angle.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
APDIP |  Apparent dip angle. If not specified then APDIP is assumed. |  IN |  No |  Numeric |  APDIP  
TRDIPDIR |  True dip direction angle. If not specified then TRDIPDIR is assumed. |  IN |  No |  Numeric |  TRDIPDIR  
TRDIP |  True dip angle. If not specified then TRDIP will be created. |  OUT |  No |  Numeric |  TRDIP  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
APDIPDIR |  Apparent dip direction angle in degrees. This is the azimuth of the sections on which the original string data was digitised. |  Yes |  0 |  0,360 |  Undefined  
  
## Example
    
    
    !APTOTRUE   
  
---  
      
    
     &IN(APPMOD),&OUT(TRUEMOD),@APDIPDIR=180  
      
    
    APTOTRUE  
      
    
    ... calculating true dip angle  
      
    
    Calculation of true dip angle complete  
      
    
    - output file TRUEMOD created with 3313 records  
      
    
    - mean true dip angle = 17.97  
      
    
    - number of absent true dip values = 0  
  
Related Topics and Activities

  * [ANISOANG Process](<anisoang.md>)

  * [ESTIMA Process](<estima.md>)

  * [Dip and Dip Direction Data](<../STUDIO_RM/Dynamic%20Anisotropy%20-%20Dip%20and%20Dip%20Direction.md>)

  * [Calculating True Dip Angles with APTOTRUE](<../STUDIO_RM/Dynamic%20Anisotropy%20-%20True%20Dip%20Angles.md>)

  * [Dynamic Anisotropy with COKRIG](<../STUDIO_RM/Dynamic%20Anisotropy-COKRIG-Guidelines.md>)

  * [Dynamic Anisotropy with ESTIMA](<../STUDIO_RM/Dynamic%20Anisotropy%20-%20Introduction.md>)