![](../HeaderCell.jpg) |  Multiple Macros Managing multiple macros in a single macro file.  
---|---  
  
# Overview

In this portion of the tutorial you are going to be introduced to the techniques used to manage and use multiple macros in a single *.mac macro file. Please complete the exercises in the order shown below, as the second exercise on this page uses the results from the first exercise.

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _Macro1a.mac

    * _Macro1b.mac

    * _Macro1c.mac

## Links to exercises

The following exercises are available on this page:

  * Storing Multiple Macros in a Single *.mac Macro File

  * Runniing Multiple Macros Stored in a Single *.mac Macro File

## Exercise: Storing Multiple Macros in a Single *.mac Macro File

In this exercise, you are going to combine three separate macro files, each containing a single macro, into one macro file containing three macros.

![](../Images/Tip.gif) |  Combine separate macro files, related to a specific function, into a single macro file; this helps to better manage your macros.  
---|---  
  
**Creat ing a working copy of the existing macro file**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file _macro1a and select Edit.  
  
![](../Images/mac_MultipleMacros%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros.
  5. Define a new File name: 'macro2.mac' and click Save.  
  
![](../Images/mac_MultipleMacros%202.gif)
  6. Check that this new file macro2.mac is open in the Notepad dialog and contains the listing shown below:  
  
![](../Images/mac_MultipleMacros%203.gif)

**Openin g the other two macro files**

  1. Select the Project Files control bar and then the Macros folder.
  2. Right-click the file _macro1b and select Edit.
  3. Check that this new file _macro1b.mac is open in the Notepad dialog and contains the listing shown below:  
  
![](../Images/mac_MultipleMacros%204.gif)
  4. Right-click the file _macro1c and select Edit.
  5. Check that this new file _macro1c.mac is open in the Notepad dialog and contains the listing shown below:  
  
![](../Images/mac_MultipleMacros%205.gif)

**Combining the three macro files into one**

  1. Select the _Macro1b.mac - Notepad dialog, right-click over the listed macro text and select Select All.

  2. Right-click again and select Copy.
  3. Select the Macro2.mac - Notepad dialog, click in the listed macro text to the right of !END, press <Enter> twice.
  4. Check that there is a full blank line between the line containing !END and the line in which the cursor is positioned.
  5. Right-click over the listed macro text and select Paste.
  6. Check that the Macro2.mac - Notepad dialog contains the two macros shown below:  
  
![](../Images/mac_MultipleMacros%206.gif)
  7. Select the _Macro1c.mac - Notepad dialog, right-click over the listed macro text and select Select All.

  8. Right-click again and select Copy.
  9. Select the Macro2.mac - Notepad dialog, click in the listed macro text to the right of the last !END, press <Enter> twice.
  10. Check that there is a full blank line between the line containing !END and the line in which the cursor is positioned.
  11. Right-click over the listed macro text and select Paste.
  12. Check that the Macro2.mac - Notepad dialog contains the three macros shown below:  
  
![](../Images/mac_MultipleMacros%207_749x1026.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * The modified Macro2.mac macro file now contains three separate macros with macro names 'MOD', 'EST' and 'DEL'.
     * The first macro calculates statistics and creates a block model prototype; the second performs a grade estimate, calculates grade model statistics and lists the results in the Command control bar; the third then deletes the temporary working files.
     * Each macro name in a macro file must be unique. If two macros with the same name are encountered, only the first one is run and the second is ignored.
     * Macro names are case sensitive.  
---|---  

**Saving the new macro file**

  1. In the Macro2.mac - Notepad dialog, select File | Save.

  2. In the Macro2.mac - Notepad dialog, select File | Exit.

  3. In the _Macro1b.mac - Notepad dialog, select File | Exit.

  4. In the _Macro1c.mac - Notepad dialog, select File | Exit.  

![note.gif \(1017 bytes\)](../Images/note.gif) |  Your modified and saved macro file Macro2.mac can be checked against the example macro file _Macro2.mac.  
---|---  
  
**![](../Images/UpArrow.gif)**Top of page

## Exercise: Running Multiple Macros Stored in a Single *.mac Macro File

In this exercise, you are going to run all three macros i.e. with macro names 'MOD', 'EST' and 'DEL', contained in the single macro file Macro2.mac., that was created in the previous exercise. The exercise procedures are as follows:

**Running the individual macros**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Start Recording.
  4. In the Select File dialog, select the file name Macro2.mac and then click Run.  
  
![](../Images/mac_MultipleMacros%208.gif)  

  5. In the Command control bar, note that 3 macros have been detected in this macro file and that you are being prompted to select one of them:  
  
![](../Images/mac_MultipleMacros%209.gif)
  6. In the Command toolbar, Command line, enter the Macro Name 'MOD' and then press <Enter>.  
  
![](../Images/mac_MultipleMacros%2010.gif)
  7. Activate the Home ribbon and select Process | Macro | Run Macro.
  8. In the Select File dialog, select the file name Macro2.mac and then click Open.
  9. In the Command toolbar, Command line, enter the Macro Name 'EST' and then press <Enter>.  
  
![](../Images/mac_MultipleMacros%2011.gif)
  10. Activate the Home ribbon and select Process | Macro | Run Macro.
  11. In the Select File dialog, select the file name Macro2.mac and then click Open.
  12. In the Command toolbar, Command line, enter the Macro Name 'DEL' and then press <Enter>.  
  
![](../Images/mac_MultipleMacros%2012.gif)
  13. In the Command control bar, check that all three macros have run to completion.
  14. In the Project Files control bar click the Refresh button.
  15. Check to make sure that the macro has deleted the files x1, x2, x3 and x4.

**![](../Images/UpArrow.gif)**Top of page