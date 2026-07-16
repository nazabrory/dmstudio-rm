# ESTIMA Process

To access this process:

  * **Estimate** ribbon **> > Interpolate >> Standard >> ESTIMA**.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#ESTIMA>)](<../command_help/_COMMAND%20TABLE_A.md#ACCMLT>).

## Process Overview

The **ESTIMA** process provides a choice of methods for grade estimation of a block model.

For in-depth conceptual information on the **ESTIMA** process, and grade estimation in general, see [Grade Estimation Introduction](<../STUDIO_RM/Grade%20Estimate%20Overview.md>).

**ESTIMA** provides the following grade estimation methods:

  * Nearest Neighbor (NN).

  * Inverse Power of Distance [IPD].

  * Ordinary Kriging (OK).

  * Simple Kriging.

  * Log Kriging.

  * Sichel's T Estimator.

  * Ordinary Macro Kriging

  * Simple Macro Kriging

  * F-value

  * Lagrange multiplier

Key ESTIMA features:

  * Multiple grades can be estimated in a single run.

  * The same grade can be estimated by different methods.

  * Different search volumes and estimation parameters can be used for the different grades.

  * Rectangular or ellipsoidal search volume with anisotropy.

  * Restriction of number of samples by octant.

  * Restriction of number of samples by key field.

  * Estimation by zone, with separate parameters for each zone.

  * Wide selection of variogram model types for both normal and lognormal kriging.

  * Automatic transformation of data if the &PROTO model is a rotated model.

  * Unfolding option available for all estimation types.

  * Optimization of sample searching to improve processing speed.

  * Parent cell estimation.

  * Selective update of a partial model.

If the input **& PROTO** model contains cells and sub-cells then values are interpolated into the existing cell structure. If **& PROTO** is empty then cells and sub-cells are created if there are sufficient samples within the search volume.

**ESTIMA** requires a search volume to be defined. This is the volume, centered on the cell being estimated, which contains the samples to be used for grade estimation. In fact more than one search volume may be defined, so that different grades can have different search volumes. The parameters describing the search volume(s) are supplied using the Search Volume Parameter file **& SRCPARM**.

**Note** : **ESTIMA** parameter files can be imported and transformed for use in **[COKRIG](<cokrig.md>)** using the Advanced Estimation console's **[Parameters](<../STUDIO_RM/Multivariate_Import_Parameters.md>)** panel).

**ESTIMA** also requires a set of estimation parameters to be defined for each grade to be estimated. These parameters are also supplied to **ESTIMA** using a file - in this case the Estimation Parameter file. It will include items such as the estimation method, the search volume reference number and for example the power, if Inverse Power of Distance is selected.

**Note** : Search volume parameter files exported from the Advanced Estimation console cannot be used as an input to the **ESTIMA** process, or the **[ESTIMATE](<estimate.md>)** screen.

**ESTIMA** estimation methods include Nearest Neighbor, Inverse Power of Distance, and Sichel's t Estimator. MOD also includes Ordinary Kriging with a single structure spherical model variogram. The additional options in EGS are a choice of variogram models, lognormal kriging and Simple Kriging. Please consult your local Datamine office if you would like further information on these modules.

**Note** : When **COKRIG** or **ESTIMA** run Dynamic Anisotropy and less than 3 angles are used, the process replaces the missing angles with angles from the selected search or variogram.

## ESTIMA and COKRIG

Key differences between **ESTIMA** and **COKRIG** :

  * In **COKRIG** , the octant method is not directly supported but can be approximated using the sector method with 4 sectors and a horizontal split.

  * Power and De Wijsian variogram models are not supported in **COKRIG**.

  * There is no option to reset negative kriging weights to zero in **COKRIG**.

Advantages of **COKRIG** over **ESTIMA** :

  * Multivariate geostatistics!

  * Optimized for parallel processing speed increase approximately by a factor of the number of (virtual) cores on the computer.

  * Significant speed improvements when using large or multiple search volumes.

  * More flexible search volume parameters segments/more than 2 additional search volumes.

