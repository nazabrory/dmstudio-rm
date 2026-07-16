# Create Isoshells - Estimation Parameters

To access this screen:

  * Display the [Create Isoshells](<Create_Isoshells.md>)screen and select the **Estimation Parameters** tab.

The Create Isoshells tool allows categorical or continuous isoshells to be created from a point sample input, such as drillholes or chip samples.

The Estimation Parameters tab is used to specify search ellipsoid parameters (axis dimensions and rotations) and select the interpolation algorithm used to estimate the values which lie between samples. These settings are relevant to continuous isolevels only. 

To produce a realistic estimated value of a point in 3D space, at least three original sample points must fall within the search ellipse which is centered on that estimation point. A maximum of 10 samples is permitted - if there are more than 10 samples, the nearest 10 samples to the point being estimated are selected.

In order to achieve anisotropy different radii and orientations can be specified for each axis. Orientations are defined by specifying rotations in degrees (-360 to 360) for up to 3 axes. See [Search volumes for grade estimation](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Introduction.md>).

To define estimation parameters for isoshell modelling:

  1. Define the dimensions and rotations of your **Estimation Search Ellipsoid**. Define radii and orientations for each axis. Orientations are defined by specifying rotations in degrees (-360 to 360) for up to 3 axes.

     * Define the **Radius** of the X, Y and Z axes. Values must be greater than zero in all cases.

     * Define the **Rotations** of the search ellipse by specifying one, two or three rotations that are applied successively. The rotation angle, and the axis about which the rotation is performed can be specified.

  2. Choose an **Estimation Method** :

     * Choose Inverse Distance Weighting to estimate values on a regular grid by weighting each sample by the inverse power of its distance from each grid point. This is typically the quickest method, however, it does not consider the spatial relationship between samples.

With this option define the power, of which the inverse is used to calculate estimated values through the weighting of each sample. If set to zero, then the arithmetic mean of samples is calculated.

     * Choose Ordinary Kriging if you need to take account of the spatial relationship between samples. Whilst typically slower, this method has the advantage of adjusting weights to compensate for the clustering of samples. Variography is determined by one of two methods:
       * **Default variogram** use a variogram with a zero nugget variance, with ranges and orientation defined by the search volume.
       * **Imported variogram** import variogram data from an external file (via the browse button) or pick any previously loaded variogram object.

Related topics and activities

  * [Create Isoshells](<Create_Isoshells.md>)
  * [Create Isoshells: Input](<CreateIsoshells_Input.md>)
  * [Create Isoshells: Condition](<CreateIsoshells_Condition.md>)

  * [Create Isoshells: Volume](<CreateIsoshells_Vol.md>)

  * [Create Isoshells: Output](<CreateIsoshells_Output.md>)

  * [Isoshells Report](<CreateIsoshells_IsoShellsRep.md>)

  * [Create Categorical Surfaces](<../STUDIO_RM/Implicit_Surface_From_Drillholes_Categorical.md>)

  * [Create Grade Shells](<../STUDIO_RM/Implicit_Surface_From_Drillholes_Continuous.md>)

  * [Search Volumes for Grade Estimation](<../STUDIO_RM/Grade%20Estimation%20Search%20Volume%20Introduction.md>)
  * [Grade Estimation Methods](<../STUDIO_RM/Grade%20Estimation%20Methods.md>)