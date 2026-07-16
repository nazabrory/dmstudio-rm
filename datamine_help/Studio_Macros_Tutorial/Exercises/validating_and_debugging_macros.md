![](../HeaderCell.jpg) |  Validating and Debugging Macros How to validate and debug macros.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools and techniques used to validate and debug macro code.

Why Validate Macros?

Validating macro code provides the ability to:

  * quickly check and validate new macro code, without actually running the macro

  * easily find macro code errors or problems in existing macro code.

What Macro Validating and Debugging Commands Are There?

Macros can be validated and debugged using the following commands:

  * PROMPT and '!!' to display current variable values

  * ECHO to display variable values (see Standard Topics > Messages > [Displaying Macro Messages](<messages.md#Exercise1>) exercise )

  * NOXRUN to validate the syntax of a macro.

Notes

  * NOXRUN stops checking when the first error is encountered and reported

  * NOXRUN checks the following:

  *     * process and macro command names

    * syntax elements of these processes or commands e.g. missing any of the following items '&', '@', '(', ')'

    * illegal characters in the syntax

  * NOXRUN does not check for the existence of filenames or fieldnames

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro4.mac

    * _Macro11.mac

## Links to exercises

The following exercises are available on this page:

  * Checking Variable Values using a PROMPT

  * Validating a Macro using NOXRUN

## Exercise: Checking Variable Values using a PROMPT

In this exercise, you are going to create a working copy of the existing macro file _Macro11.mac, run the macro and check the values of the current substitution variables. This will be done by:

  * Using a PROMPT macro command to display the current variable values.

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro11 and selectEdit.  
  
![](../Images/mac_ValidatingMacros%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro11Prompt.mac' and click Save.  
  
![](../Images/mac_ValidatingMacros%202.gif)
  6. Check that this new file Macro11Prompt.mac is open in the Notepad dialog and contains the general listing shown below:  
  
![](../Images/mac_ValidatingMacros%203.gif)
  7. In the Notepad dialog, select File | Exit.

**Us ing a PROMPT to display the current variable values**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run MacroSelect _T_ ools | _M_ acro | _R_ un Macro... or click Run Macro.
  4. In the Select File dialog, select the file name Macro11Prompt.mac and then click Open.  
  
![](../Images/mac_ValidatingMacros%204.gif)  

  5. In the Command toolbar type in '!!' when prompted for the Sample Filename:  
  
![](../Images/mac_ValidatingMacros%205.gif)
  6. In the Command control bar, note the list of variables and their current values:  
  
![](../Images/mac_ValidatingMacros%206.gif)
  7. Continue running the macro as normal, by pressing <Enter> to accept the default values for the sample file name, block model parameters' and deleting temporary files prompts.  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The use of '!!' at any point in a Prompt, allows the user to view a list of the current variables and does not disrupt the normal running of the macro when the user returns to replying to the prompts as normal.  
---|---  

## Exercise: Validating a Macro

In this exercise, you are going to create a working copy of the existing macro file _Macro4.mac, introduce errors, validate the macro and then correct the errors based on the validation feedback. This will include the following tasks:

  * Inserting errors into the existing macro

  * Running the NOXRUN validation process

  * Correcting the errors and rerunning the validation process.

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro4 and selectEdit.  
  
![](../Images/mac_ValidatingMacros%207.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Database\DMTutorials\Projects\S3MacrosTut\ProjFiles\MyProj1.
  5. Define a new File name: 'Macro4Error.mac' and click Save.  
  
![](../Images/mac_ValidatingMacros%208.gif)
  6. Check that this new file Macro4Error.mac is open in the Notepad dialog and contains the general listing shown below:  
  
![](../Images/mac_ValidatingMacros%209.gif)

Inserting Errors into the Macro

  1. In the Macro4Error.mac - Notepad dialog, line 7, click in the listed macro text immediately to the right of !GOSUB SUB1.
  2. Press <Backspace> once, to delete the '1'.
  3. In line 21, click in the listed macro text immediately to the right of !STATS &IN(samples),.
  4. Press <Backspace> once, to delete the ','.
  5. Check that the two errors have been inserted in the lines highlighted below:  
  
![](../Images/mac_ValidatingMacros%2010.gif)
  6. In the Macro4Error.mac - Notepad dialog, select File | Save.

**Validating the macro and correcting the first error**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. In the Command Toolbar, click Find Command.
  4. In the Find Command dialog, page down (x9), select noxrun and click Run.
  5. In the NOXRUN dialog, click OK.
  6. In the Select File dialog, select the file name Macro4Error.mac and then click Open.  
  
![](../Images/mac_ValidatingMacros%2011.gif)  

  7. In the Command control bar, note that the subroutine label error has been detected and reported:  
  
![](../Images/mac_ValidatingMacros%2012.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * Only the first error has been detected and reported.
     * NOXRUN needs to be run again, after the first error has been corrected, in order to detect the second error.  
---|---  
  8. In the Macro4Error.mac - Notepad dialog, line 7, click in the listed macro text immediately to the right of !GOSUB SUB.
  9. Type in '1'.
  10. Check that the first error has been corrected as highlighted below:  
  
![](../Images/mac_ValidatingMacros%2013.gif)
  11. In the Macro4Error.mac - Notepad dialog, select File | Save.

**Validating the macro and correcting the second error**

  1. Repeat steps 1. to 6. shown in the above section.  

  2. In the Command control bar, note that the second error has been detected and reported:  
  
![](../Images/mac_ValidatingMacros%2014.gif)
  3. In line 21, click in the listed macro text immediately to the right of !STATS &IN(samples).
  4. Type in ','.
  5. Check that the second error has been corrected in the line highlighted below:  
  
![](../Images/mac_ValidatingMacros%2015.gif)

  6. In the Macro4Error.mac - Notepad dialog, select File | Save.

  7. Select File | Exit.

**The final macro validation**

  1. Repeat steps 1. to 6. shown in the first section **Validating the macro and correcting the first error**.  

  2. In the Command control bar, note that all the macro commands and processes are listed without any errors:  
  
![](../Images/mac_ValidatingMacros%2016.gif)

**![](../Images/UpArrow.gif)**Top of page