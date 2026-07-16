# BOOLEAN Process  
  
To access this process:

  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **BOOLEAN** and click **Run**.
  * Enter "BOOLEAN" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/commandtable_B.md#BOOLEAN>).

## Process Overview

The **BOOLEAN** process is used to apply boolean operations to one or more wireframe data file pairs. As a process, data is processed according to physical file contents, not objects in memory. This differs from the [boolean command that work on objects](<../COMMON/boolean_operations.md>).

**BOOLEAN** is used to apply one of the following boolean operations on input wireframe(s). 

  1. Union \- Takes two wireframes and creates a single wireframe with the same surface appearance and volume of both wireframes. Also, see the help file for the [wireframe-union](<../COMMON/Wireframe%20Union%20Dialog.md>) interactive command screen. * **OUTTR** and * **OUTPT** will be generated with this method.
  2. Difference \- Takes the difference of the second from the first wireframe by removing the first volume that is common to the second. The results will differ if the first and second wireframe are swapped. Also, see the help file for the [wireframe-difference](<../COMMON/Wireframe%20Difference%20Dialog.md>) interactive command screen. * **OUTTR** and * **OUTPT** will be generated with this method.
  3. Intersection \- Takes two wireframes and creates a single wireframe output of their overlapping (common) volume. Also, see the help file for the [wireframe-intersection](<../COMMON/Wireframe%20Intersection%20Dialog.md>) interactive command screen. * **OUTTR** and * **OUTPT** will be generated with this method.
  4. Extract Separate \- Takes two wireframes and creates discrete pieces of a two wireframe intersection. The parameters **WIRE1IN** , **WIRE1ON** , **WIRE1OUT** , **WIRE2IN** , **WIRE2ON** , **WIRE2OUT** indicate which outputs are created. Also, see the help file for the [wireframe-extract-separate](<../command_help/wireframe-extract-separate.md>) interactive command dialog. * **OUTTR** and * **OUTPT** will be generated with this method.
  5. Strings from Intersection \- Takes two wireframes and creates a string outlines where the surfaces intercept. Also, see the help file for the[ wf-intersections](<../command_help/wf-intersections.md>) interactive command screen. * **OUTSTR** will be generated with this method.
  6. Solid Hull \- Creates a single shell around multiple overlapping surfaces. The option only uses the first wireframe input (* **WIRE1TR** , * **WIRE1PT**). Also, see the help file for the [convert-wf-hull](<../COMMON/Wireframe%20Solid%20Hull%20Dialog.md>) interactive command screen. * **OUTTR** and * **OUTPT** will be generated with this method.

Methods 1,2,3,4 and 5 require two independent wireframe pair files to be specified. Method 6 only requires the first wireframe pair to be specified.

Methods 1,2,3,4 and 6 will output a single wireframe data file. Method 5 will output a string file.

You can optionally control which elements of an output wireframe are generated as a result of the operations above. By default, the full collection of data resulting from the boolean calculation will be generated with methods 1,2,3,4 and 6 (5 will always output a complete string file representing the intersection of two wireframes). The Parameters tab contains parameters, in addition to @**METHOD** to allow various elements of the output data to be enabled or disabled using 0 or 1.

#### @USENORM

Determining the 'inside' or 'outside' of input wireframes, in most cases, is simple to calculate. However, where more complex interactions between wireframes occur, the definition of in and out can be ambiguous. To support the most appropriate output for these situations, @USENORM can be used to determine if input wireframe normal directions should be calculated and used to determine the inside/outside categorization. Whilst this option, if enabled, is computationally more expensive, it can help to alleviate the incorrect categorization of output elements.

## Example

For example, if you wanted to display the intersection of two overlapping wireframe volumes, but you only wanted to produce the intersecting data originally belonging ,to * **WIRE1IN** (and not * **WIRE2IN**), and not any coincident data, you would set @**METHOD** =4 and the following remaining parameters:

  * @**WIRE1IN** =1
  * @**WIRE1ON** =0
  * @**WIRE1OUT** =1 (not relevant to the intersection method)
  * @**WIRE2IN** =0
  * @**WIRE2ON** =0
  * @**WIRE2OUT** =1 (not relevant to the intersection method)

