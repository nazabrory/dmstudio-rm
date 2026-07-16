![](../HeaderCell.jpg) |  Basic Macro Layout The anatomy of a macro  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the basic layout and components of a simple recorded macro.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * _Macro1a.mac

## Exercise: Identifying the basic macro layout

In this exercise, you are going to open an existing macro file and identify the typical layout of a basic macro, the various Processes and Macro Commands.

**Opening the Macro listing in Notepad**

  1. With your application running, access the Project Files control bar.
  2. Expand the Macros folder.
  3. Right-click the file _macro1a and select Edit.  
  
![](../Images/mac_BasicMacroLayout%201.gif)  

**Identifying the basic macro layout and components**

  1. In the Notepad dialog, view the macro listing, compare it to that shown in the image below.  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * The initial recorded lines have been edited and separated using the <Enter> key
     * Spacing the macro lines can make the recorded lines easier to read
     * Blank lines should not be inserted within the listed files, fields and parameters of a process or command
     * Filenames are not case sensitive when used in a macro.  
---|---  
  
![note.gif \(1017 bytes\)](../Images/warning.gif)| 
     * Do not use the <Tab> key to space out the text or lines in a macro as this will result in the macro running with errors.  
---|---  
![](../Images/mac_BasicMacroLayout%202_401x439.gif)
  2. In the macro listing, identify the items shown in the notes below:  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| The listed macro has the following components:
     * A start, indicated by the Process START, a space and the macro name, here 'MOD'
     * Numeric or single word alphanumeric names can also be used as macro names e.g. 'MOD', 'MOD1', '1'
     * An end, indicated by the Process END
     * START and END are Macro Commands
     * STATS and PROTOM are processes.
     * The following syntax is used for Processes, their file names, field names and parameters:
     * '!' indicates a Process name e.g. !PROTOM
     * '&' indicates a file name e.g. &OUT(x2)
     * '*' indicates a field name
     * '@' indicates a parameter e.g. @ROTMOD=0.0
     * files and fields are enclosed in brackets ()
     * parameter values appear after the equals sign =
     * the column of letters and numbers listed below !PROTOM are responses to prompts issued by the !PROTOM process.  
---|---  
  3. Select File | Exit to close the Notepad dialog.

**![](../Images/UpArrow.gif)**Top of page