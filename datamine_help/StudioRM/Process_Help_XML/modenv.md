# MODENV Process

To access this process:

  * **Report** ribbon **> > Model Reserves >> Mineable Reserves**.

  * Enter "MODENV" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press ENTER.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MODENV** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MODENV>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

The **MODENV** process analyses a block model and flags those blocks that when taken individually or with adjacent blocks satisfy the grade or economic value criteria within a volume defined by the minimum mining unit (MMU) dimensions.

The tailored interface for this process is called the **Mineable Reserves Optimizer** (MRO)

For the underground situation the MMU is the minimum stope size and for the open pit case it will be a selective mining unit. 

The process will locate envelopes of economic mining units and provide a first pass evaluation of that portion of a geological model that would be economically mineable. No detailed consideration is given to the mine development required for access, ore haulage or support. 

The process provides a result analogous to the floating cone method of pit optimization in open pit mine planning. It was designated the 'floating stope' method when first implemented in the **STPMOD** process as it was initially used for underground optimization. However the method has since been extended to include the open pit case as well. The effect of different MMU dimensions and cutoffs can be evaluated with multiple runs.

The input to **MODENV** includes many files, fields and parameters, and so a set of tailored dialogs is avaiable to facilitate data entry and allow multiple options for analysing the results. . The description below is for the **MODENV** process run using the standard Files, Fields, Parameters dialog. The **MODENV** process can also be included in macros and scripts.

Note: The [ENVSEQ](<envseq.md>) process takes the envelope output model from **MODENV** and evaluates design alternatives and the economics of sequential development of envelopes. This is another feature of MRO.

**Note** : MRO has its own help file and associated tutorial. Click **?** on the MRO screen.

### Optimization Method

The shape of an MMU is defined by a set of 3D rectangular model cells (sub-MMUs) with all cells being the same size. The input geological model is reblocked onto the sub-MMU size and the MMU is moved over the reblocked model in sub-MMU increments so that all possible MMU locations are evaluated. Different algorithms (Maximum, Minimum, Ranked) are then available for defining whether an MMU is economic and will be included in a mineable envelope.

A sub-MMU may form part of multiple MMUs. The criteria for defining the optimal MMU position is selected using parameter @**OPTIMISE** which gives the following options: 

  1. Maximum ore tonnes (equivalent to minimum included waste or dilution). If several MMUs have the same tonnes, then the MMU with the maximum grade is preferred. 
  2. Maximum head grade for the MMU.
  3. Maximum contained metal for the MMU.
  4. Maximum accumulated value, where the supplied field is expressed in currency value, for example, $USD

For cases (1) - (3) a grade or equivalent grade for polymetallic deposits must be defined using field *GRADE. 

For case (4), the value field * **VALUE** should define the total cell value, to reflect mining and processing costs and the product value for the cell. Parameters @**DEFVALUE** , @**CUTOFF** and @**HDGRADE** must then be expressed as a value per unit volume. @**DEFVALUE** defines the default value for any unmodeled cell, and typically reflects the cost of mining a unit volume of waste. Both @**CUTOFF** and @**HDGRADE** parameters are normally set to zero to indicate that all blocks with a positive value are worth mining and any MMU with a positive value is acceptable for mining. Any density field or parameter supplied will be ignored and a density value of 1.0 is used internally within the process for volumetric calculations. The parameters @**MAXWASTE** and @**DILUTE** will still operate with 'waste' defined as blocks below the @**CUTOFF** parameter value. 

Both a grade (* **GRADE**) and a value (* **VALUE**) field can be used simultaneously. Both fields will be reported but the only one field will be optimized as defined by @**OPTIMISE**.

### MMU Shape and Orientation

The shape and orientation of the MMU can be specified by one of several methods, providing a progressive increase in flexibility. The four methods are: 

  1. Defined by a 3D rectangular shaped MMU which is orthogonal to the axes of the input model. The method allows the possible MMU positions to be specified by defining the MMU origin, maximum position, and MMU increment in each of the three coordinate axis directions. The parameters are: 

MMUSIZE[X|Y|Z] |  the dimensions of the MMU  
---|---  
MMUINC[X|Y|Z] |  the number of MMU increments within each MMU dimension  
MMUMIN[X|Y|Z] | the minimum coordinates (bottom left corner) for an MMU  
MMUMAX[X|Y|Z] |  the maximum coordinates (top right corner) for an MMU  
  2. The **MMUMIN** and **MMUMAX** parameters are optional. If they are not selected then the MMUMIN values are set equal to the origin of the input geological model and the **MMUMAX** to the coordinates of the top right corner of the model.

  3. The parameters limit an MMU to a rectangular shape moving on an orthogonal grid. The MMU moves in steps of **MMUSIZE** / **MMUINC** (the sub-MMU size) along each coordinate axis. The smaller the sub-MMU (ie the larger the **MMUINC**) the more positions will be sampled thus improving the approximation to a floating MMU to optimize the envelope location. However in general for each direction there is no point in making the sub-MMU size smaller than the size of the minimum subcell in the input model in that direction. The larger the **MMUINC** parameters, the longer the processing time.
  4. A non-rectangular shape can be generated by defining the MMU size in X and Y as a base dimension, and specifying a slope factor 1:n in each of the four horizontal orthogonal directions. Positive n implies an outward expansion and negative n an inward contraction. If all factors are positive and parameter **MMUSLOPI** =0 then the MMU represents an inverted truncated pyramid with a rectangular horizontal cross-section. If @**MMUSLOPI** =1 then the MMU will be a truncated cone shape with an elliptical horizontal cross-section. The required parameters are: 

