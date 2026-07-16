# Key fields

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

If each record in the sample data file is identified by a key field, then the number of samples per key field value can be restricted. The most obvious use of this feature is to prevent samples from a single hole having an overpowering influence on the estimated grade of a cell. In the following example the key field is defined as BHID. The name of the key field is specified as field KEY (i.e. * **KEY(BHID**)). The maximum number of samples with the same key field value is defined using field **MAXKEY** in the Search Volume Parameter file. If MAXKEY is set to absent data or zero, then the key field option is not be used.

If [octant](<Grade%20Estimation%20Octants.md>) search is selected then the MAXKEY parameter applies to the number of samples within an octant.

![](../Images/NextExercise.gif)[Go to the next topic](<Advanced%20Estimation%20Validation.md>) (Search Volume Parameter file table)