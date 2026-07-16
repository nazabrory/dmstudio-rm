![](../Images/HeaderCell.gif) |  MSO - Materials Setting up exclusion control for MSO  
---|---  
  
# MSO - Materials

### To access this dialog:

  * Select Materials from the MSO ribbon. At least one [scenario](<MSOv3_Scenarios.md>) must be available for selection.

Fields can be supplied in the block model and coded to indicate areas that might be included within, or excluded from, a user-defined proportion in stopes.

The exclusion control can be used to avoid the creation of stope-shapes within say deleterious-processing material or in poor rock-mass zones as a few examples of its use. The material in the model is flagged with a (numeric or alphanumeric) field and a value.

  * Up to three exclusion fields can be defined for each run.
  * Each exclusion field permits a certain maximum tolerance of inclusion within a stope-shape.
  * An exclusion-distance field can be supplied where stopes must be more than a set distance away.

Using this panel, exclusion control is defined as the maximum fractional proportion of material (by volume) in the stope-shape that is flagged as excluded.

![note.gif \(1017 bytes\)](../Images/note.gif) |  Material selection controls on the Materials tab will display both numeric and alphanumeric attributes.  
---|---  
  
The tolerance for each exclusion field is set independently, and allows for a maximum fractional proportion of the respective exclusion material to be incorporated into the stope-shape. As an example, you may be mining a secondary pillar stope and the shape of the adjacent primary backfilled stopes may bulge into the secondary, so for practical purposes you may allow say up to 5% (0.05 fraction) of backfill material within the secondary stope-shape.

If stope optimization is to be restricted to a specific zone then an inclusion field can be specified. The stope must be wholly or partially be within the inclusion zone, depending on the proportion set.

A model report-exclusion field allows mined out material or voids to be ignored in the stope evaluation.

A mixing field and associated values can be supplied to control mixing of material with different attributes. If a model has multiple ore types then stope-shapes are generated to not allow mixing of the ore types (as designated in the ore type field). No two field values from the list specified can be found in a stope.

  
Field Details:

Exclude Material: specify the attribute (of the input block model) that represents a material to be excluded to a proportion within each stope. Once selected, you will be given the chance to select the following parameters, which determine the specific Material code to be excluded, and the Maximum Allowable % of that material within the generated stope.

A default value can also be set. Defaults will normally be extracted from the currently defined model, but you can set an override default value here if required.

A Material selected for exclusion cannot be selected for inclusion or set as a Stand-Off Material (see below) but can be selected again for exclusion from the report (see further below).

  * Exclude 1 is used to set an upper limit to the proportion of a code value for the field in a stope-shape.

  * Exclude 2 is used to independently set an upper limit to the proportion of a code value for a second field in a stope-shape.

  * Exclude 3 is used to independently set an upper limit to the proportion of a code value for a third field in a stope-shape.

Include Material: as above, but used to set the attribute (of the input block model) that represents a material to be included to a proportion within each stope. This field is used to set a lower limit to the proportion of a code value for the field in a stope-shape (e.g. minimum of resource category 1 that is required to make a stope-shape).

A default value can also be set. Defaults will normally be extracted from the currently defined model, but you can set an override default value here if required.

![](../Images/Warning.gif) |  Beware of setting this value to 1.0 as this requires the stope to be completely contained within the nominated code, and will not take into other included material at the stope boundaries or numeric rounding errors in the evaluation of the stope.  
---|---  
  
Exclusion Distance Material: if a generated stope shape is sub-economic, then MSO will still consider the standing-off option when assessing the model. This field allows you to select an Attribute and Material that can be considered if it falls within a given Stand-Off Distance of the stope, used to set an upper limit to the proportion of a code value for the field in a stope-shape, located at some minimum distance from the shape in the transverse direction (e.g. not to mine within a distance from a filled stope). Note that the exclusion % applies to the stope shape after expansion in the transverse (W) direction by the exclusion distance - so the test is not just whether the stope contains the coded value.

A default value can also be set. Defaults will normally be extracted from the currently defined model, but you can set an override default value here if required.

Exclude Material from Report: using the same Attribute and Material controls as above, this area allows you to to exclude the reporting of a code value for the field in a stoping unit e.g. if the code identifies mined out material or air, or reporting of items such as voids, topography air, or backfill.

A default value can also be set. Defaults will normally be extracted from the currently defined model, but you can set an override default value here if required.

Zone Mixing Configuration: use this area to restrict the occurrence of multiple code values for a field in a stope-shape.

Once enabled, you can select the Attribute (field) containing the code values in question. You can select from any evaluation value contained within the input block model. Note that you cannot select optimization or density fields (as defined on the [Scenarios](<MSOv3_Scenarios.md>) panel).

A mixing field and associated values can be supplied to control mixing of material with different attributes. If a model has multiple ore types then stope-shapes are generated to not allow mixing of the ore types. No two field values from the list specified can be found in a stope. 

To allow some limited mixing the requirement for only one zone is relaxed providing that the dominant zone value exceeds a minimum Zone Mixing Fraction value. A minimum fraction of 1.0 would allow no mixing, and a minimum mixing fraction of 0.9 would allow the remaining coded values to have less than 0.1 of the volume of the sum of all nominated mixing codes in the stope. 

Once a valid attribute has been selected, a Not Mixed Material table will be displayed.

You then supply a list of materials for the selected attribute (2 or more), and stopes can be formed for any individual code value, but not a mixture (e.g. if different lenses have different ore types then the stope-shape cannot mix the different ore types).

Maximum Waste Percentage: define the maximum waste fraction of stope-shapes can be defined (i.e. proportion of rock with mineralization values below specified cut-off included within the stope-shape).

Waste inclusion is defined within MSO as:

(Volume of material inside diluted stope shape below cut-off)  
---  
  
* * *  
  
(volume of diluted stope shape)  
  
A setting of 100% means any waste proportion is acceptable.

It is good practice to:

  * start with a test value of 1.0 and gradually refine this in subsequent runs to monitor the impact.

  * if you have back-fill in the voids located within stope-shapes, then do not associate this material with the the one excluded from reporting (see above) as it should have a density and grade, and effectively be in one of the waste categories (diluted total waste, undiluted waste, total mass within near/far/hangwall/footwall, waste below cutoff for Far/Near/footwall/hangwall)

Results Filter Expression: select this option to enter a filter expression that will ratify material results. Use the Build button to display a simple filter expression builder containing quick access to the available block model and MSO stope optimization system fields. For example, you may only wish to report stope data above a given elevation using a filter "ZSTOPE > 2500" or only report against a specific model domain field.

If a Results Filter Expression is set, you can optionally choose to flag output stope data that fails the filter as being sub-economic.

Anneal Filter Expression: select this option to enter a filter expression to control shape annealing.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [MSO Introduction](<MSOv3_default.md>)   
[MSO Shape Frameworks](<MSO3_Frameworks_Concept.md>)   
[MSO Key Shape Concepts](<MSO3_Shape_Diagram.md>)   
[MSO Slice Method Overview](<MSO3_Slice_Method.md>)