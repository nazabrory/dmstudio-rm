![](../HeaderCell.jpg) |  Grade Estimation - Nearest Neighbour A more detailed look at the nearest neighbour grade estimation method  
---|---  
  
# Nearest Neighbour

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

For overview information on all grade estimation methods in general, see [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>).

## IMETHOD = 1

This method is chosen if the IMETHOD field in the Estimation Parameter file is set to 1.

Using this method the cell is assigned the value of the 'nearest' sample, where 'nearest' is defined as a transformed or anisotropic distance which takes account of any anisotropy in the spatial distribution of the grade.

The Nearest Neighbor method does not involve weighting sample values, and so either a numeric or an alphanumeric field can be estimated. The alphanumeric field may have up to 20 characters (5 words).

## Anisotropy Ellipsoid

All samples lying within the search volume are identified as described previously. The anisotropic distance from the sample to the cell centre is then calculated based on an anisotropy ellipsoid which is defined using an identical method to the search ellipsoid. It is usual for the search ellipsoid and the anisotropy ellipsoid to be the same. It is possible to define different ellipsoids if necessary.

The field ANISO is used to define which transformed distance to use. This field can have the values:

  * 0 \- no transformation i.e. isotropic. Distances are calculated from the coordinate system used in the Sample Data file.

  * 1 \- use the transformed distances defined by the search volume.

  * 2 \- use the transformed distances defined by the anisotropy ellipsoid.

If ANISO = 2, then it is necessary to specify the anisotropy ellipsoid using fields ANANGLE1, ANANGLE2, ANANGLE3 and ANDIST1, ANDIST2, ANDIST3. These are defined in an identical manner to SANGLEn and SDISTn as described in the Search Volume section.

Although it is possible to define different angles and axes for the anisotropy ellipsoid, the rotation axis convention must be the same as for the Search Volume, i.e. the first rotation is around SAXIS1, then SAXIS2 and finally SAXIS3.

![](../Images/NextExercise.gif)[Proceed to the next section](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>) (Inverse Power of Distance Method)

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