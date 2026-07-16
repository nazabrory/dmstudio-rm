![](../HeaderCell.gif) |  Tutorial Files List A list of files used in this tutorial.  
---|---  
  
# File Locations

Assuming a default installation, the location of sample files referenced by this tutorial is provided below.

  * C:\Database\DMTutorials\Data\VBOP\CAD

  * C:\Database\DMTutorials\Data\VBOP\Datamine

  * C:\Database\DMTutorials\Data\VBOP\Docs

  * C:\Database\DMTutorials\Data\VBOP\ODBC

  * C:\Database\DMTutorials\Data\VBOP\Pics

  * C:\Database\DMTutorials\Data\VBOP\Text

These folders contain a series of data-type-specific folders including amongst others, CAD files, native Datamine format files(*.dm), spreadsheet files and text files. Note that these folders contain many files, and that only the files listed in the table below are relevant to the Geological Modeling tutorial.

# File Names and Descriptions

The following table contains a list of the relevant files used in this tutorial. Each entry lists the existing Sample File Name, the suggested User File Name and a file Description. They are grouped according to the name of the folder in which the file is located.

Sample File Name |  **User File Name** |  **Description**  
---|---|---  
...\VBOP\CAD:  
_vb_stopo.dwg |  - |  CAD Polylines - topography contours  
_vb_ltopo.dxf |  - |  CAD Polylines - topography contours large area  
...\VBOP\Datamine:  
_ostopoi |  stopoi |  Strings - imported surface topography contours  
_ostopo |  stopo |  Strings - processed surface topography contours (_ostopoi with modified COLOUR values, conditioned with PROPER)  
_vb_assays |  - |  Drillhole Assays Table - drillhole assays table (hole identifier, interval start depth, interval end depth, gold grade [g/t], copper grade [%], rock density)  
_vb_collars |  dhcollar |  Drillhole Collars Table - drillhole collar coordinates table (hole identifier, collar coordinates, final depth, coordinate system, hole type, date)  
_vb_holes |  dholes |  Static Drillholes - desurveyed using HOLES3D from drillhole data tables (_vb_assays, _vb_collars, _vb_zones, _vb_lithology, _vb_surveys)  
_vb_holesc |  dholesc |  Static Drillholes - desurveyed and composited using COMPDH on key field ZONE (from uncomposited file _vb_holes)  
_vb_faultpt |  - |  Wireframe Points - faults' surfaces  
_vb_faulttr |  - |  Wireframe Triangles - faults' surfaces  
_vb_faults |  - |  Strings - faults model (vertical strings defining the boundaries of the fault surfaces)  
_vb_lithology |  - |  Drillhole Interval Table - drillhole rock types table (hole identifier, interval start depth, interval end depth, rock type name, rock type numeric code)  
_vb_min1st |  min1st |  Strings - ore body string model created by digitizing section perimeters around upper and lower mineralization zones (field ZONE) present in the static drillholes (_vb_holes).  
_vb_min2st |  min2st |  Strings - digitized ore body string model (_vb_min1st) with additional western and eastern extensions  
_vb_min3st |  min3st |  Strings - extended ore body string model (_vb_min2st) with additional Tag Strings  
_vb_minpt |  minpt |  Wireframe Points - ore body wireframe model created by string linking (_vb_minst)  
_vb_minst |  minst |  Strings - ore body string model created by digitizing section perimeters around upper and lower mineralization zones (field ZONE) present in the static drillholes (_vb_holes). Contains Tag Strings and all strings are conditioned.   
_vb_mintr |  mintr |  Wireframe Triangles - ore body wireframe model created by string linking (_vb_minst)  
_vb_modbound |  modbound |  Strings - modeling boundary (pair of perimeters) which coincides with the limits defined in the block modeling prototype (_vb_mprot)  
_vb_modlim |  - |  Strings - DTM creation limit (single perimeters)  
_vb_modopt |  modopt |  Block Model - combined waste+ore block model (_vb_modore) optimized using PROMOD on key field ZONE.  
_vb_modore |  modore |  Block Model - ore model created by filling the ore body wireframe model (_vbmintr/_vbminpt) using WIREFILL  
_vb_modprot |  modprot1, modprot2 |  Block Model - prototype  
_vb_modwo |  modwo |  Block Model - combined waste+ore block model using ADDMOD  
_vb_modwst |  modwst |  Block Model - waste model created by filling beneath the topography surface wireframe (_vb_stopotr/_vb_stopopt) using WIREFILL  
_vb_seisiinterp_ns5985 |  seisiinterp_ns5985 |  Strings - geological interpretation of the seismic profile image (_vb_Seismic_Section_NS_5985.bmp)  
_vb_stopo |  - |  Strings - imported and processed surface topography contours  
_vb_stopopt |  stopopt |  Wireframe Points - topography DTM created from topography contours (_vb_stopo)  
_vb_stopotr |  stopopt |  Wireframe Triangles - topography DTM created from topography contours (_vb_stopo)  
_vb_surveys |  - |  Drillhole Surveys Table - drillhole downhole surveys table  
_vb_viewdefs |  viewdefs |  Section Definition File - contains a set of plan, inclined and vertical section definitions used for viewing the geological modeling data (vertical sections correspond with sections in the geological string model _vb_minst)  
_vb_zones |  dhzones |  Drillhole Interval Table - drillhole mineralization zones table (hole identifier, interval start depth, interval end depth, mineralization zone numeric code)  
COMPS5 .dm |  COMPS5 .dm |  Drillholes file used in the Create Isoshells tutorial  
Start_End_Samples.mac |  Start_End_Samples.mac |  Macro used to create the upper and lower wireframes used in the Create Isoshells tutorial  
LOWERPT.dm |  - |  Sample lower wireframe points file  
LOWERTR.dm |  - |  Sample lower wireframe triangles file  
upperpt.dm |  - |  Sample upper wireframe points file  
uppertr.dm |  - |  Sample upper wireframe triangles file  
...\VBOP\Docs:  
_vb_holes_NLITH1.elg |  vb_holes_NLITH1 |  User Legend File - numeric rock code (field NLITH) color legend  
_vb_holes_NLITH2.elg |  vb_holes_NLITH2 |  User Legend File - numeric rock code (field NLITH) color legend patterns  
...\VBOP\ODBC:  
_vb_drillhole_data.xls |  - |  Drillhole Dat Tables - collars, downhole surveys, assays, lithology, mineralization zones tables; import file (Excel spreadsheet)  
...\VBOP\Pics:  
_vb_Seismic_Section_NS_5985.bmp |  - |  Image - seismic profile for NS section 5985.  
...\VBOP\Text:  
_vb_assays_comma.txt |  - |  Drillhole Assays Table - drillhole assays table (hole identifier, interval 'from' distance, interval 'to' distance, Au (gold) grade in gt/t, Cu (copper) grade in %, rock density in kg/m3) (*.txt format file, comma delimited)  
_vb_collars_space.txt |  - |  Drillhole Collars Table - drillhole collar coordinates table (hole identifier, collar coordinates, final depth, coordinate system, hole type, date) (*.txt format file, space delimited)  
_vb_lithology_comma.txt |  - |  Drillhole Lithology Table - drillhole rock type table (hole identifier, interval 'from' distance, interval 'to' distance,rock description, rock type numeric zone code) (*.txt format file, comma delimited)  
_vb_surveys_comma.txt |  - |  Drillhole Surveys Table - drillhole downhole surveys type table (hole identifier, 'at' distance down the hole, hole bearing [degrees, positive down], hole dip[degres]) (*.txt format file, comma delimited)  
_vb_zones_comma.txt |  - |  Drillhole Zones Table - drillhole mineralization zones table (hole identifier, interval 'from' distance, interval 'to' distance,mineralization zone code - numeric) (*.txt format file, comma delimited)  
![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [The Geological Modeling Data Set](<The_Geological_Modeling_Data_Set.md>)