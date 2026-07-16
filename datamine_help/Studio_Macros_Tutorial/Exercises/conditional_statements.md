![](../HeaderCell.jpg) |  Conditional Statements Controlling program flow with conditional statements.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the simple and blocked conditional statements used to control program flow in a macro. Please complete the exercises in the order shown below, as the second exercise on this page uses the results from the first exercise.

Why Use Conditional Statements?

Conditional statements provide the ability to:

  * provide enhanced program control

  * have flexible functionality by being able to cater for different options or scenarios

What Format do Conditional Statements Have?

Conditional statements can have one of the following general formats:

  * Simple IF command:  
  
!IF <condition>, ...,GOTO <Label>  
  
!IF <Variable> <Op> <Value>, ...,GOSUB <Label>  
  
!IF <Variable> <Op> <Value>, ..., LET <Variable>=<Value>/<Variable>  

  * Basic Blocked IF command:  
  
!IF <Variable> <Op> <Value>, ...,THEN  
<Process>/<Command>  
<Process>/<Command>  
...  
!ENDIF  

  * Advanced Blocked IF command:  
  
!IF <Variable> <Op> <Value>, ...,THEN  
<Process>/<Command>  
<Process>/<Command>  
...  
!ELSEIF <Variable> <Op> <Value>, ...,THEN  
<Process>/<Command>  
<Process>/<Command>  
...  
!ELSE  
<Process>/<Command>  
<Process>/<Command>  
...  
!ENDIF  

  * Where:

  *     * <Variable> is a substitution variable

    * <Op> is an operator from the set =,>,<,>=,<= or <>(not equals)

    * <Value> is either a constant (alphanumeric or numeric) or another variable 

    * <Label> is a command label

    * <Process>/<Command> is a process or macro command.

  * Notes:

  *     * multiple tests can be set in an IF ..., ... statement

    * multiple variables can be set in the IF... ,LET ... statement

    * multiple processes or commands can be listed in the IF... ,THEN ... ENDIF statement

    * if you use more than one condition then all conditions must be satisfied.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro7.mac

## Links to exercises

The following exercises are available on this page:

  * Controlling Program Flow using a Blocked Conditional Statement

  * Controlling Program Flow using a Simple Conditional Statement

## Exercise: Controlling Program Flow using a Blocked Conditional Statement

In this exercise, you are going to create a working copy of the existing macro file _Macro7.mac, include a conditional statement to control the loading of the substitution variables file MacTut.var and then save it to a new file Macro8a.mac.

This will include the following tasks:

  * Inserting a check for the system file MacTut.var using the SYSFILE macro command

  * Inserting a conditional statement using the blocked IF ... THEN macro command

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro7 and selectEdit.  
  
