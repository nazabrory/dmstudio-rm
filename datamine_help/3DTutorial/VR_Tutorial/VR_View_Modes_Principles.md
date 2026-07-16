![](../HeaderCell.jpg) |  VR View Modes An overview of the VR window's view modes and controls.  
---|---  
  
# VR View Modes

![](../Images/RM_shells2a.png)

The actions of the [Navigation Controls](<Navigation_Controls.md>) in the 3D window are dictated by the type of view mode that is operational at the time. This topic outlines the various options and methods for viewing data.

Viewing options are controlled by a combination of modes and controls;

  * a view mode is a particular viewing state or setting that is applied to the 3D window view; all subsequent view controls will honor the currently active mode. For example, if in Look At mode, the Spin View control can be used to rotate the view around a particular point; whereas in Floating View mode, the view cannot be spun in this way.

  * a view control is a command that will perform an action, such as setting or interactively changing the view direction. For example, the Perspective View toggle will automatically switch between a vanishing-point perspective and isometric view of the data.

## Using a Wheel Mouse

If you have a Wheel Mouse, the wheel can be used in certain viewing modes to access the following functions:

  * Zoom In - rotate wheel forward

  * Zoom Out - rotate wheel backwards

![note.gif \(1017 bytes\)](../Images/note.gif) | 

  * Zooming with the Mouse Wheel will zoom around the cursor position.
  * In the perspective view, the view zooms by moving the camera. If a LookAt point has been defined, then the speed of moving is based on the distance to the viewpoint. If the cursor is away from the view centre, then the LookAt point is moved horizontally or vertically (relative to the viewport) to keep it in the new view centre.

  
---|---  
  
### Hints:

  * If you get disoriented, activate the View ribbon and select Align View or Lock View to return to a view that is orthogonal to the current section, then, if you are still lost, choose an object or viewpoint from the Viewpoint list to get you back to familiar territory.

  * When navigating around an immersive world, use the Look At command to move towards and around an object of interest. Once active, you can rotate the entire 3D scene quickly around the selected point, using the Rotate View command.

  * Use the Viewpoint list on the View ribbon to quickly move from one object or view position to another.

  * Use multiple windows (either split and/or external views) to allow you to retain each view at a particular point of interest. You can even lock one of these views to prevent any inadvertent movement during visualization or digitizing.

  * You can select data in any window, even external 3D views. Similarly, you can digitize into any view, or orient it independently of other views. There is no theoretical limit to the number of views you can have, although a large number of views on a low-power system may cause some performance slowdown, particularly with large or numerous data objects in memory.

  * When saving viewpoints, use a descriptive name to help you select the right viewpoint while navigating.

## Changing the View during Simulation Playback

Different view modes and controls can be accessed even during play back of a simulation, for example, you can:

  * change the Inside View in a vehicle to find a better driving position

  * keep your view fixed on a moving object by choosing the Look At command and click on a moving object

  * when inside a simulation object, keep your view fixed on another object, using a similar approach to above. The "Look At object" may also be moving in the simulation.

Setting Auto-Spin and Auto-Roll

Hold down the <Shift> key and use the left or right arrows to start an automatic rotation of the contents of the 3D window. Subsequent presses of the relevant direction key can be used to speed up/slow down the rotation, or stop it and reverse direction. Similarly, you can use the up and down arrows to instigate an automatic roll.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Navigational Controls](<Navigation_Controls.md>)