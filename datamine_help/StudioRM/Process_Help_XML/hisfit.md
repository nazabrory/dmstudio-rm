# HISFIT Process

To access this process:

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **HISFIT** and click **Run**.

  * Enter "HISFIT" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_H.md#HISFIT>).

## Process Overview

Perform interactive histogram least-square distribution fitting.

**HISFIT** calculates and displays histograms which can be used to estimate the parameters of mixture of normal or lognormal distributions. A maximum of 8 modes of distribution is available. On entry to process HISFIT, a list of all numeric explicit fields are displayed. After selection of required field, the user is prompted for input of histogram parameters.

The plot files generated using PL sub-command will have missing XSCALE and YSCALE values so as to facilitate plot superimposition.

On entry to the process the following messages and prompts are displayed:-
    
    
                INTERACTION VIA CURSOR
    
    
                >>> Please wait - Initialization in progress.
    
    
                =/\=/\=/\=/\=/\=/\=/\=/\=/\=/\=/\=
    
    
                The following numeric fields are available for histogram generation
    
    
                =\/=\/=\/=\/=\/=\/=\/=\/=\/=\/=\/=
    
    
                Grade1 Grade2 Grade3 ............
    
    
                >>> Enter the field for histogram generation
    
    
                Numeric field [Grade1 ] > Enter field name.
    
    
                
    
    
                D A T A S C R E E N I N G
    
    
                ***************************
    
    
                >>> ENTER LOWER, UPPER OR BOTH LIMITS TO SCREEN <<<
    
    
                >>> THE RAW DATA. IF YOU DO NOT WISH TO APPLY <<<
    
    
                >>> THESE LIMITS THEN PRESS <RETURN> KEY : <<<
    
    
                Lower cutoff for data [nnnn.n] > Enter lower cutoff for data selection.
    
    
                Upper cutoff for data [nnnn.n] > Enter upper cutoff for data selection.
    
    
                
    
    
                H I S T O G R A M P A R A M E T E R S
    
    
                ***************************************
    
    
                >>> ENTER RELEVANT HISTOGRAM PARAMETERS. <<<
    
    
                >>> IF YOU DO NOT WISH TO ENTER THESE VALUES, <<<
    
    
                >>> USE THE DEFAULT VALUES BY PRESSING THE <RETURN> KEY.<<<
    
    
     
    
    
                >>> DEFAULT NUMBER OF BINS IS CALCULATED BY THE STURGESS RULE.
    
    
     
    
    
                Bin width [nnnn.n ] > Enter histogram bin width.
    
    
                Lower bound of first bin [nnnn.n ] > Enter lower bound of first histogram bin.
    
    
                Number of bins (max 200) [nnnn.n ] > Enter number of bins for histogram.
    
    
     
    
    
                >>> Please wait : Histogram computation in progress.

A listing of simple statistics on the input data set and histogram modal information are displayed. The generated histogram is displayed on the graphics screen and the following commands can be entered either by selecting them by cursor or by entering the 2 character commands on the keyboard:-

