![](../HeaderCell.jpg) |  Command Syntax  
---|---  
  
# Command Syntax

The JavaScript describing the action taken when the Execute button is clicked is shown below. You can see that each command is run using the function oDmApp.ParseCommand(). The command name and the corresponding files, fields and parameters are entered as a character string (i.e. enclosed within double quotes). If the string extends to two or more lines then each line is a separate string and the strings are joined using the + character.

function btnExecute_onclick()

{

try

{

AutoConnect();

oDmApp.ParseCommand("sortx &IN=dhcollar &OUT=tempcollar *KEY1=BHID @BINS=5 @ORDER=1");

oDmApp.ParseCommand("sortx &IN=dhassays &OUT=tempassays *KEY1=BHID *KEY2=FROM @BINS=5 @ORDER=1");

oDmApp.ParseCommand("sortx &IN=dhlith &OUT=templith *KEY1=BHID *KEY2=FROM @BINS=5 @ORDER=1");

oDmApp.ParseCommand("sortx &IN=dhsurvey &OUT=tempsurvey *KEY1=BHID *KEY2=AT @BINS=5 @ORDER=1");

oDmApp.ParseCommand("join &IN1=tempcollar &IN2=tempassays &OUT=temp1 *KEY1=BHID @SUBSETR=1 @SUBSETF=0 @CARTJOIN=0 @PRINT=0");

oDmApp.ParseCommand("holmer &IN1=temp1 &IN2=templith &OUT=temp2 *BHID=BHID *FROM=FROM *TO=TO");

oDmApp.ParseCommand("desurv &IN1=temp2 &IN2=tempsurvey &OUT=dholes @SURVSMTH=1 @PRINT=0");

oDmApp.ParseCommand("ddlist &IN=dholes");

}

catch(e)

{

alert("Failed\nReason: " + e.description);

}

}

Note that as for macros, symbolic file names are preceded by & (e.g. &IN), field names by * (e.g. *BHID) and parameters by @ (e.g. @BINS=5). However unlike macros there is an equals sign (=) between the symbolic and actual file names (e.g. &IN=dhcollar) and between the symbolic and actual field names (e.g. *KEY1=BHID). The files, field and parameter assignments are separated by one or more spaces.

If you made a mistake when entering the commands you can now edit the code. Make sure you keep the syntax correct. If while entering the commands you clicked in the Design Window, then you will find that the command oDmApp.ParseCommand("select-string"); has been recorded. This can be deleted.

If you have made any changes then save the file before exiting. In order to run the edited script you can either click the run script toolbar icon or select Tools | Scripting | Run Script..., from the menu. You can also right click on the background of the Customization window and select Refresh from the popup menu. Clicking the Execute button will re-run the script.

## Command Syntax

The full syntax for a command is

command &[name = ] actualName ...

*symbolicField = actualField ...

@symbolicParameter = value, value, ... ...

{filterExpression}

'data' ...

Note that

  * The symbols '...' means that the entry may be repeated any number of times.

  * The symbol '[name = ]' means that the symbolic name is optional.

  * Your appllication uses '&', '*' and '@' to differentiate names, fields and parameters.

  * Parameters can have multiple values, where appropriate.

  * Long file names (up to 20 characters) can be used, whereas macros are restricted to 8 characters.

##  Examples of Command Syntax

The following example allows a new string to be created in Studio.

The following script example is one that can be used to automate the creation of a string, including the coordinates of each vertex:

oDmApp.ParseCommand("new-string"+

" @attribute='COLOUR',18.0");

oDmApp.ParseCommand("new-string"+

" @point=5941.73205,5180.08912,184.6571,1"+

" @point=5911.08641,5127.06182,184.6571,1"+

" @point=5925.89273,5066.80353,184.6571,1"+

" @point=5964.80237,5057.85087,184.6571,1"+

" @point=6032.29166,5093.66151,184.6571,1"+

" @point=6036.76799,5145.31148,184.6571,1"+

" @point=5995.44802,5173.89113,184.6571,1"+

" @point=5942.07639,5181.81079,184.6571,4");

oDmApp.ParseCommand("cancel-command");