![](../HeaderCell.jpg) |  Filename, Path and Variable Length Limits Limits for the lengths of filenames, paths, variables and more.  
---|---  
  
# Size Limits Applicable to Various Macro Components

The table below lists the length limits that are applicable to various components that are used in macros:

Macro Component |  Maximum Length (number of characters) |  Notes |  Example Macro Code  
---|---|---|---  
Datamine filename |  20 |  Name must not include spaces |  !COPY &IN(samples),&OUT(soil_samples)  
Substitution variable name |  16 |  Start the variable with '$' and end with '#'. Name must not include spaces |  !LET $INFILE1# = samples  
Substituted substitution variable |  72 |  The maximum length applies to the length of the variable after substitution. in the example on the right, the variable length would be 7. |  -  
System file (path+filename) |  56 |  Use '\' in path names and not '/'. |  !<command> &OUT(samples)  
C:\Database\DMTutorials\Data\VBOP\Datamine\\_srfsamp.dm  
A line of macro code |  80 |  - |  -  
Labels |  16 |  A Label consists of a Label Name and a Macro Command. The label name is preceded by '!' and followed by':' - no spaces in between. Label names are case sensitive. |  !SUB1:REM  
Macro file name (file located in project directory) |  80 |  - |  BlockModelingGeostatsAndGradeEstimation.mac  
Macro file (path+name) located outside project directory |  72 |  - |  C:\Database\DMTutorials\Projects\StudioMacrosTut\ProjFiles/Standard\\_Macro2.mac  
Macro name |  8 |  Name must not include spaces and is case sensitive. |  !START macname1  
Macro name + macro description |  56 |  - |  !START macname1 Macro1 Description  
Variables File description |  68 |  This optional description appears on the |  !SUB1:REM  
Maximum number of substitution variables |  1000 |  - |  -  
Maximum number of labels |  400 |  - |  -  
Maximum depth for nesting subroutines |  16 |  - |  -  
Maximum depth for nesting IFs |  50 |  - |  -  
  
![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Macro Commands](<Studio_3_Macro_Commands.md>)