# CHKTRI Process

To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Check Wireframes**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CHKTRI** and click **Run**.
  * Enter "CHKTRI" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CHKTRI>).

## Process Overview

**CHKTRI** checks wireframe point and triangle files.

The process first reorders the **PID** value in the point file, while removing any invalid **PID** values, then reorders the **TRIANGLE** values in the triangle file, while removing triangles that reference undefined points. Optionally one can eliminate duplicate **PID** references from the triangle file (i.e. if there are duplicate points in the point file, the triangle file will only reference the first occurrence of the point).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRETRIN |  Input wireframe triangle file. |  Input |  Yes |  Wireframe Triangle  
WIREPTIN |  Input wireframe point file. |  Input |  Yes |  Wireframe Points  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
WIRETROU |  Output |  Yes |  Wireframe Triangle |  Output wireframe triangle file.  
WIREPTOU |  Output |  Yes |  Wireframe Points |  Output wireframe point file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
REMDUPID |  Set to 1 to remove duplicate PID references from the WIRETROU file (0). |  No |  0 |  0,1 |  0,1  
  
Related topics and activities

  * [CHECKIT Process](<checkit.md>)