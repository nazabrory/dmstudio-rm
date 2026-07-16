# DILUTE Process  
  
To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DILUTE** and click **Run**.
  * Enter "DILUTE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DILUTE>).

## Introduction

Allows the extension of drillhole seam intersection data to allow for dilution above and below seams.

The input drillhole data file must contain * **FROM** and * **TO** fields, which define the ranges of a particular seam or horizon intersection with a unique value of the field * **SEAMID**. This type of file may be an assay file, or a 'desurveyed' file in standard sample format, or may be constructed by the user. The file must be sorted in order of the drillhole identifier (* **BHID**) and * **FROM** fields. 

Dilution is carried out by subtracting the distance specified by parameter @**DILUP** from the * **FROM** of the top of each seam specified by * **SEAMID** , and by adding the distance @**DILDOWN** to the * **TO** of the seam. These parameters may be either positive or negative. If positive, then each seam is expanded; this corresponds to mining dilution. If negative, then each seam is contracted; this corresponds to leaving material in the floor and roof.

If the dilution envelopes of two different seams intersect, they are adjusted to prevent overlap. If the dilution envelopes of two intersections, which are identified as part of the same seam, meet, the two intersections are combined into one. If the dilution parameters are negative then seams will be removed if the total thickness becomes zero or negative. If a seam top should be extended upwards to give a negative * **FROM** , the value is set to zero.

A cut-off intersection thickness may be specified (after dilution) by use of the optional parameter @**THINNEST**.

These calculations are performed on downhole distances, and therefore do not take into account the direction of the hole. **DILUTE** is thus only suitable for drillholes with essentially the same orientation (for example, vertical).

**Note** : where dilution envelopes of adjacent seams intersect, each is reduced by an appropriate factor to remove the overlap. This factor is computed to maintain a ratio of **DILDOWN** :**DILUP** between the thicknesses assigned to the upper and lower of the two seams respectively.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file. Must contain at least fields for **BHID** , **FROM** , **TO** and **SEAMID**. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
BHID |  Borehole identifier. May be numeric or alpha. |  IN |  Yes |  Any |  BHID  
FROM |  Downhole **FROM** distance (top of intersection). |  IN |  Yes |  Numeric |  FROM  
TO |  Downhole **TO** distance (base of intersection). |  IN |  Yes |  Numeric |  TO  
SEAMID |  Identification for intersections. Must be numeric or alpha up to a maximum of 4 chars. |  IN |  Yes |  Any |  SEAMID  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DILUP |  Dilution distance up from **FROM** positions. |  Yes |  Undefined |  Undefined |  Undefined  
DILDOWN |  Dilution distance down from **TO** positions. |  Yes |  Undefined |  Undefined |  Undefined  
THINNEST |  Thinnest acceptable seam. Any thinner intersections are eliminated.  |  No |  Undefined |  Undefined |  Undefined  
  
## Example

This example shows dilution of all seams in file 'SEAMS' by adding 0.3 metres to the top and 0.5 metres to the bottom of each seam:
    
    
    !DILUTE &IN(SEAMS), &OUT(SEAMS1), *BHID(BHID),   
  
---  
      
    
    *FROM(FROM), *TO(TO), *SEAMID(SEAM), @DILUP=0.3,   
      
    
    @DILDOWN= 0.5, @THINNEST= 1  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERROR nnnn SEAMS IN HOLE AT RECORD rrrrr <<< |  There is a limit of 50 seams in each drillhole. Fatal; the process is exited.