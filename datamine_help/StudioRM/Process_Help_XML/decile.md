# DECILE Process

To access this process:

  * **Sample Analysis** ribbon **> > Statistics Processes >> Calculate Quantiles**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **DECILE** and click **Run**.
  * Enter "DECILE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_D.md#DECILE>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

Perform a decile analysis of a set of sample data.

**DECILE** retrieves samples above a supplied cut-off, they are sorted on grade, and then split into 10 bins, each representing one 'decile'. The average grade, maximum grade, minimum grade, total gold content and the proportion of the total gold content is then calculated for each bin. The top (90%+) bin is then further split into effective 1% bins and the calculations repeated. The results are stored in a system print file. The user has the option to add a topcut to the samples, and to use simple sample record selection if desired. Please see the related process [QUANTILE](<quantile.md>).

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input sample file |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PRIOUT |  Output |  Yes |  Undefined |  Output print file containing sample decile information.  
DECOUT |  Output |  No |  Table File |  Output file containing sample decile information. Not including the top 10% subsplit  
SPLITOUT |  Output |  No |  Table File |  Output file containing sample decile information. Including the top 10% subsplit  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Name of the field containing the grade to be processed. |  IN |  Yes |  Numeric |  Undefined  
SELECT |  Field containing the parameter for sample record selection. |  IN |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
CUTOFF |  Cutoff grade. |  No |  Undefined |  Undefined |  Undefined  
TOPCUT |  Apply a topcut to the file: 0 = No topcut applied. 1 = Topcut applied at grade defined in TCUTOFF |  No |  0 |  0,1 |  0,1  
TCUTOFF |  Grade to be applied as a topcut, if TOPCUT is set to 1. |  No |  Undefined |  Undefined |  Undefined  
CRITERIA |  Value to be used in sample record selection - SELECT. eg. If ROCK is the field entered in SELECT and 2 is the value entered in CRITERIA, then the Decile analysis will only take place on records where ROCK = 2. This value must be numeric. |  No |  Undefined |  Undefined |  Undefined  
  
Related topics and activities

  * [QUANTILE Process](<quantile.md>)