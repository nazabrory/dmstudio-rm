# Create Vein Surface: Automation

Note: **Studio Geo** offers a workflow environment for implicit modelling commands via its Dynamic Modelling workflow. This lets you define structure-specific settings for one or multiple output structural models, and how those structures interact. You can even post-process outputs using macros and automatically generate a structural model for downstream estimation. Contact your local Datamine office for more details about the amazing Studio Geo.

**Note** : This topic is aimed at users familiar with COM-aware scripting languages, and the [vein-from-samples](<Create_Vein_Surface.md>) command. For an overview of scripting in this product, please refer to your scripting tutorial (Help | Scripting Tutorial).

## Command Automation Overview

The following information relates to the vein-from-samples and surface-from-samples commands.

The [Create Vein Surface](<Create_Vein_Surfaces_Overview.md>) task is a focussed tool for the calculation of hanging wall (HW) and/or footwall (FW) surfaces that represent vein or vein-like lodes. Similarly, the [Create Contact Surface](<../STUDIO_RM/Surface_From_Samples.md>) task is used to generate contact surfaces between groups of contiguous categorical values.

The vein-from-samples command features a COM interface that allows virtually all interactive options of vein modelling to be accessed via script.

As with many scriptable commands in Studio products, you can access **vein-from-samples** using the ParseCommand() method, followed by a series of parameters that control the output.

## Scripted Command Initialization

As with the interactive usage of the command, data must be loaded into memory before it can be accessed by the vein-from-samples command. Once a DmApplication object has been instantied (e.g. using "window.external;"), there are multiple ways to load data, including the LoadFile() and LoadFromProject() methods, for example:  

    
    
    var objHoles = oDmApp.ActiveProject.Data.LoadFile("C:\\Database\\Drillholes.dm")
    
    
    var objHoles = oDmApp.ActiveProject.Data.LoadFromProject("Drillholes")  
    

### Command Syntax

The general syntax for this command is:
    
    
    vein-from-samples [Drillhole Object] [Field Name] [Field Value] [Parameter string]

Where:

**[Drillhole Object]** is a mandatory parameter and is a fully-qualified object name as it appears in the Sheets control bar, e.g.:
    
    
    "Drillholes=MyHoles (drillholes);"

**[Field Name]** is a mandatory parameter and is the name of the attribute containing the value to be modelled , e.g.:
    
    
    "Fieldname=ROCK"

**[Field Value]** is a mandatory parameter and is the categorical value you wish to model, e.g.:
    
    
    "Value=LODE"

**[Parameter String]** is a semi-colon-separated string of parameters, all of which are optional, used to control how a surface or volume is generated. If no parameter value is listed, the default value is used, for example:
    
    
    "BoundaryObject="MyString (strings)";PinchOut="yes";ClippingType="BoundaryString";Resolution="High";"

For more information on command parameters, plus examples, see the following sections.  

## Command Parameters

The parameter string for vein-from-samples can contain any of the following items. All parameters must be separated by a semi-colon (;). No parameters are mandatory as default values are used if any are absent. 

Any data objects referenced within parameters must exist in memory before the command is called from script.

Parameter |  Description |  Default  | Example  
---|---|---|---  
Data Context  
Drillholes (Mandatory) |  References the loaded drillholes object. |  null | 
    
    
    Drillholes=MyHoles (drillholes)  
  
FieldName (Mandatory) |  The attribute containing the value to be modelled |  null | 
    
    
    Fieldname=ROCK  
  
Value (Mandatory) |  The attribute value to be modelled |  null | 
    
    
    Value=LODE  
  
UseSelectedOnly |  Whether to only use the selected drillhole samples for the calculation. If no samples are selected, this parameter is ignored and all samples are used. |  yes | 
    
    
    UseSelectedOnly=no  
  
UseVisibleOnly |  Whether to only use the visible drillhole samples for the calculation. Any samples that are filtered out will not be used if this is set to "yes". |  yes | 
    
    
    UseVisibleOnly=no  
  
Section Plane (if not set, a 'best fit' section is used)  
UseCurrentSection  |  The reference plane to use when calculating the vein surface.

  * If no (default), the calculated best fit plane is used, unless PlaneAzimuth and PlaneDip are set.
  * If yes, the current 3D section is used

|  no | 
    
    
    UseCurrentSection=yes  
  
_PlaneAzimuth_ | If set, this is the azimuth of a custom projection plane. | null | 
    
    
    PlaneAzimuth=180.0  
  
PlaneDip | If set, this is the dip of a custom projection plane. | null | 
    
    
    DipAzimuth=45.0  
  
