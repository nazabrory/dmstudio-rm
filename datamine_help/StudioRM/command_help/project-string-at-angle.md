# project-string-at-angle ("pro")

See this command in the [**command table**.](<COMMAND%20TABLE_P.md#project-string-at-angle>)

To access this command:

  * **Digitize** ribbon **> > Transform >> Project**. 

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "project-string-at-angle"

  * Use the quick key combination "pro".
  * On the **[Find Command](<../COMMON/findcommand.md>)** screen, highlight **project-string-at-angle** and click **Run**.

## Command Overview

This command allows a new string to be created by projecting an existing string up or down a specified distance. The projection is done vertically in the Z direction. If there is no currently selected string you are prompted to select one with which to do the projection. You have to indicate the high side of the string with the cursor.

You are first asked if you wish the projection to be Up, Down, Both or Relative. If you respond with Up Down or Both you are then prompted for the target elevation. If you have asked for projection in both directions then if the string crosses the target elevation some points are projected up and some down.

If you request a _Relative_ projection method you are asked to enter the desired projection distance.

The face angle used for projection is set using the [set-face-angle](<set-face-angle.md>) command. The default value for this is 60 degrees.

If rosettes are being used then these will take priority over the face angle. If a cell model **SLOPE** field is being used this will take priority over the rosettes and the face angle. The use of rosettes can be turned on or off, as can the use of a cell model **SLOPE** field.

If the intersection with wireframes is turned on then the projection will stop when a triangle is met.

Strings can continually be selected for projection using the current settings until a new command is selected. If the resulting string is the same as the string selected for projection then no new string is created. This would occur if all the points of the string lie on the wireframe and intersection with wireframes is turned on.

Related topics and activities

  * [project-string-onto-wf](<project-string-onto-wf.md>)

  * [project-string-onto-wf-in-view](<project-string-onto-wf-in-view.md>)

  * [project-string-onto-wf-limit](<project-string-onto-wf-limit.md>)

  * [project-string-onto-wfs](<project-string-onto-wfs.md>)

  * [project-to-view-plane](<project-to-view-plane.md>)

  * [set-face-angle ("fng")](<set-face-angle.md>)