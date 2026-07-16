# MINPER Process  
  
To access this process:

  * Enter "MINPER" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MINPER** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MINPER>).

## Process Overview

Modify a set of mining design perimeters automatically, according to production scheduling data.

**MINPER** has application in both underground and open pit mining including:-

  * The generation of plans for a proposed mine design at any required time during a mining schedule.

  * The production of a series of mine plans or isometric plots, depicting the mine being excavated from start to finish.

  * For open pit situations, the production of mined profiles according to the proposed schedule, so that face slopes and advances can be checked at different times during the schedule.

The input perimeter file contains perimeters which correspond to the original production unit data that was used for production scheduling. The perimeters should be primarily related to plan definitions. Corresponding to this set of perimeters, a set of input mining direction strings are defined. The file with this data may contain simply one two point string, which describes a vector for use as a mining direction for all perimeters. Alternatively, separate direction strings may be defined for each mining perimeter, in which case the PVALUEs of the mining direction strings and perimeters should correspond. It does not matter whether the mining direction strings are inside or outside the perimeters, or whether they actually intersect the mining perimeters. The mining direction strings can be just two point vectors, or they may have many points, to represent a mining face which changes its orientation as it advances. 

The other input file is the &SHEDRES file, which contains production scheduling data at some particular point in time. This will normally have been produced by the PRODSH process, either by saving a particular file during use of the LIST UNIT CUM BAR [/DU] command, or by copying with retrieval criteria (based on a selected time) from a complete output schedule file. It will normally contain (and needs for the operation of MINPER) the fields PNUM, SNUM, TONNES and TOTALTON. The entries in the TONNES field indicate the amount of reserves left at the time the file was created, and the entries in the TOTAL TON field indicate the tonnage that has been mined up to and including that time slot.

You must also define which field in the &**SHEDRES** file corresponds to the PVALUE entries in the perimeter file, normally either PNUM or SNUM. This depends on the way in which the original &RESERVE file was prepared for entry to PRODSH.

If the &SHEDRES file comes from sources other than PRODSH, the * **PERIM** field name entry can be anything, as long as its data entries correspond to the logical PVALUE entries in the input perimeter file.

The @**MINE** parameter can be set to 0 if the user requires, to produce the remainder of the perimeters that remain to be 'mined', rather than the already 'mined' part of the perimeters (@**MINE** =1 which is the default).

The output from **MINPER** is a set of perimeters, which obviously are related to the original perimeter shapes, but have one truncated edge, representing a mining face perpendicular to the mining direction string. The position of this edge has been determined from the proportion of the perimeter which has been 'mined'. If more than one mining direction string was present in the &STRINGIN file, then only perimeters which have a corresponding string will be output. Similarly, perimeters for which there is no corresponding schedule data will not be output.

The output set of perimeters can be used to create a plan or isometric plot of the mine design at the particular time of the schedule data. Alternatively, the strings may be used as the basis of more detailed mine design work.

### Series of Mined Excavations

After a complete schedule has been produced using PRODSH, it is possible to utilize MINPER to generate a whole set of perimeters, depicting the mining excavation at selected time slots throughout the schedule. This is done by using a looping macro, in which data for particular time slots is retrieved consecutively from the schedule, and then used with MINPER to produce the mined perimeters for that time slot. This procedure may be outlined as follows:-

  1. The user must input the start time, the end time, and the time increment required.

  2. Starting at the first time slot, the data from the schedule for just that time slot is copied out by retrieval.

  3. The MINPER process is used to determine the 'mined' perimeters at that time.

  4. Using processes [EXTRA](<extra.md>) and [PROPER](<proper.md>), the original mid-bench perimeters may be converted into the pairs of corresponding toe and crest perimeters.

  5. The processes [SURTRI](<surtri.md>) and [WIREPE](<wirepe.md>) are then used to create a crossing latticework of strings over the pit surface.

  6. The process [ISOPER](<isoper.md>) is finally used to create a 3D plot of the pit surface at that time in the schedule. This plot may be logically named according to the current time slot, and incorporated into a plot catalogue file.

  7. The time slot is then incremented and steps (2) to (6) repeated until the end time is reached.

  8. The final catalogue file may then be displayed to give the user a complete run through the proposed production schedule.

