# Reposition SiroTIFF

To access this screen:

  * Use the quick key combination "rst".

  * Using the **[command line](<Command_Toolbar.md>)** , enter "reposition-sirotiff".

  * On the **[Find Command](<findcommand.md>)** screen, highlight **reposition-sirotiff** and click **Run**.

Important: Sirovision must be installed on the host system to use this screen.

Because it is not always possible to georeference Sirotiff objects at the time of creation, you can manually georeference the object using other loaded data items as a reference. This task is handled by the Reposition SiroTIFF screen.

Note: You can only perform a rotation around the Z-axis with this function - if any combination of edits are performed that require rotation around the X or Y axis, you are informed that this is not possible until the file is reloaded or refreshed.

This screen runs alongside other functionality in your application. Views may still be manipulated, and other commands and functionality used as normal during the SiroTiff repositioning process.

When the dialog is started, you are prompted to select a SiroTiff wireframe. This is done interactively in 3D views by clicking the cursor on the required wireframe. If the selected wireframe is not a SiroTiff file, you will be prompted to reselect.

You can only perform a rotation around the Z-axis with this function \- if any combination of edits are performed that require rotation around the X or Y axis, you will be informed that this is not possible until the file is reloaded or refreshed.

Once the SiroTiff wireframe has been successfully selected, the controls in the Repositioning part of the screen are enabled; these can be used to carry out basic repositioning tasks for the wireframe. Alternatively, existing controls and commands and may be used to reposition the wireframe.

Note: If you are translating a SiroTIFF wireframe by a significant virtual distance, it is possible the rounding operations within the translation process may cause the texture to become temporarily distorted. If this happens, it can be easily rectified by right-clicking the 3D icon in the [Sheets](<Sheets%20Control%20Bar%20Overview.md>) project control bar and selecting Redraw All.

The following controls are available:

  * Choose New Reference Point Click the wireframe in the 3D View to specify the new reference position. The initial point is the location on the wireframe clicked during SiroTiff selection. This may be changed at any time.

  * Move To Reposition the SiroTiff so that the **Reference Point** aligns with a specific 3D coordinate. There are 2 ways to set the position to move to:

    * The coordinates of the new location may be explicitly entered. Click **Apply** to update the screen.

    * The new location can be picked in 3D which will apply the move automatically.

Note: If you are translating a SiroTIFF wireframe by a significant virtual distance, it is possible the rounding operations within the translation process may cause the texture to become distorted. If this happens, it can be easily rectified by right-clicking the 3D icon in the [Sheets](<Sheets%20Control%20Bar%20Overview.md>) project control bar and selecting Redraw All.

  * Move By Allows the SiroTiff position to be moved incrementally by fixed amounts along the major axes. The required displacement may then be entered and applied. To allow multiple corrections, the screen remain in "Move By" mode until the **Move By** button is toggled off, or another mode is selected.

  * Rotate By Allows the SiroTiff position to be rotated incrementally around the major axes. The centre of rotation is the previous specified Reference Point. The required rotation may then be entered (in degrees) and applied. This rotation mode remains active until switched off, or another mode is selected.

  * Save New Position Write the repositioned Sirotiff data back to the original file.

Related topics and activities:

  * [reposition-sirotiff](<../command_help/reposition-sirotiff.md>)