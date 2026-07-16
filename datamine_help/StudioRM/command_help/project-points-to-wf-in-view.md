# project-points-to-wf-in-view ("pti")

See this command in the [**command table**](<COMMAND%20TABLE_P.md#project-points-to-wf-in-view>).

To access this command:

  * **Digitize** ribbon **> > Project >> Points to Wireframe in View**.

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "project-points-to-wf-in-view"

  * Use the quick key combination "pti".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **project-points-to-wf-in-view** and click **Run**.

## Command Overview

Project selected points onto a wireframe surface that is lying directly behind the selected points, along the line of sight.

For example, in the following image, 3 points are positioned above a wireframe surface, and were defined from a side (east-west) view.  
  
![](../Images/Project2View1.gif)

A plan view is selected:

![](../Images/Project2View2.gif)

The command is run and the view is set to 'east-west' (see [View Orientation](<../COMMON/View%20Orientation%20Dialog.md>)), revealing the following view:

![](../Images/Project2View3.gif)

**Tip** : Preselecting multiple points allows you to run this command for all selected points.

Command steps:

  1. Select a point (or points) in any view.

  2. Run the command.

Points are projected onto the nearest wireframe, away from the line of sight. 

**Note** : Wireframe surfaces should be positioned directly 'behind' the selected points for a valid surface to be found for projecting. 

Related topics and activities

  * [project-string-onto-wf-in-view ("ptd")](<project-string-onto-wf-in-view.md>)

  * [project-to-view-plane ("ptv")](<project-to-view-plane.md>)
  * [project-points-to-wireframe](<project-points-to-wf.md>)

  * [project-string-onto-wf-limit ("ptl")](<project-string-onto-wf-limit.md>)

  * [project-points-to-wf-angle](<project-points-to-wf-angle.md>)

  * [project-string-at-angle](<project-string-at-angle.md>)

  * [project-string-onto-wf](<project-string-onto-wf.md>)

  * [project-string-onto-wfs ("pstw")](<project-string-onto-wfs.md>)

  * [move-string-to-view ("mtv")](<move-string-to-view.md>)