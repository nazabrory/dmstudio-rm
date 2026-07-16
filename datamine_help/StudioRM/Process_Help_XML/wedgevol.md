# WEDGEVOL Process

To access this process:

  * Enter "WEDGEVOL" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **WEDGEVOL** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_W.md#WEDGEVOL>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

Evaluate a wedge volume limited by two or three DTMs or wireframe surfaces.

The process requires both wireframe files (**WIRETR1** ,**WIREPT1** and **WIRETR2** ,**WIREPT2** and optionally a third surface **WIRETR3** ,**WIREPT3** ;) and a prototype block model (**PROTO**) as input.

The wedge position parameters (**SRFTYPE1** , **SRFTYPE2** ,optionally **SRFTYPE3**) define the position of the wedge volume relative to each wireframe surface as follows:

1: the wedge is located below the surface,

2: the wedge is located above the surface.

The density of the wedge volume material is set using the **DENSITY** parameter. Subcell splitting of the wedge block model cells is controlled by the **SPLITS** parameter, where SPLIT=0 does not split parent block model cells into subcells, **SPLIT** =1 splits the parent cells once, etc. The minimum and maximum elevations of the wedge volume are defined by the **ZMIN** and **ZMAX** parameters respectively.

The output from this process is an (evaluation) results file and optionally the wedge volume block model.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
WIRETR1 |  Triangle file of update wireframe surface 1 (DTM). |  Input |  Yes |  Wireframe triangle  
WIREPT1 |  Point file of update wireframe surface 1 (DTM). |  Input |  Yes |  Wireframe points  
WIRETR2 |  Triangle file of update wireframe surface 2 (DTM). |  Input |  Yes |  Wireframe triangle  
WIREPT2 |  Point file of update wireframe surface 2 (DTM). |  Input |  Yes |  Wireframe points  
WIRETR3 |  Triangle file of wireframe surface 3 (DTM). |  Input |  No |  Wireframe triangle  
WIREPT3 |  Point file of update wireframe surface 3 (DTM). |  Input |  No |  Wireframe points  
PROTO |  Block model prototype. |  Input |  Yes |  Block model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODELOU |  Output |  No |  Block model |  Wedge block model.  
RESULTS |  Output |  Yes |  Results file |  Output evaluation results data file.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
SFTYPE1 |  Wedge below or above surface 1. Select one of the following options, with the default being 1. 1: Create wedge below. 2: Create wedge above. |  Yes |  1 |  1,2 |  1,2  
SFTYPE2 |  Wedge below or above surface 2. Select one of the following options, with the default being 2. 1: Create wedge below. 2: Create wedge above. |  Yes |  |  1,2 |  1,2  
SFTYPE3 |  Wedge below or above surface 3. Select one of the following options, with the default being 2. 1: Create wedge below. 2: Create wedge above. |  No |  2 |  1,2 |  1,2  
DENSITY |  Density of filled volumes. |  Yes |  1 |  0.001,99999 |   
SPLITS |  Subcell splitting of internal wedge block model. |  Yes |  0 |  0,3 |   
ZMIN |  Minimum elevation of wedge volume. |  Yes |  -9999999 |  |   
ZMAX |  Maximum elevation of wedge volume. |  Yes |  9999999 |  |