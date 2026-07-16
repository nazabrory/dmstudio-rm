![](../HeaderCell.jpg) |  Loops Adding loops to macros.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the techniques and commands used to construct loops in a macro.

Why Use Loops?

Loops in macros provide the ability to:

  * repeat a section of macro commands or processes a certain number of times based on a flexible counter

  * provide enhanced program control

  * have flexible functionality by being able to cater for different options or scenarios .

What Format do Loops Have?

Loops typically have the following structure:

  * General format:  
  
!<sublabel>:REM # start of subroutine  
  
!LET <var1>=<startnum> # initialize loop counter  
  
!LET <var2>=<maxnum> # set maximum no of loops  
  
!LOOP1:REM # loop start point  
  
!LET <var1>=<var1>+1 # increment counter  
  
!IF <var1> > <var2>, GOTO LOOPEND # check counter vs max no of loops  
  
<statements> #  
  
!GOTO LOOP1 # end of loop, return to loop start point  
  
!LOOPEND:REM # loop endpoint  
  
!RETURN # end of subroutine  
  
  
Where:

  *     * <sublabel> is a command label used to indicate the start of the subroutine

    * <var1> is the substitution variable whose value defines the loop counter's starting and incremented value

    * <startnum> is the value of the loop counter's starting and incremented value (this is a number or a numeric substitution variable)

    * <var2> is the substitution variable whose value defines the loop counter's maximum value

    * <maxnum> is the loop counter's maximum value (this is a number or a numeric substitution variable)

    * <statements> are processes or macro commands  

  * Notes

  *     * Loops may be embedded within loops  

  * Example  
  
!SUB1:REM # start of subroutine  
  
!LET $LNum#=0 # initialize loop counter to 0  
  
!LET $LMax#=10 # set maximum no of loops to 10  
  
!LOOP1:REM # loop start point  
  
!LET $LNum# = $LNum# + 1 # increment counter  
  
!IF $LNum# > $LMax#, GOTO LOOPEND # check counter vs max no of loops  
  
<statements> #  
  
!GOTO LOOP1 # end of loop, return to loop start point  
  
!LOOPEND:REM # loop endpoint  
  
!RETURN # end of subroutine  

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro10.mac

## Exercise: Adding a Loop to a Macro

In this exercise, you are going to create a working copy of the existing macro file _Macro10.mac, include a loop to retrieve the sample file summary statistics and display the values in a message. The modified macro will be save to a new file Macro11.mac.

This will include the following tasks:

  * Inserting the loop structure using the command label, LET, FILE, IF and GOTO macro commands

  * Inserting a set of commands to retrieve and display values using the FIELD and PROMPT macro commands

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro10 and selectEdit.  
  
![](../Images/mac_Loops%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro11.mac' and click Save.  
  
![](../Images/mac_Loops%202.gif)
  6. Check that this new file Macro11.mac is open in the Notepad dialog and contains the general listing shown below:  
  
![](../Images/mac_Loops%203.gif)

Includ**ing the loop structure**

  1. In the Macro11.mac - Notepad dialog, line 157, click in the listed macro text immediately to the right of !STATS &IN(x3),&OUT(x4),*F1(AU).
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# Loop to display summary sample statistics  
  
!FILE $file2#=x1,$numrecs2#=recs # determine number of records in file  
  
!LET $LNum#=0 # initialize loop counter to 0  
  
!LET $LMax#=$numrecs2# # set maximum no of loops to no file records  
  
!LOOP1:REM # loop start point  
  
!LET $LNum#={$LNum#+1} # increment counter  
  
!IF $LNum#>$LMax#, GOTO LOOPEND # check counter vs max no of loops  
  
<statements>  
  
!GOTO LOOP1 # end of loop, return to loop start point  
  
!LOOPEND:REM # exit from loop  
  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The '{ }'s in !LET $LNum#={$LNum#+1} ensure that the statement is treated as a calculation and not a concatenation of two sets of characters.  
---|---  
  4. Check that the loop structure's commands have been inserted as highlighted below:  
  
![](../Images/mac_Loops%204.gif)

**I** nclud**ing the data retrieval and message commands**

  1. In the Macro11.mac - Notepad dialog, line 159, click in the listed macro text immediately to the right of # Loop to display summary sample statistics.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!PROMPT  
0  
0 Summary Sample Statistics  
0 ++++++++++++++++++++++++++++++  
0  
0 Field Min Max Range  
0 -----------------------------
  4. In line 181, select <statements>.
  5. Type in the macro lines (including spaces and blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!IF $file2#=1, THEN  
  
!FIELD $file3#=x1,$recnum2#=$LNum#,$fldname2#=FIELD,  
$min2#=MINIMUM,$max2#=MAXIMUM  
  
!LET $range2# = $max2# - $min2#  
  
!PROMPT  
0 $fldname2# $min2# $max2# $range2#  
0  
  
!ELSE  
  
!PROMPT  
0 No statistics available...  
0  
  
!ENDIF  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The field statement is placed on two lines as it is to long for one line (max 80 characters). The first line ends with a ',' which indicates to your application that the command carries in the next line in the macro code:  
  
!FIELD $file3#=x1,$recnum2#=$LNum#,$fldname2#=FIELD,$min2#=MINIMUM,  
$min2#=MINIMUM,$max2#=MAXIMUM  
---|---  
  6. In line 204, click immediately to the left of !LIST &IN(x1),*F1(FIELD),*F2(MINIMUM),*F3(MAXIMUM),*F4(RANGE),.
  7. Type in '# '.
  8. In line 205, click immediately to the left of  *F5(MEAN),@PROMPT=20.0.
  9. Type in '# '.
  10. Check that your modified macro contains the additional commands and '#'s as highlighted below:  
  
![](../Images/mac_Loops%205.gif)

![note.gif \(1017 bytes\)](../Images/note.gif)| 

  * Inserting '# ' before a command will convert the line into a comment and prevent this command from running.
  * Make sure that a line of macro code ends in a ',' if the process or macro command runs over to the next line

  
---|---  
  
**Saving the modified macro file**

  1. In the Macro11.mac - Notepad dialog, select File | Save.

  2. In the Macro11.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro11.mac can be checked against the example _Macro11.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro11.mac and then click Open.  
  
![](../Images/mac_Loops%206.gif)  

  5. Press <Enter> to accept the default values for the sample file name and block model parameters' prompts.
  6. In the Command toolbar type in 'N' when prompted to delete the temporary files:  
  
![](../Images/mac_Loops%207.gif)
  7. In the Command control bar, note the additional message displaying the summary sample statistics and that the temporary files have not been deleted:  
  
![](../Images/mac_Loops%208.gif)

**Checking the summary sample statistics against the original data**

  1. Select the Project Files control bar and then the All Tables folder.
  2. Double-click the filex1 .
  3. In the x1.dm - Table Editor dialog, match the values below, to those listed in the summary statistics in the Command control bar:  
  
![](../Images/mac_Loops%209a.gif)  

  4. In the x1.dm - Table Editor dialog, select File | Exit.

**![](../Images/UpArrow.gif)**Top of page