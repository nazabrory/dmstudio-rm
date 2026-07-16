# Uniform Conditioning: Input Data

To access this screen:

  1. Display the **[Uniform Conditioning](<UniformConditioning_Introduction.md>)** wizard.

  2. Select the **Input Data** tab.

This is where the 'ingredients' for the _Uniform Conditioning_ process are entered. This includes the XYZ data fields for the input samples an (optional) model file plus the other parameters required to feed into the process, such as the specified domain field and value. From this information a minimum and maximum grade value, plus details of the number of samples and records held within the domain are displayed.

A file containing sample data is required. The samples file will need to contain positional information (XYZ), at least one grade field and (optionally) a column containing information relating to the domain of interest. This could be a points file as well as a desurveyed drillhole file. Where possible, the fields containing the positional information is extracted and automatically added to this panel (although they can also be selected or edited manually).

If no Domain field is selected, all points in the input file will be used as well as a input model (if specified).

If you do elect to condition data within a specific domain, the Domain field must exist in both the specified sample file AND the input model file. You will also only be able to select a domain value if it occurs in both the samples and model file. Only usable domain fields and values will be made available for selection. For example, if both model and samples file contain a DOMAIN field, and the samples file contains 1,2 and 3 as unique values, whereas the model file contains 2,3 and 4, you will be able to select DOMAIN, but only values 2 and 3.

| Not available | Available | Available | Not available  
---|---|---|---|---  
Model File |  | 2 | 3 | 4  
Input Model File | 1 | 2 | 3 |   
  
Once you have specified your input parameters for the process, you can move onto the next stage, [sample declustering](<UniformConditioning_Decluster.md>).

To define input data for uniform conditioning:

  1. Open the **Uniform Conditioning** wizard and display the **Input Data** screen.

  2. Select your Input samples. Browse for a Datamine file that contains sample positional information and supporting attributes. Where **XYZ** data columns are found with an expected description (X, XPT, Y, YPT and so on) they are added to the lists below automatically.

  3. Review **X** , Y and Z to ensure a valid coordinate field is specified in each.

  4. Select the Grade Field (in the samples file) that is considered. You can't proceed without one.

  5. Choose an Input Model. This is optional, and is an existing geological model, and used if you wish to make use of the **Panel** and **SMU block model** report options later in the process. If you decide not to import a model, you will still be able to generate global **Grade Tonnage** curves.

  6. If you have specified both a samples file and an Input Model (see above), the Domain list shows all unique data fields found in both data files. 

If only a samples file is set, all unique data fields detected in this file are shown. 

Note: You do not have to select a domain field; if you leave this setting blank, all samples and model data (if a model file has been selected) will be used in the Uniform Conditioning process.

  7. Review the No. of samples in the selected domain: Once you have have selected a Domain (see above), this read-only field displays the total number of sample file records found that relate to that domain.

  8. Review the No. of model records in the selected domain: Once you have selected a Domain and have also specified an Input Model , this read-only field displays the total number of records in the **Input Model** that relate to the domain.

  9. Review the Min/Max Grade: This read-only field will show the lowest and highest grade values detected in the specified samples file in the selected Domain.

  10. Decide what to do with temporary files created by the Uniform Conditioning processes. Remove temporary files is checked by default, these files are deleted after use. If you uncheck this option, they are retained, which can be useful in reviewing intermediate calculations in case of unexpected outputs.

  11. Continue setting up your Uniform Conditioning run on the [Decluster](<UniformConditioning_Decluster.md>) screen.

Related topics and activities

  * [Uniform Conditioning - Introduction](<UniformConditioning_Introduction.md>)

  * [Uniform Conditioning \- Decluster](<UniformConditioning_Decluster.md>)

  * [Uniform Conditioning \- Variograms](<UniformConditioning_Variograms.md>)

  * [Uniform Conditioning - Grade Tonnage Curves](<UniformConditioning_GlobalGradeTonnageCurves.md>)

  * [Uniform Conditioning - Panel Model Reports](<UniformConditioning_PanelBlockModelReports.md>)

  * [Uniform Conditioning - SMU Model Reports](<UniformConditioning_SmuBlockModelReports.md>)

  * [About Uniform Conditioning](<About_Uniform_Conditioning.md>)