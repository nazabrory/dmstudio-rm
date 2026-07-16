# Create Isoshells: Automation

The Create Isoshells tool can be automated using a script.

As with most commands available via Studio's COM interface, access is granted using the ParseCommand() method, and passing in parameters to define the behavior. **ParseCommand** parameters use a method of name and value pairs which is similar to those used for some other processes in Studio products:

  * Parameters must be separated by semicolons.
  * All filenames must refer to files which are already in the project \- if this is not the case, errors are displayed.
  * If no bounding box value is supplied, the bonding box is calculated automatically from the input data and boundaries.
  * If any bounding box value is supplied, all values must be defined.
  * If _TriSpacing_ is not defined, it is automatically calculated from the bounding box.

## Parameters List  

Parameter |  Notes  
---|---  
      
    
    SampleFile=filename

|  filename = dm sample file name  
      
    
    SampleXField=fieldname

|  fieldname = field name for X coordinate  
      
    
    SampleYField=fieldname

|  fieldname = field name for Y coordinate  
      
    
    SampleZField=fieldname

|  fieldname = field name for Z coordinate  
      
    
    SampleValueField=fieldname

|  fieldname = field name for values  
      
    
    SampleWeightingField=fieldname

|  fieldname = field name for weighting (optional)  
      
    
    Mode=category | continuous

|  (default=continuous)  
      
    
    Isolevel=value

|  value can be text or a number (depending on type of SampleValueField)  
Can be repeated for multiple isovalues  
      
    
    BottomCut=number

|  no bottom cut if not defined  
      
    
    TopCut=number

|  no top cut if not defined  
      
    
    Distribution=none | log | normal

|  (default=none)  
      
    
    XRadius=number

|  (default=100)  
      
    
    YRadius=number

|  (default=100)  
      
    
    ZRadius=number

|  (default=100)  
      
    
    RotAxis1=1 | 2 | 3

|  1=X, 2=Y, 3=Z  
      
    
    RotAxis2=1 | 2 | 3

|  1=X, 2=Y, 3=Z  
      
    
    RotAxis3=1 | 2 | 3

|  1=X, 2=Y, 3=Z  
      
    
    RotAngle1=number

|  number is rotation in degrees around the related axis (default=0)  
      
    
    RotAngle2=number

|  number is rotation in degrees around the related axis (default=0)  
      
    
    RotAngle3=number

|  number is rotation in degrees around the related axis (default=0)  
      
    
    IDWPower=number

|  (default=2)  
      
    
    EstimationMethod=ok | idw

|  (default=idw)  
      
    
    AlignEllipse=yes | no

|  (default=yes)  
      
    
    InsideWireframeFile=filename

|  filename = dm wf file name (optional)  
      
    
    AboveWireframeFile=filename

|  filename = dm wf file name (optional)  
      
    
    BelowWireframeFile=filename

|  filename = dm wf file name (optional)  
      
    
    PerimeterFile=filename

|  filename = dm str filename (optional)  
      
    
    UseSelectedPerimeter=yes | no

|  (default=no)  
      
    
    XMin=number

|  Minimum value in X of bounding box *  
      
    
    YMin=number

|  Minimum value in Y of bounding box *  
      
    
    ZMin=number

|  Minimum value in Z of bounding box *  
      
    
    XMax=number

|  Maximum value in X of bounding box *  
      
    
    YMax=number

|  Maximum value in Y of bounding box *  
      
    
    ZMax=number

|  Maximum value in Z of bounding box *  
      
    
    XOrigin=number

|  Local origin or bounding box in X **  
      
    
    YOrigin=number

|  Local origin or bounding box in Y **  
      
    
    ZOrigin=number

|  Local origin or bounding box in Z **  
      
    
    XLength=number

|  Length of bounding box along X axis **  
      
    
    YLength=number

|  Length of bounding box along Y axis **  
      
    
    ZLength=number

|  Length of bounding box along Z axis **  
      
    
    OutputName=text

|  (default=Isosurface)  
      
    
    TriSpacing=number

|  (default=autocalculated)  
      
    
    DifferentObjects=yes | no

|  (default=yes)  
      
    
    IncludeBoundary=yes | no

|  (default=yes)  
      
    
    Smooth=integer number

|  1=Low, 2=Medium, 3=High (default=0)  
  
* Only used where AlignEllipse=yes.

** Only used where AlignEllipse=no.

## Example
    
    
    oDmApp.ParseCommand("create-shells SampleFile=_vb_holes; SampleXField=X; SampleYField=Y; SampleZField=Z; SampleValueField=AU; Isolevel=0.5; TriSpacing=25; XRadius=15; YRadius=15; ZRadius=15 ");

Related topics and activities

  * [Create Isoshells](<Create_Isoshells.md>)

  * [Create Isoshells - Input](<CreateIsoshells_Input.md>)

  * [Create Isoshells - Condition](<CreateIsoshells_Condition.md>)

  * [Create Isoshells - Estimation Parameters](<CreateIsoshells_EstParams.md>)

  * [Create Isoshells - Volume](<CreateIsoshells_Vol.md>)

  * [Create Isoshells - Output](<CreateIsoshells_Output.md>)

  * [Isoshells Report](<CreateIsoshells_IsoShellsRep.md>)