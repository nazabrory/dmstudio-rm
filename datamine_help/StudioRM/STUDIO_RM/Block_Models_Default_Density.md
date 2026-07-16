# Block Models and Default Density

## What is Default Density?

Rock or material densities are stored in the **DENSITY** field (a standard system field) in a block model (or drillholes) file. This field is needed in order to fully utilize all the block modeling functionality within your application, especially when performing [block model evaluations](<Block_Models_Evaluation.md>). 

In the absence of a **DENSITY** field, or when absent values '-' are present in the field, the system uses the default density value currently set for the project. The default value for this parameter is '1', until you define a value to be used in your project. 

## Calculating the Default Density

The selection of a default density value should have as little detrimental effect on evaluations as possible. 

Default densities, per material, rock type or ore category, can be calculated using the [STATS](<../Process_Help_XML/stats.md>) Process and a suitable input file, for example, a drillhole assays table, drillholes or block model file.

## Setting the Default Density Manually

Typically, you set the default density for a block model evaluation using the tool doing the evaluation, such as the [Evaluate 2D Strings](<../COMMON/Evaluation2DStringsPropertiesDialog.md>) or [Evaluate Wireframe](<../COMMON/EvaluationWireframePropertiesDialog.md>) screen.

See [Block Model Evaluation](<Block_Models_Evaluation.md>).

Note: For other commands, you can set the density independently using the [set-default-density](<../command_help/set-default-density.md>) command. Note that the command-line evaluation commands referenced above do not recall the default density set in this way.

Related topics and activities:

  * [Working with Block Models](<block_models_introduction.md>)

  * [Block Model Evaluation](<Block_Models_Evaluation.md>)

  * [Block Model Size Limits](<../COMMON/Block_Models_Size_Limits.md>)

  * [Block Models Overview](<Block_Models_Evaluation.md>)