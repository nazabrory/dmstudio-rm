# Using an Operating System Command Prompt in Macros

![](../HeaderCell.jpg) |  Using an Operating System Command Prompt in Macros How to use the operating system's Command Prompt commands in a macro.  
---|---  
  
# Overview

This portion of the tutorial will introduce you to the commands and techniques used to run commands in a Command Prompt dialog from within a macro.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro15.mac

![note.gif \(1017 bytes\)](../Images/note.gif) |  Why run Command Prompt commands from a macro? Running these commands from macros provides the ability to:

  * Manipulate system files using the Command Prompt commands.
  * Run programs in the Command Prompt from within a macro.

What Command is used to run the Command Prompt dialog?

  * General format:  
  
!OPSYS  
<commands>  

  * Where:  
  
<commands> are Command Prompt commands, executables or batch files  

  * Example  
  
!OPSYS  
copy errorlog.dat macro_error_log.txt  

  * Command Prompt
  *     * The operating system's Command Prompt can be run outside of your application by selecting Start | All Programs | Accessories | Command Prompt
    * Please see the Command Prompt's help file for further details of its available commands

  
---|---  
  
## Exercise: Running Commands in the Operating System's Command Prompt

In this exercise you are going to create a local copy of the macro file _Macro15.mac by saving it to the file Macro19.mac . You will then include operating system Command Prompt commands to create and view an error log text file. This includes the following steps:

  * creating a local copy of the macro file

  * including an OPSYS macro command

  * including Command Prompt commands

  * running the macro with an error

**Creat ing a local copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro15 and selectEdit.  
  
![](../Images/mac_CommandPrompt%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro19.mac' and click Save.  
  
![](../Images/mac_CommandPrompt%202.gif)
  6. In the Macro19.mac - Notepad dialog, check that it contains the listing show below:  
  
![](../Images/mac_CommandPrompt%203.gif)

Insert**ing the OPSYS and Command Prompt commands**

  1. In the Macro19.mac - Notepad dialog, line 301, click in the listed macro text immediately to the right of:   
  
0 SUBERR: An Error has occurred ...
  2. Press <Enter> twice.
  3. Type in the macro lines (NO internal blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!OPSYS  
copy errorlog.dat macro_error_log.txt  
notepad macro_error_log.txt
  4. Check that your modified macro contains the lines highlighted below:  
  
![](../Images/mac_CommandPrompt%204.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * OPSYS can also be used to view Datamine files (*.dm) using e.g.:  
  
!OPSYS  
samples.dm
     * Files are opened using the program that is typically associated with that type of file.
     * These files need to be located in the project folder if a path is not included in the filename.
     * In a similar manner as shown above, other types of files can be opened with their respective programs.
     * Please see the operating system's Command Prompt help for further details on how to use other commands.   
---|---  

**Saving the modified macro file**

  1. In the Macro19.mac - Notepad dialog, select File | Save.

  2. In the Macro19.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro19.mac can be checked against the example _Macro19.mac.  
---|---  
  
**Testing the modified macro**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run MacroSelect _T_ ools | _M_ acro | _R_ un Macro... or click Run Macro.
  4. In the Select File dialog, select the file name Macro19.mac and then click Open.  
  
![](../Images/mac_CommandPrompt%205.gif)  

  5. In the Command toolbar type in 'samples2' when prompted for the sample file name.  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| This file does not exist and will cause an error when the macro runs.  
---|---  
  6. In the Command toolbar, press <Enter> to accept the default values for the block model parameters and temporary file deletion prompts:  
  
![](../Images/mac_CommandPrompt%206.gif)
  7. The macro continues running and the following Command Prompt and Notepad dialogs are displayed:  
  
![](../Images/mac_CommandPrompt%207.gif)  
  
  
![](../Images/mac_CommandPrompt%208.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * The running of the program Notepad.exe, from the Command Prompt, interrupts the running of the macro.
     * The macro only continues running when the Notepad dialog is closed.
     * The file macro_error_log.txt is located in the project folder.  
---|---  
  8. The macro_error_log.txt - Notepad dialog displays the contents of the macro_error_log.txt file which shows the details of the macro error which has been handled by the macros error trap i.e. routine SUBERR:  
  
![](../Images/mac_CommandPrompt%209.gif)
  9. In the Macro19.mac - Notepad dialog, select File | Exit.

  10. Note that when the Notepad dialog and then the Command Prompt dialog close, that the macro then finishes running.

**![](../Images/UpArrow.gif)**Top of page