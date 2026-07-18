import dmstudio.initialize


# constant to avoid redundant COM connections which slows down processing
OSCRIPTCON = None

class init(object):

    def __init__(self, version=None):

        """
        commands.__init__
        ------------------


        Commands initialization. After the commands class is initialized for the first time the object will
         be set to the datamine studio object. This property will avoid redundant initializaiton

        Parameters:
        -----------

        version: str
            optional datamine studio versions ('Studio3', 'StudioRM', 'StudioRM3.1', 'StudioRM3.2', 'StudioEM') If no version given, the initializtion
            will try different versions starting with StudioRM then Studio3 and finally StudioEM.

        """
        self.oScript = OSCRIPTCON
        self.version = version
        if self.oScript is None:
            self.oScript = dmstudio.initialize.studio(self.version)

    def run_command(self, command):

        """
        run_command
        -----------

        Uses the studio Parsecommand method to execute a datamine script.

        Parameters:
        -----------

        command: str
            Datamine command string to be parsed
        """

        self.oScript.Parsecommand(command)

        # update the dmdir.py file containing list of .dm files in current directory

        # dmstudio.initialize._make_dmdir()


    def parse_infields_list(self, prefix, fields, maxfields, vtype='*'):

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

    def accmlt(self,
                in_i="required",
                out_o="required",
                keys_f=['optional'],
                allrecs_p=0,
                unsorted_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        ACCMLT
        ------
        **ACCMLT** accumulates values for constant values of keyfields.

For example, if a file contained the fields **YEAR** , **MINE** , **CuProdn** , **AuProdn** then subtotals of **CuProdn** and **AuProdn** for each value of **YEAR** over all values of **MINE** could be produced.

The output is a new file containing the keyfields and the totals. The format is identical to the input file, except that all alphanumeric fields are eliminated, unless they form part of the keyfields.

The total keyfield value must be no more than 5 words long. 

Important: the input file should be sorted on the keyfields beforehand. If it is not, then totals will be for each set of sequential keyfields with the same value in the file.

        Input Files:
        ------------

        in: Table
            Input file.
            Required=Yes

        Output Files:
        -------------

        out: Table
            Output sub-total file.
            Required=Yes

        Fields:
        -------

        keys: Undefined : Undefined
            Keyfield 1 for totalling.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        allrecs:
            Accumulation flag (0). If set to 1 then all records will be copied to the output file
            showing the cumulative totals.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        unsorted:
            Unsorted flag. Default (0). Options: 0: \- An accumulated total is written to the OUT
            file every time the keyfield[s] changes. Hence, if the IN file is sorted on the
            keyfield[s] there will be 1 entry in OUT for each keyfield[s] value. If IN is not sorted
            on the keyfield[s], there may be multiple entries for the same keyfield[s] value in the
            OUT file.; 1: \- The accumulation is over all records with the same keyfield[s] value.
            Hence there will only be 1 entry in OUT for each keyfield[s] value, irrespective of
            whether the IN file is sorted or not. N.B. If UNSORTED=1, the cumulative totals option
            ALLRECS cannot be used. The process will automatically set ALLRECS to 0 if UNSORTED=1.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "accmlt "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if keys_f[0] != "optional":
            command += self.parse_infields_list("key", keys_f, 10, "*")

        if allrecs_p != "optional":
            try:
                val = float(allrecs_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"allrecs_p value {allrecs_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(allrecs_p, (int, float)):
                    raise e

        if allrecs_p != "optional":
            command += " @allrecs=" + str(allrecs_p)

        if unsorted_p != "optional":
            try:
                val = float(unsorted_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"unsorted_p value {unsorted_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(unsorted_p, (int, float)):
                    raise e

        if unsorted_p != "optional":
            command += " @unsorted=" + str(unsorted_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def append(self,
                inmods_i=['optional'],
                out_o="required",
                sequence_p=0,
                protodd_p=0,
                print_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        APPEND
        ------
        Append two or more files together.

The Data Definitions (DDs) of the files do not have to be the same; if they are not, then a superset APPEND takes place. APPEND may be in-place if the DDs of all the files are identical.

Both input files are optional. The operation is:-

  1. If neither input file is defined, then APPEND will prompt for all files to be appended together. The first file specified defines the DD; all subsequent files must have an identical DD to or a subset of the first.
  2. If only &IN1 or &IN2 is defined, then APPEND will copy the file to the output. If the input file is a catalogue file, then APPEND will append all the files in the catalogue into the output file. Only files with the same DD (or a subset of the DD) as the first file will be appended.
  3. If both &IN1 and &IN2 files are specified, then the second file will be appended to the first. If &IN1 is a catalogue file, then all files specified in &IN1 will first be appended, followed by &IN2; or all files specified in &IN2, if &IN2 is a catalogue file. The output file DD will be a superset join of the two first file DDs, and all files on either input which match the DD (or have a subset of it) will be appended together. However if @PROTODD=1, then the first file in &IN1 will be taken as the definitive DD, and only files with this DD (or a subset of it) on either input will be appended together. This enables the first input to be used as a prototype for appending from a general catalogue.

In-place appending, where the output file is equal to &IN1, is allowed in the trivial case where two input files (not catalogues) are to be appended. In this case no retrieval criteria are permitted and both files must have identical DDs (or subset of &IN1). The output file can never be the same as &IN2.

If the optional parameter @SEQUENCE is set to 1, then a field 'FILENAME' is added to the output file. This field will contain the name of the file from which each record was appended. If @SEQUENCE is set to 2, then a field 'SEQUENCE' is added with a sequential file number (1,2,...) in it. If @SEQUENCE is set to greater than 2, then both fields are added. If APPEND is carried out in-place, then @SEQUENCE is ignored and a warning message displayed.

        Input Files:
        ------------

        in1: Table
            Input file 1. This may be a catalogue file. Omit for file prompting. Enter a prototype
            DD (and set PROTODD=1) for selection from a catalogue. Otherwise the DD of the first
            file will be combined with the first IN2 file (if any) for the output file DD, and only
            files matching (or a subset of) this DD will be appended.
            Required=No

        in2: Table
            Input file 2. This may be a catalogue file. Omit for file prompting. Enter a catalogue
            file (and set PROTODD=1) for selection from this catalogue using the prototype on IN1.
            Otherwise the DD of the first file will be combined with the first IN1 entry (if any)
            for the output file DD, and only files matching (or a subset of) this DD will be
            appended. IN2 files are appended after IN1 files.
            Required=No

        Output Files:
        -------------

        out: Table
            Output file = file 1 for in place append, if IN1 nor IN2 are NOT catalogue files, both
            are defined, and have identical DDs. If SEQUENCE is set, then the output file will
            contain extra fields FILENAME (A,8) or SEQUENCE (N) or both.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        sequence:
            Options: 1,: add field FILENAME [A,8] into output file containing filenames of each
            input file.; 2,: add field SEQUENCE [N] into output file containing a file sequence no.
            [1,2,...] for each file appended.; 3,: add both FILENAME and SEQUENCE fields.
            Range=0,3
            Values=0,1,2,3
            Default=0
            Required=No

        protodd:
            Options: 1,: Use the file on IN1 as a prototype for selection of files from a catalogue
            on IN2 to be appended. Ignored unless both IN1 and IN2 specified.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        print:
            Options: 1,: Show the output file DD after all files have been appended. If neither IN1
            nor IN2 are specified, then the file names to be appended are prompted for:- Enter
            DATAMINE file name required, or <return> for default, or ] to end.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "append "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if inmods_i[0] != "optional":
            command += self.parse_infields_list("in", inmods_i, 2, "&")

        if sequence_p != "optional":
            try:
                val = float(sequence_p)
                if val not in [0.0, 1.0, 2.0, 3.0]:
                    raise ValueError(f"sequence_p value {sequence_p} is not in allowed values: [0, 1, 2, 3]")
            except ValueError as e:
                if isinstance(sequence_p, (int, float)):
                    raise e

        if sequence_p != "optional":
            command += " @sequence=" + str(sequence_p)

        if protodd_p != "optional":
            try:
                val = float(protodd_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"protodd_p value {protodd_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(protodd_p, (int, float)):
                    raise e

        if protodd_p != "optional":
            command += " @protodd=" + str(protodd_p)

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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def cokrig(self,
                samples_i="required",
                proto_i="required",
                fields_i="required",
                epar_i="required",
                spar_i="required",
                vmodel_i="optional",
                zpar_i="optional",
                string_i="optional",
                unfold_i="optional",
                outmodel_o="required",
                sampout_o="optional",
                xpt_f="optional",
                ypt_f="optional",
                zpt_f="optional",
                zone1_f_f="optional",
                zone2_f_f="optional",
                key_f="optional",
                mergest_p=1,
                arguments="optional",
                retrieval="optional"):

        r"""
        COKRIG
        ------
        COKRIG performs grade estimation using univariate and multivariate methods, including ordinary, simple kriging, inverse distance weighting and nearest neighbour. 

This process is used as part of the [Advanced Estimation](<../STUDIO_RM/Multivariate_Introduction.md>) wizard, although it can also be accessed independently via the command line as a standalone process.

        Input Files:
        ------------

        samples: Table
            Input sample data file containing X, Y, Z coordinates and grade fields.
            Required=Yes

        proto: Block Model
            Prototype block model into which estimates will be made.
            Required=Yes

        fields: Table
            Estimation fields list file specifying grades to be estimated and output fields.
            Required=Yes

        epar: Table
            Estimation parameters file defining methods, search and variogram volumes.
            Required=Yes

        spar: Table
            Search parameter file defining search volumes and sample counts.
            Required=Yes

        vmodel: Table
            Variogram model parameter file (required for kriging methods).
            Required=No

        zpar: Table
            Custom zone/soft boundary parameter file.
            Required=No

        string: String
            Input boundary string file for unfolding option.
            Required=No

        unfold: Table
            Input unfolding parameter file.
            Required=No

        Output Files:
        -------------

        outmodel: Block Model
            Output model containing estimated grades, variance, etc.
            Required=Yes

        sampout: Table
            Output sample file containing weights details.
            Required=No

        Fields:
        -------

        xpt: Numeric : Undefined
            X coordinate field in sample data.
            Default=XPT
            Required=No

        ypt: Numeric : Undefined
            Y coordinate field in sample data.
            Default=YPT
            Required=No

        zpt: Numeric : Undefined
            Z coordinate field in sample data.
            Default=ZPT
            Required=No

        zone1_f: Any : Undefined
            First zone control field name.
            Default=Undefined
            Required=No

        zone2_f: Any : Undefined
            Second zone control field name.
            Default=Undefined
            Required=No

        key: Numeric : Undefined
            Key field for limiting sample counts.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        mergest:
            Flag to control merging of consistent search/variogram parameters.
            Range=0,1
            Values=0,1
            Default=1
            Required=No

        """
        command = "cokrig "

        if samples_i == "required":
            raise ValueError("samples_i is required.")

        if samples_i != "optional":
            command += " &samples=" + samples_i

        if proto_i == "required":
            raise ValueError("proto_i is required.")

        if proto_i != "optional":
            command += " &proto=" + proto_i

        if fields_i == "required":
            raise ValueError("fields_i is required.")

        if fields_i != "optional":
            command += " &fields=" + fields_i

        if epar_i == "required":
            raise ValueError("epar_i is required.")

        if epar_i != "optional":
            command += " &epar=" + epar_i

        if spar_i == "required":
            raise ValueError("spar_i is required.")

        if spar_i != "optional":
            command += " &spar=" + spar_i

        if vmodel_i != "optional":
            command += " &vmodel=" + vmodel_i

        if zpar_i != "optional":
            command += " &zpar=" + zpar_i

        if string_i != "optional":
            command += " &string=" + string_i

        if unfold_i != "optional":
            command += " &unfold=" + unfold_i

        if outmodel_o == "required":
            raise ValueError("outmodel_o is required.")

        if outmodel_o != "optional":
            command += " &outmodel=" + outmodel_o

        if sampout_o != "optional":
            command += " &sampout=" + sampout_o

        if xpt_f != "optional":
            command += " *xpt=" + xpt_f

        if ypt_f != "optional":
            command += " *ypt=" + ypt_f

        if zpt_f != "optional":
            command += " *zpt=" + zpt_f

        if zone1_f_f != "optional":
            command += " *zone1_f=" + zone1_f_f

        if zone2_f_f != "optional":
            command += " *zone2_f=" + zone2_f_f

        if key_f != "optional":
            command += " *key=" + key_f

        if mergest_p != "optional":
            try:
                val = float(mergest_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"mergest_p value {mergest_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(mergest_p, (int, float)):
                    raise e

        if mergest_p != "optional":
            command += " @mergest=" + str(mergest_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def compdh(self,
                in_i="required",
                out_o="required",
                residual_o="optional",
                bhid_f="optional",
                from_f="optional",
                to_f="optional",
                density_f="optional",
                coreloss_f="optional",
                corerec_f="optional",
                zone_f="optional",
                zone2_f="optional",
                zone3_f="optional",
                zone4_f="optional",
                zone5_f="optional",
                doms_f=['optional'],
                interval_p="required",
                mingap_p="optional",
                maxgap_p=0,
                mincomp_p="optional",
                loss_p="optional",
                dompropn_p="optional",
                start_p=0,
                mode_p=0,
                density_p="optional",
                reverse_p=0,
                print_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        COMPDH
        ------
        Composites drillhole data down or up each drillhole. By use of retrieval criteria and a very large compositing interval, **COMPDH** can also composite over rocktypes or seams.

Compositing can be performed either down the hole from the collar, or up the hole from the **EOH** position.

The input file must be in standard sample format (as output by process **DESURV**). The output file is in an identical format. Up to a maximum of 20 explicit numeric data fields may be composited. These do not have to be specified; they are identified by the process as those fields which are not the standard ones (**BHID** , **X** , **Y** , **Z** , **LENGTH** , **A0** , **B0** , **C0** , **RADIUS** , **FROM** , **TO**).

Each drillhole is split exactly into fixed length composites for a length equal to the parameter @**INTERVAL** , starting normally from the collar; if the optional parameter @**START** is set, this is the distance down the drillhole at which compositing will begin.

If there is a gap between samples of less than or equal to a specified distance (parameter @**MINGAP**) it will be ignored; that is, the missing part will be assigned the grades of the whole composite. Any gap greater than this, but less than or equal to the parameter @**MAXGAP** , will be replaced by a dummy sample with the default values specified in the file. A gap larger than @**MAXGAP** will be taken to terminate the composite.

If the total length of samples with non-absent grade values within a composite is greater than @**MINCOMP** , then the average grade of those samples is assigned to that grade field for the entire composite. If the total length of samples with non-absent grade values within a composite is less than @**MINCOMP** , then that grade field is assigned an absent data value for the entire composite. For example:

FROM  |  TO |  AU  
---|---|---  
31.00 |  31.39 |  15.2  
31.39 |  32.00 |  absent  
  
If @**MINCOMP** =0.1, this is less than the assayed length of 0.39 and so the grade of 15.2 is assigned to the whole composite. If @**MINCOMP** =0.5, this is greater than the assayed length of 0.39 and so the absent data grade of - is assigned to the whole composite.

The file must be in the order of **BHID** and **FROM** , i.e. sorted in drillhole order in increasing downhole distance. This is the order output from the [DESURV](<desurv.md>) process.

### Weighting by Density

If a density field exists in the file then this may be used to for density weighted compositing. The density field is defined as the optional field * **DENSITY**. If any density value is absent data then the default density value will be used.

### Weighting by Core Loss or Recovery

To take into account the effects of core loss, the user may specify one of two optional fields * **CORELOSS** (core loss as a percentage) or * **COREREC** (core recovery as a percentage) to be used during compositing. The lost portion of the core will be taken into account and used in compositing. The actual treatment depends on the optional @**LOSS** parameter.

If @**LOSS** <=0 (default) then the lost part of the core will be assumed to have exactly the same grades, properties etc. as the recovered part. Core loss is ignored.

If @**LOSS** =1 then the lost core will be assumed to have default grades, density, properties etc. which will be averaged with the recovered core values. _Note: This requires that the drillhole file has default values for density & any other fields that need to be calculated._

If @**LOSS** >=2 then the lost core will be treated as cavity (zero density and grades) so that the grade of the total sample is effectively reduced by the cavity.

### Adjusting the Composite Interval

The parameter @**MODE** can be used to force equal composite lengths. If @**MODE** =0 (default) then part or all of one or more samples may be excluded from a composite. Setting @**MODE** =1 forces all samples to be included in one of the composites by adjusting the composite length.

For example if the sample data file contains 10 1m composites, and @**INTERVAL** =3 and the default @**MINCOMP** value of 1.5m is selected, then the output file will contain 3 3m composites. The final 1m sample will not be included in any composite. However if @**MODE** =1, then 3 composites each of length 3.333m will be created. If there were only 8 1m samples in the sample data file, then 3 composites of length 2.667m would be created.

### Residual Composites in COMPDH

**COMPDH** can be used to isolate and export samples excluded from composites (residual composites) using the &**RESIDUAL** output option, in combination with the compositing mode @**MODE** =0 or @**MODE** =2.

  * @**MODE** =0 Samples are excluded if the final composite length is less than @MINCOMP. These excluded samples will appear in &**RESIDUAL**.

  * @**MODE** =1 No residual file is created because all samples are included, ignoring any minimum length requirement.

  * @**MODE** =2 Excluded samples are those whose length falls outside the allowable range set by [@**INTERVAL** \- @**RESLEN**] and [@**INTERVAL** \+ @**RESLEN**]. These samples appear in &**RESIDUAL**.

#### @MODE=2

@MODE=2 allows the final composite in a given zone (defined by changes in BHID, *ZONE, *ZONE2, or *ZONE3 in a sorted drillhole file) to accommodate residual composites while still aiming for a target composite length @INTERVAL.

  * All regular composites are formed at exactly @INTERVAL length, except possibly the last composite in each zone.

  * The last composite can vary in length within the range [(@INTERVAL - @RESLEN), (@INTERVAL + @RESLEN)].

  * For holes where reverse compositing is used (indicated by @REVERSE=1), the first composite of each zone may vary in length.

  * Any composite that falls outside this range is excluded from the main output and listed in the &RESIDUAL file.

#### Using @RESLEN

The default value for @**RESLEN** is 0.5 * @**INTERVAL**. The maximum value is also 0.5 *@**INTERVAL**. If @**RESLEN** is left blank, the default option is used, which includes all residuals in &**OUT**.

If @**RESLEN** is less than 0.5 * @**INTERVAL** , any end-of-zone composite shorter than [@**INTERVAL** \- @**RESLEN**] is excluded from the &**OUT** file.

Note: Residual composites allow a small over- or under-length for the final interval, ensuring minimal sample exclusion.

### Dominant Values

COMPDH allows you to calculate up to 5 dominant values per composited interval. Fields DOM1 to DOM5 must exist in the input drillhole.

This can be useful where the input drillhole has flag fields and alpha fields which cannot be composited, so a length-weighted dominant value can be valuable information.

By default, a dominant field value must reach a minimum proportion of the total length of a composite that must share the same dominant value before that value is recorded. This is controlled by the **DOMPROPN** parameter, set to zero by default (always report the dominant value, regardless of proportion). Higher values require that the dominant values proportion exceeds the given threshold. If the dominant value within a composite is absent, the output value is absent regardless of the value of **DOMPROPN**.

        Input Files:
        ------------

        in: Drillhole
            Sample data file, sorted on **BHID** and **FROM**. Expects fields **BHID** , **FROM** ,
            **TO** , **LENGTH** , **X** , **Y** , **Z** , **A0** , **B0**.
            Required=Yes

        Output Files:
        -------------

        out: Drillhole
            Composite file.
            Required=Yes

        residual: Drillhole
            Residual composites file.
            Required=No

        Fields:
        -------

        bhid: Any : IN
            Drillhole identifier.
            Default=BHID
            Required=No

        from: Numeric : IN
            Downhole distance to sample top.
            Default=FROM
            Required=No

        to: Numeric : IN
            Downhole distance to sample bottom.
            Default=TO
            Required=No

        density: Numeric : IN
            If present, composites will be density- weighted.
            Default=DENSITY
            Required=No

        coreloss: Numeric : IN
            If present, will be taken as percentage core loss, and treated according to the
            **LOSS** parameter.
            Default=CORELOSS
            Required=No

        corerec: Numeric : IN
            If present, will be taken as percentage core recovery, (100-core loss) and treated
            according to the **LOSS** parameter.
            Default=COREREC
            Required=No

        zonen: Any : IN
            Name of a field for compositing within. (may be numeric or up to 32 character alpha).
            This field must exist in the IN and will be copied to the **OUT** file. If specified
            then new composites will be created each time the value of **ZONE** changes.Up to 5
            zones can be specified (**ZONE** to **ZONE5**).
            Default=Undefined
            Required=No

        doms: Undefined : Undefined
            Name of a dominant field. If specified, this field is copied to the output file, containing the value that appears most frequently (by total length) within each sample. The field must exist in the IN file and can be numeric or up to 32 character alpha.Up to 5 dominant fields can be specified.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        interval:
            Composite length.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=Yes

        mingap:
            Gap length to be ignored. The default gap is calculated as 0.05 **INTERVAL**. This
            default value is applied if the parameter is not specified, or if the value is specified
            as <=0. A gap of exactly zero is not permitted. If you want the composite to be split at
            every gap, use a very small value for **MAXGAP** eg 0.0001.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        maxgap:
            Gap length for termination of composite (0).
            Range=Undefined
            Values=Undefined
            Default=0
            Required=No

        mincomp:
            Minimum composite length [0.5 **INTERVAL**].
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        loss:
            If core loss or core recovery field is present, controls how it is handled: <=0 treat
            loss as part of sample =1 treat loss as default values >=2 treat as cavity [zero density
            and grades]
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        dompropn:
            The minimum proportion of the total length of a composite that must share the same
            dominant value before that value is recorded. A value between 0 and 1. See Dominant
            Values.
            Range=
            Values=
            Default=
            Required=No

        start:
            Starting distance down hole (0).
            Range=Undefined
            Values=Undefined
            Default=0
            Required=No

        mode:
            If **MODE** is 0, the default, then the maximum composite length will be defined by the
            **INTERVAL** parameter and the minimum composite length by the **MINCOMP** parameter.
            Thus it is possible for part or all of one or more samples to be excluded from the
            composite. Setting **MODE** to 1 forces all samples to be included in one of the
            composites by adjusting the composite length, while keeping it as close as possible to
            **INTERVAL**. The maximum possible composite length will then be 1.5* **INTERVAL**.
            (0)If **MODE** is 2, excluded samples are those whose length falls outside the allowable
            range set by [@**INTERVAL** \- @**RESLEN**] and [@**INTERVAL** \+ @**RESLEN**]. These
            samples appear in &**RESIDUAL**.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        density:
            Default density value of samples. This is used if no **DENSITY** field exists or if the
            **DENSITY** field contains absent values. If this is unset then the default **DENSITY**
            in the input file data definition is used as the default.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        reverse:
            Reverse compositing direction. Control whether compositing is done from collar to toe
            (default) or toe to collar. 0 : Composite samples starting at the collar. This is the
            default. 1 : Composite samples from the toe to the collar.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        print:
            =3 to display each composite and output file DD (0).
            Range=0,3
            Values=0,1,2,3
            Default=0
            Required=No

        """
        command = "compdh "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if residual_o != "optional":
            command += " &residual=" + residual_o

        if bhid_f != "optional":
            command += " *bhid=" + bhid_f

        if from_f != "optional":
            command += " *from=" + from_f

        if to_f != "optional":
            command += " *to=" + to_f

        if density_f != "optional":
            command += " *density=" + density_f

        if coreloss_f != "optional":
            command += " *coreloss=" + coreloss_f

        if corerec_f != "optional":
            command += " *corerec=" + corerec_f

        if zone_f != "optional":
            command += " *zone=" + zone_f

        if zone2_f != "optional":
            command += " *zone2=" + zone2_f

        if zone3_f != "optional":
            command += " *zone3=" + zone3_f

        if zone4_f != "optional":
            command += " *zone4=" + zone4_f

        if zone5_f != "optional":
            command += " *zone5=" + zone5_f

        if doms_f[0] != "optional":
            command += self.parse_infields_list("dom", doms_f, 5, "*")

        if interval_p == "required":
            raise ValueError("interval_p is required.")

        if interval_p != "optional":
            command += " @interval=" + str(interval_p)

        if mingap_p != "optional":
            command += " @mingap=" + str(mingap_p)

        if maxgap_p != "optional":
            command += " @maxgap=" + str(maxgap_p)

        if mincomp_p != "optional":
            command += " @mincomp=" + str(mincomp_p)

        if loss_p != "optional":
            command += " @loss=" + str(loss_p)

        if dompropn_p != "optional":
            command += " @dompropn=" + str(dompropn_p)

        if start_p != "optional":
            command += " @start=" + str(start_p)

        if mode_p != "optional":
            try:
                val = float(mode_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"mode_p value {mode_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(mode_p, (int, float)):
                    raise e

        if mode_p != "optional":
            command += " @mode=" + str(mode_p)

        if density_p != "optional":
            command += " @density=" + str(density_p)

        if reverse_p != "optional":
            try:
                val = float(reverse_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"reverse_p value {reverse_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(reverse_p, (int, float)):
                    raise e

        if reverse_p != "optional":
            command += " @reverse=" + str(reverse_p)

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0, 2.0, 3.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1, 2, 3]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def copy(self,
                in_i="required",
                out_o="required",
                arguments="optional",
                retrieval="optional"):

        r"""
        COPY
        ----
        Copy a file.

No check is made for the existence of the specified output file, which therefore can be overwritten.

If retrieval criteria are in force, the output file only contains those records which match the criteria. If an index file is copied, the output file contains the joined set of files accessed by the index; it is not itself an index.

        Input Files:
        ------------

        in: Table
            Input file.
            Required=Yes

        Output Files:
        -------------

        out: Table
            Output file.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        """
        command = "copy "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def count(self,
                in_i="required",
                out_o="required",
                keys_f=['optional'],
                arguments="optional",
                retrieval="optional"):

        r"""
        COUNT
        -----
        Outputs a file containing each different value of a set of keyfields, and the number of occurrences of each value.

An up to five word keyfield is specified as 1-5 keyfield names. The output file contains these fields, together with a new field COUNT. This contains the number of occurrences of each set of keyfield values.

A typical use of COUNT is to find the number of samples in each drillhole (keyed on drillhole ID).

**Note** : the field "COUNT", if it exists in the input file, must not be used as a keyfield.

        Input Files:
        ------------

        in: Undefined
            Input file, sorted on required keyfields.
            Required=Yes

        Output Files:
        -------------

        out: Undefined
            File containing counts. Will contain specified keyfields + field COUNT holding number
            of keyfield combinations found.
            Required=Yes

        Fields:
        -------

        keys: Undefined : Undefined
            Keyfield 1 for counting.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        """
        command = "count "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if keys_f[0] != "optional":
            command += self.parse_infields_list("key", keys_f, 10, "*")

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def delete(self,
                in_i="required",
                confirm_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        DELETE
        ------
        Deletes the physical file associated with the symbolic &IN name from disk.

**Warning** : this process deletes physical Datamine files and cannot be undone. Be careful if running this command interactively, and particularly so if via a macro as part of batch process.

If the input file is a catalogue file then all files within the catalogue can be deleted, depending on the value of the optional parameter @**CONFIRM**. If the input is a catalogue file and @**CONFIRM** =0, the user is warned that operation is on catalogue file input and must confirm that deletion of all files in the catalogue is required, before this takes place. If the input is a catalogue file and @CONFIRM= 1, the user is again warned that operation is on catalogue file input, but in this case must confirm deletion of each file in the catalogue individually, before this takes place.

A catalogue file itself may be deleted by either overwriting it with another file before deletion; or by using the [DMEDIT](<dmedit.md>) process to change the name of the field from 'FILENAM to anything else.

The following **Output** window messages display on successful completion of files:
    
    
    >>> nnnnnnnn RECORDS IN FILE filename  
    >>> FILE filename DELETED OK

        Input Files:
        ------------

        in: Undefined
            File to be deleted. If IN is a catalogue file, then all the files in the catalogue will
            be deleted if confirmed.
            Required=Yes

        Output Files:
        -------------

        Fields:
        -------

        Parameters:
        -----------

        confirm:
            Options: 1;: If **IN** is a catalogue file, then a request for confirmation will be
            issued for each file in the catalogue. If IN is a individual database file, then
            confirmation that the file is to be deleted is requested. Default: (0). >>> OPERATING ON
            A CATALOGUE FILE INPUT <<< >>> ARE YOU SURE YOU WISH TO DELETE ALL FILES <<< >>> PRESS
            <RETURN> TO CONTINUE (OR ! TO TERMINATE) >
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "delete "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if confirm_p != "optional":
            try:
                val = float(confirm_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"confirm_p value {confirm_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(confirm_p, (int, float)):
                    raise e

        if confirm_p != "optional":
            command += " @confirm=" + str(confirm_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def diffrn(self,
                inmods_i=['optional'],
                out_o="required",
                keys_f=['optional'],
                keytol_p=1e-05,
                arguments="optional",
                retrieval="optional"):

        r"""
        DIFFRN
        ------
        Perform a relational difference operation.

Records from the first input file are copied to the output file only if there is no match between the key fields of the first and second input files. The effect is to delete records from the first input file if they are matched with the entries in the second input file, using the key fields as the match criteria. Thus differencing is essentially a record deletion mechanism.

At least one key field must be specified and must appear in both input files as an explicit field. The key field may be up to 5 words long, and may be composed of up to 5 fields. If a field is specified which does not exist in both input files, it is ignored, providing at least one field matches.

Both input files must be sorted in the order of the key fields before they can be differenced. If this is not the case, the process will exit with an error message.

A typical use of the **DIFFRN** process is to delete drillholes from a file by supplying a set of borehole identifiers as the second input file.

        Input Files:
        ------------

        in1: Undefined
            File to have records deleted (sorted on required keyfields).
            Required=Yes

        in2: Undefined
            File containing keyfield values for deletion (sorted on required keyfields).
            Required=Yes

        Output Files:
        -------------

        out: Undefined
            Output file.
            Required=Yes

        Fields:
        -------

        keys: Undefined : Undefined
            Keyfield 1 for file matching.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        keytol:
            **KEYTOL** is the tolerance value used to test whether numeric key values are equal. It
            must be greater than or equal to zero. It replaces the previous heuristic comparison
            method. If **KEYTOL** is set to a negative value then zero is used. In a macro
            **KEYTOL** can be set to absent using -. "@**KEYTOL** =-" This will revert to legacy
            behaviour and use a heuristic comparison in relational commands and zero in sort.
            Range=0,+
            Values=Undefined
            Default=0.00001
            Required=No

        """
        command = "diffrn "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if inmods_i[0] != "optional":
            command += self.parse_infields_list("in", inmods_i, 2, "&")

        if keys_f[0] != "optional":
            command += self.parse_infields_list("key", keys_f, 10, "*")

        if keytol_p != "optional":
            command += " @keytol=" + str(keytol_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def extra(self,
                in_i="required",
                out_o="required",
                approx_p=0,
                seed_p="optional",
                fldfail_p=1,
                print_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        EXTRA
        -----
        **EXTRA** is a general purpose EXpression TRAnslator that allows you to _transform_ the contents of files by modifying fields and creating new ones based on the values of existing fields. **EXTRA** also makes it easy to calculate new fields in any file, based on existing fields and values. 

**Tip** : If you're looking for examples of **EXTRA** usage, see [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>).

Before **EXTRA** starts to process records from the input file, it must define which fields will appear in the output file. It is important to understand that _all_ decisions about fields in the output file are made _before_ any records are processed.

Normally, the fields that appear in the output are:

  * All fields that are in the input file

  * Fields created in the transforms you specify.

See [EXTRA examples](<../COMMON/Expression%20Translator%20Examples.md>).

        Input Files:
        ------------

        in: Undefined
            Input file.
            Required=Yes

        Output Files:
        -------------

        out: Undefined
            Output file.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        approx:
            Allow for rounding errors when making comparisons 0 = Exact comparisons 1 = Approximate
            comparisons
            Range=0, 1
            Values=0, 1
            Default=0
            Required=No

        seed:
            Seed number for pseudo-random number sequence
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        fldfail:
            Controls if missing fields cause an error or not. 0 = Missing fields do not cause an
            error. 1 = Missing fields cause an error.
            Range=0, 1
            Values=0, 1
            Default=1
            Required=No

        print:
            Display output to command processor 0 = do nothing 1 = show all code in the output
            window during processing.
            Range=0, 1
            Values=0, 1
            Default=0
            Required=No

        """
        command = "extra "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if approx_p != "optional":
            try:
                val = float(approx_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"approx_p value {approx_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(approx_p, (int, float)):
                    raise e

        if approx_p != "optional":
            command += " @approx=" + str(approx_p)

        if seed_p != "optional":
            command += " @seed=" + str(seed_p)

        if fldfail_p != "optional":
            try:
                val = float(fldfail_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"fldfail_p value {fldfail_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(fldfail_p, (int, float)):
                    raise e

        if fldfail_p != "optional":
            command += " @fldfail=" + str(fldfail_p)

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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def holes3d(self,
                collar_i="required",
                survey_i="optional",
                samples_i=['optional'],
                out_o="required",
                holesmry_o="optional",
                errors_o="optional",
                bhid_f="optional",
                xcollar_f="optional",
                ycollar_f="optional",
                zcollar_f="optional",
                from_f="optional",
                to_f="optional",
                at_f="optional",
                brg_f="optional",
                dip_f="optional",
                survsmth_p='add samples where there are more than one survey record per sample.',
                endpoint_p=0,
                desurvmd_p=1,
                dipmeth_p=1,
                inclmiss_p="optional",
                prompt_p=1,
                keepname_p="optional",
                print_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        HOLES3D
        -------
        **Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

**HOLES3D** converts a set of downhole sample data, collars location data and optionally downhole survey data, into a 'desurveyed' static drillholes file in which each sample is identified by its location (X,Y,Z coordinates) and direction (azimuth and dip) in space.

**Note** : HOLES3D is used by **[Drillhole Importer](<../COMMON/DrillholeImporter-screen.md>)**.

In the 'desurveyed' form, each drillhole sample is identified independently in 3D space without reference to its neighbours.

If two or more downhole sample files are specified (maximum 10) then they are merged so that all divisions of all sets of samples are maintained. A typical use of merging is to add an assay file to a lithology file, where the lithology intervals do not match the assay sample boundaries. Another example is to add absent data samples into holes by making the second file a single record per hole defining the total hole length.

The output from the **HOLES3D** process is in the standard drillhole format which is used elsewhere in your application. For example the drillholes can be viewed interactively, composited downhole, and used to interpolate grades into a block model.

### Using Downhole Survey Data

The downhole survey data is optional. If a survey file is not specified it is assumed that all the drillholes are vertical. If the survey file only includes a subset of the total number of drillholes, then it is assumed that all drillholes which are not included in the survey file are vertical. In both cases a warning message is displayed. The positions at which the survey readings are recorded does not have to correspond to sample positions. 

**Important** : A maximum of 50,000 survey measurements can be processed for each hole. If the number of points exceeds 50,000 then a subset will be selected so that the total number of points is less than 50,000. 

The IDs of all holes that use a subset of survey points are displayed with the progress messages in the Command Window. The IDs are also added to the **ERRORS** file. The **HOLESMRY** file shows the number of survey points processed for all holes.

Each drillhole in the downhole survey data file should have a survey measurement at its collar (AT=0). If this is not the case then the process will automatically move the first survey measurement to the collar position. A warning is issued and a list of all offending holes is displayed. If moving the survey position is not appropriate then you should edit the survey data file and rerun the process.

The process works by first computing a set of positions in space at known coordinates down each hole, and then interpolating between these known points for the top and bottom of each sample. The interpolation uses arcs of circles separately in horizontal and vertical planes.

The process will optionally calculate the XYZ coordinates of the start and end of each sample. This is controlled by parameter **ENDPOINT** , which if set to 1 will create the six extra fields. These coordinates can be useful for creating a DTM of the top or bottom of a seam or stratum.

As well as creating the desurveyed file, the process will optionally create two other files which assist in validating the input data. The **HOLESMRY** file contains a summary of the drillholes in each of the input files. It shows the number of records in each input file for each drillhole. The **ERRORS** file contains a list of:

  * surveys from the Downhole Survey file,

  * samples from the Downhole Sample file(s),

  * collars from the Collars file

which do not pass the validation tests. The tests are detailed in the description of the **ERRORS** file.

If the **HOLESMRY** file shows that one or more of the input data files do not contain entries for every drillhole then a warning is displayed. A warning is also issued if there are any entries in the **ERRORS** file. In order to correct any errors it will be necessary for you to edit the input data files and rerun the process.

You are encouraged to use the optional **HOLESMRY** and **ERRORS** files. You should also take careful note of the output display to see whether any warnings have been issued. If there are any warnings it is strongly recommended that you fix the data problems before using the desurveyed file for subsequent processing.

#### Missing Survey Records

  * Survey records in the collar table (in the **DIP** and **BRG** columns) are used (when available) if no other survey records are found for that hole. For example, if survey records exist in both the collar table and survey table for a hole, only records in the survey table are used (and collar records for that hole are ignored).

  * If no survey records exist for a hole in the survey table, the DIP and BRG values from the collar table are used.

  * If the collar table contains absent DIP or BRG records, the hole is set vertically.

### The SURVSMTH Parameter

When a hole sample is desurveyed the survey data (azimuth and dip) of the sample is used to locate the sample centre point in space. A desurveyed drillhole file contains a set of samples each with a calculated center point in XYZ world space.

Sometimes raw drillhole data tables to be desurveyed may contain more than one survey record within one sample, each with different azimuth and dips. Since a sample is by definition a straight line its location in space cannot be calculated using more than one survey record. The SURVSMTH parameter is used to automatically divide up samples where more than one survey records lie within a sample.

The samples are split in half until only one survey record lies within each sample. Therefore many samples may be created. The default value of SURVSMTH is 1 which will cause extra samples to be created so that no sample contains more than one survey record within its **FROM** and **TO** values. For no extra samples to be created the SURVSMTH parameter should be set to zero.

If the SURVSMTH parameter is set to zero and a sample does contain more than one survey record not all survey records will be taken into account. Traditionally this has been resolved by first compositing the samples to reduce their lengths. The SURVSMTH parameter avoids this requirement.

It is often the case that the first one or two samples in exploration holes contain more than one survey record because they are relatively long. This is because sample divisions have not had to have been created through assay and lithological identification near the surface

        Input Files:
        ------------

        collar: Collars
            Data file of drillhole collar locations. Expects fields **BHID** , **XCOLLAR** ,
            **YCOLLAR** and **ZCOLLAR** ; optional fields **BRG** , **DIP**. If **BRG** and **DIP**
            exist, these values will only be used when no valid survey records exist in input file
            **SURVEY**. If **BRG** and **DIP** values in **COLLAR** are absent or these columns are
            missing, holes are presumed vertical.
            Required=Yes

        survey: Downhole Survey
            Optional survey data file. Expects fields **BHID** , **AT** , **BRG** , **DIP**. If a
            borehole has Survey Data, then it must include a record for the collar location, i.e.
            **AT** =0. **DIP** /**BRG** will first be taken from **SURVEY** file, if that does not
            exist **DIP** /**BRG** will be taken from **COLLAR** and any other holes are presumed
            vertical.
            Required=No

        sample1: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample2: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample3: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample4: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample5: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample6: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample7: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample8: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample9: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        sample10: Downhole Sample
            Sample data files. This file is compulsory and must include fields **BHID** , **FROM**
            , and **TO**. It will probably also include at least one sample attribute field, such as
            grade or lithology.
            Required=Yes

        Output Files:
        -------------

        out: Drillhole
            Required=Yes

        holesmry: Table
            Required=No

        errors: 
            Required=No

        Fields:
        -------

        bhid: Any : COLLAR, SAMPLE1, SURVEY
            Drillhole identifier.
            Default=BHID
            Required=No

        xcollar: Numeric : COLLAR
            X co-ordinate of drillhole collar.
            Default=XCOLLAR
            Required=No

        ycollar: Numeric : COLLAR
            Y co-ordinate of drillhole collar.
            Default=YCOLLAR
            Required=No

        zcollar: Numeric : COLLAR
            Z co-ordinate of drillhole collar.
            Default=ZCOLLAR
            Required=No

        from: Numeric : SAMPLE1
            Downhole distance to sample top.
            Default=FROM
            Required=No

        to: Numeric : SAMPLE1
            Downhole distance to sample bottom.
            Default=TO
            Required=No

        at: Numeric : SURVEY
            Downhole distance to survey point.
            Default=AT
            Required=No

        brg: Numeric : SURVEY
            Bearing of drillhole.
            Default=BRG
            Required=No

        dip: Numeric : SURVEY
            Dip of drillhole. Dip values must always be positive when referring to the downwards
            direction if using this command in a batch process. For more information on Downhole
            Survey files, click [here](<../COMMON/filetype.md#Survey>).
            Default=DIP
            Required=No

        Parameters:
        -----------

        survsmth:
            Options: 0: Prevent samples being added to the output file.
            Range=
            Values=
            Default=add samples where there are more than one survey record per sample.
            Required=No

        endpoint:
            set to 1 to include the **X** , **Y** and **Z** coordinates of the start and end of
            each sample in the desurveyed output file. Fields **XSTART** , **YSTART** , **ZSTART** ,
            **XEND** , **YEND** and **ZEND** are created in the output file.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        desurvmd:
            Locate sample centers or end points on the desurveyed arcs. The default is 1, to
            accurately locate the sample center points. =0 : To accurately locate sample **END**
            points on the desurveyed arcs. =1 : To accurately locate sample **CENTER** points on the
            desurveyed arcs.
            Range=0,1
            Values=0,1
            Default=1
            Required=No

        dipmeth:
            Set to 1 to ensure that positive dip values point downwards, or -1 to point upwards.
            See "Defining DIP and BeaRinG", above.
            Range=0,1
            Values=0,1
            Default=1
            Required=No

        inclmiss:
            INCLude MISSing samples parameter.
            Range=
            Values=
            Default=
            Required=No

        prompt:
            Set to 1 (default) to pause **HOLES3D** execution if an error occurs. Set to 0 to
            continue processing script if errors are encountered (useful when running **HOLES3D**
            from script as processing will continue).
            Range=0,1
            Values=0,1
            Default=1
            Required=No

        keepname:
            Determine how field names are treated during processing.
            Range=
            Values=
            Default=
            Required=No

        print:
            Options: 1: to display each individual process which is run by the **HOLES3D**
            superprocess.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "holes3d "

        if collar_i == "required":
            raise ValueError("collar_i is required.")

        if collar_i != "optional":
            command += " &collar=" + collar_i

        if survey_i != "optional":
            command += " &survey=" + survey_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if holesmry_o != "optional":
            command += " &holesmry=" + holesmry_o

        if errors_o != "optional":
            command += " &errors=" + errors_o

        if bhid_f != "optional":
            command += " *bhid=" + bhid_f

        if xcollar_f != "optional":
            command += " *xcollar=" + xcollar_f

        if ycollar_f != "optional":
            command += " *ycollar=" + ycollar_f

        if zcollar_f != "optional":
            command += " *zcollar=" + zcollar_f

        if from_f != "optional":
            command += " *from=" + from_f

        if to_f != "optional":
            command += " *to=" + to_f

        if at_f != "optional":
            command += " *at=" + at_f

        if brg_f != "optional":
            command += " *brg=" + brg_f

        if dip_f != "optional":
            command += " *dip=" + dip_f

        if samples_i[0] != "optional":
            command += self.parse_infields_list("sample", samples_i, 10, "&")

        if survsmth_p != "optional":
            command += " @survsmth=" + str(survsmth_p)

        if endpoint_p != "optional":
            try:
                val = float(endpoint_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"endpoint_p value {endpoint_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(endpoint_p, (int, float)):
                    raise e

        if endpoint_p != "optional":
            command += " @endpoint=" + str(endpoint_p)

        if desurvmd_p != "optional":
            try:
                val = float(desurvmd_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"desurvmd_p value {desurvmd_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(desurvmd_p, (int, float)):
                    raise e

        if desurvmd_p != "optional":
            command += " @desurvmd=" + str(desurvmd_p)

        if dipmeth_p != "optional":
            try:
                val = float(dipmeth_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"dipmeth_p value {dipmeth_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(dipmeth_p, (int, float)):
                    raise e

        if dipmeth_p != "optional":
            command += " @dipmeth=" + str(dipmeth_p)

        if inclmiss_p != "optional":
            command += " @inclmiss=" + str(inclmiss_p)

        if prompt_p != "optional":
            try:
                val = float(prompt_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"prompt_p value {prompt_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(prompt_p, (int, float)):
                    raise e

        if prompt_p != "optional":
            command += " @prompt=" + str(prompt_p)

        if keepname_p != "optional":
            command += " @keepname=" + str(keepname_p)

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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def ijkgen(self,
                proto_i="required",
                in_i="optional",
                out_o="required",
                x_f="optional",
                y_f="optional",
                z_f="optional",
                psmodel_p="required",
                arguments="optional",
                retrieval="optional"):

        r"""
        IJKGEN
        ------
        Recalculates or calculates the IJK field for a model.

To recalculate IJK values for an existing model, this model is entered on the &**IN** file, and a prototype model (as produced by [PROTOM](<protom.md>)) entered as the &**PROTO** file. The output file &**OUT** may be the same as the input, if required. Parameter @**PSMODEL** is set to zero in this case, meaning additional attributes other than IJK will not be transferred to the output file.

@**PSMODEL** =1 can be used to append the output file with the model fields of the input file, overwriting existing fields as required.

Recalculation of IJK values is often carried out to expand a model (for example, when the original model defined did not cover sufficient volume to include all the waste rock required for an open pit). For this, it is only necessary to define the new origin, number of cells etc. using [PROTOM](<protom.md>) before using **IJKGEN**.

#### Building a model from cell centre values

To create a valid model file from a file containing just cell centre co-ordinates, the output file must be a different name from the input. Parameter @**PSMODEL** is set to 1 to ensure that all model fields are written across from the prototype to the output file. The input file does not have to be sorted.

#### Building a model from a regular set of values

Block models coming into your application from other systems often comprise a set of values on a regular grid, with no positional data. Such data can be turned into a Datamine cell model with the aid of [EXTRA](<extra.md>) and IJKGEN. The stages are:-

1\. Enter the data as a Datamine file, with one record per block.

2\. Use [EXTRA](<extra.md>) to compute cell centre co-ordinates for each block.

3\. Use IJKGEN as described above to generate a model.

4\. Sort the model on IJK for speed of access.

### The Prototype Model

The input prototype model defines the cell sizes, origin, model dimensions etc. that will appear in the output model. Thus the process [PROTOM](<protom.md>) should be used prior to **IJKGEN** to set up this prototype model. It is very important to ensure that the model origin, cell sizes etc. are chosen so that the bottom left hand corner of a cell is at the model origin. Cell sizes should be defined to be the same as in the input model on &IN, or you run the risk of creating a model with overlapping cells or gaps between cells.

The **IJKGEN** process does not check for this, as there are circumstances where this is useful (for example, creating a pseudo model from blast hole data, where each hole is assigned to a cell with unit volume).

Note that **IJKGEN** will include rotated model fields, if found in the model prototype, to the resulting output (sorted) file).

### Data lying outside the model

If the data on &IN lies outside the model limits as defined in the prototype, then the IJK field will be set to absent data with a warning message. You must remove or change such IJK values before entering processes.

### Maximum IJK Value

The maximum IJK value is 2,147,483,647. This means you can have a model with, for example, 1400x1400x1000 parent cells.

See [Block Model Size Limits](<../COMMON/Block_Models_Size_Limits.md>).

        Input Files:
        ------------

        proto: Block Model Prototype
            Input prototype model describing the model parameters. Normally set up by PROTOM. Must
            contain the numeric fields XC, YC, ZC, IJK (explicit) and XMORIG, YMORIG, ZMORIG, NX,
            NY, NZ (implicit) and XINC, YINC, ZINC (either, as required). For recalculation of IJK
            in an existing model, may be the same file as IN.
            Required=Yes

        in: Input file to be converted into a model. Must contain the fields X , Y and Z representing (sub-)cell centre locations. This can be an existing model for recalculation of IJK.
            Overwritten
            Required=No

        Output Files:
        -------------

        out: BlockModel
            Output model file. May be the same as IN where IN already contains model fields; in
            this case, recalculation is in-place. IJK will be set to absent (-) if the record lies
            outside the model limits.
            Required=Yes

        Fields:
        -------

        x: Numeric : IN
            Explicit numeric field in IN containing the X co-ordinate of the (sub-)cell centre.
            Default=X
            Required=Yes

        y: Numeric : IN
            Explicit numeric field in IN containing the Y co-ordinate of the (sub-)cell centre.
            Default=Y
            Required=Yes

        z: Numeric : IN
            Explicit numeric field in IN containing the Z co-ordinate of the (sub-)cell centre.
            Default=Z
            Required=Yes

        Parameters:
        -----------

        psmodel:
            Options: 0: Just generate IJK field without copying additional attributes to the output
            model. This is the recommended option if your output file already contains the expected
            attributes.; 1: Place all other model fields as well as IJK into the output model. This
            will copy standard fields from the prototype to the output file, overwriting any fields
            of the same name copied from the input points file.
            Range=0,1
            Values=0,1
            Default=0
            Required=Yes

        """
        command = "ijkgen "

        if proto_i == "required":
            raise ValueError("proto_i is required.")

        if proto_i != "optional":
            command += " &proto=" + proto_i

        if in_i != "optional":
            command += " &in=" + in_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if x_f != "optional":
            command += " *x=" + x_f

        if y_f != "optional":
            command += " *y=" + y_f

        if z_f != "optional":
            command += " *z=" + z_f

        if psmodel_p == "required":
            raise ValueError("psmodel_p is required.")

        if psmodel_p != "optional":
            try:
                val = float(psmodel_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"psmodel_p value {psmodel_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(psmodel_p, (int, float)):
                    raise e

        if psmodel_p != "optional":
            command += " @psmodel=" + str(psmodel_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def join(self,
                inmods_i=['optional'],
                out_o="required",
                subsetr_p=0,
                subsetf_p=0,
                cartjoin_p=0,
                keytol_p=1e-05,
                print_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        JOIN
        ----
        Performs a relational join, subset join, weave or subset weave of two input files into an output file. The type of join required is controlled by the values of the optional parameters @**SUBSETR** AND @SUBSETF.

This process belongs to a group of four similar ones within the Datamine process collection; JOIN, SUBJOI, WEAVE and SUBWVE. Each provides a different outcome, as described by the following diagram:

  
[![](../Images/JOIN_SUBJOIN_WEAVE_SUBWEAVE.jpg)](<javascript:void\(0\);>)

By default, with @SUBSETR=0 and @SUBSETF=0, JOIN writes out all records and all fields from both input files. Records are compared on the specified keyfields, and if a match is found, the two records are combined into one on the output file. If both files have identical Data Definitions then the record from the second input file is the one written out. Thus in this case the second file updates the first. If no match is found then records are written out with absent data codes for the missing fields.

  * With @SUBSETR=1 and @SUBSETF=0, a relational subset join is carried out. See process [SUBJOI](<subjoi.md>) for further details.

  * With @SUBSETR=0 and @SUBSETF=1, a relational weave is carried out. See process [WEAVE](<weave.md>) for further details.

  * With @SUBSETR=1 and @SUBSETF=1, a relational subset weave is carried out. See process [SUBWVE](<subwve.md>) for further details.

At least one keyfield must be specified and must appear in both input files as an explicit field. The keyfield may be up to 5 words long, and support is provided for up to 30 fields. If a field is specified which does not exist in both input files, it is ignored, providing at least one field matches.

Both input files must be sorted in the order of the key fields before they can be joined. If this is not the case, the process will exit with an error message.

        Input Files:
        ------------

        in1: Table
            First file to be updated (sorted on required keyfields).
            Required=Yes

        in2: Table
            Second file (update file) (sorted on required keyfields).
            Required=Yes

        Output Files:
        -------------

        out: Table
            Output file.
            Required=Yes

        Fields:
        -------

        Parameters:
        -----------

        subsetr:
            Controls whether all records or a subset are written to the output file. If set to (0)
            all records are written.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        subsetf:
            Controls whether all fields or a subset is written to the output file. If set to (0)
            all fields are written. With SUBSETR and SUBSETF set to 0 JOIN writes out all records
            and all fields from both input files. With SUBSETR=1 and SUBSETF=0 a relational subset
            join is carried out. With SUBSETR=0 and SUBSETF=1 a relational weave is carried out.
            With SUBSETR=1 and SUBSETF=1 a relational subset weave is carried out.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        cartjoin:
            If set to (0) and if no keyfields are specified the process will terminate with an
            error. If set to 1 the full Cartesian product is produced and written to the output
            file. No keyfields should be specified to produce the Cartesian product.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        keytol:
            KEYTOL is the tolerance value used to test whether numeric key values are equal. It
            must be greater than or equal to zero. It replaces the previous heuristic comparison
            method. If KEYTOL is set to a negative value then zero is used. In a macro KEYTOL can be
            set to absent using -. "@KEYTOL=-" This will revert to legacy behaviour and use a
            heuristic comparison in relational commands and zero in sort.
            Range=0,+
            Values=Undefined
            Default=0.00001
            Required=No

        print:
            >=1 Display messages on Data definitions. Default is (0)
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "join "

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if inmods_i[0] != "optional":
            command += self.parse_infields_list("in", inmods_i, 2, "&")

        if subsetr_p != "optional":
            try:
                val = float(subsetr_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"subsetr_p value {subsetr_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(subsetr_p, (int, float)):
                    raise e

        if subsetr_p != "optional":
            command += " @subsetr=" + str(subsetr_p)

        if subsetf_p != "optional":
            try:
                val = float(subsetf_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"subsetf_p value {subsetf_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(subsetf_p, (int, float)):
                    raise e

        if subsetf_p != "optional":
            command += " @subsetf=" + str(subsetf_p)

        if cartjoin_p != "optional":
            try:
                val = float(cartjoin_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"cartjoin_p value {cartjoin_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(cartjoin_p, (int, float)):
                    raise e

        if cartjoin_p != "optional":
            command += " @cartjoin=" + str(cartjoin_p)

        if keytol_p != "optional":
            command += " @keytol=" + str(keytol_p)

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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def mgsort(self,
                in_i="required",
                out_o="required",
                keys_f=['optional'],
                order_p=1,
                keysfrst_p=1,
                roworder_p=1,
                keytol_p=1e-05,
                arguments="optional",
                retrieval="optional"):

        r"""
        MGSORT
        ------
        Sort a Datamine (.dm, .dmx) file into ascending or descending order of keyfields. Ascending order is the default; descending order is specified by setting the optional parameter @**ORDER** =2.

At least one keyfield must be specified and must appear as an explicit field. For alphanumeric fields, the collating sequence is the standard Datamine-specific sort sequence for text. The fields are sorted in the order in which they are specified. If a specified keyfield is not in the file, it is ignored. A warning message is given if @**PRINT** >=1.

**Note** : SORTX and MGSORT are identical, although separate process names have been retained and **SORTX** still accessible for legacy macro purposes.

Where sufficient memory exists, the table is sorted entirely within memory. However, if the memory required exceeds that available, the table is sorted in separate 'chunks', each temporarily stored to disk and then merged together for the final write. The maximum number of records that can be sorted is therefore limited only by available disk space.

This process includes the KEYSFRST option which, by default, maintains legacy behavior by reordering key fields in the output file so that KEY1 becomes the first field, KEY2 the second field, and so on. If you specify that key fields are not reordered, then the order of fields in the OUT and IN file will be identical.

This process allows you to determine how the sort is performed with regards to duplicate key field values, using the **ROWORDER** parameter.

Note: Although the order of fields in a file does not affect subsequent processing, it makes it more difficult to review the file using Datamine's Table Editor. For example, a borehole file which is sorted by BHID, FROM and TO is more difficult to manually validate if these fields are not adjacent.

        Input Files:
        ------------

        in: Table
            File to be sorted.
            Required=Yes

        Output Files:
        -------------

        out: Table
            Sorted file.
            Required=Yes

        Fields:
        -------

        keys: Undefined : Undefined
            Keyfields for sorting .
            Default=Undefined
            Required=No

        Parameters:
        -----------

        order:
            Options: 1: For ascending order; 2: For descending order (1).
            Range=1,2
            Values=1,2
            Default=1
            Required=No

        keysfrst:
            Options: 0: output fields in the same order as the input table; 1: output key fields
            first
            Range=0,1
            Values=0,1
            Default=1
            Required=No

        roworder:
            Options: 0: Rows which contain duplicate key field values could be in any order
            (faster); 1: Rows which contain duplicate key field values will be in the input file
            order (slower) (1)
            Range=0,1
            Values=0,1
            Default=1
            Required=No

        keytol:
            **KEYTOL** is the tolerance value used to test whether numeric key values are equal. It
            must be greater than or equal to zero. It replaces the previous heuristic comparison
            method. If **KEYTOL** is set to a negative value then zero is used. In a macro
            **KEYTOL** can be set to absent using -. "@**KEYTOL** =-" This will revert to legacy
            behaviour and use a heuristic comparison in relational commands and zero in sort.
            Range=0,+
            Values=Undefined
            Default=0.00001
            Required=No

        """
        command = "mgsort "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if keys_f[0] != "optional":
            command += self.parse_infields_list("key", keys_f, 10, "*")

        if order_p != "optional":
            try:
                val = float(order_p)
                if val not in [1.0, 2.0]:
                    raise ValueError(f"order_p value {order_p} is not in allowed values: [1, 2]")
            except ValueError as e:
                if isinstance(order_p, (int, float)):
                    raise e

        if order_p != "optional":
            command += " @order=" + str(order_p)

        if keysfrst_p != "optional":
            try:
                val = float(keysfrst_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"keysfrst_p value {keysfrst_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(keysfrst_p, (int, float)):
                    raise e

        if keysfrst_p != "optional":
            command += " @keysfrst=" + str(keysfrst_p)

        if roworder_p != "optional":
            try:
                val = float(roworder_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"roworder_p value {roworder_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(roworder_p, (int, float)):
                    raise e

        if roworder_p != "optional":
            command += " @roworder=" + str(roworder_p)

        if keytol_p != "optional":
            command += " @keytol=" + str(keytol_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def modtra(self,
                model_i="required",
                grid_i="optional",
                out_o="required",
                f1_f5_f="optional",
                xg_f="optional",
                yg_f="optional",
                zg_f="optional",
                plane_p=1,
                xorig_p="optional",
                yorig_p="optional",
                zorig_p="optional",
                xspace_p="optional",
                yspace_p="optional",
                zspace_p="optional",
                numx_p="optional",
                numy_p="optional",
                numz_p="optional",
                miss_p="optional",
                print_p="optional",
                arguments="optional",
                retrieval="optional"):

        r"""
        MODTRA
        ------
        This process creates a regular grid of trace lines through a model.

These trace lines describe the continuity of a field value or set of field values in the model. Average values of all other model fields are calculated and associated with each trace segment.

The process simulates either a rectangular grid of drillholes, drilled through the model parallel to one of model axes, or a set of drillholes whose collars are defined in the optional &**GRID** file. The user specifies between one and five fields (* **F1** to * **F5**) which are used to terminate the simulated drillhole samples. If the value of any of the specified fields change, then the sample is terminated and a new sample started. The sample is written to a standard borehole format file, together with the average value of all numeric fields for that sample. If the model contains alpha fields then the dominant value of each field is also written to the output sample file. The dominant value is defined as the value which has the longest length. If the model contains a **DENSITY** field then the calculations of the average values and of the longest length are tonnage weighted.

The output drillhole file contains the standard drillhole fields - **BHID, FROM, TO, LENGTH, A0, B0** plus all the non-model fields from the model file. **BHID** is a numeric field, starting at 1 and increasing in steps of 1.

The purpose of creating the simulated drillholes is to plot a section through them. This will show the continuity of the * **FN** variable(s) in the section plane. A similar display could also be achieved using colour fill of subcells. A model section plot without colour fill will include subcell boundaries, which will display the continuity over a field or set of fields, but not as clearly as a drillhole section.

The specified fields * **F1** \- * **Fn** should have discrete values rather than being continuous; if a numeric field is specified such as an interpolated grade, then it is highly probable that the field value will change at every subcell boundary. If it is required to show continuity over a range of numeric values, then a 'flag' field should be created in the model with **EXTRA** prior to using **MODTRA**. For example if continuity is required within grade ranges 0-2, 2-5, 5-10, 10-20, 20+ then a flag value can be created in **EXTRA** for each of the 5 ranges. This flag field can then be specified as * **F1**.

  * Having defined a plane, only two of the parameters @**XORIG** , @**YORIG** , @**ZORIG** apply. For example, if @**PLANE** = 3, (YZ) then @**XORIG** is ignored. Similarly for @**XSPACE** and @**NUMX**. 

  * The dominant value of an alpha field is calculated for each drillhole sample as that value with the greatest length (tonnage weighted if there is a **DENSITY** field in the model). In order to preallocate accumulators it is assumed that there will be a maximum of 40 discrete values for any alpha field. If during the course of calculating the dominant value within a sample, a 41st value is found, then the value with the smallest current length will be dropped from the accumulators.

        Input Files:
        ------------

        model: Block Model
            Input model. Must contain the 13 standard model fields - **XC, YC, ZC, XINC, YINC,
            ZINC, XMORIG, YMORIG, ZMORIG, NX, NY, NZ, IJK** \- plus at least one other field.
            Required=Yes

        grid: Undefined
            Optional input grid file defining the location of the simulated drillholes. It must
            contain ALL fields **XG** , **YG** , **ZG** , regardless of the **PLANE** parameter
            setting. This file must NOT include an alpha **BHID** field, as this would clash with
            the numeric **BHID** field created in **OUT**.
            Required=No

        Output Files:
        -------------

        out: Drillhole File
            Output holes file. Will contain the fields **BHID, FROM, TO, X, Y, Z, LENGTH, A0, B0**
            plus all fields from input model file except the 13 standard model fields.
            Required=Yes

        Fields:
        -------

        f1_f5: Any : MODEL
            Fields over which continuity is required within a sample.
            Default=Undefined
            Required=Yes

        xg: Numeric : GRID
            Optional **GRID** field name holding X co-ordinate. Default is **XG**. Ignored if
            **PLANE** =3.
            Default=XG
            Required=No

        yg: Numeric : GRID
            Optional **GRID** field name holding Y co-ordinate. Default is **YG**. Ignored if
            **PLANE** =2.
            Default=YG
            Required=No

        zg: Numeric : GRID
            Optional **GRID** field name holding Z co-ordinate. Default is **ZG**. Ignored if
            **PLANE** =1.
            Default=ZG
            Required=No

        Parameters:
        -----------

        plane:
            Drillhole orientation. Default (1). Options: 1: \- XY. A grid of vertical holes is
            created.; 2: \- XZ. A grid of horizontal holes is created, running from North to South.;
            3: \- YZ. A grid of horizontal holes is created, running from East to West.
            Range=1,3
            Values=1,2,3
            Default=1
            Required=No

        xorig:
            X co-ordinate of collar of first drillhole. Default is model X origin plus half a
            parent cell X dimension. Ignored if **PLANE** =3 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        yorig:
            Y co-ordinate of collar of first drillhole. Default is model Y origin plus half a
            parent cell Y dimension. Ignored if **PLANE** =2 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        zorig:
            Z co-ordinate of collar of first drillhole. Default is model Z origin plus half a
            parent cell Z dimension. Ignored if **PLANE** =1 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        xspace:
            Spacing in X between drillholes. Default is the parent cell X dimension. Ignored if
            **PLANE** =3 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        yspace:
            Spacing in Y between drillholes. Default is the parent cell Y dimension. Ignored if
            **PLANE** =2 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        zspace:
            Spacing in Z between drillholes. Default is the parent cell Z dimension. Ignored if
            **PLANE** =1 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        numx:
            Number of drillholes in X direction. Default is the number up to the model X limit.
            Ignored if **PLANE** =3 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        numy:
            Number of drillholes in Y direction. Default is the number up to the model Y limit.
            Ignored if **PLANE** =2 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        numz:
            Number of drillholes in Z direction. Default is the number up to the model Z limit.
            Ignored if **PLANE** =1 or **GRID** specified.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        miss:
            Missing cells treatment. Default is (0) Options: 0: Where no model cell or subcell
            exists, no drillhole sample will be created.; 1: Where no model cell or subcell exists,
            drillhole sample will be created with missing values.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        print:
            Print flag. Default (0). 0 - minimum output. 1 - summary of percentage complete and
            number of holes written.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        """
        command = "modtra "

        if model_i == "required":
            raise ValueError("model_i is required.")

        if model_i != "optional":
            command += " &model=" + model_i

        if grid_i != "optional":
            command += " &grid=" + grid_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if f1_f5_f != "optional":
            command += " *f1-f5=" + f1_f5_f

        if xg_f != "optional":
            command += " *xg=" + xg_f

        if yg_f != "optional":
            command += " *yg=" + yg_f

        if zg_f != "optional":
            command += " *zg=" + zg_f

        if plane_p != "optional":
            try:
                val = float(plane_p)
                if val not in [1.0, 2.0, 3.0]:
                    raise ValueError(f"plane_p value {plane_p} is not in allowed values: [1, 2, 3]")
            except ValueError as e:
                if isinstance(plane_p, (int, float)):
                    raise e

        if plane_p != "optional":
            command += " @plane=" + str(plane_p)

        if xorig_p != "optional":
            command += " @xorig=" + str(xorig_p)

        if yorig_p != "optional":
            command += " @yorig=" + str(yorig_p)

        if zorig_p != "optional":
            command += " @zorig=" + str(zorig_p)

        if xspace_p != "optional":
            command += " @xspace=" + str(xspace_p)

        if yspace_p != "optional":
            command += " @yspace=" + str(yspace_p)

        if zspace_p != "optional":
            command += " @zspace=" + str(zspace_p)

        if numx_p != "optional":
            command += " @numx=" + str(numx_p)

        if numy_p != "optional":
            command += " @numy=" + str(numy_p)

        if numz_p != "optional":
            command += " @numz=" + str(numz_p)

        if miss_p != "optional":
            command += " @miss=" + str(miss_p)

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def output(self,
                in_i="required",
                fieldlst_i="optional",
                fields_f=['optional'],
                fieldnam_f="optional",
                csv_p=0,
                nodd_p=0,
                dplace_p=-1,
                implicit_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        OUTPUT
        ------
        Output a database file to a system character format file.

The file includes a special version of the Data Definition in front of it. This is used by the [INPDDF](<inpddf.md>) process to re-read the file back into a database. The format of the file produced is described in the INPDDF documentation. For interfacing with other systems, this Data Definition can be suppressed by setting the @**NODD** parameter to '1'.

The accuracy of the numeric values output is maintained, as far as possible, using a format which changes automatically with the magnitude of the number. It is therefore possible to output numbers spanning the whole range between the lowest and highest system values.

By default, all fields are output; however, the required fields, and the order in which they are output, can be chosen using the optional fields F1 \- Fn. This is helpful if the output file would otherwise be too wide for the system to handle correctly. The maximum permitted width of an output system file is 240 characters, except when exporting to CSV using the faster method described below.

If the database file name is a catalogue file (consisting of a series of file names with a field name of '**FILENAM** \- note the prefixed apostrophe), then first the catalogue file is output from the database file &**IN** , and then each file in turn, which is referenced in the catalogue file, is output. The name of each external system file generated will match that of the database file name.

Note: The following message is displayed when using OUTPUT with a catalogue file input: >>> OPERATING ON A CATALOGUE FILE INPUT <<<

### Exporting to CSV

A faster export method, described below, is invoked whenever the@CSVparameter is set to '1' and a catalog file isnotspecified.

The following additional parameters can be set:

  * @**DPLACE** \- set the number of decimal places used in the output data - for example "@DPLACE = 2" outputs up to 2 decimal places. The default of -1 indicates that the best representation for the magnitude of the data is used.

  * @**IMPLICIT** \- if "@IMPLICIT=1", and no required fields have been defined, all table fields are output, including implicit fields. The default is '0'.

When called from a script or macro, more than 25 required output fields can be defined using F1-Fnfields. These must be defined consecutively, and without gaps for example, F1,F2,F4 would not be allowed, and reading would stop afterF2.

If required output fields are defined, and a FIELDLST file is specified, then fields from the FIELDLST file are added to the end of those specified using the F1 \- Fn output fields.

In order to reduce the size of the output file, any trailing zeros (after the decimal point) and trailing spaces after text are automatically trimmed.

The maximum permitted width of 240 characters is not applicable when using this export method.

        Input Files:
        ------------

        in: Table
            Database file to be output. If IN is a catalogue file, then all files in the catalogue
            are output.
            Required=Yes

        fieldlst: Undefined
            File used to supply selected fields.
            Required=No

        Output Files:
        -------------

        Fields:
        -------

        fields: Undefined : Undefined
            Optional first output field. None specified means "all".
            Default=Undefined
            Required=No

        fieldnam: Numeric : FIELDLST
            Field in FIELDLST to identify selected fields.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        csv:
            Options: 1: Output in comma separated format (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        nodd:
            Options: 1: Suppress output of Data Definition (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        dplace:
            Exporting to CSV only: specify the maximum number of decimal places to export. Options:
            -1: Use the best representation for the magnitude of the data.; 0: Export 0 decimal
            places; 1: Export 1 decimal place.; 2: Export 2 decimal places; 3: Export 3 decimal
            places; 4: Export 4 decimal places; 5: Export 5 decimal places
            Range=-1,5
            Values=-1,0,1,2,3,4,5
            Default=-1
            Required=No

        implicit:
            Exporting to CSV only: if no output fields are specified, allows you to either export
            explicit fields only, or explicit and implicit fields. Options: 0: All explicit fields
            are exported.; 1: All fields are exported, including implicit fields.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "output "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if fieldlst_i != "optional":
            command += " &fieldlst=" + fieldlst_i

        if fieldnam_f != "optional":
            command += " *fieldnam=" + fieldnam_f

        if fields_f[0] != "optional":
            command += self.parse_infields_list("f", fields_f, 25, "*")

        if csv_p != "optional":
            try:
                val = float(csv_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"csv_p value {csv_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(csv_p, (int, float)):
                    raise e

        if csv_p != "optional":
            command += " @csv=" + str(csv_p)

        if nodd_p != "optional":
            try:
                val = float(nodd_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"nodd_p value {nodd_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(nodd_p, (int, float)):
                    raise e

        if nodd_p != "optional":
            command += " @nodd=" + str(nodd_p)

        if dplace_p != "optional":
            try:
                val = float(dplace_p)
                if val not in [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0]:
                    raise ValueError(f"dplace_p value {dplace_p} is not in allowed values: [-1, 0, 1, 2, 3, 4, 5]")
            except ValueError as e:
                if isinstance(dplace_p, (int, float)):
                    raise e

        if dplace_p != "optional":
            command += " @dplace=" + str(dplace_p)

        if implicit_p != "optional":
            try:
                val = float(implicit_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"implicit_p value {implicit_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(implicit_p, (int, float)):
                    raise e

        if implicit_p != "optional":
            command += " @implicit=" + str(implicit_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def selcop(self,
                in_i="required",
                fieldlst_i="optional",
                out_o="required",
                f1_f="optional",
                f2_f25_f="optional",
                fieldnam_f="optional",
                keepall_p=0,
                keytol_p=1e-05,
                arguments="optional",
                retrieval="optional"):

        r"""
        SELCOP
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------

        in: Table
            Input file.
            Required=Yes

        fieldlst: Undefined
            File to supply selected fields.
            Required=No

        Output Files:
        -------------

        out: Table
            Output file with selected fields.
            Required=Yes

        Fields:
        -------

        f1: Any : IN
            Selected field 1.
            Default=Undefined
            Required=Yes

        f2_f25: Any : IN
            Optional selected fields.
            Default=Undefined
            Required=No

        fieldnam: Character : FIELDLST
            Field in **FIELDLST** to identify selected fields.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        keepall:
            Options: 1: copy all records; (0): ignore duplicate successive records.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        keytol:
            **KEYTOL** is the tolerance value used to test whether numeric key values are equal. It
            must be greater than or equal to zero. It replaces the previous heuristic comparison
            method. If **KEYTOL** is set to a negative value then zero is used. In a macro
            **KEYTOL** can be set to absent using -. "@**KEYTOL** =-" This will revert to legacy
            behaviour of a tolerance of zero being used.
            Range=0,+
            Values=Undefined
            Default=0.00001
            Required=No

        """
        command = "selcop "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if fieldlst_i != "optional":
            command += " &fieldlst=" + fieldlst_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if f1_f != "optional":
            command += " *f1=" + f1_f

        if f2_f25_f != "optional":
            command += " *f2-f25=" + f2_f25_f

        if fieldnam_f != "optional":
            command += " *fieldnam=" + fieldnam_f

        if keepall_p != "optional":
            try:
                val = float(keepall_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"keepall_p value {keepall_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(keepall_p, (int, float)):
                    raise e

        if keepall_p != "optional":
            command += " @keepall=" + str(keepall_p)

        if keytol_p != "optional":
            command += " @keytol=" + str(keytol_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def seldel(self,
                in_i="required",
                fieldlst_i="optional",
                out_o="required",
                f1_f="optional",
                f2_f25_f="optional",
                fieldnam_f="optional",
                keepall_p=0,
                keytol_p=1e-05,
                arguments="optional",
                retrieval="optional"):

        r"""
        SELDEL
        ------
        Selectively deletes named fields from the input file during a copy to the output file.

The fields to be deleted are specified as * **F1** to * **Fn**. Any number of required fields may be deleted, but only one is compulsory.

If retrieval criteria are specified they will be ignored if they are on the deleted fields.

If the optional parameter @**KEEPALL** is zero (default) the output file will only contain one entry for each combination of output field values, provided that the input file is first sorted on these fields. If the input file is not sorted, then the output file will contain one entry for each combination of output field values which occur together in the input file.

The process works by checking the selected field values against the values just written to the output file. If they are identical, the current record is skipped.

        Input Files:
        ------------

        in: Table
            Input file.
            Required=Yes

        fieldlst: Undefined
            File to supply selected fields.
            Required=No

        Output Files:
        -------------

        out: Table
            Output file with deleted fields.
            Required=Yes

        Fields:
        -------

        f1: Any : IN
            Deleted field 1.
            Default=Undefined
            Required=No

        f2_f25: Any : IN
            Optional selected fields.
            Default=Undefined
            Required=No

        fieldnam: Character : FIELDLST
            Field in **FIELDLST** to identify selected fields.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        keepall:
            Used to keep or delete records with duplicate successive key field values Options: (0):
            Do not copy successive duplicate records.; 1: Copy all records to Output File, even if
            adjacent records have identical Key Field values.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        keytol:
            KEYTOL is the tolerance value used to test whether numeric key values are equal. It
            must be greater than or equal to zero. It replaces the previous heuristic comparison
            method. If KEYTOL is set to a negative value then zero is used. In a macro KEYTOL can be
            set to absent using -. "@KEYTOL=-" This will revert to legacy behaviour of a tolerance
            of zero being used.
            Range=0,+
            Values=Undefined
            Default=0.00001
            Required=No

        """
        command = "seldel "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if fieldlst_i != "optional":
            command += " &fieldlst=" + fieldlst_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if f1_f != "optional":
            command += " *f1=" + f1_f

        if f2_f25_f != "optional":
            command += " *f2-f25=" + f2_f25_f

        if fieldnam_f != "optional":
            command += " *fieldnam=" + fieldnam_f

        if keepall_p != "optional":
            try:
                val = float(keepall_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"keepall_p value {keepall_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(keepall_p, (int, float)):
                    raise e

        if keepall_p != "optional":
            command += " @keepall=" + str(keepall_p)

        if keytol_p != "optional":
            command += " @keytol=" + str(keytol_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def selexy(self,
                in_i="required",
                perim_i="required",
                out_o="required",
                x_f="optional",
                y_f="optional",
                attribs_f=['optional'],
                outside_p=0,
                perim_p="optional",
                print_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        SELEXY
        ------
        Selectively copy records for which X and Y co-ordinate values lie within a perimeter defined in a perimeter file.

If the parameter @**OUTSIDE** =1, then values outside the perimeter will be selected. A perimeter must consist of at least the standard explicit numeric fields **XP, YP, ZP, PVALUE** and **PTN**. It must contain more than 2 and less than 1500 points.

### Multiple perimeters

Multiple perimeters may be processed at once. The output file will contain records which are selected by any of the perimeters. If selection is inside perimeters (default) then the effect is that selected records will come from the union of all perimeters. If selection is outside perimeters, then records will be selected if they lie outside any one perimeter, even if they lie inside another.

There is a limit to the number of perimeters which may be processed at one time. Under no circumstances may more than 100 perimeters be processed; but this limit may be lower, depending on the implementation and the number of points in each perimeter. All perimeters are first read into the real part of Studio 3's virtual array. Each point occupies 2 words. The size of this array is usually 100,000 words for implementations. With these values, the maximum number of points is 50,000 for most implementations. Each perimeter is closed in the array, by addition of an extra point. Thus the number of perimeters that can be handled depends on the total number of points in the input file. Any perimeters that cannot fit in their entirety into the virtual array will be ignored with a warning.

Once the perimeters have been read in, **SELEXY** makes a single pass through the input file, examining each record against all perimeters. This is a very fast method of processing data, and ensures that the order of the output file is the same as the order of the input file.

**Note** : The X,Y fields in the &**IN** file are assumed to refer to the same co-ordinate system as the **XP,YP** fields in the &**PERIM** file.

### Single Perimeter

A single perimeter may be selected from a multi-perimeter file by setting the required **PVALUE** into optional parameter @**PERIM**.

### Flagging selected records

Selected records may be flagged by up to 4 words of information taken from the perimeter that selected them. These four words may be either 4 numeric fields, or a combination of alphanumeric and numeric fields up to 4 words long. These fields are identified as * **ATTRIB1** -* **ATTRIB4** ; they must exist in the perimeter file, and will be placed in the output file if they do not already exist. For example, the **PVALUE** field may be used to flag which perimeter the record was selected by. If a record should be selected by more than one perimeter, then the values will be taken from the last perimeter that selected the record.

The value of the * **ATTRIB** fields used in flagging will be that associated with the first point of the perimeter.

### In Place operations

The input and output files may be the same for in-place flagging of values. Retrieval criteria may also be used if required. There is however no point in in-place selection unless the input file contains a field that may be flagged to indicate selection. In-place updating is specified by setting the input and output files to the same names, and specifying at least one * **ATTRIB** field that exists in both the perimeter file and the input file. The **PVALUE** field is often used for this purpose. An error is generated if the *ATTRIB field does not exist already in the input file, as new fields cannot be added in-place.

        Input Files:
        ------------

        in: Undefined
            Input file for selection. Must have explicit numeric fields X and Y.
            Required=Yes

        perim: String
            Perimeter file to control selection. Must have perimeter points in clockwise order,
            with the perimeter closed. The fields required are **XP,YP,ZP,PTN** , and **PVALUE**
            (standard perimeter format). All perimeters in the file will be used, up to a maximum of
            100, or the number that will fit into the real part of the virtual array (usually
            100,000 for all except your application on the PC, where it is 10,000). Perimeters which
            do not fit will be ignored with a warning. May also contain fields **ATTRIB1** -**4**
            which can be carried across to the output file. The value of these fields at the first
            point is used.
            Required=Yes

        Output Files:
        -------------

        out: Undefined
            Output file containing all records lying within (or optionally outside) the perimeter.
            The **OUT** file may be the same as the IN file for in-place operations, unless extra
            fields ( **ATTRIB1** -**4**) from the perimeter file are being added.
            Required=Yes

        Fields:
        -------

        x: Numeric : IN
            Field in **IN** file defining the X co-ordinate.
            Default=Undefined
            Required=Yes

        y: Numeric : IN
            Field in **IN** file defining the Y co-ordinate.
            Default=Undefined
            Required=Yes

        attribs: Undefined : Undefined
            Field from the perimeter file to be placed into the output file for all records which are selected. Up to 4 words may be entered, which may be 4 numeric fields or a mixture of alphanumeric and numeric fields totalling 4 words.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        outside:
            Options: 1: Copies records of a file which have X and Y co-ordinates lying outside the
            perimeter (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        perim:
            Set to the required **PVALUE** field to select a particular perimeter from **PERIM**.
            If **PERIM** is not set, then all perimeters will be processed.
            Range=Undefined
            Values=Undefined
            Default=Undefined
            Required=No

        print:
            >=1 Display summary stats for each perimeter and DDs.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        """
        command = "selexy "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if perim_i == "required":
            raise ValueError("perim_i is required.")

        if perim_i != "optional":
            command += " &perim=" + perim_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if x_f != "optional":
            command += " *x=" + x_f

        if y_f != "optional":
            command += " *y=" + y_f

        if attribs_f[0] != "optional":
            command += self.parse_infields_list("attrib", attribs_f, 4, "*")

        if outside_p != "optional":
            try:
                val = float(outside_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"outside_p value {outside_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(outside_p, (int, float)):
                    raise e

        if outside_p != "optional":
            command += " @outside=" + str(outside_p)

        if perim_p != "optional":
            command += " @perim=" + str(perim_p)

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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def stats(self,
                in_i="required",
                fieldlst_i="optional",
                out_o="optional",
                fields_f=['optional'],
                fieldnam_f="optional",
                keys_f=['optional'],
                weight_f="optional",
                keysort_p='No',
                keytol_p=1e-05,
                pcntiles_p=0,
                sortout_p=1,
                print_p=2,
                arguments="optional",
                retrieval="optional"):

        r"""
        STATS
        -----
        Calculate general summary parametric statistics on numeric fields in a file.

Individual fields for statistics may be selected using either the ***F1, *F2** , etc fields or may be specified in the &**FIELDLST** file. If no fields are selected then statistics will be calculated for all fields.

Ten optional keyfields are provided. If no keyfields are specified then a single set of statistics will be calculated for all data. If keyfields are specified and parameter **KEYSORT** =1 or the input file is already sorted by keyfield then statistics will be calculated for each unique combination of key values. If keyfields are specified and parameter **KEYSORT** =0 and the input file is not sorted by keyfield then data will be read from the input file until the value of one of the keyfields changes and the statistics will then be calculated for that data subset.

Note: A limit of 256 fields is imposed. If more than 256 fields exist in &IN, the process will not complete.

An optional weighting field (* **WEIGHT**) is available to weight the sample data. For example in a desurveyed drillhole file the **LENGTH** field could be used as the weighting field to give length weighted grades.

Note: When calculating **MAD** and percentile statistics, **WEIGHT** is ignored.

The variance and other moments are calculated using the large sample method (for the variance a divisor of N is used, where N is the number of samples).

The following statistics are calculated for each numeric variable :-

  * total number of records in the file that meet retrieval criteria, if specified
  * number of samples (excluding absent data).
  * number of absent data values.
  * minimum, maximum, range and mid-range.
  * total and mean.
  * variance, standard deviation and standard error.
  * skewness and kurtosis.
  * geometric mean.
  * Sum, mean and variance of natural logs.
  * log estimate of mean.
  * coefficient of variation in percent.
  * number of records equal to zero.
  * number of negative value.

These results are displayed in the Command window and can also be saved to an optional &OUT file..

If the **PCNTILES** parameter is set to 1 then the 5, 10, 20, 25, 30, 40, 50, 60, 75, 80, 90 and 95 percentiles and the Median Absolute Deviation are also calculated. Processing will take longer. If this option is selected it is helpful to specify only the fields for which you wish to calculate the statistics. The Weight field is not used when calculating percentiles.

By default, statistics are calculated for all numeric variables. For example; in a typical drillhole data file containing sample co-ordinates, statistics will be calculated for both the values and the co-ordinates. The first bin in the histogram plot contains all values up to MINIMUM. The last bin contains all values above the top value. The log statistics are based on all sample values greater than, but not equal to, the system trace value.

Values of skewness and kurtosis calculated are interpreted as:

SKEWNESS |  = 0. No distortion (Gaussian).  
---|---  
|  > 0\. Positive skew (to the right).  
|  < 0\. Negative skew (to the left).  
KURTOSIS |  = 0. Mesokurtic (Gaussian).  
|  > 0\. Leptokurtic (peaked).  
|  < 0\. Platikurtic (flat).  
  
### Missing Values

When the **STATS** process is run with retrieval criteria, data that is excluded by those criteria will not be reported. This is a change from previous versions which classified excluded data as "Missing Values".

The following fields are also output:

  * **NSAMPLES** The number of samples in the chosen numeric (F1 etc) fields that are non-absent and used to calculate statistics.
  * **NMISVALS** The number of missing records in the chosen numeric (F1 etc) fields. Samples are classified as missing if they have an absent value.
  * **NUMTRACE** The number of samples in the chosen numeric (F1 etc) fields that are equal to the TRACE value
  * **EQUAL0** The number of records in the chosen numeric (F1 etc) fields that contain values that = 0.
  * **NEGATIVE** The number of records in the chosen numeric (F1 etc) fields that contain negative values.

        Input Files:
        ------------

        in: Table
            Input file.
            Required=Yes

        fieldlst: Undefined
            File to supply selected fields.
            Required=No

        Output Files:
        -------------

        out: Table
            Output file. This will contain the fields:
            Required=No

        Fields:
        -------

        fields: Undefined : Undefined
            Fields for statistics. If no fields are specified then all fields will be used.
            Default=Undefined
            Required=No

        fieldnam: Character : FIELDLST
            Field in FIELDLST to identify selected fields.
            Default=Undefined
            Required=No

        keys: Undefined : Undefined
            Key fields 1 for statistics.
            Default=Undefined
            Required=No

        weight: Numeric : IN
            Weighting field.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        keysort:
            Set to 1 to automatically sort the data by key field. Only relevant if any key fields
            have been defined. =0 : Do not automatically sort by key fields. Use the record order of
            the input file to determine changes in key field values. =1 : Automatically sort the
            input data by key fields.
            Range=Numeric
            Values=Undefined
            Default=No
            Required=No

        keytol:
            The tolerance used to test whether numeric key fields are equal. All key values are
            rounded to an integer multiple of this value. If set to zero then rounding will not be
            used.
            Range=0,+
            Values=Undefined
            Default=0.00001
            Required=No

        pcntiles:
            Set to 1 to calculate percentiles. When calculating percentiles the process will take
            longer to run. If this option is selected it is useful to specify only the fields for
            which you wish to calculate the statistics. If this option is selected the Median
            Absolute Deviation (MAD) value is also calculated. =0 : Do not calculate percentiles. Do
            not calculate the Median Absolute Deviation. =1 : Calculate the 5, 10, 20, 25, 30, 40,
            50, 60, 75, 80, 90 and 95 percentiles and the Median Absolute Deviation.
            Range=0,1
            Values=0,1
            Default=0
            Required=No

        sortout:
            Set to 1 to sort the output file by **FIELD** when key fields are being used. Sorting
            by **FIELD** makes it easier to compare values of variables across key fields when
            viewing the output file in the table editor. =0 : Do not sort the output file. =1 : Sort
            the output file by **FIELD**.
            Range=0,1
            Values=0,1
            Default=1
            Required=No

        print:
            Print flag. Default (2). 0: minimum output. 1: minimum output plus key field progress
            list. 2: full output including stats for each key field group.
            Range=0-2
            Values=0,1,2
            Default=2
            Required=No

        """
        command = "stats "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if fieldlst_i != "optional":
            command += " &fieldlst=" + fieldlst_i

        if out_o != "optional":
            command += " &out=" + out_o

        if fieldnam_f != "optional":
            command += " *fieldnam=" + fieldnam_f

        if weight_f != "optional":
            command += " *weight=" + weight_f

        if fields_f[0] != "optional":
            command += self.parse_infields_list("f", fields_f, 20, "*")

        if keys_f[0] != "optional":
            command += self.parse_infields_list("key", keys_f, 10, "*")

        if keysort_p != "optional":
            command += " @keysort=" + str(keysort_p)

        if keytol_p != "optional":
            command += " @keytol=" + str(keytol_p)

        if pcntiles_p != "optional":
            try:
                val = float(pcntiles_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"pcntiles_p value {pcntiles_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(pcntiles_p, (int, float)):
                    raise e

        if pcntiles_p != "optional":
            command += " @pcntiles=" + str(pcntiles_p)

        if sortout_p != "optional":
            try:
                val = float(sortout_p)
                if val not in [0.0, 1.0]:
                    raise ValueError(f"sortout_p value {sortout_p} is not in allowed values: [0, 1]")
            except ValueError as e:
                if isinstance(sortout_p, (int, float)):
                    raise e

        if sortout_p != "optional":
            command += " @sortout=" + str(sortout_p)

        if print_p != "optional":
            try:
                val = float(print_p)
                if val not in [0.0, 1.0, 2.0]:
                    raise ValueError(f"print_p value {print_p} is not in allowed values: [0, 1, 2]")
            except ValueError as e:
                if isinstance(print_p, (int, float)):
                    raise e

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def tongrad(self,
                in_i="required",
                out_o="required",
                csvout_o="optional",
                tgcumtiv_o="optional",
                keys_f=['optional'],
                orefrac_f="optional",
                density_f="optional",
                fields_f=['optional'],
                addfs_f=['optional'],
                factor_p=1,
                trename_p=0,
                setabsnt_p=0,
                density_p=1,
                column_p=0,
                row_p=0,
                bench_p=0,
                cogstep_p=0,
                keytol_p=1e-05,
                excel_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
        TONGRAD
        -------
        This process calculates the volume, tonnage and grade for up to 20 specified grade fields if run interactively although up to 60 fields can be selected using * **F21** etc if run from a macro or script. The results may be classified by up to five levels of keyfield.

Up to twenty additive fields can be specified. Rather than being weighted by mass these are accumulated. Examples of this type of field are revenue or cost.

All the grade and additive fields are optional. If no grade fields are specified then only tonnes and volume will be calculated.

The output results files are written to Datamine files and may optionally be saved in a system file in Comma Separated Variable (CSV) format. The CSV files contain the same results as the Datamine **OUT** and **TGCUMTIV** files, but are suitable for direct input to a spreadsheet.

#### Density Field (DENSITY)

If a density field is specified it will be used in the calculation of tonnes. If there is no density field you may assign a value to the **DENSITY** parameter. If both a density field and a density parameter are specified, the density field will be used in preference.

#### Absent Values

Absent density values are allowed in the input model file. If a record has an absent density value and the @**SETABSNT** parameter is set to 1 the parameter value for @**DENSITY** is used. The file's default value for density is never used.

Absent grades and ore fractions are allowed in the input file. The @**SETABSNT** parameter can be set to 1 to reset absent values. If a field has an absent value the default value from the data definition is used. If the default value is absent then a value of zero is used. If the @**SETABSNT** parameter is not set or has a value of zero absent grade, ore fraction and density values are detected and **TONGRAD** exits with an error.

In summary, If a grade or ore fraction field has an absent record the default value is used. If the default value is absent then a value of zero is used.

Absent density values are now allowed in the input file. If a record has an absent density value the parameter value for @DENSITY is used.

#### Keyfields (KEY1 to KEY5)

If you are using keyfields to classify the reserves (for example by rock type), then you may find it useful to run the process twice - once with keyfields and the second time without any keyfields. The second run will give just a single record in the output file, which will be the total tonnes and volume, and the average grade over the whole model.

If multiple keyfields are specified, then each line of the output results will describe each potential combination of different key field values. The data can then subsequently be utilized to produce tables with the key entries cross- referenced in many different ways with external data manipulation packages such as Excel.

#### Key Tolerance (KEYTOL)

The output files report grades and tonnes for every combination of key field. Sometimes numeric key values may differ by a very small amount, for example 0.0000000001. So that they are treated as the same number all key values will be rounded to an integer multiple of @**KEYTOL**. The default is 0.00001.

#### Additive Fields (ADDF1-20)

Fields to be treated as additive can be specified (using * **ADDF1** to * **ADDF20** in a macro, with a maximum of 10 fields via the interactive dialog). This is useful to provide a summary of total costs or revenues by keyfields in addition to just grades.

#### Ore Fractions (OREFRAC)

The ore-fraction field is optional. It is intended to be used where the contained grade fields pertain only to a certain proportion of each block, as might be the case with an MIK model. The supplied ore-fraction field must contain values between 0 and 1. If it is utilized, the output results will contain the calculated field **OTONNES** , with grades which pertain just to these **OTONNES** quantities. There will still be **TONNES** and **VOLUME** fields produced, describing the total evaluated (ore+waste) contents.

The **BENCH** , **ROW** and **COLUMN** parameters are optional. If any of them are enabled (=0), then additional **BENCH** /**ROW** /**COLUMN** values will be used in the categorization of calculated results, based on the model blocks' positions, and the parent block dimensions. These additional fields can then subsequently be used for table generation from the calculated results.

If **OREFRAC** is used then default **OREFRAC** value is taken from the file default value. If file default values is absent then default **OREFRAC** is zero. Default is used if any **OREFRAC** values are absent. Otherwise they must be between zero and 1.

#### Cut-Off Grades

The **COGSTEP** parameter is optional. If a value (>0) is supplied, then results will be split for each **COGSTEP** increment in the main (**F1**) grade field. This will enable the results to be used directly for generation of grade-tonnage curves. If the **COGSTEP** parameter is specified a grade field in **F1** MUST be specified.

An output file (* **TGCUMTIV**) containing cumulative values for cutoffs can optionally be specified and used to draw grade-tonnage curves more directly. Examples of using this table in Studio and Excel are shown below:

[![](../Images/TONGRAD1.png)](<javascript:void\(0\);>)

[![](../Images/TONGRAD2.png)](<javascript:void\(0\);>)

The **FACTOR** parameter is optional. If a value is supplied, then the values for **VOLUME** , **TONNES** and **OTONNES** will be divided by this factor.

The **TRENAME** parameter can be set to 1 to automatically change the output **VOLUME** , **TONNES** and **ORETON** field names according to the value of the **FACTOR** parameter. For example, if **TRENAME** is 1 and **FACTOR** is 1000 then the output field names are **KVOLUME** , **KTONNES** and **KORETON**. For values other than 1000 the output field names are shown in the table below.

The default value for **TRENAME** is 0. This preserves the standard field names of VOLUME, TONNES and ORETON.

Field names in Output Files for TRENAME=1  
---  
FACTOR Value | Tonnes | Volume | Ore Tonnes  
FACTOR=1 | TONNES | VOLUME | ORETON  
FACTOR=1000 | KTONNES | KVOLUME | KORETON  
FACTOR=10000 | 10KTONNES | 10KVOL | 10KOTON  
FACTOR=100000 | 100KTONNES | 100KVOL | 100KOTON  
FACTOR=1000000 | 1MTONNES | 1MVOLUME | 1MORETON  
FACTOR<1000 | TxFACTOR | VxFACTOR | OxFACTOR  
FACTOR>1000<100000 | TNxFACTOR | VOxFACTOR | OTxFACTOR  
  
The @**SETABSNT** parameter can be set to 1 to set absent grade to their default or zero values automatically. Absent Density values are set to the default **DENSITY** parameter value. The number of records that contain reset values is written to the output window. If the @**SETABSNT** is undefined or set to zero then absent grade and density values are detected and **TONGRAD** exits with an error.

### Excel Output

**Note** : Microsoft Excel 2010 or later is required on the local PC in order to view output from this command.

If @**EXCEL** is set to 1 then and the cumulative output data file (**TGCUMTIV**) has been created then the results will automatically be loaded into **EXCEL** (if version 2016 or higher is installed) and a chart of tonnes and grade against cutoff will be displayed. However note that **EXCEL** will not be run if any of the **COLUMN** , **ROW** or **BENCH** options have been selected.

If two or more KEY fields have been specified they will be combined into a single numeric compound Key field (**COMP_KEY**). The chart will then include a line for each value of **COMP_KEY**.

Also note that the process will not complete until an automatically-launched instance of Excel is closed.

        Input Files:
        ------------

        in: Model file
            Input model file
            Required=Yes

        Output Files:
        -------------

        out: Table
            Output reserves file.
            Required=Yes

        csvout: Table
            Optional CSV Output file. This is a system file, not a Datamine file. It contains the
            same results as the Datamine **OUT** file, but it is a Comma Separated Variable (CSV)
            file, suitable for input to a spreadsheet. The extension .csvwill be added automatically
            to the file name.
            Required=No

        tgcumtiv: Table
            Output tonnes grade curve cumulative data file. This can only be output if the
            @**COGSTEP** parameter is set to define cutoffs. This table can be used to create
            tonnage grade curves.
            Required=No

        Fields:
        -------

        keys: Undefined : Undefined
            Key fields for reserve classification.
            Default=Undefined
            Required=No

        orefrac: Numeric : IN
            Ore fraction field \- containing values between 0 and 1.
            Default=Undefined
            Required=No

        density: Numeric : IN
            Field containing density values. If a field is not selected then the value specified by
            the **DENSITY** parameter will be used.
            Default=DENSITY
            Required=No

        fields: Undefined : Undefined
            Grade fields for evaluation. **F1** is primary grade field.
            Default=Undefined
            Required=No

        addfs: Undefined : Undefined
            1st to 10th fields to be treated as additive.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        factor:
            Scaling factor to adjust the units of the Volume and Tonnage in the output files.
            Volume and Tonnage are divided by this factor.
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        trename:
            The @**TRENAME** parameter can be used to change the output field name of **TONNES** to
            reflect the use of the @**FACTOR** parameter.
            Range=Undefined
            Values=Undefined
            Default=0
            Required=No

        setabsnt:
            Set to 1 to allow **TONGRAD** to reset absent grade, ore fraction and density values.
            If this is used, absent grade values are set to their default values. If the default
            value is absent grade values are set to zero. If density values are absent the default
            **DENSITY** parameter value is used.
            Range=Undefined
            Values=Undefined
            Default=0
            Required=No

        density:
            Density value to be used for tonnage calculations if a **DENSITY** field is not used.
            Range=Undefined
            Values=Undefined
            Default=1
            Required=No

        column:
            Set to 1 for additional **COLUMN** (YZ slices by X) categorisation.
            Range=0,1
            Values=Undefined
            Default=0
            Required=No

        row:
            Set to 1 for additional **ROW** (XZ slices by Y) categorisation.
            Range=0,1
            Values=Undefined
            Default=0
            Required=No

        bench:
            Set to 1 for additional **BENCH** (XY slices by Z) categorisation.
            Range=0,1
            Values=Undefined
            Default=0
            Required=No

        cogstep:
            Cut-off grade step, which applied to main F1 grade field, and then used for
            categorisation of results.
            Range=Undefined
            Values=Undefined
            Default=0
            Required=No

        keytol:
            The tolerance used to test whether numeric key fields are equal. All key values are
            rounded to an integer multiple of this value. If set to zero then rounding will not be
            used.
            Range=0,+
            Values=Undefined
            Default=0.00001
            Required=No

        excel:
            Set to 1 to automatically load the cumulative data file into Excel (2010 or later
            version required) and display a graph of tonnes and grade against cutoff.
            Range=0,1
            Values=Undefined
            Default=0
            Required=No

        """
        command = "tongrad "

        if in_i == "required":
            raise ValueError("in_i is required.")

        if in_i != "optional":
            command += " &in=" + in_i

        if out_o == "required":
            raise ValueError("out_o is required.")

        if out_o != "optional":
            command += " &out=" + out_o

        if csvout_o != "optional":
            command += " &csvout=" + csvout_o

        if tgcumtiv_o != "optional":
            command += " &tgcumtiv=" + tgcumtiv_o

        if orefrac_f != "optional":
            command += " *orefrac=" + orefrac_f

        if density_f != "optional":
            command += " *density=" + density_f

        if keys_f[0] != "optional":
            command += self.parse_infields_list("key", keys_f, 20, "*")

        if fields_f[0] != "optional":
            command += self.parse_infields_list("f", fields_f, 20, "*")

        if addfs_f[0] != "optional":
            command += self.parse_infields_list("addf", addfs_f, 10, "*")

        if factor_p != "optional":
            command += " @factor=" + str(factor_p)

        if trename_p != "optional":
            command += " @trename=" + str(trename_p)

        if setabsnt_p != "optional":
            command += " @setabsnt=" + str(setabsnt_p)

        if density_p != "optional":
            command += " @density=" + str(density_p)

        if column_p != "optional":
            try:
                val = float(column_p)
                if not (0.0 <= val <= 1.0) and val != 0.0:
                    raise ValueError(f"column_p value {column_p} is not in allowed range: [0.0, [1.0]")
            except ValueError as e:
                if isinstance(column_p, (int, float)):
                    raise e

        if column_p != "optional":
            command += " @column=" + str(column_p)

        if row_p != "optional":
            try:
                val = float(row_p)
                if not (0.0 <= val <= 1.0) and val != 0.0:
                    raise ValueError(f"row_p value {row_p} is not in allowed range: [0.0, [1.0]")
            except ValueError as e:
                if isinstance(row_p, (int, float)):
                    raise e

        if row_p != "optional":
            command += " @row=" + str(row_p)

        if bench_p != "optional":
            try:
                val = float(bench_p)
                if not (0.0 <= val <= 1.0) and val != 0.0:
                    raise ValueError(f"bench_p value {bench_p} is not in allowed range: [0.0, [1.0]")
            except ValueError as e:
                if isinstance(bench_p, (int, float)):
                    raise e

        if bench_p != "optional":
            command += " @bench=" + str(bench_p)

        if cogstep_p != "optional":
            command += " @cogstep=" + str(cogstep_p)

        if keytol_p != "optional":
            command += " @keytol=" + str(keytol_p)

        if excel_p != "optional":
            try:
                val = float(excel_p)
                if not (0.0 <= val <= 1.0) and val != 0.0:
                    raise ValueError(f"excel_p value {excel_p} is not in allowed range: [0.0, [1.0]")
            except ValueError as e:
                if isinstance(excel_p, (int, float)):
                    raise e

        if excel_p != "optional":
            command += " @excel=" + str(excel_p)

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

