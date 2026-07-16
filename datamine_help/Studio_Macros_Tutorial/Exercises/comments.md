![](../HeaderCell.jpg) |  Comments Including comments in a macro.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the techniques used to insert comments into macros.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro2.mac

## Exercise: Adding Comments to a Macro

In this exercise, you are going to create a working copy of an existing macro file, add two different types of comments to it and then save it to a new file Macro3.mac.

This will include the following tasks:

  * changing the macro names 'MOD', 'EST' and 'DEL' to '1', '2' and '3' and adding descriptions

  * adding explanatory notes to each of the three blocks of macro code:

![note.gif \(1017 bytes\)](../Images/note.gif) |  Why Add Comments? Comments are added to macros for the following reasons:

  * to give the macro name an additional macro description (macro name + spaces + macro description maximum length = 73 characters)
  * to provide the macro writer with the ability to include explanatory notes
  * to provide the macro editor or reader with explanatory notes to assist in understanding the functionality of the code

What Format do Comments Have? Comments are added to macros using either of the following two formats:

  * !REM <comment text>
  * # <comment text>

where

  * <comment text> is the text used to word the comment

  
---|---  
  
![](../Images/Tip.gif) | 

  * Insert a set of header comments in your macro which include the following details:
  *     * description of what the macro does
    * name of the original author(s)
    * date
    * customization history (when, who & what)

  * An example of such a set of comments is shown below:

#============================================================== # Macro Name : BlockMod.mac # Date : 2006/10/07 # Author : G. Eologist1 # Description : This macro allows a block model to be ... # Modification History: # 2006/10/07 G. Eologist1 # 1. Original coding # 2006/12/01 M. Engineer1 # 1. ( THE_END ) Included call to subroutine (GENMSG) # 2. ( CALC2 ) Added a second SORT to solve the ... #============================================================== !START

  * Make the total length of the 'border line' a total of 75 so that it serves as a visual guide for estimating the length of macro lines (the maximum macro line length is 80 characters, after substitution of variables). This will give you 5 spare characters!

#========1=========2=========3=========4=========5=========6=========7=====

  * This comment line can also be placed at regular intervals with the macro

  
---|---  
  
**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file _Macro2 and select Edit.  
  
![](../Images/mac_Comments%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro3.mac' and click Save.  
  
![](../Images/mac_Comments%202.gif)
  6. Check that this new file Macro3.mac is open in the Notepad dialog and contains the listing shown below:  
  
![](../Images/mac_Comments%203.gif)

**Add ing descriptions to macro names**

  1. In the Macro3.mac - Notepad dialog, line 1, select the macro name MOD in the listed macro text and replace it with '1'.
  2. Immediately to the right of !START 1, press <Spacebar> (x4) and then type in the macro description 'Block Modeling'.
  3. In the Macro3.mac - Notepad dialog, line 20, select the macro name EST in the listed macro text and replace it with '2'.
  4. Immediately to the right of !START 2, press <Spacebar> (x4) and then type in the macro description 'Grade Estimation'.
  5. In the Macro3.mac - Notepad dialog, line 43, select the macro name DEL in the listed macro text and replace it with '3'.
  6. Immediately to the right of !START 3 , press <Spacebar> (x4) and then type in the macro description 'Cleanup'.
  7. Check that your macro listing contains the modified lines as highlighted below:  
  
![](../Images/mac_Comments%204.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * In the above exercise steps, the original alpha macro names 'MOD', 'EST' and 'DEL' have been replaced with shorter numeric names '1', '2' and '3' respectively
     * In addition, a short macro description has been added after each macro name
     * This combination of a short numeric macro name and a macro description makes it quicker to run a required macro and can be used to set up a simple menu system for multiple macros in a single macro file.  
---|---  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * The status bar at the bottom right margin of the Notepad dialog displays the number of the line on which the cursor is located, as highlighted below:  
  
![](../Images/mac_Comments%205.gif)  

     * Use this display or Edit | Go To ... to assist you in navigating to the correct line.
     * If the Status Bar is not displayed, it can be turned on by selecting View | Status Bar.  
---|---  

**Add ing explanatory notes in the body of the macro**

  1. In the Macro3.mac - Notepad dialog, line 1, click in the listed macro text immediately to the right of !START 1 Block Modeling.
  2. Press <Enter> twice to insert two blank lines.
  3. On the new line, type in '# ====================================================================' and press <Enter>.  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * The above line contains 70 characters i.e. including the '#' and the single space
     * The maximum number of characters per line of macro code is 80.  
---|---  
  4. On the new line, type in '# Calculate statistics and create prototype block model' and press <Enter>.
  5. On the new line, type in '# ===================================================================='.
  6. Check that your macro listing contains the additional lines, including blank lines, as highlighted below:  
  
![](../Images/mac_Comments%206.gif)
  7. In the Macro3.mac - Notepad dialog, line 24, click in the listed macro text immediately to the left of !START 2 Grade Estimation.
  8. Press <Enter> twice to insert two blank lines.
  9. Go back up to line 24, type in '# ====================================================================' and press <Enter>.
  10. On the new line, type in '# Estimate grade, calculate and display statistics' and press <Enter>.
  11. On the new line, type in '# ===================================================================='.
  12. Check that your macro listing contains the additional lines, including empty lines, as highlighted below:  
  
![](../Images/mac_Comments%207.gif)
  13. In the Macro3.mac - Notepad dialog, select lines 24 - 26, shown below, right-click and select Copy.  
  
# ====================================================================  
# Estimate grade, calculate and display statistics  
# ====================================================================
  14. In line 51, click in the listed macro text immediately to the left of !START 3 Cleanup.

  15. Press <Enter> twice to insert two blank lines.
  16. Go back to the start of line 51, click in column 1 and then right-click and select Paste.
  17. On line 52, select Estimate grade, calculate and display statistics and type in 'Delete temporary files'.
  18. Check that your macro listing contains the additional lines, including empty lines, as highlighted below:  
  
![](../Images/mac_Comments%208.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The above three sets of comments are only visible in the macro listing and are not displayed in the Command control bar when the macros are run.  
---|---  

**Saving the modified macro file**

  1. In the Macro3.mac - Notepad dialog, select File | Save.

  2. In the Macro3.mac - Notepad dialog, select File | Exit.  

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro3.mac can be checked against the example _Macro3.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro
  4. In the Select File dialog, select the file name Macro3.mac and then click Open.  
  
![](../Images/mac_Comments%209.gif)  

  5. In the Command control bar, note the displayed descriptions next to each of the three listed macros '1', '2' and '3', as highlighted below:  
  
![](../Images/mac_Comments%2010.gif)
  6. In the Command toolbar, Command line, type in '!' and then press <Enter>.  
  
![](../Images/mac_Comments%2011.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * '!' can be typed into any macro prompt dialog in order to stop execution of the macro
     * When running a macro which includes a description as shown in the above exercise, type in just the macro name e.g. '1', '2' or '3' at the prompt i.e. do not include the description.  
---|---  

**![](../Images/UpArrow.gif)**Top of page

![openbook.gif \(910 bytes\)](../Images/openbook.gif)|  Related Topics  
---|---  
| [Filename, Path and Variable Length limits](<../Principles/Filename,_Path_and_Variable_Length_Limits.md>)