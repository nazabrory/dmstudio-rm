'''
dmstudio.dmfiles
================

All datamine commands which do not use input files. The commands are mainly for generating datamine files such as ``inpfil``, ``protom`` etc.

To do:
------

* Replace multiple field/file inputs with input lists e.g. *f1, *f2... -> fields_f=['f1', 'f2']
* Exhaustive testing and debugging
* Use the same field parsing as ``dmcommands``

'''
import dmstudio.initialize

# constant to avoid redundant COM connections which slows down processing

OSCRIPTCON = None

class init(object):

    def __init__(self, version=None):

        '''
        commands.__init__
        ------------------


        Commands initialization. After the commands class is initialized  for the first time the object will
         be set to the datamine studio object. This property will avoid redundant initializaiton

        Parameters:
        -----------

        version: str
            optional datamine studio versions ('Studio3', 'StudioRM', 'StudioRM3.1', 'StudioRM3.2', 'StudioEM') If no version given, the initializtion
            will try different versions starting with StudioRM then Studio3 and finally StudioEM.

        '''
        self.oScript = OSCRIPTCON
        self.version = version
        if self.oScript is None:
            self.oScript = dmstudio.initialize.studio(self.version)

    def run_command(self, command):
        '''
        run_command
        -----------

        Uses the studio Parsecommand method to execute a datamine script.

        Parameters:
        -----------

        command: str
            datamine command string to be parsed
        '''

        try:
            self.oScript.Parsecommand(command)
        except Exception as e:
            print("Unexpected error:", e)

    def parse_infields_list(self, prefix, fields, maxfields=10, vtype='*'):

        """
        parse_infields_list
        -------------------

        Intenal function for parsing a list of *fields to a string for use in studio commands e.g. *F1, *F2, etc..

        Parameters
        ----------

        prefix: str
            starting letter or letters for the field e.g. 'F' for *F1.
        fields: list of str
            list of input fields
        maxfields: int
            maximum number of fields permitted by datamine command
        vtype: str
            variable type, input file or field. For input file vtype="&" for field vtype="*"

        Returns:
        --------

        field_string: str
            concatenated string formated for input in datamine commands

        """

        if maxfields < len(fields):
            raise ValueError("More fields have been selected than allowed by Datamine command")

        field_string = ""
        for i, field in enumerate(fields):
            field_string += " " + vtype + prefix + str(i + 1) + "=" + field + " "

        return field_string;

    def cokrig(self,
                retrieval="optional"):

        r"""
        COKRIG
        ------
        COKRIG performs grade estimation using univariate and multivariate methods, including ordinary, simple kriging, inverse distance weighting and nearest neighbour. 

This process is used as part of the [Advanced Estimation](<../STUDIO_RM/Multivariate_Introduction.md>) wizard, although it can also be accessed independently via the command line as a standalone process.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "cokrig "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def comres(self,
                reserve_o="required",
                zone_f="optional",
                retrieval="optional"):

        r"""
        COMRES
        ------
        Generates a file that contains summary results from a number of different **RESULTS** files, that have been produced by processes such as [MODRES](<modres.md>) or [TRIVAL](<trival.md>).

The output file generated is suitable for subsequent mine planning and scheduling purposes, such as interactive production scheduling (**PRODSH**). The file will contain reserve figures for production units that have been classified by the user into primary and secondary categories, and it will contain all grade fields that are contained in the input **RESULTS** files.

Production scheduling requires some initial definition of the quantities and grades of the mining units to be scheduled. The final product of any evaluation is a comprehensive **RESULTS** file that contains data describing the mining reserves. There are a number of standard fields in a **RESULTS** file, which allow each logical part of an evaluation to be stored as a data record with entries including the tonnage, volume, grade(s), grade intervals, block model position, perimeter numbers and wireframe zone numbers.

The **COMRES** process accepts the input from one or more such **RESULTS** files (maximum 20) and generates a **RESERVE** file, which will be used for subsequent production scheduling. Each record of the **RESERVE** file describes the tonnage and grade of a production unit. The classification of production units stems from user selection of various options during the operation of **COMRES**. This allows production units to be classified into primary and secondary categories, based on criteria available from the **RESULTS** files. This flexibility allows the scheduling extension module to be used for both open pit and underground mining applications.

Two numeric fields in the **RESERVE** file, **PNUM** and **SNUM** , contain the primary and secondary numbers for each production unit. The data entries in these fields come directly from the input **RESULTS** files or are assigned logically according to the selected classification option, e.g. if the secondary classification is based on perimeters, the **SNUM** values will come from the **PERIMID** values in the **RESULTS** file(s). If a number of **RESULTS** files are input, and primary classification by model is required, the **PNUM** entries will increment 1, 2, 3 etc. for each **RESULTS** file.

If secondary classification is by ore/waste, the **SNUM** values will be either 1 for ore or 2 for waste. Another alphanumeric field, **UNIT** , allows a clear primary descriptor to be assigned for each production unit, which will appear on the schedule screen in the **PRODSH** process.

The production rate at which each production unit will be mined may also be defined in the **COMRES** process. The **RESERVE** file is a normal Datamine binary file, and so may be listed, edited or joined with other files using the available relational database facilities.

### Results Files

Enter the name of each **RESULTS** file, followed by <return>. Typing <?> will show a list of the currently selected **RESULTS** files. Typing a back arrow, <, will clear all the filenames entered and reprompt from the beginning. Entries are terminated by just typing <return>. Pressing <!> will terminate the process. When more than one **RESULTS** file is entered, it is expected that each contains the same grade fields.

### Production Rates

Enter required production rate for each **RESULTS** file. Pressing <return> will put absent data into the production rate data record for that **RESULTS** file. These production rate values may be initialized or modified in the **PRODSH** production scheduling process. These values will be stored in the **PRATE** field of the **RESERVE** file.

### Production Unit Classification

For production scheduling purpose, production units are classified from data held in the **RESULTS** files, and this may be done in a number of ways. A primary and optionally a secondary means of classification is available, allowing a number of features during production scheduling. 

If more than one **RESULTS** file has been entered, the user will get the following prompt:
    
    
    > IS THE SAME TYPE OF PRIMARY AND SECONDARY CLASSIFICATION REQUIRED 
     FOR EACH RESULTS FILE [Y]/N  > 

If N or NO is entered, you will get primary and secondary classification options for each **RESULTS** file that has been entered.

If the default option has been taken for the above prompt, then the classification selected below will used for each of the supplied **RESULTS** files.

### Primary Classification

Options are:

  1. Model or Sample File
  2. Plane
  3. Perimeter
  4. Zone

Enter number for required type of primary classification, which will determine the manner of primary tonnage and grade accumulation, in addition to the primary names and numbers in the output **RESERVE** file. Just typing <return> will take the default 'MODEL' or 'SAMPLE FILE' (from a **SECTED** evaluation) primary classification.

### Secondary Classification

Options are:

  1. No secondary classification
  2. Plane
  3. Perimeter
  4. Zone
  5. Ore/Waste
  6. Grade Interval

Enter number for required type of secondary classification. Just typing <return> will take the default, omitting any secondary classification.

These primary and secondary classification prompts will be repeated for each **RESULTS** file entered, if a a separate means of classification for each file was requested above.

Once the primary and secondary classification is complete the **RESERVE** file will be generated.

        Input Files:
        ------------

        Output Files:
        -------------

        reserve: Undefined
            The output file generated, for use in subsequent scheduling processes, such as
            **PRODSH**. It will contain the following fields, in addition to all of the grade fields
            in the **RESULTS** file(s). **UNIT** A,8 Field containing the name of each production
            unit. **PNUM** N Any blocks being scheduled may be categorised according to a primary
            and secondary classification. The **PNUM** field contains the primary number. The values
            held in this field will depend on the type of primary classification selected. **SNUM**
            N Secondary classification number. The values held in this field will depend on the type
            of secondary classification selected. If ore/waste secondary classification is selected,
            it will contain values of 1 for all ore units, and values of 2 for all waste units.
            **NY** N Implicit field, defining the total number of production units in the file,
            equal to the number of records. **PRATE** N Notional production rate at which each
            production unit is to be mined. This may contain absent data values, as individual
            production rates may be defined or changed during operation of **PRODSH**. **TONNES** N
            Reserve tonnage for each production unit.
            Required=Yes

        Fields:
        -------

        zone: Numeric : RESERVE
            Optional numeric zone identifier field that has been used to define individual
            wireframe zones. This field need only be defined if reserve classification by wireframe
            zone is required.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        """
        command = "comres "

        if reserve_o == "required":
            raise ValueError("reserve_o is required.")

        if reserve_o != "optional":
            command += " &reserve=" + reserve_o

        if zone_f != "optional":
            command += " *zone=" + zone_f

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def estima(self,
                retrieval="optional"):

        r"""
        ESTIMA
        ------
        The **ESTIMA** process provides a choice of methods for grade estimation of a block model.

For in-depth conceptual information on the **ESTIMA** process, and grade estimation in general, see [Grade Estimation Introduction](<../STUDIO_RM/Grade%20Estimate%20Overview.md>).

**ESTIMA** provides the following grade estimation methods:

  * Nearest Neighbor (NN).

  * Inverse Power of Distance [IPD].

  * Ordinary Kriging (OK).

  * Simple Kriging.

  * Log Kriging.

  * Sichel's T Estimator.

  * Ordinary Macro Kriging

  * Simple Macro Kriging

  * F-value

  * Lagrange multiplier

Key ESTIMA features:

  * Multiple grades can be estimated in a single run.

  * The same grade can be estimated by different methods.

  * Different search volumes and estimation parameters can be used for the different grades.

  * Rectangular or ellipsoidal search volume with anisotropy.

  * Restriction of number of samples by octant.

  * Restriction of number of samples by key field.

  * Estimation by zone, with separate parameters for each zone.

  * Wide selection of variogram model types for both normal and lognormal kriging.

  * Automatic transformation of data if the &PROTO model is a rotated model.

  * Unfolding option available for all estimation types.

  * Optimization of sample searching to improve processing speed.

  * Parent cell estimation.

  * Selective update of a partial model.

If the input **& PROTO** model contains cells and sub-cells then values are interpolated into the existing cell structure. If **& PROTO** is empty then cells and sub-cells are created if there are sufficient samples within the search volume.

**ESTIMA** requires a search volume to be defined. This is the volume, centered on the cell being estimated, which contains the samples to be used for grade estimation. In fact more than one search volume may be defined, so that different grades can have different search volumes. The parameters describing the search volume(s) are supplied using the Search Volume Parameter file **& SRCPARM**.

**Note** : **ESTIMA** parameter files can be imported and transformed for use in **[COKRIG](<cokrig.md>)** using the Advanced Estimation console's **[Parameters](<../STUDIO_RM/Multivariate_Import_Parameters.md>)** panel).

**ESTIMA** also requires a set of estimation parameters to be defined for each grade to be estimated. These parameters are also supplied to **ESTIMA** using a file - in this case the Estimation Parameter file. It will include items such as the estimation method, the search volume reference number and for example the power, if Inverse Power of Distance is selected.

**Note** : Search volume parameter files exported from the Advanced Estimation console cannot be used as an input to the **ESTIMA** process, or the **[ESTIMATE](<estimate.md>)** screen.

**ESTIMA** estimation methods include Nearest Neighbor, Inverse Power of Distance, and Sichel's t Estimator. MOD also includes Ordinary Kriging with a single structure spherical model variogram. The additional options in EGS are a choice of variogram models, lognormal kriging and Simple Kriging. Please consult your local Datamine office if you would like further information on these modules.

**Note** : When **COKRIG** or **ESTIMA** run Dynamic Anisotropy and less than 3 angles are used, the process replaces the missing angles with angles from the selected search or variogram.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "estima "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def estimate(self,
                retrieval="optional"):

        r"""
        ESTIMATE
        --------
        The process provides a comprehensive choice of methods and controls for estimating grades.  See [ESTIMATE Wizard](<../STUDIO_RM/EstimateDialog.md>).

Related topics and activities

  * [ESTIMATE Wizard](<../STUDIO_RM/EstimateDialog.md>)

  * [ESTIMA Process](<estima.md>)

  * [GRADE Process](<grade.md>)

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "estimate "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def export(self,
                retrieval="optional"):

        r"""
        EXPORT
        ------
        The **EXPORT** process allows data to be exported to a number of data sources by making use of Datamine's extensive Data Source Drivers.

**Note** : This process cannot be recorded as a macro, although it is possible to script the loading and saving of files in non-Datamine formats. Contact your local Datamine office for more information.

Process steps:

  1. Run the process.

  2. Select a Datamine file to export.

  3. Choose a **Driver Category** and Data Type.

  4. Complete the driver-specific screens that follow (press F1 for help at any time).

The file is exported in the chosen format.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "export "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def fdin(self,
                out_o="required",
                retrieval="optional"):

        r"""
        FDIN
        ----
        Create a Datamine model from a Whittle FOUR-D results file.

The processes [FDOUT](<fdout.md>) and FDIN provide the interface between your application and the standalone Whittle FOUR-D program for pit optimization.

The process [FDOUT](<fdout.md>) takes a Datamine model and creates two ASCII output files, which can be read by FOUR-D. When FOUR-D is run an output results file is created which can be read by FDIN along with the associated parameter file. A Datamine model is created. 

Your application creates external model and parameter files, and reads external result and parameter files. All optimization procedures are carried out within Whittle FOUR-D

The FOUR-D results file has a record per block with the following information:

  * Block coordinates - IX, IY, IZ

  * Total tonnes of ROCK in the block

  * Mining cost adjustment factor

  * Processing cost adjustment factor

  * Parcel information

  * Pit number.

The block model origin and cell structure is defined by the FOUR-D parameter file. The only additional field created in the output model is PIT for the Pit Number.

The process will read fixed format or comma separated results file formats.

The output model file is not written in IJK order, and must subsequently be sorted.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Undefined
            Output model file.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "fdin "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def fxin(self,
                out_o="required",
                filetype_p=1,
                retrieval="optional"):

        r"""
        FXIN
        ----
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Undefined
            Output model file.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        filetype:
            Type of input data file. 1 = Results file 2 = Pit List file 3 = Mining Sequence file
            Range=1,3
            Values=1,2,3
            Default=1
            Required=No

        """
        command = "fxin "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if filetype_p != "optional":
            try:
                val = float(filetype_p)
                if val not in [1.0, 2.0, 3.0]:
                    raise ValueError(f"filetype_p value {filetype_p} is not in allowed values: [1, 2, 3]")
            except ValueError as e:
                if isinstance(filetype_p, (int, float)):
                    raise e

        if filetype_p != "optional":
            command += " @filetype=" + str(filetype_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def grade(self,
                retrieval="optional"):

        r"""
        GRADE
        -----
        **Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

Interpolate a single grade into a block model using basic interpolation methods:

  * Nearest Neighbour

The Nearest Neighbour interpolation method simply assigns to the subcell the grade of the nearest sample. The definition of 'nearest' takes into account the anisotropy and orientation of the search ellipsoid. The Inverse Power of Distance method also takes account of the anisotropy and orientation of the search volume when assigning weights to the samples.

  * Inverse Power of Distance

