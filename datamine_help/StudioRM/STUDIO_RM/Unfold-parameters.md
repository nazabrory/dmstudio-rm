# UNFOLD Parameters

**UNFOLD** is a grade estimation technique where folded orebodies are unfolded to reduce structural complexity. When an orebody is folded in the world coordinate space (WCS), spatial relationships are reduced which means that traditional linear estimation techniques may not do a good job at grade estimation (because mineralization occurred before the rock was folded).

An unfolding parameter file contains a single line of parameters for unfolding which is used by all estimates, which describe the unfolding transform applied to strings and samples. These parameters are required by other processes in order to unfold the block model and discretization points during a grade estimation.

  * **UNFOLD** in Advanced Estimation has been added to the [**Advanced Estimation**](<Multivariate_Introduction.md>) workflow as well as to the underlying process **[COKRIG](<../Process_Help_XML/cokrig.md>)**. The **Advanced Estimation** console can also be used to export an in-use unfolding parameters file.

See [UNFOLD in Advanced Estimation](<Unfold-advanced-estimation.md>).

  * **UNFOLD** parameters can also be input to the **ESTIMATE** wizard (powered by the **ESTIMA** process) for univariate estimation.

Typically, the unfolding parameters file is created initially by the **Unfold Wizard** , via the **User Files & Current Section** controls:

![](../Images_STUDIORM_ONLY/Unfold-parameters.png)   
_The Unfold Wizard's parameter file export function_

When this parameter file is used in **Advanced Estimation** or set as an input in **COKRIG** , unfolding is applied to all estimates in a run. It is not possible for some estimates to be unfolded while others are not in a single run of **COKRIG**. Put another way, it is not possible to execute a mixture of estimates in the world coordinate space (WCS) and unfolded coordinate space (UCS).

An _Unfolding parameter file_ contains the following compulsory fields:

Field Name | Type | Description  
---|---|---  
SAMPLE | A24 | Name of unfolded sample file. This name is used to set the sample value in the user interface. When running **COKRIG** , the value of &**SAMPLE** overrides this value if different.   
STRING | A24 | Name of string file e.g. str09_hwfe_valid. When running **COKRIG** , the value of &**STRING** overrides this value if different.  
SECTION | A24 | Section identifier field, for example, SECTION  
BOUNDARY |  | Boundary HW/FW field ID, for example, BOUNDARY  
WSTAG | A24 | Within section tag field, for example, WSTAG  
BSTAG | A24 | Between section tag field, for example, BSTAG  
LINKMODE | N | Method by which within and between section tags are defined, for example, 3  
UCSAMODE | N | Define coordinate adjustment in X , for example, 2 Adjusted  
UCSBMODE | N | Define coordinate adjustment in Y, for example, 3 True length  
UCSCMODE | N | Define coordinate adjustment in Z, for example, 2 Adjusted  
PLANE | N | Orientations of interpretation as vertical section (1) or plane (2)  
HANGID | N | Hangingwall string ID in BOUNDARY, for example, 1  
FOOTID | N | Footwall string ID in BOUNDARY, for example,. 2  
TOLRNC | N | Tolerance in the calculation of the UCSA, for example, 0  
UCSALIMT | N | Limits of UCSA, for example, 1  
ORGTAG | A24 | Tag number or origin, for example, 10001  
  
If an unfolding parameter file is selected and applied using the **Scenario Setup** screen of the **Unfold Wizard** , it will populate **Select Samples and Unfolding** with the parameters in the file. See Using Unfold in Advanced Estimation for more details.

An Unfolding parameters file may also be used when running **UNFOLD** from the **COKRIG**.

Related topics and activities

  * [UNFOLD Wizard](<UnfoldWizard.md>)

  * [UNFOLD in Advanced Estimation](<Unfold-advanced-estimation.md>)

  * [Unfolded Variograms & Search Parameters](<Unfold-Variograms-Search.md>)

  * [Advanced Estimation & Variography](<Multivariate_Introduction.md>)