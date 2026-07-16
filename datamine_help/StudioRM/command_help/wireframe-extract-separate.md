# wireframe-extract-separate ("wes")

See this command in the [**command table**.](<COMMAND%20TABLE_W.md#wireframe-extract-separate>)

To access this screen:

  * **Wireframe** ribbon **> > Boolean >> Extract Separate**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "wireframe-extract-separate"

  * Use the quick key combination "wes".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **wireframe-extract-separate** and click **Run**.

## Description

Creates separate wireframes for each logically discrete piece of data formed by the interaction of two wireframe data collections. Two separate data are input to this command, and each output represents one interconnected surface from the original objects; however original surfaces may have been divided by intersection with the other objects wireframe. Inputs can either be loaded wireframe objects or collections of preselected wireframe triangle data.

The Extract Separate command will attempt to classify each new wireframe data surface with respect to the other wireframe data. Each surface may be classified as being Inside, Outside, or On the other wireframe object. This classification method makes use of the face direction stored for each triangle within the wireframe.

See [Wireframe Extract Separate](<../COMMON/Wireframe%20Extract%20Separate%20Dialog.md>) for detailed command steps, examples and more guidelines.

**Note** : the Extract Separate screen is also displayed when the **wireframe-merge** command is run.

**Note** : this command is also available using the [BOOLEAN](<../Process_Help_XML/boolean.md>) process (@METHOD=4).

**Note** : This command supports [**flexible wireframe selection**](<../COMMON/Wireframe_Selection_Concept.md>).

Related topics and activities

  * [Wireframe Extract Separate](<../COMMON/Wireframe%20Extract%20Separate%20Dialog.md>) (screen)

  * [BOOLEAN Process](<../Process_Help_XML/boolean.md>)
  * [Selecting Wireframe Data](<../COMMON/Wireframe_Selection_Concept.md>)

  * [Wireframe Difference](<../COMMON/Wireframe%20Difference%20Dialog.md>)

  * [Wireframe Intersection](<../COMMON/Wireframe%20Intersection%20Dialog.md>)

  * [Wireframe Union](<../COMMON/Wireframe%20Union%20Dialog.md>)

  * [Wireframe Solid Hull](<../COMMON/Wireframe%20Solid%20Hull%20Dialog.md>)

  * [Strings from Intersections](<../COMMON/Wireframe%20Strings%20From%20Intersections%20Dialog.md>)