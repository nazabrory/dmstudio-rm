# SELPER Process

To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Select in 3D Perimeters**.

  * Enter "SELPER" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SELPER** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SELPER>).

## Process Overview

Select records which lie on or within a perimeter and copies them to an output file.

The process performs a similar function to **[SELEXY](<selexy.md>)** but includes the following additional features:

  * both the input files use 3 dimensional coordinates.

  * perpendicular search distances are used to define the influence of each perimeter.

  * if the input data file is in desurvey format then samples can be clipped at perimeter limits.

The output file will contain all the fields from the input file plus any attribute fields from the perimeter file. The attribute fields from the first point of each perimeter are used. Attribute values from the second and subsequent points of a perimeter are ignored.

The process may be used in place with the output file the same as the input file. In this case the attribute fields must already exist in the input file, and they will be updated if the records lies within a perimeter.

If the input and output files are different and a data record lies within more than one perimeter, then multiple copies of the record will appear in the output file. If the operation is carried out in place then the record will be assigned attribute values of the last perimeter within which it lies. Hence in the latter case the order of the perimeters is important.

Both the perimeters in the &**PERIMIN** file and the data in the &IN file use 3-dimensional coordinates. The perimeters must lie in one of the orthogonal planes (one of **XP, YP** or **ZP** must be constant). The process calculates the plane for each perimeter, and uses the appropriate pair of coordinates from the records in the &IN file. e.g. if the perimeter is an East-West section (XZ plane) then the X and Z fields from the &IN file are used to determine whether the record lies within the perimeter.

If a perimeter does not lie within one of the orthogonal planes then a warning message is displayed and the perimeter is ignored.

Search distances must be supplied defining the maximum perpendicular distances of the data record from the plane of the perimeter. Only records lying both within the perimeter and within the search distances will be processed. The search distance DPLUS is measured in the increasing direction of the perpendicular axis, and **DMINUS** in the decreasing direction.

**DPLUS** and **DMINUS** may be defined as parameters or as fields in the &**PERIMIN** file. If both are defined then the field values take priority over the parameters. **DPLUS** and **DMINUS** values of zero are not permitted and if supplied they will be substituted by 0.001. Where the **DPLUS** or **DMINUS** values are left undefined the process will default to an infinite search distance.

If the input file is a drillhole sample file and contains fields **A0, B0** and **LENGTH** , then the samples may optionally be clipped at the perimeter boundary and at the **DPLUS** and **DMINUS** limits. This is controlled by the parameter @**CLIP**. If clipping is selected and the input file also contains **FROM** and **TO** fields then they will be adjusted appropriately.

The process reads in one perimeter at a time and checks each sample against that perimeter. Perimeters may be either open or closed. There is no practical limit on the number of points in a perimeter, the number of perimeters, or on the number of samples in the input files.

If the parameter **@CLOSE** is set to 1, the input perimeters may be either open or closed and any open strings will be closed for the purpose of processing. If **CLOSE** is set to zero then open (non-closed) perimeters are ignored. The default is for all perimeters to be processed: **CLOSE** =1. A tolerance based on the scale of the coordinates is used to test whether the first and last point of a perimeter are the same.

By default the process checks that each sample lies on or inside a perimeter. Optional parameter @**OUTSIDE** can be used to select only samples lying outside the perimeter. This only works if the perimeter file only contains one perimeter, therefore a single perimeter must be selected by using retrieval criteria or by using the optional parameter @**PVALUE** to define the **PVALUE** of the required perimeter within the &**PERIMIN** file. 

A single perimeter may be selected by using retrieval criteria or by using the optional parameter @**PVALUE** to define the **PVALUE** of the required perimeter within the &**PERIMIN** file. When **OUTSIDE** is being used to select outside points, if a single perimeter has not been specified using **PVALUE** or retrieval criteria, **SELPER** will automatically stop after the first available perimeter has been processed.

Setting parameter **ALLPTS** =1 can be used to copy all input points to the output file. This is useful for flagging points within a data set by perimeter attributes but maintain the whole data set, for example flagging cells in a block model depending on which perimeter they are inside. If **ALLPTS** =1 then a point can only be copied to the output file once, regardless of how many perimeters it is inside. The output point will have the attribute values taken from the first perimeter in which it is found to be inside. If no attribute values are specified and **ALLPTS** =1 then the output file will be identical to the input file.

Note: [SELEXY](<selexy.md>) is a similar process to **SELPER** but **SELPER** has additional options.

## Input Files

Name| Description| I/O Status| Required| Type  
---|---|---|---|---  
IN| Input file for selection. Must have explicit numeric fields X , Y and Z. If sample clipping is to be used then it must also contain A0, B0 and **LENGTH** fields.| Input| Yes| Undefined  
PERIMIN| Perimeter file to control selection. The fields required are **XP, YP, ZP, PTN** and **PVALUE** (standard perimeter format). The file may also contain fields **ATTRIB1** -**5** which can be carried across to the output file. The value of these fields at the first point is used.| Input| Yes| String  
  
## Output Files

Name| I/O Status| Required| Type| Description  
---|---|---|---|---  
OUT| Output| No| Undefined| Output file containing all records lying within (or optionally outside) the perimeter. The **OUT** file may be the same as the **IN** file for in-place operations, unless extra fields ( **ATTRIB1** -**5**) from the perimeter file are being added.  
  
