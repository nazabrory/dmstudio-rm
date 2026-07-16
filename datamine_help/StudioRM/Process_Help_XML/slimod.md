# SLIMOD Process

To access this process:

  * Model ribbon >> Manipulate >> Adjust Prototype

  * Enter "SLIMOD" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **SLIMOD** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_S.md#SLIMOD>).

## Process Overview

This process splits block model cells at cell boundaries and recalculates the IJK value.

Warning: This process will only work correctly with rotated model data If * **PROTO** has the same origin and rotations as *IN, but can have different rotated origins (X0, Y0, Z0) and different local origins ([XYZ]**MORIG**).

Using this process a block model can be transferred to a new block model prototype, with a different origin, different cell size and different number of cells. The user must ensure that the new prototype definition includes all cells in the existing model.#

The output model needs to be sorted on IJK.

See [geological model file limitations](<../COMMON/Block_Models_Size_Limits.md>).

**Note** : **SLIMOD** has a tolerance to check for the creation of very small cells. A cell will not be created in the output file if it has a volume less than the parent volume of the output prototype multiplied by 0.00000001. This tolerance is smaller than in previous versions to allow for prototypes with a large parent cell dimension in one of the axes.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
PROTO |  Input prototype model describing the model parameters. Normally set up by PROTOM. Must contain the numeric fields XC, YC, ZC, IJK (explicit) and XMORIG, YMORIG, ZMORIG, NX, NY, NZ (implicit) and XINC, YINC, ZINC as explicit fields. |  Input |  Yes |  Block Model Prototype  
IN |  Input model file. |  Input |  Yes |  Block Model  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Block Model |  Output model file. This will be sorted on IJK.