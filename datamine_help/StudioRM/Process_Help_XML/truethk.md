# TRUETHK Process  
  
To access this process:

  * **Sample Analysis** ribbon **> > Prepare Samples >> True Thickness**.

  * Enter "TRUETHK" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **TRUETHK** and click **Run**.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_T.md#TRUETHK>).

## Process Overview

**Note** : This is a _superprocess_ and running it may have an effect on other Datamine files in the project.

For tabular ore bodies, based on a set of static drillhole sample data, composites are commonly created across the defined ore boundaries.

These composites can be defined by either lithological codes, or by selection and assignment of codes based on physically defined limits perimeters and/or wireframes. For subsequent analysis and reserve evaluation, a common requirement is the true width of each ore composite. 

Sometimes, the horizontal and/or vertical thicknesses are also required. The **TRUETHK** process calculates these true thickness values, based on the supplied sample lengths and orientations, and the supplied ore body dip and dip direction across which the samples have been taken.

The input file to the process is a standard desurveyed sample file, which must contain at least the fields **LENGTH** , **A0** and **B0**. Compulsory input parameters are the ore body dip and dip direction. The output file created will essentially be a copy of the input sample file, but with the additional fields **TRUETHK** , **VERTHK** , **HORTHK** and **TRUEDIP**.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Sample/composite data file. |  Input |  Yes |  Sample Data  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Sample data |  Sample/composite data with calculated true, vertical and horizontal thickness fields.  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
DIP |  Ore body dip value. |  Yes |  0 |  0,90 |   
DIPDIRN |  Ore body dip direction. |  Yes |  0 |  0,360 |   
  
## Example
    
    
    !TRUETHK  &IN(file1),   
  
---  
      
    
     &OUT(file2), @DIP=25, @DIPDIRN=300