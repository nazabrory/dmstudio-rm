# Record to File

To display this screen:

  * **Report** ribbon **> > Animate >> Record**.

Use this screen to simultaneously play back a [Sequence Animations](<Sequencing.md>) and record it to a video file for sharing with others.

Recording a simulation creates an independent video output file on your file system. It doesn't store any other information about the project being recorded other than that which is displayed within the confines of the movie boundary.

## Video Types

You can record video in one of the following formats:

  * WMV (Windows Media Video): a compressed video file format for several proprietary codecs developed by Microsoft. The original codec, known as WMV, was originally designed for Internet streaming applications, as a competitor to RealVideo. The other codecs, such as WMV Screen and WMV Image, cater for specialized content. Through standardization from the Society of Motion Picture and Television Engineers (SMPTE), WMV has gained adoption for physical-delivery formats such as HD DVD and Blu-ray Disc.  
  
WMV is the recommended format for storing 3D window animations, particularly in combination with the [Video for broadband film content (1500 Kbps total)] Video Compressor option (see below) which offers fast generation speed, and compact video files.
  * AVI (Audio Video Interleave): a multimedia container format introduced by Microsoft in November 1992 as part of its Video for Windows technology. AVI files can contain both audio and video data in a standard container that allows synchronous audio-with-video playback. Like DVDs, AVI files support multiple streaming audio and video, although these features are seldom used.

## Tips for recording

  * In most situations, the selection of the WMV format, with a suitable compression algorithm, will produce video that is suitable in terms of file size and playback quality. Windows .wmv files are much smaller in size. Remember that with most file reduction packages, the resulting output may be of a lower quality than the original source, and a balance will need to be struck between output quality and file size.

  * The uncompressed .avi option produces very large files. Use a converter to convert it to something smaller.

  * The bigger the window, the slower the export process will be. Keep the 3D window to the smallest size necessary for output.

  * Frame rate selection is important; try to maintain the lowest acceptable frame-rate for the simulation being recorded. This is best achieved by experimentation and playback.

  * The record function will try to output the requested number of frames every 'simulated' second. Try setting all your movements using alignment strings, and then specifying playback at 0.1 of real time, to get 10 times as many frames recorded a second.

  * If you want to capture the full application interface (thus enabling the display of other data windows), hold down the <SHIFT> and <CTRL> keys when starting your recording.

## Auto-Spin and Auto-Roll

Hold down the <SHIFT> key and use the left or right arrows to start an automatic rotation of the contents of the 3D window. Subsequent presses of the relevant direction key can be used to speed up or slow down the rotation, or stop it and reverse direction. Similarly, you can use the up and down arrows to instigate an automatic roll around the horizontal axis.

Automatic spinning and rolling can be performed during the playback of a simulation.

## Create a Video

To configure record video capture properties:

  1. Prepare your loaded and displayed 3D data ready for sequence animation playback. See [Sequence Animations](<Sequencing.md>).

  2. Display the **Record to File** screen.

  3. Choose the video File Type (see above).

  4. Enter a Filename and path, or use the browse button to do the same.

  5. Specify the Frames per second. This is the amount of frames per second in the recorded output. 

Note: This setting can have a significant effect on file size.

  6. Pick a **Video Compressor**. You should compress your video output to avoid unnecessarily large files. All compression codecs available to the local PC are listed.

  7. By default, simulations are recorded to file without sound. If you have a suitable audio device enabled on your system, you can select an **Audio Source** from the list provided. If the selected device supports source audio compression, you will be able to select an **Audio Compressor** codec from the list below. By default, interleaved or overlaid audio content is uncompressed.

Note: An Audio Source must be specified for WMV file formats.

  8. Click OK to begin recording.

  9. **Report** ribbon **> > Animate >> Play** or display the **Sequence Control** screen to manually engineer a sequence playback.

Note: At this point, recording mode is active, so any changes to the display in the target 3D window are recorded.

  10. Click **Record** again, or click **Stop** when you have finished making 3D window updates.

Your output video file is created in the location specified.

Related topics and activities:

  * [Sequence Animations](<Sequencing.md>)

  * [Sequence Control](<Sequence%20Control%20Dialog.md>)

  * [Create a Flythrough](<Simulation_Creating%20a%20Flythrough.md>)

  * [Lighting](<Environment_Lighting.md>)

  * [Directional Light Source](<environment_adding%20more%20light%20sources.md>)

  * [Fog](<Environment_Fog.md>)

  * [3D Sky Settings](<Environment_Sky.md>)

  * [Getting the Right 3D Effect](<Environment_Getting%20the%20right%20effect.md>)

  * [VR Objects and Simulations](<Objects_Simulation%20objects.md>)

  * [Stationary VR Object types](<Objects_Stationary%20objects.md>)

  * [Mobile Simulation Objects](<Objects_Mobile%20objects.md>)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Creating a flythrough](<Simulation_Creating%20a%20Flythrough.md>)