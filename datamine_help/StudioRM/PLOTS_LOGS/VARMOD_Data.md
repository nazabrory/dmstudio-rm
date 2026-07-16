# Variograms: Data

To access this screen:

  * Display the [Variogram](<VARMOD_Introduction.md>) screen.

  * Load an experimental variogram data file. See [Variograms: Data Selection](<VARMOD_Data_Selection.md>).

  * Display the **Charts** tab and select a variogram chart.

  * Select the Data tab.

View the lag details for the variogram selected in the [Charts](<VARMOD_Charts.md>) tab. A variogram must first be selected (highlighted in blue) in the Charts tab before data is listed in the Data tab.  

Note: On this screen, each displayed table row corresponds to a record in the loaded experimental variogram file and is represented by a point on the chart in the preview pane. The point is only displayed on the chart if the **NO.PAIRS** column value is equal to or greater than the Minimum No of Pairs parameter set in the [Data Selection](<VARMOD_Data_Selection.md>) tab. All records are listed in this pane irrespective of this.

For each experimental variogram record, the following attributes display:

Attribute | Description  
---|---  
[Key Field] | The Key Field and Key Value combination as selected on the Data Selection tab .  
GRADE | The name of the grade or quality field selected in Value Field on the Data Selection tab .  
AZI | The azimuth or dip direction, in the local coordinate system, of the varogram; '-' denotes the omnidirectional variogram.  
DIP | The dip, in the local coordinate system, of the variogram; ; '-' denotes the omnidirectional variogram.  
WAZI |  The azimuth of the variogram, in the world coordinate system. This is only included if one or more rotation angle have been defined. If rotation angles are not defined, then WAZI and AZI have the same value.   
WDIP | The dip of the variogram, in the world coordinate system. This is only included if one or more rotation angles have been defined. If rotation angles are not defined, then WDIP and DIP would have the same value.   
LAG | The lag distance.  
AVE.DIST | Average distance between sample pairs for the LAG.  
NO.PAIRS | Number of sample pairs for the LAG.  
COVAR | Covariance between sample pairs.  
VGRAM | Experimental variogram value between sample pairs.  
PWRVGRAM | The pairwise relative variogram or relative cross variogram. This is the same as the variogram or cross variogram, except that every term in the calculation is divided by the average value of the two samples contributing to that term.  
LOGVGRAM | The log variogram or cross variogram. This is calculated by taking the logs of the grade values before calculating the variogram or cross variogram.  
  
For more information on variogram parameters, see [VGRAM Process](<../Process_Help_XML/vgram.md>).

Related topics and activities

  * [Variograms](<VARMOD_Introduction.md>)

  * [VGRAM Process](<../Process_Help_XML/vgram.md>)

  * [Variogram Properties](<VARMOD_Properties.md>)

  * [Variograms: Data Selection](<VARMOD_Data_Selection.md>)

  * [Variograms: Charts](<VARMOD_Charts.md>)

  * Data Tab

  * [Model Fitting Tab](<VARMOD_Model_Fitting.md>)

  * [Editing Variograms Interactively](<VARMOD_Preview.md>)