![](../HeaderCell.jpg) |  Cross Validation Additional Notes  
---|---  
  
# Cross Validation Notes

The following additional notes on cross validation are available:

  * Introduction

  * Fitting the Model Visually

  * Selection of the Input Data

  * Output from XVALID

  * The Important Statistics

  * The Search Volume

  * Organising a Cross-validation Study

  * Practical Considerations

## 1 INTRODUCTION

Selecting a suitable variogram model type and determining its parameters is very much a subjective matter. Michel David, in his Handbook Of Applied Advanced Geostatistcal Ore Reserve Estimation (ISBN 0-444-41609-9), comments that 'After twenty years of practising geostatistics, this (model fitting) is probably the area where the least progress has been made'. Most of the standard geostatistical reference books describe the most important factors to take into account when fitting a model visually. Cross-validation (which is also known as jack-knifing or point kriging) is the only statistic-based method which is in common use, although even so it is not accepted by all practitioners.

The XVALID process provides a statistical method of fitting variogram parameters. Each sample in the data set is removed in turn and its value is estimated from the remaining data using point kriging. Thus for each sample there is an actual value and a kriged value estimated from the surrounding data. The XVALID process calculates a set of statistics comparing actuals and estimates which show how good (or bad) the estimates are. 

The first set of variogram parameters are fitted to the experimental variogram visually using VARFIT. These parameters are then used for the first run of XVALID . The output from the first run includes a set of statistics which can be compared with their optimum values as described later. One or more of the variogram parameters should then be changed and the process rerun to produce a second set of statistics. Comparing the first set of statistics with the second set will show whether the change in variogram parameters has improved the fit. The process is iterative requiring several runs of XVALID before the 'best' fit is determined. 

## 2\. FITTING THE FIRST MODEL VISUALLY

In general the first few points of the experimental variogram have been calculated using the largest number of sample pairs and are therefore the most reliable. However with some data sets the first point on the experimental variogram may have been calculated from very few sample pairs. Therefore always look at the experimental variogram table (as produced by VGRAM) to see the number of pairs used for each lag. If few pairs have been used then do not place much weight on that point. In VARFIT you can use the "Toggle - Number Of Pairs" option to turn on and off the display of sample pairs.

The main purpose of fitting a model variogram is to use it for kriging. When kriging blocks only the samples in the vicinity of the block are used to make the estimate. Hence only the first part (i.e. smaller distances) of the variogram model is used to calculate the kriging weights. Therefore it is more important that the model provides a good fit at smaller lag distances than at longer distances. For example if the search radius used for block kriging is 50 m then the maximum distance between any two samples which are to be used for the estimate is 100 m. Therefore the shape of the model variogram beyond 100 m is irrelevant.

The variogram sill value can often be approximated by the statistical variance of the samples. This can be displayed in VARFIT using the "Toggle - Variance" option. If the experimental variogram appears to waver around the sill value, then make sure that the nugget and spatial variance(s) add up to the statistical variance. However if the statistical variance does not provide a good fit then do not force the parameters to add up.

When the model has been fitted visually in VARFIT the parameters should be saved to file using the "Model - Write To File" option. This file can then be used as input to XVALID.

## 3\. SELECTION OF THE INPUT DATA

The cross-validation process can be quite time consuming, particularly with a large data set on a slow computer. Therefore it is often useful to select a 'typical' subset of the data to be used for the initial cross-validation runs, and to use the full data set for fine tuning the parameters. What constitutes a 'typical' data subset is not always easy to define, but this must be governed to a large extent by geological considerations.

One method of selecting a subset of data which is evenly distributed over the full volume is as follows:

  1. Sort the data on X,Y or Z;

  2. COPYNR to create a RECORDNO field;

  3. Decide the size of the data subset compared to the total data set; ie, the subset will be 1/N th of the total data set. Do not make the subset too small. One fifth (ie N=5) should be small enough for most purposes.

  4. Use EXTRA to set RECORDNO = MODC ( RECORDNO , N ). This will give successive records values of RECORDNO of 1, 2, 3, .... N-1, 0, 1, 2, 3 .....N-1, 0, etc

  5. COPY the data using the retrieval criteria RECORDNO=1 (or 2 or 3 etc) to create the data subset. Having selected a subset keep the same subset for all runs;

The following macro carries out the above steps:

!START M1 

!LET $N# = 5

!MGSORT &IN(samples),&OUT(temp1),*KEY1(X)

!COPYNR &IN(temp1),&OUT(temp2)

!EXTRA &IN(temp2),&OUT(temp3)

