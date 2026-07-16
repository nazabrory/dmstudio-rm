# Create Contact Surface: Automation

Note: **Studio Geo** offers a workflow environment for implicit modelling commands via its Dynamic Modelling workflow. This lets you define structure-specific settings for one or multiple output structural models, and how those structures interact. You can even post-process outputs using macros and automatically generate a structural model for downstream estimation. Contact your local Datamine office for more details about the amazing Studio Geo.

**Note** : this topic is aimed at users familiar with COM-aware scripting languages, and the [surface-from-samples](<../command_help/surface-from-samples.md>) command.

The following information relates to the vein-from-samples and surface-from-samples commands.

The [Create Vein Surface](<Create_Vein_Surfaces_Overview.md>) task is a focussed tool for the calculation of hanging wall (HW) and/or footwall (FW) surfaces that represent vein or vein-like lodes. Similarly, the [Create Contact Surface](<../STUDIO_RM/Surface_From_Samples.md>) task is used to generate contact surfaces between groups of contiguous categorical values.

The surface-from-samples command features a rich COM interface that allows virtually all of the interactive options of vein modelling to be accessed from a script.

As with many scriptable commands in Studio products, you can access vein-from-samples using the ParseCommand() method, followed by a series of parameters that control the output.

## Scripted Command Setup

As with the interactive usage of the command, data must be loaded into memory before it can be accessed by the vein-from-samples command. Once a DmApplication object has been instantied (e.g. using "window.external;"), there are multiple ways to load data, including the LoadFile() and LoadFromProject() methods, e.g.:  

    
    
    var objHoles = oDmApp.ActiveProject.Data.LoadFile("C:\\Database\\Drillholes.dmx")  
  
---  
      
    
    var objHoles = oDmApp.ActiveProject.Data.LoadFromProject("Drillholes")  
  
## Command Syntax

The general syntax for this command is:
    
    
    surface-from-samples [Drillhole Object] [Field Name] [Above Values] [Parameter string]

Where:

[Drillhole Object] is a mandatory parameter and is a fully-qualified object name as it appears in the Sheets control bar, e.g.:
    
    
    "Drillholes=MyHoles (drillholes);"

[Field Name] is a mandatory parameter and is the name of the attribute containing the value to be modelled , e.g.:
    
    
    "Fieldname=ROCK"

[Above Values] is a mandatory parameter containing semi-colon-separated values qualified with an "AboveDatum=" prefix. For example; AboveDatum=0;AboveDatum=1;AboveDatum=2;

[Parameter String] is a semi-colon-separated string of parameters, all of which are optional, used to control how a surface or volume is generated. If no parameter value is listed, the default value is used, for example:
    
    
    "BoundaryObject="MyString (strings)";ClippingType="BoundaryString";Resolution="High";UseFirst=no;Output="MyOutputFile";"  
  
---  
  
  * surface-from-samples parameters set by script will not be reinstated to the user interface when subsequently using the command interactively.
  * Where field values are specified by script, the current [long field name settings](<Long_Field_Mode.md>) for your system is honoured; attribute names are restricted to either 8 or 24 characters depending on the current setting.

For more information on command parameters, plus examples, see the following sections.  

## Command Parameters

The parameter string for vein-from-samples can contain any of the following items. All parameters must be separated by a semi-colon (;). No parameters are mandatory as default values are used if any are absent. 

Any data objects referenced within parameters must exist in memory before the command is called from script.

Parameter |  Description |  Default  | Example  
---|---|---|---  
Data Context  
Drillholes (Mandatory) |  References the loaded drillholes object. |  null | 
    
    
    Drillholes=MyHoles(drillholes)  
  
FieldName (Mandatory) |  The attribute containing the value to be modelled |  null | 
    
    
    Fieldname=ROCK  
  
AboveValues (Optional) |  A semi-colon-separated list of prefixed values, which can be either numeric or alphanumeric |  null | 
    
    
    vAboveValues = "AboveDatum=0;AboveDatum=1;AboveDatum=2;"  
  
