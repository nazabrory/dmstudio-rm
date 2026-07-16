# TDIN Process

To access this process:

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, select **TDIN** and click **Run**.
  * Enter "TDIN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TDIN>).

## Process Overview

Processes [TDOUT](<tdout.md>) and TDIN provide the interface between your application and the standalone Whittle THREE-D program for pit Optimization. 

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Block Model |  Output model file.  
  
## Example
    
    
    !TDIN &OUT(MODEL2)Enter THREE-D parameter file name:  
  
---  
      
    
    >SYSFILE>run1.mpa  
      
    
    Enter THREE-D results file name:  
      
    
    >SYSFILE>model2.eco  
      
    
    >>> 6000 RECORDS PROCESSED : TIME 14:12:12 <<<6250 blocks read and then written to model file.  
      
    
    >>> 6250 RECORDS IN FILE MODEL2 <<<  
  
Related topics and activities

  * [TDOUT Process](<tdout.md>)