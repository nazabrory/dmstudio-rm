![](../HeaderCell.jpg) |  Grade Estimation Examples Grade Estimation Examples  
---|---  
  
# Grade Estimation Examples

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

## Example 1 – Nearest Neighbor and Inverse Power Distance

The first example is a run of ESTIMA using the [Nearest Neighbo](<Grade%20Estimation%20Nearest%20Neighbour.md>)r and [Inverse Power Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>) methods.

The [Search Volume Parameter file](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>), SRCPARM1, is shown below. Remember that all 24 fields are compulsory. Three separate search volumes have been defined. The first two will be used for this example, and the third for example 2.

The first search ellipsoid has an axis of 100m dipping at 45o in the direction N25oE. The second axis is 40m and is aligned horizontally in the direction E25oS. The third axis of the search ellipsoid is 10m, perpendicular to the other two. The second search ellipsoid has the same rotations as the first ellipsoid, and then a third clockwise rotation of 65o is applied in the new XY plane.

|  SREFNUM |  SMETHOD |  SDIST |  Y |  Z |  ACT DIST |  TRAN DIST |  FIELD  
---|---|---|---|---|---|---|---|---  
1 |  1 |  2 |  40 |  100 |  10 |  25 |  45 |  0  
2 |  2 |  2 |  40 |  100 |  10 |  25 |  45 |  65  
3 |  3 |  2 |  70 |  60 |  80 |  12 |  34 |  56  
  
|  SAXIS1 |  SAXIS2 |  SAXIS3 |  MINNUM1 |  MAXNUM1 |  SVOLFAC2 |  MINNUM2 |  MAXNUM2  
---|---|---|---|---|---|---|---|---  
1 |  3 |  1 |  3 |  1 |  10 |  - |  - |  -  
2 |  3 |  1 |  3 |  1 |  500 |  - |  - |  -  
3 |  3 |  1 |  3 |  1 |  11 |  - |  - |  -  
  
|  SVOLFAC3 |  MINNUM3 |  MAXNUM3 |  OCTMETH |  MINOCT |  MINPEROC |  MAXPEROC |  MAXKEY  
---|---|---|---|---|---|---|---|---  
1 |  - |  - |  - |  0 |  - |  - |  - |  -  
2 |  - |  - |  - |  0 |  - |  - |  - |  -  
3 |  - |  - |  - |  0 |  - |  - |  - |  -  
  
All fields in the Estimation Parameter file, except VALUE_IN, are optional. In this example 7 fields are specified for file ESTPARM1, and so the remaining fields all take their default values.

In particular this means that ANISO=1, so the anisotropy ellipsoid for distance weighting is the same as the search ellipsoid.

|  VALUE_IN |  VALUE-OU |  NUMSAF_F |  SREFNUM |  IMETHOD |  POWER |  ADDCON  
---|---|---|---|---|---|---|---  
1 |  AU |  AU-NN |  - |  1 |  1 |  - |  -  
2 |  AU |  AU-IPD |  IPD-NUM |  2 |  2 |  1 |  5  
  
The required files for ESTIMA are shown below. No fields or parameters have been specified as they all take their defaults.

!ESTIMA &PROTO(PROTOMOD), &IN(SAMPLES), &MODEL(MOD1EST),

&SRCPARM(SRCPARM1), &ESTPARM(ESTPARM1)

## Example 2 – Ordinary Kriging

The [Search Volume Parameter file](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>) used here is the same file as used for example 1. The Estimation Parameter file, ESTPARM2, contains the following fields:

|  VALUE_IN |  VALUE-OU |  NUMSAF_F |  VAR_F |  SREFNUM |  IMETHOD |  VREFNUM |  LOG  
---|---|---|---|---|---|---|---|---  
1 |  AU |  AU-KRG |  N-KRG |  KV-KRG |  3 |  3 |  5 |  0  
2 |  AU |  AU-LOG |  N-LOG |  KV-LOG |  1 |  3 |  6 |  1  
  
The [Variogram Model Parameter file](<Grade%20Estimation%20Variograms.md>), VMODPARM is:

| VREFNUM| VANGLE1| VANGLE2| VANGLE3| VAXIS1| VAXIS2| VAXIS3| NUGGET  
---|---|---|---|---|---|---|---|---  
1| 5| 12| 34| 56| 3| 1| 3| 10  
2| 6| 25| 45| 0| 3| 1| 3| 0.1  
| ST1| ST1PAR| ST1PAR2| ST1PAR3| ST1PAR4  
---|---|---|---|---|---  
1| 1| 40| 30| 50| 20  
2| 1| 45| 35| 55| 0.2  
  
The required fields and parameters for ESTIMA are shown below. All fields and all other parameters take their defaults.

!ESTIMA &PROTO(PROTOMOD), &IN(SAMPLES), &MODEL(MOD2EST),

&SRCPARM(SRCPARM1), &ESTPARM(ESTPARM2),

@XPOINTS=3, @YPOINTS=3, @ZPOINTS=3

![](../Images/NextExercise.gif)[Proceed to the next section](<Grade%20Estimation%20Parameter%20Summary.md>) (Parameter summary)

![openbook.gif \(910 bytes\)](../Images/openbook.gif)|  Related Topics  
---|---  
| [Introducing the Grade Estimation User Guide](<Grade%20Estimate%20Overview.md>)[  
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