IgnoreDatum(Optional) |  A semi-colon-separated list of prefixed values, which can be either numeric or alphanumeric |  null | 
    
    
    vIgnoreValues = "IgnoreDatum=Value1;IgnoreDatum=Value2;"  
  
UseSelectedOnly |  Whether to only use the selected drillhole samples for the calculation. If no samples are selected, this parameter is ignored and all samples are used. |  yes | 
    
    
    UseSelectedOnly=no  
  
UseVisibleOnly |  Whether to only use the visible drillhole samples for the calculation. Any samples that are filtered out will not be used if this is set to "yes". |  yes | 
    
    
    UseVisibleOnly=no  
  
Section Plane (if not set, a 'best fit' section is used)  
UseCurrentSection  |  The plane to use when calculating surface normals with the Minimum Curvature method.

  * If no (default), the calculated best fit plane is used, unless PlaneAzimuth and PlaneDip are set.
  * If yes, the current 3D section is used

|  no | 
    
    
    UseCurrentSection=yes  
  
_PlaneAzimuth_ | If set, this is the azimuth of a custom projection plane. | null | 
    
    
    PlaneAzimuth=180.0  
  
PlaneDip | If set, this is the dip of a custom projection plane. | null | 
    
    
    DipAzimuth=45.0  
  
Snapping  
UseFirst |  Whether the surface should intercept at the first ("yes") or last ("no") lithology contact point. |  yes | 
    
    
    UseFirst=no  
  
IgnoredUnitsMethod |  Control how ignored units are treated:

  * 0: pass through ignored units with the best-fit surface;
  * 1: pass through ignored units at the midpoint;
  * 2: pass through ignored units at the top;
  * 3: pass through ignored units at the bottom.

|  0 | 
    
    
    IgnoredUnitsMethod=1  
  
CollarEOHOption |  Control if/how collar contact points are treated:

  * 0: snap to collar points;
  * 1: ignore all collar points;
  * 2: pass above collar points.

|  0 | 
    
    
    CollarEOHOption=1  
  
LastEOHOption |  Control if/how EOH contact points are treated:

  * 0: snap to EOH points;
  * 1: ignore all EOH points;
  * 2: pass below EOH points.

|  0 | 
    
    
    LastEOHOption=2  
  
Additional Points  
AdditionalPointsObject |  The full name of a loaded strings object. If not defined, no [additional points](<Create_Vein_Surfaces_9_Adding.md>) are used. |  null | 
    
    
    AdditionalPointsObject=Additional_Points_Drillholes (strings)  
  
Boundary  
ClippingType |  Defines the type of [boundary shaping](<Vein_Modelling_Boundary_Clipping.md>) to be applied. The following values are accepted:

  * AlphaShape: use alpha shape clipping, using the ClippingParameter value to set the Extension distance and the SegmentLength parameter to control segment length.
  * AlignedSquare: clip to a bounding cuboid, potentially extended by the ClippingParameter distance.
  * BoundaryString: clip to a nominated boundary string. If specified, BoundaryObject must also be specified. 
  * BlockModel: clip to a nominated block model. If specified, BoundaryObject must also be specified. Use BlockExtensionDistance to set the extension distance.

|  AlphaShape | 
    
    
    ClippingType=AlphaShape;ClippingParameter=25;SegmentLength=90
    
    
     
    
    
    ClippingType=AlignedSquare;ClippingParameter=50
    
    
     
    
    
    ClippingType=BoundaryString; BoundaryObject=MyBoundary (strings)
    
    
     
    
    
    ClippingType=BlockModel; BoundaryObject=ProtoModel (block model); BlockExtensionDistance=10  
  