The main differences between the variogram models for **COKRIG** and **ESTIMA** are:

  * A variogram model set number (**VSETNUM**) is used instead of a variogram reference number (**VREFNUM**)

  * The variogram model requires two additional fields **GRADE** and **GRADE2** to identify the grade or grades in the case of cross-variograms, to which the model applies.

Variogram models from either **COKRIG** or **ESTIMA** can be specified when using **COKRIG** /Advanced Estimation.

## Input Files

**Name** |  **I/O Status** |  **Required** |  **Type** |  **Description**  
---|---|---|---|---  
PROTO |  Input |  Yes |  Block_Model_File |  Input model prototype. This is a standard block model file containing the 13 compulsory fields. It may also contain the rotated model fields. If it includes cells then it must be sorted on IJK.  
IN |  Input |  Yes |  Table |  **Input sample data**. This must contain X,Y and Z fields and at least one grade field.  
SRCPARM |  Input |  Yes |  Undefined |  Search volume parameter file. This contains 24 compulsory fields defining the search volume and the number of samples needed for grade estimation. More than one search volume may be defined. All fields are numeric: SREFNUM Search volume reference number. SMETHOD Search volume shape.

  * 1 = 3D rectangle
  * 2 = ellipsoid.

SDIST1 Max search distance in direction 1. SDIST2 Max search distance in direction 2. SDIST3 Max search distance in direction 3. SANGLE1 First rotation angle for search vol. SANGLE2 Second rotation angle. SANGLE3 Third rotation angle. SAXIS1 Axis for 1st rotation (1=X,2=Y,3=Z). SAXIS2 Axis for 2nd rotation (1=X,2=Y,3=Z). SAXIS3 Axis for 3rd rotation (1=X,2=Y,3=Z). MINNUM1 Min number of samples, 1st search vol. MAXNUM1 Max number of samples, 1st search vol. SVOLFAC2 Axis multiplying factor,2nd search vol. MINNUM2 Min number of samples, 2nd search vol. MAXNUM2 Max number of samples, 2nd search vol. SVOLFAC3 Axis multiplying factor,3rd search vol. MINNUM3 Min number of samples, 3rd search vol. MAXNUM3 Max number of samples, 3rd search vol. OCTMETH Octant method flag.

  * 0 = no octant search,
  * 1 = use octants.

MINOCT Minimum number of octants to be filled. MINPEROC Minimum number of samples in an octant. MAXPEROC Maximum number of samples in an octant. MAXKEY Maximum number of samples with the same key value within an octant  SANGL1_F Name of field in the input prototype model file that contains the first rotation angle for dynamic anisotropy. SANGL2_F Name of field in the input prototype model file that contains the second rotation angle for dynamic anisotropy. SANGL3_F Name of field in the input prototype model file that contains the third rotation angle for dynamic anisotropy.  
ESTPARM |  Input |  Yes |  Undefined |  Estimation parameter file. Each record in the file describes an estimation method and its associated parameters. The fields are dependent on the estimation methods selected. All fields are optional except for VALUE_IN and SREFNUM. General fields: VALUE_IN 2A4 Field to be estimated. SREFNUM N Search volume reference number. VALUE_OU 2A4 Field to be created in MODEL (Default is VALUE_IN). {ZONE1_F} A/N 1st field for zonal estimation. The actual name of the field is given by ZONE1_F on command line eg ZONE1_F(ROCK). {ZONE2_F} A/N 2nd field for zonal estimation. NUMSAM_F 2A4 Field to be created in MODEL for the number of samples. SVOL_F 2A4 Field to be created in MODEL for dynamic search volume number. V VAR_F 2A4 Field to be created in MODEL for variance of estimate. MINDIS_F 2A4 Field to be created in MODEL for distance to nearest sample. IMETHOD N Estimation method.

  * 1 = Nearest neighbour (NN).
  * 2 = Inverse power of dist (IPD).
  * 3 = Ordinary kriging (OK).
  * 4 = Simple kriging (SK).
  * 5 = Sichel's t estimator.
  * 6 = Ordinary macro kriging.
  * 7 = Simple macro kriging.
  * 8 = Circular IPD, for estimating angles.
  * 9 = Correlation factor method.
  * 101 = F-value
  * 102 = Lagrange Multiplier

