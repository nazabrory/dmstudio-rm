![](../HeaderCell.jpg) |  Tutorial Files A list of files used throughout the Grade Estimation tutorial  
---|---  
  
# File Locations

Assuming that a default installation has been performed, all sample files referenced by this tutorial can be found under:

  * C:\Database\DMTutorials\Data\VBOP\Datamine

  * C:\Database\DMTutorials\Data\VBUG\Datamine

These folders contain a series of data-type-specific folders including amongst others, CAD files, spreadsheet files for importing and individual (native) Datamine files. Please note that these folders contain a wide range of files and that only the files listed in the table below are relevant to the grade estimation tutorial.

# File Names and Descriptions

The following table contains a list of the relevant files used in this tutorial. Each entry lists the existing Sample File Name, the suggested User File Name and a file Description. They are grouped according to the name of the folder in which the file is located.

Sample File Name |  **User File Name** |  **Description**  
---|---|---  
...\VBOP\Datamine:  
_2dblks |  - |  Strings - 2D panel outlines (mining blocks) used in panel estimation  
_2delp1pt / _2delp1tr |  2delp1pt / 2delp1tr |  Wireframe points/triangles - Sample search ellipse for 2D soil sampling  
_2depar1 |  2depar1 |  Estimation Parameters - 2D (NN, IPD, OK; no zonal control)(soil sampling grade estimates)  
_2depar2 |  - |  Estimation Parameters - 2D (NN, IPD and OK; zonal control)(soil sampling grade estimates)  
_2depar3 |  2depar3 |  Estimation Parameters - 2D (NN, IPD, OK and SK; zonal control)(soil sampling grade estimates)  
_2depar4 |  2depar4 |  Estimation Parameters - 2D (IK; zonal control)(soil sampling grade estimates)  
_2dgmod1 |  2dgmod1 |  Block Model - 2D (soils sampling AU grade estimates using IPD, no zonal control)  
_2dgmod2 |  2dgmod2 |  Block Model - 2D (soils sampling AU grade estimates using IPD and OK; zonal control field ANOM)  
_2dgmod3 |  2dgmod3 |  Block Model - 2D (soils sampling AU grade estimates using IPD, OK and SK; zonal control field ANOM)  
_2dgmod4 |  2dgmod4 |  Block Model - 2D (soils sampling AU grade estimates using IK; zonal control field ANOM)  
_2dpres1 |  2dpres1 |  Table - panel estimation results file  
_2dpmod1 |  - |  Block Model - 2D 40x40x10m prototype block model  
_2dres1 |  geres1 |  Results table - evaluation results by category for the 40x40m grade block model  
_2dspar1 |  2dspar1 |  Search Parameters - 2D (soil sampling grade estimates)  
_2dvpar1 |  2dvpar1 |  Variogram Model Parameters - 2D (soil sampling grade estimates)  
_2dvpar2 |  - |  Variogram Model Parameters - 2D (IK of mineralization zones, field ANOM)  
_2dxvs1 |  2dxvs |  Table - Cross validation results for 2D soil sampling estimation parameters  
_2dzmod1 |  2dzmod1 |  Block Model - 2D (soils sampling mineralization zones, field ANOM)  
_ostopo |  - |  Strings - surface topography contours  
_srfsamp |  - |  Points – Soil sampling (grades: Au [ppb], Cu [ppm]; Z - elevation)  
...\VBUG\Datamine:  
_3depar1 |  3depar1 |  Estimation Parameters - 3D underground ore body(grade fields CU, AG for ZONE =1 only, zonal control field ZONE)  
_3dspar1 |  3dspar1 |  Search Parameters - 3D underground ore body  
_caf5so |  - |  Strings - cut-and-fill stoping outlines (mining blocks) for -255m level  
_geres2 |  geres2 |  Results table - evaluation results by category for the '_caf5so' cut-and-fill stoping outlines  
_geres3 |  geres3 |  Results table - evaluation results by category for the '_uoretr / _uorept' ore body wireframe  
_geres4 |  geres4 |  Cut-off grades results table - evaluation of the ore body block model '_ubm5g' at 2g/t Au grade intervals  
_qqouAU |  qqouAU |  Table - QQ output for field AU (5x5x5m block model cells vs 5m composited drillholes)  
_qqplAU |  qqplAU |  Plot - QQ plot for field AU (5x5x5m block model cells vs 5m composited drillholes)  
_ubm5cat |  ubm5cat |  Block Model - 3D underground ore body (5x5x5m regular celled grade model; additional informal resource classification field CAT)  
_ubm5g |  3dbm5g |  Block Model - 3D underground ore body (5x5x5m regular celled grade model; zonal control using field ZONE)  
_ubm5z |  - |  Block Model - 3D underground ore body (5x5x5m regular celled mineralization zones model; zone field ZONE)  
_ubmlim |  - |  Strings - 3D underground block model prototype limits  
_ubmm |  - |  Block Model - 3D underground mining model i.e. grade model with 15m waste envelope (5x5x5m regular celled mineralization zones model; zone field ZONE)  
_ubmz |  - |  Block Model - 3D underground ore body (10x10x10m parent celled mineralization zones model; zone field ZONE)  
_udhz |  - |  Drillholes - (Density, grades: Au, Cu, Co, Ag, zone field ZONE; not composited)  
_udhz5c |  - |  Drillholes - (Density, grades: Au, Cu, Co, Ag, zone field ZONE; composited on 5m intervals)  
_uepe |  - |  Estimation Parameters - 3D  
_ueps |  - |  Search Parameters - 3D  
_uepv |  - |  Variogram Model Parameters - 3D  
_uoretr / _uorept |  - |  Wireframe traingles and points - underground ore body consisting of three zones  
  
![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Tutorial Exercises List](<tutorial_exercises.md>)