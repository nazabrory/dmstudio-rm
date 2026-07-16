![](../HeaderCell.jpg) |  Error Trapping Trapping errors in a macro at runtime.  
---|---  
  
# Overview

This portion of the tutorial will introduce you to the commands used to trap errors in a running macro.

Why Trap Errors?

Error trapping provides the ability to:

  * transfer the control of a running macro to a specified macro label when a Datamine fatal error occurs

  * stop the macro from unnecessarily processing data any further after a fatal error has occurred.

What Error Trapping Commands Are There?

Errors can be trapped using the following command:

  * ONERR to transfer control to a given label if a DATAMINE fatal error occurs

  * The addition of SCROFF will allow more advanced error trapping (see below).

What Errors are Trapped?

The following errors are trapped at runtime:

  * ONERR only : missing files, missing or incorrect parameters

  * ONERR and SCROFF : in addition to the above, command syntax errors can also be trapped.

What Format does the Error Trap take?

  * Standard format:  
  
!START 1  
  
!ONERR goto <label> # set the error trap  
  
<statements1>  
  
!<label>:REM # error handling subroutine  
  
<statements2> # error handling messages and commands  

  * Advanced format:  
  
!START 1  
  
!ONERR goto <label> # set the error trap  
  
!SCROFF # optional - diverts text output to a system file  
  
<statements1>  
  
!<label>:REM # error handling subroutine  
  
<statements2> # error handling messages and commands

  * Where:  
  
<label> is a command label used to indicate the error handling subroutine  
  
<statements1> the main body of the macro containing the processes or macro commands  
  
<statements2> the processes or macro commands used in handling the error (typically consists of a message and then a macro exit command)

  * Example1:  
  
!START 1  
  
!ONERR goto SUBERR  
  
<statements1>  
  
!SUBERR:REM  
  
!PROMPT  
0 An Error has occurred in subroutine $SUB# ...  
  
!GOTO THE_END  
  
<statements1>  
  
!THE_END:END

  * Example2:  
  
!START 1  
  
!ONERR goto SUBERR  
  
!SCROFF  
  
<statements1>  
  
!SUBERR:REM  
  
!PROMPT  
0 An Error has occurred in subroutine $SUB# ...  
  
!GOTO THE_END  
  
<statements1>  
  
!THE_END:END

Macro Validation vs Error Traping?

  * Macro validating and debugging tools are meant to be used to identify macro code errors e.g. syntax errors, during the macro design and writing phase

  * Error trapping is meant to used during runtime to trap errors resulting from missing or incorrect file names and parameters which may occur as a result of incorrect user input.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro11.mac

## Exercise: Trapping Errors in a Macro

In this exercise, you are going to create a working copy of the existing macro file _Macro11.mac, include the error trap and error handling routine, and then test the error handler . The modified macro will be saved to a new file Macro12.mac.

This will include the following tasks:

  * Inserting the error trap using the ONERR macro command.

  * Inserting a new error handling routine.

  * Testing the error trap.

  * Running a macro without an error trap.

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro11 and selectEdit.  
  
![](../Images/mac_ErrorTrap%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro12.mac' and click Save.  
  
![](../Images/mac_ErrorTrap%202.gif)
  6. Check that this new file Macro12.mac is open in the Notepad dialog and contains the general listing shown below:  
  
![](../Images/mac_ErrorTrap%203.gif)

Insert**ing the error trap**

  1. In the Macro12.mac - Notepad dialog, line 1, click in the listed macro text immediately to the right of !START 1 Grade Est Stats.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# ====================================================================  
# Error Trap  
# ====================================================================  
  
!ONERR goto SUBERR
  4. Check that your new error trap code contains the lines (including blank lines) highlighted below:  
  
![](../Images/mac_ErrorTrap%204.gif)

**Insert ing the error handling routine**

  1. In the Macro12.mac - Notepad dialog, line 266, click in the listed macro text immediately to the right of !RETURN i.e. at the end of subroutine 3.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# ====================================================================  
# Error Handling Routine  
# ====================================================================  
  
!SUBERR:REM  
  
!PROMPT  
0 SUBERR: An Error has occurred ...  
  
!GOTO THE_END
  4. Check that your new error handling subroutine contains the lines (including blank lines) highlighted below:  
  
![](../Images/mac_ErrorTrap%205.gif)

**Saving the modified macro file**

  1. In the Macro12.mac - Notepad dialog, select File | Save.

  2. In the Macro12.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro12.mac can be checked against the example _Macro12.mac.  
---|---  
  
**Testing the Error Trap**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run MacroSelect _T_ ools | _M_ acro | _R_ un Macro... or click Run Macro.
  4. In the Select File dialog, select the file name Macro12.mac and then click Open.  
  
![](../Images/mac_ErrorTrap%206.gif)  

  5. In the Command toolbar type in 'samples2' when prompted for the Sample Filename.
  6. In the Command toolbar, press <Enter> to accept each of the default values for the block model parameters.
  7. Press <Enter> to accept the default for the Delete temporary files? N/[Y] prompt:  
  
![](../Images/mac_ErrorTrap%207.gif)
  8. In the Command control bar, note that the errors have been detected, details of the errors listed, then trapped and handled by the error routine i.e. the 'An Error has occurred ...' message was displayed, before the macro was ended:  
  
![](../Images/mac_ErrorTrap%208.gif)

**![](../Images/UpArrow.gif)**Top of page