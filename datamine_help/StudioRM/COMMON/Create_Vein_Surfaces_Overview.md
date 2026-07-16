# Vein Modelling

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

The **Create Vein Surfaces** tool computes hanging wall (HW) and/or footwall (FW) surfaces that represent vein or vein-like structures. It can be used to model independent surfaces or a combined volume.

Surface creation is disctated by the structure of input drillhole sample values. These values represent a discrete upper and lower bounding surface. Optionally, model a closed volume representing both HW and FW surfaces and control how surfaces interact in pinch and/or swell zones. 

Structure boundaries (either HW, FW or both as a volume) align with boundaries between distinct categorical values, typically indicating lithological boundaries. As data, these are indicated by contiguous _FROM-TO_ values within the drillhole file. The output wireframe data can be used to guide downstream model estimation. For example, constraining a block model within a predicted vein volume, or using the output HW or FW surface to generate search ellipsoids for grade estimation.

The output from this function is a linear, non-bifurcating structure, which is either a wireframe surface or a volume. If you intend to model bifurcating or structures with multiple structures, or where complex trends exist, consider using the categorical modelling command instead. See [Create Categorical Surfaces](<../STUDIO_RM/Implicit_Surface_From_Drillholes_Categorical.md>).

Output is strongly influenced by modelling parameters, including:

  * The output surface type(s); HW, FW or both as a volume.

  * How output wireframe data is constrained by clipping; either using a string boundary, a prototype model or hull data extents.

  * The order of HW and FW samples, or the presence of injected 'dummy' sample points (to encourage an outcome).

  * How end-of-hole data is interpreted.

  * Volume thickness constraints, including minimum and maximum permitted true thickness limits.

  * How the presence of other data values controls surface generation; whether it should be pinched out in the presence of non-target data values or not.

  * If fault wireframe sheets are used to generate independent fault blocks. 

Considerations for deciding the above may include:

  * Your confidence in the input data.

  * The amount of positive samples that exist, and the density of those samples.

  * The geological properties of the domain environment.

  * Other supporting media such as seismic analysis, historical data, geophysical properties of the domain etc.

  * Whether a conservative or generous outcome is expected.

## Restoring and Resetting Values

The Create Vein Surface tool stores settings for each **Column** and **Value** combination and reinstates them when swapping between columns and values. The current settings cache remains in place for the duration of the project session. In fact, it is the cached data that is used when a batch run is performed.

## Pinching Out Data

Model either HW or FW surfaces as DTMs, or both surfaces as a closed volume. 

You can 'pinch out' a vein volume by enabling Pinch Out. This allows you to model pinch zones within your modelled surface where one of these conditions are met:

  * A negative sample (a sample that intercepts the predicted path of the vein but does not contain the geological unit that is being modelled) intercepts the vein. This indicates that there is an absence of the vein in this area, and a pinched out void is modelled in that area. 
  * The thickness of the modelled volume is less than a designated value. For example, if you wish to ignore vein data that is less than a mineable limit, you can set a Minimum thickness. If pinching out is active, data that represents a volume below the minimum limit is removed, creating a void in the output model.

## Summary Report

Each 'run' of the Create Vein Surface function results in summary report in the Output window. This data summarizes settings used to generate the most recent surface. For example:
    
    
    Vein-from-samples Results
    
    
    Input drillholes                      _vb_holes (drillholes)
    
    
    Column                                NLITH
    
    
    Value                                 3
    
    
    Uncertainty column                    <None>
    
    
    Default uncertainty                   0
    
    
    Drillholes used                       26 / 26
    
    
    From points used : reversed           26 : 0
    
    
    To points used : reversed             26 : 0
    
    
    End of hole points used               Yes
    
    
    Ignore gaps                           No
    
    
    Use additional points                 No
    
    
    Continuity                            24.9
    
    
    Clipping method                 Radial interp
    
    
    Radius                                48.6
    
    
    Minimum thickness                     0.05
    
    
    Expand to
    
    
    Use pinch out                         Yes
    
    
    Use auto continuity                   No
    
    
    Resolution                            Medium
    
    
    Trend smoothness                      0%
    
    
    Total hanging wall points             26
    
    
    Total foot wall points                26
    
    
    Surface type generated                HW and FW
    
    
    Vein surface output                   VeinSurf_NLITH_3
    
    
    Vein-from-samples ran successfully    
    
    
    ------------------------------

The Output window reports:

  * If the command has been run via a script.

  * If the command fails due to a missing vital parameter when run via script, it will notify you of which parameter is missing.

  * If no boundary object can be found if custom boundary has been selected.

  * If no perimeter strings can be found that are expected.

  * If no HW or FW points can be found within the specified boundary, making surface or volume calculation impossible.

  * If a vein model could not fully encompass all available positive samples, or all parts of all samples. In this situation all drillhole IDs that could not be accommodated are listed.

**Note** : You can access this command [using an automation script](<Create_Vein_Surfaces_10_Automation.md>).

### Implicit Modelling Metadata

Implicit modelling tools store metadata to allow previous settings to be reinstated automatically, and for downstream commands to understand the 'legacy' of input data. See [Implicit Modelling Metadata](<Implicit-Modelling-Metadata.md>).