Using the wireframe model produced in step (5), section profile strings along any required section line may be produced. This may be done to produce face profile strings, which may be colored differently for the different times, and then viewed in the appropriate sectional view in the design window. Querying facilities allow the user to get detailed advance distances and slopes resulting from the proposed schedule.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PERIMIN |  Input perimeter file, which must contain the fields **XP** , **YP** , **ZP** , **PTN** and **PVALUE**. |  Input |  Yes |  String  
SHEDRES |  Input schedule data file, which must contain at least the fields **TONNES** , **TOTALTON** and another field whose entries correspond with the **PVALUE** entries in the **PERIMIN** file. If this file has been produced using the **PRODSH** process, it will contain the fields **PNAME** , **PNUM** , **SNUM** , **TONNES** , **TOTALTON** , **PRATE** and a number of grade fields. |  Input |  Yes |  Undefined  
STRINGIN |  Input mining string file, which defines the direction of mining. It may contain just one string, that will be applied to all the perimeters. Alternatively, it may contain a number of strings, which define different mining directions for each of the input perimeters. In the latter case, there must be match between the **PVALUE** entries in the **PERIMIN** and **STRINGIN** files. |  Input |  Yes |  String  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOUT |  Output |  Yes |  String |  Output perimeter file, which will contain the perimeters which have been modified according to the input schedule data.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
PERIM |  Field name in the input **SHEDRES** file that corresponds with the **PVALUE** entries in the input **PERIMIN** file. |  **PERIMIN** |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
MINE |  Flag indicating whether the output perimeter file should contain unmined perimeters, 0, or the mined perimters, (1). | No | 1 | 0,1 | 0,1  
  
## Example
    
    
    !MINPER &PERIMIN(QRRYDESN), &PERIMOUT(QRRYMINP), &SHEDRES(QRRYSHED),   
  
---  
      
    
               
      
    
    &STRINGIN(MINEDIRC), *PERIM(PNUM)  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> FIELD ffffffff MISSING FROM INPUT MINING STRING FILE <<< |  The input mining string file must contain the explicit fields XP, YP, ZP, PTN and PVALUE. Fatal; the process is exited.  
>>> MISSING FIELD ffffffff IN SCHEDULE DATA FILE <<< |  The input schedule data file must contain the explicit fields TONNES, TOTALTON and another field which corresponds to the *PERIM field name entry (e.g. PNUM, SNUM). Fatal; the process is exited.  
>>> MISSING ESSENTIAL FIELD ffffffff IN PERIMETER FILE <<< |  The input perimeter file must contain the explicit fields XP, YP, ZP, PTN and PVALUE. Fatal; the process is exited.  
>>> FIELD ffffffff IN PERIMETER FILE IS NOT NUMERIC <<< |  All of the essential fields in the perimeter file must be numeric and explicit. Fatal; the process is exited.  
>>> THE INPUT AND OUTPUT PERIMETER FILES CANNOT HAVE THE SAME NAME <<< |  The input and output perimeter files must have different names. Fatal; the process is exited.  
>>> THE INPUT PERIMETER FILE AND THE INPUT MINING STRING FILES MUST BE DIFFERENT FILES <<< |  The input perimeter file and the input mining string file must have different names. Fatal; the process is exited.  
>>> THE OUTPUT PERIMETER FILE AND THE INPUT MINING STRING FILE CANNOT HAVE THE SAME NAME <<< |  The output perimeter file and the input mining string file must have different names. Fatal; the process is exited.  
>>> CANNOT MAKE TWO INTERSECTIONS WITH ARTIFICIAL MINING DIRECTION STRING AND PERIMETER <<< |  It must be possible to make a mining face perpendicular to the perimeter(s), which make two intersections with the perimeter. Fatal; the process is exited.  
>>> MORE THAN TWO INTERSECTIONS FOUND BETWEEN THE MINING DIRECTION STRING AND PERIMETER >>> CANNOT LOCATE TWO INTERSECTIONS LEFT AND RIGHT OFF MINING STRING >>> ONE INTERSECTION LOCATED, BUT NEITHER END INSIDE PERIMETER >>> MINING STRING IS PARTIALLY OUTSIDE PERIMETER |  Problems can be caused if the mining direction string passes in and out of the perimeter several times. the string should be edited so that it either does not intersect the perimeter at all or intersects the perimeter only once or twice, but no more than that. Fatal; the process is exited.  
>>> NO MINING STRING HAS BEEN LOCATED FOR PERIMETER pppppppppp.pp |  This warning message is issued whenever a record is found in the schedule data without a corresponding entry in the input mining perimeter file.  
>>> CANNOT FIND SOLUTION FOR PERIMETER ppppppppppp.pp |  In particularly strange geometric cases, an exact solution may not be possible e.g. where the perimeter end edge undulates strongly and a very small remaining tonnage is required. The MINPER process will continue with the next perimeter.