RECORDNO = modc(RECORDNO, $N#)

GO

!COPY &IN(temp3),&OUT(samples1),RECORDNO=1

!END

Although a subset of the data can be used for the initial determination of parameters, fine tuning should always be carried out on the full data set.

## 4\. OUTPUT FROM XVALID

The text written to the Output Window is divided into four sections:

  1. Progress Report

  2. Summary of Input Parameters

  3. Cross-Validation Statistics

  4. Cross-Validation Menu

For a full description refer to the XVALID on-line help file and follow the link to the Notes section. This description concentrates on section 3 - the cross-validation statistics. An example of the output is shown here:

CROSS-VALIDATION STATISTICS FOR AU

\----------------------------------------

Number of samples estimated = 1077

Number of samples not estimated = 0

Mean of actual values = 5.994147

Mean of estimated values = 5.964446

Mean difference (act - est) = 0.029706

Mean difference (as % of actual) = 0.495

Mean absolute difference = 1.612181

Variance of actual values = 7.73888

Variance of estimated values = 4.355755

Correlation coefficient = 0.666

Kriging Variance:

Mean of KV estimated from model = 4.313843

Mean of squared differences = 4.354414

Ratio = 0.99

Regression Equation:

Actual = 0.694132 + 0.888602 * Estimate

Standard Error = 2.073525

### Number of Samples

The number of samples estimated plus the number of samples not estimated equals the number of samples in the input file. A sample is not estimated if there is insufficient data in the search volume.

### Mean Values

For an unbiased estimate the actual and estimated means should be equal, although in practice a small difference is permissible.

### Mean Differences

The difference between the two mean values is expressed in three ways:

  * Mean difference (act - est). The estimated mean subtracted from the actual mean.

  * Mean difference (as % of actual). Calculated as 100 * (actual - estimated) / actual.

  * Mean absolute difference (MAD). Calculated as the mean of the positive differences of actual minus estimated.

The aim is to make all three statistics as close as possible to zero. The percentage difference (item 2) should be less than 5% and hopefully less than 2%.

### Variance of Actuals and Estimates

These two statistics are not used for estimating the variogram parameters. The variance of the actuals is fixed for the input data set, and the variance of the estimates will always be less than the variance of the actuals, because of the smoothing involved in the kriging process.

### Correlation Coefficient of Actual and Estimate:

The correlation coefficient always lies between -1 and +1, with a value of +1 showing perfect positive correlation. The aim should be to make the correlation coefficient as large as possible. However it is still possible to have a very low coefficient value (eg, 0.15) and for this value to be statistically significant, if the data set is large. The significance of a correlation coefficient can be found by calculating the t value and testing it against the distribution of Student's t:

t = r * sqrt (N - 2) / sqrt (1 - r*r)

where r is the correlation coefficient and N the number of samples.

Note that the calculation of the significance of a correlation coefficient assumes that the variables are normally distributed. One or two outliers can have a marked effect on the value of the coefficient.

### Kriging Variance

Three statistics are shown under this heading:

  1. The mean kriged variance estimated from the (variogram) model. For every kriged estimate the corresponding kriged variance is calculated, based on the relative locations of the samples and the model variogram parameters. This statistic is the average of these kriged variances.

  2. Mean of squared differences. This is calculated as the sum of (actual - estimated) squared divided by the number of samples. This is a measure of the same variance as item 1 above.

  3. Ratio. The ratio is calculated as the mean kriging variance (item 1) divided by the mean squared difference (item 2). This should lie in the range between 0.8 and 1.2, and be as close as possible to 1. This is one of the most important statistics to be considered when fitting the parameters.

### Regression Equation

One of the options on the XVALID interactive menu is to create a scatter plot of actual against estimate, as illustrated in the XVALID Process Description. If all the estimates were perfect then all points would lie on the 45 degree line. However in practice there will be a cloud of points, scattered around the 45 degree line.

The regression equation of actual on estimate is calculated using the standard least squares method. The equation has the format:

actual = c + b * estimate

For perfect regression constant c (the intercept on the Y axis - actual) should be equal to zero and the slope of the line (b) equal to 1.

## 5\. THE IMPORTANT STATISTICS

The three most critical statistics when fitting the model variogram parameters are usually considered to be:

  * mean difference (as % of actual)

  * kriging variance ratio

  * correlation coefficient

followed by:

  * mean absolute difference

  * regression line slope (constant b)

However, a change in the one of the input model variogram parameters will often result in some of the statistics improving and others getting worse. The end result is likely to be a compromise.

## 6\. THE SEARCH VOLUME

The samples to be used for kriging each point are selected using both a minimum and a maximum search volume. Only the samples which lie both outside the minimum volume and inside the maximum volume are used. The reason for including a minimum search volume is that if there are a few samples very close to the point being estimated then these samples will get most of the kriged weight and samples further away will be ignored. Thus the cross validation results will only test the values of the variogram parameters at small distances. The variogram will subsequently be used for block kriging, so it is important that the variogram fitting should reflect all distances within the proposed search volume. Therefore it is useful to be able to eliminate samples which are very close to the point being kriged, and this is done using the minimum volume.

The use of a minimum volume is particularly pertinent when the sample data set includes consecutive samples along a borehole. The samples on either side of the one being kriged will be assigned the majority of the weight. The minimum search volume should be set to eliminate either one or two samples on either side of the one being kriged.

The maximum search volume is defined using the search volume parameter file. The minimum volume is calculated by applying a multiplying factor to the axes of the maximum search volume. This factor is defined by parameter SMINFAC. The minimum volume has the same orientation as the maximum volume and will be concentric to it.

A maximum of 30 samples in the search volume is usually sufficient. Under normal circumstances the axes of the maximum search volume would be set equal to the variogram ranges in the three dimensions. If the variogram model has more than one structure then the ranges of the longest structure should be used. However if this consistently gives more than 30 samples in the search volume the search axes can be reduced by multiplying all three by a factor.

## 7\. ORGANISING A CROSS VALIDATION STUDY

A cross validation study can produce a lot of output and a lot of numbers. It is therefore important to be well organised when carrying out the study. In particular it is very useful to create a manual summary of the results, and so a prototype form suitable for recording the results of fitting one or two structure models is provided. When printing the form select landscape orientation and set all margins to zero.

Columns 1 to 11 are for the input parameters and columns 12 to 18 for the output statistics.

### Input

  * Run Number:   
This is simply a user supplied reference number.

  * Model Type:   
The variogram model type, as defined by the ST1 and ST2 fields in the variogram model file.

  * Minimum Radius Factor:    
The multiplying factor for calculating the axes of the minimum search volume (parameter SMINFAC)

  * Maximum Radii:    
The axes of the maximum search volume (fields SDIST1, SDIST2, SDIST3 in the search volume parameter file).

  * Sample number minimum and maximum:   
The minimum and maximum number of samples to be used for kriging, as defined by fields MINNUM1 and MAXNUM1 in the search volume parameter file.

  * Nugget Variance:   
The nugget variance of the variogram model. Field NUGGET in the variogram model file.

  * Structure 1 Ranges in X,Y and Z:   
Fields ST1PAR1, ST1PAR2 and ST1PAR3 in the variogram model file.

  * Structure 1 Spatial Variance:   
The spatial variance for the first structure of the model variogram. Field ST1PAR4 in the variogram model file.

  * Structure 2 Ranges in X,Y and Z:   
Fields ST2PAR1, ST2PAR2 and ST2PAR3 in the variogram model file.

  * Structure 2 Spatial Variance:   
The spatial variance for the second structure of the model variogram. Field ST2PAR4 in the variogram model file.

  * Angles:   
The three rotation angles defining anisotropy. Fields VANGLE1, VANGLE2 and VANGLE3 in the variogram model file.

### Output

  * Number of Points:   
Record here both the number of points kriged and the number of points not kriged (if any).

  * % Error:   
The mean difference (as % of actual).

  * Correlation Coefficient:   
The correlation coefficient.

  * Mean Kriging Variance:   
The mean KV estimated from the model.

  * KV Ratio:   
The kriging variance ratio.

  * MAD:   
The mean absolute difference.

  * Slope of Regression Line:   
Variable b, where Actual = c + b * Estimate

  * Comments:   
This column is available for user comments.

## 8\. PRACTICAL CONSIDERATIONS

### Adjusting the Parameters

The main variables to be 'fitted' are the model type and its parameters. However other variables which can affect the goodness of fit include the search volume and the minimum and maximum number of samples. This means that there can be a large number of variables to be considered. It is recommended, at least in the early stages of fitting, that only one variable at a time is considered.

Increasing the nugget variance while maintaining a constant sill value will increase the kriging variance estimated from the model and hence increase the kriging variance ratio. Decreasing the range will have a similar though smaller effect.

### Outliers

Outliers can have a significant effect on the cross-validation results. If an upper cut is to be applied then this should be done prior to the calculation of the experimental variograms and cross-validation. Even if cutting has been applied it is still advisable to determine the sensitivity of the cross-validation results to the highest outliers by removing them from the data set and rerunning.

### Lognormal Kriging

The lognormal variogram will often have a smoother appearance than the normal one and so lognormal kriging can be considered. The cross validation process gives a good method of comparing the results of log and normal kriging. In practice it is often found that although the log kriging model gives a better visual fit, the normal model gives better cross validation results. In the event of the two methods giving similar results it is better to choose the normal model which is more robust and less sensitive to assumptions regarding the distribution.

### Inverse Power of Distance

The process can be used to 'fit' inverse power of distance (IPD) parameters, and to compare the results with kriging. The main IPD parameters to be tested are the power and the search volume. It should be noted that the output from cross validation using IPD is identical to the kriging output and therefore includes kriging variance and kriging variance ratio even though no kriging has been carried out. For IPD these values are calculated as follows:

  * Mean of squared differences: this is calculated as for kriging ie it is the mean squared difference between actuals and estimates;

  * Mean kriging variance estimated from model: this is calculated as the variance of the mean of all samples within the search volume ie, if there are M samples within the search volume and the variance of these M samples is S2 the "kriging variance" is S2 / M.

### Nearest Neighbour

The process can also be used to 'fit' nearest neighbour (NN) parameters, and to compare the results with kriging. However there is no equivalent to the kriging variance so statistics relating to the variance are omitted.