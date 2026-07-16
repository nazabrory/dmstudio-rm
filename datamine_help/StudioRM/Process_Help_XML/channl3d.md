# CHANNL3D Process

To access this process:

  * **Sample Analysis** ribbon **> > Desurvey >> Channels**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CHANNL3D** and click **Run**.
  * Enter "CHANNL3D" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CHANNL3D>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

CHANNL3D converts a set of Channel Sample data and Channel Survey data into a 'desurveyed' Static Drillholes file in which each sample is identified by its location (X,Y,Z coordinates) and direction (azimuth and dip) in space. This is the same format as created by the [HOLES3D](<holes3d.md>) process for drillhole data.  

The input data consists of one survey file and one or more sample files. If two or more Channel Sample files are specified (maximum 6) then they are merged so that all divisions of all sets of samples are maintained. A typical use of merging is to add an assay file to a lithology file, where the lithology intervals do not match the assay sample boundaries. Another example is to add absent data samples into channels by making the second file a single record per channel defining the total channel length.

The output from the CHANNL3D process is in the standard Drillhole format which is used extensively elsewhere in Studio. For example, the channels can be viewed interactively, composited along the channel, and used to interpolate grades into a block model.  

## Using Channel Survey Data

The Channel Survey data file is compulsory and must contain at least two survey points for each channel. If survey data is not included for a channel or there is insufficient data then an error will be reported.

Survey data consists of a channel identifier (BHID) and the coordinates (XPT, YPT, ZPT) of the survey point. The first survey point for each channel must be at the start of the channel. The positions at which the survey readings are recorded does not have to correspond to sample positions.

The survey data for each channel must be sorted on distance along the channel from the start of the channel. However it is not necessary to include this distance as a field in the survey data file.

The process works by first converting the survey file to sample format by the addition of **FROM** and **TO** fields, thus creating a set of pseudo samples corresponding to the intervals between successive survey points. This is then combined with the sample file(s) using the hole merge ([HOLMER](<holmer.md>)) process so that the samples are split at all sample endpoints. The coordinates of the centre of each sample are then calculated by linear interpolation between the survey points on either side of the sample. The azimuth (**A0**) and dip (**B0**) fields are also calculated from the survey data.

If the sample data extends beyond the survey data then the process will optionally extrapolate the survey data using the azimuth and dip of the last survey sample of the channel. This is controlled by parameter EXTEND; if set to 1 then the output channel file will be extended to include all sample data; if set to 0 then the output channel file will terminate at the final survey point.

The process will optionally calculate the XYZ coordinates of the start and end of each sample. This is controlled by parameter ENDPOINT, which if set to 1 will create the six extra fields.

As well as creating the desurveyed channel file, **OUT** , the process will optionally create two other files, CHANSMRY and ERRORS, which assist in validating the input data. These files are described below.  

## Optional Output File \- CHANSMRY

The CHANSMRY file contains a single record summary of the input data for each channel. The fields include:

  * BHID \- channel identifier
  * SURVPTS \- number of survey points for each channel
  * SAMPLEi \- number of sample records in SAMPLEi input file(s) for each channel
  * SAMPLENG \- maximum length of sampling over all ( 1 6) input sample files
  * SURVLENG \- cumulative length over all survey points
  * DIFFLENG \- difference in length between SAMPLENG and SURVLENG
  * GAP_i \- length of missing samples (FROM previous TO) in input sample file i, i=1,6
  * MAX_TO_i \- maximum TO value in input sample file i, i=1,6
  * SURVFILE \- name of input survey file
  * SMPiFILE \- name of input sample file i, i=1,6

Although this file is optional it is recommended that it is created and checked. In particular if the SURVPTS value is less than 2 then the channel will not be included in the OUT file. Also if any of the GAP_i values are non zero then this indicates that samples are missing from sample file SAMPLEi which may indicate that the data needs to be checked.  

Optional Output File ERRORS

The ERRORS file reports inconsistent FROM / TO values in the samples files. The fields include:

  * SAMPFILE \- sample file number (1 6)
  * BHID \- channel identifier
  * FROM \- FROM value of record with inconsistent FROM / TO values
  * TO \- TO value of record with inconsistent FROM / TO values
  * ERROR \- error number:
  * 1: FROM > TO
  * 2: TO > next(FROM) or FROM < previous(TO)

