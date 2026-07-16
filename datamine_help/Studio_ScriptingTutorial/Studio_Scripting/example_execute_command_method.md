![](../HeaderCell.jpg) |  Example - The Execute Command Method  
---|---  
  
# The Execute Command Method

In the previous examples all commands have been accessed through the ParseCommand method of the Datamine Application Object. For example, with the following command:

oDmApp.ParseCommand("protom &OUT=" + tbModel.value + "@ROTMOD=0" +  
" N " + subcells +  
" " + tbOriginX.value +  
" " + tbOriginY.value +  
" " + tbOriginZ.value +  
" " + tbCellSizeX.value +  
" " + tbCellSizeY.value +  
" " + tbCellSizeZ.value +  
" " + tbNumCellsX.value +  
" " + tbNumCellsY.value +  
" " + tbNumCellsZ.value + " ");  

In each case the full set of files, fields, parameters and interactive responses must be included in the string that is sent by the command method to the Command Manager. 

If you want to invoke a command from a script, and you want the interactive responses to be properly interactive rather than pre-specified, then you must use the ExecuteCommand method instead of the ParseCommand method. For example.

oDmApp.ExecuteCommand("protom");

In this simple example you will be prompted interactively for the model origin, cell sizes etc. The script _scr_Example Model Prototype Interactive.htm can be run, and this file is found (with a standard installation) at C:\Database\DMTutorials\Projects\S3ScriptTut\Scripts

The Execute command method is really powerful when commands such as 'zoom-all' and 'new-string' must be used from a script as these have no parameters and therefore cannot use the ParseCommand method.