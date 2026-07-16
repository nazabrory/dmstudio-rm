# MANOVA Process

To access this process:

  * Enter "MANOVA" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.
  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **MANOVA** and click **Run**.

  * Sample Analysis ribbon >>Geochemical Processes >> Multiple Analysis of Variance.

See this process in the [Command Table](<../command_help/COMMAND%20TABLE_M.md#MANOVA>).

## Process Overview

Multivariate analysis of variance for an unbalanced and balanced design. It is a more sophisticated technique than the one way analysis of variance ([ANOVA1](<anova1.md>)), in that up to 10 groups can be tested.

**MANOVA** is a procedure for comparing multivariate sample means. As a multivariate procedure, it is used when there are two or more dependent variables, and is typically followed by significance tests involving individual dependent variables separately. 

**MANOVA** Requires an input file that contains up to 10 groups of replicate observations defined by keyfields. Note, a minimum of two compulsory keyfields are required. Absent data values are ignored.

The groups of samples which have been classified on geological, sampling, or analytical criteria are checked against each other using the Fisher F statistic to test the significance of the variance between individual samples and group means. The ratios between group variances are calculated to have a minimum value of 1 (nul hypothesis) where the samples between the groups are considered not to be significantly different from each other. Fisher F values are compared with published results from tables against the relevant degrees of freedom. Calculated F values greater than those given in the tables demonstrate that there are significant differences between the groupings.

The version of **MANOVA** provided by your product is for a balanced or unbalanced design. For example, in a balanced design, samples are present for all groupings and sub-groupings. In an unbalanced design, samples can be absent from their allocated positions ie. when a sample is split into A and B, which in turn are split again into A1, A2 and B1, B2, this is balanced. However if B2 is lost, thus not present in the analysis of variance, then the sampling is unbalanced.

### File Handling

Samples must be sorted on defined keyfields. Using Fisher F Tables, check the two degrees of freedom between the group pairs (**DF1** and **DF2**) and look for the corresponding F value in the table which corresponds to the cross over point. If this value exceeds the **MANOVA** value for a given confidence level then the nul hypothesis does not hold, ie, the sample groupings are significantly different from each other for the defined level of confidence.

The input file (&**IN**) must be sorted on the keyfields which define the sample classification groups, for example, vein, sample location, laboratory and sample split.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Input file, sorted on required keyfields. |  Input |  Yes |  Undefined  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Field for analysis of variance. |  IN |  Yes |  Numeric |  Undefined  
KEY1 |  Keyfield 1 for replicate observations. |  IN |  Yes |  Numeric |  Undefined  
KEY2 |  Keyfield 2. |  IN |  Yes |  Numeric |  Undefined  
KEY3 |  Keyfield 3. |  IN |  No |  Numeric |  Undefined  
KEY4 |  Keyfield 4. |  IN |  No |  Numeric |  Undefined  
KEY5 |  Keyfield 5. |  IN |  No |  Numeric |  Undefined  
KEY6 |  Keyfield 6. |  IN |  No |  Numeric |  Undefined  
KEY7 |  Keyfield 7. |  IN |  No |  Numeric |  Undefined  
KEY8 |  Keyfield 8. |  IN |  No |  Numeric |  Undefined  
KEY9 |  Keyfield 9. |  IN |  No |  Numeric |  Undefined  
KEY10 |  Keyfield 10. |  IN |  No |  Numeric |  Undefined  
  
## Example
    
    
    MANOVA &IN(GEOSAMPS),*VALUE)CU), *KEY1(SAMPID),  
  
---  
      
    
    *KEY2(RAMP), *KEY3(ANAL),@ECHO=1  
      
    
    --------------------------------------------------------------  
      
    
    Source of Variation DF SSQ MSQ Fcalc  
      
    
    --------------------------------------------------------------  
      
    
    Among SAMPID 4 843746. 210936. 2.89  
      
    
    Among RAMP 5 3049798. 609960. 585.54  
      
    
    Among ANAL 10 10417. 1042. --  
      
    
    Total 9  
      
    
    --------------------------------------------------------------  
  
In comparing SAMPID and RAMP, the value of Fisher F (Fcalc) for 4 and 5 degrees of freedom (DF) in published tables is as follows:

6.3 (confidence level of 0.05), 15.5 (confidence level of 0.01) and 51.7 (confidence level of 0.001). As the calculated value of 2.89 does not exceed the published values, the nul hypothesis holds, these groups of samples are not significant.

## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 122 <<< ( fileno.) IN MANOVA |  Value field does not exist  
>>> ERR 122 <<< ( fileno.) IN MANOVA |  Input file not sorted on keyfield (s)  
>>> ERR 122 <<< ( fileno.) IN MANOVA |  Compulsory keyfield not present.  
>>> ERR 122 <<< ( fileno.) IN MANOVA |  Compulsory file, field or parameter missing. Check all file, field and parameter settings.  
  
Related topics and activities

  * [ANOVA1 Process](<anova1.md>)