# Select Block Identifier

To access this screen:

  1. Run the [evaluate-wireframe](<../command_help/evaluate-wireframe.md>) command

  2. Specify the required settings in the [Evaluate Wireframe](<Evaluate%20Wireframe%20Dialog.md>) screen and click OK.

This screen is used to select a unique **Mining Block Identifier** for evaluation purposes. Click OK after specifying an identifier to perform an evaluation and display a results screen.

On accepting the results, a Results File is created in memory.

Activity steps:

  1. Display the **Select Block Identifier** screen.

  2. Enter a unique Mining Block Identifier. This number is assigned to the evaluated block. The BLOCKID value is written to the results file and the mining blocks file if you are evaluating strings, or the wireframe triangle file if you are evaluating wireframes.

Note: If the BLOCKID number already exists it is overwritten. The default number given is the existing number for the block being evaluated, or the next BLOCKID number if the block has not been previously evaluated.

Related topics and activities:

  * [Evaluate Wireframe](<Evaluate%20Wireframe%20Dialog.md>) (screen)

  * [evaluate-wireframe](<../command_help/evaluate-wireframe.md>) (command)