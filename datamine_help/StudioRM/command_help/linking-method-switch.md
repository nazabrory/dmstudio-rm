# linking-method-switch ("tlm")

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#linking-method-switch>)

To access this command:

  * On the [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>) screen, toggle **Optimal linking**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "linking-method-switch"

  * Use the quick key combination "tlm".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **linking-method-switch** and click **Run**.

## Description

Toggle between optimal and sub-optimal (fast) string linking methods.

  * If turned **ON** , when linking strings the wireframe is created optimally with the best surface being selected from those that satisfy the linking criterion. 

  * If turned **OFF** linking is done with tag strings - either provided by you, or if none exist then the closest pair of points on the two strings after translation to a common centre of gravity will form an implicit tag string. Each pair of tag strings is linked independently. The speed advantage of the sup- optimal increases with an increasing number of string points. If the sub-optimal method fails then linking will default to the optimal method.

Related topics and activities

  * [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)