Fields for IPD and NN: ANISO N Anisotropy method:

  * 0 = No anisotropy.
  * 1 = Use search vol anisotropy.
  * 2 = Use ANANGLEn.

ANANGLE1 N Anisotropy angle 1. ANANGLE2 N Anisotropy angle 2. ANANGLE3 N Anisotropy angle 3. ANDIST1 N Anisotropy distance 1. ANDIST2 N Anisotropy distance 2. ANDIST3 N Anisotropy distance 3. POWER N Power of distance for weighting. ADDCON N Constant added to distance. Fields for kriging: VREFNUM N Variogram model reference number. VANGL1_FName of field in input prototype model MODEL used to define the first variogram rotation angle for dynamic anisotropy. VANGL2_F Name of field in input prototype model MODEL used to define the second variogram rotation angle for dynamic anisotropy. VANGL3_F Name of field in input prototype model MODEL used to define the third variogram rotation angle for dynamic anisotropy. LOG N Lognormal variogram flag.

  * 0 = Normal kriging.
  * 1 = Lognormal kriging.

KRIGNEGW N Treatment of -ve weights:

  * 0 = -ve weights kept and used.
  * 1 = Ignore samples with -ve weights

KRIGVARS N Treatment of variance > sill:

  * 0 = Write variance to MODEL.
  * 1 = Set variance to sill.

Fields for lognormal kriging: GENCASE N Calculation method:

  * 0 = Rendu's method.
  * 1 = General case.

DEPMEAN N Deposit mean [If 0 then use kriged estimate]. Fields for general case: TOL N Tolerance for convergence. MAXITER N Maximum number of iterations. Fields for simple kriging: LOCALMNP N Method for calculation of local mean: 1 = use field defined in PROTO 2 = use mean within search vol. LOCALM_F 2A4 Name of local mean field in PROTO; used if LOCALMNP=1  
VMODPARM |  Input |  No |  Variogram - Model |  Variogram model parameter file. Each record in this file defines a variogram model type and its parameters. Only the **VREFNUM** field is compulsory. VREFNUM Model variogram reference number. VANGLE1 Variogram anisotropy angle 1. VANGLE2 Variogram anisotropy angle 2. VANGLE3 Variogram anisotropy angle 3. VAXIS1 Model variogram rotation axis 1. VAXIS2 Model variogram rotation axis 2. VAXIS3 Model variogram rotation axis 3. NUGGET Nugget variance. ST1 Variogram model type for structure 1.

  * 1 = Spherical.
  * 2 = Power [eg 1 - linear].
  * 3 = Exponential.
  * 4 = Gaussian.
  * 5 = De Wijsian.

ST1PAR1 1st parameter of structure 1 [Range 1 for spherical model]. ST1PAR2 2nd parameter of structure 1 [Range 2 for spherical model]. ST1PAR3 3rd parameter of structure 1 [Range 3 for spherical model]. ST1PAR4 4th parameter of structure 1 [C variance for spherical model]. STn Variogram model type for structure n. STnPARp pth parameter for structure n, where n<=9.  
STRING |  Input |  No |  String |  Input string file holding the boundary strings which define the stratified unit[s] for unfolding. 7 fields are compulsory: SECTION , BOUNDARY , PVALUE , XP , YP , ZP and PTN. 3 optional fields are WSTAG , BSTAG and TAG. The file must be sorted on SECTION , BOUNDARY PTN , with SECTION being the primary keyfield. It is assumed that the section numbering system is such that sorting on SECTION will ensure that physically adjacent sections are adjacent in the STRING file.  
  
## Output Files

**Name** |  **I/O Status** |  **Required** |  **Type** |  **Description**  
---|---|---|---|---  
MODEL |  Output |  Yes |  Block Model File |  Output model containing estimated grades, variance etc.  
SAMPOUT |  Output |  No |  Undefined |  Output sample file containing details of weights for each sample for each cell estimated.  
  
## Fields

