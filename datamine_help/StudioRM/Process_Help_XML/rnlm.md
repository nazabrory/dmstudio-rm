# RNLM Process  
  
To access this process:

  * **Sample Analysis** ribbon **> > Statistics >> Geochemical Processes >> R Mode Non Linear Mapping**.

  * Enter "RNLM" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **RNLM** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#RNLM>).

## Process Overview

R - mode non linear mapping groups together elements using the angular distances calculated from the Pearsson correlation coefficient matrix.

Note the difference with [Q mode non linear mapping](<qnlm.md>) which clusters samples on the basis of composition.

A two dimensional view of the element clusters, or the scores **NLM-X** versus **NLM-Y** , is calculated to represent them as they would appear in multi-dimensional space on the basis of element similarity between pairs of samples. All input data is standardized prior to the calculation of the correlation matrix and the linear mapping output scores are normalized prior to plotting.

R - mode non linear mapping, when compared with R - mode factor analysis, is more sophisticated and does not distort or sub-divide the element or parameter clusters. Non linear mapping will give more separable clusters than other hierarchical techniques such as R - mode cluster analysis.

**Note** : There is a restriction of 2000 samples.

### File Handling

The input file &(**IN**) must have a separate identifier field (* **SAMPID**). The output file &(**SCORES**) contains three parameters, **FIELD** the field identifier, **NLM-X** and **NLM-Y** the output scores for plotting the multi-dimensional inter-element distances as a two dimensional flat plane. Results can be displayed using **[QUIG](<quig.md>)** , **[PLOTDA](<plotda.md>)** or [PLOTAN](<plotan.md>).

### Iteration Procedure

In order to present a two dimensional view of multi-dimensional space with minimum distortion of the sample clusters, the calculated mapping error has to be minimized by an iterative method (steepest descent). This is controlled by the @**CONVLIM** parameter, that is the minimum difference allowed in the mapping error between iterations, @**MAXIT** , the maximum number of iterations permitted and the @**MAGIC** parameter which specifies the stepping function used for each iteration. If the stepping function @**MAGIC** is decreased, the number of iterations is increased with an obvious time penalty on the length of the calculation. The value used must be taken into account when there are a large number of samples. However the results can be more stable.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
SCORES |  Output |  No |  Undefined |  Optional output file for principal component scores.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
SAMPID |  Field containing sample identification |  IN |  Yes |  Any |  Undefined  
F1-10 |  Fields to be used. No fields specified means all. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CONVLIM |  Convergence limit. |  No |  0.0001 |  Undefined |  Undefined  
MAGIC |  Convergence [magic] factor. |  No |  0.35 |  Undefined |  Undefined  
MAXIT |  Maximum number of iterations . |  No |  100 |  Undefined |  Undefined  
PRINT |  |  Option |  Description  
---|---  
(0) |  Print configuration results to screen.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !RNLM    &IN(AEG2),@SCORES(RSCORES),@SAMPID='ID',  
  
---  
      
    
    @CONVLIM=0.0001,@MAGIC=0.35,@PRINT=1  
  
Related topics and activities

  * [QNLM Process](<qnlm.md>)

  * [QUIG Process](<quig.md>)

  * [PLOTDA Process](<plotda.md>)

  * [PLOTAN Process](<plotan.md>)