MMUSIZE[X|Y] |  The base dimensions of the MMU in the XY plane  
---|---  
MMUINC[X|Y] |  The number of MMU increments within the base dimension  
MMUSIZE[Z] |  The height of the MMU  
MMUINC[Z] |  The number of MMU increments within the MMU height  
MMUMIN[X|Y|Z] |  The minimum coordinates (bottom left corner) for an MMU  
MMUMAX[X|Y|Z] |  The maximum coordinates (top right corner) for an MMU  
MMUSLOPE[N|S|E|W] |  MMU slope factor (1:n) in the N|S|E|W direction. The slope factor is a ratio of sub-MMUs extended horizontally to vertically ie 0.5 would be half a sub-MMU horizontally for each sub-MMU vertically. Note that this definition is the inverse of the normal slope definition but allows a vertical side to be expressed exactly as zero whereas the standard definition of slope would require an infinite value.   
MMUSLOPI |  Flag to specify whether the MMU slope factors are to be interpolated in plan.   
0= do not interpolate ie MMU is always rectangular in plan.   
1= interpolate. ie MMU is elliptical in plan.   
  5. The **MMUMIN** and **MMUMAX** parameters are compulsory. All six parameters (**MMUMIN**[X|Y|Z] and **MMUMAX**[X|Y|Z]) must be defined for this method to be applied. The parameters cannot be used if the input model is rotated.
  6. A rotation can be applied to methods 1 or 2 by including a definition for a Rotated Model as the MMU shape template model file. In these cases the limits of the MMUs are defined by the limits of the Rotated Model, and so the parameters **MMUMIN**[X|Y|Z] and **MMUMAX**[X|Y|Z] are not required. 

  7. User defined MMU shapes can be specified by providing an MMU shape template model file, &**SHAPE** , with cells supplied to model the MMU shape(s). None of the parameters **MMUSIZE**[X|Y|Z], **MMUMIN**[X|Y|Z], or **MMUMAX**[X|Y|Z] are required. As for methods 2 and 3 the limits of the MMUs are defined by the limits of the &**SHAPE** model file. The sub-MMU dimensions are calculated by dividing the parent cell size for &SHAPE by the MMU increment **MMUINC**[X|Y|Z]. The &**SHAPE** file may include both cells and subcells to define the MMU shape. If the dimensions of the subcells are not multiples of the sub-MMU size then all MMUs intersected by subcells will be used to define to shape. The actual location of the cells in the &SHAPE model is not important, only the relative position of the cells. The MMU shape will be floated to all possible positions within the model file unless restricted by the @**INMODEL** parameter.

If required the MMU shape template file can be a Rotated Model file to allow the MMU to float non-orthogonally to the block model axes. If a * **SHAPZONE** field is supplied in the input block model and in the MMU shape template file then different MMU shapes can be used in different mining areas. If not all values of the **SHAPZONE** field in the model have a corresponding shape definition in the &**SHAPE** file then the default MMU shape will be used. In the MMU shape template file the default shape will have a **SHAPZONE** value of blank for alphanumeric fields and - for numeric fields. Up to 50 zone values can be modeled. Where a block can be extracted by MMU shapes from different zones, the shape is selected by taking the MMU shape matching the block zone or else the MMU shape that would be least diluted by other material from other zones or the MMU with the greatest value as defined by the @**SHAPEMTH** parameter.

Important: In all four methods of MMU specification, the MMU increment must be supplied. If an MMU shape is specified in the MMU shape template file the correct cell or subcell size to match the MMU increment should be selected.

### Economic Parameters for MMUs

In addition to the geometric parameters defined in the previous section the following parameters are used to define an economic MMU.

Head Grade is the minimum grade of an economic MMU. It is defined either by the single parameter @**HDGRADE** or the input model file &IN can include field * **HDGRADE** , allowing the Head Grade to vary over the model volume.

Cutoff Grade differentiates between ore and waste and is defined by parameter @**CUTOFF**. It is used in the definition of a Minimum envelope as described below.

The maximum volume of waste (material below Cutoff) that can be included in an economic MMU is defined by the @**MAXWASTE** parameter. This is expressed as a proportion between 0 (no waste allowed) and 1 (any volume of waste allowed).

The @**DILUTE** parameter defines whether the grade of an MMU should be calculated as the average of all associated sub-MMUs (@**DILUTE** =1) or just the sub-MMUs above Cutoff (@DILUTE=0). The default is 1 which implies that ore and waste cannot be selectively mined within an MMU, which is the usual case.

### Pre-Defined Waste

Pre-defined waste volumes can optionally be modeled prior to generating the envelopes. The minimum dimension of pre-defined waste can be defined, and areas satisfying these criteria can either be excluded from the envelope, or used as a last resort to mine economic ore. If parameter @**PDWONLY** is set to 1 then only the pre-defined waste envelope will be output. If @**PWDONLY** is set to 0 then both pre-defined waste and MMU envelopes will be modeled. In order to use the pre-defined waste option, all three dimensions of the pre-defined waste volume (@**PDWSIZE**[X|Y|Z]) must be defined. The dimensions of the pre-defined waste should be defined in multiples of the sub-MMU size. If this is not the case they will be rounded to the nearest sub-MMU size.

The maximum value for pre-defined waste is specified using the @PDWGRADE or @PDWVALUE parameter. The maximum volume of ore (material above Cutoff) that can be included in pre-defined waste is defined by the @MAXORE parameter. This is expressed as a proportion between 0 (no ore allowed) and 1 (any volume of ore allowed).

### Constraining Envelopes

Specific areas of the model can be excluded from the optimization to constrain the MMU envelopes. Examples would include previously mined areas, blocks above the topography surface, or areas that have been excluded for support, access or poor ground conditions. Several methods are available: 

  1. File &**EXCLUDE** can include a list of values for a field that already exists in the input model to flag those blocks as unavailable for mining. An acceptable MMU cannot contain all or part of one of these blocks. 
  2. Where a **MINED** field is supplied with the input model, a non-zero value of the **MINED** field will prohibit an MMU including that block. 
  3. The MMU can be constrained to lie within blocks in the input model by setting parameter @**INMODEL** =1. An MMU will then only be considered if the MMU volume lies completely within modeled blocks. If @**INMODEL** =0 then an MMU can include unmodeled material that is assigned a default grade (@**DEFGRADE**), default value (@**DEFVALUE**) and default density (@**DENSITY**). 

If the density of a block is set to zero then the block is considered as an air block instead of undefined waste.

### Mineable Envelopes

The process defines 'mineable envelopes', which are created by the accumulation of all best contiguous MMUs. With the @ENVTYPE parameter it is possible to define different types of envelopes:

0\. Maximum

1\. Minimum

2\. Ranked

The input model is reblocked into sub-MMU sized cells and each sub-MMU is analysed in turn. All possible MMUs which include that sub-MMU are evaluated and all sub-MMUs that lie within economic MMUs (grade greater than **Head Grade**) are flagged as part of the Maximum envelope. If a Maximum envelope has been defined (@**ENVTYPE** =0) then processing moves on and the next sub-MMU is analysed and so on until all sub-MMUs have been considered. This definition of the Maximum envelope means that several low grade sub-MMUs surrounding a group of high grade sub-MMUs may be assigned to a Maximum envelope even though the average grade of the total envelope may be below Head Grade.

If a Minimum (@**ENVTYPE** =1) or Ranked (@**ENVTYPE** =2) envelope has been selected then further processing is applied. For a Minimum envelope each sub-MMU is analysed in turn and if the sub-MMU is above Cutoff and it forms part of one or more economic MMUs then the best MMU as defined by @**OPTIMISE** is selected and all sub-MMUs within that best MMU are assigned to the Minimum envelope. In this way a sub-MMU that was initially assigned as Maximum may be reassigned as Minimum.

