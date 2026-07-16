# Transform Coordinates Automation

Transform a spatial data file's coordinates from one system to another using industry-standard coordinate systems, or your own conversion logic.

The **Transform Coordinates** console handles numerous types of coordinate representations, including cartographic and geodetic transformations. You can also automate this command.

Standard automations can be automated using the syntax:
    
    
    oDmApp.ParseCommand("transform-coordinates 
    InFile=[Full path to source file];
    
    
    OutFile=[Full path to created file];
    
    
    InCRS=[Source file CRS reference];
    
    
    OutCRS=[Target file CRS reference];
    
    
    X=[X Coordinate Field];
    
    
    Y=[Y Coordinate Field];
    
    
    Z=[Z Coordinate Field]");

For example:
    
    
    oDmApp.ParseCommand("transform-coordinates 
    InFile=C:\\Database\\MyProject\\MyStrings.dm;OutFile=C:\\Database\\MyProject\\Transformed_Strings;InCRS=G:32766;OutCRS=G:32761;X=XP;Y=YP;Z=ZP");

In the above case, oDmApp is a Studio Application object, often instantiated as an ActiveX control (but can also be referenced by the parent window handle, such as **window.external;** in Javascript.

**Note** : it is not possible to automate a **[custom](<Transform-Coordinates-Custom.md>)** transformation.

Related topics and activities

  * [Transform Coordinates](<Transform_Coordinates_Dialog.md>)

  * [Standard Coordinate Transformation](<Transform-Coordinates-Standard.md>)

  * [Custom Coordinate Transformation](<Transform-Coordinates-Custom.md>)

  * [Coordinate Systems](<Coordinate%20Systems%20Concept.md>)
  * [Coordinate System Selection](<CRSBrowserDlg.md>)