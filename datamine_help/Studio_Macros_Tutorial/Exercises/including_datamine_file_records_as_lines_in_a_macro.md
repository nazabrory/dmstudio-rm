# Including Datamine File Records as Lines in a Macro

![](../HeaderCell.jpg) |  Including Datamine File Records as Lines in a Macro How to include records from a Datamine file as lines in a macro.  
---|---  
  
# Overview

This portion of the tutorial will introduce you to the commands and techniques used to include records from a Datamine file as lines in a macro.

Why include external text as lines in a macro?

Including external text as lines in a macro provides the ability to:

  * use text (data, macro commands, processes) stored in a Datamine file as lines of code in a macro.

  * have flexible program control.

What Text Inclusion Commands Are There?

The following command is used:

  * INCLUDE to include Datamine file records as lines in a macro.

What Format does the INCLUDE Command take?

  * General format:  
  
!INCLUDE &FILE(file), *TEXT(textfld), *KEY(keyfld), @VALUE='keyval'  

  * Where:  
  
file is the name of the Datamine file containing the text  
  
textfld is the name of the field containing the text, default is TEXT; other field names can also be used  
  
keyfield is the optional key field, which permits selection of a subset of records from the file   
  
keyval is the value of the keyfield which is needs to be selected for inclusion; always used in conjunction with keyfield.  

  * Example  
  
!LET $value#='AU10CUT'  
  
!EXTRA &IN(SAMPLES) ,&OUT(CUTASSAY)  
!INCLUDE &FILE(FORMULAE) ,*TEXT(TEXT) ,* KEY(ASSAYCUT) , @VALUE='$value#'  
GO  
  
!LIST &IN(CUTASSAY)

## Prerequisites

  * Created a new project and added all the required tutorial files - exercises on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page

  * Displayed toolbars - exercises on the Displaying Toolbars page.

  * [Files](<../General/Tutorial_Files_List.md>) required for the exercises on this page:

  *     * samples (this file was generated in the exercise on the [Creating a New Macros Project](<Creating_a_New_Project.md>) page)

    * _include

    * _Macro16.mac

## Exercise: Including Datamine File Records as Lines in a Macro

In this exercise you are going to create a working copy of the existing macro file _Macro16.mac and then modify it to allow the calculation of the anomaly flag field based on a selected grade field. This includes the following steps:

  * creating a working copy of the original macro

  * viewing the macro code

  * make a local copy of the file _include.dm

  * viewing the input Datamine file for the INCLUDE command

  * replacing the existing EXTRA process formula lines in the macro with an INCLUDE command

  * inserting a PROMPT command to set the key field value

  * inserting a PROMPT command to allow selection of the required grade field

  * running the modified macro

**Creat ing a working copy of the existing macro file**

  1. Select the Project Files dialog and then the Macros folder.
  2. Right-click the file_Macro16 and selectEdit.  
  
![](../Images/mac_IncludingRecordsInAMacro%201.gif)  

  3. In the Notepad dialog, select File | Save As.
  4. In the Save As dialog, define Save in: by browsing to and selecting C:\Macros
  5. Define a new File name: 'Macro17.mac' and click Save.  
  
![](../Images/mac_IncludingRecordsInAMacro%202.gif)

**View ing the macro code**

  1. In the Notepad dialog, check that this new file is open and contains the listing shown below:  
  
![](../Images/mac_IncludingRecordsInAMacro%203.gif)  

![note.gif \(1017 bytes\)](../Images/note.gif) | 

  * The above macro uses EXTRA to set an anomaly flag field named ANOM in the input surface soil sampling file 'samples' as follows:
  *     * The field ANOM is initialized and set to '0'
    * If the AU field (gold grade in ppb) is greater than or equal to 0 AND less than 600, then ANOM is set to '1'
    * If the AU field is greater than or equal to 600, then ANOM is set to '2'
  * The EXTRA formula's lines of code are recorded as fixed lines of text in the macro file.

  
---|---  
  
Making a Local Copy of the File _include.dm

  1. Select the Project Files control bar and then the All Tables folder.

  2. Right-click the file_include and selectEdit.  
  
![](../Images/mac_IncludingRecordsInAMacro%204.gif)  

  3. In the _include.dm - Table Editor dialog, select File | Save As.

  4. Browse to the local macros tutorial project folder and define a new file name 'formulae.dm'.  
  
![](../Images/mac_IncludingRecordsInAMacro%205.gif)

**Viewing the input Datamine file that will be used with the INCLUDE command**

  1. In the formulae.dm - Table Editor dialog, check that the file contains the following 10 records  
  
