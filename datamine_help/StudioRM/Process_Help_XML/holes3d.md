# HOLES3D Process

To access this process:

  * Sample Analysis ribbon **> > Prepare Samples >> Build Static**.
  * Enter "HOLES3D" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **HOLES3D** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_H.md#HOLES3D>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

**HOLES3D** converts a set of downhole sample data, collars location data and optionally downhole survey data, into a 'desurveyed' static drillholes file in which each sample is identified by its location (X,Y,Z coordinates) and direction (azimuth and dip) in space.

**Note** : HOLES3D is used by **[Drillhole Importer](<../COMMON/DrillholeImporter-screen.md>)**.

In the 'desurveyed' form, each drillhole sample is identified independently in 3D space without reference to its neighbours.

If two or more downhole sample files are specified (maximum 10) then they are merged so that all divisions of all sets of samples are maintained. A typical use of merging is to add an assay file to a lithology file, where the lithology intervals do not match the assay sample boundaries. Another example is to add absent data samples into holes by making the second file a single record per hole defining the total hole length.

The output from the **HOLES3D** process is in the standard drillhole format which is used elsewhere in your application. For example the drillholes can be viewed interactively, composited downhole, and used to interpolate grades into a block model.

### Using Downhole Survey Data

The downhole survey data is optional. If a survey file is not specified it is assumed that all the drillholes are vertical. If the survey file only includes a subset of the total number of drillholes, then it is assumed that all drillholes which are not included in the survey file are vertical. In both cases a warning message is displayed. The positions at which the survey readings are recorded does not have to correspond to sample positions. 

**Important** : A maximum of 50,000 survey measurements can be processed for each hole. If the number of points exceeds 50,000 then a subset will be selected so that the total number of points is less than 50,000. 

The IDs of all holes that use a subset of survey points are displayed with the progress messages in the Command Window. The IDs are also added to the **ERRORS** file. The **HOLESMRY** file shows the number of survey points processed for all holes.

Each drillhole in the downhole survey data file should have a survey measurement at its collar (AT=0). If this is not the case then the process will automatically move the first survey measurement to the collar position. A warning is issued and a list of all offending holes is displayed. If moving the survey position is not appropriate then you should edit the survey data file and rerun the process.

The process works by first computing a set of positions in space at known coordinates down each hole, and then interpolating between these known points for the top and bottom of each sample. The interpolation uses arcs of circles separately in horizontal and vertical planes.

The process will optionally calculate the XYZ coordinates of the start and end of each sample. This is controlled by parameter **ENDPOINT** , which if set to 1 will create the six extra fields. These coordinates can be useful for creating a DTM of the top or bottom of a seam or stratum.

As well as creating the desurveyed file, the process will optionally create two other files which assist in validating the input data. The **HOLESMRY** file contains a summary of the drillholes in each of the input files. It shows the number of records in each input file for each drillhole. The **ERRORS** file contains a list of:

  * surveys from the Downhole Survey file,

  * samples from the Downhole Sample file(s),

  * collars from the Collars file

which do not pass the validation tests. The tests are detailed in the description of the **ERRORS** file.

If the **HOLESMRY** file shows that one or more of the input data files do not contain entries for every drillhole then a warning is displayed. A warning is also issued if there are any entries in the **ERRORS** file. In order to correct any errors it will be necessary for you to edit the input data files and rerun the process.

You are encouraged to use the optional **HOLESMRY** and **ERRORS** files. You should also take careful note of the output display to see whether any warnings have been issued. If there are any warnings it is strongly recommended that you fix the data problems before using the desurveyed file for subsequent processing.

#### Missing Survey Records

  * Survey records in the collar table (in the **DIP** and **BRG** columns) are used (when available) if no other survey records are found for that hole. For example, if survey records exist in both the collar table and survey table for a hole, only records in the survey table are used (and collar records for that hole are ignored).

  * If no survey records exist for a hole in the survey table, the DIP and BRG values from the collar table are used.

  * If the collar table contains absent DIP or BRG records, the hole is set vertically.

### The SURVSMTH Parameter

When a hole sample is desurveyed the survey data (azimuth and dip) of the sample is used to locate the sample centre point in space. A desurveyed drillhole file contains a set of samples each with a calculated center point in XYZ world space.

