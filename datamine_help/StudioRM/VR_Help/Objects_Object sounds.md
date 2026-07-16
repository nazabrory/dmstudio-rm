# Add Sound to VR Objects

Sounds can be added to any **[VR Object type](<Object_Adding_an_object_type.md>)** and the intensity of the sound can be varied according to the distance between the current view position and the center of the object.

To add sound to a VR object:

  1. Right-click the object name in the VR Object Types folder in the Sheets window (active 3D window sub-folder) and click Properties. 

**Tip** : you can also double-click on the object type name.

  2. Choose the browse button adjacent to the Sound box and select a sound wave (.wav) file from disk.

  3. Type a sound attenuation distance in the Attenuation box. Sounds will have 100% intensity up to this distance from the object in all directions; the intensity then reduces, or attenuates, as you move away from the objects - or the object moves away from you. Typical settings for Attenuation vary between 1 and 10, but this does depend on the sound level used when recording the wave file. Attenuation uses an exponential decay function i.e. the sound level at a distance of 100 meters is very much less than half the sound level at 50 meters.

## Troubleshooting Sounds

The intensity of sound is a function of the Attenuation value and the distance from the object, but it is also controlled by the recording level in the sound wave file, and the volume settings used on your computer.

#### If the sound level is too high or low

  * You can increase or reduce the sound level of all objects with the volume controls.

  * You can increase or reduce the sound level of individual objects by using a lower attenuation value.

#### If you have no sound

Right click the VR object in the **Sheets** control bar and select **Inside View** \- this will place you at the origin of the sound source where the sound is at its theoretical maximum intensity. To increase the sound level away from the object, increase the Attenuation value.

Related topics and activities

  * [Adding Object Types](<Object_Adding_an_object_type.md>)

  * [Placing VR Objects](<Objects_Placing_objects_on_surfaces.md>)

  * [Adding lights to objects](<Objects_Object%20lights.md>)