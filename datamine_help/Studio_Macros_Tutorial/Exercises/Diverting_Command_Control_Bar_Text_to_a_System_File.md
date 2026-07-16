# Diverting Command Control Bar Text to a System File

![](../HeaderCell.jpg) |  Diverting Command Control Bar Text to a System File How to divert Command control bar text to a system file during macro runtime.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the tools and techniques used to divert the text displayed in the Command control bar to a system file when a macro runs.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro12.mac

![note.gif \(1017 bytes\)](../Images/note.gif) |  Why Divert Command Control Bar Text? Diverting the Command control bar text provides the ability to:

  * significantly reduce the amount of text, associated with the running of processes, being displayed in the Command control bar
  * while at the same time, only displaying the prompts and messages.

What Text Diversion Commands Are There? Text diversion is controlled by the following macro commands:

  * SCROFF to divert Command control bar text output into a system file during macro execution
  * SCRON to restore Command control bar text output previously diverted by a SCROFF command..

Notes:

  * SCROFF requires a preceding ONERR or HOLD
  * The diverted text is stored in the system text file errorlog.dat, which is located in the project folder
  * Multiple SCROFF and SCRON commands can be used in a single macro.

What Format does the Text Diversion Command take?

  * General format:  
  
!START 1  
  
<required macro command> # prerequisite  
  
!SCROFF # optional - diverts text output to a system file  
  
<statements1>  
  

  * Where:  
  
<required macro command> ONERR or HOLD must precede SCROFF  
  
<statements1> the main body of the macro containing the processes or macro commands

  * Example1:  
  
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

  * Example2:  
  
!START 1  
  
!HOLD  
  
!SCROFF  
  
<statements1>

  
---|---  
  
## Exercise: Diverting Command Control Bar Text to a System File

In this exercise, you are going to create a working copy of the existing macro file _Macro12.mac, include the Command control bar text diversion command and then save the modified macro to a new file Macro13.mac.

This will include the following tasks:

  * Inserting the Command control bar text diversion instruction using the SCROFF macro command

  * Running the macro with the text diversion

  * Viewing the contents of the log file.

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro12 and selectEdit.  
  
![](../Images/mac_DivertingText%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro13.mac' and click Save.  
  
![](../Images/mac_DivertingText%202.gif)
  6. Check that this new file Macro13.mac is open in the Notepad dialog and contains the general listing show below:  
  
![](../Images/mac_DivertingText%203.gif)

Insert**ing the Command control bar text diversion command**

  1. In the Macro13.mac - Notepad dialog, line 7, click in the listed macro text immediately to the right of !ONERR GOTO SUBERR.
  2. Press <Enter> twice.
  3. Type in the macro line shown below:  
  
!SCROFF
  4. Check that your new text diversion code contains the modified lines highlighted below:  
  
![](../Images/mac_DivertingText%204.gif)

**Saving the modified macro file**

  1. In the Macro13.mac - Notepad dialog, select File | Save.

  2. In the Macro13.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro13.mac can be checked against the example _Macro13.mac.  
---|---  
  
**Testing the Text Diversion**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run MacroSelect _T_ ools | _M_ acro | _R_ un Macro... or click Run Macro.
  4. In the Select File dialog, select the file name Macro13.mac and then click Open.  
  
![](../Images/mac_DivertingText%205.gif)  

  5. In the Command control bar, use the values for all the prompts as shown below:  
  
![](../Images/mac_DivertingText%206.gif)
  6. In the Command control bar, note that the macro has run without listing all the processes output text as was happening previously; only the various subroutine, grade estimation and summary statistics report messages have been displayed, as shown in the images below:  
  
![](../Images/mac_DivertingText%207.gif)  
  
  
![](../Images/mac_DivertingText%208.gif)

**Viewi ng the contents of the log file in Notepad**

  1. In a Windows Explorer dialog, browse to C:\Database\DMTutorials\Projects\S3MacrosTut\ProjFiles\MyProj1.
  2. Right-click the fileerrorlog.datand selectOpen With....  
  
![](../Images/mac_DivertingText%209.gif)
  3. If the Caution dialog is displayed, click Open With....  
  
![](../Images/mac_DivertingText%2010.gif)  

  4. In the Windows dialog, select the Select the program from a list option and then click OK.  
  
![](../Images/mac_DivertingText%2011.gif)
  5. In the Open With dialog, select [Notepad] and then click OK.  
  
![](../Images/mac_DivertingText%2012.gif)
  6. In the errorlog.dat - Notepad dialog, note the process output text as shown below:  
  
![](../Images/mac_DivertingText%2013.gif)
  7. In the errorlog.dat - Notepad dialog, select File | Exit.  
  

In the above example, the macro was run without error; when a macro runs with an error and the error is handled by the ONERR error trap, the details of the error message(s) can also be found in this log file. 

![note.gif \(1017 bytes\)](../Images/note.gif)| The contents of this log file are overwritten each time a macro runs.  
---|---  

**![](../Images/UpArrow.gif)**Top of page