Sometimes raw drillhole data tables to be desurveyed may contain more than one survey record within one sample, each with different azimuth and dips. Since a sample is by definition a straight line its location in space cannot be calculated using more than one survey record. The SURVSMTH parameter is used to automatically divide up samples where more than one survey records lie within a sample.

The samples are split in half until only one survey record lies within each sample. Therefore many samples may be created. The default value of SURVSMTH is 1 which will cause extra samples to be created so that no sample contains more than one survey record within its **FROM** and **TO** values. For no extra samples to be created the SURVSMTH parameter should be set to zero.

If the SURVSMTH parameter is set to zero and a sample does contain more than one survey record not all survey records will be taken into account. Traditionally this has been resolved by first compositing the samples to reduce their lengths. The SURVSMTH parameter avoids this requirement.

It is often the case that the first one or two samples in exploration holes contain more than one survey record because they are relatively long. This is because sample divisions have not had to have been created through assay and lithological identification near the surface

## Defining Dip and Bearing

@**DIPMETH** determines the dip convention used to describe hole data. It can be set to 1 to ensure that positive dip values point downwards, or -1 to point upwards.

Things get more complex if there is a a mixture of survey data from the input collar table and an input survey table, containing its own dip and bearing information. In this situation, where both data exists:

  * Survey records in the collar table (in the **DIP** and **BRG** columns) are used (when available) if no other survey records are found for that hole. That is, if survey records exist in both the collar table and survey table for a hole, only records in the survey table are used (and collar records for that hole are ignored).

  * If no survey records exist for a hole in the survey table (but a survey table is specified), the **DIP** and **BRG** values from the collar table are used instead.

    * If the collar table contains absent **DIP** or **BRG** records, the hole is set vertically.

