# Review Variograms

To access this screen:

  * Using the [Advanced Estimation](<Multivariate_Introduction.md>) dialog, select the Review Variograms menu item.

To perform grade interpolation using [kriging](<Grade%20Estimation%20Methods.md>), an appropriate variogram model is needed. If co-kriging is used, a multivariate variogram model set is required which has the same ranges for all models.

**Note** : If you have imported data from Datamine Supervisor, variograms derived from the imported project are automatically associated with the corresponding estimation(s).

If zones are specified on the **[Select Samples](<Multivariate_Select_Samples.md>)** screen, a variogram model set is required for each zone. If one of the non-kriging estimation methods has been selected (nearest neighbour, inverse distance and so on) then a variogram model is not required.

Variograms can be imported from a Datamine Supervisor project using the Import option on the [Scenario Setup](<Multivariate_Scenario_Setup.md>) panel.

Usually the variogram models will have been fitted or imported at the _[Fit Models](<Multivariate_Fit_Models.md>)_ stage. However it is also possible to import or export a model on the **Review Variograms** screen.

**Note** : The _Confirm Variograms_ panel allows the user to review the selected model or select a different model.

To add a new variogram model set:

  1. Below the **Available Variograms** table (middle of the screen), click **Add**.

  2. Define [Model Parameters](<Multivariate_VariogramParameters.md>).

  3. Define [Variogram Model Set Properties](<Multivariate_VariogramModelSetProperties.md>).

To assign a variogram model to an estimation:

  1. Review the **Select an estimation to view or apply variogram models** list.

All estimations configured using the [Define an Estimation](<Multivariate_Define_Estimations.md>) screen are listed, together with the respective grade(s) and zone. For kriging estimates the default variogram model reference number is also shown.

  2. Highlight one of the estimation runs (left-click).

  3. Review the **Available Variograms** list and select an existing model.

Available variogram model sets are displayed, along with the grades, zone, univariate or multivariate and how the fitting was performed - manually, automatically, or a "mix". 

  4. Click **Apply variogram model to estimation [estimation number]**.

**Note** : If only one variogram model is available, it is automatically assigned to the highlighted estimation and the application button is unavailable.

To manage the Available Variograms list:

  * Click **Add** to insert a new variogram model with default parameters into the list.

  * Click **Remove** to remove an existing variogram from the current set.

  * Click **Clear list** to remove all variograms from the scenario. 

  * Click **Import** to import a variogram model file and show it in the table above.

**Note** : During variogram model import, file contents will be analyzed to ensure it contains the fields required to complete the estimation process. For example, if a zone field (either the first or second zone) is expected but cannot be found in the incoming file, a message will be displayed explaining which field is expected and cannot be found. Similarly, other required fields such as **VSETNUM** , **GRADE** , **GRADE2** and **TRANS** fields are checked.

  * Click **Export** to export the currently selected variogram to an external file, for import in other projects.