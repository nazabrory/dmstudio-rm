![](../HeaderCell.jpg) |  Working With Variables Defining and using substitution variables in a macro.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the techniques used to define, use, save and retrieve substitution variables in a macro. Please complete the exercises in the order shown below, as the second exercise on this page uses the results from the first exercise.

Why Use Variables?

Variables provide the ability to:

  * reuse portions of the macro code using a range of filenames, fieldnames, parameters and retrieval criteria

  * perform basic arithmetic calculations using variables

  * pass values from prompts to processes

  * provide enhanced program control

  * save and retrieve a set of values specific to a particular macro run

  * transfer variable values between macros or between macros and scripts.

What Format do Variables Have?

The following rules apply to the construction of variables:

  * Takes the general form '$x#', where 'x' is taken from the set 0-9, a-z and A-Z, i.e.

  *     * Starts with '$'

    * Contains numeric (integers) and/or alphanumeric characters

    * Ends with '#'

  * Ending with '#' prevents overlapping of variables e.g. '$1' is contained in '$11', which could potentially lead to incorrect substitution - changing these variables to '$1#' and '$11#' would prevent this

  * Alphanumeric characters are case sensitive in variables

  * Variables are a maximum of 16 characters long

  * When substituted, the length of the substituted variable should not exceed 72 characters

  * A maximum of 1000 variables can be defined in a macro

  * Variables can be used to replace any part of a macro command or process line, including the command or process itself

  * Variables can not be used to substitute labels.

How are Variable Values Set?

Variable values are typically set using the following macro commands:

  * LET

  * PROMPT

Examples

The following are general examples of variables set using LET:

!LET $Var1 = Assays Simple string setting  
!LET $Var2 = 'XYZ Project' Quotes are used if blanks are included  
!LET $Var3 = 35.4 Simple number setting  
!LET $Var4 = $Var1 Setting one variable to another  
!LET $Var5 = {$Var3 + 4.5} Simple arithmetic operation (permitted operators are +, -, * or /; enclose the expression in {})  
!LET $Var6 = SIN($Var3) Single value numeric function  
!LET $Var7 = MAX($Var3,$Var5) Two argument numeric function

  * Functions include:

  *     * general: INT, ABS, MOD, MAX, MIN.

    * power: EXP,SQRT, RAIS,

    * logarithmic: LOG, LOGN, LOGE.

    * trigonometric: SIN, COS, TAN, ASIN, ACOS, ATAN.

How are Variables Loaded and Saved?

Loading variables command:

  * general format:  
  
