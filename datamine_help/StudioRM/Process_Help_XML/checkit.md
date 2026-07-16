# CHECKIT Process

To access this process:

  * **Data** ribbon **> > Data Tools >> String Utilities >> Check Strings**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **CHECKIT** and click **Run**.
  * Enter "CHECKIT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#CHECKIT>).

## Process Overview

**CHECKIT** carries out validation checks on string data.

The process first renumbers all **PVALUE** s starting with 1 and incrementing by 1\. A new string is started whenever the old **PVALUE** changes or when the point number (**PTN**) is 1. This is done in case the input file contains two or more strings with the same **PVALUE**. 

Duplicate points within a string are identified, and the second and subsequent occurrences of any point are removed, except for the last point which can be the same as the first.

Duplicate strings are removed. This is done by summing the **XP** , **YP** and **ZP** coordinates for each string, and identifying strings with identical accumulated values. Therefore strings are duplicates if they have the same points, even though other attributes may be different. It is possible to define two strings which use the same set of points, but in a different order. In this particular case the method would incorrectly flag the strings as identical. If this situation is a possibility then the strings should be checked interactively in the Design Window.

The process **[PROPER](<proper.md>)** also carries out checks on string files.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input string file. |  Input |  Yes |  String File  
  
## Example
    
    
    !CHECKIT &IN(strings1),&OUT(strings2)  
  
---  
      
    
    CHECKIT   
      
    
     - Point and string validation  
      
    
    ... input validation  
      
    
    ... validating string data  
      
    
    ... 6 duplicate points removed  
      
    
    ... 2 duplicate strings removed  
      
    
    ... input file strings1  
      
    
    contains 6 strings with a total of 129 points  
      
    
    ... output file strings2  
      
    
    contains 4 strings with a total of 111 points  
      
    
    ... process complete  
  
Related topics and activities

  * [CHKTRI Process](<chktri.md>)

  * [PROPER Process](<proper.md>)