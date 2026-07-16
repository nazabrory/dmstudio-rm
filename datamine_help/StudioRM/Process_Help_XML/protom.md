# PROTOM Process  
  
To access this process:

  * **Model** ribbon **> > Create >> Auto Prototype >> Prototype**.

  * Enter "PROTOM" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **PROTOM** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_P.md#PROTOM>).

## Process Overview

This process creates a block model data definition, also known as a 'prototype'.

Default values are set up by the process, based on the user's response to a series of interactive prompts. The prototype model is created in the form required by all of the orebody modeling processes.

By default the prototype model is defined orthogonal to the world coordinate system. However the parameter @ROTMOD allows a local coordinate system to be defined which can include both an origin translation and up to three rotations. The method for defining the translation and rotations is consistent with the **[CDTRAN](<cdtran.md>)** process.

**Note** : You can also create a prototype model using the [Create Model Prototype](<../COMMON/CreateModelPrototype_Dialog.md>) screen.

### Interactive Prompts

**PROTOM** , if run interactively, requires additional information to be provided using the Command toolbar.

The first two interactive prompts are independent of the value of @ROTMOD:
    
    
    >>>> IS A MINED-OUT FIELD REQUIRED? Y/(N) >

Y to include a field MINED in the output prototype.
    
    
    >>>> ARE SUBCELLS TO BE USED? Y/(N) >

Y to allow the model to include sub-cells.

If **ROTMOD** =0, you are prompted to enter the coordinates of the model origin
    
    
    >>>>     PLEASE SUPPLY CO-ORDINATES OF MODEL ORIGIN
    
    
    X >     X Co-ordinate.
    
    
    Y >     Y coordinate.
    
    
    Z >     Z coordinate.

If **ROTMOD** =1, you prompted to enter the model origin in both the world and local coordinate systems:
    
    
    >>>> PLEASE SUPPLY COORDINATES OF MODEL ORIGIN IN THE WORLD COORDINATE SYSTEM.>>>
    
    
    X0 >     X coordinate
    
    
    Y0 >     Y coordinate
    
    
    Z0 >     Z coordinate
    
    
    >>>> NOW ENTER THE SAME MODEL ORIGIN POINT SPECIFIED IN THE LOCAL COORDINATE SYSTEM.>>>
    
    
    X >     X coordinate
    
    
    Y >     Y coordinate
    
    
    Z >     Z coordinate

If **ROTMOD** =1 , you are prompted to enter the three rotation axes and corresponding rotation angles. The three axes X,Y and Z are denoted as axes 1,2 and 3 respectively. A rotation about angle 'N' is measured positively in the clockwise direction when viewed along axis N from high values to low values. For example a rotation of 35 degrees about axis 1 represents a dip of 35 degrees downwards from the horizontal plane. The first rotation angle must be 1,2 or 3. If only one rotation is required then the second and third rotation axes should be defined as zero.
    
    
    >>> NOW ENTER THE MODEL ROTATION ANGLES >>>
    
    
    ROTATION 1: ANGLE (-360 TO +360) >

First rotation angle.
    
    
    AXIS (1, 2 OR 3) >

Axis about which first rotation is applied.
    
    
    ROTATION 2: ANGLE (-360 TO +360) >

Second rotation angle.
    
    
    AXIS (0,1,2 OR 3) >

Axis about which second rotation is applied.
    
    
    ROTATION 3: ANGLE (-360 TO +360) >

Third rotation angle.
    
    
    AXIS (0,1,2 OR 3) >

Axis about which third rotation is applied.

Whatever the value of ROTMOD the user is finally prompted for the cell dimensions and the number of cells:
    
    
    >>> PLEASE SUPPLY CELL DIMENSIONS
    
    
    X >     Cell dimension in X.
    
    
    Y >     Cell dimension in Y.
    
    
    Z >     Cell dimension in Z.
    
    
    >>>> NUMBER OF CELLS IN EACH DIRECTION
    
    
    X >     Number of cells in X.
    
    
    Y >     Number of cells in Y.
    
    
    Z >     Number of cells in Z.

## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Block Model Prototype |  Output prototype model file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
ROTMOD |  Select 1 to generate a prototype for a rotated block model, or 0 (zero, the default) for a non-rotated prototype. |  No |  0 |  0,1 |  0,1  
  
Related topics and activities

  * [Create Model Prototype](<../COMMON/CreateModelPrototype_Dialog.md>)

  * [CDTRAN Process](<cdtran.md>)