![](../HeaderCell.jpg) |  Introduction to Running a Macro  
---|---  
  
# Introduction to Running a Macro

You may already have macros that you use for running sequences of commands. Input to these macros is usually through either the prompt or screen command. However as you will have already realized the HTML interface provides a far more attractive, comprehensive and easy to use method of entering files, fields, parameters and other runtime variables. 

In order to take advantage of the HTML interface you don't have to convert your entire macro to script. You can simply set up the interface in HTML and pass the values of the variables to your macro. Therefore the only changes you need to make to your macro are to remove the prompt or screen commands and allow the macro to read the variable values which you have entered through the HTML interface. At the end of the macro you can pass the values of variables back to the script.

Scripting uses the 'var' file to transfer variables and their values between the script and the macro. This is the file already used by the varload and varsave macro commands for saving information between Datamine sessions. It is also the file used by the older versions of these commands, STKPAR and STKSAV. The varload() and varsave() methods provide the equivalent functions in scripting, and are included as part of the Datamine Application Object. The macro will be executed using the ParseCommand method of the Application Object.