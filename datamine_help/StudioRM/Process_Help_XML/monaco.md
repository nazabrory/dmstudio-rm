# MONACO Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics Processes >> Generate Random Numbers**.

  * Enter "MONACO" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MONACO** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MONACO>).

## Process Overview

Create random numbers.

**Note** : this process is retained for legacy macro support only. Consider using the **[RANDOM](<random.md>)** process instead.

MONACO requires only an OUT file specification and NRECS to determine how many random number records to create. This file is populated by further information supplied by you when the process is run.

To generate random number output with MONACO:

  1. Run the **MONACO** process.

  2. Enter the **OUT** file name. This file is generated in your project folder with either a .dm or .dmx extension.

  3. Select the Parameters tab.

  4. Enter the number of records (NRECS) to create in the output file.

  5. Click **OK** to launch the process.

  6. In the **Output** window, enter the name of the **FIELD** to create in the output file. This numeric field will contain random value records, one per row where the total number of rows = **NRECS**.

  7. Choose a random distribution **TYPE** from the following options:

     * 1 UNIFORM IN RANGE 0 TO 1
     * 2 EXPONENTIAL WITH PARAMETER P1
     * 3 NORMAL, MEAN P1, STDEV P2
     * 4 LAPLACE, MEAN P1, SPREAD P2
     * 5 EXTREME VALUE, PARAMETERS P1,P2
     * 6 CAUCHY, CENTRE P1, SPREAD P2
     * 7 LOGNORMAL, LOG MEAN P1, LOG STDEV P2
  8. If another **FIELD** is required in the output file (for additional random values), repeat steps 6 and 7.

  9. Enter "!" and press ENTER to create the file.

**Note** : you can also generate random numbers using the **[EXTRA](<extra.md>)** process.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output file  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
NRECS |  Number of records required in output file | Yes | Undefined | Undefined | Undefined  
  
## Example 
    
    
    !MONACO $OUT(myFile), @NRECS(5)  
  
---  
      
    
    NEXT  
      
    
    FIELD > MYFIELD  
      
    
    >>> DISTRIBUTION TYPES AVAILABLE ARE --         <<<  
      
    
    >>>     1  UNIFORM IN RANGE 0 TO 1              <<<  
      
    
    >>>     2  EXPONENTIAL WITH PARAMETER P1        <<<  
      
    
    >>>     3  NORMAL, MEAN P1, STDEV P2            <<<  
      
    
    >>>     4  LAPLACE, MEAN P1, SPREAD P2          <<<  
      
    
    >>>     5  EXTREME VALUE, PARAMETERS P1,P2      <<<  
      
    
    >>>     6  CAUCHY, CENTRE P1, SPREAD P2         <<<  
      
    
    >>>     7  LOGNORMAL, LOG MEAN P1, LOG STDEV P2 <<<  
      
    
    DISTRIB> 1  
      
    
    NEXT  
      
    
    FIELD > !  
      
    
    >>>       5 Records in File:  
      
    
    C:\myProjectFolder\myfile.dm  
      
    
    >>> MONACO   Complete <<<