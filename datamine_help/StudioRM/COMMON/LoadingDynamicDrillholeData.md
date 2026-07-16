# Dynamic Drillhole Data

Your application supports two processes for creating and displaying drillholes. The first is the **static** method which uses the HOLES3D process and the second is the **dynamic** method which creates drillholes from data 'on-the-fly'. This topic discusses the requirements and options for creating dynamic drillholes.

Note: This process is utilized in your product by [Drillhole Importer](<DrillholeImporter-screen.md>). This tool is the recommended method for connecting to component drillhole database tables and ensure your modelling campaign uses the latest data.

The principal difference between static and dynamic drillholes is that static drillholes are stored as a desurveyed drillhole file, typically generated using a process. Dynamic drillholes use component data tables in memory (from any data source) to create drillholes in memory. Your choice will ultimately depend on how your exploration or production data is presented to you.

Tip: Use [**MineTrust**](<../MineTrust/MineTrust-Aware-Projects.md>) to ensure you always have the latest field data available for your modelling, estimation and blast layout projects.

## Data for Desurveying

Note: Use [Drillhole Importer](<DrillholeImporter-screen.md>) to quickly and easily manage dynamic drillhole data and create reusable data connections.

The format of the source data is not important provided there is a driver available to load the data into memory. The desurveying algorithm requires certain data as a minimum before it can create drillhole trace and sample composites. 

The following drillhole tables can be used to generate holes:

  * Collars \- required; contains drillhole XYZ collar coordinate, coordinate system, coordination and drilled date data

  * Surveys \- required; contains drillhole survey depth, survey bearing and dip data

  * Assays \- required; sample interval start and end depth, mineral grade or quality data; rock density data

  * Lithology \- required; sample interval start and end depth, lithology codes, short and long descriptions; rock density data

  * Interval log(s) \- interval start and end depth; interval data e.g. mineralized zone identifiers, rock mass rating values

  * Depth log(s) \- depth; point measurement data e.g. geophysical survey data, other download log data.

**Note** : If there is no survey table and there is no Azimuth and Inclination in the collars table, the desurvey algorithm will create vertical hole traces.

## Gaps, Overlaps and Duplicates

Your application is tolerant of sampling gaps, overlapping samples and duplicated samples, which may be unintentional data errors. These are all detected and reported to the appropriate sheet in the Reports window.

#### Gaps

Where there are gaps between samples, the values of all data fields within the gap interval will be treated as absent data when calculating composite values.

#### Overlapping and duplicated samples

Studio's compositing algorithms handle overlaps and duplicate samples correctly without calculating biased results.

  * For duplicate records Studio uses the arithmetic average for grade values.

  * For overlapping records, it uses a length weighted average value. There is no limit on the number of overlaps or duplicates for an interval.

## Absent Data, Weighting and Composites

#### Absent Data

Studio deals with absent data values encountered in a composite by ignoring them when calculating the weighted or dominant text value of the composite. If all samples in the composite have absent values, the composite value will be absent. If the Specific Gravity Weighting method is being used but there is no S.G. value then the weighting method will revert to standard length weighting.

#### Weighting Method

The weighting of composite sample values may be by either Length or by weight (Length x Specific Gravity, assuming a uniform sample cross-section).

#### Compositing Text Values

The dominant text value in a composite is determined by calculating the total length of each text value e.g. lithology codes, and assigning the value with the maximum length to the composite.

## Data Table Attributes

Typical data table attributes for dynamic drillhole component files and objects are:

### Collars

Field |  Description  
---|---  
BHID |  Hole name  
Easting |  X co-ordinate of the collar  
Northing |  Y co-ordinate of the collar  
Elevation |  Z co-ordinate of the collar  
Length |  Length of the hole  
Azimuth |  Azimuth at the collar  
Inclination |  Dip at the collar  
  
### Surveys

Field |  Description  
---|---  
BHID |  Hole name  
Depth At |  Depth of survey point down hole  
Azimuth |  Azimuth at survey point  
Inclination |  Dip at survey point  
  
### Assays

Field |  Description  
---|---  
BHID |  Hole name  
Depth From |  Distance down the hole of start of sample  
Depth To |  Distance down the hole of end of sample  
Density |  Rock density  
Sample 1 |  First grade or quality data column  
Sample 2 |  Second ...  
Sample 3 |  Third ...  
Sample 4 |  Fourth ...  
  
### Lithology

Field |  Description  
---|---  
BHID |  Hole name  
Depth From |  Distance down the hole of start of sample  
Depth To |  Distance down the hole of end of sample  
Density |  Rock density  
Sample 1 |  First rock description data column  
Sample 2 |  Second ...  
Sample 3 |  Third ...  
Sample 4 |  Fourth ...  
  
## Loading Data and Defining Holes

Use **Drillhole Importer** to load dynamic table data, validate and desurvey to create a static drillhole file.

One way to create dynamic drillholes is to use the [Data Load Wizard](<Data%20Load%20Wizard_Import%20Data%20Tables.md>).

Related topics and activities

  * [Drillhole Importer](<DrillholeImporter-screen.md>)
  * [Data Load Wizard](<Data%20Load%20Wizard_Import%20Data%20Tables.md>)

  * [Define Holes](<Define%20Holes%20Dialog.md>)

  * [Build Holes](<build%20holes%20dialog.md>)