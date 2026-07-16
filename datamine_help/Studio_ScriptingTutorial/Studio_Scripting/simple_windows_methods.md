# Simple Windows Methods

There are three commonly used windows methods which can be added to a script.

  * alert() - displays a message to the user.

  * confirm() - prompts the user to click an OK or Cancel button to confirm or cancel an operation.

  * prompt() - prompts the user to enter a text string or some values.

All these methods display a simple dialog to the screen called a popup dialog box.

## Prerequisites

  * The file SortCollars.htm is used in the exercises below. This file sorts the collars using the file _scr_SortCollars.htm and outputs the file tempcollar.htm, and can be found at C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts

## Exercise: Adding an Alert

In this exercise we will add an alert message to a script. The alert() method is used to display a dialog box containing the value of a variable or a text string. For example insert an alert() at the start of the function to display a title.

  1. View the file _scr_SortCollars.htm located in the `C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts` directory, using Notepad.
  2. Locate the line starting with oDmApp.ParseCommand.
  3. Enter the alert command with suitable text as shown below:

alert("This script sorts the collars file using BHID");

`oDmApp.ParseCommand("sortx &IN=dhcollar &OUT=SortedCollars *KEY1=BHID @BINS=5 @ORDER=1");`

  7. Save the file as 'SortCollars.htm'. 

The file extension should be defined for you. Leave this application open with the loaded file as we shall use this in later exercises.

  8. Select Scripts >> Run Script... from the Home ribbon.

  9. In the Browsing for script file... dialog select the `_scr_SortCollars`.htm file (this file was created in step 6).

  10. In the Customization window note that the script is loaded and shows the 'SortCollars' text.

  11. Clear the Command window by right-clicking in the window and selecting Clear from the menu.

  12. Execute the script.

  13. The popup message displays:

![](../Images/Studio3%20Scripting%20Simple%20Windows%200001.jpg)

  14. Click OK.

  15. The Command window now shows the output from the script.

![](../Images/UpArrow.gif)Top of page

## Exercise: Adding a Prompt

The prompt() method displays a dialog which includes a message that you set and provides a text field for you to enter a response. Two buttons, Cancel and OK, give you the option to:

  * Cancel \- cancel the entire operation

  * OK \- accept the input and continue the operation

The prompt() method has two arguments; the first is the prompt message which is displayed on the dialog. The second argument is a default reply which is displayed in the text box. If you don't want to specify a default reply then just enter two successive double quotes ("").

The method returns a value when you click on one of the buttons. 

Clicking Cancel returns a value of null, irrespective of what is in the text box. Clicking OK returns the value of the text string in the text box.

We will use the prompt() method to request the name of the collars file, and store the value in variable cfile. You should then add a test to check the value of cfile. If cfile is empty ("") or null then return will terminate the function.

Finally you will need to replace the hard-coded file name dhcollar by the variable name cfile in the command which sorts the file. Note that cfile is a variable, and so must not be included within the double quotes. Therefore, the argument for oDmApp.ParseCommand is split into three parts separated by a '+' sign as shown in the example below. Make sure there is a space immediately in front of &OUT=tempcollars, so that files, fields and parameters are all separated by spaces. Then;

  1. Continue to use the `_scr_SortCollars` file in Notepad.
  2. Enter the following two lines between the alert and the oDmApp command as shown below.

    
    
    alert("This script sorts the collars file using BHID");
    
    
     
    
    
    var cfile = prompt("Enter the name of the collars file: ", "dhcollar");
    
    
     
    
    
    if (cfile == "" || cfile == null) return;
    
    
     
    
    
    oDmApp.ParseCommand("sortx &IN=" + cfile + " &OUT=SortedCollars *KEY1=BHID @BINS=5 @ORDER=1");

