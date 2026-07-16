# link-crossover-switch ("tlc")

See this command in the [**command table**.](<COMMAND%20TABLE_L.md#link-crossover-switch>)

To access this command:

  * On the [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>) screen, toggle **Link crossover checking**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "link-crossover-switch"

  * Use the quick key combination "tlc".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **link-crossover-switch** and click **Run**.

## Command Overview

Toggle crossover checking on or off for string linking. If the crossover toggle is enabled, any link that would contain crossovers is automatically rejected.

If sub-optimal linking has been selected and fails then optimal linking is attempted instead. If optimal linking also fails and you have checked that there are no crossovers in the strings, the best strategy is to toggle crossover linking off, complete the link, and then use the wireframe intersections command [wf-intersections](<wf-intersections.md>) to locate the crossover.

Warning: crossover checking will increase processing time, especially where the strings have a large number of points. For regular string shapes it is better to disable crossover checking, but a wireframe intersection check is still recommended regardless.

Related topics and activities

  * [Project Settings: Wireframe Linking](<../COMMON/Project%20Settings_%20Wireframe%20Linking.md>)

  * [wf-intersections](<wf-intersections.md>)