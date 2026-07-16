# Automatic Model Fitting

To access this screen:

  * In the [**Advanced Estimation**](<Multivariate_Dialogs_Overview.md>) wizard, select [**Fit Models**](<Multivariate_Fit_Models.md>). Select the **Auto. Fit** tab.

This tab, part of the **Fit Models** screen, is used to fit a model to the currently selected variogram automatically. 

Both univariate and multivariate model fitting is possible and you can restrict model parameter values using a range of controls to add and configure model structures of varying types.

"Auto-fitting" can be performed once a variogram has been generated and displays in the centre of the screen. Initially, no model structures exist. Auto-fitting generates structures in an attempt to fit a model to the variogram directions that are currently available.

When you fit a model to a variogram, you transform the empirical (often noisy) spatial dependence data into a smooth function that can be used for interpolation and spatial prediction. The fitted model describes the key spatial parameters (nugget, sill, range), which are crucial for understanding and predicting spatial patterns in the dataset.

Key model fitting concepts:

  * **Nugget** Represents the semivariance at zero distance. It accounts for measurement errors or spatial variation occurring at distances smaller than the sampling resolution.

  * **Sill** The value where the semivariance levels off, representing the total variance of the data once spatial correlation is no longer present.

  * **Range** The distance beyond which the semivariance no longer increases, meaning there is no further spatial correlation between points.

### Run Auto Fitting

The following activity assumes that a **[scenario has been created](<Multivariate_Scenario_Setup.md>)** , [samples selected](<Multivariate_Select_Samples.md>), [variograms created](<Multivariate_Create_Variograms.md>) and the [Fit Models](<Multivariate_Fit_Models.md>) screen displayed.

To automatically fit a model to the target variogram:

  1. Activate the **Auto. fit** tab.

  2. Click **Run auto-fitting** to launch the auto-fitting process and generate initial structures - an attempt will be made to fit a model to the variogram directions that are ticked for display and are shown as thumbnails on the bottom row of the panel.

  3. Refine the auto fitting parameters for a subsequent run:

     1. Where covariograms exist, decide if a multivariate or univariate model should be fitted:

        * If **Fit multivariate model** is **checked** , a multivariate model is fitted to the selected variogram (depending on the current [Variogram Type](<Multivariate_Fit_Models.md>)). 

        * If **Fit multivariate model** is **unchecked** , the univariate instance is assumed.

     2. Choose how the total sill of the model is set:

        * If **Set total sill to variance** is **checked** , the total sill of the model is set equal to the statistical variance of the samples.

        * If **Set total sill to variance** is **unchecked** , the total sill is calculated from the experimental variogram(s).

     3. Define the Minimum nugget %. This refers to the smallest possible value of the nugget (the semivariance at zero distance) that can be used when fitting a model to a variogram. The nugget represents the variability or discontinuity that exists at short distances.

This setting represents the minimum nugget variance as a percentage of the total sill. Setting this to zero permits a zero nugget variance to be calculated.

     4. Choose the Minimum sill % per structure. This refers to the smallest possible value of the sill (the plateau that the semivariance reaches at large distances) that can be used when fitting a theoretical variogram model. The sill represents the total variance in the data after accounting for spatial correlation, meaning it's the level at which spatial dependence no longer influences the data beyond a certain distance (the range).

The sill of each individual structure must exceed the defined minimum percentage of the total sill. This prevents small structures being introduced that have little influence on the total model.

     5. Review the table showing the **Available structures**.

        * Each structure is defined as one of three **Structure type** s: _Spherical, Exponential_ or _Gaussian_. 

        * If **Constrain range** is checked, **Min** and **Max** range values can be specified to constrain the range of each structure.

        * To **edit an existing structure** , highlight it in the list, edit its properties and click **Apply**.

        * To **add a new structure** make sure none of the existing structures are highlighted, select the required values for Structure type, min and max, and then **Apply** the values.

        * To **remove a structure** , select it and click **Remove**. This cannot be undone.

  4. You can also import nugget values from an external file:

     1. Check Use nugget from file.

     2. Browse for a file containing the nugget data. The file must contain at least the two fields **NUGGET** and **GRADE** for univariate models and also the field **GRADE2** for a multivariate model. A standard model variogram file is acceptable.

Related topics and activities

  * [Fit Models](<Multivariate_Fit_Models.md>)

  * [Fit Models Manually](<Multivariate_FitModels_ManualFitting.md>)

  * [Model Parameters](<Multivariate_FitModels_ModelParameters.md>)

  * [Save Models](<Multivariate_FitModels_SaveModels.md>)

  * [Format Models](<Multivariate_FitModels_Format.md>)

  * [Advanced Estimation & Variography](<Multivariate_Introduction.md>)