# DESURV Process

To access this process:

  * **Sample Analysis** ribbon **> > Desurvey >> Static>> Desurvey**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DESURV** and click **Run**.
  * Enter "DESURV" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DESURV>).

## Process Overview

Converts drillhole data, consisting of collar location data and assay data identified by downhole distances, into a 'desurveyed' drillhole file in which each sample is identified by its location and direction in space. In this 'desurveyed' form, each sample may be treated independently without reference to its neighbours.

The output from the **DESURV** process is in the standard sample format used elsewhere in the your application (for example compositing and cell interpolation).

The input data file must be sorted in drillhole identifier (* **BHID**) and in downhole distance (* **FROM**) order.

A progress message is displayed every 500 samples processed. 

If a survey file is used, but there is no entry for a particular hole, then that hole is assumed to be vertical, and a message to this effect is displayed.

If the field names in the &**IN1** or &**IN2** files are not the standard ones expected, then the equivalences must be given in the command line. For example, suppose that the field name for the drillhole identifier is **HOLENUM** instead of **BHID** , and the field names for **FROM** and **TO** are _from_ and _to_ (lower case), then the command would be entered as:
    
    
    !DESURV *FROM(from),*TO(to),*BHID(HOLENUM)......  
  
---  
  
### Using Downhole Survey Values

The process may optionally take a file of drillhole survey measurements taken down the hole. The positions at which these surveys were taken does not have to correspond to sample positions. 

**Note** : Up to 50,000 measurements may be taken down each hole. 

The survey file must be sorted in drillhole identifier (* **BHID**) and increasing downhole distance (* **AT**) order. If a survey file is used, but there is no entry for a particular hole, then the hole is assumed to be vertical. If a drillhole has survey data, then it must include a set of data for the collar location i.e. AT=0.

The process works by first computing a set of positions in space at known co-ordinates down each hole, and then interpolating between these known points for the top and bottom of each sample. The interpolation uses arcs of circles separately in horizontal and vertical planes.

### The SURVSMTH Parameter

When a hole sample is desurveyed the survey data (azimuth and dip) of the sample is used to locate the sample centre point in space. A desurveyed drillhole file contains a set of samples each with a calculated center point in XYZ world space.

Sometimes raw drillhole data tables to be desurveyed may contain more than one survey record within one sample, each with different azimuth and dips. Since a sample is by definition a straight line its location in space cannot be calculated using more than one survey record. The SURVSMTH parameter is used to automatically divide up samples where more than one survey records lie within a sample.

The samples are split in half until only one survey record lies within each sample. Therefore many samples may be created. The default value of SURVSMTH is 1 which will cause extra samples to be created so that no sample contains more than one survey record within its **FROM** and TO values. For no extra samples to be created the SURVSMTH parameter should be set to zero.

If the SURVSMTH parameter is set to zero and a sample does contain more than one survey record not all survey records will be taken into account. Traditionally this has been resolved by first compositing the samples to reduce their lengths. The SURVSMTH parameter avoids this requirement.

It is often the case that the first one or two samples in exploration holes contain more than one survey record because they are relatively long. This is because sample divisions have not had to have been created through assay and lithological identification near the surface.

### The DESURVMD Parameter

**DESURV** is used to locate points on samples accurately in space. The interpolation uses arcs of circles so straight line samples. The **DESURVMD** parameter specifies whether the sample centre points or the sample end points are located on the arcs. Possible vales are 0 or 1. The default is 1, to accurately locate the sample centre points.

> **=0** : To accurately locate sample END points on the desurveyed arcs. This may be preferred for visualisation as it will minimise gaps between the sample ends.
> 
> **=1** : To accurately locate sample CENTRE points on the desurveyed arcs. This is usually used for input into grade estimation as its the sample centre points that are used for grade estimation.

It should be noted that for the majority of data sets the difference between the methods will be immaterial.

### The ENDPTS Parameter