Regardless, all survey records (either in &**COLLAR** or &**SURVEY**) respect the **DIPMETH** parameter.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
COLLAR |  Data file of drillhole collar locations. Expects fields **BHID** , **XCOLLAR** , **YCOLLAR** and **ZCOLLAR** ; optional fields **BRG** , **DIP**.  If **BRG** and **DIP** exist, these values will only be used when no valid survey records exist in input file **SURVEY**. If **BRG** and **DIP** values in **COLLAR** are absent or these columns are missing, holes are presumed vertical. |  Input |  Yes |  Collars  
SURVEY |  Optional survey data file. Expects fields **BHID** , **AT** , **BRG** , **DIP**. If a borehole has Survey Data, then it must include a record for the collar location, i.e. **AT** =0. **DIP** /**BRG** will first be taken from **SURVEY** file, if that does not exist **DIP** /**BRG** will be taken from **COLLAR** and any other holes are presumed vertical.  |  Input |  No |  Downhole Survey  
SAMPLE1-10 |  Sample data files. This file is compulsory and must include fields **BHID** , **FROM** , and **TO**. It will probably also include at least one sample attribute field, such as grade or lithology. |  Input |  Yes |  Downhole Sample  
  
## Output Files

Name |  I/O Status |  I/O Status |  Required |  Type  
---|---|---|---|---  
OUT |  Output desurveyed sample data file. This will include fields **BHID** , **FROM** , **TO** , **LENGTH** , **X** , **Y** , **Z** , **A0** , **B0** , and all other fields which were included in the sample file(s). The **X** ,**Y** and **Z** fields are the coordinates of the centre of each sample. The **A0** and **B0** fields are the azimuth and dip of the sample, respectively. This cannot be the same file name as ERRORS (see below) For more information on Downhole Survey files, click [here](<../COMMON/filetype.md#Survey>). |  Output |  Yes |  Drillhole  
HOLESMRY |  Optional output file containing a summary of the drillholes in each of the input files. It shows the number of records in each input file for each drillhole identifier (**BHID**). This can be very useful for validating the data, and showing what data is missing from which holes. |  Output |  No |  Table  
ERRORS |  Optional output file containing a list of surveys and samples which do not pass the validation tests. This cannot be the same file name as the **OUT** file (see above). Tests 1-4 refer to the **SURVEY** file, tests 5-7 are applied to the data in files **SAMPLE1** to **SAMPLE6** , and test 7 is on the **COLLAR** file

  1. a survey file has been specified.
  2. each **BHID** has a survey reading for **AT** =0.
  3. each **BHID** in the (merged) sample file has at least one entry in the **SURVEY** file.
  4. the downhole **TO** value of a sample is greater then the downhole **FROM** value.
  5. Holes with more than 10,000 survey points are identified. Only a subset will be processed.
  6. the **FROM** /**TO** interval for one sample does not overlap the **FROM** /**TO** interval of the next sample.
  7. the **FROM** /**TO** interval is not duplicated.
  8. **XCOLLAR** , **YCOLLAR** and **ZCOLLAR** are not absent data. Only one of the errors 4-6 will be reported even if a sample fails more than one of these tests.

The output file will contain the following fields: \- **FILE** : the name of the file in which the error was identified, \- **PROBLEM** : a brief description of the problem, \- **BHID** : the drillhole identifier, \- **FROM** : the downhole **FROM** distance of the sample, \- **TO** : the downhole **TO** distance of the sample. In order to correct the problems it will be necessary to edit the original data files. |  Output |  No |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
BHID |  Drillhole identifier. |  COLLAR, SAMPLE1, SURVEY |  No |  Any |  BHID  
XCOLLAR |  X co-ordinate of drillhole collar. |  COLLAR |  No |  Numeric |  XCOLLAR  
YCOLLAR |  Y co-ordinate of drillhole collar. |  COLLAR |  No |  Numeric |  YCOLLAR  
ZCOLLAR |  Z co-ordinate of drillhole collar. |  COLLAR |  No |  Numeric |  ZCOLLAR  
FROM |  Downhole distance to sample top. |  SAMPLE1 |  No |  Numeric |  FROM  
TO |  Downhole distance to sample bottom. |  SAMPLE1 |  No |  Numeric |  TO  
AT |  Downhole distance to survey point. |  SURVEY |  No |  Numeric |  AT  
BRG |  Bearing of drillhole. |  SURVEY |  No |  Numeric |  BRG  
DIP |  Dip of drillhole. Dip values must always be positive when referring to the downwards direction if using this command in a batch process. For more information on Downhole Survey files, click [here](<../COMMON/filetype.md#Survey>). |  SURVEY |  No |  Numeric |  DIP  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SURVSMTH |  | **Option** | **Description**  
---|---  
0 |  Prevent samples being added to the output file.  
1 |  add samples where there are more than one survey record per sample.  
  
When a hole sample is desurveyed the survey data (azimuth and dip) of the sample is used to locate the sample centre point in space. A desurveyed drillhole file contains a set of samples each with a calculated center point in XYZ world space.

Sometimes raw drillhole data tables to be desurveyed may contain more than one survey record within one sample, each with different azimuth and dips. Since a sample is by definition a straight line its location in space cannot be calculated using more than one survey record. The SURVSMTH parameter is used to automatically divide up samples where more than one survey records lie within a sample.

The samples are split in half until only one survey record lies within each sample. Therefore many samples may be created. The default value of SURVSMTH is 1 which will cause extra samples to be created so that no sample contains more than one survey record within its FROM and TO values. For no extra samples to be created the SURVSMTH parameter should be set to zero.

If the SURVSMTH parameter is set to zero and a sample does contain more than one survey record not all survey records will be taken into account. Traditionally this has been resolved by first compositing the samples to reduce their lengths. The SURVSMTH parameter avoids this requirement.

It is often the case that the first one or two samples in exploration holes contain more than one survey record because they are relatively long. This is because sample divisions have not had to have been created through assay and lithological identification near the surface.

No |  1 |  0,1 |  0,1  
ENDPOINT |  set to 1 to include the **X** , **Y** and **Z** coordinates of the start and end of each sample in the desurveyed output file. Fields **XSTART** , **YSTART** , **ZSTART** , **XEND** , **YEND** and **ZEND** are created in the output file. |  No |  0 |  0,1 |  0,1  
DESURVMD |  Locate sample centers or end points on the desurveyed arcs. The default is 1, to accurately locate the sample center points. =0 : To accurately locate sample **END** points on the desurveyed arcs. =1 : To accurately locate sample **CENTER** points on the desurveyed arcs. | No | 1 |  0,1 |  0,1  
DIPMETH |  Set to 1 to ensure that positive dip values point downwards, or -1 to point upwards. See "Defining DIP and BeaRinG", above. | No | 1 |  0,1 |  0,1  
INCLMISS |  INCLude MISSing samples parameter.

  * 0: the **OUT** file will not include **FROM** / **TO** intervals that were missing from the input sample files
  * 1: the OUT file will include a record for every missing FROM / TO interval in the input sample files. The grades will all be set to absent data

| No | 0 |  0,1 |  0,1  
PROMPT |  Set to 1 (default) to pause **HOLES3D** execution if an error occurs. Set to 0 to continue processing script if errors are encountered (useful when running **HOLES3D** from script as processing will continue). |  No |  1 |  0,1 |  0,1  
KEEPNAME |  Determine how field names are treated during processing.

  * 0: any non-standard field names are converted to standard field names in output files.
  * 1: non-standard field names are carried through to the output files.

|  No |  1 |  0,1 |  0,1  
PRINT |  |  Option |  Description  
---|---  
1 |  to display each individual process which is run by the **HOLES3D** superprocess.  
No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !HOLES3D    &COLLAR(collars),   
  
---  
      
    
      &SURVEY(surveys),   &SAMPLE1(assays),   &SAMPLE2(lith),   
      
    
        &OUT(assay.d),    &HOLESMRY(holesmry),   
      
    
         &ERRORS(errors),  
      
    
    *BHID(BHID),   *XCOLLAR(XCOLLAR),   *YCOLLAR(YCOLLAR),   
      
    
        *ZCOLLAR(ZCOLLAR),     
      
    
    *FROM(FROM),   *TO(TO),   
      
    
       *AT(AT),   *BRG(BRG),    *DIP(DIP),  
      
    
    @ENDPOINT=0.0  
  
## Error and Warning Messages

Message |  Description |  Solution  
---|---|---  
No Survey File |  The specified survey file can be found, or one is not specified. Process will terminate |  Specify a valid survey file for &SURVEY  
No Survey AT=0 |  One or more records has been found with a zero distance to a survey point |  Review input data and resolve/remove unexpected data, or accept results as expected.  
No Survey Data |  No valid survey data can be found in the specified survey column |  Review input data and resolve unexpected data  
TO < FROM |  One or more records exist where the TO value is less than the FROM value |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Sample Overlap |  Overlapping sample information has been found in one or more input hole component files |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Duplicate FROMs |  One or more duplicate FROM values has been found in input data |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Absent collars |  One or more drillholes has no corresponding collar specification. |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Duplicate collars |  One or more duplicate collar values has been found in input data |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Duplicate surveys |  One or more duplicate survey records has been found in input data |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Out of range DIP/BRG |  One or more DIP and or BRG values has been detected outside of the expected range. |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Out of range AT |  One or more AT values has been detected outside of the expected range. |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Absent FROM/TO |  One or more samples is missing a FROM or TO value |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Duplicate TOs |  One or more duplicate TO values has been found in input data |  Review input data and resolve/remove unexpected data, or accept results as expected.  
Could not find Datamine file collars |  The file name entered for the collars files cannot be found. |  An alternative file name must be provided before the process can proceed.  
Output holes and errors file cannot be the same |  The same file name has been specified for OUT and ERRORS |  Make file names unique for OUT and ERRORS  
Duplicate collars exist in file COLLAR |  Duplicate collar positions have been found in COLLAR file |  Review input data and resolve duplicate information, or accept results as expected.  
Duplicate survey records exist in file SURVEY |  Duplicate collar positions have been found in SURVEY file |  Review input data and resolve duplicate information, or accept results as expected.  
Out of range or absent values for BRG and DIP exist in file SURVEY |  Survey file contains absent or unexpected data records for either BRG or DIP (or both). This could be negative values or values > 360 |  Review input data and remove unexpected data, or accept results as expected.  
Out of range or absent values for AT exist in file SURVEY |  Survey file contains absent or unexpected data records for AT |  Review input data and remove unexpected data, or accept results as expected.  
xxx holes have survey data, but do not have a survey point at the collar (AT=0). The problem has been accounted for during desurveying by resetting the AT value of the first survey point to AT=0. However you should correct your survey file. |  Survey file contains missing survey point information at collar position (AT=0) |  Correct survey file  
Collar file BHID and survey file BHID have different data definitions which could result in truncation of BHID values. | Differing attribute widths or types for BHID in collar and survey files. | Harmonize attribute types between component files for BHID.  
  
**Note** : "out-of-range" can include any unexpected data input, including negative values.