In the text above the '=' is an assignment and the '==' is a comparison. The '||' is a boolean operator meaning OR. The whole expression reads 'if cfile is empty or cfile is null then return'. It should be noted that if the '=' replaces the '==' then an assignment would take place within the 'if' decision , however, the code would not be incorrect. This is a common mistake using this language construct.

  3. Save your text file.
  4. Refresh the Customization window (and re-load the script) by right-clicking it and selecting Refresh.
  5. Clear the Command window by right-clicking in the window and selecting Clear from the menu.
  6. Execute the script. Note that the alert message still shows. Click OK.
  7. The prompt message is now displayed and shows the default `dhcollar` file name. clear the text box and click OK.

![](../Images/Studio3%20Scripting%20Simple%20Windows%200002.jpg)

  8. Nothing appears in the Command window output as the filename was blank.
  9. Repeat step 7 and with the `dhcollar` filename in the text box click **OK**.
  10. The Command window now shows the output from the script.
  11. Perform this exercise for the output file as well. Remember, you can use the right-click menu in the Customization pane to select Refresh \- this will reload the last saved script file state.

The text after the edit for the output file should look similar to the following. The names of the variables and text used may differ.
         
         alert("This script sorts the collars file using BHID");
         
          
         
         var cfile = prompt("Enter the name of the collars file: ", "dhcollar");
         
          
         
         if (cfile == "" || cfile == null) return;
         
          
         
         var ofile = prompt("Enter the name of the output file: ", "SortedCollars");
         
          
         
         if (ofile == "" || ofile == null) return;
         
          
         
         oDmApp.ParseCommand("sortx &IN=" + cfile + " &OUT=" + ofile  + " *KEY1=BHID @BINS=5 @ORDER=1");

![](../Images/UpArrow.gif)Top of page

## Exercise: Adding a Confirmation

The confirm() method displays a dialog that includes a user specified message and provides two buttons, Cancel and OK. This is similar to prompt() except that the only response is to click one of the two buttons. The method returns the Boolean value true if OK is clicked or false if Cancel is clicked. You can then add code to act according to which button has been clicked. For example use confirm() to display the names of the files that have been selected, and to abort the operation if Cancel is clicked.

  1. Continue to edit the `_scr_SortCollars` file in a text editor:

Enter the following confirm line between the comparison for the output file and the oDmApp command as shown below:
         
         alert("This script sorts the collars file using BHID");
         
          
         
         var cfile = prompt("Enter the name of the collars file: ", "dhcollar");
         
          
         
         if (cfile == "" || cfile == null) return;
         
          
         
         var ofile = prompt("Enter the name of the output file: ", "SortedCollars");
         
          
         
         if (ofile == "" || ofile == null) return;
         
          
         
         if (!confirm("The input file selected is: \n" + "Collars: " + cfile +"\n\n The output file is: " + ofile)) return ;
         
          
         
         oDmApp.ParseCommand("sortx &IN=" + cfile + " &OUT=" + ofile  + " *KEY1=BHID @BINS=5 @ORDER=1");

The '\n' character above forces a new line in the output text.

The '!' in front of confirm() reverses the Boolean value. For example if Cancel is clicked, the value of confirm() will be false. However adding '!' will make the response true, so the action will be return and the operation will terminate. The whole expression reads 'if the files are not OK then return'.

  1. Save your text file.
  2. Back in your application, use the Home ribbon to select Scripts >> Run Script
  3. In the Browsing for script file... dialog select the `_scr_SortCollars`.htm file.
  4. Clear the Command window by right clicking in the window and selecting Clear from the menu.
  5. Execute the script. Note that the alert message still shows as well as both prompts. Click OK to all prompt and alert dialogs.
  6. The confirm message is now displayed:

![](../Images/Studio3%20Scripting%20Simple%20Windows%200003.jpg)

Click Cancel and note that no output is displayed within the Command output window.

  7. Repeat step 7 and click OK to the confirm message.
  8. The Command window now shows the output from the script.

![](../Images/UpArrow.gif)Top of page

Note: The alert() and confirm() methods are particularly useful for debugging a script. Although the prompt() method can be used to enter a value it is a rather crude way of doing so. One of the main advantages of scripting is using HTML to create an attractive interface, as we will soon see.