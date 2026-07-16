# MOD2BLKS Process  
  
To access this process:

  * Enter "MOD2BLKS" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MOD2BLKS** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MOD2BLKS>).

## Process Overview

**MOD2BLKS** creates mining block strings, reserves file and dependencies suitable for use in Studio OPs scheduler. 

It is sometimes appropriate to schedule block model data rather than create more precise mining shapes for scheduling. 

For example, if carrying out a pre-feasibility study, a strategic planning exercise or if the deposit is wide and tabular the model cells may be a good approximation of the shapes that would be mined and hence are suitable for scheduling.

## Dependency control

By default, vertical dependencies are created between from a model cell to the cell directly below it.

Additional non-vertical dependencies can be created by using the additional parameters. These are used to specify up to four vectors, defined by number of model cells, that will be converted to dependencies. For example, setting **Q1NX** =2, **Q1NY** =0 and **Q1NZ** =1 will add a dependency from each cell to the cell two along to the right and one level down.

## PIT, BENCH and PHASE attributes

**PIT** , **BENCH** and **PHASE** attributes are added to the mining block strings and the results files.

  * The **PIT** value is hardcoded to 1. 

  * The **BENCH** value is taken from the model data definition. 

  * The **PHASE** attribute is either taken from the model file (using the **PHASE** field) or hardcoded to 1.

## Input Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODEL |  Input |  Yes |  Block Model |  The block model from which to create the mining block outlines and reserves. This must be a regular block model. You should also be aware of how many cells it contains each model cell will produce mining block outline for use in the scheduler. If you have a geological resource model it is probable that you should use the **[REBLOCK](<reblock.md>)** process to regularise the model and increase its parent cell size.  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
BLOCKS |  Output |  Yes |  Strings |  The output mining block perimeter strings. These are created at the top of each model cell. This will contain a **BLOCKID** value that is equal to the **IJK** value of the model cell from which it was created. It also contains the fields **DPLUS** , **DMINUS** and **PFLOW** which are used by the scheduler in Studio OP.  
RESULTS |  Output |  Yes |  Table |  The output results file. This contains the values from each cell and the **VOLUME** and **TONNES** of each cell.  
DEPEND |  Output |  Yes |  Table |  Output dependency file for use in Studio OP scheduling. This will contain the fields **BLOCKID1** , **BLOCKID2** , **PERCENT** and **TYPE**.  
DEPENDST |  Output |  Yes |  Table |  This is a string file that represents the dependencies that **MOD2BLKS** has created. It can be used for visualisation of the dependencies.  
WIRETR |  Output |  No |  Wireframe triangles |  Output mining blocks wireframe triangle file. Used for visualisation - contains **DEPANIM** field representing dependencies.  
WIREPT |  Output |  No |  Wireframe points |  Output mining blocks wireframe point file. Used for visualisation.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  **Default**  
---|---|---|---|---|---  
DENSITY |  The model field which contains density values. This is used to calculate mining block tonnages. |  MODEL |  No |  Alphanumeric |  Undefined  
PHASE |  An optional model numeric **PHASE** field. If set this is transferred to the mining block reserves and strings. If not set the output **PHASE** number is 1. |  MODEL |  No |  Alphanumeric |  Undefined  
  
## Parameters  

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DENSITY |  The default density to be used if the model file does not contain a density field or if the model density value is absent and **SETABSNT** =1. |  N | - |  - |  -  
SETABSNT |  If set to 1 then absent model density values will be set to the default density value. The default value for **SETABSNT** is 1. |  Y | 0 |  0,1 |  0,1  
Q1NX/Y/Z |  First quadrant: number of cells in X/Y/Z for dependency creation |  Y | 1 (X) 0 (Y) 1 (Z) | -10, 10 | -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10  
Q1NX/Y/Z |  First quadrant: number of cells in X/Y/Z for dependency creation |  Y | 1 (X) 0 (Y) 1 (Z) | -10, 10 | -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10  
Q2NX/Y/Z |  Second quadrant: number of cells in X/Y/Z for dependency creation |  Y | 0 (X) -1 (Y) 1 (Z) | -10, 10 | -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10  
Q3NX/Y/Z |  Third quadrant: number of cells in X/Y/Z for dependency creation |  Y | -1 (X) 0 (Y) 1 (Z) | -10, 10 | -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10  
Q4NX/Y/Z |  Fourth quadrant: number of cells in X/Y/Z for dependency creation |  Y | 0 (X) 1 (Y) 1 (Z) | -10, 10 | -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10  
  
Related topics and activities

  * [Reblock Process](<reblock.md>)