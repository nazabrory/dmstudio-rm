# Options: 3D Initial States

To access this screen:

  * On the [Options](<Options.md>) screen, expand the 3D tab and select **Initial States**.

Control how 3D windows appear initially after creation, including the primary 3D view on startup. These settings apply to all future projects created in your application. 

Per-window settings can also be set, providing the 3D window was created as an **[independent](<Independent_3D_Windows.md>)** type.

These options can also be changed after startup using either the [3D View](<Ribbon_View_VR.md>) ribbon or the [Environment Settings](<../VR_Help/EnvironmentalSettings_Dialog.md>) screen. In this situation, settings are stored per project.

Option | Description  
---|---  
**Perspective mode** |  If **checked** , 3D window data is displayed to support vanishing point perspective. If **unchecked** , 3D window data is displayed in an isometric manner, without perspective support. See [Perspective and Orthogonal Views](<../VR_Help/Perpective%20and%20Orthogonal%20Modes.md>).  
View direction |  Set the initial view direction for 3D windows using one of the preset view types listed.

  * _Plan_ view orthogonally to a flat, horizontal plane.
  * _N-S_ view orthogonally to a North-South plane.
  * _S-N_
  * _E-W_
  * _W-E_
  * _3D_ view orthogonally to the current default section.

  
**Lock view to section** |  If **checked** , the 3D window view direction is locked to a section plane (see above) after creation, by default. Windows can be unlocked using the **3D View** ribbon or equivalent options. If **unchecked** , 3D view directions are not locked and can be adjusted interactively. See [Section Locking](<Section_Locking.md>) and [lock-view ("lvw")](<../command_help/lock-view.md>).  
**Grid** |  Determine the type of default grid that displayed by 3D window by default. This can be: 

  * _< none>_
  * A Section grid
  * A grid that snaps to the 3D Hull of all loaded data objects. 
  * The current grid's Default Template. 

Note: any grid can be [set to be the system default](<TheGridsFolder.md>).  
Indicators |  Decide which 3D indicators display when 3D windows are created, from the following non-exclusive options:

  * [Axis Indicator](<../VR_Help/Axis_Indicator.md>)
  * [Axis Controller](<../VR_Help/axes%20control%20tool%20overview.md>)
  * [View Controller](<../VR_Help/view_controller.md>)

  
**Background color** | Select either a **Single** or **Gradient** back-fill for new 3D windows.   
Clipping |   
**Front** , **Back** |  Adjust the global clipping planes for clipping, which determine the 'corridor' in which data is visible within a 3D window, as a distance from the 3D camera in an orthogonal direction.  
**Bias additional Clipping planes by** | Move the global clipping plane by a small amount to overcome visibility issues with data drawn on a section plane.  
Use polygon offset |  If **checked** , strings which have been digitized by snapping to a wireframe or section plane are slightly offset (default 'ticked'). This can prevent the digitized data from being partially 'hidden' by the wireframe or section plane surface. If **unchecked** , digitized strings that are coincident with wireframe data are not adjusted, but may be unexpectedly obscured.  
  
Related topics and activities:

  * [Options: 3D ](<Options_InTouch.md>)
  * [Options: 3D General](<Options_InTouch-General.md>)

  * [3D Options: Stereo](<Options_InTouch-Stereo.md>)

  * [Options: 3D Printing](<Options_InTouch-Printing.md>)

  * [Viewing Data](<Interface_Viewing%20Data.md>)

  * [3D Design](<../VR_Help/Designing_in_VR.md>)

  * [3D Window Visualization](<../VR_Help/VR_Introduction.md>)

  * [External 3D Views](<External_3D_Windows.md>)

  * [Independent 3D Windows](<Independent_3D_Windows.md>)

  * [Clipping 3D Data](<../VR_Help/Clipping-Data.md>)

  * [Windows, Sheets, Projections and Overlays](<concept_views%20sheets%20overlays.md>)

  * [The View Hierarchy](<View%20Hierarchy.md>)

  * [3D Window Templates](<3D_Window_Templates.md>)

  * [3D Window Drawing Units](<3D%20Window%20Drawing%20Units.md>)