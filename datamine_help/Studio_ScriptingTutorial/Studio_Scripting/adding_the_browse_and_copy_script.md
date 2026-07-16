# Adding the Browse and Copy Script

You now have an HTML user interface, together with all the hooks for the script.

Remember that scripts are usually made up of a number of event handlers. These are small sections of script that are executed by the browser when some relevant event occurs.

This script will respond to the following events:

  * When the window loads (a window onload event occurs). We use this event to make a connection to the Datamine Application Object.

  * When either the **Browse** buttons are pressed (a button onClick event occurs). This will execute a call to the Datamine Application Object that will display the Browser window, waits for a selection to be made and then copied the selection into the corresponding text box.

  * When the OK button is pressed (a button onClick event occurs). We use this event to ensure that both Input and Output files have been specified and that the retrieval criteria that has been specified is added before the command to copy the files is executed.

## Prerequisites

  * Ensure a suitable script editor is installed and running

  * You will continue to use the Browse.htm file created in the previous exercise - [Creating the Browse and Copy Interface](<creating_the_browse_and_copy_interface.md>). This file can be found at `C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts` when the previous exercise has been completed.

## Exercise: Adding the windows onload event

In this exercise you will add an event that will be fired when the window is loaded.

  1. Open the`Browse.htm`file as saved from the [previous exercise](<creating_the_browse_and_copy_interface.md>).
  2. In between the <HEAD> and </HEAD> tags, insert the following
         
         <SCRIPT language = "Javascript">      
  
---  
           
         function window_onload() {}  
           
         </SCRIPT>  
  
  3. You now need to enter the Javascript code to be executed when this event occurs. First, we need to establish a connection between the script and the Datamine Application Object. To accomplish this we must define a Datamine application variable, and refer to a routine to instantiate the Datamine Application Object. 
  4. Before the function window_onload() text (the line above) type the following text (the oDmBrowser variable will be referred to later).
         
         var oDmApp = null;      
  
---  
           
         var oScript = null;      
           
         var oDmBrowser;  
  

  4. Between the opening and closing brackets of the window_onload() function, type the text 'AutoConnect();'. This instructs the onload event to call a function AutoConnect that we will now write. This routine will use the variable oDmApp defined in step 5.
  5. After the window_onload() function and after the '}' symbol copy and paste (as HTML) the following text:
         
         function AutoConnect() {          
  
---  
           
         oScript = window.external.System.CreateObject("DatamineStudio.ScriptHelper");      
           
         oScript.initialize(window);    oDmApp = oScript.getApplication();      
           
         if (oDmApp== null)    {  
           
         return false;}      
           
         else      
           
         {return true;  
           
         }  
           
         }  
  

  8. The final code should look like the following:
         
         var oDmApp= null;      
  
---  
           
         var oScript = null;      
           
         var oDmBrowser;function   
           
         window_onload() {      
           
         AutoConnect();    }  
           
            
           
         function AutoConnect() {          
           
         oScript = window.external.System.CreateObject("DatamineStudio.ScriptHelper");      
           
         oScript.initialize(window);    oDmApp = oScript.getApplication();      
           
         if (oDmApp== null)      
           
         {return false;}      
           
         else      
           
         {return true;}      
           
         }  
  

  9. Next, you need to ensure the window_onload function is called each time the web page is opened. This can be done using the <BODY> tag's onload event.

Change the <BODY> tag to this:  

         
         <BODY onload="AutoConnect();">  
         

  10. Now, each time the page loads, the **AutoConnect**() function will be called, creating a Datamine Application (**oDmApp**) and a scripting helper (**oScript**) object.

Note: The variable oDmApp, oScript and the AutoConnect function are necessary for every scripted solution that connects to the Datamine Application Object. The AutoConnect function initialises the Datamine Application Object and presents the script with access to this object via the oDmApp variable. The oScript variable gives access to the Script Helper object.

## Exercise: Adding the OK button onClick handler

In this exercise you will add an onClick event that will be fired when the OK button is pressed. When the button is pressed, the script checks that the Input and Output files are present and that the existence of any retrieval criteria is added to the copy command. The copy command is then invoked. Only the retrieval criteria is optional with this script. The input and Output files must exist in order for the script to continue:

  1. Following the last data entry, but before the closing </SCRIPT> tag, enter the following:
         
         function btnOK_onclick() {}  
  
