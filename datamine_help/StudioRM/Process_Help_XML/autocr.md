# AUTOCR Process

To access this process:

  * Sample Analysis ribbon **> > Geochemical Processes >> Auto Correlation Analysis**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **AUTOCR** and click **Run**.
  * Enter "AUTOCR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_A.md#AUTOCR>).

## Process Overview

Auto-correlation analysis is used to quantify and define anomalous thresholds and halo size on regularly grided soil sample lines. **AUTOCR** can also be used to measure dispersion limits in stream sediments, as long as fixed distances are used for sampling.

The process calculates the auto correlation function **R-L** of a single field against sample **DISTANCE** or **LAG** (see Figure 1). By default, lag distance is used to calculate the auto correlation function. If sample distance, or a multiple of sample distance is required, use the parameter **SAMPDIST**.

Anomalous samples related to lag or sample distance (**LAG** or **DISTANCE**) are identified by strong and well defined peaks of **R-L** , the covariance between neighboring samples. Dispersion limits from mineralized stream sediments are defined by breaks in slope along the stream sediment train as defined by **LAG-L**.

**Note** : There is a restriction of 4000 samples for a given line or dispersion train. For the analysis to be valid the data points must be equi-distant from each other. All fields containing the same value should be removed prior to the analysis. A plot macro should be written to display the results.

## File Handling

The input file (&IN) must contain a sample identifier (* **SAMPID**) which is declared on input. There is an obligatory output file (&OUT) of the results containing the fields **LAG-L** , **DISTANCE** , **R-L** and the significance levels for each observation which can be viewed by the plotting processes, e.g. [PLOTDA](<plotda.md>) and [PLOTAN](<plotan.md>).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. Must contain sample identity field. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file includes LAG-L, DISTANCE. R-L the auto correlation function and SIGNIC the significance of the auto correlation function for use in graphical processes.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
SAMPID |  Compulsory sample identifier field. |  IN |  Yes |  Undefined |  Undefined  
F1 |  First variable for evaluation. If no variables are selected all variables will be processed. |  IN |  No |  Numeric |  Undefined  
F2 |  Second variable for evaluation. |  IN |  No |  Numeric |  Undefined  
F3 |  Third variable for evaluation. |  IN |  No |  Numeric |  Undefined  
F4 |  Fourth variable for evaluation. |  IN |  No |  Numeric |  Undefined  
F5 |  Fifth variable for evaluation. |  IN |  No |  Numeric |  Undefined  
F6 |  Six variable for evaluation. |  IN |  No |  Numeric |  Undefined  
F7 |  Seventh variable for evaluation. |  IN |  No |  Numeric |  Undefined  
F8 |  Eighth variable for evaluation. |  IN |  No |  Numeric |  Undefined  
F9 |  Ninth variable for evaluation. |  IN |  No |  Numeric |  Undefined  
F10 |  Tenth variable for evaluation. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SAMPDIST |  |  Option |  Description  
---|---  
(0) |  Distance between sample points to calculate the auto-correlation function. If no distance is specified the sample distance is lag distance.  
No |  0 |  Undefined |  Undefined  
PRINT |  >0 Display results on the screen (0). |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !AUTOCR &IN(L10),&OUT(L10ACR),@SAMPID='ID',*F1(BA),*F2(SR),@SAMPDIST=20  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
*** Warning *** nnnnn Samples exceed the maximum of 4000. |  The first 4000 will be processed.  
*** Error *** No numeric fields on file (filename). >>> ERR 122 <<< ( fileno.) IN AUTOCR |   
*** Error *** SAMPID field (fieldname) is not in input file. *** Error *** in reading data from file (filename). >>> ERR 200 <<< ( fileno.) IN AUTOCR |   
*** Error *** Compulsory file, field or parameter missing. >>> ERR 120 <<< ( fileno.) IN AUTOCR |