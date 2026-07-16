# Accessing a Datamine File's Data

![](../HeaderCell.jpg) |  Accessing a Datamine File's Data How to access the records in a Datamine file using the FILE and FIELD macro commands.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the commands used to check for the existence of a Datamine file and to access its data.

How can Macro Accessed Data be Used?

Macro accessed data provides the ability to:

  * assign a substitution variable a value from a specific field and record in Datamine file

  * use this substitution variable in macro commands or processes

  * use this substitution variable for calculation purposes

  * use this substitution variable in macro messages.

What Format do these file checking and data accessing commands have?

The following commands are used:

  * Check for the existence of a Datamine file using the FILE command:  
  
!FILE <var1>=<filename>,<var2>=recs  
  
Where:

  *     * <var1> is the substitution variable whose value is set to '1' if the file exists, '0' if it does not

    * <filename> is the name of the Datamine file

    * <var2> is the substitution variable whose value is set to the number of records in the file

    * recs is a placeholder name.  

  * Extract the data from the Datamine file using the FIELD command::  
  
!FIELD <var1>=<filename>,<var2>=<N>,<var3>=<field1>  
  
Where:

  *     * <var1>, <var2>, <var3> are substitution variables

    * <filename> is the name of the Datamine file to be read

    * <N> is the number of the record in the Datamine file that is to be read

    * <field1> is the name of the field to be read in the Datamine file.

  * Examples  
  
Checking for the existence of the file and determining it's number of records:  
  
!FILE $file1#=samples,$numrecs1#=recs  
  
Extracting the values for the fields AU and CU in the 5th record:  
  
!FIELD $file2#=samples,$recnum1#=5,$fldval1#=AU,$fldval2#=AG

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro9.mac

## Exercise: Accessing a Datamine File's Data

In this exercise, you are going to create a working copy of the existing macro file _Macro9.mac, include commands to check for the existence of a file, retrieve a record's field values and then display the values in a message and then save it to a new file Macro10.mac.

This will include the following tasks:

  * Inserting a check for the existence of a file using the FILE macro command

  * Inserting a data record reading step using the FIELD macro command

  * Inserting a set of messages displaying the variables' values using the PROMPT macro command

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro9 and selectEdit.  
  
![](../Images/mac_AccessDatamineFile%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros
  5. Define a new File name: 'Macro10.mac' and click Save.  
  
![](../Images/mac_AccessDatamineFile%202.gif)
  6. Check that this new file Macro10.mac is open in the Notepad dialog and contains the general listing show below:  
  
![](../Images/mac_AccessDatamineFile%203.gif)

Includ**ing the check for the existence of the Datamine file**

  1. In the Macro10.mac - Notepad dialog, line 160, click in the listed macro text immediately after the last character of:  
  
!LIST &IN(x1),*F1(FIELD),*F2(MINIMUM),*F3(MAXIMUM),*F4(RANGE),  
*F5(MEAN),@PROMPT=20.0
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
# Check, extract and calculate  
  
!FILE $file1#=x4,$numrecs1#=recs
  4. Check that the additional message section contains the lines highlighted below:  
  
![](../Images/mac_AccessDatamineFile%204.gif)

Includ**ing the conditional record reading, calculation and message display statements**

  1. In the Macro10.mac - Notepad dialog, line 164, click in the listed macro text immediately to the right of !FILE $file1#=x4,$numrecs1#=recs.
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!PROMPT  
0  
0 Summary Block Model Statistics  
0 ++++++++++++++++++++++++++++++  
0  
0 Field Min Max Range  
0 -----------------------------  
  
!IF $file1#=1, THEN  
  
!FIELD $file2#=x4,$recnum1#=1,$fldname#=FIELD,$min#=MINIMUM,$max#=MAXIMUM  
  
!LET $range# = $max# - $min#  
  
!PROMPT  
0 $fldname# $min# $max# $range#  
0  
  
!ELSE  
  
!PROMPT  
0 No statistics available...  
0  
  
!ENDIF
  4. In line 192, click immediately to the left of !LIST &IN(x4),*F1(FIELD),*F2(MINIMUM),*F3(MAXIMUM),*F4(RANGE),.
  5. Type in '# '.
  6. In line 193, click at the start of the line  *F5(MEAN),@PROMPT=20.0.
  7. Type in '# '.
  8. Check that the macro contains these additional commands and '#'s as highlighted below:  
  
![](../Images/mac_AccessDatamineFile%205.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| Inserting '# ' before a command will convert the line into a comment and prevent this command from running.  
---|---  

**Saving the modified macro file**

  1. In the Macro10.mac - Notepad dialog, select File | Save.

  2. In the Macro10.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro10.mac can be checked against the example _Macro10.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate theHomeribbon and selectProcess | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro10.mac and then click Open.  
  
![](../Images/mac_AccessDatamineFile%206.gif)  

  5. Press <Enter> to accept the default values for the sample file name and block model parameters' prompts.
  6. In the Command toolbar type in 'N' when prompted to delete the temporary files:  
  
![](../Images/mac_AccessDatamineFile%207.gif)
  7. In the Command control bar, note the message displaying the summary block model statistics and that the temporary files have not been deleted:  
  
![](../Images/mac_AccessDatamineFile%208.gif)

**Checking the summary statistics against the original data**

  1. Select the Project Files control bar and then the All Tables folder.
  2. Double-click the filex4 .
  3. In the x4.dm - Table Editor dialog, match the values highlighted in red below, to those listed in your macro listing and the summary statistics in the Command control bar:  
  
![](../Images/mac_AccessDatamineFile%209a.gif)  

  4. In the x4.dm - Table Editor dialog, select File | Exit.

**![](../Images/UpArrow.gif)**Top of page