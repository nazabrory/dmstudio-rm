# Running the Polygon Script

You can access your application and activate the Home ribbon to select JScript | Run Script and specify the name of the HTML file that you have created. This is how it would normally be run, and this is the only way that you can check that the HTML interface looks right inside your application.

## Debugging the Script with Alert

Microsoft provides a number of sophisticated debugging environments, which are by far the best way of understanding where a script is going wrong. But, for this example, the simplest debugging aid is the JavaScript alert() function that you used earlier.

With alert() you can display messages and the values of variables in a pop-up message box which is created at some point during the execution of your script.

For example, to check the value of the Filter text box before attempting to use it, you can add the following statement usually within or close to the place that it is used such as the btnOK_onclick event handler:
    
    
    alert("The current filter is " + tbFilter.value);

When executed, this statement produces a message box similar to the following:

![](../Images/Studio3%20Scripting%20Polygon%200004.jpg)

There are limitations to this method of debugging; inserting an in-line alert statement will pause your script waiting for further input (which can be useful) but it will only be able to report information that is 'known' up to that point - for example, if your script introduced a cyclic loop that prevented it from arriving at the **alert**() message, the message itself would never be displayed and would be of little use. Other options are available in scripting languages to allow a particular function to be run in case of any error code being returned. This is outside the scope of this tutorial.