For a Ranked envelope the value (as defined by @**OPTIMISE**) of every possible MMU position is evaluated and if it is above Head Grade then it is flagged as economic. All economic MMUs are sorted by value. The MMU with the maximum value is selected and all sub-MMUs within that MMU are assigned as Ranked. The next best MMU is then selected and those sub-MMUs that are not already assigned as Ranked are identified and evaluated. If the sum of the incremental sub-MMUs is above Head Grade then the incremental sub-MMUs are flagged as Ranked. This procedure is repeated until all economic MMUs in the sorted list have been processed. As with the calculation of the Minimum envelope a sub-MMU that was initially assigned as Maximum may be reassigned as Ranked.

As can be seen from the above definitions all three envelope types use the Head Grade to define an economic MMU but only the Minimum envelope uses the Cutoff Grade, to define the boundary between ore and waste. In general it is suggested that the Head Grade and Cutoff Grade are made equal. However if the Head Grade is calculated on the basis that it carries all costs but the Cutoff Grade represents the breakeven operating cost then Cutoff Grade can be made less than Head Grade. This will allow marginal ore to be included in the envelope although this could result in the grade of an envelope being below Head Grade but above Cutoff Grade.

The Ranked envelope gives a slightly smaller tonnage, but higher average grade, than the Minimum envelope and will maximize the value of the deposit for a given Head Grade. The Ranked envelope algorithm ensures that the grade of a Ranked envelope will always be above Head Grade. Unless the option of using a Cutoff Grade less than the Head Grade is appropriate it is suggested that the Ranked envelope is selected (@**ENVTYPE** =2) rather than the Minimum envelope (@**ENVTYPE** =1).

The Maximum envelope provides an outer envelope encompassing all acceptable alternate MMU positions that contain and could be considered to mine the ore blocks. Detailed mine design should be based around the Ranked or Minimum envelope and be within the Maximum envelope. The increment between the Ranked or Minimum envelope and the Maximum envelope includes marginal ore that can be used if the design needs to include additional material.

### Envelope Numbering

If @**ENVNUM** =1 then envelopes of contiguous sub-MMUs will be identified and each envelope will be assigned a unique envelope number. Sub-MMUs are considered to be contiguous if they share a common face but are not contiguous if they only share a common edge. Envelope numbers are assigned sequentially starting at 1 and incrementing by 1. The Results file then includes an evaluation of each envelope.

If @**ENVNUM** =0 then all sub-MMUs within all envelopes are assigned envelope number 1 (field **ENVNUM** =1) so the results file is just the total evaluation over all envelopes. Setting @**ENVNUM** =0 makes processing faster.

### Post-Processing Waste

An optional waste post-processing step, controlled by parameter @**OPTWASTE** , is used to determine whether a waste sub-MMU that is enclosed by or adjacent to a mineable envelope should be included as part of the envelope. A test is made to determine how many MMUs which include that sub-MMU meet the Head Grade criteria. This is expressed as a fraction of the total number of MMUs that include the sub-MMU. If this fraction is greater than or equal to the @**OPTWASTE** parameter then the sub-MMU is included as part of the mineable envelope. If this post-processing option is not required then the value of the parameter should be set to zero which is the default.

### Output Files

Three output files can be selected:

  * OUT - A copy of the input model with extra field MINED

  * ENVMODEL - Envelope model showing envelope type and envelope number for each sub-MMU

  * RESULTS - Results file - grade and tonnes by envelope

All three files are optional but a minimum of one file must be selected. Although the contents of the two model files are always calculated by the process the actual files are only created if they have been selected. Very large files can take several minutes to write, so if a file is not required then it is faster not to select it. 

#### Output Model

All blocks in the input file (&**IN**) are written to the output model file (&**OUT**) without subdivision but with the addition of a * **MINED** field to indicate the proportion of the input block that is included in a mineable envelope.

#### Envelope Model

The Envelope block model (&**ENVMOD**) identifies cells lying within mineable envelopes. It provides an aid to visualisation and is required as input to the sequencing process **ENVSEQ**. The cell size is defined by the sub-MMU increment size and by default this is used as the parent cell size for the envelope model. However the @**XSUBCELL** , @**YSUBCELL** and @**ZSUBCELL** parameters can be used to define the parent cell in terms of multiples of the sub-MMU size. 

In addition to the standard 13 model fields the envelope model includes the following: 

  * * **GRADE** recording the average block grade.
  * * **VALUE** for the accumulated value of a block.
  * * **DENSITY** the average density.
  * * **ENVBEST** the grade (if @OPTIMISE=1,2,3) or the accumulated value (if @OPTIMISE=4) of the best MMU in which the sub-MMU participates. 
  * * **OPTIMISE** an implicit numeric field which records the value of the @OPTIMISE parameter. 
  * * **ENVNUM** the envelope number.
  * * **ENVELOPE** records the envelope type for each block: 

UND |  undefined (not explicitly modeled) in the input model and not included in an envelope  
---|---  
EXC |  excluded in the input model  
MOD |  modeled in the input model, but not included in an envelope  
PDW |  pre-defined waste  
MAX-UND |  undefined in the input model but included in a Maximum envelope  
MAX-MOD |  modeled in the input model and included in a Maximum envelope  
MAX-PDW |  initially classified as pre-defined waste but then included in a Maximum envelope  
MIN-UND |  undefined in the input model but included in a Minimum envelope  
MIN-MOD |  modeled in the input model and included in a Minimum envelope  
MIN-PDW |  initially classified as pre-defined waste but then included in a Minimum envelope  
MIN-IUND |  undefined in input model and added to a Minimum envelope in the post-processing phase  
MIN-IMOD |  modeled in input model and added to a Minimum envelope in the post-processing phase  
RNK-UND |  undefined in the input model but included in a Ranked envelope  
RNK-MOD |  modeled in the input model and included in a Ranked envelope  
RNK-PDW |  initially classified as pre-defined waste but then included in a Ranked envelope  
RNK-IUND |  undefined in input model and added to a Ranked envelope in the post-processing phase  
RNK-IMOD |  modeled in input model and added to a Ranked envelope in the post-processing phase  
  
As can be seen from the definitions above the model may include blocks in those areas within the envelope that are not explicitly defined in the input model. 

The @**ENVOUT** parameter controls which of the above envelope types are written to the envelope model:

0 |  all values  
---|---  
1 |  all values except UND (the default)  
2 |  all values except UND, MOD, EXC  
3 |  all values except UND, MOD, EXC, PDW  
4 |  all values except UND, MOD, EXC, PDW, MAX-UND, MAX-MOD, MAX-PDW  
  