![](../Images/mac_IncludingRecordsInAMacro%206a.gif)  
  

     * Field KEY is the key field and contains values 'AU' and 'CU' corresponding to the gold and copper fields

     * Field TEXT contains five records of EXTRA formula lines for each of the two different key fields i.e. AU and CU

The EXTRA formula lines of code are different for each key field

The five EXTRA formula lines of code for key field AU (records 1-5) are the same as those listed in the macro in the file Macro17.mac:  
  
![](../Images/mac_IncludingRecordsInAMacro%207.gif)

![note.gif \(1017 bytes\)](../Images/note.gif)| The file contains two alphanumeric fields:  
---|---  
  2. In the formulae.dm - Table Editor dialog, select File | Exit.

**Replacing the existing EXTRA process formula lines in the macro with an INCLUDE command**

  1. In the Notepad dialog, select the following five lines:  
  
if (AU>=0 AND AU<600)  
ANOM = 1  
elseif (AU>=600)  
ANOM = 2  
end
  2. Type in the following line:  
  
!INCLUDE &FILE(formulae), *TEXT(TEXT), *KEY(KEY), @VALUE='AU'

  3. Check that your modified macro contains the lines highlighted below:  
  
![](../Images/mac_IncludingRecordsInAMacro%208.gif)  
![note.gif \(1017 bytes\)](../Images/note.gif)| The above macro, if run after the above edits have been made, would yield the same results as the initial macro in the file _Macro16.mac:  
---|---  

**Inserting a PROMPT to set the key field value**

  1. In the Macro17.mac - Notepad dialog, line 1, click in the listed macro text immediately to the right of:   
  
!START 1 Flag Sample File with ANOM field
  2. Press <Enter> once.
  3. Type in the macro lines shown below, ending each line, except the last, with <Enter>:  
  
!PROMPT  
0  
1 Select grade field (AU,CU)[AU] > '$GrdFld#',a,2,AU,CU  
0
  4. At the end of line 11, select:  
  
'AU'
  5. Type in:  
  
'$GrdFld#'
  6. Check that your modified macro contains the additional and modified lines highlighted below:  
  
![](../Images/mac_IncludingRecordsInAMacro%209_450x266.gif)  
  
![note.gif \(1017 bytes\)](../Images/note.gif)| There should be no spaces between the '=' and ''$GrdFld#' in the parameter setting '@VALUE=$GrdFld#.  
---|---  

**Saving the modified macro file**

  1. In the Macro17.mac - Notepad dialog, select File | Save.

  2. In the Macro17.mac - Notepad dialog, select File | Exit.

![note.gif \(1017 bytes\)](../Images/note.gif)| Your modified and saved macro file Macro17.mac can be checked against the example _Macro17.mac.  
---|---  
  
**Running the modified macro file**

  1. Select the Command control bar and click inside the Message pane.
  2. In the Message pane, if it contains message text, right-click and select Clea _r_.

  3. Activate the Home ribbon and select Process | Macro | Run MacroSelect _T_ ools | _M_ acro | _R_ un Macro... or click Run Macro.
  4. In the Select File dialog, select the file name Macro17.mac and then click Open.  
  
![](../Images/mac_IncludingRecordsInAMacro%2010.gif)  

  5. In the Command control bar, note that the macro is prompting the user to select either the CU or the AU (default) grade field, as highlighted below:  
  
![](../Images/mac_IncludingRecordsInAMacro%2011.gif)
  6. In the Command toolbar note that the command line is displaying the default value AU as highlighted below:  
  
![](../Images/mac_IncludingRecordsInAMacro%2012.gif)
  7. Select the Command toolbar and then press <Enter> to accept this default value.
  8. In the Command control bar, note that the AU conditional statement has been used to create the field ANOM in the file xsamples , as highlighted below:  
  
![](../Images/mac_IncludingRecordsInAMacro%2013.gif)  
![note.gif \(1017 bytes\)](../Images/note.gif)| 
     * If for some reason you have selected another dialog or window e.g. the Command control bar, while the macro is prompting you for values, re-select the Command toolbar before continuing.
     * The thin blue line around the command line indicates that it has focus and is ready to receive your input.  
---|---  
  9. Repeat steps 3. to 8. while typing in 'CU' at the prompt for a grade field.
  10. In the Command control bar, check that the CU conditional statement has been used to create the field ANOM in the file xsamples , as highlighted below:  
  
![](../Images/mac_IncludingRecordsInAMacro%2014.gif)

**![](../Images/UpArrow.gif)**Top of page