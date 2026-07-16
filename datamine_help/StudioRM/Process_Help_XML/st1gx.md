# ST1GX Process  
  
To access this process:

  * **Sample Analysis** ribbon **> > Statistics >> Statistics Processes >> Sturgess Rule Statistics**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ST1GX** and click **Run**.
  * Enter "ST1GX" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#ST1GX>).

## Process Overview

Calculates general summary statistics for a single field, in log or non-log mode with or without class selection using Sturgess' Rule.

The calculated statistics include:-

  * total number of records in the file.
  * number of values used for statistical analysis.
  * number of missing values.
  * minimum, maximum, range, total and mean.
  * variance, standard deviation and standard error.
  * skewness and kurtosis.
  * coefficient of variation.
  * mean plus 2 and mean plus 4 standard deviations.
  * median.
  * mode.

These results are displayed in the Output control bar, and can be copied to the printer or printfile. A list of **BIN** sizes with **BIN** counts and percentage frequency for each class, cumulative frequency, class interval and number of **BINS** are also calculated. In addition, printer plots on a normal probability scale are calculated and can be sent to the printer or printfile.

The first bin in the histogram plot contains all values up to **MINIMUM**. The last bin contains all values above the top value. If **LOGMODE** is set to 1, antilogs are automatically calculated.

Values of skewness and kurtosis calculated are interpreted as:

**SKEWNESS** |  = 0. No distortion (Gaussian).  
---|---  
|  > 0\. Positive skew (to the right).  
|  < 0\. Negative skew (to the left).  
**KURTOSIS** |  = 0. Mesokurtic (Gaussian).  
|  > 0\. Leptokurtic (peaked).  
|  < 0\. Platikurtic (flat).  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Field for statistics. |  IN |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
BINSIZE |  Bin width for histogram [computed]. |  No |  Undefined |  Undefined |  Undefined  
MINIMUM |  Minimum bin limit [computed]. |  No |  Undefined |  Undefined |  Undefined  
STURGESS |  |  Option |  Description  
---|---  
1 |  class interval [bin width] and minimum class value [bin limit] are calculated according to the following equation: Class interval = 1 + 3.3 log N [Sturgess Rule] and values within each bin are placed at the mid-point of each class (0).  
No |  0 |  0,1 |  0,1  
LOGMODE |  |  Option |  Description  
---|---  
1 |  log transformation [base 10] is calculated (0).  
No |  0 |  0,1 |  0,1  
PERC |  |  Option |  Description  
---|---  
0 |  numeric bin count for histogram; >0 percentage bin count for histogram (0).  
No |  0 |  Undefined |  Undefined  
  
## Example
    
    
    !ST1GX    &IN(SEDREG),*VALUE(CU),@LOGMODE=1,@STURGESS=1  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 121 <<< ( fileno) IN STATS1 |  File read error. Fatal; the process is exited. Check the range of values of the * **VALUE** field in the &**IN** file.  
NO MODES DETECTED - CHECK CLASS INTERVAL |  Error computing statistics (e.g. empty file). Fatal; the process is exited. Check the range of values of the * **VALUE** field in the &**IN** file.