Edit Samples  
MergeGaps |  Control if/how sample gaps are treated:

  * 0: do not merge samples. Only the first HW and FW value are used.
  * 1: merge samples so that only the first HW and final FW (or end-of-hole if set) are used.
  * 2: ignore any samples that have multiple value intervals.

|  0 | 
    
    
    MergeGaps=50  
  
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
  
Controls  
MinimumThickness |  The value to be used to either remove data (below) or the depth to expand the output volume depending on whether RemoveBelow is "yes" or "no" (see below). |  0.05 | 
    
    
    MinimumThickness=0.25  
  
RemoveBelow | 

  * If set to yes, any volume that is below the MinimumThickness is removed/pinched out. This equates to the Remove below UI option.
  * If set to no, any volume below the MinimumThickness is expanded to that value. This equates to the Expand to UI option.

|  yes | 
    
    
    RemoveBelow=no  
  
MaximumThickness |  An optional value to set the maximum thickness of the vein. |  null | 
    
    
    MaximumThickness=30  
  
BoundaryThickness |  An optional value to set the boundary thickness of the vein. |  null | 
    
    
    BoundaryThickness=0.0  
  
Resolution |  Sets the density of the grid used to form the output volume, using one of these values:

  * VeryLow
  * Low
  * Medium
  * High
  * VeryHigh

|  Medium | 
    
    
    Resolution=Low  
  
PinchOut |  Determines if HW and FW surfaces is pinched out if they become inverted. Either yes or no. |  yes | 
    
    
    PinchOut=no  
  
Output  
OutputVeinFile |  The name of the wireframe object to be created. |  "VeinSurf_[Attribute]_[Value]" | 
    
    
    OutputVeinFile=MyVein  
  
OutputMeanSurfaceFile |  If specified, a trend surface is generated of the specified object name. |  "VeinTrend_[Attribute]_[Value]" | 
    
    
    OutputMeanSurfaceFile=MyMeanSurface  
  
OutputBoundaryFile | The name of the output boundary strings object to create. If empty (default), no boundary strings object is generated. | Null | 
    
    
    OutputBoundaryFile=MyBoundaryObject  
  
OutputContactPoints | The name of the output contact points object to create. If empty (default), no contact points object is generated. | Null | 
    
    
    OutputContactPoints=MyContactPoints  
  
SuppressOutput |  Whether summary information is prevented from being printed to the Output window when vein-from-samples is executed. Permitted values are "yes" or "no" | no | 
    
    
    SuppressOutput=yes  
  
SurfaceType |  Choose which data to be output from the command. Valid values are: 0: Hangingwall only 1: Footwall only 2: A volume representing both surfaces (default) | 2 | 
    
    
    SurfaceType=1  
  
## Command Automation Examples

### Simple Lithological Modelling Example

In the following example, a file called "holes.dm" is loaded from the project directory and referenced as a loaded object. The value **NLITH** =3 is used to create a volume representing a non-pinched out surface. A Gaussian calculation is performed to interpolate the HW and FW surfaces.

The surface is intersected with a fault surface (`Fault_Sheet_Flattr/fault_sheet_flatpt`) splitting the output into independent two blocks, emulating a reverse fault.

The output volume (`SurfaceType=2` is set as example, despite this being the default value) is clipped according to its alpha shape, and as the surface is suspected to be continuous but sparsely sampled, the output volume is expanded to a minimum of 0.1 meters throughout. The continuity and clipping parameter is automatically calculated.

The output volume is used for downstream model sub-celling so is set to a high resolution.

Unless otherwise specified, default parameter values are used.

Finally, the output object is saved to disk as a wireframe pair file.
    
    
    var oDmApp=window.external;  
  