If the **ENDPTS** parameter is set to 1, the sample end points are recorded in the output file in the 6 fields [XYZ]START and [XYZ]END. The output file will still contain the standard sample centre point output for a desurveyed drillhole file in the fields X, Y and Z.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Data file of downhole distances, sorted on **BHID** and **FROM**. Expects fields **BHID** , **XCOLLAR** , **YCOLLAR** , **ZCOLLAR** , **FROM** , **TO** ; optional **BRG** , **DIP**. |  Input |  Yes |  Downhole Sample  
IN2 |  Survey data file, sorted on **BHID** and **AT**. Expects fields **BHID** , **AT** , **BRG** , **DIP**. If a borehole has survey Data, then it must include a record for the collar location, i.e. AT=0 |  Input |  No |  Downhole Survey  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Drillhole |  Output sample data file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
BHID |  Drillhole identifier. |  IN1 |  No |  Any |  BHID  
XCOLLAR |  X co-ordinate of drillhole collar. |  IN1 |  No |  Numeric |  XCOLLAR  
YCOLLAR |  Y co-ordinate of drillhole collar. |  IN1 |  No |  Numeric |  YCOLLAR  
ZCOLLAR |  Z co-ordinate of drillhole collar. |  IN1 |  No |  Numeric |  ZCOLLAR  
FROM |  Downhole distance to sample top. |  IN1 |  No |  Numeric |  FROM  
TO |  Downhole distance to sample bottom. |  IN1 |  No |  Numeric |  TO  
AT |  Downhole distance to survey point. |  IN2 |  No |  Numeric |  AT  
BRG |  Bearing of drillhole. |  IN2 |  No |  Numeric |  BRG  
DIP |  Dip of drillhole. |  IN2 |  No |  Numeric |  DIP  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SURVSMTH |  =0 to prevent samples being added to the output file. =1 to add samples where there are more than one survey record per sample. (1). When a hole sample is desurveyed the survey data (azimuth and dip) of the sample is used to locate the sample centre point in space. A desurveyed drillhole file contains a set of samples each with a calculated center point in XYZ world space. Sometimes raw drillhole data tables to be desurveyed may contain more than one survey record within one sample, each with different azimuth and dips. Since a sample is by definition a straight line its location in space cannot be calculated using more than one survey record. The SURVSMTH parameter is used to automatically divide up samples where more than one survey records lie within a sample. The samples are split in half until only one survey record lies within each sample. Therefore many samples may be created. The default value of SURVSMTH is 1 which will cause extra samples to be created so that no sample contains more than one survey record within its **FROM** and **TO** values. For no extra samples to be created the SURVSMTH parameter should be set to zero. If the SURVSMTH parameter is set to zero and a sample does contain more than one survey record not all survey records will be taken into account. Traditionally this has been resolved by first compositing the samples to reduce their lengths. The SURVSMTH parameter avoids this requirement. It is often the case that the first one or two samples in exploration holes contain more than one survey record because they are relatively long. This is because sample divisions have not had to have been created through assay and lithological identification near the surface. | No |  1 | 0,1 | 0,1  
DESURVMD |  Locate sample centers or end points on the desurveyed arcs. The default is 1, to accurately locate the sample center points. =0 : To accurately locate sample **END** points on the desurveyed arcs.  =1 : To accurately locate sample **CENTER** points on the desurveyed arcs.  | No | 1 | 0,1 | 0,1  
ENDPTS |  Write out fields containing the sample end point coordinates. The default value is 0, to not write out the sample end points. =0 : Do not write sample end points to the output file.  =1 : Write out numeric fields [**XYZ**]**START** and [**XYZ**]**END** containing the sample start and end point coordinates. | No | 0 | 0,1 | 0,1  
PRINT |  >=2 to display each output record and sample data file DD (0). | No | 0 | 0,2 | 0,1,2  
  
## Example
    
    
    !DESURV    &IN1(BHOLES),   
  
---  
      
    
     &OUT(BHOLES.D)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 107 <<< ( fileno) IN DESURV |  The survey data file must be in BHID, AT order. Fatal; the process is exited.  
>>> ERR 130 <<< ( fieldno) IN DESURV |  Missing compulsory field (number fieldno) in sample data file which must contain at least BHID, XCOLLAR, YCOLLAR, ZCOLLAR, FROM and TO. Fatal; the process is exited.  
>>> NO SURVEY DATA - HOLE ASSUMED VERTICAL - llllllll aaaaaaaa....... |  llllllll is the *BHID local name (e.g. BHID) and aaaaaaaa (up to 40 chars) is the actual name (e.g. BH0003). The hole will be taken as vertical.  
>>> MORE THAN 2000 SURVEY POINTS <<< |  Only the given number 2000 will be processed, the rest ignored. If the BRG and DIP fields appear on the input sample file this message will appear if the number of samples exceeds 2000.