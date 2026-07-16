![](../HeaderCell.jpg) |  Grade Estimation - Kriging More details about the kriging estimation method  
---|---  
  
# Kriging

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

For overview information on all grade estimation methods in general, see [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>).

## IMETHOD = 3 or IMETHOD = 4

Kriging is the geostatistical method for estimating the grade of a volume. The two variations of [kriging](<Grade%20Estimation%20Kriging.md>) available in ESTIMA are Ordinary Kriging and Simple Kriging, which are identified by the IMETHOD field in the Estimation Parameter file:

  * Ordinary Kriging (OK): IMETHOD = 3

  * Simple Kriging (SK): IMETHOD = 4

As with [Inverse Power of Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>) method (IPD), kriging assigns weights to the surrounding data. However, one of the major advantages of kriging is that the weights are calculated in order to minimize the error variance.

## Spatial Location of Samples

When minimizing the error variance, kriging takes into account the spatial location of the samples relative to each another. Hence, if several samples are bunched together, this will be taken into account when the weights are calculated and the weights reduced accordingly. This is not the case for IPD, where the weight is only dependent on the distance of the sample from the point being estimated, and does not take account of the location of the other samples.

The calculation of the kriged weights is based on the model variogram, which describes the correlation between two samples as a function of the distance between them. Further details of variogram models are given in the Variogram Model Parameter file section.

## Ordinary and Simple Kriging

For Ordinary Kriging (OK) a weight is calculated for each sample, and the sum of these weights is 1. For Simple Kriging(SK) a weight Wi is calculated for each sample and a weight of ( 1 - ΣW ) is assigned to the mean grade.

Simple Kriging is not as responsive as Ordinary Kriging to local trends in the data, since it depends partially on the mean grade, which is assumed to be known, and constant throughout the area. Ordinary Kriging is therefore the most commonly used method of kriging. For further details of the kriging methodology and the calculation of weights, please consult the [geostatistical references](<Grade%20Estimation%20References.md>).

The inputs for Ordinary Kriging and Simple Kriging are very similar and so the following description applies to both methods. There is a small section towards the end which is specific to Simple Kriging.

## Lognormal Kriging

ESTIMA allows linear and lognormal kriging for both Ordinary Kriging and Simple Kriging.

The field LOG in the Estimation Parameter file is used to select whether linear or lognormal kriging is to be used.

For linear kriging the weights are applied to the sample grades, whereas for lognormal kriging the weights are applied to the logs of the grade and then back transformed. All transformations are done within ESTIMA. For Ordinary Kriging the lognormal back transformation used is:

Ec = exp (Σ Wi x log (Gi) + 0.5 x (Σ Wi x σ(Li,Li) - Σ ΣWi x Wj x σ(Li,Lj)))

Where:

  * Ec is the kriged estimate

  * Wi is the weight for sample i

  * Gi is the grade for sample i

  * σ(Li,Lj) is the covariance of the logs of the grades of sample i and j

The algorithm for lognormal kriging is based on the method by P.A Dowd in his paper entitled ‘Lognormal Kriging – The General Case’, referred to in the Bibliography.

Two methods of calculation are allowed – Rendu’s approximation method, and the General Method. It should be noted that the General method is an iterative process and can require several solutions of the kriging matrix for each panel kriged. It therefore has a longer run time than Rendu’s method. You are strongly recommended to read the paper by P.A.Dowd, but its conclusions are summarized below. The variable C is the spatial variance for a spherical variogram model.

  1. For small values of C(<1), the general case of lognormal kriging, assuming conservation of lognormality, gives results which are not significantly different from those obtained without the assumption of conservation of lognormality. As C increases the kriging variances obtained from both methods remain very similar, but the difference in kriging weights become increasingly significant.

  2. Rendu’s approximation consistently underestimates the kriging variance even for relatively small panels (e.g. sides equal to 20% of the range).

  3. Ordinary kriging consistently overestimates the kriging variance.

  4. All methods give similar results for very small panels (sides of 5% or les of the range), except when a nugget variance (Co) is present; then ordinary kriging results differ significantly from the others.

  5. As Co increases, the results obtained from Rendu’s approximation approach those obtained without the assumption of conservation of lognormality, although the approximation still significantly underestimates the kriging variance. The significance of the differences in the results obtained from ordinary kriging and from the other methods increases as the nugget variance increases.

You are also strongly recommended to read other papers on the subject. In particular, pages 119-120 of the Handbook of Applied Advanced Geostatistical Ore Reserve Estimation by Michel David show that great care must be taken when applying lognormal kriging.

If lognormal kriging is selected then it is necessary to indicated whether Rendu's approximation or the General Case is to be applied by entering the appropriate value for the field GENCASE.

  * GENCASE= 0 use Rendu's approximation

  * GENCASE= 1 use the General Case method

If the General Case is selected then three more fields, DEPMEAN, TOL and MAXITER should be included in the Estimation Parameter file, as described below.

The lognormal kriged variance is calculated as a relative variance, VR , relative to the square of the mean, m, of the deposit:

VR = VA / m2

In order for the process to calculate the absolute variance, VA, it is necessary to specify either the actual deposit mean, m, or set it to zero. If the absolute variance is set to zero, then the process uses the kriged estimate of the cell as the mean.

  * DEPMEAN > 0 use this value as the mean

  * DEPMEAN = 0 use the kriged estimate as the mean

The General Case method uses an iterative procedure for calculating the kriged weights. The weights are calculated and compared with their previous estimates. If each weight lies within a certain tolerance of its previous value then the new weights are accepted; otherwise, another set of weights is calculated. The tolerance, field TOL, and the maximum number of iterations, field MAXITER are user defined. If the weights have not converged after MAXITER iterations then the calculation for that cell terminates and the newest set of weights are used.