## Fields

Name| Description| Source| Required| Type| Default  
---|---|---|---|---|---  
X| Field in **IN** file defining the X co-ordinate.| IN| Yes| Numeric| Undefined  
Y| Field in **IN** file defining the Y co-ordinate.| IN| Yes| Numeric| Undefined  
Z| Field in **IN** file defining the Z co-ordinate.| IN| Yes| Numeric| Undefined  
DPLUS| Field in **PERIMIN** defining the search distance measured in the increasing direction of the perpendicular axis. The default field name is **DPLUS** , which will be used if it exists in the **PERIMIN** file.| PERIMIN| No| Numeric| DPLUS  
DMINUS| Field in **PERIMIN** defining the search distance measured in the decreasing direction of the perpendicular axis. The default field name is **DMINUS** , which will be used if it exists in the **PERIMIN** file.| PERIMIN| No| Numeric| DMINUS  
ATTRIB1| Field from the perimeter file to be placed into the output file for all records which are selected. This may be a multi-word alpha field.| PERIMIN| No| Any| Undefined  
ATTRIB2| Second field from the perimeter file to be placed into the output file for all records selected by the perimeter.| PERIMIN| No| Any| Undefined  
ATTRIB3| Third field from the perimeter file to be placed into the output file for all records selected by the perimeter.| PERIMIN| No| Any| Undefined  
ATTRIB4| Fourth field from the perimeter file to be placed into the output file for all records selected by the perimeter.| PERIMIN| No| Any| Undefined  
ATTRIB5| Fifth field from the perimeter file to be placed into the output file for all records selected by the perimeter.| PERIMIN| No| Any| Undefined  
  
## Parameters

Name| Description| Required| Default| Range| Values  
---|---|---|---|---|---  
OUTSIDE|  | Option| Description  
---|---  
1| Copies only those records of a file lying outside the perimeter (0).  
No| 0| 0,1| 0,1  
PVALUE| Set to the required PVALUE to select a particular perimeter from PERIMIN. If PVALUE is not set, then all perimeters will be processed.| No| Undefined| Undefined| Undefined  
CLIP| | Option| Description  
---|---  
1| Clip samples at the perimeter boundary (0). If sample clipping is to be used then it must also contain A0, B0 and LENGTH fields.  
No| 0| 0,1| 0,1  
DPLUS| The search distance measured in the increasing direction of the perpendicular axis.| No| Undefined| Undefined| Undefined  
DMINUS| The search distance measured in the decreasing direction of the perpendicular axis.| No| Undefined| Undefined| Undefined  
CHECKROT| Choose if you wish to automatically process rotated models or not:

  * 0: do NOT automatically check for a rotated model prototype. Use this setting if the input model is rotated and the input model cells are already transformed into the perimeter coordinate system. 
  * 1: automatically check for a rotated model prototype and internally transform the model cell centres accordingly. 

| No| 0| 0,1| 0,1  
IJKSORT| This can be used to automatically sort block models when selecting model cells within perimeters

  * 0: do NOT automatically sort the output file by **IJK** if it has an **IJK** field. 
  * 1:automatically sort the output file by **IJK** if it has an **IJK** field. 

| No| 0| 0,1| 0,1  
PRINT| >=1 Display summary statistics for each perimeter (0).| No| 0| 0,1| 0,1  
  
## Example
    
    
    !SELPER &IN (ASSAYS.D), &PERIMIN (PERIM), &OUT (SUBSET),  
  
---  
      
    
    *X (X), *Y (Y), *Z (Z), *ATTRIB1 (ZONE),  
      
    
    *ATTRIB2 (ROCKTYPE), @CLIP=1, @PRINT=1.  
  
## Error and Warning Messages

Message| Description| Solution  
---|---|---  
>>> ERROR IN &PERIMIN FIELDS <<<| A field is missing or contains an invalid data type (i.e. alphanumeric instead of numeric). | Check the fields XP, YP, ZP, PVALUE, PTN, and optionally DPLUS, DMINUS in the &PERIMIN file.  
>>> ERROR IN &IN FIELDS <<<| A field is missing or contains an invalid data type (i.e. alphanumeric instead of numeric).| Check the *X, *Y, *Z fields in the &IN file.  
>>> CLIPPING CANNOT BE DONE IN-PLACE <<<| If the clipping option is selected (@CLIP=1) an &OUT file must be defined.| Define an output file &OUT.  
>>> ATTRIBUTE FIELDS CANNOT BE COPIED IN-PLACE <<<| If copying is to be done in-place (i.e. the &OUT and &IN files are the same) the attribute fields being copied from the &PERIMIN file must already exist in the &IN file.| Check that the selected attribute fields exist in the &PERIMIN file.  
>>> TOO MANY POINTS IN PERIMETER - <<<| There are too many points in a perimeter in the &PERIMIN file. The storage space allocated during process installation is insufficient.| Either reduce the number of points in the perimeter or increase the allocated storage space for the maximum number of points per string (perimeter).  
  
Related topics and activities

  * [SELEXY Process](<selexy.md>)