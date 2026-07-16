# Select Table Type

To access this screen:

  * **Data** ribbon **> > Objects >> New >> New Hole Table**.

  * Activate the Data ribbon and select Objects | New | New Hole Table

Select a type of dynamic database table to create.

Data tables, for each type, require a minimum field specification. For example, _Collars_ tables will, as a minimum, require a _Hole ID_ , _Easting_ , _Northing_ , _Elevation_ , _Length_ and _Azimuth_ for each collar position, so these columns are automatically created, without corresponding values.

The following list shows a full breakdown of the fields included in each new table type:

Table type |  Contains fields  
---|---  
Collars | 

  * Hole Name,
  * Easting,
  * Northing,
  * Elevation,
  * Length,
  * Azimuth,
  * Inclination

  
Surveys | 

  * Hole Name,
  * Depth At,
  * Azimuth,
  * Inclination

  
Traces | 

  * Hole Name,
  * Depth At,
  * Easting,
  * Northing,
  * Elevation,
  * Azimuth,
  * Inclination

  
Assays | 

  * Hole Name,
  * Depth From,
  * Depth To,
  * Grade_1, Grade_2, ....Grade_15,

  
Lithology | 

  * Hole Name,
  * Depth From,
  * Depth To,
  * Lithology

  
Intersections | 

  * Hole Name,
  * Depth From,
  * Depth To,
  * Zone,
  * length weighted average grades

  
Header | 

  * Hole Name

  
Interval log | 

  * Hole Name,
  * Depth From,
  * Depth To

  
Depth log | 

  * Hole Name,
  * Depth At

  
Not set | 

  * None

  
  
Tip: You can view your newly created data object in memory using the [Data Object Manager](<Data%20Manager%20Dialog.md>), before or after saving your project.

Related topics and activities:

  * [Drillhole Representation](<Drillhole%20Representation%20in%20Studio.md>)