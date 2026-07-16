# CORREL Process  
  
To access this process:

  * **Sample Analysis** ribbon **> > Statistics >> Statistics Processes >> Bivariate Statistics**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CORREL** and click **Run**.
  * Enter "CORREL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CORREL>)

## Process Overview

Calculates bivariate statistics on pairs of numeric fields in a file. All results are output as the bottom left-hand triangle of a full two-dimensional matrix. Output is written to the display, and includes the following:-

  * a summary of the mean and variance of each numeric field.

  * sample number matrix.

  * correlation matrix.

  * covariance matrix.

  * F ratio matrix.

  * paired t test matrix.

The sample number matrix contains the number of pairs of samples for each pair of fields. This shows when one or other of the fields has absent data values. If none of the records contain missing data then all the elements of the matrix will contain the same value.

The mean and variance of each field shown in the summary statistics are calculated using all the available data, whereas the matrices are calculated using only data where neither sample is missing. Thus if there is missing data it is not possible for example to calculate the correlation coefficient from the covariance and variances. Bivariate statistics are calculated by default for all pairs of numeric fields. Thus if for example the data file contains sample co-ordinates statistics will be calculated for the X and Y co-ordinates.

Also see this online [Knowledge Base article](<https://datamine.freshdesk.com/en/support/solutions/articles/19000084719-correl-calculation-of-bivariate-statistics-for-numerical-fields>) (Internet connection required).

## Statistics

### Correlation Coefficient

The correlation coefficient is a number between -1 and 1 which measures the degree to which two variables are linearly related. If there is perfect linear relationship with positive slope between the two variables, we have a correlation coefficient of 1; if there is positive correlation, whenever one variable has a high (low) value, so does the other. Further details are available from:

<http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient>

<http://www.stats.gla.ac.uk/steps/glossary/paired_data.html>

### Covariance

Covariance provides a measure of the strength of the correlation between two or more sets of random variables. For example between Au and Ag in a set of samples. Further details are available from:

<http://mathworld.wolfram.com/Covariance.html>

### F Ratio Test

The F Ratio test determines whether the variances of two sets of measured values with different numbers of samples are significantly different from each other. For example to compare the variance of Au grades for samples in rock types A and B . Further details are available from:

<http://www.acastat.com/Handbook/14.html>

<http://www.itl.nist.gov/div898/handbook/eda/section3/eda3673.htm>

### Paired t Test

The paired t test determines whether two paired sets of measured values are significantly different from each other. For example if a set of samples are analysed by two laboratories and you want to test whether there is a difference between them. Further details are available from:

<http://www.itl.nist.gov/div898/handbook/prc/section3/prc311.htm>

<http://udel.edu/~mcdonald/statpaired.html>

<http://mathworld.wolfram.com/Pairedt-Test.html>

### Pooled t test

The pooled t test determines whether two sets of measured values with different numbers of samples are significantly different from each other. For example to compare the mean Au grade for samples in rock types A and B . Further details are available from:

<http://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm>

<http://www.stat.yale.edu/Courses/1997-98/101/meancomp.htm>

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. |  Input |  Yes |  Undefined  
FIELDLST |  File to supply selected fields. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
F1 |  First field to be correlated. No fields specified means all. |  IN |  No |  Numeric |  Undefined  
F2 |  Second field to be correlated. |  IN |  No |  Numeric |  Undefined  
F3 |  Third field to be correlated. |  IN |  No |  Numeric |  Undefined  
F4 |  Fourth field to be correlated. |  IN |  No |  Numeric |  Undefined  
F5 |  Fifth field to be correlated. |  IN |  No |  Numeric |  Undefined  
F6 |  Sixth field to be correlated. |  IN |  No |  Numeric |  Undefined  
F7 |  Seventh field to be correlated. |  IN |  No |  Numeric |  Undefined  
F8 |  Eighth field to be correlated. |  IN |  No |  Numeric |  Undefined  
F9 |  Ninth field to be correlated. |  IN |  No |  Numeric |  Undefined  
F10 |  Tenth field to be correlated. |  IN |  No |  Numeric |  Undefined  
FIELDNAM |  Field in FIELDLST to identify selected fields. |  FIELDLST |  No |  Character |  Undefined  
  
## Example
    
    
    !CORREL    &IN(SAMPLES)    
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
ERR 122 <<< ( fileno) IN CORREL |  No numeric fields in file, or fields specified were not numeric. Fatal; the process is terminated.  
ERR 121 <<< ( fileno) IN CORREL |  File read error. Fatal; the process is terminated.