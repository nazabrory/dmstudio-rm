![](../HeaderCell.jpg) |  Grade Estimation - Parameter File An overview of the Grade Estimation Parameter file.  
---|---  
  
# Estimation Parameter File

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

The following table summarizes the fields in the Estimation Parameter file. Only fields VALUE_IN and SREFNUM are compulsory; if other fields are not included in the file then their default values are used.

The field names for the Zone fields are enclosed in { ... }. This signifies that this is not the actual name of the field in the file; the actual name you should use is the name of the Zone field that is included in your Input Sample and Input Prototype Model files e.g. ROCK or FLTZONE.

The default value of the VALUE_OU field is the name you have specified as the VALUE_IN value.

The Estimation Parameter File contains the following fields:

Estimation Parameter File  
---  
Field Name |  Type |  Default |  Methods |  Description  
VALUE_IN |  A-8 |  |  All |  Name of field to be estimated  
VALUE_OU |  A-8 |  {VALUE_IN} |  All |  Name of field to be created  
SREFNUM |  N |  |  All |  Search volume reference number  
{ZONE1_F} |  A or N |  |  All |  1st field controlling estimation by zone  
{ZONE2_F} |  A or N |  |  All |  2nd field controlling estimation by zone  
NUMSAM_F |  A-8 |  |  All except NN |  Field to contain number of samples used.  
SVOL_F |  A-8 |  |  All |  Field to contain dynamic search volume.  
VAR_F |  A-8 |  |  All except NN |  Field to contain variance.  
MINDIS_F |  A-8 |  |  All |  Field to contain transformed distance to nearest sample.  
IMETHOD |  N |  1 |  All |  Estimation method: 1=NN, 2=IPD, 3=OK, 4=SK, 5=ST  
ANISO |  N |  1 |  NN,IPD |  Anisotropy method:  
  
1=search vol, 2=use ANANGLE, etc  
ANANGLE1 |  N |  0 |  NN,IPD |  Anisotropy angle 1  
ANANGLE2 |  N |  0 |  NN,IPD |  Anisotropy angle 2  
ANANGLE3 |  N |  0 |  NN,IPD |  Anisotropy angle 3  
ANDIST1 |  N |  1 |  NN,IPD |  Anisotropy distance 1  
ANDIST2 |  N |  1 |  NN,IPD |  Anisotropy distance 2  
ANDIST3 |  N |  1 |  NN,IPD |  Anisotropy distance 3  
POWER |  N |  2 |  IPD |  Power of distance for IPD weighting  
ADDCON |  N |  0 |  IPD, ST |  IPD - constant added to distance ST - additive constant for lognormal  
VREFNUM |  N |  1 |  OK, SK |  Variogram model reference number  
LOG |  N |  0 |  OK, SK |  Lognormal kriging flag: 0=linear, 1=log  
GENCASE |  N |  0 |  LOG=1 |  Variogram kriging flag: 0=Rendu, 1=General Case  
DEPMEAN |  N |  0 |  LOG=1 |  Mean for lognormal variance calculation  
TOL |  N |  0.01 |  GENCASE=1 |  Convergence tolerance for log kriging  
MAXITER |  N |  3 |  GENCASE=1 |  Maximum iterations for log kriging  
KRIGNEGW |  N |  0 |  OK, SK |  Treatment of negative kriging weights: 0=keep & use, 1=ignore -ve wg samples  
KRIGVARS |  N |  1 |  Linear Kriging |  Treatment of negative kriging variance >sill: 0=keep KV>sill, 1=set KV equal to sill  
LOCALMNP |  N |  2 |  SK |  Method for calculation of local mean: 1=field from &PROTO, 2 = calculate mean  
LOCALM_F |  A-8 |  |  SK |  Name of local mean in &PROTO  
VANGL1_F |  A-8 |  (NO DEFAULT) |  OK, SK |  Name of field in &PROTO representing 1st dynamic anisotropy variogram angle  
VANGL2_F |  A-8 |  (NO DEFAULT) |  OK, SK |  Name of field in &PROTO representing 2nd dynamic anisotropy variogram angle  
VANGL3_F |  A-8 |  (NO DEFAULT) |  OK, SK |  Name of field in &PROTO representing 3rd dynamic anisotropy variogram angle  
  
![](../Images/NextExercise.gif)[Proceed to the next section](<Grade%20Estimation%20Additional%20Features.md>) (Key fields)

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