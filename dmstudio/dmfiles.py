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
        if self.oScript is not None:
            try:
                if self.oScript.ActiveProject is None:
                    import warnings
                    warnings.warn(
                        "Datamine Studio RM is connected, but no active project is loaded. "
                        "Please open a project (.rmproj) in Studio RM before executing commands.",
                        UserWarning
                    )
            except Exception:
                pass

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

    def comres(self,
                reserve_o="required",
                zone_f="optional",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def estimate(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def export(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def fdin(self,
                out_o="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def fxin(self,
                out_o="required",
                filetype_p=1,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inpddf(self,
                out_o="required",
                print_p=0,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inpfil(self,
                out_o="required",
                print_p=0,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inpfml(self,
                out_o="required",
                print_p=0,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inputc(self,
                out_o="required",
                print_p=0,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def inputd(self,
                out_o="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def link(self,
                out_o="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def listdr(self,
                out_o="optional",
                fieldnam_f="optional",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def loadcf(self,
                print_p=0,
                level_p=0,
                encrypt_p=0,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def monaco(self,
                out_o="required",
                nrecs_p="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

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
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def picted(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def protom(self,
                out_o="required",
                rotmod_p=0,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def protop(self,
                out_o="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def quig(self,
                out_o="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

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
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def scrfmt(self,
                out_o="optional",
                text_f="optional",
                width_p=80,
                print_p=0,
                arguments="optional",
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
                if not (1.0 <= val <= 132.0) and val != 80.0:
                    raise ValueError(f"width_p value {width_p} is not in allowed range: [1.0, [132.0]")
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def secdef(self,
                out_o="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def setenv(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def sortx(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def sudttr(self,
                wiretr_o="required",
                wirept_o="required",
                sid_p="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def surlog(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def sustp2(self,
                out_o="required",
                direct_p="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def sustpe(self,
                out_o="required",
                direct_p="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def syspar(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def tdin(self,
                out_o="required",
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def ver(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

    def xrun(self,
                arguments="optional",
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

        if arguments != "optional":
            command += " " + arguments

        if retrieval != "optional":
            command += "{" + retrieval + "}"

        self.run_command(command)

