# Grid Properties: Advanced Options

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

To access this screen:

  * Display the [**Grid Properties**](<grid%20properties%20dialog.md>) screen and select the **Advanced Options** tab.

Define advanced formatting options for 3D grids, the coordinate system used, whether the grid will extend to the boundaries of the screen, or a specified distance, as well as options for grid labelling.

## Local Coordinate Grids

You can define a local coordinate system in one of two ways. You choose the method using the Track to section check box on this screen for section grid types only:

  * Define the local and world coordinate common point manually

Define two sets of XYZ positions: the first is the position in space to locate your world origin, for example, 0, 0, 0, and the second set of digits dictates the distance and direction from this point that becomes the local origin. This is not the same as setting a new world origin.

This method is used if Track to section is unchecked.

  * Inherit the local coordinates from the current section definition

With this approach, the grid is tied to the default or active section. The grid will then always display local coordinates where the actual values will depend on the Local XYZ values specified (default 0, 0, 0).

With this method, local coordinates are inherited from the current section definition, so you won't need to define the common World point coordinate, or the Azimuth and **Dip** settings

This method is used if Track to section is checked.

The World and Local settings are just used to specify the coordinates of a known point in world coordinates and local coordinates. For example, a collar might be at (1000,2000,250) in world coordinates, and at (0,0,0) in local coordinates, which would result in the grid origin being at the collar position. Or, if the local coordinates for the collar were (0,0,250) then the grid origin would be 250 units below the collar position. For more information on local and world coordinate systems, see [Understanding Coordinate Systems](<Coordinate%20Systems%20Concept.md>).

When World and Local origin points (the 'common point' defining the positional relationship between world and local origins) are defined and you are not using the Track to section option, you can configure details about how the local coordinate system is calculated, using **Scale 1:N** , **Azimuth** and **Dip** settings.

## Screen Options

The following options are available on this screen:

Option | Description  
---|---  
Use Local Coordinates |  Grids can be defined using world or local coordinate systems; a world coordinate system is one that has a definitive origin that does not relate to any particular object in memory - in this situation, all grid values are relative to a common origin.  If checked, a local coordinate system is used instead, which allows you to determine another point to be used as an origin - this is in relation to the world coordinate origin. See "Local Coordinate Grids" above, for more information.  
Track to Section |  Only available if **Use Local Coordinates** is checked. This setting determines how a local grid coordinate system is applied using the **Local Origin** options, which determine where the _local_ origin (0,0,0) for a grid is positioned on the section.:

  * _Manual_ Choose your own **Local** and **Scale 1:N** values (see below).
  * Bottom Center
  * Bottom Left
  * Bottom Right
  * Top Center
  * Top Left
  * Top Right
  * _Center_

  
Scale 1:N |  Set the coordinate system scale. For example, if the map was at a scale of 1:1000, this would mean that 1 unit on the grid would represent 1000 units in the world. Note that the interval, local point and constraints settings are all in local coordinates so if you change the scale you may want to change these settings also.  
Azimuth  | Set the azimuth of the local coordinate system grid, in relation to the world system orientation.   
Dip | Set the dip of the local coordinate system.  
Minimum XYZ |  Define minimum grid constraints in each major axis. This restricts the extents of the grid periphery for 3D hulls, or 'snap' the grid to fit neatly around any visual object in memory. These options are only available if a 3D Hull grid type is being defined, and the Snap to hull option is unchecked.  
Maximum XYZ | Set the upper bounds for grids in each axis.  
Snap to hull |  If checked, you can choose to wrap the grid around all of your data, or a specific data object using the drop-down list provided.  All loaded 3D objects are listed.  
Prefix | Set a custom prefix for label text.  
Suffix | Set a custom suffix for grid labels.  
  
Related topics and activities:

  * [**Grid Properties**](<grid%20properties%20dialog.md>)

  * [Grid Properties: Advanced Options](<grid%20properties%20dialog.md>)

  * [Grid Properties: More Line Formatting](<VR_Grids_More_Line_Formatting.md>)

  * [Grid Properties: Templates](<VR_Grids_Templates.md>)