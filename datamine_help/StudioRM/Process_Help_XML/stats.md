# STATS Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics >> Statistics Processes >> Summary Statistics**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **STATS** and click **Run**.
  * Enter "STATS" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#STATS>).

## Process Overview

Calculate general summary parametric statistics on numeric fields in a file.

Individual fields for statistics may be selected using either the ***F1, *F2** , etc fields or may be specified in the &**FIELDLST** file. If no fields are selected then statistics will be calculated for all fields.

Ten optional keyfields are provided. If no keyfields are specified then a single set of statistics will be calculated for all data. If keyfields are specified and parameter **KEYSORT** =1 or the input file is already sorted by keyfield then statistics will be calculated for each unique combination of key values. If keyfields are specified and parameter **KEYSORT** =0 and the input file is not sorted by keyfield then data will be read from the input file until the value of one of the keyfields changes and the statistics will then be calculated for that data subset.

Note: A limit of 256 fields is imposed. If more than 256 fields exist in &IN, the process will not complete.

An optional weighting field (* **WEIGHT**) is available to weight the sample data. For example in a desurveyed drillhole file the **LENGTH** field could be used as the weighting field to give length weighted grades.

Note: When calculating **MAD** and percentile statistics, **WEIGHT** is ignored.

The variance and other moments are calculated using the large sample method (for the variance a divisor of N is used, where N is the number of samples).

The following statistics are calculated for each numeric variable :-

  * total number of records in the file that meet retrieval criteria, if specified
  * number of samples (excluding absent data).
  * number of absent data values.
  * minimum, maximum, range and mid-range.
  * total and mean.
  * variance, standard deviation and standard error.
  * skewness and kurtosis.
  * geometric mean.
  * Sum, mean and variance of natural logs.
  * log estimate of mean.
  * coefficient of variation in percent.
  * number of records equal to zero.
  * number of negative value.

These results are displayed in the Command window and can also be saved to an optional &OUT file..

If the **PCNTILES** parameter is set to 1 then the 5, 10, 20, 25, 30, 40, 50, 60, 75, 80, 90 and 95 percentiles and the Median Absolute Deviation are also calculated. Processing will take longer. If this option is selected it is helpful to specify only the fields for which you wish to calculate the statistics. The Weight field is not used when calculating percentiles.

By default, statistics are calculated for all numeric variables. For example; in a typical drillhole data file containing sample co-ordinates, statistics will be calculated for both the values and the co-ordinates. The first bin in the histogram plot contains all values up to MINIMUM. The last bin contains all values above the top value. The log statistics are based on all sample values greater than, but not equal to, the system trace value.

Values of skewness and kurtosis calculated are interpreted as:

SKEWNESS |  = 0. No distortion (Gaussian).  
---|---  
|  > 0\. Positive skew (to the right).  
|  < 0\. Negative skew (to the left).  
KURTOSIS |  = 0. Mesokurtic (Gaussian).  
|  > 0\. Leptokurtic (peaked).  
|  < 0\. Platikurtic (flat).  
  
### Missing Values

When the **STATS** process is run with retrieval criteria, data that is excluded by those criteria will not be reported. This is a change from previous versions which classified excluded data as "Missing Values".

The following fields are also output:

  * **NSAMPLES** The number of samples in the chosen numeric (F1 etc) fields that are non-absent and used to calculate statistics.
  * **NMISVALS** The number of missing records in the chosen numeric (F1 etc) fields. Samples are classified as missing if they have an absent value.
  * **NUMTRACE** The number of samples in the chosen numeric (F1 etc) fields that are equal to the TRACE value
  * **EQUAL0** The number of records in the chosen numeric (F1 etc) fields that contain values that = 0.
  * **NEGATIVE** The number of records in the chosen numeric (F1 etc) fields that contain negative values.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Table  
