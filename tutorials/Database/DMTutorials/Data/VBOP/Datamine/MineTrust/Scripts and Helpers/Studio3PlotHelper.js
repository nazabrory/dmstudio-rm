//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
// Studio 3 Plot Helper Class - to assist in the loading of Plot Templates
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

function Studio3PlotHelper(AP) {

    var self ;
    var oScript;
    
	// Methods 
	this.createPlot = createPlot;                           //returns boolean
	this.deletePlot = deletePlot;                           //returns boolean
    this.setDefaults = setDefaults;

	//you need to specify one of these - defaults are provided
	this.alwaysShowDialog           = showDialogAlways;
	this.neverShowDialog            = showDialogNever;
	this.showDialogWhenIncomplete   = showDialogWhenIncomplete;
	
	//you need to specify one of these - defaults are provided
	this.loadExistingDataOnly       = dataLoadExisting;
	this.loadRefreshData            = dataLoadRefresh;
	this.reloadData                 = dataLoadReload;
	
	//you need to specify one of these - defaults are provided
	this.loadSheetAlways            = sheetAlwaysLoad;
	this.loadSheetPartial           = sheetPartialLoad;
	this.loadSheetWhenIncomplete    = sheetWhenIncompleteLoad;

	// Properties
	this.oScript        = new ActiveXObject("DatamineStudio.ScriptHelper");
	this.oScript.debug  = false;
	this.ActiveProject = AP.ActiveProject;
    self                = this;
    
    //define some reasonable default parameters
    this.name       = "";
    this.pathname   = "" ;
    this.dialogShow = this.oScript.DmSheetTemplateDialog.dmSheetTemplateDialogNever ;
    this.dataLoad   = this.oScript.DmSheetTemplateData.dmSheetTemplateDataRefresh ;
    this.sheetLoad  = this.oScript.DmSheetTemplateSheet.dmSheetTemplateSheetPartial ;
	this.dataResize = true;
	this.debug      = false;
	
	function template() {
	//----------------------------------------------------------------------------
	//
	//	Function:		template
	//	Description:	template
	//
	//-----------------------------------------------------------------------------
        try {
            alert("Not Written Yet!");
        } catch(err) {
             error("Error - ");
			 return false;            
        }
    }

	function createPlot(PlotName) {
        try {
            if (PlotName == ""){
                error("Warning - create Studio 3 plot called with an empty name");
            }
            else
            {
                
                
                if (self.debug){
                    self.dialogShow = self.oScript.DmSheetTemplateDialog.dmSheetTemplateDialogAlways;
                    self.dataLoad   = self.oScript.DmSheetTemplateData.dmSheetTemplateDataExisting;
                    self.sheetShow  = self.oScript.DmSheetTemplateSheet.dmSheetTemplateSheetAlways;
                }
                return  self.ActiveProject.LoadSheetTemplateData(PlotName, self.dialogShow,
                                    self.dataLoad, self.sheetShow, self.dataResize);
            }
        } catch(err) {
            error("Error - creating Studio 3 plot "+PlotName);
			return false;            
        }
    }
    
    function deletePlot(){
        try {
            //some code in here to delete the plot sheet using the self.name
            if (self.name == "") {
                error("Warning - attempt to delete a plot sheet with an empty name");
            }
            else
            {
                return self.ActiveProject.RemovePlotSheet(self.name);
            }
        } catch(err) {
             error("Error - could not delete plot specified as "+self.name);
			 return false;            
        }
    }
    
    function setDefaults(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateDialog.dmSheetTemplateDialogNever ;
            self.dataLoad   = self.oScript.DmSheetTemplateData.dmSheetTemplateDataRefresh ;
            self.sheetLoad  = self.oScript.DmSheetTemplateSheet.dmSheetTemplateSheetPartial ;
	        self.dataResize = true;
	        self.debug      = false;
        } catch(err) {
        }
    }
   
    //Show the dialog - three options are 
    //  1 - DmSheetTemplateDialog.dmSheetTemplateDialogAlways - always shows the configuration dialog
    //  2 - DmSheetTemplateDialog.dmSheetTemplateDialogNever - never show the configuration dialog
    //  3 - DmSheetTemplateDialog.dmSheetTemplateDialogIncomplete - show the dialog when data is incomplete
    //      this depends on how the data is loaded - with data loaded as Existing this will allow the
    //      user to match up files that have been used in the template but which cannot be found on disk

    function showDialogAlways(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateDialog.dmSheetTemplateDialogAlways ;
        } catch(err) {
        }
    }
    function showDialogNever(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateDialog.dmSheetTemplateDialogNever ;
        } catch(err) {
        }
    }
    function showDialogWhenIncomplete(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateDialog.dmSheetTemplateDialogIncomplete ;
        } catch(err) {
        }
    }
   
    //load the data 
    //  1 - DmSheetTemplateData.dmSheetTemplateDataExisting - load existing data only and do not show data that
    //          cannot be found
    //  2 - DmSheetTemplateData.dmSheetTemplateDataRefresh - refresh the data when it is loaded - loads existing 
    //          and then tries to refresh other data that may be in other directories - it looks in the 
    //          project folder for files that it cannot source
    //  3 - DmSheetTemplateData.dmSheetTemplateDataReload - reload data into studio 3 and then show the plot.
  
    function dataLoadExisting(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateData.dmSheetTemplateDataExisting ;
        } catch(err) {
        }
    }
    function dataLoadRefresh(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateData.dmSheetTemplateDataRefresh ;
        } catch(err) {
        }
    }
    function dataLoadReload(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateData.dmSheetTemplateDataReload ;
        } catch(err) {
        }
    }
   
    //create the sheet
    //  1 - DmSheetTemplateSheet.dmSheetTemplateSheetAlways - always show the sheet even if data is not loaded
    //  2 - DmSheetTemplateSheet.dmSheetTemplateSheetPartial - show the sheet if partial data is loaded
    //  3 - DmSheetTemplateSheet.dmSheetTemplateSheetFull - show the sheet only when all the data is loaded

    function sheetAlwaysLoad(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateSheet.dmSheetTemplateSheetAlways ;
        } catch(err) {
        }
    }
    function sheetPartialLoad(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateSheet.dmSheetTemplateSheetPartial ;
        } catch(err) {
        }
    }
    function sheetWhenIncompleteLoad(){
        try {
            self.dialogShow = self.oScript.DmSheetTemplateSheet.dmSheetTemplateSheetFull ;
        } catch(err) {
        }
    }
   
    function error(strMessage){
	    alert(strMessage);
	    return false;	
	}	


}
