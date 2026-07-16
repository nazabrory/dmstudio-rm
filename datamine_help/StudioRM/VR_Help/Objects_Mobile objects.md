# Mobile Simulation Objects

Object models must be added to the **VR Object Type** folder for the active 3D window (In the Sheets control bar) before they can be added to the view. For more information on adding object types see [VR Object Types](<Object_Adding_an_object_type.md>), [VR Objects and Simulations](<Objects_Simulation%20objects.md>) and [Stationary VR Object types](<Objects_Stationary%20objects.md>).

Before placing an object in the world view, review the object properties by double-clicking the object name in the **VR Object Types** folder. The object Name and Model file are displayed.

## Mobile Object Types

For mobile objects, which can be navigated over an undulating surface, the Force upright option is usually switched off. If the object should remain upright when placed or moving on a surface, turn this option on. 

In the Movement box, set the Maximum speed (meters or feet per second), Maximum acceleration, Maximum turn rate (arc distance per second), Maximum climb angle (degrees) and Maximum roll angle (degrees) of the vehicle.

The Viewpoint Offset controls the Inside View or driving position relative to the origin of the object model. The origin is normally located at the center of the base of the object, so to raise the driver's view position, increase the Z offset. To move the inside view position forward, increase the Y offset. To move the inside view position to the side of the vehicle, increase (right) or decrease (left) the X offset.

The other object properties (Sound and Lights) are optional.

To drive a hovering VR object across a terrain surface:

  1. Define a new object type. See [VR Object Types](<Object_Adding_an_object_type.md>).

  2. Place a new object anywhere on a 3D surface:
     1. Click **OK**.

A new item appears in the **VR Object Types** folder of the **Sheets** control bar.

     2. Right-click the new object type entry and select **Place Objects**.
     3. Left click to 'drop' the object onto the loaded 3D surface.

The 3D object appears in the **3D** view.

     4. Click **ESC** to exit object placement mode.

**Note** : you can also right-click to snap the object to any existing data position, depending on your snap settings.

  3. Right-click the new object item in the **Sheets** control bar and choose **Inside View**.

The camera zooms to a position 'inside' the 3D object. 

  4. Right-click the new VR object again and choose **Control**.

Use the navigational controls to drive the object across the surface.

Related topics and activities

  * [Placing objects](<Objects_Placing_objects_on_surfaces.md>)

  * [Simulation objects](<Objects_Simulation%20objects.md>)

  * [Adding lights to objects](<Objects_Object%20lights.md>)

  * [ Adding sound to objects](<Objects_Object%20sounds.md>)