The envelope model can be evaluated directly, and with the use of **BLKPER** a series of boundary strings can be output for wireframing, or with **BLKTRI** the model can be directly wireframed. 

#### Results File

A summary report for each envelope is written to the &**RESULTS** file with statistics on volume, tonnes, grade or value, envelope limits and center of gravity. 

If a Maximum envelope has been selected then the results will include all material classified as MAX-UND, MAX-MOD or MAX-PDW. If a Minimum envelope has been selected then the results are for the five MIN-* envelope types and similarly for a Ranked envelope.

### Maximum Size of Envelope Model

The maximum size of the envelope model is 100,000,000. If the input parameters define an envelope model with more than this number of potential sub-MMUs then the process terminates with an error message. The calculation of the maximum potential number of sub-MMUs is illustrated in the following table:

|  X |  Y |  Z  
---|---|---|---  
@MMUMIN[XYZ]  |  200  |  300 |  400  
@MMUMAX[XYZ] |  3200 |  1800 |  1400  
Range = MMUMAX - MMUMIN |  3000 |  1500 |  1000  
@MMUSIZE[XYZ] |  30 |  15 |  10  
@MMUINC[XYZ] |  3 |  3 |  2  
Sub-MMU Size = MMUSIZE / MMUINC |  10 |  5 |  5  
Number of Sub-MMUs = Range / Increment Size |  300 |  300 |  200  
  
The limits of the envelope model are defined by parameters **MMUMIN**[XYZ] and **MMUMAX**[XYZ], and the sub-MMU size is defined by dividing the MMU size by the number of increments per MMU. Therefore in the above example there will be 300 sub-MMUs in X, 300 in Y and 200 in Z making a total of 300*300*200 = 18,000,000 potential cells. This model could therefore be created in the EP version but not in the SP version.

### Processing Speed

Processing speed is affected by a wide range of factors including:

  * Input model size
  * Maximum potential number of sub-MMUs in output envelope model
  * Parameter values
  * Computer hardware and operating system
  * Available contiguous memory

The **MODENV** process has five large arrays which are used for storing input model data, intermediate processing data and output model data. These arrays are organised so that as much as possible is held in physical memory with the remainder being stored in virtual memory ie on disk. As memory access is very much faster than disk access the processing speed will slow down significantly if virtual memory has to be used. Unfortunately simply adding more physical memory to the computer only helps up to a point as there is a limit (usually 2Gb) on the amount of memory the operating system can address for a single program such as Studio. 

It order to maximize available memory the following steps are recommended:

  * Minimize the number of memory resident programs that are loaded when the computer starts.
  * Reboot the computer, load and run Studio immediately. Do not run other programs.
  * Minimize the maximum potential number of sub-MMUs (cells) in the output envelope model.

Consult your Datamine support office for more information on computer memory requirements. 

##### The Slicing Option

An option exists that can help to optimize memory usage. If all the storage arrays fit into memory then no further optimization is possible but if the arrays are too large then **MODENV** slices the input geological model into sub-models that do fit into memory and processes each one individually. The sub-models overlap to avoid any edge effect and are recombined back into a single model.  
  
The overlap is in the X direction and the width of the overlap is controlled by parameter @**XOVERLAP**. The default is 2 which means that in length units the overlap for each edge is twice the size of the MMU dimension in X. The minimum width, excluding overlap, is the parent cell size in X of the input geological model. Consider the following example:

  * Parent cell size in X of geological model (XINC) = 12
  * Size of MMU in X (MMUSIZEX) = 8
  * Overlap parameter (@XOVERLAP) = 2 

In this case, the overlap on each side will be 16 (8 * 2) and the minimum total slice width will be 12 + 2 * 16 = 44. If @**XOVERLAP** is set to 1 then the overlap on each side will be 8 (8 * 1) and the minimum total slice width will be 12 + 2 * 8 = 28. 

Note: This calculation is to find the _minimum_ slice width. In practice a slice will usually include several parent cell widths from the geological model plus the overlap either side.

Experience has shown that an @**XOVERLAP** value of 2 is sufficient to eliminate almost all approximations caused by slicing. For most practical situations an @**XOVERLAP** value of 1 is sufficient and will give only minimal differences from the full solution of no slicing. If an @**XOVERLAP** value of 2 is used and the minimum width slice does not all fit in physical memory then the processing speed will be reduced as virtual memory is used and a message will be displayed in the **Command** Window. If processing is taking too long then it is suggested that the command is terminated (using the x button on the **Command** menu bar) and rerun with an @**XOVERLAP** value of 1. If the minimum slice width still does not fit in memory then other options to reduce run time are available as described in the Minimizing Run Time section below.

If a large model is being processed then it can be useful to first run a test to find whether virtual memory will be required. If parameter @**NORUN** is set to 1 then the size of each slice will be calculated and compared with the available memory but the actual envelopes will not be calculated. The report in the **Command** window identifies which slices will require virtual memory as illustrated below. A decision may then be made to reduce the size of the overlap (@**XOVERLAP**) and rerun.

Although the slicing option can be used for most cases there are some combinations of inputs for which the geological model cannot be sliced and virtual memory usage is still required for large models. The restrictions are:

  * The **SHAPE** file must not include any records, so the Minimum Mining Unit (MMU) cannot be defined as a mini model.
  * If the **IN** model is rotated then a SHAPE file cannot be used. The limits and rotation of the envelope model will be the same as the limits and rotation of the IN model.
  * The **SHAPE** file cannot be rotated.

### Minimizing Run Time

  * Always do a test run first with a small number of MMU increments. Ideally set **MMUINCX** = **MMUINCY** = **MMUINCZ** = 1 and use the min/max volume parameters (@**MMUMIN**[XYZ],@ **MMUMAX**[XYZ]) to restrict the volume of the envelope model.
  * The number of potential cells in the output envelope model has the biggest effect on run time so always keep the MMU increment parameters as small as possible.
  * Use the @**ENVOUT** parameter to eliminate some **ENVELOPE** categories of cells from the envelope model. For example setting @**ENVOUT** =2 will eliminate cells that have **ENVELOPE** values of:
    * _UND_ (undefined): volumes without cells in the geological model
    * _MOD_ (model): cells in the geological model but not in an envelope
    *  _EXC_ (excluded): cells that have been defined as excluded

