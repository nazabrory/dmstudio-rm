# NSMODBAK Process

To access this process:

  * Enter "NSMODBAK" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **NSMODBAK** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_N.md#NSMODBAK>).

## Process Overview

The process back transforms one or more variogram models that have been fitted to experimental variogram created from normal-score transformed samples. See [NSCORE Process](<nscore.md>).

The &**IN** file is a variogram model file containing at least one model. If a **TRANS** field exists, only models with a value of 1 will be converted. &**SAMPLES** is also required, which is the output from the variogram creation process and will contain grade fields matching those found in the ***GRADE** field of the input &**IN** file.

The output is a model variogram file containing back-transformed variogram models.

This process is triggered during **Advanced Estimation** , specifically from the [Save Models](<../STUDIO_RM/Multivariate_FitModels_SaveModels.md>) tab.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model variogram file. This should contain a **GRADE** field containing the name of the grade it relates to. If this contains the **TRANS** field, it will only convert variograms where **TRANS** =1. |  Input |  Yes |  Variogram Model  
SAMPLES |  Input sample data file. This should be the file which was transformed as part of the original variogram creation. It should contain grade fields matching the names in **GRADE** in the input model file IN |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Variogram Model |  Output model variogram file which will contain the back-transformed variogram models. Back-transformed variograms will have **TRANS** =-1  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X/Y/ZPT |  Coordinate fields in the input **SAMPLES** file |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Type |  Values  
---|---|---|---|---|---  
VSETNUM |  Variogram model set number to be assigned to &**OUT** file. |  No |  1 |  Undefined |  Undefined  
  
## Example
    
    
    !NSMODBAK &IN(vmodel_4),&OUT(vmodel_4_BT),&SAMPLES(isaacs),  
  
---  
      
    
    *XPT(XPT),*YPT(YPT),*ZPT(ZPT),@VSETNUM=2.0  
  
Related topics and activities

  * [NSCORE Process](<nscore.md>)

  * [NSTRANS Process](<nstrans.md>)