## Variogram Model

For each VALUE_IN field to be estimated by kriging, the corresponding variogram reference number (VREFNUM) should be defined in the Estimation Parameter file. This is simply a reference to the model variogram type and parameters as stored in the Variogram Model Parameter file. Therefore any numeric value can be used so long as it is unique in the Variogram Model Parameter file.

The models stored in the Variogram Model Parameter file can be either normal or lognormal.

The field LOG in the Estimation Parameter file is used to select whether linear or lognormal kriging is to be used.

## Kriging the Cells

As for Nearest Neighbor and Inverse Power Distance, the first step is to identify all samples lying in the search volume, restricted by the constraints on the minimum and maximum number of samples. The kriging matrix is then set up and solved to produce the kriging weights and hence the kriged estimate.

In addition to the kriged estimate, three secondary variables can be calculated for each cell and saved in the Output Model file.

  * the number of samples used for kriging

  * the kriged variance

  * the transformed distance to the nearest sample

In order to save these secondary variables, their field names must be defined in the Estimation Parameter file, as described previously.

## Negative Kriging Weights

Under certain conditions, the weights assigned to one or more of the samples can be negative. This is most likely to happen when the model variogram has a low nugget variance and a sample is shielded from the cell by other samples lying directly between it and the cell. It is unlikely that negative weights would account for more than a few percent of the total weight. Although negative weights are mathematically correct, there is a school of thought which considers that negative weights are incorrect and should be set to zero. This can be done using the field KRIGNEGW:

  * KRIGNEGW = 0 negative weights kept and used

  * KRIGNEGW= 1 negative weights set to zero

If negative weights are set to zero, then the weights of the other samples are proportionally adjusted so that the sum of the weights still equals 1. Any checks on the minimum number of samples (MINNUMn) are applied before kriging weights are calculated, so it is possible to have less than MINNUMn samples.

## Kriging Variance > Sill

Due to the mathematical complexities of the kriging calculations it can sometimes happen that the kriged variance is slightly greater than the sill of the model variogram. Field KRIGVARS in the Estimation Parameter file controls whether the calculated variance remains above the sill or is set equal to the sill.

  * KRIGVARS = 0 keep variances > sill

  * KRIGVARS = 1 reset variances > sill equal to sill

This control only applies to linear kriging. Variances for lognormal kriging are dependent on the value of DEPMEAN and are therefore often greater than the sill.

## Simple Kriging

Simple kriging assigns a weight to a local mean value, as well as assigning weights to the surrounding samples. Fields LOCALMNP and LOCALM_F in the Estimation Parameter file are used to select how this local mean value is defined:

  * LOCALMNP = 1 use a field in the Input Prototype Model file to define the local mean.

  * LOCALMNP = 2 calculate the local mean as the arithmetic mean of all samples lying in the search volume.

If LOCALMNP = 1 then the name of the field in the Input Prototype Model file which defines the local mean must also be specified. The field name in the Estimation Parameter file is LOCALM_F and is an 8 character alphanumeric field. For example:

Description |  Name of field to be estimated |  Name of field in output model |  Search volume reference number |  Estimation method |  Method for estimating local mean for SK |  Local mean field in Input Prototype Model File |  Model variogram reference number  
---|---|---|---|---|---|---|---  
Field Name |  VALUE_IN |  VALUE_OU |  SREFNUM |  IMETHOD |  LOCALMNP |  LOCALM_F |  VREFNUM  
Field Type |  A-8 Chars |  A-8 Chars |  N |  N |  N |  A-8 chars |  N  
Record 1 |  AU |  AU-OK |  1 |  3 |  - |  |  1  
Record 2 |  AG |  AU-OK |  1 |  3 |  1 |  AU-LMEAN |  1  
  
The grade AU is to be estimated by both Ordinary Kriging (IMETHOD = 3) and Simple Kriging (IMETHOD = 4). For Simple Kriging the local mean is provided by field AU-LMEAN in the Input Prototype Model file. Therefore, this field must have been created previously. This could be done in a prior run of ESTIMA, using IPD with POWER = 0 and a large search radius. This would give the arithmetic mean of all samples lying in the search volume. Alternatively, the mean values depending on a rock type or other geological feature could be assigned.

The grade AG will also be estimated using simple kriging. As LOCALMNP = 2 the local mean will be calculated as the arithmetic mean of all samples lying in the search volume. This is calculated before the maximum number and key field constraints are applied.

![](../Images/NextExercise.gif)[Proceed to the next section](<Grade%20Estimation%20Sichels%20T%20Estimator.md>) (Sichel's T Estimator)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Introducing the Grade Estimation User Guide](<Grade%20Estimate%20Overview.md>)[  
Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>)[  
Grade Estimation Dynamic Search Volumes](<Grade%20Estimation%20Dynamic%20Search%20Volumes.md>)[  
Grade Estimation Octants](<Grade%20Estimation%20Octants.md>)[  
Grade Estimation Key Fields](<Grade%20Estimation%20Key%20Fields.md>)[  
Grade Estimation Search Volume Parameter File](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>)[  
Grade Estimation Cell Discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>)[  
Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)[  
Grade Estimation Parameter File](<Grade%20Estimation%20Parameter%20File.md>)[  
Grade Estimation Additional Features  
Grade Estimation Variograms  
Grade Estimation Run Time Optimization  
Grade Estimation Rotated Models  
Grade Estimation Output and Results  
Grade Estimation Parameter Summary  
Grade Estimation System Limits](<Grade%20Estimation%20Additional%20Features.md>)[  
Grade Estimation References  
  
ESTIMA command Help   
ESTIMATE command Help  
The Estimate dialog  
VARFIT Command Help](<Grade%20Estimation%20References.md>)