Note: The above categories of **ENVELOPE** are often not needed in the envelope model.

  * Only select the output files that you actually need. Creating each file adds to the processing time. Maybe for the first run just select an envelope model and do not select either the mined model or the reserves output file. Creating the mined model can add significantly to the processing time so don't create it if you are not going to use it.
  * Set @**ENVNUM** =0 so that envelopes are not assigned unique numbers.
  * Set the @**XOVERLAP** parameter to 1. 

### Progress Messages

The level of information and progress messages displayed in the Output Window is controlled by parameter @INFO which is either 1 (minimum), 2 (intermediate) or 3 (maximum). Although the default is 2 it is suggested that a value of 3 is selected if the run time is more than a few seconds so that progress can be monitored closely. As well as information in the Output Window detailed progress is recorded in the message area at the bottom left corner of the window. 

## Input Files

Name| Description| I/O Status| Required| Type  
---|---|---|---|---  
IN| Input model file for evaluation. This must have the fields **XMORIG** , **YMORIG** , **ZMORIG** , **NX** , **NY** , **NZ** (implicit) and **IJK** , **XC** , **YC** and **ZC** (explicit). **XINC** , **YINC** and **ZINC** must exist as either explicit (sub-cells permitted) or implicit (no sub-cells). There must also be at least one explicit numeric data field, to be specified as * **VALUE** or * **GRADE**. The records may be in any order, but speed is increased if they are in IJK order. If it is a Rotated Model then it must also include the fields **X0, Y0, Z0, ANGLE1, ANGLE2, ANGLE3, ROTAXIS1, ROTAXIS2** , and **ROTAXIS3**.| Input| Yes| Block Model  
SHAPE| Input envelope shape template file to define one or more envelope shapes, or the orientation of the default envelope shape. Must contain fields **XC, YC, ZC, XINC, YINC, ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK** and optionally * **ZONE**. If the envelope orientation is not parallel to the input model then this model file must be a Rotated Model that include the fields **X0, Y0, Z0, ANGLE1, ANGLE2, ANGLE3, ROTAXIS1, ROTAXIS2** , and **ROTAXIS3**.| Input| No| Block Model  
EXCLUDE| Optional input file to supply those values of one field in the input model that define an area for exclusion from the envelope. A maximum of 50 values is allowed. The field name in this file should be the same as a field in the input model file.| Input| No| Undefined  
  
## Output Files

Name| I/O Status| Required| Type| Description  
---|---|---|---|---  
OUT| Output| No| Block Model| Output model file with the additional field *MINED. May be the same as &IN if no new fields are created.  
ENVMODEL| Output| No| Block Model| Output model with the envelope grade distribution, where the envelope mimimum mining unit increment defines the cell size. The file is a standard model file with the fields ***VALUE, *GRADE, *ENVBEST, *DENSITY, *ENVELOPE** and * **SHAPZONE** if specified. The value in the * **ENVBEST** field depends on the value of @**OPTIMISE** : 

  * If @**OPTIMISE** =1 (maximise ore tonnes) then the value in the field is ore tonnes.
  * If @**OPTIMISE** =2 (maximise grade) then the value in the field is grade.
  * If @**OPTIMISE** =3 (maximise metal) then the value in the field is metal content.
  * If @**OPTIMISE** =4 (maximise dollars) then the value in the field is dollars.

  
RESULTS| Output| No| Undefined| Output results file to report statistics for each envelope, with fields ***ENVNUM, *ENVELOPE, *SHAPZONE** (if specified), ***VALUE, *GRADE, VOLUME, TONNES, MINX, MAXX, MINY, MAXY, MINZ, MAXZ, COGX, COGY, COGZ. *ENVELOPE** and ***SHAPZONE** fields are reported individually and in total.  
  
## Fields

Name| Description| Source| Required| Type| Default  
---|---|---|---|---|---  
VALUE| Numeric (explicit) field for the value of input model blocks.| IN| No| Numeric| Undefined  
GRADE| Numeric (explicit) field for the grade of input model blocks.| IN| Yes| Numeric| Undefined  
SHAPZONE| Field in the input model and envelope shape template file when different envelope shapes are allowed in different mining areas.| IN, SHAPE| No| Any| Undefined  
ENVBEST| Numeric (explicit) field for the best envelope grade or value in the &**ENVMODEL** file. | Undefined| No| Numeric| ENVBEST  
ENVELOPE| Alphanumeric (explicit) field for the cell type in the &**ENVMODEL** file. The default name **ENVELOPE** is used if none is supplied.| Undefined| No| Character| ENVELOPE  
ENVNUM| Numeric (explicit) field for the envelope number in the &**ENVMODEL** and &**RESULTS** files. The default name **ENVNUM** is used if none is supplied.| Undefined| No| Numeric| ENVNUM  
HDGRADE| Optional field for the head grade of envelopes in which the block participates. The envelope head grade must be greater than the head grade value supplied from any participating block. Absent values are ignored.| IN| No| Numeric| Undefined  
MINED| Proportion of block within the envelope| Undefined| No| Numeric| MINED  
DENSITY| Optional density field in the input model for average grade and tonnage calculations.| IN| No| Numeric| DENSITY  
  
## Parameters

Name| Description| Required| Default| Range| Values  
---|---|---|---|---|---  
CUTOFF| Cutoff grade to be applied to input model blocks.| Yes| 0| Undefined| Undefined  
HDGRADE| Required head grade for economic envelopes.| Yes| 0| Undefined| Undefined  
DEFGRADE| Default grade for envelope volume not modelled with blocks, or blocks with an absent grade or value.| No| 0| Undefined| Undefined  
DEFVALUE| Default value for envelope volume not modelled with blocks, or blocks with an absent grade or value. This parameter is expressed as value per unit volume.| No| 0| Undefined| Undefined  
DENSITY| Density value where a density field is not supplied, the value is absent, or the envelope volume is not modelled with blocks. If set to zero then absent blocks are assumed to be air.| No| 1| Undefined| Undefined  
MAXWASTE| Maximum waste material in an envelope, expressed as a volume fraction, for an envelope evaluation to be accepted as an alternative in the optimal selection. The default (1.0) allows any proportion of waste provided the head grade target is met. The value cannot be lower than the @**PDWASTE** value.| Yes| 1| 0,1| Undefined  
MAXORE| Maximum ore material in a pre-defined waste shape, expressed as a volume fraction.| Yes| 0| 0,1| Undefined  
PDWVALUE| Maximum value for a pre-defined waste shape.| Yes| 0| Undefined| Undefined  
PDWGRADE| Maximum grade for a pre-defined waste shape.| Yes| 0| Undefined| Undefined  
PDWASTE| Maximum pre-defined waste material in an envelope, expressed as a volume fraction, for an envelope evaluation to be accepted as an alternative in the optimal selection. The default value of 0 allows no pre-defined waste, and a value between 0 and 1 allows pre-defined waste to be taken as a last resort to extract otherwise economic ore.| No| 0| 0,1| Undefined  
OPTWASTE| Post-process remnant waste "internal" to the envelope that is not flagged as pre-defined waste or already included in a mining envelope to evaluate if the waste can be in one, some, or all alternative envelopes. The proportion is specified as a fraction, and will only be processed for a non-zero value. Only those blocks that are outside the minimum envelope but included in the maximum envelope are considered. A value of zero would generate the maximum envelope.| No| 0| 0,1| Undefined  
OPTIMISE| Method for selecting optimal envelope position where alternate positions are available to be considered: 

  1. Maximize ore tonnes ie minimize [below cutoff] waste. 
  2. Maximize grade.
  3. Maximize contained metal. 
  4. Maximize accumulated value.