!VARLOAD <file>[,@MERGE=<merge>] [,@DESC=$dname#][ ,$varname# ...]  

  * where:

  *     * <file> is a system file path name up to 56 chars long.

    * If the parameter "MERGE" is not specified, or <merge> is zero, all current variables are erased.

    * If <merge> is 1, any variable that already exists in memory is updated with the file value, and new variables are added to those in memory.

    * Both <file> and <merge> may be substitution variables.

    * $varname# is a substitution variable to be loaded from <file>

    * The description supplied when the file was created can optionally be restored into a supplied variable <$dname>.

    * If the optional list of variables is given, only these variables are considered; otherwise all variables are loaded.

    * The list may be extended onto as many lines as necessary; continuation is implied by ending the previous line with a comma.

Saving variables command:

  * general format  
  
!VARSAVE <file>[,@MERGE=<merge>] [,@DESC=<description>][ ,$name# ...]  

  * where:

  *     * <file> is a system file path name up to 56 chars long.

    * If the parameter "MERGE" is not specified, or <merge> is zero, all contents of <file> are cleared first.

    * If <merge> is 1, any variable that already exists in the file is updated with the current macro value, and new variables are added to the file.

    * Both <file> and <merge> may be substitution variables.

    * $varname# is a substitution variable to be saved to <file>

    * A description for the contents of the file can be supplied.

    * The description is stored on the first record of the file with the revision number, and can be up to 68 characters long.

    * Quotes may be used enclose the description.

    * If the optional list of variables is given, only these variables are considered; otherwise all variables are saved.

    * The list may be extended onto as many lines as necessary; continuation is implied by ending the previous line with a comma.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro5.mac

    * _Macro6a.mac

## Links to exercises

The following exercises are available on this page:

  * Defining and Using Variables

  * Saving and Retrieving Variables

## Exercise: Defining and Using Variables

In this exercise, you are going to create a working copy of the existing macro file _Macro5.mac, include variable definition commands, modify existing processes to use these variables then save it to a new file Macro6.mac.

This will include the following tasks:

  * Defining variables using the LET command

  * Replacing existing portions of processes to make use of these variables.

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro5 and selectEdit.  
  
![](../Images/mac_WorkingWithVariables%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro6a.mac' and click Save.  
  
![](../Images/mac_WorkingWithVariables%202.gif)
  6. Check that this new file Macro6a.mac is open in the Notepad dialog and contains the general listing show below:  
  
![](../Images/mac_WorkingWithVariables%203.gif)

**Defin ing the variables**

  1. In the Macro6a.mac - Notepad dialog, line 1, click in the listed macro text immediately to the right of !START 1 Grade Est Stats.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# ====================================================================  
# Define Variables  
# ====================================================================  
  
!LET $INFILE1# = samples  
  
!LET $XMORIG# = 5610  
  
!LET $YMORIG# = 4580  
  
!LET $ZMORIG# = 275  
  
!LET $XINC# = 40  
  
!LET $YINC# = 40  
  
!LET $ZINC# = 10  
  
!LET $NX# = 30  
  
!LET $NY# = 26  
  
!LET $NZ# = 1
  4. Check that your new variables definition section contains the lines (including blank lines) as highlighted below:  
  
![](../Images/mac_WorkingWithVariables%204_450x487.gif)

**Modifying the existing commands to include the defined variables**

  1. In the Macro6a.mac - Notepad dialog, line 45, select samples and type in '$INFILE1#'.
  2. On line 50, select 5610 and type in '$XMORIG#'.
  3. On line 51, select 4580 and type in '$YMORIG#'.
  4. On line 52, select 275 and type in '$ZMORIG#'.
  5. On line 53, select 40 and type in '$XINC#'.
  6. On line 54, select 40 and type in '$YINC#'.
  7. On line 55, select 10 and type in '$ZINC#'.
  8. On line 56, select 30 and type in '$NX#'.
  9. On line 57, select 26 and type in '$NY#'.
  10. On line 58, select 1 and type in '$NZ#'.
  11. In the Macro6a.mac - Notepad dialog, line 68, select samples and type in '$INFILE1#'.
  12. Check that the two modified subroutines contains the changes highlighted below:  
  
![](../Images/mac_WorkingWithVariables%205.gif)

**Saving the modified macro file**

  1. In the Macro6a.mac - Notepad dialog, select File | Save.

  2. In the Macro6a.mac - Notepad dialog, select File | Exit.  

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro6a.mac can be checked against the example _Macro6a.mac.  
---|---  
  
**![](../Images/UpArrow.gif)**Top of page

## Exercise: Saving and Retrieving Variables

In this exercise, you are going to create a working copy of the existing macro file _Macro6a.mac, include variable file loading and saving commands and then save it to a new file Macro6b.mac.

This will include the following tasks:

  * Including the variable file loading command VARLOAD

  * Including the variable file saving command VARSAVE

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro6a and selectEdit.  
  
![](../Images/mac_WorkingWithVariables%206.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Database\DMTutorials\Projects\S3MacrosTut\ProjFiles\MyProj1.
  5. Define a new File name: 'Macro6b.mac' and click Save.  
  
![](../Images/mac_WorkingWithVariables%207.gif)
  6. Check that this new file Macro6b.mac is open in the Notepad dialog and contains the general listing show below:  
  
![](../Images/mac_WorkingWithVariables%208.gif)

**Includ ing the variable file loading and saving sections**

  1. In the Macro6b.mac - Notepad dialog, line 25, click in the listed macro text immediately to the right of !LET $NZ# = 1.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# ====================================================================  
# Load Substitution Variables File  
# ====================================================================  
  
!VARLOAD MacTut.var, @MERGE=1
  4. Check that your new variable file loading section contains the lines (including blank lines) highlighted below:  
  
![](../Images/mac_WorkingWithVariables%209.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * Please note the following MERGE parameter setting options:
     *        * MERGE=1 - will update any variable that already exists in memory with the file value, and new variables are added to those in memory.
       * MERGE=0 - will erase all current variables.  
---|---  
  5. In the Macro6b.mac - Notepad dialog, line 105, click in the listed macro text immediately to the right of !RETURN.
  6. Press <Enter> twice.
  7. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# ====================================================================  
# Save Substitution Variables File  
# ====================================================================
  8. In the Macro6b.mac - Notepad dialog, line 111, click in the listed macro text immediately to the right of !THE_END:REM.
  9. Press <Enter> twice.
  10. Type in the macro line shown below:  
  
!VARSAVE MacTut.var, @DESC="Studio_3_Macros_Tutorial_Variables", @MERGE=0
  11. Check that your new variables definition section contains the lines (including blank lines) as highlighted below:  
  
![](../Images/mac_WorkingWithVariables%2010.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| Individual variables can also be saved using the syntax e.g. !VARSAVE MacTut.var, @MERGE=0, $INFILE1#, $XMORIG#  
---|---  

****S** avingthe modified macro file**

  1. In the Macro6b.mac - Notepad dialog, select File | Save.

  2. In the Macro6b.mac - Notepad dialog, select File | Exit.  

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro6b.mac can be checked against the example _Macro6b.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro6b.mac and then click Open.  
  
![](../Images/mac_WorkingWithVariables%2011.gif)  

  5. In the Command control bar, note that your application finds and runs the single macro i.e. macro name '1', in the modified macro file.
  6. Check the output in the Command control bar (scroll up to the first few lines) and note that the macro has run to completion with a warning i.e. it could not load the variable file because it did not yet exist. The file was however created when the VARSAVE command ran. The warning is highlighted below:  
  
![](../Images/mac_WorkingWithVariables%2012.gif)
  7. Repeat steps 1. to 6. and check that the macro has run without this previous warning.

**Viewing the contents of the variable file 'MacTut.var'**

  1. Select the Project Files control and click Refresh.
  2. Select the All Files folder, right-click the fileMacTut and selectEdit. 
  3. In the Notepad dialog, check that your variable file contains the 10 variables and their values listed below:  
  
![](../Images/mac_WorkingWithVariables%2013.gif)
  4. In the Notepad dialog, select File | Exit.

**![](../Images/UpArrow.gif)**Top of page

![openbook.gif \(910 bytes\)](../Images/openbook.gif)|  Related Topics  
---|---  
| [Filename, Path and Variable Length limits](<../Principles/Filename,_Path_and_Variable_Length_Limits.md>)