The ...**IN** /**ON** /**OUT** parameters are only applicable where @**METHOD** =4. The Strings from Intersection method (@**METHOD** =5), by comparison, ignores all parameters other than @**METHOD**.

**Note** : This process supports **[retrieval criteria](<../COMMON/Retrieval_Criteria_Overview.md>)**.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRE1TR |  First input wireframe triangle file. |  Input |  Yes |  Wireframe triangle file.  
WIRE1PT |  First input wireframe points file. |  Input |  Yes |  Wireframe points file.  
WIRE2TR | Second input wireframe triangle file. This is only used where METHOD=1,2,3,4,5.  |  Input |  No |  Wireframe triangle file  
WIRE2PT |  Second input wireframe points file. |  Input |  No |  Wireframe points file.  
  
## Output Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
OUTTR |  Output wireframe triangle file. This is only used where METHOD=1,2,3,4,6. | Output |  No |  Wireframe triangles file.  
OUTPT | Output wireframe points file. This is only used where METHOD=1,2,3,4,6. | Output |  No |  Wireframe points file.  
OUTSTR | Output string file. This is only used where METHOD=5. | Output |  No |  String file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
METHOD |  Parameter to define the boolean operation run on the input wireframe(s). =1 : Union - Takes two wireframes and creates a single wireframe with the same surface appearance and volume of both wireframes. =2 : Difference - Takes the difference of the second from the first wireframe by removing the first volume that is common to the second. The results will differ if the first and second wireframe are swapped. =3 : Intersection - Takes two wireframes and creates a single wireframe output of their overlapping (common) volume.  =4 : Extract Separate - Takes two wireframes and creates discrete pieces of a two wireframe intersection. The parameters WIRE1IN, WIRE1ON, WIRE1OUT, WIRE2IN, WIRE2ON, WIRE2OUT, USENORM indicate which outputs are created. =5 : Strings from Intersection - Takes two wireframes and creates a string outlines where the surfaces intercept..  =6 : Solid Hull - Creates a single shell around multiple overlapping surfaces. The option only uses the first wireframe input..  |  Yes |  1 |  1,5 | 1,2,3,4,5  
WIRE1IN |  The first wireframe inside the second wireframe: the output includes elements from the first wireframe which fall inside (or below for a DTM) the second wireframe.  =0 : false.  =1 : true.  |  No |  1 |  0,1 |  0,1  
WIRE1OUT |  The first wireframe on the second wireframe: the output includes elements from the first wireframe which fall directly on the surface of the second wireframe.  =0 : false.  =1 : true. |  No |  1 |  0,1 |  0,1  
WIRE2IN |  The second wireframe inside the first wireframe: the output includes elements from the second wireframe which fall inside (or below for a DTM) the first wireframe. =0 : false. =1 : true. |  No |  1 |  0,1 |  0,1  
WIRE2ON |  The second wireframe on the first wireframe: the output includes elements from the second wireframe which fall directly on the surface of the first wireframe.  =0 : false.  =1 : true.  |  No |  1 |  0,1 |  0,1  
WIRE2OUT |  The second wireframe outside the first wireframe: the output includes elements from the second wireframe which fall outside (or above for a DTM) the first wireframe.  =0 : false.  =1 : true.  |  No |  1 |  0,1 |  0,1  
USENORM |  Use wireframe face normals to determine which elements the output should contain.  =0 : false.  =1 : true.  |  No |  0 |  0,1 |  0,1  
  
## Example
    
    
    !START M1        
  
---  
      
    
    # - Use !LOCDBOFF to look for files outside the local   
      
    
     folder   
      
    
    # - Use local files by deleting the next line or use   
      
    
     !LOCDBON  
      
    
    !LOCDBOFF  
      
    
    !BOOLEAN  &WIRE1TR(green_pyr_tr),  
      
    
              &WIRE1PT(green_pyr_pt),  
      
    
              &WIRE2TR(red_cube_tr),  
      
    
              &WIRE2PT(red_cube_pt),  
      
    
              &OUTTR(BooleanTR),  
      
    
              &OUTPT(BooleanPT),  
      
    
              &OUTSTR(BooleanSTR),@METHOD=1.0,@WIRE1IN=1.0,@WIRE1ON=1.0,  
      
    
              @WIRE1OUT=1.0,@WIRE2IN=1.0,@WIRE2ON=1.0,@WIRE2OUT=1.0  
      
    
    !END  
  
Related topics and activities

  * [Boolean operations](<../COMMON/boolean_operations.md>)

  * [Wireframe Difference](<../COMMON/Wireframe%20Difference%20Dialog.md>)

  * [Wireframe Union](<../COMMON/Wireframe%20Union%20Dialog.md>)

  * [Wireframe Extract Separate](<../COMMON/Wireframe%20Extract%20Separate%20Dialog.md>)

  * [Wireframe Intersection](<../COMMON/Wireframe%20Intersection%20Dialog.md>)

  * [Wireframe Solid Hull](<../COMMON/Wireframe%20Solid%20Hull%20Dialog.md>)

  * [Wireframe Strings From Intersections](<../COMMON/Wireframe%20Strings%20From%20Intersections%20Dialog.md>)