# LUNICOND Process  
  
To access this process:

  * Enter "LUNICOND" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **LUNICOND** and click **Run**.

  * Run as part of the [Uniform Conditioning Wizard](<../Uniform_Conditioning/UniformConditioning_Introduction.md>)

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_L.md#LUNICOND>).

## Process Overview

The goal of Localized Uniform Conditioning is to provide a more 'intuitive' presentation of uniform conditioning result by assigning a unit-level mean average grade based on calculations of the tonnages and grades above each cut-off grade, dispersed within the panel according to their rank. This process is implemented interactively via the Uniform Conditioning Wizard.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
UCMODEL |  A model file containing the conditioned panels. This model is the output model from the process **UNIFCOND** , containing the uniform conditioned distribution (metal, grade and proportion at each cut-off). |  Input |  Yes |  Model  
SMUMODEL |  An SMU model, containing a linear estimate of a grade, for the localization ranking of the uniform conditioned panel distribution. |  Input |  No |  Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUTMODEL |  Output |  Yes |  Undefined |  The output locally-conditioned model.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KRIGING |  The field in the input SMU model containing the linear estimated values upon which the UC distribution will be ranked. |  IN |  Yes |  Alphanumeric |  Undefined  
OUTFIELD |  The field in the output locally-conditioned model (**OUTMODEL**) to contain the values resulting from localized uniform conditioning. |  IN |  Yes |  Alphanumeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CUTMIN |  The minimum cutoff grade to be considered during Uniform Conditioning. |  No |  0 |  |   
CUTINT |  The size of each grade cutoff interval | No | 10 |  |   
CUTNUM |  The number of grade cutoff intervals to considered during Uniform Conditioning. | No | 10 |  |   
  
Related topics and activities

  * [Uniform Conditioning Wizard](<../Uniform_Conditioning/UniformConditioning_Introduction.md>)

  * [UNIFCOND Process](<unifcond.md>)

  * [GAUSANAM Process](<gausanam.md>)