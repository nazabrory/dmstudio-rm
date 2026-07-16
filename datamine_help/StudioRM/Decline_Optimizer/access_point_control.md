# Access Point Control

To access these controls:

  * Display the [Decline Optimizer](<DeclineOptimizerDialog.md>) screen and select the **Path Control** tab.

The **Access Point Control** area of the **Path Control** tab is used to define access points are positioned with automatically generated optimal decline shapes.

Activity steps

  1. Use Change gradient by to adjust the decline's gradient to be changed by a specified number of degrees per Unit length rather than going directly from a straight section to the target gradient.

  2. Decide if a **Flat Control Field** is to be used. This is a numeric attribute (field) in the input control string that contains the value of the minimum flat distance at each point. 

Note: If you choose a field, this overrides the **Minimum Flat Distance at Access Points** setting (see below) and makes it unavailable.

  3. If **Flat Control Field** (see above) is _(Do Not Use)_ , set the Minimum Flat Distance at Access Points. This determines the decline sections that pass through the points on the input control string (considered to be access points) must be flat or horizontal for at least the specified distance.

Related topics and activities

  * [Decline Optimizer Introduction](<DeclineOptimizerDialog.md>)