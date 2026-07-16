# BLKPER Process

To access this process:

  * Model ribbon **> > Data From Model >> Perimeters**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **BLKPER** and click **Run**.
  * Enter "BLKPER" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/commandtable_B.md#BLKPER>).

## Introduction

Creates a set of perimeters around blocks in a model file.

The perimeters are either on horizontal benches or on vertical sections, parallel to the axes of the model. The starting perimeter, the distance between perimeters and the number of perimeters are defined by parameter. All perimeters are open and clockwise for perimeters surrounding model cells. For empty areas (voids), perimeters are created to isolate the void, and then linked to the non-void zone.

More specifically, If a set of cells completely surrounds a void then this is dealt with by creating an anti-clockwise perimeter around the void. This is then linked to the enclosing clockwise perimeter with a two-way bridge of zero width.

If a cell contains sub-cells, it is treated as if it were a complete cell.

More than one perimeter will be created for each plane if there are disjoint groups of cells.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file, which must contain the standard model fields. |  Input |  Yes |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  String |  Output perimeter file. Perimeter values have the format: PVALUE = nnn.mm where:- nnn = the plane number. mm = the perimeter number in the plane. XP,YP and ZP are true world coordinates.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DIRECT |  Parameter to specify the plane of the output perimeter: 1 = XY, 2 = XZ, 3 = YZ. |  Yes |  1 |  1,3 |  1,2,3  
STARTPOS |  Value of the coordinate perpendicular to the output plane for the first plane. |  Yes |  Undefined |  Undefined |  Undefined  
STIZE |  Distance between output planes. This must be positive. |  Yes |  Undefined |  Undefined |  Undefined  
NUMPLANE |  Number of output planes. |  Yes |  Undefined |  Undefined |  Undefined  
SMOOTH |  Controls perimeter generation (0): |  Option |  Description  
---|---  
0 |  Join cell corners;  
1 |  Join the midpoints of cell sides in order to smooth the outline.  
No |  0 |  0,1 |  0,1  
CONNECT |  Controls internal and external perimeter connections. |  Option |  Description  
---|---  
0 |  Do not connect internal and external perimeter connections.  
1 |  Connect internal perimeters to external perimeters as a single perimeter.  
2 |  Create only internal perimeters.  
  
No |  1 |  0,2 |  0,2  
BRADJUST |  Specifies gap to create between coincident segments in bridged parameters to assist later evaluation. Only used if @CONNECT=1 |  No |  0.0 |  Undefined |  Undefined  
  
## Example
    
    
    !BLKPER &IN(FEMODEL), &OUT(PERIMS), @DIRECT=1, @STARTPOS= -45,   
  
---  
      
    
     @STIZE=10, @NUMPLANE=10, @SMOOTH=0, Fe>46  
      
    
    Reading through the model file -  
      
    
    3185 Model records read  
      
    
    1 perimeter(s) output for plane -45  
      
    
    1 perimeter(s) output for plane -35  
      
    
    1 perimeter(s) output for plane -25  
      
    
    >>> 101 RECORDS IN FILE PERIMS <<<  
  
## Error and Warning Messages

Message  
---  
ERROR : @STARTPOS is not within the model  
ERROR : @DIRECT not in the range 1 to 3  
ERROR : @NUMPLANE not +ve  
ERROR : @STIZE not +ve