ClippingParameter |  The extension distance to use when ClippingType=AlphaShape or ClippingType=AlignedSquare. |  50.0 |  See ClippingType  
Segment Length |  The alpha segment length to use when ClippingType=AlphaShape. |  50.0 |  See ClippingType  
BoundaryObject |  Mandatory if ClippingType=Custom or Block. Denotes the boundary string or block model object to be used. Warning: if specifying a boundary string object, the boundary string must contain a field with an attribute name that matches FieldName. The values within this field will denote independent boundary strings. Even if your string object contains a single, closed string, this attribute must be present in order to apply a custom boundary via scripting. |  null |  See ClippingType  
BlockExtensionDistance |  An optional extension distance to use if ClippingType=Block. |  null |  See ClippingType  
Faults  
FaultObject |  A loaded wireframe object containing fault data. Multiple fault wireframes within the file can be attributed by a unique FaultIDColumn value. |  null | 
    
    
    FaultObject=Fault_Sheet_Flattr/fault_sheet_flatpt (wireframe)  
  
FaultIDColumn |  Attribute that denotes independent fault sheets in the FaultObject.  If not specified, the fault wireframe is considered a single fault sheet. |  null | 
    
    
    FaultIDColumn=SURF  
  
ExtendFaults |  Whether to treat faults that terminate inside of a fault block as scissor faults. |  no | 
    
    
    ExtendFaults=yes  
  
Output  
Output |  The name of the wireframe object to be created. |  "VeinSurf_[Attribute]_[Value]" | 
    
    
    Output=MySurface"  
  
OutputBoundaryFile | The name of the output boundary strings object to create. If empty (default), no boundary strings object is generated. | Null | 
    
    
    OutputBoundaryFile=MyBoundaryObject  
  
OutputContactPoints | The name of the output contact points object to create. If empty (default), no contact points object is generated. | Null | 
    
    
    OutputContactPoints=MyContactPoints  
  
SuppressOutput |  Define if summary information is exported to the Output window when vein-from-samples is executed. Permitted values are "yes" or "no" | no | 
    
    
    SuppressOutput=yes  
  
##  Create Contact Surfaces Script Example 

In the following example, a file called "_vb_holes_edited.dm" is loaded from the project directory and referenced as a loaded object. 

The aim is to model the contact surface between two groups of lithological values held in an NLITH attribute; 0, 1 and 2 represent all "above" values and the remainder (2, 3 and 4, although these aren't stated explicitly - they are established as "below" by their lack of inclusion in the "above" list).

The output volume is clipped according to its alpha shape. Unless otherwise specified, default parameter values are used.

Finally, the output object is saved to disk as a wireframe pair file.

Contact Surfaces Automation Script Example
    
    
    var oDmApp=window.external;  
  
---  
      
    
    var objHoles=mApp.ActiveProject.Data.LoadFile("C:\\Database\\MyProjectFolder\\_vb_holes_edited.dm")  
      
    
    var vDrillholes = "_vb_holes_edited (drillholes);";  
      
    
    var vFieldName = "Fieldname=NLITH;";  
      
    
    var vAboveValues = "AboveDatum=0;AboveDatum=1;AboveDatum=2;";  
      
    
    var vIgnoreValues = "IgnoreDatum=Int1;IgnoreDatum=In2;"  
      
    
    var vClipType = "AlphaShape";  
      
    
    var vClipRadius = 40;  
      
    
    var vOutput = "contact_surface_007";  
      
    
    var vCommand = "vein-from-samples "   
      
    
         + vDrillholes + vFieldName + vAboveValues + vIgnoreValues;  
      
    
    var vExtras = "ClippingType=" + vClipType   
      
    
         +  
      
    
        "; ClippingParameter="   
      
    
         + vClipRadius +  
      
    
        "; Output="   
      
    
         + vOutput +  
      
    
        "; UseFirst=no"   
      
    
         +  
      
    
        "; UseEndOfHolePoints=no"   
      
    
         +  
      
    
        ";"  
      
    
    oDmApp.ParseCommand(vCommand+vExtras);  
      
    
    var saveobj = oDmApp.ActiveProject.Data.IsLoaded(vOutput);  
      
    
    saveobj.SaveAsDatamineFile(vOutput, oDmApp.ActiveProject.ExtendedPrecision,   
      
    
         true, ""); //save to physical file   
  
Related topics and activities

  * [Create Contact Surface](<../STUDIO_RM/Surface_From_Samples.md>)