# TRIVAL Process  
  
To access this process:

  * **Wireframe** ribbon **> > Process | Wireframe Processes | Evaluate Against Wireframe**.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, select **TRIVAL** and click **Run**.
  * Enter "TRIVAL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **TRIVAL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TRIVAL>).

## Process Overview

Evaluates a standard Datamine block model against a triangulated wireframe model, reporting on the contents of closed wireframes or the reserves below or above a single-surface (digital terrain model) wireframe.

Trival generates a **RESULTS** file of reserves from an orebody model and an input wireframe; and optionally produces an output orebody model in which a proportion **MINED** field is updated. Evaluation is normally by partial block, but can optionally be done on a full-block basis in which any block with a **MINED** proportion greater than 0.5 is marked as wholly **MINED** , any proportion less than 0.5 is treated as zero. Results can be classified by XY, XZ, or YZ planes. The results file can be read by [TABRES](<tabres.md>) to produce various reserve tabulations.

The input wireframe triangle file must contain an **SID** (Surface IDentification) field. If an 'upper' digital terrain model is supplied (with **SID** values all +1) then the model created will fill cells below the surface. Inversely, if all **SID** values are -1, then cell filling will be done above the surface. For solid wireframe models (in which **SID** values of +1 represent upward facing surfaces and -1 represent lower facing surfaces), cells are filled inside the wireframe. Any number of separate zones may be handled within one run of **TRIVAL** , provided they are all held within the same pair of &**WIREPT** , &**WIRETR** files. The SID field is produced automatically by **TRIANR** (set to +1 or -1 at user option).

### Input and Output Models

The input model is in standard Datamine model file format, and may contain cells and sub-cells, in any order; the model does not have to be sorted on IJK to be processed by **TRIVAL**. The fraction of the cell or sub-cell mined may be stored in the **MINED** field of the optional output model file, as a value in the range 0 to 1. The output model file will be an exact copy of the input file, with the **MINED** field added if it did not already exist in the input file. The output model file may be the same as the input model file (in-place updating) if the **MINED** field existed in the input file.

### Balancing Volumes

**TRIVAL** produces for each pass through the model a balancing volume record in the results file; the balancing volume recorded (NOT the same as that produced by **[MODRES](<modres.md>)**) is the total volume of the model less the volume intersected by the wireframe zone evaluated.

### Densities

In computation of tonnages from volumes, any **DENSITY** field within the input model is used. If the **DENSITY** field exists, then unmodelled regions will use the default value of the **DENSITY** field. If the **DENSITY** field does not exist, then an overall density may be supplied by use of the @**DENSITY** parameter. If this was not supplied, then the density used is 1.0.

### Passes through the Model File

The process reads in one wireframe zone at a time (as identified by the **ZONE** field if present in the triangle file). For each wireframe zone **TRIVAL** reads through the entire model and records its evaluation against each separately. If successive zones overlap, or the input model already contains **MINED** values greater than 0, there are two ways in which the evaluation may be recorded in the **RESULTS** file and the output **MINED** field.

**Note** : Up to 2000 unique zone values can exist in the specified **ZONE** field.

These two options are controlled by the supplied value of the optional @**INCRMENT** parameter. Either it will be considered that all mining is additive if @**INCRMENT** is set to 0, (i.e. that there are no overlapping zones), in which case any cell already partly mined will have the full volume of the current evaluation added to the amount mined - subject to a maximum proportion mined of 1.0. Alternatively, if @**INCRMENT** is set to 1, it will be considered that mining is incremental, and that successive zones are to be considered as mine expansions, and overlap totally. In this case, a partly mined cell will be output with a proportion mined which is the maximum of the previous and current proportions. In this case, naturally, if the current proportion mined is less than the previous, there will be no evaluated volume in the results file for the cell.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
MODELI |  Model file for evaluation. Must contain at least the fields XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK. |  Input |  Yes |  Block Model  
WIRETR |  Input wireframe triangle file. |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
RESULTS |  Output |  Yes |  Undefined |  The output results file, in a format suitable for input into the TABRES process  
MODELO |  Output |  No |  Block Model |  Optional output model file. This may be the same as the input, if the MINED field exists in the input file. The MINED field will be created in the output file if it does not exist.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
ZONE |  Optional zone identifier field (numeric or single-word alpha) in the WIRETR triangle file, defining individual wire-frame zone models. This field will be added to the results file. Up to 2000 zone values can exist in the specified column. |  IN |  No |  a/n |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DENSITY |  Set required density value. This will only be used if there is no DENSITY field in the input model. If there is no DENSITY field, and no DENSITY parameter, then a value of 1.0 is used. |  Yes |  |  |   
FULLCELL |  = 0 : partial cell evaluation = 1 : whole cell evaluation in place of partial cell evaluation (0).. |  No |  0 |  0,1 |  0,1  
MINE |  Optional; if non-zero, output proportion mined in MINED field of MODELO file (0). |  No |  0 |  0,1 |  0,1  
PLANE |  Optional alpha parameter defining slice orientation to be used in classification of results 'XY', 'XZ', or 'YZ'. |  No |  "XY" |  |  XY, YZ, XZ  
INCRMENT |  (0) If non-zero, mining is assumed to be incremental, and for any (sub-)cell the amount mined in any pass must be greater than the total mined so far for it to be recorded. If zero, mining is assumed to be additive, subject to a total mined fraction of 1. |  No |  0 |  0....1 |  0,1  
MODLTYPE |  Type of wireframe model to be evaluated; one of the following options:- =1 : solid 3d, interior to be evaluated. =3 : surface, cells to be evaluated below [for XY], to south [for XZ], or to west [for YZ]. =4 : surface, cells to be evaluated above [for XY], to north [for XZ], or to east [for YZ]. |  No |  0 |  |  1, 3, 4  
CHKOVLAP |  Control checking of overlapping triangles. This applies only to model types of 3 and 4. If set to 1 then checking of triangle overlaps is performed. If set to zero then no checking will occur. Checking should be done where DTMs curve over themselves as in some seam models. Checking can be turned off for DTMs where this is known not to occur, such as in an open pit wireframe. If checking is turned off the process will run faster. (1). |  No |  0 |  0,1 |  0,1  
CHECKROT |  Set to 1 to automatically check for and correctly process rotated models. The default value is zero. If this is not set to 1 and the model is rotated then the wireframe points need to be transformed into the model coordinate space using CDTRAN before running TRIFIL. |  No |  0 |  0,1 |  0,1  
NOSID |  |  Option |  Description  
---|---  
1 |  Disables checking of SIDs for increased speed. Use for single surfaces only.  
No |  0 |  0,1 |  0,1  
PRINT |  =1 : ; Show a line for each cell evaluated in each perimeter.(0). |  No |  0 |  0,1 |  0,1  
  
