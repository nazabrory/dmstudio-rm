![](../HeaderCell.jpg) |  Grade Estimation Parameter Summary A summary of the parameters associated with Grade Estimation  
---|---  
  
# Parameter Summary

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

A summary of all parameters is given in the following table. All parameters are optional, and if not specified will take their default values:

ESTIMA - Summary of Parameters  
---  
Parameter |  Default |  Method(s) |  Description  
XSUBCELL |  1 |  All |  Number of subcells in X if &PROTO is empty  
YSUBCELL |  1 |  All |  Number of subcells in Y if &PROTO is empty  
ZSUBCELL |  1 |  All |  Number of subcells in Z if &PROTO is empty  
DISCMETH |  1 |  IPD, OK, SK |  Cell discretisation method:

  * 1=use @XPOINTS etc
  * 2=use @XDSPACE etc

  
XPOINTS |  1 |  @DISCMETH=1 |  Number of discretisation points in X  
YPOINTS |  1 |  @DISCMETH=1 |  Number of discretisation points in Y  
ZPOINTS |  1 |  @DISCMETH=1 |  Number of discretisation points in Z  
XDSPACE |  1 pt at cell centre |  @DISCMETH=2 |  Distance between discretisation points in X  
YDSPACE |  1 pt at cell centre |  @DISCMETH=2 |  Distance between discretisation points in Y  
ZDSPACE |  1 pt at cell centre |  @DISCMETH=2 |  Distance between discretisation points in Z  
PARENT |  0 |  All |  Parent cell flag:

  * 0=estimate individual cells
  * 1=parent, all disc.pts
  * 2=parent, select disc.pts

  
MINDISC |  1 |  @PARENT=2 |  Minimum number of discretisation points  
XMIN |  &PROTO min X |  All |  Minimum X value for model updating  
XMAX |  &PROTO max X |  All |  Maximum X value for model updating  
YMIN |  &PROTO min Y |  All |  Minimum Y value for model updating  
YMAX |  &PROTO max Y |  All |  Maximum Y value for model updating  
ZMIN |  &PROTO min Z |  All |  Minimum Z value for model updating  
ZMAX |  &PROTO max Z |  All |  Maximum Z value for model updating  
COPYVAL |  0 |  All |  Copy flag:

  * 0=absent data in insufficient data
  * 1=copy existing value(s) to Output Model

  
FVALTYPE |  1 |  OK, SK |  F value approximation:

  * 1=use exact cell dimensions
  * 2=approximate cell dimensions

  
FSTEP |  1 |  @FVALTYPE=2 |  Step size for cell approximation for F value  
LINKMODE |  3 |  Unfold |  Method of defining string linking  
UCSAMODE |  2 |  Unfold |  The type of UCSA coordinate  
UCSBMODE |  3 |  Unfold |  The type of UCSB coordinate  
UCSCMODE |  2 |  Unfold |  The type of UCSC coordinate  
PLANE |  1 |  Unfold |  The plane of the structural interpretations  
HANGID |  - |  Unfold |  The value of hangingwall field in &STRING file  
FOOTID |  - |  Unfold |  The value of footwall field in &STRING file  
TOLRNC |  0 |  Unfold |  Tolerance in the calculation of UCSA coordinate  
ORGTAG |  - |  Unfold |  Tag number defining origin of UCSB axis  
PRINT |  0 |  All |  Flag controlling quantity of displayed output:

  * 0=minimum
  * 1=medium
  * 2=maximum

  
ECHO |  0 |  All |  Flag controlling output sent to print file:

  * 0=do not send to file
  * 1=send to file

  
  
## Files and Fields

A summary of all the files used by ESTIMA is given in the following table:

File Name |  Input/Output |  Mandatory/Optional |  Description  
---|---|---|---  
PROTO |  I |  M |  Input prototype model  
IN |  I |  M |  Sample data file  
SRCPARM |  I |  M |  Search volume parameter file  
ESTPARM |  I |  M |  Estimation parameter file  
VMODPARM |  I |  O |  Variogram model parameter file  
STRING |  I |  O |  Unfolding strings file  
MODEL |  O |  M |  Output model  
SAMPOUT |  O |  O |  Sample output file  
  
Most of these files have been described in detail in the previous sections. A brief description of the Input Prototype Model and Sample Data files is given here:

## Input Prototype Model

This is a standard Datamine model file containing the 13 compulsory fields. In addition it may contain the following three fields:

  * LOCALM_F: the local mean for simple kriging

  * ZONE1_F: first field for zonal control

  * ZONE2_F: second field for zonal control

## Sample Data File

This file must contain the X, Y and Z coordinates of the samples, and at least one grade field.

ESTIMA expects the names of the coordinate fields to be X, Y and Z. However, if other names have been used then they can be specified, for example:

*X(EAST), *Y(NORTH), *Z(RL)

The name(s) of the grade field(s) are defined using the fields VALUE_IN in the Estimation Parameter file. The other fields (all optional) in the Sample Data file are:

  * ZONE1_F: first field for zonal control

  * ZONE2_F: second field for zonal control

  * KEY: field used to restrict samples per keyfield

  * LENGTH_F: field for Inverse Power Distance length weighting

  * DENS_F: field for Inverse Power Distance density weighting

These fields are specified in the same way as specifying coordinates e.g. *KEY(BHID).

However, please note that if there was a field named KEY in the Sample Data file and MAXKEY was set to 1 or more in the Estimation Parameter file, then the process would use the field KEY for restricting samples even if *KEY(KEY) was not specified.

A similar situation to the KEY field example applies to the other fields, which is why they have been given names which are unlikely to occur in normal use.

## Summary of Fields

ESTIMA uses field naming conventions. The fields which are prompted for are shown below. Note that all fields are optional:

Parameter| Default| Method(s)  
---|---|---  
IN| X| X coordinate of sample data  
Y| Y coordinate of sample data  
Z| Z coordinate of sample data  
KEY| Key field used to restrict samples for estimation  
LENGTH_F| Field used for length weighting for IPD  
DENS_F| Field used for density weighting for IPD  
IN, PROTO, MODEL, ESTPARM| ZONE1_F| First field for zonal control  
ZONE2_F| Second field for zonal control  
STRING| SECTION| Section identifier for unfolding  
BOUNDARY| Boundary identifier for unfolding  
WSTAG| Within section tag  
BSTAG| Between section tag  
TAG| Tag field  
  
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
Grade Estimation System Limits](<Grade%20Estimation%20Additional%20Features.md>)[  
Grade Estimation References  
  
ESTIMA command Help   
ESTIMATE command Help  
The Estimate dialog  
VARFIT Command Help](<Grade%20Estimation%20References.md>)