# VR Object Types

**Object types** are categories of object to be displayed in the active 3D window. You will need to create an object type before individual instances of an object can be added to a 3D window.

To add an object type:

  1. Display the **Sheets** control bar. This is typically found in your Home menu, although this differs between products.

  2. Load a surface to act as the 'ground' for your object. A topography would work well.

  3. Enable [perspective mode](<Perpective%20and%20Orthogonal%20Modes.md>). 

  4. Right-click the VR Object Types folder and choose New.

  5. On the Object Type Properties screen, add a **Name**.

  6. Browse for a **Model**. This must a DirectX data file (.x).

**Note** : several DirectX objects are installed with your application. You can find them in your installation folder's **VR** sub-folder.

  7. Optionally, browse for a **Sound** file. This can be any .wav format audio file. You can also set the rate at which the sound decays as the object becomes further away from the camera by setting its **Attenuation**. A higher value leads to a more obvious spatial change.

  8. If you want the object to be a **Light** source, **[set one up](<Objects_Object%20lights.md>)**.

  9. Type the hover height e.g. 10 (meters or feet) in the Z**Viewpoint Offset** box.

  10. Turning on the Force upright option will keep the view level (like a helicopter), turning this off causes the view position to pitch and roll in response to the surface below.

  11. Set a Maximum speed of '50' m/s, Acceleration of '3' m/s2, a Max. turn of '150' m, Max. climb of '80' degrees (near vertical wall) and a Max. roll of '80' degrees.

  12. Choose the type of Shading your object will have:

     * **Wireframe** show your object as a wireline view with no filled polygons.

     * **Flat** render each triangle of the wireframe with a solid colour texture.

     * **Smooth** smooth out the texture of the object across its surface.

  13. Place your object(s) into your 3D scene. See related topics, below for useful links.

Related topics and activities

  * [Placing Objects on Surfaces](<Objects_Placing_objects_on_surfaces.md>)

  * [Place a Group of VR Objects](<Objects_Placing%20a%20group%20of%20objects.md>)

  * [Stationary VR Object types](<Objects_Stationary%20objects.md>)

  * [VR Objects and Simulations](<Objects_Simulation%20objects.md>)

  * [Mobile Simulation Objects](<Objects_Mobile%20objects.md>)

  * [Add a VR Object Light](<Objects_Object%20lights.md>)

  * [Add Sound to VR Objects](<Objects_Object%20sounds.md>)