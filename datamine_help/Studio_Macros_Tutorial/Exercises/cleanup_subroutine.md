# Cleanup Subroutine

![](../HeaderCell.jpg) |  Using a Catalogue File in a Cleanup Subroutine How to use a catalogue file in a cleanup subroutine in a macro.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the techniques used to set up a cleanup subroutine in a macro.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro4.mac

## Exercise: Using a Catalogue File in a Cleanup Subroutine

In this exercise, you are going to create a working copy of the existing macro file _Macro4.mac, modify the existing cleanup routine and then save it to a new file Macro5.mac.

This will include the following tasks:

  * Inserting a catalogue file generation step using the process PICDIR

  * Replacing the multiple file deletion processes with a single deletion process.

![note.gif \(1017 bytes\)](../Images/note.gif) |  Why a Cleanup Subroutine? A Cleanup Subroutine within a macro allows:

  * deletion of temporary working files
  * the ability to disable the cleanup subroutine for testing and error solving.

What Format does a Cleanup Subroutine Have? Simple format:

  * is called by the macro command:  
  
!GOSUB <subroutinename>
  * contains a series of file deletion processes:  
  
!DELETE &IN(filename)

Standard format:

  * is called by the macro command:  
  
!GOSUB <subroutinename>
  * contains a catalogue file generation command:  
  
!DIR &OUT(cataloguefilename) <file selection template>  

  * contains a single catalogue file deletion command:  
  
!DELETE &IN(cataloguefilename) process.

Advanced format:

  * is called by the macro command:  
  
!GOSUB <subroutinename>
  * contains a catalogue file generation command:  
  
!PICDIR &OUT(cataloguefilename) <parameters>  
<pattern matching expression(s)>
  * contains a single catalogue file deletion command:  
  
!DELETE &IN(cataloguefilename) process.

  * Please see the process description of PICDIR, in your application's online help system for further details.

  
---|---  
  
![](../Images/Tip.gif) | 

  * use a simple naming convention for temporary filenames e.g. X*.dm, as this makes the creation of a catalogue file, using retrieval criteria, a lot easier.
  * use the same naming convention for the catalogue file as that used for the temporary working files - this ensures that the catalogue file is also deleted after the working files have been deleted.

  
---|---  
  
![note.gif \(1017 bytes\)](../Images/warning.gif) |  The use of a catalogue file for file deletion purposes is a powerful tool and has the ability to delete many files in one operation.To prevent the unwanted deletion of files, follow the recommendations below:

  1. Thoroughly check the catalogue file generation step i.e. specifically the retrieval criteria used to populate the catalogue file
  2. Run this part of the subroutine and generate the catalogue file
  3. View the catalogue file in the Table Editor and check that the correct files are listed in the field 'FILENAM
  4. If the catalogue file contains the incorrect file list, DO NOT delete this file using theDELETEprocess, as this will result in the files listed in the catalogue file being deleted. Rather delete all the records in the catalogue file and then save it - this will render the catalogue file harmless
  5. Rerun steps 1. to 4. if required
  6. Include the deletion of the catalogue file step in the subroutine
  7. Rerun the subroutine and check the results.

  
---|---  
  
**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file_Macro4 and selectEdit.  
  
![](../Images/mac_CleanupSubroutine%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'Macro5.mac' and click Save.  
  
![](../Images/mac_CleanupSubroutine%202.gif)
  6. Check that this new file Macro5.mac is open in the Notepad dialog and contains the cleanup subroutine listing highlighted below:  
  
![](../Images/mac_CleanupSubroutine%203.gif)

**Modify ing the cleanup subroutine**

  1. In the Macro5.mac - Notepad dialog, line 71, select !DELETE &IN(x1),@CONFIRM=0.0 and type in '!DIR &OUT(xcat),x?'.
  2. On line 73, select x2 and type in 'xcat'.
  3. On line 75-77, select:   
  
!DELETE &IN(x3),@CONFIRM=0.0  
  
!DELETE &IN(x4),@CONFIRM=0.0
  4. Press <Backspace> three times.
  5. Check that your modified cleanup subroutine listing only contains the lines highlighted below:  
  
![](../Images/mac_CleanupSubroutine%204.gif)  
  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * The syntax for the file selection template used in the above DIR (LISTDR) process is 'x?'.
     * This syntax makes use of the wildcard character '?' and will result in the selection of all files, irrespective of length, starting with 'x'.
     * This syntax is not case sensitive.
     * The catalogue file xcat uses the same file naming convention as the temporary working files i.e. 'x*'; this ensures that the catalogue file is also deleted after the temporary files have been deleted.  
---|---  

![note.gif \(1017 bytes\)](../Images/warning.gif) | 

  * Datamine files (*.dm) that are deleted using either the Project Files control bar or the process DELETE are permanently deleted.
  * These files cannot be retrieved i.e. they do not end up in a 'Recycle Bin' as is the case when files are deleted using the Windows Explorer dialog.

  
---|---  
  
**Saving the modified macro file**

  1. In the Macro5.mac - Notepad dialog, select File | Save.

  2. In the Macro5.mac - Notepad dialog, select File | Exit.  

![note.gif \(1017 bytes\)](../Images/note.gif) |  Your modified and saved macro file Macro5.mac can be checked against the example _Macro5.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run Macro.
  4. In the Select File dialog, select the file name Macro5.mac and then click Open.  
  
![](../Images/mac_CleanupSubroutine%205.gif)  

  5. In the Command control bar, note that you application finds and runs the single macro i.e. macro name '1', in the modified macro file.
  6. Check the output in the Command control bar and make sure that all processes listed in the macro file have been run successfully and that the temporary files have been deleted using a catalogue file as highlighted below:  
  
![](../Images/mac_CleanupSubroutine%206.gif)

**![](../Images/UpArrow.gif)**Top of page