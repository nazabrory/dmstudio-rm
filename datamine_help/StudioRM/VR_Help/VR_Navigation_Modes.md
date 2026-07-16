# 3D View Modes and Controls

The actions of the [Navigational Controls](<VR_Navigational_Controls.md>) in the 3D window are dictated by the type of view mode that is operational at the time. This topic outlines the various options and methods for viewing data in the 3D window.

Viewing options are controlled by a combination of modes and controls;

  * a view mode is a particular viewing state or setting that is applied to the 3D window view; all subsequent view controls will honor the currently active mode. For example, if in Look At mode, the Spin View control can be used to rotate the view around a particular point; whereas in Floating View mode, the view cannot be spun in this way.

  * a view control is a command that will perform an action, such as setting or interactively changing the view direction. For example, the Perspective View toggle will automatically switch between a vanishing-point perspective and isometric view of the data.

## Navigating in an Orthogonal Projection

Navigating in a parallel projection can feel counter-intuitive to those used to perspective projections. The main reason for this is that as the 'camera' moves forwards, objects in the view do not appear to get closer, as they do not get any bigger. The only indication of forward motion is usually when objects start getting clipped by the views front clipping plane. This can be a problem if you are trying to use the free-flight tools, as any subsequent rotations around the camera may be confusing. It is recommended, therefore, you only use the free flight tools for panning whilst in this mode. All other navigation should be done using either preset viewpoints, or [Look At](<vr_navigation_look_at.md>) mode.

In perspective projections, there are 2 primary options for making an object look bigger on the screen: either move the camera closer to it (move forwards), or reduce the field of view (apply zoom). Neither of these options are available in a parallel projection, so the Zoom to region button should be used instead. After selecting this button, the new viewing area should be outlined on the current view by using the left mouse button and dragging the bounding rectangle. Releasing the button will cause the camera to pan so that the rectangle is central, and alter the view width to fit the bounding rectangle. For convenience, the system will also place the Floating Viewpoint in the centre of the view, to make subsequent rotations easier. The depth of the Floating Viewpoint will either be on the first item intercepted in the middle of the view, or an average depth of objects in the view if no item is intercepted.

## Using a Mouse Wheel

If you have a mouse with a wheel, the wheel can be used in certain viewing modes to access the following functions:

  * Zoom In - rotate wheel forward

  * Zoom Out - rotate wheel backwards

Zooming with the Mouse Wheel will zoom around the cursor position.

In the [perspective view](<Perpective%20and%20Orthogonal%20Modes.md>), the view zooms by moving the camera. If a LookAt point has been defined, then the speed of moving is based on the distance to the viewpoint. If the cursor is away from the view centre, then the LookAt point is moved horizontally or vertically (relative to the viewport) to keep it in the new view centre

Tip: Before you zoom in using the mouse wheel, left or right-click any part of your 3D scene. Zooming will then be performed around this point.

### Tips:

  * If you get disoriented, choose Level View to return to a horizontal view, then, if you are still lost, choose an object or viewpoint from the Viewpoint list to get you back to familiar territory.

  * When navigating around an immersive world, use the Look At command to move towards and around an object of interest. Once active, you can rotate the entire VR scene quickly around the selected point, using the Rotate View command.

  * Use the View list on the **3D View** ribbon to quickly move from one object or view position to another.

  * When [saving viewpoints](<VR_Viewpoints.md>), use a descriptive name to help you select the right viewpoint while navigating.

## Changing the View during Animations

Different view modes and controls can be accessed even during play back of a simulation, for example, you can:

  * change the **Inside View** in a vehicle to find a better driving position

  * keep your view fixed on a moving object by choosing the **Look At** command and click on a moving object

  * when inside a simulation object, keep your view fixed on another object, using a similar approach to above. The "Look At object" may also be moving in the simulation.

## Auto View Spin

Hold down the <Shift> key and use the left or right arrows to start an automatic rotation of the contents of the 3D window. Subsequent presses of the relevant direction key can be used to speed up/slow down the rotation, or stop it and reverse direction. Similarly, you can use the up and down arrows to instigate an automatic roll.

Related topics and activities

  * [Viewpoints](<VR_Viewpoints.md>)

  * [3D Window Navigation](<VR_Navigational_Controls.md>)

  * [Perspective and Orthogonal Modes](<Perpective%20and%20Orthogonal%20Modes.md>)

  * [View From Outside](<VR_Navigation_Outside_View.md>)

  * [View From Inside](<VR_Navigation_Inside_View.md>)

  * [Look At](<vr_navigation_look_at.md>)