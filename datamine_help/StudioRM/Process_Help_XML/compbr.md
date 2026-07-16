# COMPBR Process  
  
To access this process:

  * **Sample Analysis** ribbon **> > Prepare Samples >> Composite >> Composite With Recovery**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **COMPBR** and click **Run**.
  * Enter "COMPBR" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [Command Table](<../command_help/_COMMAND%20TABLE_C.md#COMPBR>).

## Process Overview

Composites drillhole data over horizontal benches, with additional computation of a recovered grade and recovered fraction for a specified field at a given cut-off.

The **COMPBR** process is a modification of the [COMPBE](<compbe.md>) process, and composites in an identical way. The difference comes in the recovered grade and fraction calculations. For the specified field * **VALUE** , the weighted **FRACTION** of each composite above the given parameter @**CUTOFF** is computed, together with the mean grade **REC.VAL** of this fraction. These values relate to those that could be achieved with selective mining within benches at the specified cut-off.

Further details of the compositing process are given in the [COMPBE](<compbe.md>) description.

The file must be in the order of **BHID** and **FROM** (sorted in drillhole order in increasing downhole distance). This is the order output from the [DESURV](<desurv.md>) process.

Note: A progress message is displayed for every 500 samples read.

### Weighting by density

If a density field exists in the file then this may be used too for density weighted compositing. The density field is defined as the optional field *DENSITY. If any density value is absent data then the default density value will be used.

### Weighting by core loss or recovery

To include the effects of core loss, the user may specify one of two optional fields * **CORELOSS** (core loss as a percentage) or * **COREREC** (core recovery as a percentage) to be used during compositing. The lost portion of the core will be taken into account and used in compositing. The actual treatment depends on the optional @**LOSS** parameter. If @**LOSS** <=0 (default) then the lost part of the core will be assumed to have exactly the same grades, properties etc. as the recovered part; in other words, the core loss is ignored. If however @**LOSS** = 1 then the lost core will be assumed to have default grades, density, properties etc. which will be averaged with the recovered core values.

If @LOSS>=2 then the lost core will be treated as cavity (zero density and grades) so that the grade of the total sample is effectively reduced by the cavity.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
IN |  Sample data file, sorted on BHID and FROM. Expects fields BHID, FROM, TO, LENGTH, X, Y, Z, A0, B0. |  Input |  Yes |  Drillhole  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Drillhole |  Composite file. Will include implicit field CUTOFF and explicit fields REC.VAL and FRACTION for recovered values.  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
VALUE |  Field for recovered grade computations. |  IN |  Yes |  Numeric |  Undefined  
BHID |  Drillhole identifier. |  IN |  No |  Any |  BHID  
FROM |  Downhole distance to sample top. |  IN |  No |  Numeric |  FROM  
TO |  Downhole distance to sample bottom. |  IN |  No |  Numeric |  TO  
DENSITY |  If present, composites will be density-weighted |  IN |  No |  Numeric |  DENSITY  
CORELOSS |  If present, will be taken as percentage core loss, and treated according to the LOSS parameter. |  IN |  No |  Numeric |  CORELOSS  
COREREC |  If present, will be taken as percentage core recovery, (100-core loss) and treated according to the LOSS parameter. |  IN |  No |  Numeric |  COREREC  
ZONE |  Name of field for compositing within. (may be numeric or up to 4 character alpha). This field must exist in the IN and will be copied to the OUT file. If specified then new composites will be created each time the value of ZONE changes. |  IN |  No |  Any |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
INTERVAL |  Bench height. |  Yes |  Undefined |  Undefined |  Undefined  
CUTOFF |  Cutoff to be applied to VALUE. |  Yes |  Undefined |  Undefined |  Undefined  
MINGAP |  Gap length to be ignored. The default gap is calculated as 0.05 INTERVAL. This default value is applied if the parameter is not specified, or if the value is specified as <=0. A gap of exactly zero is not permitted. If you want the composite to be split at every gap, use a very small value for MAXGAP eg 0.0001. |  No |  Undefined |  Undefined |  Undefined  
MAXGAP |  Gap length for termination of composite (0). |  No |  0 |  Undefined |  Undefined  
ELEV |  Reference bench elevation (0). |  No |  0 |  Undefined |  Undefined  
MINCOMP |  Minimum composite length [0.5 INTERVAL]. |  No |  Undefined |  Undefined |  Undefined  
MAXCOMP |  Maximum composite length [2.0 INTERVAL]. |  No |  Undefined |  Undefined |  Undefined  
LOSS |  If core loss or core recovery field is present, controls how it is handled: |  Option |  Description  
---|---  
0 |  Treat loss as part of sample.  
1 |  Treat loss as default values.  
2 |  Treat as cavity [zero density and grades]  
No |  0 |  0,2 |  0,1,2  
PRINT |  >2 to display each composite and output file DD (0). |  No |  0 |  0,2 |  0,1,2  
  
## Example
    
    
    !COMPBR &IN(BHOLES.D), &OUT(COMPSR.4), @INTERVAL=4,   
  
---  
      
    
             @ELEV=35,  
      
    
    @CUTOFF=0.5, *VALUE(CU)  
      
    
       
      
    
    >>> 170 SAMPLES INPUT <<<  
      
    
    >>> 67 COMPOSITES OUTPUT <<<  
  
## Error and Warning Messages

Message |  Description  
---|---  
>>> ERR 122 <<< ( fileno) IN COMPBR |  Missing essential fields in input sample file or there are more than 20 explicit numeric data fields for compositing. Fatal; the process is exited.  
>>> ERR 124 <<< ( fileno) IN COMPBR |  The composite length specified in @**INTERVAL** is negative or zero. Fatal; the process is exited.  
>>> ERR 130 <<< ( 0) IN COMPBR |  The maximum acceptable composite length specified in @**MAXCOMP** is less than the required composite length specified in @**INTERVAL**. Fatal; the process is exited.  
>>> ERR 131 <<< ( 0) IN COMPBR |  The maximum acceptable composite length specified in @**MAXCOMP** is less than the minimum acceptable composite length specified in @**MINCOMP**. Fatal; the process is exited.