| Yes| 2| 1,4| 1,2,3,4  
DILUTE| Include waste with ore in envelope grade calculations, and * **ENVBEST** output: 

  * 0 - Ore only.
  * 1 - Ore and waste.

| Yes| 1| 0,1| 0,1  
ENVTYPE| Report the minimum or maximum envelope in the results file for sequencing. Both minimum and maximum envelopes are generated in the optimiser. 

  * 0 - maximum envelope. 
  * 1 - minimum envelope.

| Yes| 1| 0,1| 0,1  
ENVNUM| Apply a unique numbering scheme to the envelopes. Having unique numbers can slow down processing by [very] approximately 20%. 

  * 0 - apply the same number to all envelopes.
  * 1 - Make envelope numbers unique.

| Yes| 1| 0,1| 0,1  
INMODEL| Constrain envelopes to the volume of the input model occupied by blocks: 

  * 0 - unconstrained.
  * 1 - envelope volume to be completely occupied by blocks in the input model.

| Yes| 0| 0,1| 0,1  
SHAPEMTH| Method for selection from alternative envelope shapes when zones are specified: 

  * 0 - envelope shape matching block zone.
  * 1 \- envelope shape with minimum zone dilution.
  * 2 - envelope shape with best value irrespective of zone combination.

| Yes| 0| 0,2| 0,1,2  
PDWONLY| Flag to specify whether the current run should create both predefined waste and mining envelopes, or only the pre-defined waste envelope: 

  * 0 - both pre-defined waste and mining envelopes. 
  * 1 - pre-defined waste envelope only.

| No| 0| 0,1| 0,1  
MMUINCX| Number of envelope increments within the minimum envelope dimension in X coordinate.| Yes| 1| 1,+| Undefined  
MMUINCY| Number of envelope increments within the minimum envelope dimension in Y coordinate.| Yes| 1| 1,+| Undefined  
MMUINCZ| Number of envelope increments within the minimum envelope dimension in Z coordinate.| Yes| 1| 1,+| Undefined  
MMUSIZEX| Minimum envelope dimension in the horizontal X coordinate.| Yes| 0| Undefined| Undefined  
MMUSIZEY| Minimum envelope dimension in the horizontal Y coordinate.| Yes| 0| Undefined| Undefined  
MMUSIZEZ| Minimum envelope dimension in the vertical Z coordinate.| Yes| 0| Undefined| Undefined  
PDWSIZEX| Minimum pre-defined waste shape dimension in the horizontal X coordinate.| Yes| 0| Undefined| Undefined  
PDWSIZEY| Minimum pre-defined waste shape dimension in the horizontal Y coordinate.| Yes| 0| Undefined| Undefined  
PDWSIZEZ| Minimum pre-defined waste shape dimension in the vertical Z coordinate.| Yes| 0| Undefined| Undefined  
MMUSLOPN| Envelope slope factor 1:n in the northerly direction, positive outwards| No| 0| Undefined| Undefined  
MMUSLOPS| Envelope slope factor 1:n in the southerly direction, positive outwards| No| 0| Undefined| Undefined  
MMUSLOPE| Envelope slope factor 1:n in the easterly direction, positive outwards| No| 0| Undefined| Undefined  
MMUSLOPW| Envelope slope factor 1:n in the westerly direction, positive outwards| No| 0| Undefined| Undefined  
MMUSLOPI| Specifies if the slope factors are to be interpolated between orthogonal directions 0 - rectangular horizontal shape 1 - elliptical horizontal shape| No| 0| Undefined| Undefined  
MMUMINX| Minimum X coordinate for envelope volume. This is not required if an envelope shape template file &**SHAPE** is defined.| No| Undefined| Undefined| Undefined  
MMUMINY| Minimum Y coordinate for envelope volume. This is not required if an envelope shape template file &**SHAPE** is defined.| No| Undefined| Undefined| Undefined  
MMUMINZ| Minimum Z coordinate for envelope volume. This is not required if an envelope shape template file &**SHAPE** is defined.| No| Undefined| Undefined| Undefined  
MMUMAXX| Maximum X coordinate for envelope volume. This is not required if an envelope shape template file &**SHAPE** is defined.| No| Undefined| Undefined| Undefined  
MMUMAXY| Maximum Y coordinate for envelope volume. This is not required if an envelope shape template file &SHAPE is defined.| No| Undefined| Undefined| Undefined  
MMUMAXZ| Maximum Z coordinate for envelope volume. This is not required if an envelope shape template file &**SHAPE** is defined.| No| Undefined| Undefined| Undefined  
MMUMAXZ| Maximum Z coordinate for envelope volume. This is not required if an envelope shape template file &**SHAPE** is defined.| No| Undefined| Undefined| Undefined  
MMUMAXZ| Maximum Z coordinate for envelope volume. This is not required if an envelope shape template file &**SHAPE** is defined.| No| Undefined| Undefined| Undefined  
MMUMAXZ| Maximum Z coordinate for envelope volume. This is not required if an envelope shape template file &**SHAPE** is defined.| No| Undefined| Undefined| Undefined  
XSUBCELL| Number of subcells per parent cell in X direction| No| 1| 1,100| Undefined  
YSUBCELL| Number of subcells per parent cell in Y direction| No| 1| 1,100| Undefined  
ZSUBCELL| Number of subcells per parent cell in Z direction| No| 1| 1,100| Undefined  
ENVOUT| Flag to control which **ENVELOPE** types are included in the output envelope file &**ENVMODEL** :| Option| Description  
---|---  
0| Include all values of the field **ENVELOPE**  
1| Include all values of the field **ENVELOPE** except _UND_  
2| Include all values of the field **ENVELOPE** except _UND_ , _MOD. EXC_  
3| Include all values of the field **ENVELOPE** except UND, _MOD, EXC, PDW_  
4| Include all values of the field **ENVELOPE** except _UND, MOD, EXC, PDW, MAX-UND, MAX-MOD, MAX-PDW_  
No| 1| 0,4| 0,1,2,3,4  
XOVERLAP| Overlap in X between successive slices, defined as the number of MMUs in X. ie in length units the overlap is @**XOVERLAP** * @**MMUSIZEX** :| Option| Description  
---|---  
1| \- overlap of 1 MMU widths in X  
2| \- overlap of 2 MMU widths in X  
No| 2| 1,2| 1,2  
CALCENV| Flag to select either a test run to report slicing and memory statistics or a full run to calculate the mineable envelopes:| Option| Description  
---|---  
0| \- test run; do not calculate mineable envelopes  
1| \- full run; calculate mineable envelopes  
No| 1| 0,1| 0,1  
PROGRESS| Progress counter increment for progress messages displayed in the bottom right corner of the Studio window. Increasing the increment can reduce processing time.| No| 5000| Undefined| UNdefined  
INFO| Flag to control the level of information displayed to the Output Window during processing:| Option| Description  
---|---  
1| Minimum level of output  
2| Intermediate level of output  
3| Maximum level of output  
No| 2| 1,3| 1,2,3  
  