![](../Images/mac_ConditionalStatements%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro8a.mac' and click Save.  
  
![](../Images/mac_ConditionalStatements%202.gif)
  6. Check that this new file Macro8a.mac is open in the Notepad dialog and contains the general listing show below:  
  
![](../Images/mac_ConditionalStatements%203.gif)

Includ**ing the check for the variable file and the conditional statement**

  1. In the Macro8a.mac - Notepad dialog, line 29, click in the listed macro text immediately after the last = at the end of the third row of the header:  
  
# ====================================================================  
# Load Substitution Variables File  
# ====================================================================
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!SYSFILE $exists1#=MacTut.var  
  
!IF $exists1#=1,THEN
  4. In line 35, immediately before the '!' in !VARLOAD MacTut.var, @MERGE=1, press <Spacebar> four times to indent the line.
  5. In line 35, click in the listed macro text immediately to the right of !VARLOAD MacTut.var, @MERGE=1.
  6. Press <Enter> twice.
  7. Type in the macro line shown below:  
  
!ENDIF
  8. Check that your modified loading substitution variables section contains the lines highlighted below:  
  
![](../Images/mac_ConditionalStatements%204.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * The list of macro commands and process that are used inside a blocked if statement are indented so that the macro code is easier to read.
     * In the above example the line is indented using four spaces.
     * Do NOT use <Tab> to space out or indent lines of code in a macro.  
---|---  

**Saving the modified macro file**

  1. In the Macro8a.mac - Notepad dialog, select File | Save.

  2. In the Macro8a.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro8a.mac can be checked against the example _Macro8a.mac.  
---|---  
  
**![](../Images/UpArrow.gif)**Top of page

## Exercise: Controlling Program Flow using a Simple Conditional Statement

In this exercise, you are going to create a working copy of the existing macro file _Macro8a.mac, include a conditional statement to control the deletion of the temporary files and then save it to a new file Macro8b.mac.

This will include the following tasks:

  * Inserting an additional prompt in the PROMPT command

  * Inserting a skip deletion label

  * Inserting a conditional statement using the simple IF ... ,GOTO ... macro command

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro8a and selectEdit.  
  
![](../Images/mac_ConditionalStatements%205.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Database\DMTutorials\Projects\S3MacrosTut\ProjFiles\MyProj1.
  5. Define a new File name: 'Macro8b.mac' and click Save.  
  
![](../Images/mac_ConditionalStatements%206.gif)
  6. Check that this new file Macro8b.mac is open in the Notepad dialog and contains the general listing shown below:  
  
![](../Images/mac_ConditionalStatements%207.gif)

**Insert ing an additional prompt**

  1. In the Macro8b.mac - Notepad dialog, line 64, click in the listed macro text immediately to the right of the last 0 in the set of PROMPT lines:  
  
!PROMPT  
...  
1 Z No Cells [$NX#] >'$NX#',n  
0
  2. Press <Enter> once only.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
0 Temporary File Deletion  
0 =======================  
0  
1 Delete temporary files? N/[Y] >'$YN1#',a,1,N,Y  
0
  4. Check that your modified prompt section contains the additional lines highlighted below:  
  
![](../Images/mac_ConditionalStatements%208.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| There should be NO blank lines between any of the display text lines or prompt lines in the body of the PROMPT statement.  
---|---  

Inserting the simple conditional statement and end command label

  1. In the Macro8b.mac - Notepad dialog, line 137, click in the listed macro text immediately after !SUB3:REM.
  2. Press <Enter> twice.
  3. Type in the conditional statement shown below:  
  
!IF $YN1#='N', GOTO SKIP_DEL
  4. In line 143, click in the listed macro text immediately to the right of !DELETE &IN(xcat),@CONFIRM=0.0.
  5. Press <Enter> twice.
  6. Type in the command label shown below:  
  
!SKIP_DEL:REM
  7. Go back to line 141, click in the listed macro text immediately to the left of !DIR &OUT(xcat),x?, press <Spacebar> four times to indent the line.
  8. Go to line 143, click in the listed macro text immediately to the left of !DELETE &IN(xcat),@CONFIRM=0.0, press <Spacebar> four times to indent the line.
  9. Check that your modified temporary files deletion section contains the additional and modified lines as highlighted below:  
  
![](../Images/mac_ConditionalStatements%209.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The combination of the conditional statement and the additional command label allows the deletion of temporary files to be skipped if the answer to the prompt is 'N'.  
---|---  

**Saving the modified macro file**

  1. In the Macro8b.mac - Notepad dialog, select File | Save.

  2. In the Macro8b.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro8b.mac can be checked against the example _Macro8b.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro8b.mac and then click Open.  
  
![](../Images/mac_ConditionalStatements%2010.gif)  

  5. Press <Enter> to accept the default values for the sample file name and block model parameters.
  6. In the Command control bar, note the additional temporary file deletion prompt .  
  
![](../Images/mac_ConditionalStatements%2011.gif)
  7. In the Command toolbar type in 'N' when prompted to delete the temporary files:  
  
![](../Images/mac_ConditionalStatements%2012.gif)
  8. In the Command control bar, check that the macro has run to completion without errors and that the temporary files have NOT been deleted i.e. that the last displayed output is from the LIST command:  
  
![](../Images/mac_ConditionalStatements%2013.gif)
  9. In the Project Files control bar, check that the temporary files are listed:  
  
![](../Images/mac_ConditionalStatements%2014.gif)
  10. Repeat steps 1. to 7., this time selecting the option to delete the temporary files.

**![](../Images/UpArrow.gif)**Top of page