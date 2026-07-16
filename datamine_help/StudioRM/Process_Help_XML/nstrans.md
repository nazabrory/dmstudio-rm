# NSTRANS Process

To access this process:

  * Enter "NSTRANS" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **NSTRANS** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_N.md#NSTRANS>).

## Process Overview

This process transforms a set of data to a normal distribution.

This process is run as part of Advanced Estimation if the Transform | Normal Score option is selected on the [Create Variograms](<../STUDIO_RM/Multivariate_Create_Variograms.md>) panel.

The input to this process is a sample data file containing at least one grade field to be transformed. It may also include a declustering weight field (*DCWGT). The file does not need XYZ coordinate data in order to do the transform. However coordinates will be required if variograms are to be calculated for the transformed data.

The process creates an output file containing transformed points. This will contain the same data as the input file, but with an extra transformed data field (*NSGRADE).

You can also restrict the scope of transformation by setting a minimum (@MINGRADE) and/or maximum (@MAXGRADE) grade value to transform.

**Note** : This process supports **[retrieval criteria](<../COMMON/Retrieval_Criteria_Overview.md>)**.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input sample data file. This must include the grade field **GRADE** and may also include the declustering weight field **DCWGT** . |  Input |  Yes |  Samples file  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
Out |  Output file containing transformed points.This contains the same data as the **IN** file, but with the added transformed data field **NSGRADE**. |  Output |  Yes |  Samples file  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
GRADE |  Field in the input sample file **IN** defining the grade to be transformed. |  IN |  Yes |  Numeric |  Undefined  
DCWGT |  Optional declustering weights field in the **IN** file. |  IN |  No |  Numeric |  Undefined  
NSGRADE |  Field in the output file **OUT** containing the transformed grade.(This may be the same as **GRADE** , in which case it overwrites the original value) |  - |  No |  Alphanumeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MINGRADE |  Minimum **GRADE** value input from the IN sample file. |  No |  0 |  Undefined |  Undefined  
MAXGRADE |  Maximum **GRADE** value input from the IN sample file. |  No |  Undefined |  Undefined |  Undefined  
  
## Example
    
    
    !NSTRANS &IN(dcisaacs),&OUT(nscore1),  
  
---  
      
    
    *GRADE(V), *NSGRADE(TRANS), @MINGRADE=0.0,@MAXGRADE=1700.0  
  
Related topics and activities

  * [NSCORE Process](<nscore.md>)

  * [NSMODBAK Process](<nsmodbak.md>)