### Example 1 - No Slicing Required

Only 2 MMU increments in X, Y and Z so everything fits into memory
    
    
    !MODENV &IN(_vsbmgrd),&OUT(OUT1),&ENVMODEL(ENVMOD1),  
  
---  
      
    
    &RESULTS(RESULTS1),*GRADE(AU),*ENVBEST(ENVBEST),  
      
    
    *ENVELOPE(ENVELOPE),  
      
    
    *ENVNUM(ENVNUM),*MINED(MINED),*DENSITY(DENSITY),  
      
    
    @CUTOFF=3.4,@HDGRADE=3.0,@DEFGRADE=0.0,@DEFVALUE=0.0,  
      
    
    @DENSITY=1.0,@MAXWASTE=1.0,@MAXORE=0.0,@PDWVALUE=0.0,  
      
    
    @PDWGRADE=0.0,@PDWASTE=0.0,@OPTWASTE=0.0,@OPTIMISE=2.0,  
      
    
    @DILUTE=1.0,@ENVTYPE=2.0,@ENVNUM=1.0,@INMODEL=0.0,  
      
    
    @SHAPEMTH=0.0,@PDWONLY=0.0,  
      
    
    @MMUINCX=2,@MMUINCY=2,@MMUINCZ=2,  
      
    
    @MMUSIZEX=10,@MMUSIZEY=10,@MMUSIZEZ=10,  
      
    
    @PDWSIZEX=0.0,@PDWSIZEY=0.0,@PDWSIZEZ=0.0,@MMUSLOPN=0.0,  
      
    
    @MMUSLOPS=0.0,@MMUSLOPE=0.0,@MMUSLOPW=0.0,@MMUSLOPI=0.0,  
      
    
    @XSUBCELL=1.0,@YSUBCELL=1.0,@ZSUBCELL=1.0,@ENVOUT=3.0,  
      
    
    @XOVERLAP=2,@PROGRESS=5000.0,@INFO=2.0  
      
    
       
      
    
    MODENV 19:05:02  
      
    
                -------------------------------------------------------------------   
      
    
                MMU Parameters  
      
    
            --------------  
      
    
                 MMU Size in XYZ       =   
      
    
                 10  10  10  
      
    
                 Increment Size in XYZ = 5  5  5  
      
    
                 Slope in NSEW         =   
      
    
                 0  0  0  0    
      
    
                -------------------------------------------------------------------  
      
    
                19:05:03 Memory Optimization complete ...  
      
    
                -------------------------------------------------------------------  
      
    
                Slicing Optimization  
      
    
                --------------------  
      
    
                 Input parameters are suitable for slicing version of   
      
    
                 MODENV.  
      
    
                 Slicing will be in the X direction.  
      
    
                 Envelope model extent in X ranges from 5870 to 6320  
      
    
                 Overlap parameter:                  2  
      
    
                 Overlap width each side of slice:   20  
      
    
                 Max slice width (including overlap) in memory: 14400  
      
    
                 Max slice width (excluding overlap) in memory: 14360  
      
    
                 Estimated maximum number of slices: 1   
      
    
                -------------------------------------------------------------------  
      
    
                Model fits into memory so slicing not required.  
      
    
                -------------------------------------------------------------------  
      
    
                 MODENV0 TIME >19: 5: 3  
      
    
                 Information and Progress  
      
    
                 ------------------------  
      
    
                 The level of information displayed is controlled by parameter   
      
    
                 INFO which is currently set to 2.  
      
    
                 Possible values are 1-minimum, 2-intermediate, 3-maximum.  
      
    
                 A value of 3 is recommended for processing large models.   
      
    
                 Memory allocation started  
      
    
                 -------------------------  
      
    
                 Memory allocation complete  
      
    
             See message area for detailed progress for each stage  
      
    
                 -----------------------------------------------------  
      
    
                 1. Accumulate input model  
      
    
                      Start: 19: 5: 3  
      
    
                      End:   19: 5:   
      
    
                 3   Duration: 0 secs  
      
    
                 2. Eliminate infeasible MMUs  
      
    
                      Start: 19: 5: 3  
      
    
                      End:   19: 5:   
      
    
                 3   Duration: 0 secs  
      
    
                  3. Accumulate MMUs  
      
    
                      Start: 19: 5: 3  
      
    
                      End:   19: 5:   
      
    
                 4   Duration: 1 secs  
      
    
                  4a. Flag best MMUs for ranked envelopes - sort   
      
    
                      Start: 19: 5: 4  
      
    
                      End:   19: 5:   
      
    
                 4   Duration: 0 secs  
      
    
                  4b. Flag best MMUs for ranked envelopes - assign  
      
    
                      Start: 19: 5: 4  
      
    
                      End:   19: 5:   
      
    
                 4   Duration: 0 secs  
      
    
                 5. Assign envelope numbers   
      
    
                      Start: 19: 5: 4  
      
    
                         ... envelope   
      
    
                 number 1 assigned   
      
    
                         ... envelope   
      
    
                 number 2 assigned  
      
    
                         ... envelope   
      
    
                 number 3 assigned  
      
    
                         ... envelope   
      
    
                 number 4 assigned  
      
    
                        ... envelope   
      
    
                 number 5 assigned  
      
    
                             .........  
      
    
                         ... envelope   
      
    
                 number 31 assigned  
      
    
                         ... envelope   
      
    
                 number 32 assigned  
      
    
                         ... envelope   
      
    
                 number 33 assigned   
      
    
                      End:   19: 5:   
      
    
                 4   Duration: 0 secs  
      
    
                 6. Calculate and output results file  
      
    
                      Start: 19: 5: 4  
      
    
                      End:   19: 5:   
      
    
                 4   Duration: 0 secs  
      
    
                 7. Write the mined out model file  
      
    
                      Start: 19: 5: 4  
      
    
                      End:   19:   
      
    
                 5: 4   Duration: 0 secs  
      
    
                 8. Write the envelope model file   
      
    
                       Start: 19: 5: 4   
      
    
                      End:   19:   
      
    
                 5: 4   Duration: 0 secs   
      
    
                  -------------------------------------------------------------------  
      
    
                  17522 records in Envelope Model file ENVMOD1  
      
    
                  72 records in Results file RESULTS1  
      
    
                  33 envelopes identified  
      
    
                  15066 records in Output Model file OUT1  
      
    
                  -------------------------------------------------------------------   
      
    
                 19:05:04     MODENV finished               
  