For Inverse Power of Distance and Ordinary Kriging you may record the number of samples which are used to make each estimate. This is done by specifying a **NUMSAM** field. 

  * Ordinary Kriging

If you select Ordinary Kriging then you must also define a one or two structure spherical model variogram. It is assumed that any anisotropy in the variogram ranges has the same orientation as the search volume, but the actual values of the ranges are independent of the dimensions of the search volume. For Ordinary Kriging you may also record the kriged variance of the estimate by specifying a **VARIANCE** field.

Note: Only one grade field can be interpolated at a time. **[COKRIG](<cokrig.md>)** should be used when multiple grade fields need to be interpolated at a time.

For any method, you must specify an [input prototype block model](<../COMMON/filetype.md#BlockMod>), and an input sample data file. If the input prototype model contains cells and subcells then values are interpolated into the existing cell structure. If the prototype model is empty then cells and subcells are created if there are sufficient samples within the search volume.  
  
For kriging, a search volume is defined by a 3D ellipsoid which is centered on each subcell of the model in turn, and is used to select the samples for interpolating that subcell. You must define the lengths for the three axes of the ellipsoid, which may be different if you want an anisotropic volume. If you want a spherical search volume then set all three axes equal to the radius of the required sphere. You may orientate the search ellipsoid by specifying three sets of rotation angles and axes. The definition of the rotation angles and axes is described in section 3 of the Grade Estimation User Guide.  
  
You may select to use the zone control option by specifying a **ZONE** field. This will restrict the samples that are used for making the estimate to have the same **ZONE** value as the prototype model subcell. For example if both the prototype model and sample data files include a numeric rocktype field **ROCK** , then specifying **ZONE**(ROCK) will ensure that subcells which are rocktype N will be estimated using samples which are rocktype N.

The samples from the input sample file &**IN** can be weighted by specifying a **LENGTH** field.

**Note** : It frequently happens that samples are not evenly distributed around the subcell being estimated, but are clustered together. One way of minimizing this problem is to divide the search volume into octants and ensure that a minimum number of octants have samples in them. This is defined using the **MINOCT** , **MINPEROC** and **MAXPEROC** parameters.

### Input Files

**Name** |  **I/O Status** |  **Required** |  **Type** |  **Description**  
---|---|---|---|---  
PROTO |  Input |  Yes |  Block Model prototype |  Input prototype model. This must contain at least the fields **XC** , **YC** , **ZC** , **XINC** , **YINC** , **ZINC** , **XMORIG** , **YMORIG** , **ZMORIG** , **NX** , **NY** , **NZ** , **IJK**.  If the file contains cells and subcells, then these cells and subcells will be copied to the output model with the new grade field added. If the file does not contain cells and subcells then they will be created if there is sufficient data within the search ellipsoid.  
IN |  Input |  Yes |  Drillhole |  Input sample data. This must contain the X, Y and Z coordinates of each sample and the grade field (**VALUE**) to be estimated. This will usually be a drillhole file, but can be any file containing the four required fields  
  
### Output Files

**Name** |  **I/O Status** |  **Required** |  **Type** |  **Description**  
---|---|---|---|---  
MODEL |  Output |  Yes |  Block Model |  Output interpolated model. This will include all the fields in the input prototype model plus the estimated grade field (**VALUE**). In addition the number of samples field (**NUMSAM**) and the variance field (**VARIANCE**) will be included if they have been specified

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "grade "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def indest(self,
                x_f="optional",
                y_f="optional",
                z_f="optional",
                zone1_f_f="optional",
                zone2_f_f="optional",
                key_f="optional",
                length_f_f="optional",
                dens_f_f="optional",
                discmeth_p="optional",
                xpoints_p=1,
                ypoints_p=1,
                zpoints_p=1,
                xdspace_p="optional",
                ydspace_p="optional",
                zdspace_p="optional",
                parent_p="optional",
                mindisc_p=1,
                copyval_p="optional",
                fvaltype_p="optional",
                fstep_p="optional",
                xmin_p="optional",
                xmax_p="optional",
                ymin_p="optional",
                ymax_p="optional",
                zmin_p="optional",
                zmax_p="optional",
                xsubcell_p=1,
                ysubcell_p=1,
                zsubcell_p=1,
                order_p="optional",
                grmethod_p="optional",
                pgfields_p="optional",
                retrieval="optional"):

        r"""
        INDEST
        ------
        **Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

The INDEST process uses the Indicator Estimation (IE) method to estimate grades into a block model using the cumulative distribution function (CDF) of indicator transformed sample grades

To operate, INDEST needs a series of threshold values between the smallest and largest grade values. These threshold values, referred to as cutoffs, are used to numerically build the CDF of each block in the model. For each cutoff, data in the search volume are transformed into 0s and 1s: 1s if the data are greater than the threshold, and 0s if they are less than or equal. It then estimates the probability that the block grade is greater than the threshold value, using one of the standard estimation methods. This is usually kriging, but INDEST allows other methods such as Nearest Neighbour or Inverse Power of Distance to be used. Performing this operation for each cutoff across the range of the sample data approximates the CDF for the model cell. After the CDF is built, it is post processed to calculate the indicator estimated grade.

INDESTuses the ESTIMAprocess to do the estimation for each cutoff. For further details of ESTIMA.

If you are using Indicator Kriging (IK) then you must already have calculated a variogram for each cutoff, and stored the models in the Variogram Model file. The[VGRAM](<vgram.md>)process has specific features for calculating indicator variograms.

For each cutoff INDESTcalculates the following data which can optionally be stored in the **Output Model** file:

  * The proportion (fraction) of the model subcell which is above cutoff.

  * The grade of the proportion of the subcell which lies above cutoff.

The main output from INDESTis the grade above a cutoff of zero, ie the indicator estimated grade of the total subcell.

### Estimation Parameter File

In order to useINDESTyou must specify one record in the Estimation Parameter File &**ESTPARM** for each cutoff. This requires the numeric field **CUTOFF** to be included in the file.

The * **VALUE_IN** field is the grade in the input sample &**IN** file to which the cutoffs are applied. Note that this is different from the use of the * **VALUE_IN** field when using ESTIMATE for Indicator Estimation.

If the * **VALUE_OU** field is not specified then the * **VALUE_IN** field will be created in the output model file to hold the indicator estimated grade. If a * **VALUE_OU** field is specified in the first record of the Estimation Parameter File, then this value will be used for the indicator estimated grade in the output model file

You can only estimate one set of indicators in a single run. In other words all the **VALUE_IN** fields must be the same. Also when using **INDEST** you cannot estimate a grade using non indicator methods in the same run.

If you are using zone control then you must explicitly specify all combinations of zone field(s) in the Estimation Parameter File. You cannot use the option that is available in ESTIMA that allows you to specify an absent data zone field value that then applies to all zones that are not explicitly identified in&ESTPARM.

If you are using zone control then you may use different cutoffs for different zones. However the PRABn and GRABn fields in the output model file must then be handled very carefully! The maximum number of cutoff values is 24.

Fields for indicator estimation:

  * **BINGRADE** : Used when **GRMETHOD** =4 to set the grade below the cutoff

  * **ABVGRADE** : Sets the grade above the cutoff (only used for the top bin)

### Grade Above Cutoff

The calculation of the grade above each cutoff requires that the average grade between each successive pair of cutoffs be specified. For example if cutoff grades of 2, 5, 6.5 and 9.5g/t are selected then average grades are required for the ranges:

From  |  To  
---|---  
0 |  2  
2 |  5  
5 |  6.5  
6.5 |  9.5  
9.5 |  ∞  
  
Four methods are available to specify the average grade for each range, controlled by parameter @**GRMETHOD** :

GRMETHOD  |  Description  
---|---  
1 |  Average of minimum and maximum cutoff values. The grade above the highest cutoff is calculated as the highest cutoff plus half the difference between the highest and second highest cutoffs.  
2 |  Calculated by INDEST from the grades of the samples in the &**IN** file.  
3 |  Calculated by INDEST from the grades of the samples in the &**IN** file. However for the top bin (above the highest cutoff) the median grade is calculated.  
4 |  Values are specified by the user, using the **BINGRADE** and **ABVGRADE** fields in the &**ESTPARM** file. The **BINGRADE** field contains the grade below the cutoff and the **ABVGRADE** field the grade above the cutoff. The ABVGRADE field is therefore only used for the top bin.  
  
**GRMETHOD** of 4 is illustrated in the following table:

CUTOFF  | BINGRADE |  ABVGRADE   
---|---|---  
2 |  1.3 |  -  
5 |  3.6 |  -  
6.5 |  5.7 |   
9.5 |  7.8 |  11.1  
  
The values used by INDEST can be recorded by specifying an output &**AVGRADES** file.

### Indicators

Indicator values are calculated for each sample in the input sample &**IN** file for each cutoff. An indicator takes the value:

0 ‑ the grade is less than or equal to the cutoff.

1 ‑ the grade is above the cutoff.

The indicator values can be saved by specifying an output &**INDICATE** file.

###  Output Model 

Fields **PRAB1 ... PRAB** n will be created in the Output Model file to store the proportion of the subcell above each cutoff. These are calculated directly by ESTIMA. Then the fields **GRAB1 ... GRAB** n are calculated during the post-processing to store the corresponding grade above each cutoff. The grade above cutoff values (**GRABn**) are calculated from the proportion and average grade between each pair of cutoffs. For example:

Cutoff Number  |  Cutoff  |  PRABn  |  Calculation   
---|---|---|---  
4 |  9.5 |  0.1 |  GRAB4= 11.1 (This figure is taken directly from the ABVGRADE field)  
3 |  6.5 |  0.3 |  GRAB3= {0.1x11.1 + (0.3‑0.1)x7.8} / 0.3 = 8.9  
2 |  5 |  0.6 |  GRAB2= {0.1x11.1 + (0.3‑0.1)x7.8 + (0.6‑0.3)x5.7} / 0.6 = 7.3  
1 |  2 |  0.85 |  GRAB1= {0.1x11.1 + (0.3‑0.1)x7.8 + (0.6‑0.3)x5.7 + (0.85‑0.6)x3.6} / 0.85 = 6.21  
0 |  0 |  1 |  Indicator Grade=0.1x11.1 + (0.3‑0.1)x7.8 + (0.6‑0.3)x5.7 \+ (0.85‑0.6)x3.6 + (1.0‑0.85)x1.3 = 5.48  
  
The **PRABn** and **GRABn** fields will be stored in the output &**MODEL** file if parameter @PGFIELDS is set to 1.

### Order Relation

One of the main drawbacks of the indicator estimation method is the Order Relation Problem. This will occur if the proportion of the subcell above cutoff n is estimated to be less than the proportion above cutoff n+1. ie PRAB(n) < PRAB(n+1). Three options are available to correct for this, controlled by parameter ORDER:

=1: Downwards.  
=2: Upwards.  
=3: Average of methods 1 and 2.

The recommended method (and default) is 3.

### Input Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
PROTO |  Input |  Yes |  Block_Model_File |  Input model prototype. This is a standard block model file containing the 13 compulsory fields. It may also contain the rotated model fields. If it includes cells then it must be sorted on IJK.  
IN |  Input |  Yes |  Undefined |  Input sample data. This must contain X,Y and Z fields and at least one grade field.  
SRCPARM |  Input |  Yes |  Undefined |  Search volume parameter file.  This contains 24 compulsory fields defining the search volume and the number of samples needed for grade estimation. More than one search volume may be defined. All fields are numeric:

  * SREFNUM: Search volume reference number.
  * SMETHOD: Search volume shape.
  *     * 1 = 3D rectangle
    * 2 = ellipsoid.
  * SDIST1: Max search distance in direction 1.
  * SDIST2: Max search distance in direction 2.
  * SDIST3: Max search distance in direction 3.
  * SANGLE1: First rotation angle for search vol.
  * SANGLE2: Second rotation angle.
  * SANGLE3: Third rotation angle.
  * SAXIS1: Axis for 1st rotation (1=X,2=Y,3=Z).
  * SAXIS2: Axis for 2nd rotation (1=X,2=Y,3=Z).
  * SAXIS3: Axis for 3rd rotation (1=X,2=Y,3=Z).
  * MINNUM1: Min number of samples, 1st search vol.
  * MAXNUM1: Max number of samples, 1st search vol.
  * SVOLFAC2: Axis multiplying factor,2nd search vol.
  * MINNUM2: Min number of samples, 2nd search vol.
  * MAXNUM2: Max number of samples, 2nd search vol.
  * SVOLFAC3: Axis multiplying factor,3rd search vol.
  * MINNUM3: Min number of samples, 3rd search vol.
  * MAXNUM3: Max number of samples, 3rd search vol.
  * OCTMETH: Octant method flag.
    * 0=no octant search
    * 1=use octants
  * MINOCT: Minimum number of octants to be filled.
  * MINPEROC: Minimum number of samples in an octant.
  * MAXPEROC: Maximum number of samples in an octant.
  * MAXKEY: Maximum number of samples with the same key value within an octant.

  
ESTPARM |  Input |  Yes |  Undefined |  Estimation parameter file. Each record in the file describes an estimation method and its associated parameters. The fields are dependent on the estimation methods selected. All fields are optional except for **VALUE_IN** , **SREFNUM** and **CUTOFF**. General fields:

  * VALUE_IN: Grade field to be estimated.
  * SREFNUM: Search volume reference number.
  * CUTOFF: Cutoff grade for indicator calculation.
  * VALUE_OU: Output indicator estimated grade field to be created in **MODEL** (Default is **VALUE_IN**). The required field name must be specified in the first record of the Estimation Parameter file. Values in subsequent records will be ignored.
  * {ZONE1_F}: A/N 1st field for zonal estimation. The actual name of the field is given by the **ZONE1_F** field. e.g. **ZONE1_F**(**ROCK**).
  * {ZONE2_F}: A/N 2nd field for zonal estimation.
  * NUMSAM_F: Field to be created in MODEL for the number of samples.
  * SVOL_F: Field to be created in MODEL for dynamic search volume number.
  * VAR_F: Field to be created in MODEL for variance of estimate.
  * MINDIS_F: Field to be created in MODEL for distance to nearest sample.
  * IMETHOD: Estimation method.
    1. Nearest neighbour (NN)
    2. Inverse power of distance (IPD)
    3. Ordinary Kriging (OK)
    4. Simple Kriging (SK)
    5. Sichel's T Estimator

**Fields for IPD:**

  * ANISO: Anisotropy method:
    1. No anisotropy
    2. Use search volume anisotropy
    3. Use ANANGLEn
  * ANANGLE1: N Anisotropy angle 1.
  * ANANGLE2: N Anisotropy angle 2.
  * ANANGLE3:N Anisotropy angle 3.
  * ANDIST1: N Anisotropy distance 1.
  * ANDIST2: N Anisotropy distance 2.
  * ANDIST3: N Anisotropy distance 3.
  * POWER: N Power of distance for weighting.
  * ADDCON: N Constant added to distance.

Fields for kriging:

  * VREFNUM: Variogram model reference number.
  * LOG: N Lognormal variogram flag. 0 = normal kriging. 1 = lognormal kriging.
  * KRIGNEGW: N Treatment of -ve weights: 0 = -ve weights kept and used. 1 = ignore samples with -ve weights
  * KRIGVARS: N Treatment of variance > sill: 0 = write variance to MODEL. 1 = set variance to sill. Fields for lognormal kriging:
  * GENCASE: N Calculation method: 0 = Rendu's method. 1 = General case.
  * DEPMEAN: N Deposit mean [If 0 then use kriged estimate]. Fields for general case:
  * TOL: N Tolerance for convergence.
  * **MAXITER** : N Maximum number of iterations. Fields for simple kriging:
  * **LOCALMNP** : N Method for calculation of local mean: 1 = use field defined in PROTO 2 = use mean within search vol.
  * LOCALM_F: Name of local mean field in PROTO; used if LOCALMNP=1

Fields for indicator estimation

  * **BINGRADE** : Used when **GRMETHOD** =4 to set the grade below the cutoff

  * **ABVGRADE** : Sets the grade above the cutoff (only used for the top bin)

  
VMODPARM |  Input |  No |  Variogram \- Model |  Variogram model parameter file.  Each record in this file defines a variogram model type and its parameters. Only the VREFNUM field is compulsory.

  * VREFNUM: Model variogram reference number.
  * VANGLE1: Variogram anisotropy angle 1.
  * VANGLE2: Variogram anisotropy angle 2.
  * VANGLE3: Variogram anisotropy angle 3.
  * VAXIS1: Model variogram rotation axis 1.
  * VAXIS2: Model variogram rotation axis 2.
  * VAXIS3: Model variogram rotation axis 3.
  * NUGGET: Nugget variance.
  * ST1: Variogram model type for structure 1.
    1. Spherical
    2. Power
    3. Exponential
    4. Gaussian
    5. De Wijsian
  * ST1PAR1: 1st parameter of structure 1 [Range 1 for spherical model].
  * ST1PAR2: 2nd parameter of structure 1 [Range 2 for spherical model].
  * ST1PAR3: 3rd parameter of structure 1 [Range 3 for spherical model].
  * ST1PAR4: 4th parameter of structure 1 [C variance for spherical model].
  * STn: Variogram model type for structure n. STnPARp pth parameter for structure n, where n<=9.

  
  
### Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODEL |  Output |  No |  Block Model File |  Output model containing estimated grades, variance etc.  
AVGRADES |  Output |  No |  Undefined |  Output file containing cutoff grade ranges and average grade used for each range. It will include zone field(s), if any, plus the following fields: 

  * **BIN** : bin or grade range number 
  * **LO_CUT** : lower cutoff grade 
  * **UP_CUT** : upper cutoff grade 
  * **NSAMPLES** : number of samples in IN file lying within the bin 
  * **BINGRADE** : bin grade used for indicator kriging. This is dependent on the **GRMETHOD** parameter . 
  * **SAMPMEAN** : mean grade of samples in IN file lying within the bin 

  
INDICATE |  Output |  No |  Undefined |  Output indicator file. This is a copy of the sample input IN file, but also includes the 0/1 indicator values for each cutoff  
SAMPOUT |  Output |  No |  Undefined |  Output sample file containing details of weights for each sample for each cell estimated.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        x: Numeric : IN
            X coordinate of sample data in IN file. If not specified, then X is assumed.
            Default=Undefined
            Required=No

        y: Numeric : IN
            Y coordinate of sample data in IN file. If not specified, then Y is assumed.
            Default=Undefined
            Required=No

        z: Numeric : IN
            Z coordinate of sample data in IN file. If not specified, then Z is assumed.
            Default=Undefined
            Required=No

        zone1_f: Any : IN
            First field for zonal control.
            Default=Undefined
            Required=No

        zone2_f: Any : IN
            Second field for zonal control.
            Default=Undefined
            Required=No

        key: Numeric : IN
            Key field used to specify the field limiting the number of samples for estimation. The
            field must exist in the IN file.
            Default=Undefined
            Required=No

        length_f: Numeric : IN
            Field used for length weighting in IPD. The field must exist in the IN file.
            Default=Undefined
            Required=No

        dens_f: Numeric : IN
            Field used for density weighting in IPD. The field must exist in the IN file.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        discmeth:
            Cell discretisation method:
            Range=
            Values=
            Default=
            Required=No

        xpoints:
            Number of discretisation points in X. (1)
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        ypoints:
            Number of discretisation points in Y. (1)
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        zpoints:
            Number of discretisation points in Z. (1)
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        xdspace:
            Distance between discretisation points in X if DISCMETH=2. The default gives just one
            point.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        ydspace:
            Distance between discretisation points in Y if DISCMETH=2. The default gives just one
            point.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        zdspace:
            Distance between discretisation points in Z if DISCMETH=2. The default gives just one
            point.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        parent:
            Flag to control parent cell estimation:
            Range=
            Values=
            Default=
            Required=No

        mindisc:
            Minimum number of discretisation points. Only used if PARENT=2. The default is (1).
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        copyval:
            Flag controlling copying of values from PROTO to MODEL if there is insufficient data to
            estimate them:
            Range=
            Values=
            Default=
            Required=No

        fvaltype:
            Flag for cell size approximation for F values:
            Range=
            Values=
            Default=
            Required=No

        fstep:
            Step size for cell approximation. This is only used if **FVALTYPE** =2.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        xmin:
            Minimum X value for model updating. The default is the X model origin.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        xmax:
            Maximum X value for model updating. The default is the maximum X value for **PROTO**.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        ymin:
            Minimum Y value for model updating. The default is the Y model origin.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        ymax:
            Maximum Y value for model updating. The default is the maximum Y value for **PROTO**.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        zmin:
            Minimum Z value for model updating. The default is the Z model origin.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        zmax:
            Maximum Z value for model updating. The default is the maximum Z value for **PROTO**.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        xsubcell:
            Number of subcells per parent cell in X if **PROTO** is empty. The default is (1).
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        ysubcell:
            Number of subcells per parent cell in Y if **PROTO** is empty. The default is (1).
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        zsubcell:
            Number of subcells per parent cell in Z if **PROTO** is empty. The default is (1).
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        order:
            Order relation correction method:
            Range=
            Values=
            Default=
            Required=No

        grmethod:
            Method for specifying average grade within each cutoff range:
            Range=
            Values=
            Default=
            Required=No

        pgfields:
            Flag to select whether the proportion above cutoff fields (PRABn) and the grade above
            cutoff fields (GRABn) should be included in the output MODEL file:
            Range=
            Values=
            Default=
            Required=No

        """
        command = "indest "

        if x_f != "optional":
            command += " *x=" + x_f

        if y_f != "optional":
            command += " *y=" + y_f

        if z_f != "optional":
            command += " *z=" + z_f

        if zone1_f_f != "optional":
            command += " *zone1_f=" + zone1_f_f

        if zone2_f_f != "optional":
            command += " *zone2_f=" + zone2_f_f

        if key_f != "optional":
            command += " *key=" + key_f

        if length_f_f != "optional":
            command += " *length_f=" + length_f_f

        if dens_f_f != "optional":
            command += " *dens_f=" + dens_f_f

        if discmeth_p != "optional":
            command += " @discmeth=" + str(discmeth_p)

        if xpoints_p != "optional":
            command += " @xpoints=" + str(xpoints_p)

        if ypoints_p != "optional":
            command += " @ypoints=" + str(ypoints_p)

        if zpoints_p != "optional":
            command += " @zpoints=" + str(zpoints_p)

        if xdspace_p != "optional":
            command += " @xdspace=" + str(xdspace_p)

        if ydspace_p != "optional":
            command += " @ydspace=" + str(ydspace_p)

        if zdspace_p != "optional":
            command += " @zdspace=" + str(zdspace_p)

        if parent_p != "optional":
            command += " @parent=" + str(parent_p)

        if mindisc_p != "optional":
            command += " @mindisc=" + str(mindisc_p)

        if copyval_p != "optional":
            command += " @copyval=" + str(copyval_p)

        if fvaltype_p != "optional":
            command += " @fvaltype=" + str(fvaltype_p)

        if fstep_p != "optional":
            command += " @fstep=" + str(fstep_p)

        if xmin_p != "optional":
            command += " @xmin=" + str(xmin_p)

        if xmax_p != "optional":
            command += " @xmax=" + str(xmax_p)

        if ymin_p != "optional":
            command += " @ymin=" + str(ymin_p)

        if ymax_p != "optional":
            command += " @ymax=" + str(ymax_p)

        if zmin_p != "optional":
            command += " @zmin=" + str(zmin_p)

        if zmax_p != "optional":
            command += " @zmax=" + str(zmax_p)

        if xsubcell_p != "optional":
            command += " @xsubcell=" + str(xsubcell_p)

        if ysubcell_p != "optional":
            command += " @ysubcell=" + str(ysubcell_p)

        if zsubcell_p != "optional":
            command += " @zsubcell=" + str(zsubcell_p)

        if order_p != "optional":
            command += " @order=" + str(order_p)

        if grmethod_p != "optional":
            command += " @grmethod=" + str(grmethod_p)

        if pgfields_p != "optional":
            command += " @pgfields=" + str(pgfields_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inpddf(self,
                out_o="required",
                print_p=0,
                retrieval="optional"):

        r"""
        INPDDF
        ------
        Input a complete file, including its Data Definition, in a standard format (as generated by the [OUTPUT](<output.md>) process) from a character external system file.

The format of the file read by **INPDDF** is as follows:

Data Definition

Contents  |  Format   
---|---  
<file name> |  20A4 (not used)   
<file description> |  20A4   
<Total fields> |  <Explicit fields> 2I8 (words)  
  
For the total number of fields above, one record per field (or per 4 characters for alphanumeric fields):-  

<Field name> |  N/A <length>  
---|---  
<ISWD pointer> <Char default> |  2A4,1X,A1,2I4,  
<numeric default> |  4X,A4,E14.6  
  
The character default is only set for alphanumeric fields; the numeric is only set for numeric fields. The ISWD pointer is absent (zero) for implicit fields, or the sequential word number in the file for explicit fields.

### Data Records

Data records have entries for explicit fields only; all numeric fields will be output in either F or E format, depending on magnitude. Each number will be 12 characters long (e.g. F12.0). All alphanumeric fields will be read in multiples of A4, without spaces, except where an alphanumeric field follows a numeric field, in which case there will be 4 blanks left before the start of the alphanumeric field.  
  
Errors in the DD format will cause the process to be abandoned with an error message; errors in the data format will cause each record in error to be displayed with an error message, and the record ignored.  
  
The maximum record width that may be handled is 240 characters.  
  
The characters !! in positions 1 and 2 are used internally to terminate the data; therefore no record should start with !!.  
  
The following messages are output to the display when using INPDDF with a catalogue file input:
    
    
    >>> OPERATING ON A CATALOGUE FILE INPUT <<<  
      
    >>> COPYING IN FILE file1  
    >>> 99999999 RECORDS IN FILE file 1  
    >>> COPYING IN FILE file2  
    >>> 99999999 RECORDS IN FILE file 2

        Input Files:
        ------------

        Output Files:
        -------------

        out: Table
            Database file to be created. If OUT is a catalogue file, then all files in the
            catalogue will be input.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        print:
            >=1 to display each record (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "inpddf "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inpfil(self,
                out_o="required",
                print_p=0,
                retrieval="optional"):

        r"""
        INPFIL
        ------
        Creates a file and enters free format data into it. Free format data is separated by commas.

The data may come either from the keyboard, or from a system file external to the database.

**INPFIL** acts like a combination of [INPUTD](<inputd.md>) & [INDATA](<indata.md>). Records may not start with the character !. This is because the ! symbol acts as the end-of-data character. Thus macro files should not be read in with INPFIL; use [INPUTC](<inputc.md>) instead.

**Note** : within a macro, the Data Definition cannot be terminated by the ! character, as this will terminate the **INPFIL** process; instead another special purpose character (such as [) may be used.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Table
            File to be created.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        print:
            >=1 to display each record (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "inpfil "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inpfml(self,
                out_o="required",
                print_p=0,
                retrieval="optional"):

        r"""
        INPFML
        ------
        Creates a file and enters data of fixed format into it. The data may come either from the keyboard, or from a system file external to the database; the system file records must be no longer than 80 characters.

The data format may come either from the file description, entered when the Data Definition is requested, or from the format line.

1\.  |  INPFML may be considered as a combination of [INPUTD](<inputd.md>). Incorrect data records (i.e. not matching the specified format statement) will be ignored, with a message to the display.  
---|---  
|  |   
2. |  Records may not start with !. This is because the ! symbol acts as the end-of-data character.  
|  |   
3. |  Macro files, in which each command starts with !, are best entered through [INPUTC](<inputc.md>).  
|  |   
4. |  Within a macro, the Data Definition cannot be terminated by the ! character, as this will terminate the **INPFML** process; instead another special purpose character (such as [) may be used.  
|  |   
5. |  The user is prompted for the following information  
|  >FILE DESCRIPTION > |  Up to 60 character text file description, or a FORTRAN format in brackets, defining the format of data to be read in (e.g. by the INPUTF or INPUTW processes). Order of fields is that in the DD and the type of each field must match that in the DD. Character data must be in A4 units (e.g. 3A4,A2), numbers in E, F or G format (e.g. 3F12.0), integers as F format (e.g. F6.0) and X for spaces. Maximum length of format statement is 80 characters, including the enclosing brackets, and maximum length of data record to which format applies is also 80 characters.  
|  > NEXT FIELDNAME > |  Up to 24 character field 'name'. May be upper or lower case text, numbers, or special symbols. Internal blanks in field names should be avoided, and _ / . - used instead. Fields should not start with !, *, & or @, as such names will give rise to syntax problems under some circumstances.  
|  > TYPE A/N (N) > |  A for alphanumeric field, N or return for numeric field.  
|  > LENGTH (1) > |  Length in characters for alphanumeric fields only. Question omitted for numeric fields.  
|  > STORED? (Y) > |  Y or return for explicit fields, N for implicit (file constant) fields. Implicit fields are not supplied in data records.  
|  > DEFAULT > |  Default value to replace absent data (in processes which carry out this replacement). Just <return> for blank default value for alphanumeric and zero for numeric fields. For implicit fields the constant values must be entered.  
|  The above is repeated for each field until ! entered for NEXT FIELDNAME. Then:  
|  > CONFIRM? > |  OK, ok, YES, Y or y to end DD.  
|  > SYSFILE > |  External system file name from which the formatted data is to be read, or return for entry from the keyboard. Format of the system file name is system specific, with a maximum of 56 characters allowed, including pathnames.  
|  > FORMAT > |  FORTRAN format in brackets, defining the format of data records to be read. Order of fields is that in the DD and the type of each field must match that in the DD. Character data must be in A4 units (e.g. 3A4,A2), numbers in E, F or G format (e.g. 3F12.0), integers as F format (e.g. F6.0) and X for spaces. Maximum length of format statement is 80 characters, including the enclosing brackets, and maximum length of data record to which format applies is also 80 characters. If format is already in the FILE DESCRIPTION, then enter just return.  
|  > DATA > |  If no SYSFILE, data lines in defined format. ! terminates.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Table
            File to be created.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        print:
            >=1 to display each record (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "inpfml "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inputc(self,
                out_o="required",
                print_p=0,
                retrieval="optional"):

        r"""
        INPUTC
        ------
        Creates a text file of standard form, with 80 characters per record. The Data Definition is set up automatically to contain a single alphanumeric field of length 20 words (80 characters) with the fieldname T.

The data may optionally be read from a system file external to the database. This is useful to set up character files e.g. macros \- which have been created outside a database.

Blank lines within the external file are loaded (as far as the record count is concerned) but are ignored in all processing, as blank is absent data within a text field.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Table
            File to be created.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        print:
            >=1 to display each record (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "inputc "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inputd(self,
                out_o="required",
                retrieval="optional"):

        r"""
        INPUTD
        ------
        Creates a file containing a Data Definition only. Such files may be used in subsequent data input and processing functions.

### Use of the ! Character

The ! character, entered at the FIELDNAME > prompt, normally is used to terminate Data Definition entry. Entered at any other prompt, the ! character has the effect of canceling the entry for the existing fieldname, and dropping control back to the FIELDNAME > prompt. 

Within a macro, the Data Definition cannot be terminated by the ! character, as this will terminate the [INPFML](<inpfml.md>) process; instead another special purpose character (such as [) may be used. 

### Prompts

When INPUTD is run, you are prompted for the following information in the Command toolbar:

  * > FILE DESCRIPTION >

Up to 24 character field 'name'. May be upper or lower case text, numbers, or special symbols. Internal blanks in field names should be avoided, and _ / . - used instead. Fields should not start with !, *, & or @, as such names will give rise to syntax problems under some circumstances.

  * > TYPE A/N (N) >

A for alphanumeric field, N or return for numeric field.

  * > LENGTH (1) >

Length in characters for alphanumeric fields only. Question omitted for numeric fields.

  * > STORED? (Y) >

Y or return for explicit fields, N for implicit (file constant) fields. Implicit fields are not supplied in data records.

  * > DEFAULT >

Default value to replace absent data (in processes which carry out this replacement). Just <return> for blank default value for alphanumeric and zero for numeric fields. For implicit fields the constant values must be entered.

The above is repeated for each field until ! entered for NEXT FIELDNAME. Then:

  * > CONFIRM? >

OK, ok, YES, Y or y to end DD.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Table
            File to be created.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "inputd "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def link(self,
                out_o="required",
                retrieval="optional"):

        r"""
        LINK
        ----
        Important: This command is maintained for macro backward compatibility with earlier product versions released before the advent of the Studio range. The **LINK** process is intended to only be run from macros.

LINK may be used to create a new Datamine file inside the project folder, by linking an existing Datamine binary file located outside of the project folder.  
  
LINK with a catalogue file input may be used to restructure a set of Datamine files in the project folder. First files are unlinked (!UNLINK) individually; your application is exited (!**LOGOFF**); the existing database is deleted using system delete commands; your application is then re-entered, re-creating the database; then !**LINK** is entered using the catalogue file copied out previously.

The length of the system file name, including the full path name, is restricted to 56 characters.

The database file name is attached to symbolic file &**OUT**. The name of the external binary file is requested interactively.

**Note** : The external file name cannot be a catalogue file.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Table
            Database file name.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "link "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def listdr(self,
                out_o="optional",
                fieldnam_f="optional",
                retrieval="optional"):

        r"""
        LISTDR
        ------
        Creates a list of all Datamine files within the project folder.

Wildcarding is supported and an output catalogue file can be generated. Filenames or filename templates may be entered as retrieval criteria. The form is:- ?<string>?.<string> or:- ?<string>?.? Please Note: This command is only available from macros. The use of a catalogue file is backwards compatible but note that file names are restricted to a maximum of twenty (20) characters.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Catalogue
            Output catalogue file, giving list of files to be used by processes
            **[APPEND](<append.md>)** , **[DELETE](<delete.md>)** , [DISPLA](<displa.md>),
            [INPDDF](<inpddf.md>), [LIST](<list.md>) and [OUTPUT](<output.md>).
            Required=No

        Fields:
        -------

        fieldnam: Any : 
            Name of field in **OUT** containing file paths
            Default=Undefined
            Required=No

        Parameters:
        -----------

        """
        command = "listdr "

        if out_o != "optional":
            command += " &out=" + out_o

        if fieldnam_f != "optional":
            command += " *fieldnam=" + fieldnam_f

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def loadcf(self,
                print_p=0,
                level_p=0,
                encrypt_p=0,
                retrieval="optional"):

        r"""
        LOADCF
        ------
        Convert a macro file (*.mac) into a standard menu file (*.men) for faster execution.

LOADCF pre-processes macros to increase their general runtime performance. Specific optimization can be performed for customized SCREEN based menu applications. Three levels of processing (controlled by setting parameter LEVEL in the dialog) are available:  

LEVEL = 0 Converts the macro file into the standard .STK and .MEN files.  

LEVEL = 1 Optimizes the performance for screen based menus with the following:

  1. Pre-processes and verifies !SCREEN definitions to create 'tokenized' SCreen Code (.SCC) and SCreen Text (.SCT) files for the menu.
  2. Replaces !SCREEN code with references to relevant entries in .SCC file.
  3. Strips !REM and # inline remarks, remove indentation.

**Note** : If there is more than one macro in the file to be loaded, only the first macro will be loaded. .

You can choose the name of the binary random access menu file to be created. This may be up to 56 characters long, and may include pathnames. It must not contain the character '.', except as part of an up to three character extension. If an extension is given, it will be used; otherwise an extension of form .MEN will be appended. The following are legal menu names:-

  * mymenu.men

  * Datamine/mymenu.dat

If the response to the menu name question is blank<return> or just <return>, then a name MENUFILE.DAT will be assumed. This is for compatibility with earlier releases of Datamine products.

The menu name set up in !**LOADCF** is the one that must be specified in the !**menu** or !**nomenu** commands.

Note: The !**LOADCF** process deletes the stack file <name>.STK, where <name> is the requested macro name minus the extension.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        print:
            Macro line display (0). =0 Do not display.=1 Display each line of the macro file as
            loaded.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        level:
            Level of menu compilation . =0 Standard compilation. =1 'Optimise' for !SCREEN
            processing (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        encrypt:
            Encryption level (0). =0 None. =1 Macro is encrypted
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "loadcf "

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if level_p != "optional":
            try:
                val = float(level_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"level_p value {level_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(level_p, (int, float)):
                    raise e

        if level_p != "optional":
            command += " @level=" + str(level_p)

        if encrypt_p != "optional":
            try:
                val = float(encrypt_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"encrypt_p value {encrypt_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(encrypt_p, (int, float)):
                    raise e

        if encrypt_p != "optional":
            command += " @encrypt=" + str(encrypt_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def monaco(self,
                out_o="required",
                nrecs_p="required",
                retrieval="optional"):

        r"""
        MONACO
        ------
        Create random numbers.

**Note** : this process is retained for legacy macro support only. Consider using the **[RANDOM](<random.md>)** process instead.

MONACO requires only an OUT file specification and NRECS to determine how many random number records to create. This file is populated by further information supplied by you when the process is run.

To generate random number output with MONACO:

  1. Run the **MONACO** process.

  2. Enter the **OUT** file name. This file is generated in your project folder with either a .dm or .dmx extension.

  3. Select the Parameters tab.

  4. Enter the number of records (NRECS) to create in the output file.

  5. Click **OK** to launch the process.

  6. In the **Output** window, enter the name of the **FIELD** to create in the output file. This numeric field will contain random value records, one per row where the total number of rows = **NRECS**.

  7. Choose a random distribution **TYPE** from the following options:

     * 1 UNIFORM IN RANGE 0 TO 1
     * 2 EXPONENTIAL WITH PARAMETER P1
     * 3 NORMAL, MEAN P1, STDEV P2
     * 4 LAPLACE, MEAN P1, SPREAD P2
     * 5 EXTREME VALUE, PARAMETERS P1,P2
     * 6 CAUCHY, CENTRE P1, SPREAD P2
     * 7 LOGNORMAL, LOG MEAN P1, LOG STDEV P2
  8. If another **FIELD** is required in the output file (for additional random values), repeat steps 6 and 7.

  9. Enter "!" and press ENTER to create the file.

**Note** : you can also generate random numbers using the **[EXTRA](<extra.md>)** process.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Undefined
            Output file
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        nrecs:
            Number of records required in output file
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=Yes

        """
        command = "monaco "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if nrecs_p == "required":
            raise ValueError("nrecs_p is required.")

        if nrecs_p != "optional":
            command += " @nrecs=" + str(nrecs_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def picdir(self,
                out_o="required",
                file_f="optional",
                append_p=0,
                print_p=0,
                sort_p=0,
                longname_p=0,
                retrieval="optional"):

        r"""
        PICDIR
        ------
        Writes file names to an output file (catalogue file) if the file name or field names within the file match the given pattern expressions.

### Expression Syntax

In the following text all keywords are capitalized. When running **PICDIR** , any keyword may be entered in either uppercase or lowercase and abbreviated to its first three (or more) characters.

The syntax of a pattern matching expression is:

|  [FILE] |  [REGEXP] |  <pattern> |   
---|---|---|---|---  
or |  FIELD |  [REGEXP] |  <pattern> |   
or |  FIELD |  <kind> |  |   
or |  FIELD |  [REGEXP] |  <pattern> , |  <kind>  
  
The keyword "FILE" is optional. If a pattern is to be matched against field names, the keyword "FIELD" must be included. The field "kind" will be matched against the type (numeric or alphanumeric) and storage class (explicit or implicit) of the fields in any file.

The keyword "REGEXP" is normally omitted, in which case "pattern" may consist of literal characters to be matched, or one of the following elements:

? |  Any single character  
---|---  
* |  Wildcard. A group of zero or more characters  
[...] |  Any one of the characters enclosed in the square brackets. The short hand notation "a-z" means any lowercase letter; refer to the examples below for more details.  
[^...] |  Any character except one of these  
  
The special meaning of a character (e.g. "*") is lost if the character is preceded by "\", hence the match a literal "*", use "\\*". Quotes (double or single) may be used to enclose patterns if desired.

Where a pattern is applied to file names, lower case letters are translated into upper case before the pattern is used.

If the keyword "REGEXP" is used, the pattern specifies a full regular expression. Regular expressions allow advanced users to make more complex selections than are possible by using the pattern elements specified above.

A regular expression in **PICDIR** may contain the following elements.

% |  Matches the beginning of the file or field name  
---|---  
$ |  Matches the end of the file or field name  
* |  Zero or more occurrences of the preceding pattern element.  
? |  As above  
[...] |  As above  
[^...] |  As above  
  
The "kind" is a list of field type or storage class specifiers, separated by commas. Keywords that specify field type are "NUMERIC" or "ALPHANUMERIC". Storage classes are "EXPLICIT" or "IMPLICIT". Of course, any of these may be abbreviated to three (or more) letters.

If more than one type or class keyword is given, the last one specified is used.

### Concatenation of Expressions

The result of a pattern matching expression is either TRUE or FALSE. 

Any result may be inverted by preceding the expression by the keyword "NOT" (for example, "NOT XPICRT,IMPLICIT"). Two expressions may be joined together by "AND" or "OR" operators. The result is another expression. 

The "AND" operator has higher precedence than "OR". Parentheses (brackets) may be used to override the normal order of evaluation of expressions.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Catalogue
            Output catalogue file, giving list of files.
            Required=Yes

        Fields:
        -------

        file: Character : OUT
            Optional name for the field that is to contain the file names. The default is
            "'FILENAM", i.e. PICDIR will produce a catalogue file.
            Default=FILENAM
            Required=No

        Parameters:
        -----------

        append:
            If set to 1 then selected field names will be appended to the **OUT** file, provided it
            exists and has a valid DD (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        print:
            Options: 0: No display of matching file names >0 Display file names as they are
            selected. (0)
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        sort:
            If set to 1 then the output file will be sorted after all file names have been written
            to it (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        longname:
            If set to 1 then the fields **LOGICAL** (5A4) and **SYSTEM** (32A4) will be added to
            the output file. **LOGICAL** is the full, logical (long) name of the file. **SYSTEM**
            contains the full path name of the file. The default for **LONGNAME** is (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "picdir "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if file_f != "optional":
            command += " *file=" + file_f

        if append_p != "optional":
            try:
                val = float(append_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"append_p value {append_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(append_p, (int, float)):
                    raise e

        if append_p != "optional":
            command += " @append=" + str(append_p)

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if sort_p != "optional":
            try:
                val = float(sort_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"sort_p value {sort_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(sort_p, (int, float)):
                    raise e

        if sort_p != "optional":
            command += " @sort=" + str(sort_p)

        if longname_p != "optional":
            try:
                val = float(longname_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"longname_p value {longname_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(longname_p, (int, float)):
                    raise e

        if longname_p != "optional":
            command += " @longname=" + str(longname_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def picted(self,
                retrieval="optional"):

        r"""
        PICTED
        ------
        Interactive display and manipulation of Datamine plot files to produce composite plots.

PICTED allows different plot files to be displayed concurrently, and permits rescaling and positioning of individual plots. The composite picture created in this way may be saved to an output *.dm format plot file.

### Process Options

On running the process, the following options are displayed:

  1. SET PLOT DIMENSIONS IN MM

  2. DISPLAY A FILE (AND ADD TO ACTIVE LIST)

  3. SET/CHANGE OFFSETS/SCALES

  4. REMOVE FILE FROM ACTIVE LIST

  5. SAVE DISPLAY INTO NEW PLOT FILE

  6. REFRESH DISPLAY

  7. HARDCOPY CURRENT DISPLAY

  8. EXIT

Each of the above options generates subsidiary interactions:

  1. For SET PLOT DIMENSIONS IN MM:

    
    
    CURRENT PLOT DIMENSIONS ARE : X = XXX.XX, Y = YYY.YY
    
    
    >>> SET NOMINAL PLOT SIZE IN MM>
    
    
    X > Supply X plot dimension.
    
    
    Y > Supply Y plot dimension.
    
    
    FILE > Supply plot file name.
    
    
    >>> EXPAND (>1) OR REDUCE (<1) FACTOR >
    
    
    X > Supply X scaling factor.
    
    
    Y > Supply Y scaling factor.
    
    
    >>> X AND Y OFFSETS IN MM --
    
    
    X > Supply X offset from picture origin for the local origin of
    
    
    the current plot file.
    
    
    Y > Supply Y offset from picture origin for the local origin of
    
    
    the current plot file.
    
    
    SET OR CHANGE SCALES AND OFFSETS
    
    
    >>> N FILES ACTIVE ---
    
    
    >>>================================================
    
    
    >>> FILENAME FILE LIMITS SCALED BY OFFSETS
    
    
    >>> X Y X Y X Y
    
    
    >>>================================================
    
    
    >>> xxxxxxxx nn.n nn.n nn.n nn.n nn.n nn.n

  2. For DISPLAY A FILE (AND ADD TO ACTIVE LIST):

The Project Browser is displayed in order to select the required plot file.

  3. For SET/CHANGE OFFSETS/SCALES:

Scales and offsets are prompted for, as for option 2.

  4. For REMOVE FILE FROM ACTIVE LIST:

The Project Browser dialog is displayed in order to select the required plot file.
    
    
    REMOVE FILE FROM ACTIVE LIST
    
    
    >>> CURRENTLY ACTIVE FILES ARE --
    
    
    >>> xxxxxxxx
    
    
    >>> yyyyyyyy

  5. For SAVE DISPLAY INTO NEW PLOT FILE:

The Project Browser is displayed in order to define the required output plot file location and name.

  6. For REFRESH DISPLAY:

The Graphics widow display is cleared and regenerated from the plot files in the active list.

  7. For HARDCOPY CURRENT DISPLAY:

This function is not available.

  8. For EXIT

The **PICTED** process is terminated.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "picted "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def protom(self,
                out_o="required",
                rotmod_p=0,
                retrieval="optional"):

        r"""
        PROTOM
        ------
        This process creates a block model data definition, also known as a 'prototype'.

Default values are set up by the process, based on the user's response to a series of interactive prompts. The prototype model is created in the form required by all of the orebody modeling processes.

By default the prototype model is defined orthogonal to the world coordinate system. However the parameter @ROTMOD allows a local coordinate system to be defined which can include both an origin translation and up to three rotations. The method for defining the translation and rotations is consistent with the **[CDTRAN](<cdtran.md>)** process.

**Note** : You can also create a prototype model using the [Create Model Prototype](<../COMMON/CreateModelPrototype_Dialog.md>) screen.

### Interactive Prompts

**PROTOM** , if run interactively, requires additional information to be provided using the Command toolbar.

The first two interactive prompts are independent of the value of @ROTMOD:
    
    
    >>>> IS A MINED-OUT FIELD REQUIRED? Y/(N) >

Y to include a field MINED in the output prototype.
    
    
    >>>> ARE SUBCELLS TO BE USED? Y/(N) >

Y to allow the model to include sub-cells.

If **ROTMOD** =0, you are prompted to enter the coordinates of the model origin
    
    
    >>>>     PLEASE SUPPLY CO-ORDINATES OF MODEL ORIGIN
    
    
    X >     X Co-ordinate.
    
    
    Y >     Y coordinate.
    
    
    Z >     Z coordinate.

If **ROTMOD** =1, you prompted to enter the model origin in both the world and local coordinate systems:
    
    
    >>>> PLEASE SUPPLY COORDINATES OF MODEL ORIGIN IN THE WORLD COORDINATE SYSTEM.>>>
    
    
    X0 >     X coordinate
    
    
    Y0 >     Y coordinate
    
    
    Z0 >     Z coordinate
    
    
    >>>> NOW ENTER THE SAME MODEL ORIGIN POINT SPECIFIED IN THE LOCAL COORDINATE SYSTEM.>>>
    
    
    X >     X coordinate
    
    
    Y >     Y coordinate
    
    
    Z >     Z coordinate

If **ROTMOD** =1 , you are prompted to enter the three rotation axes and corresponding rotation angles. The three axes X,Y and Z are denoted as axes 1,2 and 3 respectively. A rotation about angle 'N' is measured positively in the clockwise direction when viewed along axis N from high values to low values. For example a rotation of 35 degrees about axis 1 represents a dip of 35 degrees downwards from the horizontal plane. The first rotation angle must be 1,2 or 3. If only one rotation is required then the second and third rotation axes should be defined as zero.
    
    
    >>> NOW ENTER THE MODEL ROTATION ANGLES >>>
    
    
    ROTATION 1: ANGLE (-360 TO +360) >

First rotation angle.
    
    
    AXIS (1, 2 OR 3) >

Axis about which first rotation is applied.
    
    
    ROTATION 2: ANGLE (-360 TO +360) >

Second rotation angle.
    
    
    AXIS (0,1,2 OR 3) >

Axis about which second rotation is applied.
    
    
    ROTATION 3: ANGLE (-360 TO +360) >

Third rotation angle.
    
    
    AXIS (0,1,2 OR 3) >

Axis about which third rotation is applied.

Whatever the value of ROTMOD the user is finally prompted for the cell dimensions and the number of cells:
    
    
    >>> PLEASE SUPPLY CELL DIMENSIONS
    
    
    X >     Cell dimension in X.
    
    
    Y >     Cell dimension in Y.
    
    
    Z >     Cell dimension in Z.
    
    
    >>>> NUMBER OF CELLS IN EACH DIRECTION
    
    
    X >     Number of cells in X.
    
    
    Y >     Number of cells in Y.
    
    
    Z >     Number of cells in Z.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Block Model Prototype
            Output prototype model file.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        rotmod:
            Select 1 to generate a prototype for a rotated block model, or 0 (zero, the default)
            for a non-rotated prototype.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "protom "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if rotmod_p != "optional":
            try:
                val = float(rotmod_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"rotmod_p value {rotmod_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(rotmod_p, (int, float)):
                    raise e

        if rotmod_p != "optional":
            command += " @rotmod=" + str(rotmod_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def protop(self,
                out_o="required",
                retrieval="optional"):

        r"""
        PROTOP
        ------
        To create a prototype plot file with defined plot and data area shape/size, and optionally data ranges and scaling factors.

**PROTOP** is the first process to be used before plotting starts. It defines the prototype that will subsequently be used by plot processes. The main parts defined are the plot region (the total true size of the plot) and, within this, the data area, into which most plot processes will place plotted data. Sizes are defined in millimeters, and may be measured from existing plots, so that any in-house standard plot shape and size may be duplicated.

Within the data area, it is also possible to specify data ranges and/or scales if required. Thus a plot prototype could be set up for, for example, a series of bench plans. However, ranges and scales may be defined later, if required, during the plot process itself.

#### Scaling

Scales are defined separately in the X and Y directions, as data units per plotted millimeter. Thus, if the data units are meters, then an X SCALE (or Y SCALE) of 1 will give one meter per plotted millimeter, or a scale of 1:1000. An X SCALE of 2 will give 1:2000, and so on. If the data units are feet, then an X SCALE of 3.28084 will give 3.28084 feet per plotted millimeter (i.e. a scale of 1:1000).

#### Data Ranges and Scales

The user may define three values for X and Y defining the scale (X SCALE), and minimum and maximum data values (X MIN and X MAX). Any two out of these three must be defined, and the remaining value is then calculated. However, if all three are defined, then they must be consistent; the data range must map into the defined data area at the given scale. The process checks for this. Note that if the minimum and maximum are defined, then these are mapped into the data area, and can give rise to different scales in X and Y; to ensure the same scale in X and Y, it is better to give a data minimum or maximum and the required scale.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Plot Prototype
            Plot prototype file to be created.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "protop "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def quig(self,
                out_o="required",
                retrieval="optional"):

        r"""
        QUIG
        ----
        Quick generation of a number of different types of plot with full auto-scaling. Scatter plots, histograms, line and perimeter plots may be produced, displayed and optionally output to a plot file.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Block Model Prototype
            Output prototype model.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "quig "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def random(self,
                out_o="required",
                outfield_f="optional",
                nrecs_p="required",
                distrib_p="required",
                ps_f=['optional'],
                seed_p=0,
                retrieval="optional"):

        r"""
        RANDOM
        ------
        Generate random numbers. RANDOM is similar to (and supersedes) the legacy **[MONACO](<monaco.md>)** process.

The type of random distribution is primarily dictated by DISTRIB. Each option supports either one or two parameters (P1 and P2).

  * 1Produce random numbers using a **uniform** distribution with minimum **P1** and maximum **P2**.

  * 2Produce random numbers using an **exponential** distribution with rate **P1**.

  * 3Produce random numbers using a **normal** distribution with mean **P1** and standard deviation **P2**.

  * 4Produce random numbers using a **Laplacian** distribution with location **P1** and scale parameter **P2**.

  * 5Produce random numbers using a **Weibull** distribution with shape parameter **P1** and scale parameter **P2**.

  * 6 Produce random numbers using a **Cauchy** distribution with location **P1** and scale parameter **P2**.

  * 7Produce random numbers using a **lognormal** distribution with log mean **P1** and log standard deviation **P2**.

**Note** : you can also generate random numbers using the **[EXTRA](<extra.md>)** process.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Table
            Output file containing random values.
            Required=Yes

        Fields:
        -------

        outfield: Any : IN
            Field to write the random variables into.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        nrecs:
            Number of records required in output file
            Range=Undefined
            Values=Undefined
            Default=1
            Required=Yes

        distrib:
            Type of distribution to use to generate random numbers. See "Distribution Options"
            above.
            Range=1,7
            Values=1,2,3,4,5,6,7
            Default=1
            Required=Yes

        p1:
            First parameter of the chosen distribution.
            Range=Undefined
            Values=Undefined
            Default=0
            Required=Yes

        p2:
            Second parameter of the chosen distribution. Ignored if **DISTRIB** =2.
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        seed:
            Random number seed. If the same non-zero seed is used for multiple runs then the same
            set of random numbers will be generated. If **SEED** is zero, subsequent results with
            the same parameters will differ.
            Range=Undefined
            Values=Undefined
            Default=0
            Required=No

        """
        command = "random "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if outfield_f != "optional":
            command += " *outfield=" + outfield_f

        if ps_f[0] != "optional":
            command += self.parse_infields_list("p", ps_f, 2, "@")

        if nrecs_p == "required":
            raise ValueError("nrecs_p is required.")

        if nrecs_p != "optional":
            command += " @nrecs=" + str(nrecs_p)

        if distrib_p == "required":
            raise ValueError("distrib_p is required.")

        if distrib_p != "optional":
            try:
                val = float(distrib_p)
                if val not in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]:
                    raise ValueError(f"distrib_p value {distrib_p} is not in allowed values: [1, 2, 3, 4, 5, 6, 7]")
            except ValueError as e:
                if isinstance(distrib_p, (int, float)):
                    raise e

        if distrib_p != "optional":
            command += " @distrib=" + str(distrib_p)

        if seed_p != "optional":
            command += " @seed=" + str(seed_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def scrfmt(self,
                out_o="optional",
                text_f="optional",
                width_p=80,
                print_p=0,
                retrieval="optional"):

        r"""
        SCRFMT
        ------
        Legacy process used to format text using format controls defined in the **SCREEN** command.

The output is sent to the screen, and optionally the print file and/or a Datamine file. The text to be formatted can be entered directly, or supplied from an external text file, with an optional keyword. Only one external file (and key if supplied) can be referenced.

In the external file the key is prefixed by the characters . Specification of an external file is as follows:
    
    
    sysfile [,key [,prepended fmt_txt]]

**Note** : The maximum number of formatted text lines allowed is 500.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Undefined
            Output database file.
            Required=No

        Fields:
        -------

        text: Character : OUT
            Optional name for the field that is to contain the formatted text. The default is
            "TEXT".
            Default=TEXT
            Required=No

        Parameters:
        -----------

        width:
            Width of output text in characters in the range 1-132 (80).
            Range=1,132
            Values=Undefined
            Default=80
            Required=No

        print:
            Control whether output should be sent to the print file, with the default as none (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "scrfmt "

        if out_o != "optional":
            command += " &out=" + out_o

        if text_f != "optional":
            command += " *text=" + text_f

        if width_p != "optional":
            try:
                val = float(width_p)
                if not (1.0 <= val <= 132.0):
                    raise ValueError(f"width_p value {width_p} is not in allowed range: [1.0, 132.0]")
            except ValueError as e:
                if isinstance(width_p, (int, float)):
                    raise e

        if width_p != "optional":
            command += " @width=" + str(width_p)

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def secdef(self,
                out_o="required",
                retrieval="optional"):

        r"""
        SECDEF
        ------
        Create a section definition file to support the creation and clipping of data in a 3D window. A Section Definition is a numerical representation of a 3D plane. 

See [3D Sections](<../VR_Help/Sections.md>).

The output section definition file contains the following fields, and is recognized in all Studio products as the section definition file type:

SVALUE  |  Section number  
---|---  
XCENTRE  |  X coordinate of the center of the section.  
YCENTRE  |  Y coordinate of the center of the section.  
ZCENTRE  |  Z coordinate of the center of the section.  
SDIP  |  Dip of the section.  
SAZI  |  Azimuth of the section (the dip direction of the section plane).  
STHICK |  The width of the section corridor. This is split equally both in front of and behind the section. Essentially, this is the width of a cross section of data displayed when clipping is set to both front and back.  
DPLUS  |  Extent of the section in the positive (azimuth) direction.  
DMINUS  |  Extent of the section in the negative (opposite to azimuth) direction.  
HSIZE |  Horizontal dimension of the section plane.  
VSIZE |  Vertical dimension of the section plane.  
  
**SECDEF** outputs a 3D section defined using subsequent command line prompts. 

For example, When this process is run, the following messages and prompts are displayed in the **Command** control bar; responses are typed into the **Run Command** field:
    
    
    NUMBER OF SECTIONS (0 TO END >  1
    
    
     >>> NUMBER OF SECTIONS =     1
    
    
     >>> SELECT ONE OF THE FOLLOWING --
    
    
     >>>          1    VERTICAL OR INCLINED SECTION
    
    
     >>>                   DEFINED ABOUT CENTRE POINT
    
    
     >>>          2    VERTICAL SECTION DEFINED BY
    
    
     >>>                   END POINTS
    
    
     >>>          3    PLAN VIEW DEFINED BY CORNER
    
    
     >>>                   POINTS
    
    
    > 1
    
    
    SVALUE > 1
    
    
    XC     > 5000
    
    
    YC     > 6000
    
    
    ZC     > 0
    
    
    DIP    > 90
    
    
    AZI    > 180
    
    
    DMAX   > 50
    
    
    DPLUS  > 25
    
    
    DMINUS > 25
    
    
    HSIZE  > 500
    
    
    VSIZE  > 100
    
    
     >>> SECTION PLANE PARAMETERS ---
    
    
     >>> FIRST SECTION (OF     1)
    
    
     >>> SVALUE >          1.00
    
    
     >>> XC     >       5000.00
    
    
     >>> YC     >       6000.00
    
    
     >>> ZC     >          0.00
    
    
     >>> DIP    >         90.00
    
    
     >>> AZI    >        180.00
    
    
     >>> DMAX   >         50.00
    
    
     >>> DPLUS  >         25.00
    
    
     >>> DMINUS >         25.00
    
    
     >>> HSIZE  >        500.00
    
    
     >>> VSIZE  >        100.00
    
    
    ARE THEY CORRECT (Y/N) > Y
    
    
    NUMBER OF SECTIONS (0 TO END > 0
    
    
     >>>       1 Records in File ... secdef1.dm <<<
    
    
    >>> SECDEF   Complete <<<

If sections already exist in **OUT** , the file is appended. This way, you can easily create a file of multiple definitions.

Note: You can only have one section definition file loaded in the 3D window at any one time, but each file can contain any number of section definitions. Attempts to load another file will result in the current one being closed.

Data is saved to a Section Definition file. This file can contain multiple section views, and previously saved views are accessed using the 3D view ribbon, if your product supports one. You can also step back and forward through loaded section definitions using the following commands:

  * [move-previous-section ("mps")](<../command_help/move-previous-section.md>)

  * [move-next-section ("mns")](<../command_help/move-next-section.md>)

        Input Files:
        ------------

        Output Files:
        -------------

        out: Undefined
            Output file of section definitions, containing the fields **SVALUE, XCENTRE, YCENTRE,
            ZCENTRE, SDIP, SAZI, VAZI, VDIP, HSIZE, VSIZE, DPLUS, DMINUS, SCALE, TEXT, COUNT**
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "secdef "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def setenv(self,
                retrieval="optional"):

        r"""
        SETENV
        ------
        Updates the environment with new variables.

**SETENV** copies environment file data from a system file or the keyboard to a temporary file, then merges the temporary file with the current environment set of environment variables.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "setenv "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def sortx(self,
                retrieval="optional"):

        r"""
        SORTX
        -----
        Note: **SORTX** and [MGSORT](<mgsort.md>) have identical functionality. **SORTX** is retained for legacy macro support. **MGSORT** offers a performance improvement over **SORTX**.

See [MGSORT Process](<mgsort.md>).

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "sortx "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def sudttr(self,
                wiretr_o="required",
                wirept_o="required",
                sid_p="required",
                retrieval="optional"):

        r"""
        SUDTTR
        ------
        Read in a legacy SURPAC .DTM system file (SURPAC v1) and create two related Datamine files.

&**WIREPT** is a file containing a list of point coordinates. &**WIRETR** is a file containing point triples which define triangles. These files are the same as those output by **[SURTRI](<surtri.md>)**.

* * *

        Input Files:
        ------------

        Output Files:
        -------------

        wiretr: Wireframe Triangle
            Wireframe triangle data file with the fields **TRI-NO,PT1,PT2,PT3**.
            Required=Yes

        wirept: Wireframe Points
            Wireframe point data file with the fields **PTN,XP,YP,ZP**.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        sid:
            Surface identifier with a lower surface having the value -1, and a top surface the
            value +1 (-1).
            Range=Undefined
            Values=-1,1
            Default=-1
            Required=Yes

        """
        command = "sudttr "

        if wiretr_o == "required":
            raise ValueError("wiretr_o is required.")

        if wiretr_o != "optional":
            command += " &wiretr=" + wiretr_o

        if wirept_o == "required":
            raise ValueError("wirept_o is required.")

        if wirept_o != "optional":
            command += " &wirept=" + wirept_o

        if sid_p == "required":
            raise ValueError("sid_p is required.")

        if sid_p != "optional":
            try:
                val = float(sid_p)
                if val not in [-1.0, 1.0]:
                    raise ValueError(f"sid_p value {sid_p} is not in allowed values: [-1, 1]")
            except ValueError as e:
                if isinstance(sid_p, (int, float)):
                    raise e

        if sid_p != "optional":
            command += " @sid=" + str(sid_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def surlog(self,
                retrieval="optional"):

        r"""
        SURLOG
        ------
        **SURLOG** is a data input process which will read a character format system file containing records of survey information and measurements as recorded on a digital data recorder by electronic survey equipment.

This process constitutes the first step in survey data processing, creating a Datamine file of the survey measurements. The file stored on the data logger containing the measurements will have to be transferred to the computer, as an ASCII format file, prior to running this process.

The process will create up to three output files of data containing general survey job information, coordinates of the survey stations occupied and referenced during the survey and angle and/or distance measurements taken to fix the position of survey stations or mining excavations. The output files can then be input to suitable survey measurement reduction processes:

  * [SURTAC](<surtac.md>)

Reduction of survey tacheometry measurements.

  * [SUROBS](<surobs.md>)

Reduction of measurements to survey stations.

It is suitable for the input of survey data, where job header information records are followed by measured angles and distances to surface or underground features. It can also be used for the input of borehole logs where header records containing borehole identifier and collar coordinates are followed by down-the-hole measurements to lithological contacts and mineral assay samples. The data needs to be processed further to compute sample positions in space for geological interpretation work:

  * [DESURV](<desurv.md>)

Drillhole survey data is used to produce a file of samples independently located in space.

  * SURLOG

Combines the data input capabilities of existing processes and provides extended flexibility in allowing the output to multiple files and also the re-formatting of data. The following processes allow the user to input fixed or free format data interactively or from an ASCII system file:

  * [INDATA](<indata.md>)

Free format data input (maximum of 80 character line width).

  * [INPUTW](<inputw.md>)

Fixed format data input (maximum of 240 character line width).

The format supplied by the user in these processes are fixed for every record read from the system file, and records not matching the prescribed format are rejected.

The reading of the input system file in **SURLOG** is controlled by user-defined input format files.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "surlog "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def sustp2(self,
                out_o="required",
                direct_p="required",
                retrieval="optional"):

        r"""
        SUSTP2
        ------
        Create a perimeter file from a SURPAC2 string file.

The last point on a SURPAC string file is not output if it matches the first point (and hence indicates a closed string). Isolations are given unique PVALUEs.

        Input Files:
        ------------

        Output Files:
        -------------

        out: String
            Output perimeter file with the standard fields PVALUE,PTN,XP,YP,ZP plus STRNO, which
            contains the SURPAC string number. Additional fields in the SURPAC file are returned as
            D0,D1,...D9 if they exist.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        direct:
            Parameter to specify the plane of the STRing file: 1=XY, 2=XZ, 3=YZ.
            Range=1,3
            Values=1,2,3
            Default=1
            Required=Yes

        """
        command = "sustp2 "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if direct_p == "required":
            raise ValueError("direct_p is required.")

        if direct_p != "optional":
            try:
                val = float(direct_p)
                if val not in [1.0, 2.0, 3.0]:
                    raise ValueError(f"direct_p value {direct_p} is not in allowed values: [1, 2, 3]")
            except ValueError as e:
                if isinstance(direct_p, (int, float)):
                    raise e

        if direct_p != "optional":
            command += " @direct=" + str(direct_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def sustpe(self,
                out_o="required",
                direct_p="required",
                retrieval="optional"):

        r"""
        SUSTPE
        ------
        Imports a SURPAC string file (assumed to be closed perimeters, but only the case if the last and first SURPAC points are duplicated) into a Datamine perimeter file.

Uses the STRing number as the perimeter number and depending on the value of @DIRECT will load the string file into the perimeter file XP,YP,ZP fields appropriately.

The user is required to know the orientation of the string file coordinates ie section or plan.

        Input Files:
        ------------

        Output Files:
        -------------

        out: String
            Output perimeter file with the standard fields PVALUE,PTN,XP,YP,ZP.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        direct:
            Parameter to specify the plane of the STRing file: 1=XY, 2=XZ, 3=YZ.
            Range=1,3
            Values=1,2,3
            Default=1
            Required=Yes

        """
        command = "sustpe "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if direct_p == "required":
            raise ValueError("direct_p is required.")

        if direct_p != "optional":
            try:
                val = float(direct_p)
                if val not in [1.0, 2.0, 3.0]:
                    raise ValueError(f"direct_p value {direct_p} is not in allowed values: [1, 2, 3]")
            except ValueError as e:
                if isinstance(direct_p, (int, float)):
                    raise e

        if direct_p != "optional":
            command += " @direct=" + str(direct_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def syspar(self,
                retrieval="optional"):

        r"""
        SYSPAR
        ------
        Displays application system parameters. No parameters are required. Information is output to the **Command** window.

Related topics and activities

  * [OPSYS Macro Command](<../Macro_Command_Help/OPSYS.md>)

  * [SYSFILE Macro Command](<../Macro_Command_Help/sysfile.md>)

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "syspar "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def tdin(self,
                out_o="required",
                retrieval="optional"):

        r"""
        TDIN
        ----
        Processes [TDOUT](<tdout.md>) and TDIN provide the interface between your application and the standalone Whittle THREE-D program for pit Optimization.

        Input Files:
        ------------

        Output Files:
        -------------

        out: Block Model
            Output model file.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "tdin "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def unfold(self,
                out_o="required",
                quads_o="optional",
                x_f="optional",
                y_f="optional",
                z_f="optional",
                section_f="optional",
                boundary_f="optional",
                wstag_f="optional",
                bstag_f="optional",
                tag_f="optional",
                unitname_f="optional",
                hangwall_f="optional",
                footwall_f="optional",
                ucsa_f="optional",
                ucsb_f="optional",
                ucsc_f="optional",
                linkmode_p=3,
                ucsamode_p=2,
                ucsbmode_p=3,
                ucscmode_p=2,
                plane_p=1,
                hangid_p="optional",
                footid_p="optional",
                unitid_p="optional",
                tolrnc_p=0,
                ucsalimt_p=1,
                orgtag_p='-',
                retrieval="optional"):

        r"""
        UNFOLD
        ------
        Transforms a set of X,Y,Z data into an Unfolded Coordinate System [UCS] as defined by a stratified geological unit.

**UNFOLD** is the process for unfolding a stratified unit. The main purpose of unfolding strata is to calculate the stratigraphical distances between points - for example, Figure 1, below, shows 2 drillhole samples either side of an anticline. The standard geometrical distance between them is a straight line, however, from a geological point of view, the distance separating them is a line following the anticline structure (shown as dashed line). It is this distance, called the stratigraphical or natural or unfolded distance, that would then be used in variogram calculation and grade estimation.

This unfolding technique involves transforming the standard coordinates (orthogonal X,Y,Z axes) of every sample to an unfolded coordinate system (UCS). The UCS axes are not straight lines, and are not orthogonal to each other.

[![](../Images/unfold1.gif)](<javascript:void\(0\);>)

Figure 1: Geometrical and Stratigraphical Distances Between Two Points

![](../Images/image001.gif) |  Standard geometrical distance between A and B. Calculated from standard orthogonal X, Y, Z axes.  
---|---  
![](../Images/image002.gif) |  Stratigraphical distance between A and B. Calculated from unfolded coordinate system (UCS) axes.  
  
Figure 2, further below, shows a simple example of sections through a stratified deposit. A plan showing the strike of the orebody is also shown in this figure. The unfolded coordinate system (UCS) has 3 axes, A, B and C:

  * A - hangingwall-footwall direction (perpendicular to the orebody);

  * B - down-dip (along the centre line between hangingwall and footwall);

  * C - along strike.

The **UNFOLD** process is used to calculate the **UCS** coordinates of desurveyed drillhole data. Variogram analysis can then be undertaken based on the **UCS**. The parameters of the variogram model are therefore calculated in the UCS. A model with cells and subcells within the folded stratified unit is created using standard methods. This model is defined using the world coordinate system.

### Methodology

The following method is illustrated with structural interpretations on vertical sections. However the method can also be applied when the interpretations are in plan. Structural interpretations must be provided as digitized strings on vertical sections. At a minimum, two structural strings on two sections are required to define the UCS coordinates of samples in the stratified unit. The structural strings will often be the hangingwall and footwall as shown in Figure 2, below.

The method involves creating a series of hexahedrons modelling the stratified unit. Such a hexahedron is shown in Figure 3, below, where it is defined by 6 surfaces:

BH1 BF1 CF1 CH1 BH2 BF2 CF2 CH2  |  Surfaces between adjacent hangingwall and footwall points within a section. Because the sections themselves are planar, these surfaces are planar. All points on each of these surfaces have the same `along strike' (UCSC) coordinate.  
---|---  
BH1 BH2 CH2 CH1 BF1 BF2 CF2 CF1  |  Surfaces between sections and between adjacent points on the hangingwall or footwall respectively. All points on each of these surfaces have the same `across strike' (UCSA) coordinate.  
BH1 BH2 BF2 BF1 CH1 CH2 CF2 CF1  |  Surfaces between sections and between points on the hangingwall and footwall.  
  
Any point Q lying within the stratified unit will lie within one of these hexahedrons. The UCS coordinates of the point can then be calculated by interpolation within the hexahedron.

[![](../Images/unfold2.gif)](<javascript:void\(0\);>)

Figure 2: Coordinate Axes in the UCS

[![](../Images/unfold3.gif)](<javascript:void\(0\);>)

Figure 3: Hexahedron Defined by 6 Surfaces

### Unfolded Coordinate System (UCS)

The three reference axes are:

  * A - hangingwall-footwall direction (perpendicular to the orebody);

  * B - down-dip (along the centre line between hangingwall and footwall);

  * C - along strike.

UCS values may be scaled in one of four ways to define the relative position of data within and across the sections:

  1. Normalised. A normalised coordinate is a value between 0 and 1 describing the distance as a proportion of the total distance along the axis.

  2. Adjusted. An adjusted coordinate is the normalised coordinate value multiplied by the average length of the appropriate axis (see Section 1.2.6), based on the data from all sections.

  3. True Length. The true length coordinate is the distance from the UCS origin measured in standard units.

  4. World Coordinates. Where appropriate, a UCS value can correspond to one of the standard (orthogonal X,Y,Z) axes.

The true length coordinate approximates the distance from the origin of the UCS coordinate system of the selected axis, but is measured in the standard coordinate system units.

  * For UCSA, this provides a measure of width or true width.

  * For UCSB it is the distance along the dip-direction of the strata.

  * UCSC defaults to the `adjusted' units - this is generally satisfactory as UCSC should correspond to the direction of the fold axis.

### Creation of Links

The method of creating the hexahedrons involves linking footwall and hangingwall strings within a section. The user defines these links when digitizing the strings using a similar method to tagging in wireframing. Figure 4, below, shows an example where points AH to FH have been linked to AF to FF respectively.

Each of these links joins points on the hangingwall and footwall that the user considers have the same `down-dip' (UCSB) coordinate. It is not essential for the first and last points on each string to be linked. Any points on a string before the first linked point or after the last linked point will be ignored.

If you don't define any links between the hangingwall and footwall, the algorithm automatically creates one between the first points, and one between the last points of each string.

In order to calculate the A and B coordinates of any point Q, the process takes every digitized point on the hangingwall, and creates a corresponding point on the footwall with the same down-dip distance, taking into account the links defined by the user. This is illustrated in Figure 5, below, which is an enlargement of Figure 4. In this example points A, B, C, D, E and F have been defined as linked by the user.

For all other digitized points on the hangingwall (H1 , H2 , etc) and footwall (F1 , F2 , etc) strings, the linking is done automatically as follows:

[![](../Images/unfold4.gif)](<javascript:void\(0\);>)

Figure 4: User Defined Links

The distance AH H1 is calculated as a fraction of the distance AH BH measured along the hangingwall. A new point I is then created on the footwall, where I has the same fractional distance measured from AF as H1 does from AH
    
    
    AH H1 /AH H1 H2 BH = AF I1 /AF F1 BF

and similarly:
    
    
    BH H3 H4 /BH H3 H4 H5 CH = BF I4 /BF CF

This process is repeated for each digitized point Hi on the hangingwall \- pairing it with a new point Ii on the footwall as illustrated in Figure 5, below. The reverse process is then undertaken, creating points on the hangingwall which correspond to digitized points Fi on the footwall. This reverse process is not shown in Figure 5. By joining up the pairs of points at the same fractional distances, a series of quadrilaterals are created. Point Q will lie within one of these quadrilaterals (CH CF I6 H6 ) as illustrated in Figure 5.

### Calculation of USCA and B Coordinates

Consider first the two dimensional problem of calculating the normalized A and B coordinates of point Q as illustrated in Figure 5. It is assumed for this calculation that Q lies on the sectional plane which includes the structural interpretations.

`Points AM , M1 , M2 , BM , M3 , ..., FM` are the midpoints of the link lines and provide a reference line for the down-dip axes.

Coordinate A of point Q is calculated by first identifying the quadrilateral within which the point lies i.e. CH CF I6 H6 . A straight line is the drawn through Q intersecting the hangingwall at QH , and the footwall at QF . The line is drawn such that the hangingwall and footwall intersections are at the same proportional distance in CH H6 and CF I6 respectively:
    
    
    CH QH /CH H6 = CF QF /CF I6 = CM QM /CM M6

The normalized value of coordinate A is calculated as:
    
    
    AN = QH Q/QH QF

The normalized value of coordinate B is calculated as:
    
    
    BN = AM BM CM QM /AM BM CM DM EM FM

### Points Between Sections

The method described so far assumed that point Q lies exactly on section. In order to calculate the A and B coordinates for a point lying between sections k and k+1 the above process must be extended to three dimensions. This involves linking points between sections in a similar manner to the linking within sections described previously. In the following description AH , BH etc are again used to denote points linked by the user, and Hi are intermediate points on the strings which are linked automatically. However it should be noted that although a point on the hangingwall may be linked by the user to a point on the footwall within a section, it is not necessary that the same point is linked by the user to a point on the next section.

Point AH on section k is linked to point AH on section k+1, point BH on section k is linked to point BH on section k+1, and similarly for C to H. Links are always from hangingwall to hangingwall. Each digitized point H on section k is linked to a point on section k+1. Linking is also applied from points on section k+1 back to section k.

Any point Q whose coordinates are to be estimated then lies within a wireframe hexahedron. Slicing this shape with a vertical plane through Q parallel to the sections will create a quadrilateral. This is then used to calculate coordinates A and B, as described previously.

You create links only between hangingwall and footwall points, within any sections. Links between footwalls on adjacent sections are always done within the process. The reason for this is that once three links have been defined, the fourth can be automatically determined from the other three. It is therefore unnecessary for the user to define footwall to footwall links, and could lead to inconsistency in the data if it were allowed.

The method described in this section assumes that the sectional interpretations are parallel. If this is not the case, then an intermediate plane through point Q is created using a similar method to that described previously.

Figure 6, below, shows a plan view of the sections. Each section line (eg SH SH ) represents the maximum extent of projection of the hangingwall and footwall onto plan. A line is drawn through Q such that the intersections TH and TF divide the hangingwall and footwall in the same proportions:
    
    
    SH TH /SH UH = SF TF /SF UF

[![](../Images/unfold5.gif)](<javascript:void\(0\);>)

Figure 5: Automatic Links

### Calculation of UCSC Coordinate

In the majority of cases the sections on which the structures have been defined will be parallel. If this is not the case then it is assumed that the sections are perpendicular to the strike, as illustrated in the plan view in Figure 6, below - that is, all points on any given section have the same `along strike' (UCSC) coordinate.

The total distance along strike is estimated by creating a reference point on each section and calculating the length of the line joining these reference points. This reference vector therefore defines the average strike length and direction.

The reference point on each section is the origin (defined by @ORGTAG), or if this is not specified, it is 0.5 of the distance along the median line (axis B). The reference vector is calculated between each pair of sections. The actual length of the vector between sections i and i+1 is denoted by Vi . The length of the C axis is then the sum of all Vi 's. This is denoted as CLEN which is R1 R2 R3 R4 in Figure 6.

Figure 6 is a plan showing point Q lying between sections 3 and 4. The normalized along strike coordinate C of point Q is calculated as:
    
    
    CN = R1 R2 R3 RQ /CLEN

[![](../Images/unfold6.gif)](<javascript:void\(0\);>)

Figure 6: Calculation of Along Strike Coordinate C

### UCS Coordinate Units

When the UCS coordinates of point Q are calculated, an intermediate section plane will have been interpolated and a number of `normalized', `adjusted' and `true length' measures are available to generate the required UCS A, B and C coordinates.

The normalized coordinates (**AN** , **BN** , **CN**) of point Q as calculated previously all lie between 0 and 1. They represent a proportion of the total distance along each axis, and so it is not easy to relate these values to actual distances. The normalized coordinate space is equivalent to unfolding and stretching the stratified unit into a unit cube.

In the generation of the quadrilaterals, a number of average measures are calculated. The average length of axis C is **CLEN** as described previously. The average length of the across strike axis A (**ALEN**), and the down-dip axis B (**BLEN**) are calculated as follows.

Figure 5 shows the median line AM BM CM DM EM FM for section k. The length of this line is denoted **BLEN** . The average length of the down-dip axis is then calculated as the weighted average of the k **BLEN** values over all sections. The weights used are the distance of influence of each section ie k half way to the next section measured along the C axis.

For each section the area enclosed by the hangingwall, footwall, and the top and bottom links is calculated. This is then divided by the length of the median line **BLENK** for that section to calculate the average across strike width, denoted as **WK** for section k. The average length of axis A, **ALEN** , is then calculated as the weighted average of WK over all sections.

The relationship between the normal coordinates of point Q (AN , BN , CN ) and the adjusted coordinates (AA , BA , CA ) is then:
    
    
    AA = AN  * ALEN
    
    
    BA = BN  * BLEN
    
    
    CA  = CN * CLEN

For the intermediate section associated with point Qm, a local estimate of the length of the across strike width (axis A), and the down dip distance (axis B) is calculated. These distances define the `true length' coordinates for point Q. Where appropriate, any one of the original (X, Y, Z) world coordinate values can be assigned to be a UCS coordinate axis.

The selection of the most appropriate coordinate system for the UCS axes will be dictated by the fold structure, the available digitized strings, and the requirements of variogram modelling and kriging (or other interpolation methods). Several coordinate systems may be of interest - for example, to interpolate block grades by stratigraphic position, and also prepare contours of true thickness in long section.

The default parameters for **UNFOLD** are as follows:

  * @**UCSAMODE** = 2 to calculate the relative position in the stratified unit from the `adjusted' coordinate.

  * @**UCSBMODE** = 3 to calculate the unfolded position appropriate to each section.

  * @**UCSCMODE** = 2 to calculate the approximate position along the fold axis based on an `adjusted' coordinate.

The relative position of samples in the unfolded coordinate system is strongly influenced by the use of an origin, within section and between section strings, and the selection of `normalized', `adjusted' and `true length' coordinates. It is recommended that the position of samples in the unfolded coordinate system be plotted to verify the results of the unfolding process.

### File Handling

The following files are used by the UNFOLD process:

#### &IN - Input Data File

This file holds the standard X,Y,Z coordinate values which are to be transformed into the UCS. The values are held in the fields *X,*Y,*Z.

#### &STRING \- Input Boundary Strings

This file holds strings that define the hangingwall and footwall of each stratum on each section. It is a standard string file with the fields **PVALUE, PTN, XP,YP, ZP**. It must also include:

* **BOUNDARY** |  Boundary identifier. A numeric field identifying the boundary represented by each string. Obviously its value must be constant for all points in a string.  
---|---  
* **SECTION** |  Section identifier. A numeric field identifying the section number of each string. If sections are West-East then * **SECTION** could hold the Northing value.  
  
The file may contain some or all of the optional fields:

* **WSTAG** |  Within section tags. A numeric field holding tag values used to link between the hangingwall and footwall strings within sections. The values in this field will be ignored if @**LINKMODE** =1 or 3.  
---|---  
* **BSTAG** |  Between section tags. A numeric field holding tag values used to link between hangingwall strings on adjacent sections. The values in this field will be ignored if @**LINKMODE** =2 or 3.  
* **TAG** |  Tag. A numeric field holding tag values used to link strings either within or between sections. The precise usage of the values in this field is controlled by @**LINKMODE**. A tag value of 0 or - indicates that the point is not linked.  
  
The &STRING must be sorted by *SECTION, *BOUNDARY, PTN. It is assumed that the section numbering system is such that sorting by *SECTION will ensure that physically adjacent sections are adjacent in the &STRING file.

#### &UNITDEF \- Input Unit Definitions

This optional file must contain the fields:

* **UNITNAME** |  A numeric or alpha field holding the name of a stratigraphical unit defined by strings in the &**STRING** file.  
---|---  
* **FOOTWALL** |  A numeric field holding the value of the * **BOUNDARY** field for strings in the &**STRING** file that define the footwall of the stratigraphical unit.  
* **HANGWALL** |  A numeric field holding the value of the * **BOUNDARY** field for strings in the &**STRING** file that define the hangingwall of the stratigraphical unit.  
  
#### &OUT \- Output Data File

The output data file contains all the fields of the &IN file plus:

* **UNITNAME** |  Stratigraphical unit name. A numeric or alpha field defining the unit in which each data point lies.  
---|---  
* **UCSA** |  Unfolded Coordinate System (UCS) A coordinate. A numeric field holding the hangingwall-footwall direction coordinate.  
* **UCSB** |  Unfolded Coordinate System (UCS) B coordinate. A numeric field holding the down-dip coordinate.  
* **UCSC** |  Unfolded Coordinate System (UCS) C co -ordinate. A numeric field holding the along strike coordinate.  
  
The &**OUT** file may not be the same as the &**IN** file, ie, in-place operation is not allowed. The &**OUT** file will not necessarily be in the same order as the &**IN** file. The &**OUT** file will contain all data records from the &**IN** input file for which **UNFOLD** could calculate UCS coordinates. Any data points that are outside the unfolding quadrilaterals are not written to &**OUT** (unless @**TOLRNC** is used).

#### &QUADS \- Output Unfolding Quadrilaterals

The linkages between points effectively form a type of wireframe. The wireframing used in **UNFOLD** is based on quadrilaterals rather than triangles, and therefore uses non planar surfaces, as described previously.

The quadrilaterals can be output to an optional &**QUADS** file. This is a standard perimeter file (**PVALUE, PTN, XP, YP, ZP**) with additional fields **BLOCKTYP** , * **UNITNAME** and * **SECTION**. Field **BLOCKTYP** has the following values:

  1. Quadrilateral joining adjacent hangingwall and footwall points within the same section which have the same downdip coordinate (eg, BH1 BH2 CF1 CH1 in Figure 3);

  2. Quadrilateral joining hangingwall and footwall points on one section with points on the adjacent section (eg, BH1 BH2 CH2 CH1 in Figure 3);

  3. A special case of **BLOCKTYP** = 2, defining a downdip reference plane where UCSB=0. This is described further on.

### Detailed Features

#### Link Points

It should be noted that it is permissible for a single point on one string to be linked to two points on the other wall, or to two points on the next section.

User-defined link points between sections need not link continuously from a point on one string, to a point on the next string, to a point on the next string, and so on. Hence a point with tag value N may occur on the first three sections, but there may be no tag with value N on the fourth. A tag with the value N may then be reused on the fifth and subsequent sections.

#### Multiple Units

In all examples so far it has been assumed that there is just a single stratified structure with a hangingwall and a footwall. In practice there may be a series of stratified units as illustrated in Figure 7\. The footwall of the first unit becomes the hangingwall of the second unit, and so on. Each unit is treated independently, so that the UCS coordinates for unit i are based on the thickness, downdip distance and along strike distance for the individual unit number i.

Rather than run UNFOLD multiple times, once for each unit, the process has been designed to allow the definition of multiple units, which are all processed in a single run. The UCS coordinates are written to the output file together with a unit identifier.

It is possible for overlapping strata to be defined using the &UNITDEF file. If this does happen and a point to be transformed lies in two or more units then it will be shown in the output file as lying in the first unit, in the order in which they are defined in the &UNITDEF file.

#### Unit Definition

The definition of a stratified unit is controlled either by a unit definition file or by parameter, with the file taking priority if both methods are specified. The &**UNITDEF** file contains the three fields * **HANGWALL** , * **FOOTWALL** and * **UNITNAME**. * **HANGWALL** and * **FOOTWALL** are the values of the * **BOUNDARY** field from the &STRINGS file. The * **UNITNAME** field may be alpha or numeric, and is included in the &**OUT** file for each sample.

If the parameter method is used to select a single unit then @**HANGID** and @**FOOTID** must both be specified. The @**UNITID** parameter is optional. The unit name field in the &**OUT** file is created according to the following rules:

  * If a &**UNITDEF** file is specified, then: the * **UNITNAME** field will be copied from this file. It can therefore be either alpha or numeric depending on its type in the &**UNITDEF** file.

  * If a &**UNITDEF** file is not specified, then:

    * if a * **UNITNAME** field exists in the &IN file, then * **UNITNAME** field will be copied from the &IN file.

  * if a * **UNITNAME** field does not exist in the &IN file, then

    * if parameter @**UNITID** is - or is not specified, then a field **UNITNAME** is created as an 8 character alpha field, and all values set to WITHIN.

    * if parameter @**UNITID** is specified, then a field **UNITNAME** is created as numeric, and all values are set to the value specified.

[![](../Images/unfold7.gif)](<javascript:void\(0\);>)

Figure 7: Multiple Stratified Units

### Data Outside the Unit (@TOLRNC and @UCSALIMT)

The linking method used here effectively defines a type of wireframe. It should be noted that in general it is not possible therefore to calculate the UCS coordinates of any point lying outside this wireframe. If the volume of influence of the first and last sections can be extrapolated geologically outside the wireframe, then the extent of the wireframe should be adjusted. In practice this means that the user should create two new sections before the first and after the last, which contain copies of all strings on the first and last respectively.

It is possible that a sample can be identified geologically as lying within a certain unit, yet it lies outside the hangingwall or footwall surface of the wireframe. This would happen if the actual unit varied non linearly between the interpreted sections. In these circumstances it is still possible to calculate UCS coordinates by use of the @**TOLRNC** parameter.

This defines a margin, expressed as a fraction of the hangingwall-footwall distance UCSA, within which a sample can lie and still be assigned UCS coordinates. In most cases, the value for @**TOLRNC** would not need to be more than a few percent, but if necessary, can be set to much larger value. For example if @**TOLRNC** is set to 0.05 (i.e. 5%) then the normalized value of UCSA may lie between -0.05 and 1.05. This tolerance value only applies to the UCSA hangingwall-footwall direction.

Note that if @**TOLRNC** is used when **UNFOLD** is processing several stratified units (ie, when a &**UNITDEF** is specified), a record from the &IN file may occur more than once in the &**OUT** file. For example, a sample lying near the 'unit 1'/'unit 2' boundary of figure 7 may be selected as being in unit 1 with a normalized UCSA coordinate of 0.99. If @**TOLRNC** =0.05, it may also be selected as being in unit 2 with a normalized UCSA coordinate of -- 0.01. It will therefore occur twice in the &OUT file. 

If the @**TOLRNC** parameters is used, each stratigraphic unit should be processed in **UNFOLD** separately, and only those samples belonging to the stratigraphic unit should be supplied.

The Parameter @UCSALIMT is used in conjunction with @**TOLRNC** to define the limits of the **UCSA** coordinate if **UCSAMODE** =1 or 2 and . This parameter provides additional control on normalized (@**UCSAMODE** =1) and adjusted (@**UCSAMODE** =2) coordinate values as follows:

  1. UCSA coordinates can be <0 and >1 as described above (This is the default).
  2. UCSA coordinates can be <0, but if they are calculated as >1, then will be reset to 1.

  3. UCSA coordinates can be >1, but if they are calculated as <0, then are reset to 0.

  4. UCSA coordinates that are calculated as <0 or >1 are reset to 0 and 1 respectively.

The above description is in terms of the normalized UCSA value (@**UCSAMODE** =1). If adjusted (@**UCSAMODE** =2) is selected then the coordinate is calculated as the normalized value multiplied by the average thickness in the direction of the UCSA axis.

### Direction of Axes

The UCSA coordinate values always increase from the hangingwall to the footwall of each unit. For instance, if the UCSA values are normalized they will vary from 0 on the hangingwall, to 1 on the footwall.

The UCSB coordinates increase in the same direction as the digitized boundary strings. In all the illustrations so far it is assumed that the strings go from top to bottom, and the UCSB coordinates therefore increase with depth. However, if the strings were digitized from bottom to top, then the origin of axis UCSB will be at the bottom of each section.

Another method of changing the origin for the UCSB axis is by using the @ORGTAG parameter. This selects the tag number which defines the origin position from which the UCSB coordinate is measured. UCSB coordinates are then measured as positive in the direction towards the last digitized point, and negative towards the first digitized point on the string.

The UCSC coordinates increase in the order in which the strings occur in the &STRING file. For example, with West East section strings sorted by increasing Northing, the UCSC coordinates increase with Northing. The UCSC axes direction could be reversed by changing the order of the &STRING file data by using a different *SECTION field.

### Non-Continuous Units

If one or both strings do not exist on an intermediate section, then there will be a break in the wireframe. For the purpose of calculating the along strike distance CLEN, the two sections either side of the break will be joined with a single line connection. This is illustrated in Figure 8. **BOUNDARY** 's 3 and 7 exist on sections 1, 2, 5 and 6, but not on sections 3 or 4. Therefore unit A only exists between sections 1 and 2, and between 5 and 6.

If a unit pinches out on a section then the user may represent this by defining coincident hangingwall and footwall strings on intermediate sections. This is illustrated in Figure 9, below.

[![](../Images/unfold8.gif)](<javascript:void\(0\);>)

Figure 8: Break in Continuity of a Unit

[![](../Images/unfold9.gif)](<javascript:void\(0\);>)

Figure 9: Pinching Out a Unit

### Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file containing the X,Y and Z fields of points in the world coordinate system which are to be transformed to the UCS. |  Input |  Yes |  Undefined  
STRING |  Input string file holding the boundary strings which define the stratified unit[s]. 7 fields are compulsory: **SECTION , BOUNDARY , PVALUE,XP,YP,ZP** and **PTN**. 3 optional fields are **WSTAG , BSTAG** and **TAG**.  The file must be sorted on **SECTION , BOUNDARY PTN,** with **SECTION** being the primary keyfield. It is assumed that the section numbering system is such that sorting on **SECTION** will ensure that physically adjacent sections are adjacent in the **STRING** file. |  Input |  Yes |  String  
UNITDEF |  Optional input file containing the **BOUNDARY** value for the hangingwall and footwall of each stratified unit. It must contain the 3 fields: **UNITNAME** , **HANGWALL** and **FOOTWALL**.  If **UNITDEF** is not defined, the stratified unit must be defined by **UNITID** , **HANGID**. |  Input |  No |  Undefined

        Input Files:
        ------------

        Output Files:
        -------------

        out: Undefined
            The output file contains all the fields from the **IN** file plus the UCS coordinate
            fields **UCSA** , **UCSB** and **UCSC** , and the **UNITNAME** field. The **OUT** file
            must be different from the **IN** file.
            Required=Yes

        quads: Undefined
            Optional output file containing the quadrilaterals linking hangingwall and footwall
            points within and between sections. The file contains 8 fields: **PVALUE, PTN, XP, YP,
            ZP BLOCKTYP, SECTION** and **UNITNAME**.
            Required=No

        Fields:
        -------

        x: Numeric : IN
            The numeric field name in the IN file holding the data X co-ordinate, in world
            coordinates. The default field name is X.
            Default=Undefined
            Required=No

        y: Numeric : IN
            The numeric field name in the IN file holding the data Y co-ordinate, in world
            coordinates. The default field name is Y.
            Default=Undefined
            Required=No

        z: Numeric : IN
            The numeric field name in the IN file holding the data Z co-ordinate, in world
            coordinates. The default field name is Z.
            Default=Undefined
            Required=No

        section: Numeric : STRING
            The numeric field name in the **STRING** file holding the section identifier. The
            default field name is **SECTION**.
            Default=Undefined
            Required=No

        boundary: Numeric : STRING
            The numeric field name in the **STRING** file holding the boundary identifier. The
            default field name is **BOUNDARY**.
            Default=Undefined
            Required=No

        wstag: Numeric : STRING
            Within Section **TAG**. A numeric tag field in the **STRING** file, defining the
            stratigraphical links between hangingwall and footwall points on strings within the same
            section. A value of 0 or - means that the point is not linked. The default field name is
            **WSTAG**.
            Default=Undefined
            Required=No

        bstag: Numeric : STRING
            Between Section **TAG**. A numeric tag field in the **STRING** file, defining the
            stratigraphical links between 2 points on strings on adjacent sections with the same
            **BOUNDARY**. A value of 0 or - means that the point is not linked. The default field
            name is **BSTAG**.
            Default=Undefined
            Required=No

        tag: Numeric : STRING
            A numeric tag field in the **STRING** file, defining both the stratigraphical links
            between points on strings within the same section, and between points on adjacent
            sections with the same **BOUNDARY**. A value of 0 or - means that the point is not
            linked. The default field name is **TAG**.
            Default=Undefined
            Required=No

        unitname: Any : UNITDEF
            An alpha or numeric field in the **UNITDEF** file defining the name or number of the
            unit. The default field name is **UNITNAME**.
            Default=Undefined
            Required=No

        hangwall: Any : UNITDEF
            A numeric field in the **UNITDEF** file which defines the **BOUNDARY** value of the
            hangingwall for each **UNITNAME**. The default field name is **HANGWALL**.
            Default=Undefined
            Required=No

        footwall: Numeric : UNITDEF
            A numeric field in the **UNITDEF** file which defines the **BOUNDARY** value of the
            footwall for each **UNITNAME**. The default field name is **FOOTWALL**.
            Default=Undefined
            Required=No

        ucsa: Numeric : OUT
            The name of the A coordinate field in the UCS measured perpendicular to the strings
            within a section [across strike]. The field is created in the **OUT** file and has the
            default name of **UCSA**.
            Default=Undefined
            Required=No

        ucsb: Numeric : OUT
            The name of the B coordinate field in the UCS measured parallel to the boundary strings
            [down dip]. This field is created in the **OUT** file and has the default name of
            **UCSB**.
            Default=Undefined
            Required=No

        ucsc: Numeric : OUT
            The name of the C coordinate field in the UCS measured from section to section [along
            strike]. This field is created in the **OUT** file and has the default name of **UCSC**.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        linkmode:
            The method by which links between strings are created. Options: 0: \- Within section
            links are defined by the **WSTAG** field, or by the **TAG** field if **WSTAG** does not
            exist. Between section links are defined by the **BSTAG** field, or by the **TAG** field
            if **BSTAG** does not exist.; 1: \- Within section links are defined automatically.
            Between section links are defined by the **BSTAG** field, or by the **TAG** field if
            **BSTAG** does not exist.; 2: \- Within section links are defined by the **WSTAG**
            field, or by the **TAG** field if **WSTAG** does not exist. Between section links are
            defined automatically.; 3: Within section links are defined automatically. Between
            section links are defined automatically. For simple structures it is not essential to
            define tag points on the strings; using the default value (3) ensures that automatic
            linking will be applied both within and between sections.
            Range=0,3
            Values=0,1,2,3
            Default=3
            Required=No

        ucsamode:
            The type of UCSA coordinate written to the OUT file. Default (2). Options: 1: \-
            coordinates are normalised.; 2: \- coordinates are adjusted.; 3: \- coordinates are true
            length.; 4: \- coordinates are world X value.; 5: \- coordinates are world Y value.; 6:
            \- coordinates are world Z value.
            Range=1,6
            Values=1,2,3,4,5,6
            Default=2
            Required=No

        ucsbmode:
            The type of UCSB coordinate written to the OUT file. Default (3). Options: 1: \-
            coordinates are normalised.; 2: \- coordinates are adjusted.; 3: \- coordinates are true
            length.; 4: \- coordinates are world X value.; 5: \- coordinates are world Y value.; 6:
            \- coordinates are world Z value.
            Range=1,6
            Values=1,2,3,4,5,6
            Default=3
            Required=No

        ucscmode:
            The type of UCSC coordinate written to the OUT file. Default (2). Options: 1: \-
            coordinates are normalised.; 2: \- coordinates are adjusted.; 3: \- coordinates are true
            length.; 4: \- coordinates are world X value.; 5: \- coordinates are world Y value.; 6:
            \- coordinates are world Z value.
            Range=1,6
            Values=1,2,3,4,5,6
            Default=2
            Required=No

        plane:
            The plane of the structural interpretations defined in the **STRING** file. Default
            (1). 1 - vertical sectional interpretation. 2 - interpretation in plan.
            Range=1,2
            Values=1,2
            Default=1
            Required=No

        hangid:
            The value of the field **BOUNDARY** in the **STRING** file that defines the hangingwall
            of the unit. It will be used if the **UNITDEF** file is not defined.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        footid:
            The value of the field **BOUNDARY** in the **STRING** file that defines the footwall of
            the unit. It will be used if the **UNITDEF** file is not defined.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        unitid:
            If **HANGID** and **FOOTID** are used then the corresponding unit number is defined by
            parameter **UNITID**.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        tolrnc:
            Tolerance in the calculation of the **UCSA** coordinate expressed as a proportion of
            the UCSA width. The default is (0).
            Range=Undefined
            Values=Undefined
            Default=0
            Required=No

        ucsalimt:
            Flag to define the limits of the **UCSA** coordinate if **UCSAMODE** =1 or 2 and
            **TOLRNC** >0\. The options below are defined in terms of the Normalized mode
            [**UCSAMODE** =1]. Default (1) Options: 1: UCSA values can be less than 0 and greater
            than 1; 2: UCSA values can be less than 0. Values calculated as greater than 1 are reset
            to 1; 3: UCSA values calculated as less than 0 are reset to 0. Values can be greater
            than 1; 4: UCSA values calculated as less than 0 are reset to 0. Values calculated as
            greater than 1 are reset to 1
            Range=1,4
            Values=1,2,3,4
            Default=1
            Required=No

        orgtag:
            Tag number of points which define the origin surface from which the UCSB coordinate is
            measured. The default surface if **ORGTAG** is undefined (-) is created from the first
            points on each of the hangingwall and footwall strings.
            Range=Undefined
            Values=Undefined
            Default=-
            Required=No

        """
        command = "unfold "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if quads_o != "optional":
            command += " &quads=" + quads_o

        if x_f != "optional":
            command += " *x=" + x_f

        if y_f != "optional":
            command += " *y=" + y_f

        if z_f != "optional":
            command += " *z=" + z_f

        if section_f != "optional":
            command += " *section=" + section_f

        if boundary_f != "optional":
            command += " *boundary=" + boundary_f

        if wstag_f != "optional":
            command += " *wstag=" + wstag_f

        if bstag_f != "optional":
            command += " *bstag=" + bstag_f

        if tag_f != "optional":
            command += " *tag=" + tag_f

        if unitname_f != "optional":
            command += " *unitname=" + unitname_f

        if hangwall_f != "optional":
            command += " *hangwall=" + hangwall_f

        if footwall_f != "optional":
            command += " *footwall=" + footwall_f

        if ucsa_f != "optional":
            command += " *ucsa=" + ucsa_f

        if ucsb_f != "optional":
            command += " *ucsb=" + ucsb_f

        if ucsc_f != "optional":
            command += " *ucsc=" + ucsc_f

        if linkmode_p != "optional":
            try:
                val = float(linkmode_p)
                if val not in [0.0, 1.0, 2.0, 3.0]:
                    raise ValueError(f"linkmode_p value {linkmode_p} is not in allowed values: [0, 1, 2, 3]")
            except ValueError as e:
                if isinstance(linkmode_p, (int, float)):
                    raise e

        if linkmode_p != "optional":
            command += " @linkmode=" + str(linkmode_p)

        if ucsamode_p != "optional":
            try:
                val = float(ucsamode_p)
                if val not in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]:
                    raise ValueError(f"ucsamode_p value {ucsamode_p} is not in allowed values: [1, 2, 3, 4, 5, 6]")
            except ValueError as e:
                if isinstance(ucsamode_p, (int, float)):
                    raise e

        if ucsamode_p != "optional":
            command += " @ucsamode=" + str(ucsamode_p)

        if ucsbmode_p != "optional":
            try:
                val = float(ucsbmode_p)
                if val not in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]:
                    raise ValueError(f"ucsbmode_p value {ucsbmode_p} is not in allowed values: [1, 2, 3, 4, 5, 6]")
            except ValueError as e:
                if isinstance(ucsbmode_p, (int, float)):
                    raise e

        if ucsbmode_p != "optional":
            command += " @ucsbmode=" + str(ucsbmode_p)

        if ucscmode_p != "optional":
            try:
                val = float(ucscmode_p)
                if val not in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]:
                    raise ValueError(f"ucscmode_p value {ucscmode_p} is not in allowed values: [1, 2, 3, 4, 5, 6]")
            except ValueError as e:
                if isinstance(ucscmode_p, (int, float)):
                    raise e

        if ucscmode_p != "optional":
            command += " @ucscmode=" + str(ucscmode_p)

        if plane_p != "optional":
            try:
                val = float(plane_p)
                if val not in [1.0, 2.0]:
                    raise ValueError(f"plane_p value {plane_p} is not in allowed values: [1, 2]")
            except ValueError as e:
                if isinstance(plane_p, (int, float)):
                    raise e

        if plane_p != "optional":
            command += " @plane=" + str(plane_p)

        if hangid_p != "optional":
            command += " @hangid=" + str(hangid_p)

        if footid_p != "optional":
            command += " @footid=" + str(footid_p)

        if unitid_p != "optional":
            command += " @unitid=" + str(unitid_p)

        if tolrnc_p != "optional":
            command += " @tolrnc=" + str(tolrnc_p)

        if ucsalimt_p != "optional":
            try:
                val = float(ucsalimt_p)
                if val not in [1.0, 2.0, 3.0, 4.0]:
                    raise ValueError(f"ucsalimt_p value {ucsalimt_p} is not in allowed values: [1, 2, 3, 4]")
            except ValueError as e:
                if isinstance(ucsalimt_p, (int, float)):
                    raise e

        if ucsalimt_p != "optional":
            command += " @ucsalimt=" + str(ucsalimt_p)

        if orgtag_p != "optional":
            command += " @orgtag=" + str(orgtag_p)

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def ver(self,
                retrieval="optional"):

        r"""
        VER
        ---
        Displays the current Studio version and build number in the Command control bar, and optionally the version update history.

  1. In the Command toolbar, run the VER command.

  2. On the VER screen, review the settings in the Parameters tab and click OK. 

Note: Selecting [1] in the PRINT drop-down list displays the update history.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "ver "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def xrun(self,
                retrieval="optional"):

        r"""
        XRUN
        ----
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "xrun "

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

