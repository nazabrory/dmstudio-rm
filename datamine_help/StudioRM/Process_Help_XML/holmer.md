# HOLMER Process

To access this process:

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **HOLMER** and click **Run**.

  * Enter "HOLMER" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_H.md#HOLMER>).

## Process Overview

Merge two sets of drillhole data samples with different downhole distances.

The two sets on the input files are matched on borehole identifier (* **BHID**), * **FROM** and * **TO** fields, and the output file contains the logical join of both sets of samples, so that all the divisions of both sets of samples are maintained.

Typical uses are to add lithology data to a sample file, where the lithology intervals do not match assay sample boundaries, to define coal seams by merging in seam definitions with the assays, or to add absent data samples. The intersections file produced by **SECTED** , defining the **FROM** and **TO** intersection pairs for each perimeter on each chosen drillhole, may be merged with the original sample data file using **HOLMER**. Compositing and modeling may then be carried out on this merged file over the defined intersections.

The two input files must be sorted on fields * **BHID** and * **FROM**. Holes are matched on their * **BHID** values. Within each hole, the * **FROM** and * **TO** values are compared, and a record output for each * **FROM** and * **TO** pair. The output file will contain records for each hole in either input file, and all fields contained in both input files. Absent data values are inserted for all fields which do not have a value in one or the other file over the given interval.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  Input file 1. Must contain at least fields for BHID, FROM,and TO. |  Input |  Yes |  Downhole Sample  
IN2 |  Input file 2. Must contain at least fields for BHID, FROM,and TO. |  Input |  Yes |  Downhole Sample  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Downhole Sample |  Output file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
BHID |  Borehole identifier. May be numeric or alpha. |  IN1, IN2 |  Yes |  Numeric |  BHID  
FROM |  Downhole FROM distance (top of intersection). |  IN1, IN2 |  Yes |  Numeric |  FROM  
TO |  Downhole TO distance (base of intersection). |  IN1, IN2 |  Yes |  Numeric |  TO  
  
## Examples
    
    
    !HOLMER &IN(ASSAYS), &IN2(SEAMS), &OUT(INTERX),   
  
---  
      
    
    *BHID(BHID), *FROM(FROM), *TO(TO)  
  
### Example 1: Adding Absent Data Samples

&IN1 |  &IN2 |  &OUT  
---|---|---  
FROM |  TO |  Au |  FROM |  TO |  FROM |  TO |  Au  
1.3 |  1.8 |  0.6 |  0.0 |  120.0 |  0.0 |  1.3 |  -  
1.8 |  2.5 |  1.4 |  |  |  1.3 |  1.8 |  0.6  
50.5 |  51.5 |  2.4 |  |  |  1.8 |  2.5 |  1.4  
51.5 |  52.0 |  1.2 |  |  |  2.5 |  50.5 |  -  
|  |  |  |  |  50.5 |  51.5 |  2.4  
|  |  |  |  |  51.5 |  52.0 |  1.2  
|  |  |  |  |  52.0 |  120.0 |  -  
  
A single hole is shown. The &**IN1** file contains the Au intersections. The &**IN2** file contains a single record for the hole showing the total drilling length (0-120). The output file contains records for each 'sample' from 0-120, with absent data Au values inserted.

The output file is thus a complete record of the drillhole, generated without the need to type in each absent data Au record. Note that the order of the input files is not important in this example.

### Example 2: Seam Definition

&IN1 |  &IN2 |  &OUT  
---|---|---  
FROM |  TO |  CV |  FROM |  TO |  seam |  FROM |  TO |  CV  
0.0 |  5.2 |  0 |  5.4 |  8.9 |  1 |  0.0 |  5.2 |  0  
5.2 |  7.2 |  10234 |  12.5 |  16.3 |  2 |  5.2 |  5.4 |  10234  
7.2 |  9.0 |  11367 |  |  |  |  5.4 |  7.2 |  10234  
12.2 |  14.2 |  9552 |  |  |  |  7.2 |  8.9 |  11367  
14.2 |  16.5 |  10197 |  |  |  |  8.9 |  9.0 |  11367  
|  |  |  |  |  |  12.2 |  12.5 |  9552  
|  |  |  |  |  |  12.5 |  14.2 |  9552  
|  |  |  |  |  |  14.2 |  16.3 |  10197  
|  |  |  |  |  |  16.3 |  16.5 |  10197  
  
A single hole is shown. The output file contains all the divisions contained in both input files. In particular, it now shows the exact CV values and lengths contained within the seams. These may now be used in, for example, compositing (the [COMPDH](<compdh.md>) process). The order of the input files is not important in this example.

In the above two examples, which file is defined as &IN1 and which as &IN2 does not matter, as both files have different fields (apart from the compulsory * **BHID** , * **FROM** and * **TO**). If, however, the files have one of more fields in common, apart from the compulsory ones, then values from &**IN2** will update those from &**IN1** over the matching intervals. In this respect, **HOLMER** acts as the **[JOIN](<join.md>)** process. If all * **FROM** and * **TO** intervals match, then **HOLMER** works exactly like the **JOIN** process.

* * *

## Error and Warning Messages

Message |  Description  
---|---  
>>> FILE ffffffff CANNOT BE USED AS BOTH <<<  
>>> INPUT AND OUTPUT BY THIS PROCESS <<<  
>>> ERR 130 <<< ( n) IN HOLMER |  n is the file number (1 for &IN1,2 for &IN2). Fatal; the process is exited.  
>>> FROM OR TO FIELD DOES NOT EXIST OR IS ALPHA <<<  
>>> ERR 123 <<< ( 0) IN HOLMER |  The cause could be different fieldnames in the two input files for *FROM or *TO. Fatal; the process is exited.  
>>> INPUT FILE NOT SORTED ON KEYFIELD <<<  
>>> ERR 122 <<< ( n) IN HOLMER |  n is the file number (1 for &IN1, 2 for &IN2). Fatal; the process is exited.