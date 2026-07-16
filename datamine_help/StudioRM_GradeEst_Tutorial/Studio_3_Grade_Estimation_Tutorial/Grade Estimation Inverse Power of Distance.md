# Grade Estimation Inverse Power of Distance

![](../HeaderCell.jpg) |  Grade Estimation - Inverse Power of Distance A more detailed look at the inverse power of distance grade estimation method  
---|---  
  
# Inverse Power of Distance

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

For overview information on all grade estimation methods in general, see [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>).

## IMETHOD = 2

This method is chosen if the IMETHOD field in the Estimation Parameter file is set to 2.

For Inverse Power Distance (IPD) the estimated value is calculated by weighting each sample by the inverse power of its distance from the cell. The required power is defined using the field POWER. If POWER is set to zero, then the arithmetic mean of the samples is calculated.

All samples lying within the search volume are identified as described previously, and restrictions on the minimum and maximum number of samples applied. An estimate is made of the grade of each [discretised](<Grade%20Estimation%20Cell%20Discretisation.md>) point in the cell. This is done using the anisotropic distance in exactly the same way as described for the Nearest Neighbor method. The estimated cell value is then calculated as the arithmetic mean of the estimates of the discretised points.

## ADDCON

If a sample lies exactly on a discretised point, then it will be at zero distance from that point and will get 100% of the weight. This can lead to a biased estimate, particularly if there is only one discretised point and there are other samples lying within the cell. However, this can be avoided by specifying a positive value for the field ADDCON.

The value of ADDCON is first normalized by dividing the value specified by the length of the largest anisotropy axis. The process will then add the value of ADDCON to each distance before estimating the value at the discretised point.

## Length and Density Weighting

It is possible to include both length and/or density weighting in the Inverse Power Distance calculation by specifying fields *LENGTH_F and/or *DENS_F. For example:

*LENGTH_F(LENGTH), *DENS_F(DENSITY)

If density and length weighting are used then the weight Wi assigned to sample i for estimating a discretised point is:

Wi = Li x ρi / DiP

where:

  * Li is the length of sample i

  * ρi is the density of sample i

  * DiP is the transformed distance of sample i from the discretised point, raised to the power P

The estimate Ek of discretised point k is then given by:

Ek = Σ Wi x Gi / Σ W

where:

  * Gi is the grade of sample i.

The cell estimate Ec is then calculated as the arithmetic mean of all discretised points:

Ec = Σ Ek / N

where:

  * N is the number of discretised points.

If *LENGTH_F and/or *DENS_F have been specified, but a record in the Sample Data file has absent data value(s) for these field(s), then that sample will not be used in the estimation.

## Inverse Power Distance Variance

In addition to the Inverse Power Distance estimate, the variance, V, of the samples is also calculated. This is simply the classical statistical variance of all the samples used for making the Inverse Power Distance estimate:

V = ( Σ Gi2 \- ( Σ Gi )2 / NS ) / ( NS \- 1 )

where:

  * Gi is the grade of sample i

  * NS is the number of samples used in making the estimate

This secondary field can be saved in the Output Model file using field VAR_F as described in [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>).

![](../Images/NextExercise.gif)[Proceed to the next section](<Grade%20Estimation%20Kriging.md>) (Kriging Method)

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