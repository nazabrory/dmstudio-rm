# Estimate Angles

To access this screen:

  * **Advanced Estimation** wizard **> > Select Prototype**.

Interpolate angle data between recorded 3D data points and convey this trend information during grade estimation. This helps with the estimation as trends will be used to encourage interpolation in one or more directions.

Angle Data can be interpolated between known 3D points. Typically, this data takes the form of a [Datamine points file](<../COMMON/filetype.md>), with each record containing (in addition to 3D coordinates), an attribute representing the known dip of the trend (such as **TRDIP**) and the dip direction (such as **TRDIPDIR**) at that point. Any number of angles can be specified within the file. Once a file has been selected, your application will attempt to map the coordinate fields to known/expected descriptions. You can adjust these assignments using the X/Y/Z drop-down lists if you need to.

Angle data is then interpolated. Interpolation is performed independently; there is no correlation between angles. These interpolated angle values are then added to the Model with angles block model file when the Estimate Angles button is used.

Select this angle-estimated model to use it in downstream estimation. 

To estimate angles into a block model for use in grade estimation:

  1. Choose an **Input model**. This represents your model prototype, and can be either a dedicated prototype or any other block model (its prototype is used).

  2. Select your **Angle data**. This is a Datamine points file containing dip and dip direction information.

Where possible, **X** , **Y** and **Z** coordinate fields are detected and displayed. Otherwise, select the coordinate fields for each axis.

  3. Select the Angle Fields containing values representing anisotropy.

  4. Choose whether to interpolate angular information with respect to a geological zones indicated by the input points:

     * If **Restrict to matching zones** is **checked** , select **Zone1** and, optionally, **Zone2**. 

**Note** : These zones are entirely independent of the zones optionally specified using the Define Custom Zones screen, which reflects zonal information imparted by the input sample data. The zones selected here are used to constrain the interpolation of angular data.

     * If **Restrict to matching zones** is **unchecked** , angular interpolation is unconstrained.

  5. Choose the angular interpretation method. The principles behind interpolation are the same as for grade estimation. See [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>).

     * Inverse power distance. If set, a **Power** can be set (this determines the strength of influence of known data values over neighbouring locations).

If IPD is chosen, you can also define a Cell Discretization value in each axis.

     * Nearest neighbour. Interpolate using a simple nearest neighbour approach.

  6. Choose if parent or subcell estimation is performed when estimating angles:

     * Select Sub-cells estimation to estimate directional data into each sub-cell.

     * Select Parent cell estimation (the default) to interpolate angular data for each parent cell in the output model.

  7. Choose the **Search Parameters** for the estimation:

     * Distance (Isotropic)The distance used to generate interpolated angular values. Higher values will tend to calculate more general angular trends, although this is highly sensitive to the input points data.

     * Minimum samplesThe minimum number of samples within the search scope required to estimate an angle.

     * Maximum samplesThe maximum number of samples within the search scope required to estimate an angle.

  8. Click **Estimate Angles** to generate a block model with interpolated angular data. The model is generated and its name appears in the **Model with angles** field. If the model already exists, it is overwritten. 

Once a model has been generated, it can be selected and used as an input to grade estimation by enabling the Model with angles field check box.

**Note** : If the **Model with angles** check box is **unchecked** , the **Input model** is used instead (which may or may not contain interpolated angle information). This check box can't be selected until an angle-estimated model has been generated, or a previously-generated angle model selected using the browse button provided.

Related topics and activities

  * [Select Prototype](<Multivariate_Select_Prototype.md>)

  * [Define Dynamic Anisotropy Fields](<Multivariate_Select_Prototype_DA.md>)

  * [Advanced Estimation Screens](<Multivariate_Dialogs_Overview.md>)