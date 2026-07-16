# grid-dtms ("grd")

See this command in the [command table.](<COMMAND%20TABLE_G.md#grid-dtms>)

To access this command:

  * **Explicit** ribbon **> > DTM >> Make**.

## Command Overview

Create a grid of points to represent the average, minimum or maximum elevations of points belonging to multiple (and potentially overlapping) wireframe surfaces.

You can also use this command to output useful geotechnical information such as:

  * Vertical and horizontal thickness.

  * True thickness and true dip.

This information gives you a useful statistical analysis of the structure and can help guide downstream decisions on estimation, evaluation and even mining method.

Displays the [Create Grid DTMs](<../COMMON/grid%20dtms%20dialog.md>) screen.

### grid-dtms Automation

This command can be scripted. Here's an example of a Javascript function that generates a fully-constrained set of points. The supported parameters for this command are:
    
    
    // Azimuth=<decimal>              grid orientation azimuth
    
    
    // Dip=<decimal>                  grid orientation dip
    
    
    // ConX=<decimal>                 constraints origin x
    
    
    // ConY=<decimal>                 constraints origin y
    
    
    // ConZ=<decimal>                 constraints origin x
    
    
    // ConNumX=<integer>              constraints number of points x
    
    
    // ConNumY=<integer>              constraints number of points y
    
    
    // CopyWfData=[true|false]        write attributes copy wireframe
    
    
    // VertThick=<string>             write attributes vertical column
    
    
    // HoriThick=<string>             write attributes horizontal column
    
    
    // Truethick=<string>             write attributes true thickness column
    
    
    // DistMode=[first|average|last]  surface chosen distance
    
    
    // SpaceX=<decimal>               spacing x
    
    
    // SpeceX=<decimal>               spacing y

Snippet:
    
    
    oDmApp.ActiveProject.Data.LoadFile(ProjDir + "/topotr.dm");  
  
---  
      
    
    var objTopo = oDmApp.ActiveProject.Data.LastObjectAdded;  
      
    
    var vCommand = "grid-dtms ";  
      
    
    var vExtras =  
      
    
    "SpaceX=" + "5" +  
      
    
    "; SpaceY=" + "5" +  
      
    
    "; DistMode=" + "first" +  
      
    
    "; Azimuth=" + "0" +  
      
    
    "; Dip=" + "0" +  
      
    
    "; ConX=" + "6000" +  
      
    
    "; ConY=" + "5500" +  
      
    
    "; ConZ=" + "200" +  
      
    
    "; ConNumX=" + "20" +  
      
    
    "; ConNumY=" + "40" +  
      
    
    "; CopyWfData=" + "true" +  
      
    
    "; VertThick=" + "VERT" +  
      
    
    "; HoriThick=" + "HORI" +  
      
    
    "; TrueThick=" + "TRUE" +  
      
    
    ";"  
      
    
    oDmApp.ParseCommand(vCommand+vExtras);  
      
    
    var saveobj    = oDmApp.ActiveProject.Data.LastObjectAdded;  
      
    
    saveobj.SaveAsDatamineFile("Grid_Points1_Sanity", oDmApp.ActiveProject.ExtendedPrecision, true, "");  
  
Command steps:

  1. Ensure at least one wireframe object exists in memory.

  2. Run this command.

  3. The [Grid DTMs](<../COMMON/grid%20dtms%20dialog.md>) screen displays.

  4. To output the points to the current point object, choose Current Object. Otherwise, choose New Object, and add the name to the edit box.

  5. The **Grid Increment** specifies the grid point spacing in the **X** and **Y** axes. Points will only be created where they lie over an included surface.

  6. Where there are overlapping surfaces, both within a single wireframe, and/or between multiple wireframes, **Combine Elevations** chooses how the sample point elevation are calculated. This can either be the minimum elevation encountered, the maximum elevation, or an average of all the elevations encountered.

  7. The wireframe objects to be used to generate the point grid can be selected within the Objects list. These can either be selected by ticking the box next to the required wireframe name, or by using the pick arrow button, and then clicking on the wireframe in a 3D view.

**Tip** : Hover your cursor over a truncated object name to display it in full.

  8. Select OK to generate points data.

Related topics and activities

  * [Create Grid DTMs](<../COMMON/grid%20dtms%20dialog.md>)
  * [ Wireframe Update Hull Dialog](<../COMMON/wireframe%20surface%20merge%20dialog.md>)
  * [ Wireframe Decimate Dialog](<../COMMON/Wireframe%20Decimate%20Dialog.md>)