**Name** |  **Description** |  **Source** |  **Required** |  **Type** |  **Default**  
---|---|---|---|---|---  
X |  X coordinate of sample data in IN file. If not specified, then X is assumed. If the unfolding option is used, then the X coordinate must be set to the unfolded UCSA coordinate. |  IN |  No |  Numeric |  Undefined  
Y |  Y coordinate of sample data in IN file. If not specified, then Y is assumed. If the unfolding option is used, then the Y coordinate must be set to the unfolded UCSB coordinate. |  IN |  No |  Numeric |  Undefined  
Z |  Z coordinate of sample data in IN file. If not specified, then Z is assumed. If the unfolding option is used, then the Z coordinate must be set to the unfolded UCSC coordinate. |  IN |  No |  Numeric |  Undefined  
ZONE1_F |  First field for zonal control. A maximum of 202 zone combinations is permitted. |  IN |  No |  Any |  Undefined  
ZONE2_F |  Second field for zonal control. A maximum of 202 zone combinations is permitted. |  IN |  No |  Any |  Undefined  
KEY |  Key field used to specify the field limiting the number of samples for estimation. The field must exist in the IN file. |  IN |  No |  Numeric |  Undefined  
LENGTH_F |  Field used for length weighting in IPD. The field must exist in the IN file. |  IN |  No |  Numeric |  Undefined  
DENS_F |  Field used for density weighting in IPD. The field must exist in the IN file. |  IN |  No |  Numeric |  Undefined  
SECTION |  The name of the numeric field in the STRING file holding the section identifier; used if the unfolding option is required. The default field name is SECTION. |  STRING |  No |  Numeric |  SECTION  
BOUNDARY |  The name of the numeric field in the STRING file holding the boundary identifier; used if the unfolding option is required. The default field name is BOUNDARY. |  STRING |  No |  Numeric |  BOUNDARY  
WSTAG |  Within Section TAG; used if the unfolding option is required. This is a numeric field in the STRING file, defining the stratigraphical links between hangingwall and footwall points on strings within the same section. A value of 0 or - means that the point is not linked. The default field name is WSTAG. |  STRING |  No |  Numeric |  Undefined  
BSTAG |  Between Section TAG; used if the unfolding option is required. This is a numeric field in the STRING file, defining the stratigraphical links between 2 points on strings on adjacent sections with the same BOUNDARY. A value of 0 or - means that the point is not linked. The default field name is BSTAG. |  STRING |  No |  Numeric |  Undefined  
TAG |  A numeric tag field in the STRING file; used if the unfolding option is requires. It defines both the stratigraphical links between points on strings within the same section, and between points on adjacent sections with the same BOUNDARY. A value of 0 or - means that the point is not linked. The default field name is TAG. |  STRING |  No |  Numeric |  Undefined  
  
## Parameters

**Name**| **Description**| **Required**| **Default**| **Range**| **Values**  
---|---|---|---|---|---  
DISCMETH| Cell discretisation method:| **Option**| **Description**  
---|---  
1| \- use XPOINTS , YPOINTS , ZPOINTS to define the number of points in the X,Y,Z directions  
2| \- use XDSPACE , YDSPACE , ZDSPACE to define the distance between points. The default is method (1).  
No| 1| 1,2| 1,2  
XPOINTS| Number of discretisation points in X. (1)| No| 1| Undefined| Undefined  
YPOINTS| Number of discretisation points in Y. (1)| No| 1| Undefined| Undefined  
ZPOINTS| Number of discretisation points in Z. (1)| No| 1| Undefined| Undefined  
XDSPACE| Distance between discretisation points in X if DISCMETH=2. The default gives just one point.| No| Undefined| Undefined| Undefined  
YDSPACE| Distance between discretisation points in Y if DISCMETH=2. The default gives just one point.| No| Undefined| Undefined| Undefined  
ZDSPACE| Distance between discretisation points in Z if DISCMETH=2. The default gives just one point.| No| Undefined| Undefined| Undefined  
PARENT| Flag to control parent cell estimation:| **Option**| **Description**  
---|---  
**0**|  \- Estimate into individual subcells.  
**1**|  \- Represent parent cell by a full 3D matrix of points.  
**2**|  \- Represent parent cell by a 3D matrix of points, but select only points lying within subcells. The default is (0).  
  