---  
  
  2. Within the body of the btnOK_onclick() function (between the '{' and '}' characters), copy and paste the following text:
         
         if (tbInputFile.value != "" && tbOutputFile.value != "")    {  
  
---  
           
         var theCommand = "copy &in="   
           
         + tbInputFile.value   
           
         + " &out=" + tbOutputFile.value;      
           
            
           
         if (tbRetrieval.value != "")       
           
            
           
         {  
           
         theCommand += " {" + tbRetrieval.value + "}";      
           
         oDmApp.ParseCommand(theCommand);      
           
         }  
           
         }  
  
  3. After this code has been added to the HTML document, Save your document.

## Exercise: Adding the Browse button onClick handlers

In this exercise we will add the two Browse functions and provide a function that will show the Browser window to the user.

  1. As before, enter the following text immediately below the last data entered, and before the closing </SCRIPT> tag:
         
         function btnBrowse1_onclick() {    }  
  
---  
  

  3. Within the body of the btnBrowse1_onclick() function (between the '{' and '}' characters), copy and paste (as HTML) the following text:
         
         tbInputFile.value = DisplayBrowser();

The DisplayBrowser() function is one you will creaqte below, its value will be placed into the value field of the text box tbInputValue:

  3. Repeat steps 1 to 3 using 'btnBrowse2' button and using the following text in the btnBrowse2_onclick() function. This time the value field of the text box tbOutputValue will be populated:
         
         tbOutputFile.value = DisplayBrowser();

  3. Notice that the same function is called but different text boxes are used to display the result. We now need to define this function called DisplayBrowser() that will browse for the files.

Copy and Paste (as HTML) the following text before btnBrowse1_onclick() function:
         
         function DisplayBrowser() {      
  
---  
           
         oDmBrowser = oDmApp.ActiveProject.Browser;      
           
         oDmBrowser.TypeFilter = oScript.DmFileType.dmNothing;      
           
         oDmBrowser.Show(false);          
           
         return oDmBrowser.FileName;      
           
         }  
  

  6. Saveyour document. That script section in full, for reference, should be:
         
         <SCRIPT language = "Javascript">      
  
---  
           
         var oDmApp = null;      
           
         var oScript = null;      
           
         var oDmBrowser;function window_onload()   
           
              {      
           
              Autoconnect()      
           
              }  
           
         function AutoConnect()   
           
              {         
           
              oScript = window.external.System.CreateObject("DatamineStudio.ScriptHelper");      
           
              oScript.initialize(window);      
           
              oDmApp = oScript.getApplication();      
           
              if (oDmApp== null)    {return false;}      
           
              else      
           
              {return true;}  
           
             }  
           
         function btnOK_onclick()   
           
              {    if (tbInputFile.value != "" && tbOutputFile.value != "")  {      
           
              var theCommand = "copy &in="   
           
              + tbInputFile.value   
           
              + " &out=" + tbOutputFile.value;      
           
              if (tbRetrieval.value != "")   
           
              {theCommand += " {"   
           
              + tbRetrieval.value + "}";   
           
              oDmApp.ParseCommand(theCommand);    }  
           
              }  
           
         function btnBrowse1_onclick()   
           
              {    tbInputFile.value = DisplayBrowser();    }  
           
         function btnBrowse2_onclick()   
           
              {    tbOutputFile.value = DisplayBrowser();    }  
           
         function DisplayBrowser()   
           
              {      
           
              oDmBrowser = oDmApp.ActiveProject.Browser;      
           
              oDmBrowser.TypeFilter = oScript.DmFileType.dmNothing;      
           
              oDmBrowser.Show(false);          
           
              return oDmBrowser.FileName;    }  
           
         }  
           
         </SCRIPT>  
           
            
  

![](../Images/UpArrow.gif)Top of page

## Operation of the Script

The btnOK_onclick() event handler script checks to see that both Input and Output text boxes contain some data. This data should be the name of a file. The command is then built up from the command 'copy &in=' followed by the input filename, followed by '&out=' and then followed by the output filename. Suitable spaces are introduced to satisfy the command syntax.

Appended onto the command is the retrieval criteria if it exists. 

The copy command is then invoked using the ParseCommand function.

The Browse buttons are used to call a function which will show the Browser window. The user then selects a filename and the function returns this value and populates the appropriate text box with it. The return statement in the function DisplayBrowser() will ensure that the FileName text is returned to the calling function when it is finished.