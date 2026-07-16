# Advanced Estimation & Variography

The Advanced Estimation (AE) wizard provides a range of methods for estimating grades into a block model including both univariate and multivariate kriging methods. 

### Unvariate vs. Multivariate Kriging

  * With univariate kriging each block estimate is calculated from the sample values for a single variable (grade).

  * The multivariate cokriging method uses values from other grades that are correlated to the grade being estimated.

**Note** : Advanced Estimation is part of the Studio RM toolset. Additional licensing modules aren't required.

At the heart of the **Advanced Estimation** wizard lies the **[COKRIG](<../Process_Help_XML/cokrig.md>)** process, although other processes and custom functionality support the workflow from initial samples to estimated model.

The two main cases where cokriging can improve estimates (that is, reduce the kriging variance compared to univariate kriging) are:

  * Where a variable is poorly sampled but correlates with a secondary variable that is much better sampled
  * Where a variable has poor low spatial continuity, but correlates with one that has better continuity.

In both cases additional variables can help to improve estimates of the first variable, particularly in the first case. Cokriging can be used if there is a full set of data for both the primary and secondary grades, but there is often very little or no improvement in the estimates.

Multivariate estimation requires the variables to be well correlated, either positively or negatively. The mutual spatial behaviour of regionalised variables is known asco-regionalization. Cokriging requires the same conditions to be satisfied as kriging does, but needs additional variography and modelling tools which are provided by the **Advanced Estimation** wizard.

### Advanced Estimation: 2D vs. 3D Data

Advanced estimation can be performed using 2D or 3D data. Where samples with 2D data have been selected, panel behavior will be adjusted in some cases to ensure inputs the function are valid. 

For example, axes for which it is not possible to rotate around are disabled when computing the variograms and fitting the models, and the Investigate Anisotropy panel will only display a single isocontour plot where 2D data has been specified. Other adjustments are made internally to ensure 2D data is processed correctly, particularly with regards to calculations involving rotation.

AE supports both univariate and multivariate estimation:

  * **Guided Workflow** a series of sequential tasks that build up a univariate or multivariate estimation study. These appear in a vertical list on the left of the wizard.
  * Scenario ManagementAE parameters are wrapped up in convenient scenarios, which can be copied, and even exported for use in another project. 
  * Datamine Supervisor Integrationimport variogram models directly from a Datamine Supervisor project file, instead of configuring them in the AE wizard. See Datamine Supervisor Integration, below.
  * **Unfolding** unfold data prior to estimation from within the AE wizard.
  * Custom Zonesallows selected zones to be merged into custom zones for soft boundary estimation. 
  * **Bivariate Data Analysis** calculate and display bivariate statistics by domain for each pair of grades.
  * **3D Variogram Visualization** create a 3D block model of variogram values to determine the directions of anisotropy.
  * **Variogram Calculation** for both variograms and for cross-variograms if cokriging.
  * **Variogram Model Fitting** with dynamic lag control and automatic fitting options, plus a choice of model fitting types (variogram, log variogram, madogram and so on.)
  * **Kriging Neighbourhood Analysis (KNA)** to assist in the selection of optimal sample search volume and estimation parameters. See [Kriging Neighbourhood Analysis](<KNA-Introduction.md>).
  * Parameter Import & Exportimport existing COKRIG parameter files, including files compatible with ESTIMA, directly into the AE wizard. This can save time and ensure a consistent approach to estimation.
  * **Estimation Method Support** with all practical approaches covered, including ordinary and simple kriging, plus cokriging of course. You can also estimate using nearest neighbour and inverse distance methods. Sub-celling is also available.

**Tip** : If you have access to multiple monitors, float the Advanced Estimation dialog to a spare monitor so the application can be seen in full throughout the process.

### Datamine Supervisor Integration

You can run variography and KNA using Datamine Supervisor or Studio RM - it's up to you. 

If you choose to use Supervisor data, all variography and KNA functionality is hidden, showing you only the panels you need to complete your estimation. Set up your scenario in Studio RM, import parameter files then define your estimation and run it. 

You need to decide on your workflow up front, using a switch on the [Scenario Setup](<Multivariate_Scenario_Setup.md>) panel.

Importing project data from Supervisor automatically populates the [Define Estimations](<Multivariate_Define_Estimations.md>) and [Define Search Volumes](<Multivariate_Select_Search_Volumes.md>) screens. Variograms from the Supervisor project will also (if possible) be automatically assigned to the created estimations.

You can also extract scenario data from a Datamine Supervisor _project_ (the project must be from Supervisor v8.14.2.3 or later). The imported project must contain a Datamine-compatible variogram.

These Supervisor integration options are independent; for example, you may choose to complete your variography in Datamine Supervisor and fill in the scenario details yourself, or use the AE wizard for variography but import scenario details from a Supervisor project, or any combination of these methods.