### Interactive Prompts

ENTER EVALUATION PARAMETERS  |  Standard evaluation consists of mean grades and tonnages for each <bench or section> Enter Y or Yes (or <RETURN>) for standard evaluation: Enter N or No to specify evaluation parameters. >YES/NO > Y or Yes or <return> to use these; N or No to enter parameters.  
---|---  
ROCKTYPE CLASSIFICATION  |  Each evaluation (within a perimeter on a <bench or section> may be classified by rocktype. There are two types of classification possible:- By ore, waste, air, stockpile etc. or by given values of the rocktype field: Results may only be classified by rocktype if there is a suitable rocktype field. Enter Y or Yes (or <RETURN>) for classification. Enter N or No to omit classification by rocktype  
|  If Y or Yes:  
|  Enter name of field defining rocktype:-  
|  >FIELD > Enter required field name.  
CLASSIFICATIONS POSSIBLE ON FIELD nnnnnnnn OF TYPE n  |  You may either specify up to 20 values of the field, each of which will be separately identified in the results: or you may classify rocktypes as ore, waste, air, stockpile, etc. Enter Y or Yes (or <RETURN>) to classify by ore etc: Enter N or No to classify by rocktype field value.  
If Y, Yes or <return>; |   
CLASSIFICATION BY ORE, WASTE ETC.  |  Enter pairs of values in form:- <rocktype value>,<class> where the class may be one of the following:- ORE WSTE AIR S1 S2 S3 S4 S5 S6 S7 The rocktype field is of type n End by entering (blank) or (blank,blank) Maximum entries is 40: unnamed rocktypes will be classified as waste (WSTE). >VALUE,CLASS> Enter value,class; terminate by blank.  
If N or No: |   
CLASSIFICATION BY VALUES OF FIELD nnnnnnnn  |  Enter one value per line of this field of type n Terminate with (blank) or (blank,blank) Maximum number or entries is 20 >VALUE > Enter required rocktype field value; terminate with blank.  
|  After rocktype classification, or if no rocktype classification, and if the model contains grade fields:  
GRADE INTERVALS  |  If no grade intervals are specified then means are calculated. Otherwise you may specify grade ranges of a named numeric field. Enter Y or Yes (or <RETURN>) to specify grade ranges. Enter N or No to compute means only. If Y, Yes or <return>; Enter name of main grade field. >FIELD > Enter field name.  
GRADE INTERVALS FOR MAIN GRADE nnnnnnnn  |  Enter (lower,upper) limits separated by commas: E.g. 0.1,0.25 <RETURN>. The lower bound is excluded and the top included in the range. Enter 0,0 (or blank) to end. Max bins 20 Under- and over-flow bins are added automatically. >LOWER,UPPER> e.g. .5,.6; 0,0 to end.  
|  Is this satisfactory? Enter Y or Yes (or <RETURN>) if so: Enter N or No to restart entries.  
  
## Example
    
    
    !TRIVAL    &PROTO(PROTOMOD),&MODELI(MODTOPO),&WIREPT(TOPOPT),          
  
---  
      
    
    &WIRETR(TOPOTR),&RESULTS(RESULTS),*ZONE(ROCK),@MODLTYPE=1,          
      
    
    @PLANE='XY'  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> NO DATA IN INPUT FILE <<< >>> ERR 136 <<< ( n) IN TRIFIL |  The input wireframe point data file has no data. Fatal; the process is exited.  
>>> MISSING OR ALPHA FIELDS IN MODEL PROTOTYPE <<< >>> ERR 142 <<< ( n) IN TRIFIL |  The input model file has no data. Fatal; the process is exited.  
>>> MISSING OR ALPHA FIELDS IN WIREPT FILE <<< >>> ERR 145 <<< ( n) IN TRIFIL |  Fatal; the process is exited.  
>>> INPUT AND OUT MODEL FILE MAY NOT BE SAME <<< >>> IF NEW FIELDS (E.G. MINED) MUST BE CREATED IN OUTPUT FILE <<< >>> ERR 123 <<< ( 0) IN TRIVAL |  The name of the &**MODELI** file must not be the same as the &**MODELO** file if new fields for example, **MINED** , **ZONE** are being created in the output file. Fatal; the process is exited.