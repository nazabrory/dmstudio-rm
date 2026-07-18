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


        Commands initialization. After the commands class is initialized for the first time the object will
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

    def inpfil(self,
                out_o="required",
                print_p=0,
                arguments="optional",
                retrieval="optional"):

        r"""
    .. warning::
        **USE WITH CAUTION** – This command has known interactive or console-
        prompt behaviour. It *may* work with fully-specified arguments via
        ``Parsecommand()``, but unexpected pop-ups or missing parameters will
        lock the COM server. Verify manually before using in automation.

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