No| 1| 0,2| 0,1,2  
DYANKR| Flag to select whether the variogram model rotation angles should use the dynamic anisotropy option:| **Option**| **Description**  
---|---  
**0**|  \- Do not use dynamic anisotropy. Use angles VANGLEn as defined in the variogram model parameter file VMODPARM.  
**1**|  \- If the search volume uses dynamic anisotropy, then the variogram model uses the same set of angles.  
**2**|  \- Use dynamic anisotropy, but with a different set of angles from the search volume. The names of the corresponding fields are specified by fields VANGLn_F in the estimation parameter file ESTPARM.  
  
No| 1| 0,2| 0,2  
MINDISC| Minimum number of discretisation points. Only used if PARENT=2. The default is (1).| No| 1| Undefined| Undefined  
COPYVAL| Flag controlling copying of values from PROTO to MODEL if there is insufficient data to estimate them:| **Option**| **Description**  
---|---  
**0**|  \- Assign absent data value[s] in MODEL.  
**1**|  \- Copy from PROTO to MODEL. The default is (0).  
No| 0| 0,1| 0,1  
FVALTYPE| Flag for cell approximation for F values:| **Option**| **Description**  
---|---  
**0**|  \- The exact dimensions of the cell are used  
**1**|  \- Each cell is approximated by one of a discrete number of cell sizes. The default is (1).  
No| 1| 1,2| 1,2  
FSTEP| Step size for cell approximation. This is only used if FVALTYPE=2.| No| Undefined| Undefined| Undefined  
XMIN| Minimum X value for model updating. The default is the X model origin.| No| Undefined| Undefined| Undefined  
XMAX| Maximum X value for model updating. The default is the maximum X value for PROTO.| No| Undefined| Undefined| Undefined  
YMIN| Minimum Y value for model updating. The default is the Y model origin.| No| Undefined| Undefined| Undefined  
YMAX| Maximum Y value for model updating. The default is the maximum Y value for PROTO.| No| Undefined| Undefined| Undefined  
ZMIN| Minimum Z value for model updating. The default is the Z model origin.| No| Undefined| Undefined| Undefined  
ZMAX| Maximum Z value for model updating. The default is the maximum Z value for PROTO.| No| Undefined| Undefined| Undefined  
XSUBCELL| Number of subcells per parent cell in X if PROTO is empty. The default is (1).| No| 1| Undefined| Undefined  
YSUBCELL| Number of subcells per parent cell in Y if PROTO is empty. The default is (1).| No| 1| Undefined| Undefined  
ZSUBCELL| Number of subcells per parent cell in Z if PROTO is empty. The default is (1).| No| 1| Undefined| Undefined  
ALLWGTS| Flag controlling which samples are written to the sample output file if IMETHOD=9 [correlation factor method].| **Option**| **Description**  
---|---  
0| \- Only samples with non-zero weights are written to the sample output file.  
1| \- All samples in the search volume including those with zero weights are written to the sample output file.  
No| 0| 0,1| 0,1  
LINKMODE| The method by which links between strings are created; used if the unfolding option is required.| **Option**| **Description**  
---|---  
0| \- Within section links are defined by the WSTAG field, or by the TAG field if WSTAG does not exist. Between section links are defined by the BSTAG field, or by the TAG field if BSTAG does not exist.  
1| Within section links are defined automatically. Between section links are defined by the BSTAG field, or by the TAG field if BSTAG does not exist.  
2| \- Within section links are defined by the WSTAG field, or by the TAG field if WSTAG does not exist. Between section links are defined automatically.  
3| \- Within section links are defined automatically. Between section links are defined automatically. For simple structures it is not essential to define tag points on the strings; using the default value (3) ensures that automatic linking will be applied both within and between sections.  
No| 3| 0,3| 0,1,2,3  
UCSAMODE| The type of UCSA coordinate; used if the unfolding option is required. Default (2).| **Option**| **Description**  
---|---  
**1**|  \- Coordinates are normalised.  
**2**|  \- Coordinates are adjusted.  
**3**|  \- Coordinates are true length.  
**4**|  \- Coordinates are world X value.  
**5**|  \- Coordinates are world Y value.  
**6**|  \- Coordinates are world Z value.  
No| 2| 1,6| 1,2,3,4,5,6  
UCSBMODE| The type of UCSB coordinate; used if the unfolding option is required. Default (3).| **Option**| **Description**  
---|---  
**1**|  \- Coordinates are normalised.  
**2**|  \- Coordinates are adjusted.  
**3**|  \- Coordinates are true length.  
**4**|  \- Coordinates are world X value.  
**5**|  \- coordinates are world Y value.  
**6**|  \- coordinates are world Z value.  
No| 3| 1,6| 1,2,3,4,5,6  
UCSCMODE| The type of UCSC coordinate; used if the unfolding option is required. Default (2).| **Option**| **Description**  
---|---  
**1**|  \- Coordinates are normalised.  
**2**|  \- Coordinates are adjusted.  
**3**|  \- Coordinates are true length.  
**4**|  \- Coordinates are world X value.  
**5**|  \- Coordinates are world Y value.  
**6**|  \- Coordinates are world Z value.  
No| 2| 1,6| 1,2,3,4,5,6  
PLANE| The plane of the structural interpretations defined in the STRING file; used if the unfolding option is required. Default (1).| **Option**| **Description**  
---|---  
**1**|  \- Vertical sectional interpretation.  
**2**|  \- Interpretation in plan.  
No| 1| 1,2| 1,2  
HANGID| The value of the field BOUNDARY in the STRING file that defines the hangingwall of the unit, used if the unfolding option is required. It will be used if the UNITDEF file is not defined.| No| Undefined| Undefined| Undefined  
FOOTID| The value of the field BOUNDARY in the STRING file that defines the footwall of the unit, used if the unfolding option is required. It will be used if the UNITDEF file is not defined.| No| Undefined| Undefined| Undefined  
TOLRNC| Tolerance in the calculation of the UCSA coordinate expressed as a proportion of the UCSA width; used if the unfolding option is required. The default is (0).| No| 0| Undefined| Undefined  
UCSALIMT| Flag to define the limits of the UCSA coordinate if UCSAMODE=1 or 2 and TOLRNC>0\. The options below are defined in terms of the Normalized mode [UCSAMODE=1]. Default (1)| Option| Description  
---|---  
1| \- UCSA values can be less than 0 and greater than 1  
2| \- UCSA values can be less than 0. Values calculated as greater than 1 are reset to 1  
3| \- UCSA values calculated as less than 0 are reset to 0. Values can be greater than 1  
4| \- UCSA values calculated as less than 0 are reset to 0. Values calculated as greater than 1 are reset to 1  
No| 1| 1,4| 1,2,3,4  
ORGTAG| Tag number of points which define the origin surface from which the UCSB coordinate is measured. The default surface if ORGTAG is undefined (-) is created from the first points on each of the hangingwall and footwall strings.| No| -| Undefined| Undefined  
PRINT| Display control:| **Option**| **Description**  
---|---  
**0**|  Minimum output including progress message.  
**1**|  As 0 plus details of input parameters.  
**2**|  as 1 plus display of each cell value. The default is (0).  
No| 0| 0,2| 0,12  
  
## Example
    
    
    !ESTIMA &PROTO (PROTOMOD),&IN (SAMPLES),&MODEL (MODEL1),   
  
---  
      
    
    &SRCPARM (SRCPARM1),&ESTPARM  (ESTPARM2)  
      
    
    ,&VMODPARM (VMODELS),  
      
    
    *ZONE1_F (ROCK),  
      
    
    @XPOINTS=3, @YPOINTS=3, @ZPOINTS= 3  
  
Related topics and activities

  * [ESTIMATE](<estimate.md>)

  * [COKRIG Process](<cokrig.md>)

  * [Grade Estimation Introduction](<../STUDIO_RM/Grade%20Estimate%20Overview.md>)