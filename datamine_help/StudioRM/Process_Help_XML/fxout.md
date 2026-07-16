# FXOUT Process

To access this process:

  * **Data** ribbon **> > Transfer >> Whittle >> Output FOUR-X**.
  * Enter "FXOUT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **FXOUT** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_F.md#FXOUT>).

## Process Overview

Export a Datamine block model file to a Whittle FOUR-X format text file.

The following optional and required fields are expected in the block model file:

  * TOLTON \- optional; minimum tonnage in parcel to be output on export (0.5)

  * FORMAT \- optional; output format for economic file (0): 0 - fixed format, 1 - comma separated

  * ELEMENT \- required; number of elements to be processed (1): limited to 10 for FOUR-X.

  * ZONEFLD \- optional; prompt for optional ZONE field (0): 0 - don't prompt for ZONE field, 1 - prompt for ZONE field

#### Processing Methods

Select one of the following methods for specifying the tonnage and metal content of the cell or subcell:

  * METHOD ASet the parcel name (type code) and the numeric tons and metal field names for each parcel type code specified. This is then repeated for each possible parcel type. This means that each parcel type's tons and metal content are contained in a separate fields. This is probably better for regularised block models, on record per block. 

After specifying the method, you are prompted for the following information:

    1. Maximum number of product parcels.

    2. Default density

    3. Merge identical product parcel types Y/N ?

    4. Rock tonnes field name (ROCK)

    5. Mining cost adjustment field name

    6. Processing cost adjustment field name

    7. Optionally set the 'Zone field name' if this option was selected in the Parameters tab.

    8. Product parcel code (1-4 chars or blank to finish)

    9. Tonnes field name (TONNES)

    10. Metal content field (METAL)

    11. Accept the data specification with "Y" and process.

  * METHOD BDefine three fields (the parcel code field name, the parcel tons field name and the metal tonnes field name). This is much more in line with a subcelled block model which allows multiple records for each parent block. The best way of doing this is to calculate the tons and metal in each subcell and then accumulate on the parcel name field and IJK. This will give just one record for each parcel type for each parent-cell, reducing the size of the import model. 

After specifying the method, you are prompted for the following information:

    * Maximum number of product parcels.

    * Default density

    * Merge identical product parcel types Y/N ?

    * Rock tonnes field name (ROCK)

    * Mining cost adjustment field name

    * Processing cost adjustment field name

    * Optionally set the 'Zone field name' if this option was selected in the Parameters tab.

    * Product parcel code (1-4 chars or blank to finish)

    * Tonnes field name (TONNES)

    * Metal content field (METAL)

    * Ore type field name

    * Accept the data specification with "Y" and process.

The exported FOUR-X model file has a record per block with the following information:

  * Block coordinatesIX, IY, IZ

  * Total tonnes of ROCK in the block Mining cost adjustment factor

  * Processing cost adjustment factor

  * An optional Zone number, which can be used to indicate the source of the block in the original model.

  * Parcels. Zero or more parcels can be defined for each block on separate records. Up to 99 parcels are allowed.

Each parcel has the following information:

  * Rock type code (1-4 characters). This should not contain a period('.'), be 'ROCK' or start with 'GR_'. It is case sensitive and should be left justified.

  * Tonnage of the parcel Metal content of the parcel for up to 10 elements

  * Metal content is measured in metal units, not grade.

A parcel is allowed to have a tonnage and zero metal content, to allow multiple 'waste' material types to be identified. The block dimensions are defined by the Datamine model cell structure. The rock type code must be supplied as an alphanumeric field. Only the first 4 characters are accepted. The required field names are supplied interactively.

An explicit field for tonnes of rock and metal content in the cell/sub-cell is required, together with optional explicit fields for mining cost adjustment, and processing cost adjustment. Where sub-cells are supplied, then block averages are calculated for the optional mining and processing cost adjustment factors.

The user can choose whether multiple sub-cells of the same rock type code within a cell are to be summed into one parcel or not. If sub-cells are being output as separate parcels, a limit can be set on the total number of parcels output for a block. If necessary, parcels are combined with the same rules as the FOUR-X FXRB reblocking program. If a sub-cell model is supplied it must be in sorted (IJK) order.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input model file. |  Input |  Yes |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
TOLTON |  Minimum tonnage in parcel to be output (0.5) |  No |  0.5 |  Undefined |  Undefined  
FORMAT |  Output format for economic file (0) 0 - fixed format 1 - comma separated |  No |  0 |  Undefined |  Undefined  
ELEMENT |  Number of elements to be processed (1) Limited to 10 for FOUR-X. |  Yes |  1 |  Undefined |  Undefined  
ZONEFLD |  Prompt for optional ZONE field (0) 0 - don't prompt for ZONE field 1 - prompt for ZONE field |  No |  0 |  0,1 |  0,1  
  
Related topics and activities

  * [FDOUT Process](<fdout.md>)

  * FXOUT Process

  * [FXIN Process](<fxin.md>)