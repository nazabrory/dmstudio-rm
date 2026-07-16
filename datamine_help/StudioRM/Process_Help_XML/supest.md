# SUPEST Process

To access this process:

  * Enter "SUPEST" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **SUPEST** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SUPEST>).

## Process Overview

Converts a Datamine perimeter file to a SURPAC string file.

The compulsory standard fields of a Datamine perimeter file are **PVALUE, PTN, XP,YP,ZP** and optionally **PCODE** (4 character alphanumeric). In SURPAC the first and last point in a perimeter are identical if closed, whereas your application automatically closes a perimeter. The standard fields in a SURPAC string file are **STRING NUMBER, Y,X,Z, DESCRIPTION**. **STRING NUMBER** is in the range 1-98, so the allocation of **STRING NUMBER** is done as using the @**STRNO** parameter.

The following prompts appear on running the process:

>SYSFILE> |  String file pathname  
---|---  
>JOBID> |  SURPAC jobid (max 10 characters)  
>DATE> |  Date (max 8 characters). Leave blank to use the current system date  
>PURPOSE> |  Purpose of string file (max 42 characters)  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input perimeter file with the standard fields **PVALUE,PTN,XP,YP,ZP** and optionally **PCODE**. |  Input |  Yes |  String  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
XP |  Standard perimeter field **XP**. |  IN |  No |  Numeric |  XP  
YP |  Standard perimeter field **YP**. |  IN |  No |  Numeric |  YP  
ZP |  Standard perimeter field **ZP**. |  IN |  No |  Numeric |  ZP  
DESC1 |  First field to be included in the string file comment. |  IN |  No |  Any |  Undefined  
DESC2 |  Second field to be included in the string file comment. |  IN |  No |  Any |  Undefined  
DESC3 |  Third field to be included in the string file comment. |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
STRNO |  Method of calculating SURPAC string number (0). SURPAC string numbers are in the range 1-98. **STRNO** =0 uses the **PVALUE** field **STRNO** =n increments the **PVALUE** from n. |  No |  0 |  Undefined |  Undefined  
  
## Example
    
    
    !SUPPEST     &IN(PITPER), @STRNO=0>SYSFILE   
  
---  
      
    
    >SURSTR  
      
    
    >JOBID   
      
    
    >>DATE   
      
    
    >>PURPOSE >  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> NOT A VALID PERIMETER FILE <<< |  The &IN perimeter file specified does not contain one of the compulsory fields PVALUE, PTN, XP,YP,ZP. Fatal; the process is exited.  
>>> INVALID STRING NUMBER: NSTR = nnnnnnnnnnn <<< |  The STRING NUMBER is outside the valid range of 1 to 98. Fatal; the process is exited.  
>>> POINT NUMBER NOT IN SEQUENCE, PTN = nnnnnnnnn <<< |  The PTN (point number) is out of sequence in the &IN perimeter file specified. Fatal; the process is exited.  
>>> NO POINTS AVAILABLE FOR SUPEST OUTPUT <<< |  No perimeter points were found to output to the SURPAC string file. Fatal; the process is exited.  
>>> FIELD ffffffff DOES NOT EXIST <<< |  One of the fields specified for *XP, *YP, *ZP does not exist in the &IN perimeter file specified. Fatal; the process is exited.  
  
Related topics and activities

  * [SUPES2 Process](<supes2.md>)

  * SUPEST Process