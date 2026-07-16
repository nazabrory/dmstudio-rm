# COMPDH Process  
  
To access this process:

  * **Sample Analysis** ribbon **> > Prepare Samples >> Composite**.
  * **Sample Analysis** ribbon **> > Prepare Samples >> Composite >> Composite Down Drillholes**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **COMPDH** and click **Run**.
  * Enter "COMPDH" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#COMPDH>).

## Process Overview

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

## Input Files

Name| I/O Status| Required| Type| Description  
---|---|---|---|---  
**IN**|  Input| Yes| Drillhole| Sample data file, sorted on **BHID** and **FROM**. Expects fields **BHID** , **FROM** , **TO** , **LENGTH** , **X** , **Y** , **Z** , **A0** , **B0**.  
  
## Output Files

Name| I/O Status| Required| Type| Description  
---|---|---|---|---  
OUT| Output| Yes| Drillhole| Composite file.  
RESIDUAL| Output | No| Drillhole| Residual composites file.  
  
## Fields

Name| Description| Source| Required| Type| Default  
---|---|---|---|---|---  
BHID| Drillhole identifier.| IN| No| Any| BHID  
FROM| Downhole distance to sample top.| IN| No| Numeric| FROM  
TO| Downhole distance to sample bottom.| IN| No| Numeric| TO  
DENSITY| If present, composites will be density- weighted.| IN| No| Numeric| DENSITY  
CORELOSS| If present, will be taken as percentage core loss, and treated according to the **LOSS** parameter.| IN| No| Numeric| CORELOSS  
COREREC| If present, will be taken as percentage core recovery, (100-core loss) and treated according to the **LOSS** parameter.| IN| No| Numeric| COREREC  
ZONE(N)| Name of a field for compositing within. (may be numeric or up to 32 character alpha). This field must exist in the IN and will be copied to the **OUT** file. If specified then new composites will be created each time the value of **ZONE** changes.Up to 5 zones can be specified (**ZONE** to **ZONE5**).| IN| No| Any| Undefined  
DOM1-5|  Name of a dominant field. If specified, this field is copied to the output file, containing the value that appears most frequently (by total length) within each sample. The field must exist in the IN file and can be numeric or up to 32 character alpha.Up to 5 dominant fields can be specified.| IN| No| Any| Undefined  
  
## Parameters

Name| Description| Required| Default| Range| Values  
---|---|---|---|---|---  
INTERVAL| Composite length.| Yes| Undefined| Undefined| Undefined  
MINGAP| Gap length to be ignored. The default gap is calculated as 0.05 **INTERVAL**. This default value is applied if the parameter is not specified, or if the value is specified as <=0. A gap of exactly zero is not permitted. If you want the composite to be split at every gap, use a very small value for **MAXGAP** eg 0.0001.| No| Undefined| Undefined| Undefined  
MAXGAP| Gap length for termination of composite (0).| No| 0| Undefined| Undefined  
MINCOMP| Minimum composite length [0.5 **INTERVAL**].| No| Undefined| Undefined| Undefined  
LOSS| If core loss or core recovery field is present, controls how it is handled: <=0 treat loss as part of sample =1 treat loss as default values >=2 treat as cavity [zero density and grades]| No| Undefined| Undefined| Undefined  
DOMPROPN| The minimum proportion of the total length of a composite that must share the same dominant value before that value is recorded. A value between 0 and 1. See Dominant Values.|  |  |  |   
START| Starting distance down hole (0).| No| 0| Undefined| Undefined  
MODE| If **MODE** is 0, the default, then the maximum composite length will be defined by the **INTERVAL** parameter and the minimum composite length by the **MINCOMP** parameter. Thus it is possible for part or all of one or more samples to be excluded from the composite. Setting **MODE** to 1 forces all samples to be included in one of the composites by adjusting the composite length, while keeping it as close as possible to **INTERVAL**. The maximum possible composite length will then be 1.5* **INTERVAL**. (0)If **MODE** is 2, excluded samples are those whose length falls outside the allowable range set by [@**INTERVAL** \- @**RESLEN**] and [@**INTERVAL** \+ @**RESLEN**]. These samples appear in &**RESIDUAL**.| No| 0| 0,1| 0,1  
DENSITY| Default density value of samples. This is used if no **DENSITY** field exists or if the **DENSITY** field contains absent values. If this is unset then the default **DENSITY** in the input file data definition is used as the default.| No| Undefined| Undefined| Undefined  
REVERSE|  Reverse compositing direction. Control whether compositing is done from collar to toe (default) or toe to collar. 0 : Composite samples starting at the collar. This is the default. 1 : Composite samples from the toe to the collar. | No| 0| 0,1| 0,1  
PRINT| =3 to display each composite and output file DD (0).| No| 0| 0,3| 0,1,2,3  
  
## Examples
    
    
    !COMPDH &IN(.D), &OUT(COMPS.4),   
  
---  
      
    
             @INTERVAL=4  
      
    
       
      
    
    >>> 170 SAMPLES   
      
    
     INPUT <<<>>> 67 COMPOSITES OUTPUT <<<  
      
    
       
      
    
    !COMPDH &IN(BHOLES.D),   
      
    
             &OUT(SEAM.1), @INTERVAL=999999, @MINCOMP= 1, SEAM= 1  
      
    
       
      
    
    >>> 345 SAMPLES INPUT   
      
    
     <<<  
      
    
    >>> 42 COMPOSITES OUTPUT <<<  
  
Here the interval is set to be very large to force compositing over the entire seam, selected as the value of field "SEAM"=1 in the input file. The minimum composite length is set to 1, the minimum mining width.

## Error and Warning Messages

Message| Description  
---|---  
>>> ERR 122 <<< ( fileno) IN COMPDH| Missing essential fields in input sample file or there are more than 20 explicit numeric data fields for compositing. Fatal; the process is exited.  
>>> ERR 124 <<< ( fileno) IN COMPDH | The composite length specified in @INTERVAL is negative or zero. Fatal; the process is exited.