### Example 2 - Slicing Required
    
    
    10 MMU increments in X and Y and 5 increments in Z so slicing is required  
  
---  
      
    
    !MODENV &IN(_vsbmgrd),&OUT(OUT2),&ENVMODEL(ENVMOD2),  
      
    
    &RESULTS(RESULTS2),*GRADE(AU),*ENVBEST(ENVBEST),  
      
    
    *ENVELOPE(ENVELOPE),  
      
    
    *ENVNUM(ENVNUM),*MINED(MINED),*DENSITY(DENSITY),  
      
    
    @CUTOFF=3.4,@HDGRADE=3.0,@DEFGRADE=0.0,@DEFVALUE=0.0,  
      
    
    @DENSITY=1.0,@MAXWASTE=1.0,@MAXORE=0.0,@PDWVALUE=0.0,  
      
    
    @PDWGRADE=0.0,@PDWASTE=0.0,@OPTWASTE=0.0,@OPTIMISE=2.0,  
      
    
    @DILUTE=1.0,@ENVTYPE=2.0,@ENVNUM=1.0,@INMODEL=0.0,  
      
    
    @SHAPEMTH=0.0,@PDWONLY=0.0, @MMUINCX=10,@MMUINCY=10,@MMUINCZ=5,  
      
    
    @MMUSIZEX=10,@MMUSIZEY=10,@MMUSIZEZ=10,  
      
    
    @PDWSIZEX=0.0,@PDWSIZEY=0.0,@PDWSIZEZ=0.0,@MMUSLOPN=0.0,  
      
    
    @MMUSLOPS=0.0,@MMUSLOPE=0.0,@MMUSLOPW=0.0,@MMUSLOPI=0.0,  
      
    
    @XSUBCELL=1.0,@YSUBCELL=1.0,@ZSUBCELL=1.0,@ENVOUT=1.0,  
      
    
    @XOVERLAP=2,@PROGRESS=5000.0,@INFO=2.0              
      
    
       
      
    
    MODENV   16:40:53  
      
    
            -------------------------------------------------------------------  
      
    
            MMU Size in XYZ       = 10  10   
      
    
              10  
      
    
            Increment Size in XYZ = 1  1  2  
      
    
            Slope in NSEW         =   
      
    
             0  0  0  0  
      
    
            -------------------------------------------------------------------  
      
    
            -------------------------------------------------------------------  
      
    
            Optimum maximum number of records in memory = 16.744218 million  
      
    
            Optimum maximum width in X that will fit in memory = 250  
      
    
            -------------------------------------------------------------------  
      
    
            16:40:55   Memory Optimization complete ...  
      
    
            -------------------------------------------------------------------  
      
    
            Slicing Optimization  
      
    
            --------------------  
      
    
             Input parameters are suitable for slicing version of MODENV.  
      
    
             Slicing will be in the X direction.  
      
    
             Envelope model extent in X ranges from 5870 to 6320  
      
    
             Overlap parameter:                             2  
      
    
             Overlap width each side of slice:              20  
      
    
             Max slice width (including overlap) in memory: 250  
      
    
             Max slice width (excluding overlap) in memory: 210  
      
    
             Estimated maximum number of slices: 3  
      
    
             -------------------------------------------------------------------  
      
    
             16:40:55   Slice 1 starting ...  
      
    
             MODENV0 TIME >16:40:55  
      
    
             16:45:59   Slice 1 complete for X range 5870 to   
      
    
             6100  
      
    
             16:46:31   Slice 2 starting ...  
      
    
             MODENV0 TIME >16:46:31  
      
    
             16:53:35   Slice 2 complete for X range 6100 to   
      
    
             6320  
      
    
             16:54:38   Post-processing envelope model   
      
    
             ...  
      
    
             16:56:18   Assigning numbers to a maximum   
      
    
             of 46 envelopes ...  
      
    
             16:56:19   Calculating envelope number equivalences   
      
    
             ...  
      
    
             16:56:22   Applying envelope numbers ...  
      
    
             17:02:05   Calculating results ...  
      
    
             17:03:49   Creating output model ...   
      
    
             -------------------------------------------------------------------  
      
    
             1467823 records in Envelope Model file ENVMOD2  
      
    
             72 records in Results file RESULTS2  
      
    
             28 envelopes identified   
      
    
             15066 records in Output Model file OUT2  
      
    
             -------------------------------------------------------------------   
      
    
            17:13:55   MODENV finished  
  
### Comparison of Examples

The only difference in input between the two examples is the number of increments per MMU. Using 10x10x5 increments in example 2 is far too many and was done for illustrative purposes only. A comparison of the mineable tonnes and grade shows that using the much smaller increment size allows a little more flexibility in identifying mineable material with an increase of 5.3% in tonnage but a decrease of 2.2% in grade. However the run time was very consderably more.

Description|  Example1|  Example2|  Comment  
---|---|---|---  
MMU Size|  10 x 10 x 10|  10 x 10 x 10|  -  
Number of MMU Increments|  2 x 2 x 2 = 8|  10 x 10 x 5 = 500|  62.5 times more sub-mmus in EG2  
MMU Increment Size|  5 x 5 x 5|  1 x 1 x 2|  -  
Total Run Time (secs)|  2|  1,982|  EG2 takes 991 times longer  
Records in Envelope Model|  17,522|  1,467,823|  -  
Number of Envelopes|  33|  28|  -  
Envelope Tonnes|  4,655,049|  4,903,200|  5.3% increase in tonnes  
Envelope Grade|  4.589|  4.489|  2.2% decrease in grade  
  

Related topics and activities

  * [ENVSEQ Process ](<envseq.md>)