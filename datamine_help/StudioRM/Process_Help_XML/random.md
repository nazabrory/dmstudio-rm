# RANDOM Process  
  
To access this process:

  * Enter "RANDOM" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **RANDOM** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_R.md#RANDOM>).

## Process Overview

Generate random numbers. RANDOM is similar to (and supersedes) the legacy **[MONACO](<monaco.md>)** process.

The type of random distribution is primarily dictated by DISTRIB. Each option supports either one or two parameters (P1 and P2).

  * 1Produce random numbers using a **uniform** distribution with minimum **P1** and maximum **P2**.

  * 2Produce random numbers using an **exponential** distribution with rate **P1**.

  * 3Produce random numbers using a **normal** distribution with mean **P1** and standard deviation **P2**.

  * 4Produce random numbers using a **Laplacian** distribution with location **P1** and scale parameter **P2**.

  * 5Produce random numbers using a **Weibull** distribution with shape parameter **P1** and scale parameter **P2**.

  * 6 Produce random numbers using a **Cauchy** distribution with location **P1** and scale parameter **P2**.

  * 7Produce random numbers using a **lognormal** distribution with log mean **P1** and log standard deviation **P2**.

**Note** : you can also generate random numbers using the **[EXTRA](<extra.md>)** process.

## Input Files

## Output Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
OUT |  Output file containing random values. | Output |  Yes |  Table  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
OUTFIELD |  Field to write the random variables into. |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
NRECS |  Number of records required in output file |  Yes |  1 |  Undefined | Undefined  
DISTRIB |  Type of distribution to use to generate random numbers. See "Distribution Options" above. | Yes | 1 | 1,7 | 1,2,3,4,5,6,7  
P1 | First parameter of the chosen distribution.  | Yes | 0 |  Undefined | Undefined  
P2 | Second parameter of the chosen distribution. Ignored if **DISTRIB** =2. | No | 1 |  Undefined | Undefined  
SEED | Random number seed. If the same non-zero seed is used for multiple runs then the same set of random numbers will be generated. If **SEED** is zero, subsequent results with the same parameters will differ. | No | 0 |  Undefined | Undefined  
  
Related topics and activities

  * [MONACO](<monaco.md>)

  * [EXTRA Process](<extra.md>)