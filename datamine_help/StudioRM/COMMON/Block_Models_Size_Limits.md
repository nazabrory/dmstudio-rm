# Block Model Size Limits

The size of a block model that can be created in your application is limited by the maximum IJK value. 

The IJK field is an index value giving the location of the parent cell for each cell or subcell. Therefore, all subcells in a parent cell have the same IJK value. The minimum IJK value is 0 and the maximum potential IJK value for a model is calculated as NX*NY*NZ-1 where NX is the maximum number of parent cells in the X direction, etc.

The maximum IJK value is 2,147,748,647. This means you can create a model with, for example, `1465*1465*1000` parent cells positions. 

## Subcells per Parent Cell: recommendations

There is no limit to the number of subcells in a parent cell; however, a virtual array error may be caused in the **[ADDMOD](<../Process_Help_XML/addmod.md>)** process if an excessive number of subcells per parent cell exist in one or both of the input models.

Adding two sets of subcells is a complex process: the maximum number of subcells per parent cell that can be created in the output model depends on several factors, including the number of subcells in each of the input files, and the relative geometrical configuration of the two sets of subcells. 500 subcells per parent cell is an approximate limit for an individual model you can create more than this without causing a problem in ADDMOD, but processing will slow down considerably.

When creating a model using **[TRIFIL](<../Process_Help_XML/trifil.md>)** , there are two methods for creating subcells:

  1. Splitting based on the dip of the wireframe: ensures that 1, 2, 4 or 8 subcells are created in any direction. This means that when ADDMOD is used for two models, subcell boundaries in one or more directions will coincide minimizing the number of subcells in the output model.
  2. Splitting using SUBCELL parameters: the number of subcells as defined by the [**XYZ**]**SUBCELL** parameters should either be the same for both models, or the [**XYZ**]**SUBCELL** parameter should be a multiple or submultiple of the corresponding parameter used to create the other model.

**Note** : Using the **RESOL** parameter helps to minimize the number of subcells per parent cell when the **ADDMOD** process is used. The number of subcells in a parent cell can also be reduced by using **PROMOD** , or by re-blocking the model onto a prototype with a small parent cell.

## Loading Models

Datamine-format block models use an on-disk system, in which just the references to the original disk file are loaded into memory, rather than the full model. This allows much larger models to be accessed than would be possible if the complete block model file were loaded into memory. Block models that are loaded directly from non-Datamine formats cannot use this mechanism, and so typically use much more memory for a given number of cells.

The quantity of memory used by an on-disk models references to the original disk file is proportional to both the number of cells and subcells used, as well as the number of possible parent cells, as determined by the model prototype. If not enough memory is available, then the system reverts to a slower disk-based referencing method.

Problems may occur with large models when insufficient memory is available, or when memory has become fragmented for example, after the computer has been running continuously for a long period. In these cases, Windows memory management may cause the system to slow to an unusable level, often appearing as though the program has frozen. To address these issues, the prototype should be fitted closely to the model, where possible. If necessary, the [PROTOM](<../Process_Help_XML/protom.md>) and [SLIMOD](<../Process_Help_XML/slimod.md>) commands can be used to modify the prototype, keeping the same parent cell size, but changing the model origin and the number of cells in each direction. After the model has been revised in this way, it must be sorted by IJK.

If the prototype cannot be modified, and the block model has a relatively small number of cells and subcells, it may be possible to load the model with the **Force In-Memory Model** option selected on the Datamine Block Model screen, In Memory Modelgroup. This specifies that the method associated with non-Datamine format files is used. Consequently, the amount of memory required is proportional to the number of cells and subcells, rather than the extents of the block model.

In the case of a large model, for which neither method is successful, you may need to move it onto a new prototype with a larger parent cell. ThePROTOM,SLIMODandSORTXcommands can be employed to achieve this, using IJK as the key field.

## Summary

If the number of potential cells in the prototype is too high, you may experience problems with the Datamine file format and loaded models. Where possible, fit prototypes closely to their data, and if problems persist, move to a model with a larger parent cell size. When loading block models, the primary limit is the maximum potential IJK value, rather than the number of records. There are two options for reducing this:

  * If the actual model cells form a small volume within the limits of the model prototype, then the prototype should be adjusted so that the limits fit tightly around the model cells. Keep the same parent cell size, but change the model origin, and the number of cells in each direction, as follows:
    * In the X dimension, move the model origin by an integer multiple of the parent cell size.
    * Perform a similar action for the Y and Z dimensions.
    * Use the create-model-prototype or PROTOM command to define the new prototype.
    * Use the IJKGEN command, with @**PSMODEL** =0, to recalculate the IJK value based on the new origin and number of cells

  * Put the model onto a new prototype with a larger parent cell: for example, if the size of the parent cell is doubled in each dimension, then the maximum potential **IJK** value is reduced by a factor of 8.
    * Keep the same origin, but increase the size of the parent cell in one or more dimensions by an integer multiple of the current parent cell.
    * Use the PROTOM and [IJKGEN](<../Process_Help_XML/ijkgen.md>) commands, as described above.

Note: Having too many subcells per parent cell will reduce performance, and may require additional memory. As an approximate guide, using more than 500 subcells may start to impact performance.

Related topics and activities

  * [ADDMOD Process](<../Process_Help_XML/addmod.md>)

  * [TRIFIL Process](<../Process_Help_XML/trifil.md>)

  * [SLIMOD Process](<../Process_Help_XML/slimod.md>)

  * [PROTOM Process](<../Process_Help_XML/protom.md>)

  * [IJKGEN Process](<../Process_Help_XML/ijkgen.md>)