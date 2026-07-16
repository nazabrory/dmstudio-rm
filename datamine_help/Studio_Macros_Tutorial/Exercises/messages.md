![](../HeaderCell.jpg) |  Messages Displaying macro messages in the Command control bar.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the macro command used to display macro messages in the Command control bar.

Why Use Macro Messages?

Macro messages provide the ability to:

  * display a line of text

  * display the value of a substitution variable

  * monitor the progress of a macro by displaying a simple message at key locations in the macro.

What Format do Macro Message Commands Have?

Messages can be displayed using one of the following commands:

  * ECHO command:  
  
!ECHO <Text>  
!ECHO  
!ECHO <Text> <Variable>  

  * PROMPT command:  
  
!PROMPT  
0  
0 <Text>  
0  
0 <Text> <Variable>

  * Where:

  *     * <Text> is a string of characters from the set 0-9, a-z and A-Z

    * <Variable> is a variable.

  * Examples  
  
!ECHO  
!ECHO Sample File  
!ECHO -----------  
!ECHO  
!ECHO Filename: $Var1#  
  
The above could also be done using:  
  
!PROMPT  
0  
0 Sample File  
0 -----------  
0  
0 Filename: $Var1#

![](../Images/Tip.gif) | 

  * Use the PROMPT macro command to display multiple message lines.
  * Use the ECHO macro command to display single message lines.

  
---|---  
  
## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro8b.mac

## Exercise: Displaying Macro Messages

In this exercise, you are going to create a working copy of the existing macro file _Macro8b.mac, include a set of messages to display the values of substitution variables, messages indicating macro progress and then save it to a new file Macro9.mac.

This will include the following tasks:

  * Inserting a set of messages displaying variables' values using the PROMPT macro command

  * Inserting macro progress messages using the ECHO macro command

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro8b and selectEdit.  
  
![](../Images/mac_Messages%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro9.mac' and click Save.  
  
![](../Images/mac_Messages%202.gif)
  6. Check that this new file Macro9.mac is open in the Notepad dialog and contains the general listing shown below:  
  
![](../Images/mac_Messages%203.gif)

Includ**ing the set of messages using the PROMPT command**

  1. In the Macro9.mac - Notepad dialog, line 37, click in the listed macro text immediately to the right of !ENDIF.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# ====================================================================  
# Display Substitution Variables' Values  
# ====================================================================  
  
!PROMPT  
0  
0 Loaded Variables' Values:  
0 =========================  
0  
0 Sample Filename: $INFILE1#  
0  
0 X Model Origin: $XMORIG#  
0 Y Model Origin: $YMORIG#  
0 Z Model Origin: $ZMORIG#  
0  
0 X Cell Size: $XINC#  
0 Y Cell Size: $YINC#  
0 Z Cell Size: $ZINC#  
0  
0 X No Cells: $NX#  
0 Y No Cells: $NY#  
0 Z No Cells: $NZ#  
0  
0 Delete temp files: $YN1#  
0
  4. Check that the additional message section contains the lines highlighted below:  
  
![](../Images/mac_Messages%204.gif)

Includ**ing the macro progress messages using the ECHO command**

  1. In the Macro9.mac - Notepad dialog, line 113, click in the listed macro text immediately to the right of !SUB1:REM.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!ECHO  
!ECHO SUB1: Calculate statistics and create prototype block model  
!ECHO
  4. In the Macro9.mac - Notepad dialog, line 140, click in the listed macro text immediately to the right of !SUB2:REM.
  5. Press <Enter> twice.
  6. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!ECHO  
!ECHO SUB2: Estimate grade, calculate and display statistics  
!ECHO
  7. In the Macro9.mac - Notepad dialog, line 171, click in the listed macro text immediately to the right of !SUB3:REM.
  8. Press <Enter> twice.
  9. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!ECHO  
!ECHO SUB3: Delete Temporary Files  
!ECHO
  10. In the Macro9.mac - Notepad dialog, line 191, click in the listed macro text immediately to the right of !THE_END:REM.
  11. Press <Enter> twice.
  12. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!ECHO  
!ECHO THE_END: Macro Finished...  
!ECHO
  13. Check that the additional messages have been included as highlighted below:  
  
![](../Images/mac_Messages%205.gif)  
  
![](../Images/mac_Messages%206.gif)

**Saving the modified macro file**

  1. In the Macro9.mac - Notepad dialog, select File | Save.

  2. In the Macro9.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro9.mac can be checked against the example _Macro9.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro9.mac and then click Open.  
  
![](../Images/mac_Messages%207.gif)  

  5. Press <Enter> to accept the default values for the sample file name, block model parameters and temporary file deletion prompts.

  6. In the Command control bar, note the message displaying the loaded variables' values:  
  
![](../Images/mac_Messages%208.gif)
  7. In the Command control bar, note the four macro progress messages:  
  
![](../Images/mac_Messages%209.gif)  
  
![](../Images/mac_Messages%2010.gif)  
  
![](../Images/mac_Messages%2011.gif)  
  
![](../Images/mac_Messages%2012.gif)

**![](../Images/UpArrow.gif)**Top of page