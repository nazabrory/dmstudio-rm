![](../HeaderCell.jpg) |  Running Macros from Scripts How to run a macro from within a script.  
---|---  
  
# Overview

This portion of the tutorial will introduce you to the commands and techniques used to run a macro from a script.

Why run a macro from a script?

Running macros from scripts provides the ability to:

  * Make use of existing macros from within the scripting environment.

  * Combine both macros and scripts to provide a flexible custom script-macro solution.

  * Information can be passed between macros and scripts using the substitution variable file (*.var)

What Script Command is used to Run a Macro?

The following script command is used:

  * oDmApp.ParseCommand("xrun Macro18.mac 1");

where:

  * xrun is the Studio Process used to run a macro

  * Macro16.mac is the name of the macro file containing the macro

  * 1 is the name of the macro

![note.gif \(1017 bytes\)](../Images/note.gif) |  The XRUN macro command can also be used within a macro to run i.e. call another macro.  
---|---  
  
## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * formulae (this file was generated in the exercise on the [Including Datamine File Records as Lines in a Macro](<including_datamine_file_records_as_lines_in_a_macro.md>) page)

    * _Macro16.mac

    * _Run_Macro18.htm

## Exercise: Running a Macro from a Script

In this exercise you are going to create a local copy of the macro file _Macro16.mac by saving it to the file Macro18.mac . You will then view the contents of the script file _Run_Macro18.htm and the associated macro file Macro18.mac and then run the macro by running the script. This includes the following steps:

  * creating a local copy of the macro file

  * viewing the script code

  * viewing the macro code

  * running the script 

**Creat ing a local copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro16 and selectEdit.  
  
![](../Images/mac_RunMacroFromScript%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro18.mac' and click Save.  
  
![](../Images/mac_RunMacroFromScript%202.gif)

**View ing the macro code**

  1. In the Macro18.mac - Notepad dialog, check that it contains the listing shown below:  
  
![](../Images/mac_RunMacroFromScript%203.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)|  The above macro uses EXTRA to set an anomaly flag field named ANOM in the input surface soil sampling file 'samples' .  
---|---  
  2. In the Macro18.mac - Notepad dialog, select File | Exit.

**View ing the script code**

  1. Select the Project Files dialog and then the Web Files folder.
  2. Right-click the file_Run_Macro18 and selectEdit.  
  
![](../Images/mac_RunMacroFromScript%204.gif)
  3. In the _Run_Macro18.htm tab, right-click over the white background and select View Source.
  4. In the _Run_Macro18.mac - Notepad dialog, line 42, check that it contains the command show below:  
  
![](../Images/mac_RunMacroFromScript%206.gif)
  5. In the _Run_Macro18.mac - Notepad dialog, select File | Exit.

**R unning the script**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. In the _Run_Macro18.htm tab, click Execute.
  4. In the Command control bar, note that the macro has run and generated the new file xsamples.dm :  
  
![](../Images/mac_RunMacroFromScript%208.gif)

![note.gif \(1017 bytes\)](../Images/note.gif)| Please see the Scripting Tutorial for more details on running macros from scripts.  
---|---  
  
**![](../Images/UpArrow.gif)**Top of page