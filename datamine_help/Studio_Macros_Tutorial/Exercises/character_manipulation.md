![](../HeaderCell.jpg) |  Character Manipulation Manipulating characters in string substitution variables.  
---|---  
  
# Overview

This portion of the tutorial will introduce you to the commands and techniques used to manipulate characters in string substitution variables.

Why Manipulate String Substitution Variables?

Manipulating string substitution variables provides the ability to:

  * format string data stored as a variable

  * extract data about or from within a string

  * concatenate strings.

What String Manipulation Commands Are There?

Strings can be manipulated using the following commands:

  * EVAR to determine if a substitution string is valid

  * INDX to determine the position of one string within another

  * LENG to determine the length of a string

  * LWC to convert a string to lower case

  * SUBS to extract a substring

  * UPC to convert a string to upper case

What Format do the Character Manipulation Commands take?

  * General formats:  
  
!let <var>=EVAR(<str1>)  
  
!let <var>=INDX(<str1>,<str2>)  
  
!let <var>=LENG(<str1>)  
  
!let <var>=LWC(<str1>)  
  
!let <var>=SUBS(<str1>,<var1>,[<var2>])  
  
!let <var>=UPC(<str1>)  

  * Where:  
  
<var> is a substitution variable  
  
<var1> is a numeric substitution variable or constant  
  
<var2> is a numeric substitution variable or constant  
  
<str1> is a string substitution variable  
  
<str2> is a string substitution variable.

  * Notes

  *     * If <str1> or <str2> contain embedded blanks which must be preserved, the variable or constant should be enclosed in (single) quotes.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro13.mac

## Exercise: Manipulating String Substitution Variables

In this exercise, you are going to create a working copy of the existing macro file _Macro13.mac , include commands to format the Yes/No temporary files deletion response to upper case and also format the displayed summary statistics to 2 decimal places. The modified macro will be save to a new file Macro14.mac.

This will include the following tasks:

  * Using the UPC character manipulation command to convert the Yes/No reply to Upper Case

  * Using the INDX character manipulation command to determine the position of the '.' in the summary statistics display variables

  * Using the SUBS character manipulation command to extract the required number of string characters

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro13 and selectEdit.  
  
![](../Images/mac_CharacterManipulation%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro14.mac' and click Save.  
  
![](../Images/mac_CharacterManipulation%202.gif)
  6. Check that this new file Macro14.mac is open in the Notepad dialog and contains the general listing show below:  
  
![](../Images/mac_CharacterManipulation%203.gif)

Insert**ing the command for formatting the Y/N reply**

  1. In the Macro14.mac - Notepad dialog, line 102, click in the listed macro text immediately to the right of:  
  
1 Delete temporary files? N/[Y] >'$YN1#',a,1,N,Y
  2. Type in the additional code:  
  
,n,y
  3. In the Macro14.mac - Notepad dialog, line 103, click in the listed macro text immediately to the right of:  
0.
  4. Press <Enter> twice.
  5. Type in the macro line shown below:  
  
!LET $YN1# = UPC($YN1#)
  6. Check that your modified macro contains the modified and additional lines highlighted below:  
  
![](../Images/mac_CharacterManipulation%204.gif)

Insert**ing the commands for formatting the summary statistics**

  1. In the Macro14.mac - Notepad dialog, line 196, click in the listed macro text immediately to the right of   
  
!LET $range2# = $max2# - $min2#
  2. Press <Enter> twice.
  3. Type in the macro lines (including <Spacebar> spaces and blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!LET $8spaces# = '........'  
  
!LET $fldname2# = SUBS($fldname2#$8spaces#,1,8)  
  
!LET $indmin2# = INDX($min2#,'.')  
  
!IF $indmin2#>0, LET $min2# = SUBS($min2#,1,{$indmin2#+2})  
  
!LET $indmax2# = INDX($max2#,'.')  
  
!IF $indmax2#>0, LET $max2# = SUBS($max2#,1,{$indmax2#+2})  
  
!LET $indrange2# = INDX($range2#,'.')  
  
!IF $indrange2#>0, LET $range2# = SUBS($range2#,1,{$indrange2#+2})
  4. In line 215, reduce the number of spaces from four to two, between the variables $fldname2# and $min2# in the line:  
  
0 $fldname2# $min2# $max2# $range2#
  5. Check that your modified macro contains the lines (including blank lines) highlighted below:  
  
![](../Images/mac_CharacterManipulation%205.gif)

**Saving the modified macro file**

  1. In the Macro14.mac - Notepad dialog, select File | Save.

  2. In the Macro14.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro14.mac can be checked against the example _Macro14.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro14.mac and then click Open.  
  
![](../Images/mac_CharacterManipulation%206.gif)  

  5. In the Command control bar, press <Enter> to accept the default values for the sample file name and block model parameters prompts.
  6. Type in 'n' or 'y' at the temporary file deletion prompt.  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * In previous exercises only 'Y' or 'N' i.e. upper case letters, were used in the response, as:
     *        * this prompt only accepted 'Y' or 'N'
       * the IF statement in SUB3 only tested for upper case 'Y' or 'N' responses
     * As a result of the above code modifications:
     *        * this prompt now accepts 'Y', 'N', 'y' or 'n'
       * the reply is formatted to upper case
       * the IF statement in SUB3 still only tests for upper case 'Y' or 'N' responses
     * What this now allows you to do is reply without having to worry about whether the Caps Lock is on or off.  
---|---  
  7. In the Command control bar, note the new format for the summary sample statistics i.e. the Field name column is fixed at 8 characters width and the displayed statistics have been rounded down to 2 decimal places:  
  
![](../Images/mac_CharacterManipulation%207.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The displayed summary statistics fields Min, Max and Range could also be formatted to a fixed width using a similar technique as that used for the Field column.  
---|---  

**![](../Images/UpArrow.gif)**Top of page