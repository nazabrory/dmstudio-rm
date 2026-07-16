# Categorical Surfaces & Grade Shells Automation

**Note** : this topic is aimed at users familiar with COM-aware scripting languages, and the [create-categorical surface](<../command_help/create-categorical-surfaces.md>)s and [create-grade-shells](<../command_help/create-grade-shells.md>) commands. For an overview of scripting in this product, please refer to your scripting tutorial.

The create-categorical-surfaces and create-grade-shells commands feature a rich COM interface that allows virtually all of the interactive options of implicit modelling to be accessed from a script.

As with many scriptable commands in Studio products, you can access vein-from-samples using the ParseCommand() method, followed by a series of parameters that control the output.

Scripted Command Setup

As with the interactive usage of the command, data must be loaded into memory before it can be accessed by the vein-from-samples command. Once a **DmApplication** object has been instantied (for example using "window.external;"), there are multiple ways to load data, including the LoadFile() and LoadFromProject() methods, for example:  

    
    
    var objHoles = oDmApp.ActiveProject.Data.LoadFile("C:\\Database\\Drillholes.dm")
    
    
     
    
    
    var objHoles = oDmApp.ActiveProject.Data.LoadFromProject("Drillholes")  
    

Also note:

  * Parameters set by script will not be reinstated to the user interface when subsequently using the command interactively.
  * Where field values are specified by script, the current [long field name settings](<../COMMON/Long_Field_Mode.md>) for your system will be honoured; attribute names will be restricted to either 8 or 24 characters depending on the current setting.

## Command Syntax

The general syntax for automating either command is:
    
    
    create-categorical-surfaces (or create-grade-shells)[Drillhole Object] [Field Name] [Field Value] [Global Uncertainty (optional)] [Output File Definition] | [Ellipsoids Object] (optional) | [Other Parameters]

Where:

[Drillhole Object] is a mandatory parameter and is a fully-qualified object name as it appears in the Sheets control bar, for example:
    
    
    "Drillholes=MyHoles (drillholes);"

[Field Name] is a mandatory parameter and is the name of the attribute containing the value to be modelled, for example:
    
    
    "Fieldname=ROCK"

[Field Value] is a mandatory parameter and is either the categorical value you wish to model (create-categorical-surfaces) or the cut-off grade value to be used to model grade shells (create-grade-shells), for example:
    
    
    "Value=LODE"
    
    
     
    
    
    "Value=4.1"

[Global Uncertainty] is an optional parameter and is the default uncertainty value to be applied if a more specific (table-based) uncertainty value does not exist, or is not specified, for example:
    
    
    "DefaultUncertainty=0.05;"

[Output File Definition] defines the output object name for the calculated volume, for example:
    
    
    "OutputFile=MyOutputObject;"

[Other Parameters] is a semi-colon-separated string of parameters, all of which are optional, used to control how a volume is generated. If no parameter value is listed, the default value will be used, for example:
    
    
    "GridSize=3;PercentageExtra=40;AutoRadius=true;Intervals=True;TrendType=1;UncertaintyColumn=UNCERT;"  
    

## Command Parameters

The parameter string for vein-from-samples can contain any of the following items. All parameters must be separated by a semi-colon (;). No parameters are mandatory as default values will be used if any are absent. 

Any data objects referenced within parameters must exist in memory before the command is called from script.

Parameter| Description| Default | Example  
---|---|---|---  
Data Context  
Drillholes (Mandatory)| References the loaded drillholes object.| null| "Drillholes=MyHoles (drillholes);"  
FieldName (Mandatory)| The attribute containing the value to be modelled| null| "Fieldname=ROCK;"  
Value  
(Mandatory)| The attribute value to be modelled, either a categorical value (create-categorical-surfaces) or a numeric cut-off value (create-grade-shells). | null| "Value=LODE;""Value=1.6;"  
OutputFile| The name of the wireframe object to be created.| null| "OutputFile=MyOutputObject;"  
SuppressOutput| Whether to disable the printing of a summary report to the output window when running the command.| no| "SuppressOutput=yes;"  
DefaultUncertainty| A numeric uncertainty value to be used if UncertaintyColumn is not specified, or it is specified and the value for a record is absent.| 0| "DefaultUncertainty=0.05;"  
UncertaintyColumn| A numeric attribute in Drillholes containing per-record uncertainty values.| None - global or zero uncertainty will be used| "UncertaintyColumn=UNCERT;"  
IgnoreAbsents| Defines if absent data is to be included in processing.

  * If set to no, absent data values are treated as negative sample data when modelling an output volume.
  * If set to yes, absent data values detected in the selected Column will be ignored.