If an error is identified then the OUT file will not be created.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
SURVPTS |  Survey data point file containing channel identifier and 3D coordinates. Expects fields BHID, XPT, YPT, ZPT. The points must be sorted by location along the channel. |  Input |  Yes |  Point Data  
SAMPLE1 |  First sample data file. This file is compulsory and must include fields BHID, FROM, and TO. It will probably also include at least one sample attribute field, such as grade or lithology. |  Input |  Yes |  Downhole Sample  
SAMPLE2-6 |  Five optional sample data files containing BHID, FROM and TO, and probably at least one sample attribute field. |  Input |  No |  Downhole Sample  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output desurveyed sample data file. This will include fields BHID, FROM, TO, LENGTH, X, Y, Z, A0, B0, and all other fields which were included in the sample file(s). The X, Y and Z fields are the coordinates of the centre of each sample. The A0 and B0 fields are the azimuth and dip of the sample, respectively. |  Output |  Yes |  Drillhole  
CHANSMRY |  Optional output file containing a summary record for each channel in the input files. Although the file is optional it is recommended that it is created as it can be useful for validating the data, and showing what data is missing from which channels. |  Output |  No |  Table  
ERRORS |  Optional output file containing a list of samples which do not pass the validation tests. These validation tests identify errors in the FROM / TO values. These errors will cause the process to fail so it is recommended that you create and review the ERRORS file. |  Output |  No |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
BHID |  Channel identifier |  SURVPTS SAMPLE1 |  No |  Any |  BHID  
XPT |  X coordinate of survey point |  SURVPTS |  No |  Numeric |  XPT  
YPT |  Ycoordinate of survey point |  SURVPTS |  No |  Numeric |  YPT  
ZPT |  Z coordinate of survey point |  SURVPTS |  No |  Numeric |  ZPT  
FROM |  Along channel distance to sample start. |  SAMPLE1 |  No |  Numeric |  FROM  
TO |  Along channel distance to sample end |  SAMPLE1 |  No |  Numeric |  TO  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
EXTEND |  Option to extend channel beyond last survey point: 0 - Terminate channel at the last survey point. 1 - Extend channel to maximum TO value in the input samples files. |  No |  1 |  1, 3 |  1,2,3  
ENDPOINT |  Option to include the X, Y, Z coordinates of the start and end of each sample in the desurveyed output file. 0 - Start and end coordinates are not included in OUT file. 1 - Fields XSTART, YSTART, ZSTART, XEND, YEND and ZEND are created in the OUT file. |  No |  1 |  1,4 |  1,2,3,4  
  
## Example
    
    
    !CHANNL3D   
  
---  
      
    
      &SURVPTS(survey_points),  &SAMPLE1(ASSAYS),  &SAMPLE2(LITHO),  
      
    
    &OUT(CHANNEL_OUT),   
      
    
      &CHANSMRY(CHANNEL_SUMMARY),  
      
    
    &ERRORS(CHANNEL_ERRORS),   
      
    
      @ENDPOINT=1,  @EXTEND=1  
      
    
    Output window  
      
    
    CHANNL3D - Create drillhole representation of channel   
      
    
     samples  
      
    
        
      
    
    ... Input validation  
      
    
    ... Checking sample file(s).  
      
    
     ... No TO/FROM overlaps have been identified   
      
    
     in sample files  
      
    
        
      
    
     ... Calculating sample segment locations  
      
    
     ... Merging samples from file ASSAYS  
      
    
     ... Merging samples from file LITHO  
      
    
        
      
    
     ... Creating summary file CHANNEL_SUMMARY  
      
    
        
      
    
     WARNING:  
      
    
     ... Some channels have no data for one or more   
      
    
     input files.  
      
    
     ... 3 channels have 0 or 1 survey points  
      
    
     ... 2 channels have 0 samples  
      
    
     ... Check file CHANNEL_SUMMARY for details  
      
    
        
      
    
     ... Calculating sample end points  
      
    
        
      
    
     Output Files:  
      
    
     ... Results file CHANNEL_OUT contains 2874 records  
      
    
     ... Errors file CHANNEL_ERRORS contains 0 records  
      
    
     ... Channels summary file CHANNEL_SUMMARY contains   
      
    
     55 records  
      
    
        
      
    
     CHANNL3D process complete  
      
    
       
  
Related topics and activities

  * [HOLES3D Process](<holes3d.md>)

  * [HOLMER Process](<holmer.md>)