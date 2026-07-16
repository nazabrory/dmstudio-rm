# PPQQPLOT Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics Processes >> PP and QQ Plots**.

  * Enter "PPQQPLOT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PPQQPLOT** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PPQQPLOT>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

This process calculates and displays PP (probability-probability) and QQ (quantile-quantile) plots. These are graphical techniques for determining if two data sets come from populations with a common distribution.

#### PP Plots

The PP plot is a plot of the cumulative probability of the first data set against the cumulative probability of the second data set for a series of cutoff grades. If the two sets come from a population with the same distribution, the points should fall approximately along the 45 degree reference line.

In order to calculate the cumulative probability for each file, samples are divided into bins as defined by parameter BINSIZE.

#### QQ Plots

The QQ plot is a plot of the quantiles of the first data set against the quantiles of the second data set, where a quantile is defined as the fraction (or percent) of points below the given value. For example the 0.2 (or 20%) quantile is the point at which 20% percent of the data fall below and 80% fall above that value. If the two sets come from a population with the same distribution, the points should fall approximately along the 45 degree reference line.

**Note** : The q-q plot is similar to a probability plot. For a probability plot, the quantiles for one of the data samples are replaced with the quantiles of a theoretical distribution. Further information on QQ plots is available from the Engineering Statistics Handbook (<http://www.itl.nist.gov/div898/handbook/eda/section3/qqplot.htm>).

If there are 100 or more samples in each of the IN1 and IN2 files then the 1%, 2%, 3%, ..., 100% percentiles are calculated. If there are less than 100 samples in either file then quantiles are calculated in multiples of 100/N where N is number of samples in the smaller file. 

#### Key Field

If a **KEY** field is specified then the field must exist in the **IN1** file. The same **KEY** field may also exist in the **IN2** file. A PP or QQ line or set of symbols will be created for each unique value of the **KEY** field.

If the **KEY** field only exists in the **IN1** file then all the samples from the **IN2** file will be matched with the samples from the **IN1** file for every **KEY** field value. This is particularly useful if you are comparing multiple realisations from a conditional simulation run with the original sample data as shown in example 3 below.

#### Output Files

The **PPOUT** and **QQOUT** files contain the data from which the plot files are constructed. You then have three options for creating the plots:

  * draft quality plots can be created by specifying the **PPPLOT** and **QQPLOT** output plot files, which are created by **PPQQPLOT** using the graphics processes. The plot size, scaling, annotation etc are all fixed.

  * the **PPOUT** and **QQOUT** files can be used as input to the **CHART** process. Although this is still only draft quality, you can specify plot size, scaling, colour, text size, axis annotation, title, legend, etc.

  * you can export the **PPOUT** and **QQOUT** files to Excel or any charting package.

The PPOUT file includes the following fields:

Field |  Description  
---|---  
LOWER |  Lower bound of grade range, calculated using parameter **BINSIZE**.  
UPPER |  Upper bound of grade range  
N1 |  If the **WEIGHT1** field has not been selected then **N1** is the number of samples in the bin (between **LOWER** and **UPPER**) for file **IN1**. Otherwise it is the sum of the weights for the samples in the bin.  
PROB1 |  The probability (percentage) of samples in file IN1 lying within the bin.  
CUMPROB1 |  The cumulative probability (percentage) of samples in file IN1 less than **UPPER**.  
MEAN1 |  The mean grade of samples in file **IN1** lying within the bin.  
N2 |  If the **WEIGHT2** field has not been selected then **N2** is the number of samples in the bin (between **LOWER** and **UPPER**) for file **IN2**. Otherwise it is the sum of the weights for the samples in the bin.  
PROB2 |  The probability (percentage) of samples in file **IN2** lying within the bin.  
CUMPROB2 |  The cumulative probability (percentage) of samples in file IN2 less than **UPPER**.  
MEAN2 |  The mean grade of samples in file **IN2** lying within the bin.  
  
The QQOUT file includes the following fields:

Field |  Description  
---|---  
QUANTILE |  The quantile (expressed as a percentile)  
VALUE1 |  The corresponding quantile grade in file IN1.  
VALUE2 |  The corresponding quantile grade in file IN2.  
  
If PPPLOT and QQPLOT files are specified then plot files will be created even if the PPOUT and QQOUT files are not specified.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  First input data file. There must be a minimum of 5 records. |  Input |  Yes |  Table  
IN2 |  Second input data file. This can be the same as the first input file IN1. There must be a minimum of 5 records. |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PPOUT |  Output table for PP plot. At least one of the four output files must be specified. |  Output |  No |  Table  
PPPLOT |  Output plot file for PP plot. At least one of the four output files must be specified. |  Output |  No |  Plot  
QQOUT |  Output table for QQ plot. At least one of the four output files must be specified. |  Output |  No |  Table  
QQPLOT |  Output plot file for PP plot. At least one of the four output files must be specified. |  Output |  No |  Plot  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE1 |  Field in input file **IN1** to be plotted along the X axis of the PP and QQ plot. |  IN1 |  Yes |  Numeric |  Undefined  
VALUE2 |  Field in input file **IN2** to be plotted along the Y axis of the PP and QQ plot. |  IN2 |  Yes |  Numeric |  Undefined  
WEIGHT1 |  Weighting field for **VALUE1** in input file **IN1**. |  IN1 |  No |  Numeric |  Undefined  
WEIGHT2 |  Weighting field for **VALUE2** in input file **IN2**. |  IN2 |  No |  Numeric |  Undefined  
KEY |  Key field in the input **IN1** and optionally **IN2** file. The plot will include a line or set of symbols for each key field value. |  IN1 |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MINIMUM1 |  Minimum value of **VALUE1** field in input file IN1. Values below the minimum are ignored. |  No |  0 |  Undefined |  Undefined  
MINIMUM2 |  Minimum value of **VALUE2** field in input file IN2. Values below the minimum are ignored. |  No |  0 |  Undefined |  Undefined  
MAXIMUM1 |  Maximum value of **VALUE1** field in input file IN1. Values above the maximum are ignored. |  No |  Undefined |  Undefined |  Undefined  
MAXIMUM2 |  Maximum value of **VALUE2** field in input file IN2. Values above the maximum are ignored. |  No |  Undefined |  Undefined |  Undefined  
PLOTTYPE |  Flag to specify plot type (1); =1 : Scatter plot, using symbol X; =2 : Line plot |  No |  1 |  1,2 |  1,2  
BINSIZE |  Bin size for PP plot. |  No |  1 |  Undefined |  Undefined  
DIAGONAL |  Flag to control whether the diagonal (45 degree line) should be included on the plot (1). =0 : no diagonal line; =1 : include diagonal line. |  No |  1 |  0,1 |  0,1  
PROGRESS |  Flag to control amount of output written to Output Window (1). =0 : no output; =1 : progress messages |  No |  1 |  0,1 |  0,1  
DISPLAY |  Flag to select whether or not to display plot files. =0 : do not display plot files. =1 : display plot files. |  No |  1 |  0,1 |  0,1