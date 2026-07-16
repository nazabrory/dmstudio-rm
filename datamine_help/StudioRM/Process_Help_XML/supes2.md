# SUPES2 Process  
  
To access this process:

  * Enter "SUPES2" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SUPES2** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SUPES2>).

## Process Overview

Legacy process to write a Datamine perimeter file to a SURPAC2 string file.

String file is a system file in SURPAC2 format.

You are prompted for the following:

>SYSFILE> |  String file pathname  
---|---  
>JOBID> |  SURPAC jobid (max 10 characters)  
>DATE> |  Date (max 8 characters). Leave blank to use the current system date  
>PURPOSE> |  Purpose of string file (max 42 characters)  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input perimeter file with the fields **STRNO,PTN,XP,YP,ZP** and optionally **STRBRK, D0,D1,...D9**. |  Input |  Yes |  Undefined  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
PVALUE |  String number field. This would be **PVALUE** for a standard perimeter file or **STRNO** for a file that originated from SURPAC (PVALUE) |  IN |  No |  Numeric |  PVALUE  
XP |  Standard perimeter field **XP**. |  IN |  No |  Numeric |  XP  
YP |  Standard perimeter field **YP**. |  IN |  No |  Numeric |  YP  
ZP |  Standard perimeter field **ZP**. |  IN |  No |  Numeric |  ZP  
STRBRK |  Field identifying breaks in strings that should be output as 'isolations'. This would be **PVALUE** for a file that originated from **SURPAC**. |  IN |  No |  Any |  Undefined  
D0 |  First field to be included in the string file comment. |  IN |  No |  Any |  Undefined  
D1 |  Second field to be included in the string file comment. |  IN |  No |  Any |  Undefined  
D2 |  Third field to be included in the string file comment. Fields up to D9 can be specified. |  IN |  No |  Any |  Undefined  
  
Related topics and activities

  * [SUPEST Process](<supest.md>)

  * SUPES2 Process