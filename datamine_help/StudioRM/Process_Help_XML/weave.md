# WEAVE Process

To access this process:

  * **Data** ribbon **> > Data Tools >> Relational >> Weave**.

  * Enter "WEAVE" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **WEAVE** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_W.md#WEAVE>).

## Process Overview

Join two sorted files on designated keyfields. Matching input fields and all records are output.

This process belongs to a group of four similar ones within the Datamine process collection; JOIN, SUBJOI, WEAVE and SUBWVE. Each provides a different outcome, as described by the following diagram:

  
[![](../Images/JOIN_SUBJOIN_WEAVE_SUBWEAVE.jpg)](<javascript:void\(0\);>)

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN1 |  First file to be updated (sorted on required keyfields). |  Input |  Yes |  Table  
IN2 |  Second file (update file) (sorted on required keyfields). |  Input |  Yes |  Table  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Table |  Output file.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
KEY1 |  Keyfield 1 for matching on. |  IN1, IN2 |  Yes |  Any |  Undefined  
KEY2 |  Keyfield 2. |  IN1, IN2 |  No |  Any |  Undefined  
kEY3 |  Keyfield 3. |  IN1, IN2 |  No |  Any |  Undefined  
KEY4 |  Keyfield 4. |  IN1, IN2 |  No |  Any |  Undefined  
KEY5 |  Keyfield 5. |  IN1, IN2 |  No |  Any |  Undefined  
KEY6 |  Keyfield 6. |  IN1, IN2 |  No |  Any |  Undefined  
KEY7 |  Keyfield 7. |  IN1, IN2 |  No |  Any |  Undefined  
KEY8 |  Keyfield 8. |  IN1, IN2 |  No |  Any |  Undefined  
KEY9 |  Keyfield 9. |  IN1, IN2 |  No |  Any |  Undefined  
KEY10 |  Keyfield 10. |  IN1, IN2 |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
KEYTOL |  **KEYTOL** is the tolerance value used to test whether numeric key values are equal. It must be greater than or equal to zero. It replaces the previous heuristic comparison method.  If **KEYTOL** is set to a negative value then zero is used.  In a macro **KEYTOL** can be set to absent using -. "@**KEYTOL** =-" This will revert to legacy behaviour and use a heuristic comparison in relational commands and zero in sort.  |  No |  0.00001 |  0,+ |  Undefined  
  
Related topics and activities

  * [JOIN Process](<join.md>)

  * [SUBJOI Process](<subjoi.md>)

  * [SUBWVE Process](<subwve.md>)