---  
      
    
    var objHoles=mApp.ActiveProject.Data.LoadFile("C:\\Database\\MyProjectFolder\\Holes.dm")  
      
    
    var vDrillholes = "Holes (drillholes);";  
      
    
    var vUseUncertainty = "yes;"  
      
    
    var vFaults = "Fault_Sheet_Flattr/fault_sheet_flatpt   
      
    
         (wireframe);"  
      
    
    var vFaultIDCol = "COLOUR"  
      
    
    var vFieldName = "Fieldname=NLITH;";  
      
    
    var vValue = "Value=3;";  
      
    
    var vPinchOut = "no";  
      
    
    var vClipType = "AlphaShape";  
      
    
    var vClipRadius = 25;  
      
    
    var vThickness = 0.1;  
      
    
    var vOutput = "vein_from_samples_007";  
      
    
    var vSurfaceType = 2;  
      
    
    var Res = "High"  
      
    
    var vRemoveBelow = "no"; //Use Expand   
      
    
         to option  
      
    
    var vCommand = "vein-from-samples "   
      
    
         + vDrillholes + vFieldName + vValue + vUncertainty;  
      
    
    var vExtras = ";MinimumThickness="+   
      
    
         vThickness +  
      
    
        "; RemoveBelow="+vRemoveBelow   
      
    
         +  
      
    
        "; UseUncertainty="+vUseUncertainty   
      
    
         +  
      
    
        "; UseCurrentSection="+vUseCurrentSection   
      
    
         +  
      
    
        "; OutputVeinFile="+   
      
    
         vOutput +  
      
    
        "; SurfaceType="   
      
    
         + vSurfaceType +  
      
    
        "; ClippingType="   
      
    
         + vClipType +  
      
    
        "; ClippingParameter="   
      
    
         + vClipRadius +  
      
    
        "; PinchOut="   
      
    
         + vPinchOut +   
      
    
        "; FaultObject="   
      
    
         + vFaults +  
      
    
        "; FaultIDColumn="   
      
    
         + vFaultIDCol +  
      
    
        "; PinchOut="   
      
    
         + vPinchOut +   
      
    
        "; Resolution="   
      
    
         + Res +  
      
    
        "; SuppressOutput="   
      
    
         + "yes" +  
      
    
        ";"  
      
    
    oDmApp.ParseCommand(vCommand+vExtras);  
      
    
    var saveobj = oDmApp.ActiveProject.Data.IsLoaded(vOutput);  
      
    
    saveobj.SaveAsDatamineFile(vOutput, oDmApp.ActiveProject.ExtendedPrecision,   
      
    
         true, ""); //save to physical file   
  
## Parameter Sensitivity Test Example

The next example tests the input samples' sensitivity to increasing continuity. The script outputs 10 volumes, with increasing continuity values. As a continuity test, UseUncertainty is set to "yes" to ensure a Gaussian calculation is performed (continuity is not relevant for Minimum Curvature calculations.

This script could easily be adapted to generate outputs for a range of parameter settings or, with nest for-next loops, a 2- or even 3-dimensional matrix of outputs (although be wary of the number of outputs you are creating):
    
    
    var oDmApp=window.external;  
  
---  
      
    
    var objHoles=mApp.ActiveProject.Data.LoadFile("C:\\Database\\MyProjectFolder\\Holes.dm")  
      
    
    var vDrillholes = "Holes (drillholes);";  
      
    
    var vFieldName = "Fieldname=NLITH;";  
      
    
    var vValue = "Value=3;";  
      
    
    for (i = 20; i <= 30; i++) {  
      
    
      var vPinchOut = "no";  
      
    
      var vClipType = "AlphaShape";  
      
    
      var vUseUncertainty = "yes;"  
      
    
      var vContinuity = i;  
      
    
      var vClipRadius = 25;  
      
    
      var vThickness = 0.1;  
      
    
      var vOutput = "vein_from_samples_007";  
      
    
      var vSurfaceType = 2;  
      
    
      var Res = "High"  
      
    
      var vCommand = "vein-from-samples   
      
    
         " + vDrillholes + vFieldName + vValue + vUncertainty;  
      
    
      var vExtras = "Continuity="   
      
    
         + vContinuity +   
      
    
        "; MinimumThickness="+   
      
    
         vThickness +  
      
    
        "; UseUncertainty="+vUseUncertainty   
      
    
         +  
      
    
        "; OutputVeinFile="+   
      
    
         vOutput +  
      
    
        "; SurfaceType="   
      
    
         + vSurfaceType +  
      
    
        "; ClippingType="   
      
    
         + vClipType +  
      
    
        "; ClippingParameter="   
      
    
         + vClipRadius +  
      
    
        "; PinchOut="   
      
    
         + vPinchOut +   
      
    
        "; Resolution="   
      
    
         + Res +  
      
    
        ";"  
      
    
       oDmApp.ParseCommand(vCommand+vExtras);  
      
    
       var saveobj = oDmApp.ActiveProject.Data.IsLoaded(vOutput   
      
    
         + "_" + i);  
      
    
      saveobj.SaveAsDatamineFile(vOutput,   
      
    
         oDmApp.ActiveProject.ExtendedPrecision, true, ""); //save   
      
    
         to physical file  
      
    
    }  
      
    
       
  
Related topics and activities

  * [vein-from-samples ](<../command_help/vein-from-samples.md>)(command)

  * [Vein Modelling](<Create_Vein_Surfaces_Overview.md>)

  * [Automating Studio Products](<concept_studio%203%20scripting%20overview.md>)

  * [Scripting Overview](<concept_studio%203%20scripting%20overview.md>)