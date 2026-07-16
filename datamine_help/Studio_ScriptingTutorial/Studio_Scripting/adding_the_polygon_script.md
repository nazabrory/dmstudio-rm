# Adding the Polygon Script  
  
The first step is now complete: you have an HTML user interface, together with all the hooks for the script.

Unlike macros and menus, scripts are usually made up of a number of "event handlers". These are small sections of script that are executed by the browser when some relevant event occurs.

Only two events are handled in this script:

  * When the window loads (a window onload event occurs). We use this event to make a connection to the Datamine Application Object.

  * When the OK button is pressed (a button onClick event occurs). We use this event to ensure that point and/or string data is processed and saved.

## Prerequisites

  * Ensure a suitable scripting environment is available.

  * We will continue to use the Polygon.htm file created in the previous exercise.

## Exercise: Adding the windows onload event

In this exercise we will add an event to your HTML code, that will be fired when the window is loaded.

  1. Open the HTM page constructed as part of [Creating the Polygon Interface](<creating_the_polygon_interface.md>) in Notepad.

  2. Anywhere between the <HEAD> and </HEAD> tags, define a <SCRIPT language = "Javascript"> tag and a closing </SCRIPT> tag.

In between these two tags, create a function that will be triggered when a page is loaded (you'll set up the event itself in a moment).
         
         <SCRIPT language = "Javascript">      
  
---  
           
         function window_onload() {}      
           
         </SCRIPT>  
  

  4. You now need to enter the JavaScript code to be executed when this event occurs. First, you need to establish a connection between the script and the Datamine Application Object. To accomplish this we must define a Datamine application variable, and refer to a routine to instantiate the Datamine application object. 
  5. Before the function window_onload() (but after the <SCRIPT...> tag) type the following text:
         
         var oDmApp = null;      
  
---  
           
         var oScript = null;  
  

  4. Within the body of the window_onload() function (between the '{' and '}' characters), type the text 'AutoConnect();'. This instructs the onload event to call a function AutoConnect that you will now construct.  
  
This routine will use the variable oDmApp defined in step (5) above.
  5. After the window_onload() function and after the '}' symbol copy and paste (as HTML) the following text:
         
         function AutoConnect() {          
  
---  
           
         oScript = window.external.System.CreateObject("DatamineStudio.ScriptHelper");      
           
         oScript.initialize(window);      
           
         oDmApp = oScript.getApplication();      
           
            
           
         if (oDmApp== null)      
           
         {  
           
         return false;      
           
         }  
           
         else      
           
         {return true;    }  
           
         }  
  

  8. To check; the code that appears immediately after the opening <SCRIPT...> tag should look like the following:
         
         var oDmApp = null;      
  
---  
           
         var oScript = null;function   
           
         window_onload() {      
           
         AutoConnect();  
           
         }  
           
            
           
         function AutoConnect() {          
           
         oScript = window.external.System.CreateObject("DatamineStudio.ScriptHelper");      
           
         oScript.initialize(window);      
           
         oDmApp = oScript.getApplication();      
           
         if (oDmApp== null){      
           
         return false;      
           
         }  
           
         else      
           
         {  
           
         return true;  
           
         }  
           
         }  
  

  9. Next, you need to ensure the window_onload function is called each time the web page is opened. This can be done using the <BODY> tag's onload event.

Change the <BODY> tag to this:  
  

         
         <BODY onload="AutoConnect();">  
         

  10. Now, each time the page loads, the AutoConnect() function will be called, creating a Datamine Application (oDmApp) and a scripting helper (oScript) object.

**Note** : The variable oDmApp, oScript and the AutoConnect function are necessary for every scripted solution that connects to the Datamine Application Object. The AutoConnect function initialises the Datamine Application Object and presents the script with access to this object via the oDmApp variable. The oScript variable gives access to the Script Helper object.

![](../Images/UpArrow.gif)Top of page

## Exercise: Adding the OK button onClick event

In this exercise you will add an onClick event that will be fired when the OK button is pressed. When the button is pressed, the script saves the point and/or string data, process it using CONPOL and other commands, then re-load the resulting polygon back into the 3D Window

  1. Viewing the source code of yoru script again, add the following code just before the closing </SCRIPT> tag

`function btnOK_onclick() {}`

  3. Within the body of the btnOK_onclick() function (between the '{' and '}' characters), copy and paste (as HTML) the following text:
         
         //   
  
---  
           
              Remove temporary work files    oDmApp.ActiveProject.Deletefile('_tmp*');//   
           
                 alert("The current filter is " + txtFilter.value);  
           
             if   
           
              (chkIncPoint.checked) //  Create file from point data with XP   
           
              and YP only  
           
             {  
           
                 oDmApp.ActiveProject.Design.SaveAllPointsAsDmFile("_tmp001",   
           
              true, "");  
           
                 if   
           
              (txtFilter.value != "")  
           
                 {  
           
                     oDmApp.ParseCommand("picrec   
           
               &IN=_tmp001 &OUT=_tmp001a @APPEND=0 '" + txtFilter.value   
           
              + "' 'END'");  
           
                     oDmApp.ParseCommand("copy   
           
              &IN=_tmp001a &OUT=_tmp001");  
           
                 }  
           
                 oDmApp.ParseCommand("extra   
           
              &in=_tmp001 &out=_tmp002 'XP=XPT YP=YPT erase(XPT,YPT,ZPT,SYMBOL)   
           
              go'");  
           
             }  
           
             if   
           
              (chkIncString.checked) // Create file from string data with XP and   
           
              YP only  
           
             {  
           
                 oDmApp.ActiveProject.Design.SaveAllStringsAsDmFile("_tmp003",   
           
              true, "");  
           
                 if   
           
              (txtFilter.value != "")  
           
                 {  
           
                     oDmApp.ParseCommand("picrec   
           
               &IN=_tmp003 &OUT=_tmp003a @APPEND=0 '" + txtFilter.value   
           
              + "' 'END'");  
           
                     oDmApp.ParseCommand("copy   
           
              &IN=_tmp003a &OUT=_tmp003");  
           
                 }  
           
                 oDmApp.ParseCommand("extra   
           
              &in=_tmp003 &out=_tmp004 {'" + txtFilter.value + "'}   
           
              'erase(ZP,PTN,PVALUE,SYMBOL,LSTYLE) go'");  
           
             }  
           
               
           
             if   
           
              (chkIncPoint.checked && chkIncString.checked) // Append string   
           
              coordinates to point coordinates  
           
             {  
           
                 oDmApp.ParseCommand("append   
           
              &IN1=_tmp002 &IN2=_tmp004 &OUT=_tmp005 @SEQUENCE=0 @PROTODD=0   
           
              @PRINT=0");  
           
                 oDmApp.ParseCommand("copy   
           
              &IN=_tmp005 &OUT=_tmp002");  
           
             }  
           
             else   
           
              if (chkIncString.checked  && !chkIncPoint.checked)  
           
             {  
           
                 oDmApp.ParseCommand("copy   
           
              &IN=_tmp004 &OUT=_tmp002");  
           
             }  
           
             //   
           
              All X,Y coordinates are now in _tmp002.  Now run CONPOL.  
           
             var   
           
              command = "conpol &IN=_tmp002 &PERIMOUT=_tmp001 *X=XP   
           
              *Y=YP";  
           
             if   
           
              (txtExtDist.value != "")  
           
                 command   
           
              += " @EXTDIS=" + txtExtDist.value;  
           
             oDmApp.ParseCommand(command);  
           
             oDmApp.ParseCommand("proper   
           
              &PERIMIN=_tmp001 &PERIMOUT=_tmp002 @TOL=0.000001 @CLOSE=1");  
           
             oDmApp.ActiveProject.Data.LoadFromProject("_tmp002");   
           
              // load new polygon into design window  
           
             oDmApp.ActiveProject.Deletefile('_tmp*');  
  

![](../Images/UpArrow.gif)Top of page

## Operation of the Script

The btnOK_onclick() event handler script creates and uses several temporary files, all called "_tmp00n", which are deleted both at the beginning and at the end of the script.

If the Include point data check-box is checked, the script writes all point data to a file, using the PICREC command the file is then filtered as specified in the "Filter" text box, if any. This file is then processed by EXTRA to remove all but the XP and YP fields.

If the Include string data check-box is checked, the script writes strings to another file, again using the command PICREC and whatever filter has been specified, and uses EXTRA to remove and rename fields. If both check-boxes were ticked, it appends all the data into one file.

Next, the script runs CONPOL. Notice how the basic command is assigned to a JavaScript variable, and the value for the EXTDIS parameter is added if appropriate.

CONPOL does not close the resulting polygon. Hence the script uses PROPER to close it before re-loading the polygon into the Design Window.

Finally, the script deletes all the temporary files created during the execution.