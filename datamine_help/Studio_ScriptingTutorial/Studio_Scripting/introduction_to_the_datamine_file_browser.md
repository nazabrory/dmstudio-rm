![](../HeaderCell.jpg) |  Introduction to the File Browser  
---|---  
  
# Introduction to the File Browser

In the following example we will use the File Browser for selecting file names rather than the window prompt() method. This is the same dialog that you would use if running commands interactively:

[![](../Images/Studio3%20Scripting%20File%20Browser%200001.jpg)](<../Images/Studio3%20Scripting%20File%20Browser%200001.jpg>)  
---  
[Expand this image...](<../Images/Studio3%20Scripting%20File%20Browser%200001.jpg>)  
  
## Prerequisites

  * This exercise will be using the _scr_SortCollarsPrompAlertConfirm.htm file. This file will be modified to incorporate the File Browser Object, and can be found under C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts if a standard installation exists.

## Links to exercises

The following exercises are available on this page:

  * Exercise 1: Adding the Project File Browser

## Exercise: Adding the Project File Browser

The File Browser is accessed using the ActiveProject Browser Object of the Studio Application Object. The specific parts of the object we will be accessing are a TypeFilter and FileName property and the Show method.

There are a number of tasks that have to be added to the starting file, such as:

  * Creation of the new Browser Object.

  * Setting properties and calling methods from within the Browser Object.

  * Using the output of the Browser Object.

To do the above, follow these procedures:

  1. Using Notepad, open the file _scr_SortCollarsPromptAlertConfirm.htm located in the database directory C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts  
  
Click Open.

  3. We now need to remove some code in the btnExecute_onclick() method. The first task is to remove the prompt from the code. To do this just type '//' in front of the prompt command. This will have the effect of commenting out the line completely, as shown below.  
  
// strCFile = prompt ("Enter the name of the collars file", "dhcollar");
  4. Now we must add the code that will define the variable for the Browser Object as shown below. The strCFile variable already exists and the new variable will be placed immediately above it.

var oDmBrowser;

var strCFile;

  5. We must now link that variable to the Object in the Datamine Application Object. This is shown below:

alert("This script Sorts the Collars File.");

// strCFile = prompt ("Enter the name of the collars file", "dhcollar");

oDmBrowser = oDmApp.ActiveProject.Browser;

  6. Finally we need to access the oDmBrowser object and set the TypeFilter property, show the dialog to the user and then retrieve the FileName information. This is shown below, these commands should be placed straight after the creation of the object and before the confirm line:

oDmBrowser.TypeFilter = oScript.DmFileType.dmCollars;

oDmBrowser.Show(false);

strCFile = oDmBrowser.FileName;

  7. The above lines allow the TypeFilter to be defined (in this case to the dmCollars type). This allows the browser to show Datamine files of the correct type when it is shown to the user. The Show method shows the dialog to the user. The assignment of the browser filename to the variable strCFile allows information to be obtained from the browser and into a local variable for use later on.
  8. Search for a '_scr_SortCollars' text, (the way you do this will depend on your particular editor). When the text is found change it to 'Sort Collars Browser'. There should only be two occurrences of this text.
  9. Save the file with the name 'SortCollarsBrowser.htm'. The file should be saved to C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts.  
  
Leave this application open with the loaded file in case any changes need to be made.
  10. In Studio, activate the Home ribbon and select JScipt | Run Script.
  11. In the Browsing for script file... dialog select the SortCollarsBrowser.htm file.
  12. In the Customization window note that the script is loaded and shows the 'Sort Collars Browser' text.
  13. Clear the Command window by right-clicking in the window and selecting Clear from the menu.
  14. Execute the script.
  15. The popup alert message is shown to the user. Click OK.
  16. Select the dhCollar file from the Browser window and click OK.
  17. Click OK to the confirmation message and view the output in the Command window.

**![](../images/UpArrow.gif)**Top of page

![note.gif \(1017 bytes\)](../images/note.gif) |  We have used a TypeFilter of 'dmCollars' in the above example. There are many more filter types that can be used. If the file type is not known then the type dmAny should be used.  
---|---