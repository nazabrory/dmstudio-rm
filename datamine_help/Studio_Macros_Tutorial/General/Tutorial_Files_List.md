![](../HeaderCell.jpg) |  Tutorial Files A list of files used throughout the Macros tutorial.  
---|---  
  
# File Locations

Assuming that a default installation has been performed, all Datamine (*.dm) files referenced by this tutorial can be found under:

  * C:\Database\DMTutorials\Data\VBOP\Datamine\

Providing the example macro and script files have been manually copied to a top-level folder as described here, the macro (*.mac) and script (*.htm) files referenced by this tutorial can be found under:

  * C:\Macros\

# File Names and Descriptions

The following table contains a list of the relevant files used in this tutorial. Each entry lists the existing Sample File Name, the suggested User File Name and a file Description. They are grouped according to the name of the folder in which the files are located.

Sample File Name |  **User File Name** |  **Description**  
---|---|---  
...\Data\VBOP\Docs:  
- |  - |   
...\Data\VBOP\Datamine:  
_srfsamp |  - |  Points Soil sampling (grades: Au [ppb], Cu [ppm]; Z - elevation)  
_include |  formulae |  Table - contains EXTRA formulae lines for use with the INCLUDE command example  
C:\Macros\  
_Macro1a.mac |  Macro1a.mac |  Recorded macro (1/3) containing processes STATS and PROTOM  
_Macro1b.mac |  Macro1b.mac |  Recorded macro (2/3) containing processes GRADE and LIST  
_Macro1c.mac |  Macro1c.mac |  Recorded macro (3/3) containing the process DEL  
_Macro2.mac |  Macro2.mac |  Multiple macros (macros 1, 2 and 3) in a single macro file  
_Macro3.mac |  Macro3.mac |  _Macro2.mac with Comments  
_Macro4.mac |  Macro4.mac |  _Macro3.mac with individual macros replaced by subroutines  
_Macro5.mac |  Macro5.mac |  _Macro4.mac with modified cleanup subroutine  
_Macro6a.mac |  Macro6a.mac |  _Macro5.mac with variable definition section  
_Macro6b.mac |  Macro6b.mac |  _Macro6b.mac with variable loading and saving sections  
_Macro7.mac |  Macro7.mac |  _Macro6b.mac with prompt section  
_Macro8a.mac |  Macro8a.mac |  _Macro7.mac with a blocked conditional statement  
_Macro8b.mac |  Macro8b.mac |  _Macro8a.mac with a simple conditional statement  
_Macro9.mac |  Macro9.mac |  _Macro8b.mac with messages  
_Macro10.mac |  Macro10.mac |  _Macro9.mac with data accessing section using FILE and FIELD  
_Macro11.mac |  Macro11.mac |  _Macro10.mac with a loop structure  
_Macro12.mac |  Macro12.mac |  _Macro11.mac with an error trap  
_Macro13.mac |  Macro13.mac |  _Macro12.mac with SCROFF text diversion  
_Macro14.mac |  Macro14.mac |  _Macro13.mac with character manipulation  
_Macro15.mac |  Macro15.mac |  _Macro14.mac with environment variables  
_Macro16.mac |  - |  Macro containing process EXTRA used to create a field ANOM (anomaly) in the samples file  
_Macro17.mac |  Macro17.mac |  _Macro16.mac with an INCLUDE command replacing lines of EXTRA code  
- |  Macro18.mac |  Copy of _Macro16.mac for use by _Run_Macro18.htm  
_Macro19.mac |  Macro19.mac |  _Macro15.mac with an OPSYS command and Command Prompt commands  
_Run_Macro18.htm |  - |  Example script to run the macro file Macro18.mac (a local copy of _Macro15.mac)  
  
![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Tutorial Exercises List](<../Exercises/Tutorial_Exercise_List.md>)