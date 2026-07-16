# TRIPOI Process

To access this process:

  * Enter "TRIPOI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **TRIPOI** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TRIPOI>).

## Process Overview

This command can be used to project points vertically onto a nominated wireframe surface.

Note: The input file must be sorted on the X coordinate.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file to be intersected. Must contain fields X , Y , Z. Must be sorted on X. |  Input |  Yes |  Undefined  
WIRETR |  Input wireframe triangle file. |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input wireframe point file. |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file with additional elevation field.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
X |  Name of intersection X field in IN. |  IN |  Yes |  Numeric |  Undefined  
Y |  Name of intersection Y field in IN. |  IN |  Yes |  Numeric |  Undefined  
Z |  Name of output elevation field in OUT. |  OUT |  Yes |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
KEEP |  To carry through points not intersected by any triangle, with Z |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !START WF_Proje  
  
---  
      
    
       
      
    
    #Define here the maximum segment size  
      
    
       
      
    
    !LET $DMAX#=10  
      
    
       
      
    
    !PROPER   &amp;PERIMIN(input_grid),&amp;PERIMOUT(Conditioned_Grid),  
      
    
       
      
    
              @MODE=1.0,@AREA=0.0,@LENGTH=0.0,@REFPOINT=0.0,@CLOSE=0.0,  
      
    
       
      
    
              @VPLANE=1.0,@DMAX=$DMAX#,@TOL=0.0,@REDUCE=0.0,@EXTEND=0.0,  
      
    
       
      
    
              @CROSS=0.0  
      
    
       
      
    
    !MGSORT   &amp;IN(conditioned_grid),&amp;OUT(cond_grid_sort),*KEY1(XP),  
      
    
       
      
    
              *KEY2(YP),*KEY3(ZP),@ORDER=1.0,@KEYSFRST=1.0,@ROWORDER=1.0  
      
    
       
      
    
    !TRIPOI   &amp;IN(cond_grid_sort),&amp;WIRETR(reef_combinedtr),  
      
    
       
      
    
              &amp;WIREPT(reef_combinedpt),&amp;OUT(projected_grid),*X(XP),  
      
    
       
      
    
              *Y(YP),*Z(ZP),@KEEP=0.0  
      
    
       
      
    
    !MGSORT   &amp;IN(projected_grid),&amp;OUT(Final_Output),*KEY1(PVALUE),  
      
    
       
      
    
              *KEY2(PTN),@ORDER=1.0,@KEYSFRST=1.0,@ROWORDER=1.0  
      
    
    !END  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 120 <<< (y) in TRIPOI |  Missing or invalid file (y is the file number).  
>>> ERR 121 <<< (y) in TRIPOI |  Missing or invalid fields (y is the file number).  
>>> TOO MANY FIELD <<< >>> ERR 122 <<< (y) in TRIPOI |  Too many fields in the output file. Note: Maximum fields = 256  
>>> NO DATA IN INPUT FILE <<< >>> ERR 136 <<< (y) in TRIPOI |  No data in the input file &**IN**.  
>>> MISSING OR ALPHA FIELD (S) IN MODEL PROTOTYPE <<< >>> ERR 142 <<< (y) in TRIPOI |  Either the input model does not include the required thirteen model fields, or the fields are alpha rather than numeric.  
>>> MISSING OR ALPHA FIELD (S) IN WIREPT FILE <<< >>> ERR 145 <<< (y) in TRIPOI |  Either the input wireframe points file does not include the required four numeric fields (XP,YP,ZP,PID), or the fields are alpha rather than numeric.  
>>> MISSING OR ALPHA FIELD (S) IN WIRETR FILE <<< >>> ERR 146 <<< (y) in TRIPOI |  Either the input wireframe triangle file does not include the required four numeric fields (**PID1** ,**PID2** ,**PID3** ,**TRIANGLE**), or the fields are alpha rather than numeric.