Essentially, yes will only constrain the surface with samples that contain non-selected values. No will constrain the surface with any other samples (absent and non-selected values). | yes| "IgnoreAbsents=no;"  
Create Trends  
TrendType| Can be either 0 or 1. If 0, a single (default) automatically-calculated ellipsoid will be used to generate the output volume. If 1, an input ellipsoids object name is used (and makes the EllipsoidObject parameter mandatory)| 0| "TrendType=1;"  
EllipsoidObject| Required if TrendType is 1, this is the name of a loaded ellipsoids object (not a visualization ellipsoid).| 0| "EllipsoidObject=MyEllipsoids;"  
PreviewGridMode| Controls how/if a trend preview grid is generated as part of surface generation. By default, no preview ellipsoid grid will be generated (0)

  * If set to zero (0), no preview grid will be generated. Only the modelled surface will be generated and displayed Default.
  * If set to 1, only the preview grid will be displayed, no surface.
  * If set to 2, both preview grid and surface will be generate and displayed.

If a preview grid is displayed, it will be generated at the resolution determined by PreviewGridResolution (see below).| 0 (zero)| "PreviewGridMode=2; PreviewGridResolution=3;"  
PreviewGridResolution| If PreviewGridMode (see above) is either 1 or 2, this parameter determines the resolution of the ellipsoid grid. The integer passed represents the number of ellipsoid in any grid axis. The default is 3 (3 x 3 x 3 grid)| 3| "PreviewGridMode=2; PreviewGridResolution=3;"  
Surface Generation Controls  
CompositingLength| Choose the frequency and resolution of ellipsoid locations to be used during surface calculation.If set to zero, or not specified, automatic compositing will be applied, based on the structure and relative layout of input data, otherwise a non-zero and non-negative numeric value should be specified to define the compositing length.| Automatic| "CompositingLength=5;"  
GridSize| Sets the Resolution of the 3D grid used to construct the output object. A numeric value, which will be used for all axes of the points grid.

  * 80 is the same as [Very low]
  * 120 is the same as [Low]
  * 160 is the same as [Medium]
  * 200 is the same as [High]
  * 240 is the same as [Very High]

Higher values can lead to increased processing times. Try lower values first for initial studies.| 80| "GridSize=80;"  
PercentageExtra| A value specifying the size of the bounding box with respect to the input points, where zero represents a cuboid hull that intercepts the data limits. Generally, a bounding cuboid that is larger than the hull of the input positive samples is required.| 40| "PercentageExtra=20;"  
CapTop| If this is **yes** then the surface will pass close to the start of the drillhole if the drillhole begins within the solid being modelled.If this is **no** , surface generation will not be constrained to the start of the drillhole.| no| "CapTop=yes;"  
CapBottom| If this is **yes** then the surface will pass close to the end of the drillhole if the drillhole begins within the solid being modelled.If this is **no** , surface generation will not be constrained to the end of the drillhole.| no| "CapBottom=no;"  
SnapEnable| If set to **true** , a post-processing step is performed after surface generation to attempt to create a tighter fit between the surface and intercept positions. Processing will take longer.If set to **false** , no post-processing is performed.| false| "SnapEnable=true;"  
SnapIgnoreDistance| The maximum contact snapping distance. Any contact points whose distance to the undeformed surface exceeds this value will be ignored by the snapping routine.| 10| "SnapIgnoreDistance=10;"  
SnapPatchSize| The fixed patch size for the contact snapping routine. When patching the surface to snap to contacts, this is the width of the patches measured along the surface and will be the same for all contacts.The default value of **0** means dynamic patch size is used instead.| 0 (Dynamic patch size)| "SnapPatchSize=10;"  
SnapAutoScaleFactor| The dynamic patch size scale factor. This is only used if "SnapPatchSize" is not specified or set to **0**.When using dynamic patch size, the size of the patches is determined as a multiple of the distance between the contact point and the undeformed surface. This means contact points that are further away will result in larger patches. 

  * 1 is the same as [Low]
  * 10 is the same as [Medium]
  * 100 is the same as [High]

