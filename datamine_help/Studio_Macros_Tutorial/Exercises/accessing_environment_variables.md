![](../HeaderCell.jpg) |  Environment Variables Working with environment variables.  
---|---  
  
# Overview

This portion of the tutorial will introduce you to the commands and techniques used to read environment variables' values.

What can I do with environment variables?

Accessing environment variables provides the ability to:

  * read and then use the values of environment variables in macros.

What Environment Variable Commands Are There?

The following command is used:

  * ENV to access environment variables.

What Format does the Environment Variable Command take?

  * General format:  
  
!let <var>=ENV(<str1>[,<var2>])  

  * Where:  
  
<str1> is the name of an environment variable (see below):  
  
  
<var2> is the optional environment variable setting (1, 2, ...).

  * Example  
  
!let $date#=env(date)

  * Notes

  *     * If the <var2> argument is not supplied, the default value of '1' is used.

What Environment Variables can be accessed?

The following environment variables are commonly used in macros :

  * date

  * time

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro14.mac

## Exercise: Reading the Value of an Environment Variable

In this exercise, you are going to create a working copy of the existing macro file _Macro14.mac , include a command to read and then display the values of two environment variables. The modified macro will be saved to a new file Macro15.mac.

This will include the following tasks:

  * Using the ENV macro command to set the values of date and time substitution variables

  * Using the PROMPT macro command to display these values

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro14 and selectEdit.  
  
![](../Images/mac_EnvironmentVariables%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro15.mac' and click Save.  
  
![](../Images/mac_EnvironmentVariables%202.gif)
  6. Check that this new file Macro15.mac is open in the Notepad dialog and contains the general listing shown below:  
  
![](../Images/mac_EnvironmentVariables%203.gif)

Insert**ing the environment variable commands**

  1. In the Macro15.mac - Notepad dialog, line 235, click in the listed macro text immediately to the right of:   
  
!FILE $file1#=x4,$numrecs1#=recs
  2. Press <Enter> twice.
  3. Type in the macro lines (including blank lines) shown below, ending each line, except the last, with <Enter>:  
  
!LET $date# = ENV(date)  
  
!LET $time# = ENV(time)
  4. Check that your modified macro contains the lines (including blank lines) highlighted below:  
  
![](../Images/mac_EnvironmentVariables%204.gif)

Insert**ing the additional message commands**

  1. In the Macro15.mac - Notepad dialog, line 241, click in the listed macro text immediately to the right of:   
  
!PROMPT
  2. Press <Enter> once.
  3. Type in the macro lines shown below, ending each line, except the last, with <Enter>:  
  
0  
0 Date: $date# Time: $time#
  4. Check that your modified macro contains the lines (including blank lines) highlighted below:  
  
![](../Images/mac_EnvironmentVariables%205.gif)

**Saving the modified macro file**

  1. In the Macro15.mac - Notepad dialog, select File | Save.

  2. In the Macro15.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro15.mac can be checked against the example _Macro15.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro15.mac and then click Open.  
  
![](../Images/mac_EnvironmentVariables%206.gif)  

  5. Press <Enter> to accept the default values for the sample file name, block model parameters and file deletion prompts.
  6. In the Command control bar, note the new Date and Time message line, as highlighted below:  
  
![](../Images/mac_EnvironmentVariables%207.gif)  

![note.gif \(1017 bytes\)](../Images/note.gif)| 

  * The date format is dd/mm/yy
  * The date can be reformatted using the character manipulation commands covered in the exercise [Manipulating String Substitution Variables](<character_manipulation.md#Exercise1>).

  
---|---  
![](../Images/Tip.gif)| 

  * Enter or create dates in a macro using the format yyyymmdd e.g. 20071004
  * Store them in a numeric field in your Datamine file
  * This allows data to be easily sorted by date, which is not always possible with other data formats e.g. dd/mm/yy.

  
---|---  
  
**![](../Images/UpArrow.gif)**Top of page