# ENVSEQ Process   
  
To access this process:

  * **Report** ribbon **> > Model Reserves >> MIneable Reserves >> Sequence Envelopes**.
  * View the **[Find Command](<../COMMON/findcommand.md>)** screen, select **ENVSEQ** and click **Run**.
  * Enter "ENVSEQ" into the [Command Line](<../COMMON/Command_Toolbar.md>) and press <ENTER>.

See this process in the [[Command Table](<../command_help/COMMAND%20TABLE_E.md#ENVSEQ>)](<../command_help/_COMMAND%20TABLE_A.md#ACCMLT>).

## Process Overview

Process a block model generated from the [MODENV](<modenv.md>) process and evaluate the economics of mining satellite ore envelopes taking into account development, access and processing requirements to produce an extraction sequence.

The **MODENV** process outputs a grade (or value) model with additional fields * **ENVELOPE** and * **ENVNUM** to define the cell classification and each distinct spatial grouping of mined cells based on the optimization criteria: 

  1. maximum ore tonnes (equivalent to minimum included waste or dilution). If several minimum mining units (MMUs) have the same tonnes, then the MMU with the maximum grade is preferred. 
  2. maximum MMU head grade 
  3. maximum MMU contained metal 
  4. maximum accumulated value, where the supplied field is expressed in currency value eg dollar value. 

In all cases except (4), the supplied field would be a grade (or equivalent grade for polymetallic deposits) that is handled as a density weighted average. 

The **MODENV** process also outputs a &**RESULTS** file which summarizes the envelope statistics for tonnage, grade, value, extent and centre of gravity for each combination of envelope number * **ENVNUM** , cell classification * **ENVELOPE** and * **SHAPZONE**. Only the results for * **ENVELOPE** classification of **TOTAL** are used in the sequencing. 

The mining sequence must take into account development, access and processing requirements. The criteria for ranking the envelope sequence can be selected from the same list of optimization criteria used to generate the MMU envelope, and a different criteria can be used to optimize the sequence. 

The costs of sequential development of any satellite orebody from one that is already included in the extraction sequence are calculated from data in the costs penalty &**COSTS** file. The penalties are a function of the size and relative spatial position of the two MMU envelopes. The file must have a representative number of entries for the field size (**SIZE**), horizontal distance (**HORDIST**), vertical distance (**VERDIST**), and grade/value penalty to interpolate the initial fixed development cost (**PENALTY1**), and the variable haulage/extraction cost (**PENALTY2**). 

The units of **PENALTY1** and **PENALTY2** depend on the optimizing criteria used in the the run of **ENVSEQ** : 

  1. ore tonnes 
  2. grade 
  3. metal content 
  4. accumulated value (eg dollar value) 

For example if **OPTIMISE** =3 (metal content), then **PENALTY1** is the metal equivalent for the fixed cost development corresponding to **HORDIST** and **VERDIST** distances. **PENALTY2** is the metal equivalent per tonne per unit distance for the cost of transporting SIZE units of material over the **HORDIST** and **VERDIST** distances. 

The envelope separation can be measured by centre of gravity (@**DISTMETH** =1), or closest distance between the envelope surfaces (@**DISTMETH** =2). Sufficient values must be included in the &**COSTS** file to allow the penalties to be interpolated for every combination of envelopes. Every combination of the selected values of **SIZE** , **HORDIST** and **VERDIST** must be included in the &**COSTS** file, and the file must be sorted in order of increasing **SIZE** , **HORDIST** and **VERDIST**. The penalty applied to an envelope to determine if it can be mined will take into account the **PENALTY1** to provide access from the prior envelope, and the cumulative haulage/extraction cost (sum of **PENALTY2** values in the sequence). 

An envelope sequence file &**SEQUENCE** is used to predefine sequence relationships between envelopes that the user wants to predefine. Three types of relationships can be defined: 

  1. To specify one or more envelopes that will be developed at the start of the sequence (specify **ENVNUM1** and **SEQTYPE** =1). This option could be used to provide access through multiple shafts. 
  2. To specify that one envelope must be developed from another (specify **ENVNUM1** , **ENVNUM2** and **SEQTYPE** =2) 
  3. To specify that one envelope must be developed from another but allowing other intermediate envelopes (specify ENVNUM1, **ENVNUM2** and **SEQTYPE** =3)

If a &**SEQUENCE** file is not defined the process chooses the envelope that has the highest value based on the defined reference point, after penalties have been applied. If no reference point is defined then the envelope with the highest insitu value is chosen as the starting envelope.  
  
The best mining sequence is reported in the &**OUT** file with pairs of envelope numbers **ENVNUM1** and **ENVNUM2**. The result can be visualized as an inverted tree structure (of parent-child relationships) with any envelope linked back to only one parent envelope. A parent envelope may have more than one child.

## Input Files

Name |  Description |  I/O Status |  Required |  Type  
---|---|---|---|---  
ENVMODEL |  Input model file for evaluation. This will have been created as the output &**ENVMODEL** file by process **MODENV**. It must have the fields **XMORIG** , **YMORIG** , **ZMORIG** , **NX** , **NY** , **NZ** (implicit), **IJK** , **XC** , **YC** and **ZC** (explicit). **XINC** , **YINC** and **ZINC** must exist as either explicit (sub-cells permitted) or implicit (no sub-cells). If it is a Rotated Model then it must also include the fields X0, Y0, Z0, ANGLE1, ANGLE2, ANGLE3, ROTAXIS1, ROTAXIS2, and ROTAXIS3. The file also has the fields ***GRADE, *VALUE, *ENVBEST, *DENSITY, *OPTIMISE, *ENVELOPE** and ***SHAPZONE** if specified. The value in the * **ENVBEST** field depend on the default value of the implicit field * **OPTIMISE** :  1 - (maximize ore tonnes) then the values in the two fields are ore tonnes.  2 - (maximize grade) then the values in the two fields are grade.  3 - (maximize metal) then the values in the two fields are metal content.  4 - (maximize dollars) then the values in the two fields are dollars. |  Input |  Yes |  Block Model  
RESULTS |  Input results summary file to report statistics for each envelope, with fields ***ENVNUM, *ENVELOPE, *SHAPZONE, *GRADE, *VALUE, VOLUME, TONNES, MINX, MAXX, MINY, MAXY, MINZ, MAXZ, COGX, COGY, COGZ**. Each combination of * **ENVELOPE** (and * **SHAPZONE** if supplied) is included by **MODENV** but only those records where * **ENVELOPE** has the value '**TOTAL** ' are used in the sequencing. |  Input |  Yes |  Undefined  
COSTS |  Input file to define the costs associated with alternate sequence combinations. The fields **SIZE** , **HORDIST** , **VERDIST** , **PENALTY1** , **PENALTY2** are required. The file must have all combinations of the discrete values selected for **SIZE** , **HORDIST** and **VERDIST** and be sorted in the same field order. |  Input |  Yes |  Undefined  
SEQUENCE |  Optional input file to define required sequence relationships between envelopes. Three fields **ENVNUM1** , **ENVNUM2** and **SEQTYPE** are required. |  Input |  No |  Undefined  
  
## Output Files

Name |  I/O Status |  Required |  Type |  Description  
---|---|---|---|---  
OUT |  Output |  Yes |  Undefined |  Output sequence summary file, with pairs of sequence relationships in **ENVNUM1** and **ENVNUM2**. The initial envelope value **IVALUE** , the penalty values **PENALTY1** and **PENALTY2** to the previous envelope, and **PENALTY3** for prior envelopes and the final envelope value **FVALUE** are output. This file will also contain the centre of gravity of each envelope, if @**DISTMETH** =1, or the coordinates of the closest points, if @**DISTMETH** =2 stored in the fields (**X1,Y1,Z1**) and (**X2,Y2,Z2**).  
  
## Fields

Name |  Description |  Source |  Required |  Type |  Default  
---|---|---|---|---|---  
GRADE |  Numeric (explicit) field for the grade of input model blocks. |  ENVMODEL |  No |  Numeric |  Undefined  
VALUE |  Numeric (explicit) field for the value of input model blocks. |  ENVMODEL |  No |  Numeric |  Undefined  
SHAPZONE |  Field in the input model to distinguish zones. |  ENVMODEL |  No |  Any |  Undefined  
ENVBEST |  Numeric (explicit) field for the best envelope grade or value in the &ENVMODEL file. |  ENVMODEL |  Yes |  Numeric |  ENVBEST  
ENVELOPE |  Alphanumeric (explicit) field for the cell envelope code in the &ENVMODEL file. |  ENVMODEL |  Yes |  Character |  ENVELOPE  
ENVNUM |  Numeric (explicit) field for the envelope number in the &ENVMODEL file. |  ENVMODEL |  No |  Numeric |  ENVNUM  
DENSITY |  Optional density field in the input model for average grade and tonnage calculations. |  ENVMODEL |  No |  Numeric |  Undefined  
  
## Parameters

Name |  Description |  Required |  Default |  Range |  Values  
---|---|---|---|---|---  
HDGRADE |  Required head grade for economic envelopes. The definition of head grade depends on the value of @**SEQOPT**. An absent value will cause the head grade test to be ignored. |  Yes |  Undefined |  Undefined |  Undefined  
REFZ |  Reference elevation for calculation of penalties for the initial envelope. If a &**SEQUENCE** file is not defined then the reference elevation would normally be the surface elevation. The coordinate system for defining @**REFZ** is the unrotated system used in &**ENVMODEL**. |  No |  Undefined |  Undefined |  Undefined  
REFX |  Reference X coordinate for calculation of penalties for the initial envelope. If a &**SEQUENCE** file is not defined then the reference X coordinate would normally be the Easting of the existing or proposed shaft. The coordinate system for defining @**REFX** is the unrotated system used in &**ENVMODEL**. If the value is set to absent data (the default) then neither the X or Y reference coordinates are used. |  No |  Undefined |  Undefined |  Undefined  
REFY |  Reference Y coordinate for calculation of penalties for the initial envelope. If a &**SEQUENCE** file is not defined then the reference Y coordinate would normally be the Easting of the existing or proposed shaft. The coordinate system for defining @**REFY** is the unrotated system used in &**ENVMODEL**. If the value is set to absent data (the default) then neither the X or Y reference coordinates are used. |  No |  Undefined |  Undefined |  Undefined  
SEQOPT |  Method to be used for ranking the envelope sequence: 0 - Use the same method used for optimizing the &**ENVMODEL** model. This is recorded as the default value of implicit field **OPTIMISE** in file &**ENVMODEL**.  1 - Maximize ore tonnes ie minimize [below cutoff] waste.  2 - Maximize grade  3 - Maximize contained metal  4 - Maximize accumulated value ie for dollar value. |  No |  0 |  0,4 |  0,1,2,3,4  
DISTMETH |  Method for defining the envelope separation: 1 - measured by centre of gravity 2 - measured as the closest distance between the envelope surfaces. |  Yes |  1 |  1,2 |  1,2  
  
## Example
    
    
    !ENVSEQ &ENVMODEL(envmod3),&RESULTS(results3),&COSTS(costs2),  
  
---  
      
    
    &OUT(seq1),*GRADE(NI1),*ENVGRADE(GRADE),*ENVELOPE(ENVELOPE),  
      
    
    *ENVNUM(ENVNUM),@HDGRADE=1.2,@REFZ=0.0,@REFX=0.0,  
      
    
    @REFY=0.0,@SEQOPT=0.0,@DISTMETH=1.0  
  
Related topics and activities

  * [MODENV Process](<modenv.md>)