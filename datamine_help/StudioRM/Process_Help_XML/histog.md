# HISTOG Process

To access this process:

  * **Sample Analysis** ribbon **> > Charts >> Histogram File**.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **HISTOG** and click **Run**.

  * Enter "HISTOG" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_H.md#HISTOG>).

## Process Overview

Generates a frequency histogram and a cumulative frequency histogram for any numeric field. The histogram file itself can be listed, showing the results of classifying the data into bins.

Note: Any sample value below @**MINIMUM** will be put into the bottom bin. Any sample value above @**MINIMUM** \+ @**BINSIZE** * @**NUMBINS** will be put into the top bin.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file. This will contain one record for each histogram bin and nine fields LOWER, MIDDLE, UPPER, FREQENCY, CUMFREQ., AVIVAL, FREQ-%, CUMF-%, TOTVAL.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Field to be histogrammed (numeric). |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
BINSIZE |  Bin width. |  Yes |  Undefined |  Undefined |  Undefined  
MINIMUM |  Lower bound of first bin. |  Yes |  Undefined |  Undefined |  Undefined  
NUMBINS |  Number of bins (max 50). |  Yes |  Undefined |  1,50 |  Undefined  
PRINT |  >=1 display all records, all samples outside bins, the output file DD (0). |  No |  0 |  0,1 |  0,1  
  
* * *

## Example
    
    
    !HISTOG &IN(SAMPLES),&OUT(HISTFILE),@BINSIZE=0.5, @MINIMUM=0.5,@NUMBINS=25  
  
---  
  
This creates the histogram file **HISTFILE**. A frequency plot may then be generated and displayed in the following way:
    
    
    !PLOTHI &IN(HISTFILE),&PROTO(PLOTPROT),&PLOT(HIST.P),          
  
---  
      
    
    *X1(LOWER),*X2(UPPER),*Y(FREQENCY),         
      
    
    @XMIN=0.5,@XMAX=13,@YMIN=0,  
      
    
    @YMAX=100!DISPLA &IN(HIST.P)  
  
Note that the **PLOTHI** call assumes that the maximum frequency in any bin is 100. This may be checked using **STATS1** on **FREQENCY** , if required. 

**Tip** : The plot would also be improved with a frame (**[PLOTFR](<plotfr.md>)**), not shown here.

## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 130 <<< ( fileno) IN HISTOG |  Field *VALUE is not numeric. fileno is the internal file number of the &IN file. Fatal; the process is exited.  
>>> ERR 131 <<< ( 0) IN HISTOG |  An unsuitable parameter value has been specified. For example a negative bin width @BINSIZE or 0 for @NUMBINS. Fatal; the process is exited.  
>>> WARNING - nnnn BINS REQUESTED  
>>> RESET TO MAXIMUM OF 500 |  An illegal value of @NUMBINS has been entered. The value is reset to the maximum of 500.  
  
Related topics and activities

  * [HISFIT Process](<hisfit.md>)