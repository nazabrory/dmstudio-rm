![](../HeaderCell.jpg) |  Grade Estimation - Key Fields How key fields are used in grade estimation  
---|---  
  
# Key fields

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

If each record in the sample data file is identified by a key field, then the number of samples per key field value can be restricted. The most obvious use of this feature is to prevent samples from a single hole having an overpowering influence on the estimated grade of a cell. In the following example the key field is defined as BHID. The name of the key field is specified as field KEY (i.e. *KEY(BHID)). The maximum number of samples with the same key field value is defined using field MAXKEY in the Search Volume Parameter file. If MAXKEY is set to absent data or zero, then the key field option is not be used.

If [octant](<Grade%20Estimation%20Octants.md>) search is selected then the MAXKEY parameter applies to the number of samples within an octant.

![](../Images/NextExercise.gif)[Proceed to the next section](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>) (Search Volume Parameter file table)

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
|  [Introducing the Grade Estimation User Guide](<Grade%20Estimate%20Overview.md>)[  
Grade Estimation Search Volume Introduction](<Grade%20Estimation%20Search%20Volume%20Introduction.md>)[  
Grade Estimation Dynamic Search Volumes](<Grade%20Estimation%20Dynamic%20Search%20Volumes.md>)[  
Grade Estimation Octants](<Grade%20Estimation%20Octants.md>)[  
Grade Estimation Search Volume Parameter File](<Grade%20Estimation%20Search%20Volume%20Parameter%20File.md>)[  
Grade Estimation Cell Discretisation](<Grade%20Estimation%20Cell%20Discretisation.md>)[  
Grade Estimation Methods](<Grade%20Estimation%20Methods.md>)[  
Grade Estimation Parameter File](<Grade%20Estimation%20Parameter%20File.md>)[  
Grade Estimation Additional Features  
Grade Estimation Variograms  
Grade Estimation Run Time Optimization  
Grade Estimation Rotated Models  
Grade Estimation Output and Results  
Grade Estimation Parameter Summary  
Grade Estimation System Limits](<Grade%20Estimation%20Additional%20Features.md>)[  
Grade Estimation References  
  
ESTIMA command Help   
ESTIMATE command Help  
The Estimate dialog  
VARFIT Command Help](<Grade%20Estimation%20References.md>)