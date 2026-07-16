![](../HeaderCell.jpg) |  Holes3D script example  
---|---  
  
# Holes3D Full Script example

var oDmApp= null;

var oScript = null;

function AutoConnect()

{

try {

oScript = new ActiveXObject("DatamineStudio.ScriptHelper");

oScript.initialize(window);

oDmApp = oScript.getApplication();

if (oDmApp == null || oDmApp.ActiveProject == null) //Attempt to Use the Active Datamine Session

{

alert("There are no active Studio3 projects open.\n Please open a project before continuing.");

window.close(); // Closes the script window

return false;

}else

return true;

}

catch(e) {

alert("Failed\nReason: " + e.description);

if ( oDmApp) oDmApp.Quit(); // release the session to close it down

}

return false;

}

function btnExecute_onclick()

{

try {

if (!AutoConnect())

return;

oDmApp.ParseCommand("sortx &IN=dhcollar &OUT=tempcollar *KEY1=BHID @BINS=5 @ORDER=1");

oDmApp.ParseCommand("sortx &IN=dhassays &OUT=tempassays *KEY1=BHID *KEY2=FROM @BINS=5 @ORDER=1");

oDmApp.ParseCommand("sortx &IN=dhlith &OUT=templith *KEY1=BHID *KEY2=FROM @BINS=5 @ORDER=1");

oDmApp.ParseCommand("sortx &IN=dhsurvey &OUT=tempsurvey *KEY1=BHID *KEY2=AT @BINS=5 @ORDER=1");

oDmApp.ParseCommand("holmer &IN1=tempassays &IN2=templith &OUT=temp1 *BHID=BHID *FROM=FROM *TO=TO");

oDmApp.ParseCommand("join &IN1=tempcollar &IN2=temp1 &OUT=temp2 *KEY1=BHID @SUBSETR=1 @SUBSETF=0 @CARTJOIN=0 @PRINT=0");

oDmApp.ParseCommand("desurv &IN1=temp2 &IN2=tempsurvey &OUT=dholes @SURVSMTH=1 @PRINT=0");

oDmApp.ParseCommand("ddlist &IN=dholes");

}

catch(e) {

alert("Failed\nReason: " + e.description);

}

}

function btnHelp_onclick()

{

var features = "height=600,width=400,status=yes,toolbar=no,menubar=no,location=no scrollbars=yes";

var common = "holes3d";

var installpath = "C:/Program Files/Datamine/Studio3/";

installpath = installpath.replace(" ", "%20");

var helpcommand = "mk:@MSITStore:" + installpath + "/Help/DatamineStudio.chm::/Studio_3_General/Concept_Studio%203%20Scripting%20Overview.htm";

window.open(helpcommand , common, features);

}

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Recording and Playback of Scripts](<recording_and_playback_of_scripts.md>)