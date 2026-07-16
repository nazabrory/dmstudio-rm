![](../HeaderCell.jpg) |  Prompting for Data Using interactive prompts to set variable values in a macro.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the techniques used to set substitution variables in a macro through the use of interactive prompts.

Why Use Prompts?

Prompts provide the ability to:

  * interactively prompt the user for data

  * create simple interactive menus

  * provide enhanced program control

What Format do Prompts Have?

Prompt statements have the following general format:

  * Format:  
  
!PROMPT  
0 Prompt Heading Text  
0 =============  
0  
1 Prompt for alphanumeric value [Default] >'$Var1',a,8  
0   
1 Prompt for numeric value [Default] >'$Var3', n  
0   

  * Where:

  *     * 0 indicates a displayed line of text e.g. a blank line (no text after the '0'), heading or general message

    * 1 indicates a prompt

    * [Default] is the default value for the prompt. The default value needs to be within square brackets

    * '$Var1' indicates the name of the variable using the standard variable format

    * a,8 indicates that the variable is an alphanumeric character string of up to 8 characters

    * n indicates that the variable is numeric.

  * Notes:

  *     * a single PROMPT statement can contain multiple displayed text lines and prompts

    * variables can be used to replace text or defaults in the PROMPT statement e.g.  
  
1 $PromptText# [$Default1#] >'$Var1',a,8  

    * the above [$Default1#] is optional

    * the replies to prompts can be further restricted by including an optional list of permitted values, comma separated, after the variable alpha or numeric format e.g.  
  
1 Would you like to delete temporary files? N/[Y] >'$YN#',a,1,N,Y

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro6b.mac

## Exercise: Setting Variable Values Using Prompts

In this exercise, you are going to create a working copy of the existing macro file _Macro6b.mac, include a prompt section and then save it to a new file Macro7.mac.

This will include the following tasks:

  * Inserting a prompt using the PROMPT macro command

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro6band selectEdit.  
  
![](../Images/mac_Prompts%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro7.mac' and click Save.  
  
![](../Images/mac_Prompts%202.gif)
  6. Check that this new file Macro7.mac is open in the Notepad dialog and contains the general listing show below:  
  
![](../Images/mac_Prompts%203.gif)

Includ**ing the prompt statement**

  1. In the Macro7.mac - Notepad dialog, line 31, click in the listed macro text immediately to the right of !VARLOAD MacTut.var, @MERGE=1.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# ====================================================================  
# Prompt for Samples Filename and Block Model Parameters  
# ====================================================================  
  
!PROMPT  
0  
0 Samples File  
0 =============  
0  
1 Sample Filename [$INFILE1#] >'$INFILE1#',a,8  
0  
0 Block Model Parameters  
0 ======================  
0  
1 X Model Origin [$XMORIG#] >'$XMORIG#',n  
1 Y Model Origin [$YMORIG#] >'$YMORIG#',n  
1 Z Model Origin [$ZMORIG#] >'$ZMORIG#',n  
0  
1 X Cell Size [$XINC#] >'$XINC#',n  
1 Y Cell Size [$YINC#] >'$YINC#',n  
1 Z Cell Size [$ZINC#] >'$ZINC#',n  
0  
1 X No Cells [$NX#] >'$NX#',n  
1 Y No Cells [$NY#] >'$NY#',n  
1 Z No Cells [$NZ#] >'$NZ#',n  
0
  4. Check that your new prompt section contains the lines (including blank lines) as highlighted below:  
  
![](../Images/mac_Prompts%204.gif)

**Saving the modified macro file**

  1. In the Macro7.mac - Notepad dialog, select File | Save.

  2. In the Macro7.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro7.mac can be checked against the example _Macro7.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro7.mac and then click Open.  
  
![](../Images/mac_Prompts%205.gif)  

  5. In the Command control bar, note that your application finds and runs the single macro i.e. macro name '1', in the modified macro file.
  6. In the Command control bar, note that the macro is showing both the display text and first prompt line as highlighted below:  
  
![](../Images/mac_Prompts%206.gif)
  7. In the Command toolbar note that the command line is displaying the default value 'samples', as highlighted below:  
  
![](../Images/mac_Prompts%207.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * If for some reason you have selected another dialog or window e.g. the Command control bar, while the macro is prompting you for values, re-select the Command toolbar before continuing.
     * The thin blue line around the command line box indicates that it is ready to receive your input.  
---|---  
  8. Press <Enter> to accept this default value.
  9. Repeat steps 6. to 8. for the remaining prompts, using the default values.
  10. In the Command control bar, check that the macro has prompted for all 10 values highlighted below and that it has run to completion without errors:  
  
![](../Images/mac_Prompts%208.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The macro can be stopped by typing in '!' on the command line at any prompt.  
---|---  

**![](../Images/UpArrow.gif)**Top of page