AA  |  ANNOTATE AXES [/DA]  |  X annotation > Enter X-axis annotation. Y annotation > Enter Y-axis annotation.  
---|---|---  
AP  |  ANNOTATE PLOT [/DP]  |  Default annotation is 'Histogram Type' at top of plot. The new user defined Annotation of up to 80 chars can be positioned anywhere in the plot area. Annotation > _Enter plot annotation._ >>> Coords of bottom left corner >>> Define start point of text with cursor Move cursor to required position F1 function key or Button 1 on the mouse. >>> XPOS = 123.45 , YPOS = 678.90 Cursor position is reported Angle of anot. > _Enter angle in degrees, clockwise from positive X-axis._  
CP  |  CHANGE PARAMETER [/MC]  |  Change the value of one of the model parameters. Current values are displayed and prompts are displayed for defining a new value: Model histogram : Distribution type L with 1 components. Component: 1 Mean: 5.1090 Standard Deviation: 3.9412 Proportion: 1.000 A listing of all parameters. Select component number [1] >  _Select number 1 - 8._ Select parameter (Mean, Std., Prop) [Mean] > Parameter value [5.1090] >  _Select new value._  
CU  |  CURSOR [/CU]  |  Switch to cursor input mode. >>> Changing to keyboard input mode. >EDIT > CU >>> Changing to cursor input mode.  
DF  |  DEFAULTS [/E]  |  Set/change default settings. _Current Default Values_ 1 Character Size [4.0] 2 Default Color [1] 3 Background Fill Color [1128] 4 Data Area Fill Color [1126] 5 Histogram Color [4] 6 Model Histogram Color [10] 7 Return to Main Process > Option >  _Select option 1-7._ For Option 1: Set Character size and aspect ratio >Charsize >  _Enter size in mm (0-100)_ >Aspratio >  _Enter ratio (0-10)_ For Option 2: Set default color for plotting >Color >  _Enter color (1-15)_ For Option 3: Set background fill color for plotting >Background fill color >  _Enter fill code (1126 - 1140)_ For Option 4: Set data area fill color for plotting > Data area fill color >  _Enter fill code (1126 - 1140)_ For Option 5: Set histogram color for plotting > Color >  _Enter color (1-15)_ For Option 6: Set model histogram color for plotting > Color > _Enter color (1-15)_  
DP  |  DISPLAY PARAMETERS [/MD]  |  Display model parameters : Model histogram : Distribution type L with 1 components. Component: 1 Mean: 5.1090 Standard Deviation: 3.9412 Proportion: 1.000 A listing of all parameters.  
EX  |  EXIT [/X]  |  Exit from process HISFIT.  
GI  |  GRID [/DG]  |  Define grid type, grid interval for grid annotation. Most useful grid types are 3 (frame with inside ticks, the default) Grid type > _Enter grid value_ X interval > _Enter X tick interval_ Y interval > _Enter Y tick interval_ >>> Number of decimal places for annotation X coordinate> _Enter no. decimals for X axis_ Y coordinate> _Enter no. decimals for Y axis_  
GM  |  GET MODEL [/FG]  |  Get a model from the output file. This will become the current model. >>> Getting model from output file. Model ref. no. > _Enter model ref number as defined when using WRITE MODEL [/FW] command._ >>> Now plot model (PLOT CURRENT MODEL [/DM]) if required.  
HE  |  HELP [/H]  |  All the commands available in process HISFIT are displayed. SYSTEM CONTROL Redraw [/CR] Help [/CH] Cursor [/CU] Reset Limits [/CL] Histogram Type [/CG] PLOT CONTROL Redraw [/PR] Help [/PH] Annotate Axes [/PA] Annotate Plot [/PP] Grid [/PG] Plot Current Model [/PM] Plot Model Components [/PC] MODEL CONTROL Redraw [/MR] Help [/MH] Change Parameters [/MC] Display Parameters [/MD] Histogram [/MG] Summary Stats [/MS] Non-Parametric Stats [/MN] Multi Distribution [/MM] Single Distribution [/MI] FILE IN/OUT Redraw [/FR] Help [/FH] Macro [/FA] Write Histogram [/FG] Superimpose Plot [/FS] Make Plot File [/FM] Get Model [/FG] Write Model [FW]  
HI  |  HISTOGRAM [/MG]  |  Calculate histogram. A list of available numeric explicit fields are displayed and the following prompts are displayed:- Enter the field for histogram generation Numeric field [AU ] > Lower cutoff for data [ 1.0 ] > Upper cutoff for data [ 31.0 ] > Bin width [ 2.2 ] > Lower bound of first bin [ 1.0 ] > Number of bins (max 200) [ 14.0 ] > After the selection of histogram parameters, simple statistics and histogram modal information for the selected field are displayed.  
---|---|---  
MM  |  MULTI DISTRIBUTION [/MM]  |  Estimate parameters for multiple distribution model of histogram. The following prompts are displayed:- Distribution type [L] > _Enter "L" for Lognormal or "N" for Normal_ Number of components (max 8) [3] > _Enter 1-8._ >>> ENTER THE PARAMETERS FOR COMPONENT 1<<< Mean [ 6.5 ] > Standard dev [ 2.8814 ] > Proportion [ 0.4784 ] > The above prompts are repeated for every component. A list of the initial and final estimated for the required multimodal distribution analysis are displayed and the user is then prompted for: Accept the final estimates in preference to the initial estimates? Confirm ("Y" or "N") [Y ] >  
MS  |  SINGLE DISTRIBUTION [/MI]  |  Estimate parameters for single distribution model histogram. Distribution type [L] > _Enter "L" for Lognormal or "N" for Normal_ Mean [ 5.109 ] > Standard dev [ 3.9412 ] >  
NS  |  NON-PARAMETRIC STATS [/MN]  |  Calculate and display non-parametric statistics on current field.  
PA  |  REDRAW [/DR]  |  Refresh screen.  
PC  |  PLOT MODEL COMPONENTS [/DC]  |  Display individual model component. Enter component number [1] > _Enter 1-8._  
PL  |  MAKE PLOT FILE [/FM]  |  Make a plot file of the screen display. Plot file name > _Enter name of plot file._  
PM  |  PLOT CURRENT MODEL [/DM]  |  Display of current histogram model. Also acts as a toggle to remove model display.  
RU  |  MACRO [/FA]  |  Run a macro of commands. The following prompts are displayed: RUN A MACRO OF INTERACTIVE GRAPHICS COMMANDS ============================================ The macro must only contain valid commands and their data. Nesting is not permitted. Enter the name of the system file to execute SYSFILE> _Enter macro system filename._  
SE  |  HISTOGRAM TYPE [/CG]  |  Select histogram plot and display types. The following messages and prompts are displayed:- >>> Select histogram plot type. The available histogram plot types are: 10 Frequency Plot by AU 11 Frequency Plot by Log(AU ) 20 % Frequency Plot by AU 21 % Frequency Plot by Log(AU ) 30 Probability Plot by AU 31 Probability Plot by Log(AU )-Log scale bins 32 Probability Plot by Log(AU )-Linear scale bins Histogram plot type [ 10] > _Select plot type_ The following histogram and model display types are available :- 1 BAR GRAPH 2 LINE GRAPH 3 SYMBOL (PLUS) 4 SYMBOL (CROSS) Data histogram display type [ 1] > _Select 1-4._ Model histogram display type [ 2] > _Select 1-4._  
SS  |  SUMMARY STATS [/MS]  |  Calculate and display summary statistics on current field.  
SU  |  SUPERIMPOSE PLOT [/FS]  |  Superimpose a Datamine plot file on current display. DATAMINE FILENAME? > _Enter the required plot file name._  
WH  |  WRITE HISTOGRAM [/FG]  |  Write histogram to file. The following fields are generated:- LOWER, MIDDLE, UPPER, FREQENCY, CUMFREQ., FREQ-%,CUMF-%, AVIVAL, FIELD and TOTVAL. The following prompt is displayed:- Histogram file name > _Enter output histogram file name._  
WM  |  WRITE MODEL [/FW]  |  Write model to output file. The model parameters are written to the following fields:- MODELREF, FIELD, DISTTYPE, NUM.COMP, MEAN1, STD.DEV1, PROP1,...,MEAN8, STD.DEV8, PROP8. The following prompt is displayed:- Model ref. no. > _Enter model reference number._  
XY  |  RESET LIMITS [/CL]  |  Set X-Y limits of histogram display area. XMIN Enter minimum X value. XMAX Enter maximum X value. YMIN Enter minimum Y value. YMAX Enter maximum Y value.  
  
## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Raw data file. Must contain at least one numeric explicit field. |  Input |  Yes |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
MODELOU |  Output |  No |  Histogram |  Histogram model output file. The histogram distribution model parameters can be written to this file. The models written to this file can be retrieved at any time while running the program. The process will generate the required fields:- MODELREF, FIELD, DISTTYPE, NUM.COMP, MEAN1, STD.DEV1, PROP1,.,MEAN8, STD.DEV8, PROP8.  
  
## Example
    
    
    !HISFIT    &IN(BHOLES.D), &MODELOU(HISMODEL)  
  
---  
  
## Error and Warning Messages

Message |  Description  
---|---  
*** Error - Input file does not exist. *** |  Fatal: the process is exited  
*** Error - Input file missing numeric explicit fields.*** |  Fatal: the process is exited  
  
Mathematical Algorithm

The algorithm used for the multi-modal distribution fitting in process **HISFIT** is a non-linear least-squares formulation. Details of this algorithm can be found in the following papers:-

Clark, I., 1977, ROKE, a computer program for nonlinear least-squares decomposition of mixtures of distributions: Computers and Geosciences, v. 3, no. 2, p. 245-249.

McCammon, R.B., 1969, FORTRAN IV program for nonlinear estimation: Kansas Geol. Survey Computer Contr. 34, 20 p

Related topics and activities

  * [HISTOG Process](<histog.md>)