FIELDLST |  File to supply selected fields. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  No |  Table |  Output file. This will contain the fields:

  * FIELD: field for which statistics have been calculated
  * NRECORDS: total number of records in the input data (including those excluded by retrieval criteria)
  * NSAMPLES: number of records (samples) used to calculate the statistics
  * NMISVALS: number of missing values - either absent or excluded by retrieval criteria
  * NUMTRACE: number of samples equal to TRACE
  * MINIMUM: minimum sample value
  * MAXIMUM: maximum sample value
  * RANGE: range of the sample values
  * TOTAL: sum of the sample values
  * MEAN: mean of sample values
  * VARIANCE: variance of the sample values (Absent if fewer than two sample values)
  * STANDDEV: standard deviation of the input sample values
  * STANDERR: standard error of the input sample values
  * SKEWNESS: skewness of the sample values
  * KURTOSIS: kurtosis of the sample values
  * GEOMEAN: geometric mean of the input sample values
  * SUMLOG: sum of the sample log values
  * MEANLOG: mean of the sample log values
  * LOGVAR: variance of the sample log values (If more than one sample value)
  * LOGESTM: log estimate of the mean
  * COVARTN%: coefficient of variation in percent
  * **MIDRANGE** : value mid-way between the minimum and maximum values
  * EQUAL0: number of samples with a value of zero
  * NEGATIVE: number of negative samples
  * **WGTFIELD** : weight field used
  * DATAFILE: name of the input data file

If keyfields have been specified then they will also be included. There will be one record for each numeric field for every combination of keyfields.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1-20 |  Fields for statistics. If no fields are specified then all fields will be used. |  IN |  No |  Numeric |  Undefined  
FIELDNAM |  Field in FIELDLST to identify selected fields. |  FIELDLST |  No |  Character |  Undefined  
KEY1-10 |  Key fields 1 for statistics. |  IN |  No |  Any |  Undefined  
WEIGHT |  Weighting field. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
KEYSORT |  Set to 1 to automatically sort the data by key field. Only relevant if any key fields have been defined. =0 : Do not automatically sort by key fields. Use the record order of the input file to determine changes in key field values. =1 : Automatically sort the input data by key fields. |  No |  No |  Numeric |  Undefined  
KEYTOL |  The tolerance used to test whether numeric key fields are equal. All key values are rounded to an integer multiple of this value. If set to zero then rounding will not be used. |  No |  0.00001 |  0,+ |  Undefined  
PCNTILES |  Set to 1 to calculate percentiles. When calculating percentiles the process will take longer to run. If this option is selected it is useful to specify only the fields for which you wish to calculate the statistics. If this option is selected the Median Absolute Deviation (MAD) value is also calculated. =0 : Do not calculate percentiles. Do not calculate the Median Absolute Deviation. =1 : Calculate the 5, 10, 20, 25, 30, 40, 50, 60, 75, 80, 90 and 95 percentiles and the Median Absolute Deviation. |  No |  0 |  0,1 |  0,1  
SORTOUT |  Set to 1 to sort the output file by **FIELD** when key fields are being used. Sorting by **FIELD** makes it easier to compare values of variables across key fields when viewing the output file in the table editor. =0 : Do not sort the output file. =1 : Sort the output file by **FIELD**. |  No |  1 |  0,1 |  0,1  
PRINT |  Print flag. Default (2). 0: minimum output.  1: minimum output plus key field progress list.  2: full output including stats for each key field group. |  No |  2 |  0-2 |  0,1,2  
  
* * *

## Example
    
    
    !STATS    &IN(ASSAYS), &OUT(DHSTATS), *F1(AU), *F2(AG),   
  
---  
      
    
    *F3(CU),*WEIGHT(LENGTH)   
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 121 <<< ( fileno) IN STATS |  File read error. Fatal; the process is exited. Check the values of the fields in the specified &IN file.  
>>> ERR 122 <<< ( fileno) IN STATS |  No numeric fields in file, or fields specified were not numeric. Fatal; the process is exited. In the &IN file, check that the specified *Fn fields are numeric; check that the file contains numeric fields.  
  
Related topics and activities

  * [STATNP Process](<statnp.md>)

  * [STATCOM Process](<statcom.md>)