# PROPER Process  
  
To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Process Strings**.

  * Enter "PROPER" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PROPER** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PROPER>)

## Process Overview

Copy and condition a set of perimeters.

This process is used to:

  * Add an **AREA** field.
  * Make all perimeters clockwise or anticlockwise.
  * Close or open all perimeters.
  * Set a minimum or maximum string segment length.
  * Reduce the number of points by a percentage.
  * Extend or shrink perimeters.

Optionally, the input may be treated as strings as opposed to perimeters. If so parameters **AREA, CLOCKWSE, VPLANE, EXTEND** and **CROSS** are ignored.

The reduce and tolerance options will not remove points that have a valid **TAG**. That is if a field TAG exists and is not set to 0 or missing.

Input perimeters must be planar. If the perimeters are within 6 digit tolerance of either the **XY, XZ** or **YZ** then they will be assumed to lie on the orthogonal plane. The output perimeters will be constant in the third dimension. This is useful if the perimeters have numerical rounding errors produced by prior processing. Non-planar perimeters will not be processed or output.

All perimeters will automatically be checked for crossovers and consecutive duplicate points. The duplicate points will be removed, however, the malformed perimeters will not be processed or output.

After point reduction or extension some perimeters may become malformed. These will be reported and output.

Extra points added by use of the @**EXTEND** or @**DMAX** parameters will have all attribute values set the same as the first point of the original perimeter.

For perimeters that are not on an orthogonal plane clockwise direction will be taken from an orthogonal view plane. All perimeters in parallel planes will have the same clockwise sense.

This process may be run without an output file for checking perimeters and reporting areas. It may not be run in place.

## Input Files

Name| Description| I/O Status| Required| Type  
---|---|---|---|---  
PERIMIN| The input perimeter file. The fields required are **XP,YP,ZP,PTN** , and **PVALUE** (standard perimeter format). All perimeters in the file will be used. All other fields will be copied. Perimeters must be planar.| Input| Yes| String  
  
## Output Files

Name| I/O Status| Required| Type| Description  
---|---|---|---|---  
PERIMOUT| Output| No| String| Output perimeter file. Contains all fields from the input file plus optionally **AREA**.  
  
## Parameters

Name| Description| Required| Default| Range| Values  
---|---|---|---|---|---  
MODE| For **MODE** =1 only parameters **CLOSE, DMAX, TOL, REDUCE** are used to treat strings. =0 : Treat as perimeters. =1 : Treat as strings.| No| 0| 0,1| 0,1  
AREA| field containing perimeter area creation flag =0 : dont create field **AREA** in **PERIMOUT** . =1 : create field **AREA** in **PERIMOUT** .| No| 0,1| 0,1| 0,1  
CLOSE|  =0 : will remove last point of a perimeter if perimeter is closed. . =1 : will add first point to end of perimeter if perimeter not closed..| No| 0| Undefined| -,0,1  
CLOCKWSE| =0 : make all perimeters anti-clockwise. =1 : make all perimeters clockwise.| No| Undefined| Undefined| -,0,1  
VPLANE| Viewing plane for clockwise sense for non-orthogonal planes (1). =1 : XY plane from +Z. =2 : XZ plane from -Y. =3 : YZ plane from +X.| No| 1| 1,3| 1,2,3  
DMAX| The maximum chord length used when inserting additional points into long chords.| No| Undefined| Undefined| Undefined  
TOL| Minimum allowable chord length used when removing points. Default is (0) for removal of consecutive duplicates.| No| 0| Undefined| Undefined  
REDUCE| Percentage point reduction 0 to 90 (0).| No| 0| 0,90| Undefined  
EXTEND| +/- perpendicular extension distance (0).| No| 0| Undefined| Undefined  
CROSS| | Option| Description  
---|---  
(0)| do not attempt to resolve crossovers in extended perimeters.  
No| 0| 0,1| 0,1  
ZEROXYZ| Internally set the X, Y or Z value of input perimeters to zero. An example of when this is useful is if you want to calculate plan areas of 3 dimensional perimeters =(0) : Do not internally adjust any coordinates in the input perimeters..  =1 : Internally treat all X coordinates in the input strings as zero.  =2 : Internally treat all Y coordinates in the input strings as zero.  =3 : Internally treat all Z coordinates in the input strings as zero. | Yes| 0| 0,3| 0,1,2,3  
  
## Example
    
    
    !PROPER &PERIMIN(PIN),&PERIMOUT(POUT)  
  
---  
      
    
    @AREA=1,@CLOSE=0,@CLOCKWSE=0,@DMAX=200,@TOL=1,@REDUCE=0,@EXTEND=10,@CROSS=-  
      
    
    PROPER TIME > 9:30:41  
      
    
    Perimeter 1.0000 Input Area = 206491.10 Points = 31 C/W  
      
    
    Perimeter 1.0000 Output Area = 297585.82 Points = 50 A/C  
      
    
    >>> 50 RECORDS IN FILE POUT <<<  
  
## Error and Warning Messages

Message| Description  
---|---  
>>> &PERIMIN FILE NOT FOUND <<<>>> &PERIMIN FIELD ERRORS <<<>>> &PERIMOUT file missing <<<| Warning only, output is optional.  
>>> Empty perimeter file !!! Perimeter nnn does not have enough points.| Perimeters has less than 3 points.  
>>> Perimeter nnn not in valid plane.| Perimeter is not planar.  
>>> Perimeter nnn has too many points - ignored.>>> Perimeter nnn malformed - ignored.| The perimeter contains crossovers  
>>> Perimeter nnn output malformed.| After point reduction or extension the perimeter has become malformed.  
>>> Perimeter points = not output.| After point reduction or extension the perimeter has less than 3 points.  
>>> Perimeter nn distance between mmm and kkk < tolerance.| Points within tolerance being reduced.  
>>> Perimeter nnn input area = nnn points = kkk C/W| Summary for each input perimeter after reduction by tolerance giving area, number of points and direction ( C/W or A/C).  
>>> Perimeter nnn output area = mmm points = kkk C/W| Summary for each output perimeter giving area, number of points and direction (C/W or A/C).  
>>> Deviation between planes:>>> Minimum deviation: nnn>>> Maximum deviation: mmm|  Summary of deviations in degrees between the planes of the perimeters.