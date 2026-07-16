# Create a Flythrough

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

To create a flythrough animation in a 3D scene:

  1. Create a [**VR object type**](<Object_Type_Properties_Dialog.md>) that has a non-zero **Max. speed**.

Note: For a flythrough, it doesn't matter what 3D object type you pick as you will be hiding it before playback. Similarly, lights and sounds aren't important.

  2. Create [an alignment string](<Strings_Digitize%20and%20Edit.md>). This is the string along which your VR object will travel.

Note: You can also load a string. The advantage of creating one is that you know it relates to your other loaded and displayed data.

  3. Place a new VR object by right clicking the object type in the **Sheets** or **Project Data** control bar and selecting **Place Objects**.

  4. Left or right click to place the object anywhere in the view. This is the same as digitizing a point.

  5. Open the **[VR Object Properties](<Object_Properties_Dialog.md>)** screen by right clicking on the object in the Sheets or **Project Data** control bar and selecting Properties.

  6. Expand the Attach to String list and pick the alignment string you created earlier.

  7. In the **Objects** folder, right-click your updated VR object and select **Inside View**.

  8. Uncheck the VR object to hide it from the 3D scene.

  9. **Report** ribbon **> > Animate >> Play**.

Your object acts as a camera, rolling along the alignment string until it reaches the end.

Tip: You can adjust the 3D view dynamically during playback, and can even Look At other objects whilst you are moving (good for panning around points of interest).

Related topics and activities:

  * [Create a VR Object Type](<Object_Type_Properties_Dialog.md>)

  * [Create Alignment Strings](<Strings_Digitize%20and%20Edit.md>)

  * [Attach VR Objects to Strings](<Strings_Attaching%20objects%20to%20strings.md>)

  * [Project a String ](<Strings_Fitting%20a%20string%20to%20a%20surface.md>)

  * [Sequence Animations](<Sequencing.md>)

  * [Record to File](<simulation_recording.md>)

  * [Environmental Settings](<EnvironmentalSettings_Dialog.md>)

  * [VR Objects and Types](<VR-Objects-and-Types.md>)