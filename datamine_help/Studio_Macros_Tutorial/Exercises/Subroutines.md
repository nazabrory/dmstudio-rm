![](../HeaderCell.jpg) |  Subroutines Using subroutines in a macro.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the use of subroutines in a macro.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro3.mac

## Exercise: Including Subroutines in a Macro

In this exercise, you are going to create a working copy of the existing macro file _Macro3.mac, replace the existing three macros in the macro file with a single macro consisting of three subroutines and then save it to a new file Macro4.mac.

This will include the following tasks:

  * Inserting calls to three new subroutines and an end label at the start of the macro

  * Insert an end label

  * Inserting a subroutine label at the start of each block of subroutine macro code (x3)

  * Inserting return commands at the end of each block of subroutine macro code (x3)

  * Keeping the first !START and last !END macro commands.

![note.gif \(1017 bytes\)](../Images/note.gif) |  Why Subroutines? Subroutines within macros allow:

  * macros to be broken down into manageable blocks of code when writing, testing and error fixing
  * the same sequence of commands to be used several times from different points in the macro without having to repeat the commands
  * allow flexible program flow control and branching when used in conjunction with conditional statements

What Format do Subroutines Have? Subroutines are added to macros using the following format:

  * are called by a !GOSUB <subroutinename> macro command
  *     * where <subroutinename> = label + ':' + macro command e.g. !SUB1:REM
    * <subroutinename> is a maximum of 16 characters long
  * end with a !RETURN macro command.

  
---|---  
  
![](../Images/Tip.gif) |  When subdividing a macro into subroutines, try to restrict a subroutine to performing, within reason:

  * either a moderate length single function i.e. a coherent group of processes
  * or a group of small functions.

  
---|---  
  
**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro3 and selectEdit.  
  
![](../Images/mac_Subroutines%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro4.mac' and click Save.  
  
![](../Images/mac_Subroutines%202.gif)
  6. Check that this new file Macro4.mac is open in the Notepad dialog and contains the listing shown below:  
  
![](../Images/mac_Subroutines%203.gif)

**Add ing the calls to the subroutines**

  1. In the Macro4.mac - Notepad dialog, line 1, click in the listed macro text immediately to the right of !START 1 Block Modeling.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last one, with <Enter>:  
  
# ====================================================================  
# Subroutine Calls  
# ====================================================================  
  
!GOSUB SUB1  
  
!GOSUB SUB2  
  
!GOSUB SUB3  
  
!GOTO THE_END  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The fourth call uses !GOTO and not !GOSUB, as the macro will not be returning from the end label.  
---|---  
  4. Check that your macro listing contains the additional lines, including blank lines, as highlighted below:  
  
![](../Images/mac_Subroutines%204.gif)

**Add ing the first subroutine's label and return**

  1. In the Macro4.mac - Notepad dialog, line 17, click in the listed macro text immediately to the right of the last =.
  2. Press <Enter> twice, to insert two blank lines.
  3. Type in type in '!SUB1:REM'.
  4. On line 36, select !END and type in '!RETURN'.
  5. Check that your macro listing contains the additional and modified lines, including blank lines, as highlighted below:  
  
![](../Images/mac_Subroutines%205.gif)

**Add ing the remaining subroutines' labels and returns**

  1. In the Macro4.mac - Notepad dialog, line 42, select !START 2 Grade Estimation and type in '!SUB2:REM'.
  2. On line 63, select !END and type in '!RETURN'.
  3. On line 69, select !START 3 Cleanup and type in '!SUB3:REM'.
  4. On line 77, click in the listed macro text immediately to the right of !DELETE &IN(x4),@CONFIRM=0.0.
  5. Press <Enter> twice, to insert two blank lines.
  6. Type in type in '!RETURN'.
  7. Press <Enter> twice, to insert two blank lines.
  8. Type in type in '!THE_END:REM'.
  9. Check that your macro listing contains the modified and additional lines highlighted below:  
  
![](../Images/mac_Subroutines%206.gif)

**Tidying up the start and end of the macro**

  1. In the Macro4.mac - Notepad dialog, line 1, select Block Modeling and type in 'Grade Est Stats'.
  2. On line 1, check that the macro only contains one !START.
  3. On line 83, check that the macro only contains one !END.

**Saving the modified macro file**

  1. In the Macro4.mac - Notepad dialog, select File | Save.

  2. In the Macro4.mac - Notepad dialog, select File | Exit.  

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro4.mac can be checked against the example _Macro4.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro4.mac and then click Open.  
  
![](../Images/mac_Subroutines%207.gif)  

  5. In the Command control bar, note that your application finds and runs the single macro i.e. macro name '1', in the modified macro file.
  6. Check the output in the Command control bar and make sure that all processes listed in the macro file have been run successfully and that the four temporary files have been deleted.

**![](../Images/UpArrow.gif)**Top of page