| 10| "SnapAutoScaleFactor=10;"  
  
##  Examples 

### Create-categorical-surfaces

In the following example, a file called "holes.dm" is loaded from the project directory and referenced as a loaded object. The value ZONE=2 is being modelled.

A custom ellipsoids object is loaded, with the ellipsoids being automatically scaled according to the distance between samples (Auto radius). An uncertainty value of 0.01 is used throughout and no uncertainty column is set.

Finally, the output object is saved to disk as a wireframe pair file.
    
    
    var oDmApp=window.external;  
  
---  
      
    
    var objHoles=mApp.ActiveProject.Data.LoadFile("C:\\Database\\MyProjectFolder\\Holes.dm")  
      
    
    var vFieldName = "Fieldname=ZONE;";  
      
    
    var vValue = "Value=2;";  
      
    
    var vUncertainty = 0.01  
      
    
    var vOutput = "categorical_output;";  
      
    
    var vGridSize = 150  
      
    
    var sEllipsoidsObject = "MyLoadedEllipsoids;";  
      
    
    var vExtras = "AutoRadius=true;Intervals=false;TrendType=1;"  
      
    
    var vCommand = "create-categorical-surfaces " + objHoles + vFieldName + vValue + Uncertainty + vOutput +    
      
    
    sEllipsoidsObject;  
      
    
    oDmApp.ParseCommand(vCommand+vExtras);  
      
    
    var saveobj = oDmApp.ActiveProject.Data.IsLoaded(vOutput);  
      
    
    saveobj.SaveAsDatamineFile(vOutput, oDmApp.ActiveProject.ExtendedPrecision,   
      
    
    true, ""); //save to physical file   
  
### Create-grade-shells

The next example is similar, but uses the same input holes object as above to model grade shells representing a CU cutoff of 6.5:
    
    
    var oDmApp=window.external;  
  
---  
      
    
    var objHoles=mApp.ActiveProject.Data.LoadFile("C:\\Database\\MyProjectFolder\\Holes.dm")  
      
    
    var vDrillholes = "Holes (drillholes);";  
      
    
    var vFieldName = "Fieldname=CU;";  
      
    
    var vValue = "Value=6.5;";  
      
    
    var vUncertainty = 0.01  
      
    
    var vOutput = "grade_shell_output;";  
      
    
    var vGridSize = 150  
      
    
    var sEllipsoidsObject = "MyLoadedEllipsoids;";  
      
    
    var vExtras = "AutoRadius=true;Intervals=false;TrendType=1;CapTop=yes;CapBottom=no;SnapEnable=true;"  
      
    
    var vCommand = "create-categorical-surfaces " + objHoles + vFieldName + vValue + Uncertainty + vOutput +   
      
    
    sEllipsoidsObject;  
      
    
    oDmApp.ParseCommand(vCommand+vExtras);  
      
    
    var saveobj = oDmApp.ActiveProject.Data.IsLoaded(vOutput);  
      
    
    saveobj.SaveAsDatamineFile(vOutput, oDmApp.ActiveProject.ExtendedPrecision,   
      
    
    true, ""); //save to physical file   
      
    
       
  
Related topics and activities

  * [Categorical Modelling](<Implicit_Surface_From_Drillholes_Categorical.md>)

  * [Grade Shell Modelling](<Implicit_Surface_From_Drillholes_Continuous.md>)

  * [create-categorical-surfaces](<../command_help/create-categorical-surfaces.md>)

  * [create-grade-shells](<../command_help/create-grade-shells.md>)

  * [Create Vein Surfaces](<../COMMON/Create_Vein_Surfaces_Overview.md>)

  * [vein-from-samples](<../command_help/vein-from-samples.md>)