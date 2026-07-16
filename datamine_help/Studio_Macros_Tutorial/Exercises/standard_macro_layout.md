![](../HeaderCell.jpg) |  Standard Macro Layout The standard components of a macro.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the location and layout of the typical sections found within a custom written macro.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * _Macro12.mac

## Links to exercises

The following exercises are available on this page:

  * Identifying the Different Sections of a Macro

## Exercise: Identifying the Different Sections of a Macro

In this exercise, you are going to open an existing macro file and identify the location of the typical sections found within a custom macro. This will include locating and familiarizing yourself with the general layout of the following features or sections:

  * comments

  * error trap sections

  * variable definition, loading and saving sections

  * messages

  * prompts

  * subroutines

  * conditional statements

  * loops

**Opening the Macro listing in Notepad**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file _macro12 and select Edit. 

**Identifying Comments**

  1. In the Notepad dialog, find and familiarize yourself with the general layout of a macro comment as shown in the image below. ![](../Images/mac_StandardMacroLayout%202.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * Comments are used for different purposes and are located at various positions within a macro, typically:
     *        * an introductory heading section at the start of a macro
       * short headings at the start of subroutines or sections (as in the above example)
       * short explanatory comments within the body of a section
     * See [Comments](<comments.md>) for more details.  
---|---  

**Identifying Error Traps**

  1. In the Notepad dialog, find and familiarize yourself with the general layout of an error trap and it's error handling routine as shown in the images below. ![](../Images/mac_StandardMacroLayout%203.gif)  
  
![](../Images/mac_StandardMacroLayout%204.gif)  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * The error trapping construction consist of two parts:
     *        * the first error trap portion is typically located just after the start of the macro
       * the second error handling routine is typically located towards the end of the macro
     * See [Error Trapping](<error_trapping.md>) for more details.  
---|---  

**Identifying Substitution Variable Definition, Loading and Saving Sections**

  1. In the Notepad dialog, find and familiarize yourself with the general layout of variable definition, loading and saving sections as shown in the images below. ![](../Images/mac_StandardMacroLayout%205.gif)  
  
![](../Images/mac_StandardMacroLayout%206.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * Substitution variables are managed in different sections, typically:
     *        * a variable definition section for defining default values
       * an optional variable loading section for loading variable settings used in the last run
       * an optional variable saving section for saving variable settings used in the current run
     * Defining substitution variables as needed within the body of the macro makes managing variables more difficult and so is not generally recommended.
     * See [Working with Variables](<working_with_variables.md>) for more details.  
---|---  

**Identifying Messages**

  1. In the Notepad dialog, find and familiarize yourself with the general layout of messages as shown in the images below. ![](../Images/mac_StandardMacroLayout%207.gif)  
  
![](../Images/mac_StandardMacroLayout%208.gif)  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * Messages are located where required within the body of the macro to inform the user of:
     *        * macro results or variable values
       * macro progress
       * errors
     * See [Messages](<messages.md>) for more details.  
---|---  

**Identifying Subroutines**

  1. In the Notepad dialog, find and familiarize yourself with the general layout of subroutine calls and subroutines as shown in the image below. ![](../Images/mac_StandardMacroLayout%209.gif)![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * Subroutines are used to organize the main body of the macro into distinct groups or sections of related processes and commands, and typically consists of:
     *        * a section containing the calls to the different subroutines, located towards the top of the macro, after the initial sections but before the subroutines themselves
       * the individual subroutines with their required starting labels and return commands
     * See [Subroutines](<Subroutines.md>) for more details.  
---|---  

**Identifying Conditional Statements**

  1. In the Notepad dialog, find and familiarize yourself with the general layout of a conditional statement construction as shown in the image below. ![](../Images/mac_StandardMacroLayout%2010.gif)![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * Conditional statements are generally used to control the flow of a macro and can be found in two forms:
     *        * a simple conditional statement
       * a blocked conditional statement (as shown in the example in the above image)
     * See [Conditional Statements](<conditional_statements.md>) for more details.  
---|---  

**Identifying Loops**

  1. In the Notepad dialog, find and familiarize yourself with the general layout of a loop construction as shown in the image below. ![](../Images/mac_StandardMacroLayout%2011.gif)  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * Loops are used to control the number of times a group of processes and macro commands are run and as a minimum, consists of the following components (see above example image):
     *        * loop counter initialization
       * loop counter maximum number
       * loop start point
       * loop counter increment
       * maximum number of loops check
       * the group(s) of macro commands and processes
       * return to loop start point step
       * loop exit point
     * See [Loops](<loops.md>) for more details.  
---|---  
  2. Select File | Exit to close the Notepad dialog.

![note.gif \(1017 bytes\)](../Images/note.gif)| The above mentioned macro features and sections are explained in details in the exercises on the remaining pages of this tutorial.  
---|---  
  
**![](../Images/UpArrow.gif)**Top of page