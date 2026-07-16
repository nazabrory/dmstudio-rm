# PERDTM Process  
  
To access this process:

  * **Digitize** ribbon **> > Transform >> Project >> Project Strings to Wireframe**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **PERDTM** and click **Run**.
  * Enter "PERDTM " into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#ENGLOG>)](<../command_help/COMMAND%20TABLE_P.md#PERDTM>).

## Process Overview

Convert 2-dimensional perimeters to 3-dimensional perimeters by vertical projection onto a DTM surface.

Values for additional fields in the input perimeter are taken as constant for the string and therefore carried across to each point of that string in the output perimeter.

**Note** : A perimeter must lie entirely within the area defined by the DTM wireframe, otherwise points lying beyond will have undefined ZP values.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PERIMIN |  Input perimeter file |  Input |  Yes |  String  
WIRETR |  Input DTM triangle file |  Input |  Yes |  Wireframe Triangle  
WIREPT |  Input DTM point file |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PERIMOUT |  Output |  Yes |  String |  Output perimeter file  
  
## Example
    
    
    !PERDTM &PERIMIN(PER),&WIREPT(ZON1PT),&WIRETR(ZON1TR),  
  
---  
      
    
    &PERIMOUT(PERZ)    
  
## Error and Warning Messages

Message | Description  
---|---  
>>> WARNING - POINT IDENTIFIER nnnnnn TOO LARGE >>> AT POINT FILE RECORD NUMBER rrrr. |  There is a problem with the point data file.  
>>> FIELD aaaaaaaa MISSING FROM TRIANGLE FILE |  One of the compulsory triangle fields (PID1,PID2,PID3) is missing.  
>>> FIELD aaaaaaaa MISSING FROM POINT FILE |  One of the compulsory point fields (XP,YP,ZP,PVALUE,PID,PTN) is missing.  
  
Related topics and activities

  * [project-points-to-wf-in-view ("pti")](<../command_help/project-points-to-wf-in-view.md>)
  * [project-string-onto-wf-in-view ("ptd")](<../command_help/project-string-onto-wf-in-view.md>)
  * [project-to-view-plane ("ptv")](<../command_help/project-to-view-plane.md>)
  * [project-points-to-wireframe](<../command_help/project-points-to-wf.md>)

  * [project-string-onto-wf-limit ("ptl")](<../command_help/project-string-onto-wf-limit.md>)

  * [project-points-to-wf-angle](<../command_help/project-points-to-wf-angle.md>)

  * [project-string-at-angle](<../command_help/project-string-at-angle.md>)

  * [project-string-onto-wf](<../command_help/project-string-onto-wf.md>)

  * [project-string-onto-wfs ("pstw")](<../command_help/project-string-onto-wfs.md>)

  * [move-string-to-view ("mtv")](<../command_help/move-string-to-view.md>)