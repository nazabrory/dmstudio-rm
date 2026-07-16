![](../HeaderCell.jpg) |  Creating a new Macros Project Creating a new project file for the macros tutorial.  
---|---  
  
# Overview

The sections below introduce you to the creation and saving of a new project.

## Prerequisites

  * Check that you have the tutorial data folders installed. These are located (with a standard installation) under C:\Database\DMTutorials. This path should exist and contain two sub-folders; Data and Projects. The contents of the Data folder will be accessed throughout the tutorial, and any files you create will be stored in the Projects area.

  * All demo macro files must be copied to the C:\Macros top-level folder, as described [here](<../General/the_macros_data_set.md#SettingUpData>).  
  
If you cannot locate these folders, please contact your Datamine Support Consultant.

  * Read through the pages under the tutorial heading "Principles"

## Exercise: Creating and Saving a New Project

In this lesson, you are going to create a new project file "Macros Tut 1", add the relevant data files and then save the project.

## Creating a new Project and adding Files

  1. Launch your application.

  2. If prompted, select a valid license for your application and, when the Start page is displayed, click the New Project... link

  3. If the Studio Project Wizard (1. Welcome ...) dialog is displayed, click the Next button (the welcome screen isn't shown if the Skip this page in future option was selected the last time a new project was created).

  4. In the Studio Project Wizard (2. Project Properties) dialog, define the settings as shown below:

     * Name: MacrosTut1

     * Location: C:\Macros

     * Create Extended precision project: disabled

     * Automatically add files...: enabled  

  5. In the Studio Project Wizard (2. Project Properties) dialog, click Project Settings....

  6. In the Project Settings dialog, Automatic Project Updates group, set the options as shown below and then click OK:  
  
\- Detect new files in the project folder when the project is opened: enabled  
\- Detect files added to or removed from the project folder while the project is open: enabled  
Automatically update project (no prompts): enabled  

  7. Back in the Studio Project Wizard (2. Project Properties) dialog, click Next.

  8. In the Studio Project Wizard (3. Project Files) dialog, click Add File(s)....

  9. In the Select files to add to new project dialog, browse to the folder C:\Database\DMTutorials\Data\VBOP\Datamine,

  10. Select the following Datamine files:

     * _include.dm

     * _srfsamp.dm

  11. Click Open.

  12. In the Studio Project Wizard (3. Project Files) dialog, click Add File(s)....

  13. In the Select files to add to new project dialog, define Files of type: as [All Files (*.*)]

  14. Define Look in: by browsing and selecting the folder C:\Database\DMTutorials\Projects\S3MacrosTut\ProjFiles\Standard.

  15. Select the following macros and script files:

     * _Macro1a.mac

     * _Macro1b.mac

     * _Macro1c.mac

     * _Macro2.mac

     * _Macro3.mac

     * _Macro4.mac

     * _Macro5.mac

     * _Macro6a.mac

     * _Macro6b.mac

     * _Macro7.mac

     * _Macro8a.mac

     * _Macro8b.mac

     * _Macro9.mac

     * _Macro10.mac

     * _Macro11.mac

     * _Macro12.mac

     * _Macro13.mac

     * _Macro14.mac

     * _Macro15.mac

     * _Macro16.mac

     * _Macro17.mac

     * _Macro19.mac

     * _Run_Macro18.htm

  16. Click Open.

  17. In the Studio Project Wizard (3. Project Files) dialog, review the list of added files and then click Next.

  18. In the Studio Project Wizard (4.Your project is ready to create) dialog, click Finish.

## Creating a working copy of the Sample File '_srfsamp'

  1. Activate the Data ribbon and select Data Tools | Tables | Copy File

  2. In the COPY dialog, define the settings in the Files , Fields and Parameter tabs, as shown in the table below, and then click OK:  

**COPY dialog Settings**  
---  
**Files tab** |   
_**Input Files**_ |   
IN |  _srfsamp  
_**Output Files**_ |   
**OUT** |  samples  
**Retrieval tab** |   
Retrieval Criteria |  none  
  3. In the Project Files control bar, check that the new file "Samples" is listed under the All Files folder.  

![note.gif \(1017 bytes\)](../Images/note.gif) | 
     * The file _srfsamp is located in the folder C:\Database\DMTutorials\Data\VBOP\Datamine and is linked to the macro tutorial's project folder.
     * The new file Samples , which is a copy of this linked file, is located in the project folder
     * An important requirement of macros is that the input files which are used by processes in the macro, are located in the project folder.  
---|---  
![note.gif \(1017 bytes\)](../Images/note.gif)| LINKandUNLINKAn alternative to creating a local copy of the external file for use by the macros, is to use the processes LINK and UNLINK . This creates a link file in the project folder which is a direct link to the file in the external folder. These processes can only be run from within a macro and not the Command toolbar. The general procedure for using these processes in this tutorial would be as follows:
     * Use LINK to link the external file _srfsamp (located in the folder C:\Database\DMTutorials\Data\VBOP\Datamine) into the tutorial's project folder (C:\Database\DMTutorials\Projects\S3MacrosTut\ProjFiles\MyProj1) via a local temporary link file e.g. filename samples . The example macro code for this would be:  
  
!LINK &OUT(samples)  
C:\Database\DMTutorials\Data\VBOP\Datamine\\_srfsamp.dm
     * Run all the required processes as normal.
     * Use UNLINK to remove the linked temporary file . The example macro code for this would be:  
  
!UNLINK &IN(samples)  
  
---|---  

## Saving the Project

  * Use the Project button (top left corner of the screen to select the Save command.

![note.gif \(1017 bytes\)](../Images/note.gif) | 

  * This project file will be used for the remaining exercises in this tutorial
  * The project file can be set to be automatically updated after project changes have been made e.g. importing data, generating legends. This is set in the Project Settings dialog found on the Home ribbon under Project | Settings, and then selecting the Project tab. Then, selecting both the Detect New Files... and Detect Files Added... check boxes ensure automatic updating is performed

  
---|---  
  
![](../Images/UpArrow_7x9.gif) Top of page