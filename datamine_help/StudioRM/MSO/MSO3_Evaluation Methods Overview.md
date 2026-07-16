![](../Images/HeaderCell.gif) |  Evaluation Methods An explanation of High and Low-Precision evaluations  
---|---  
  
# MSO Evaluation Methods

The stope-shape annealing procedure incrementally improves the value of the stope-shape. This can require thousands of iterations, and the adjusted stope must be evaluated against the block model repeatedly. This is a relatively time consuming analysis to embed in an optimisation procedure.

Two methods of evaluation are available:

Exact Evaluation

This is the method used traditionally in mine planning software where an exact geometric (or Boolean) intersection of cells overlapping with the stope wireframe is made. This is termed wireframe-cell-evaluation (and has been labelled "Exact" or "Precise" in various contexts).

The method is actually the more conservative evaluation method as it evaluates only the proportion of the cell within the wireframe surface used. Accuracy depends on the sub-celling detail as the evaluation method cuts the corners off cells that lay outside of the wireframe surface (hence understates metal inventory) and can also include additional wedges of rock with no grade from the absent cell portions inside the wireframe surface, as depicted in Figure 4-3

Approximate Evaluation

A faster method designed for (discretised) sub-cell block models has been implemented using ray-tracing techniques. This is termed cell-centreline-evaluation (and has been labelled "Approximate" or "Fast" in various contexts). Note that the results are not indicative of the name used (Approximate) but rather of the volume calculation technique applied.

The method uses a ray-trace through the sub-cell centroid (along the Model Discretisation Plane W-axis) to intersect the wireframe shape, and calculate the portion of the sub-cell (from the trace) that falls within the wireframe shape.

For Datamine Studio block models, the cell-centreline method is used in the TRIFIL process to create sub-cell models within a wireframe. Using the same cell-centreline for evaluation of stope wireframes means that the sub-cell approximations are common between the original model creation procedure and the stope evaluation technique in SOO. Hence geometric errors are minimised. This is less the case if model cells are split in the discretisation process. Where smaller sub-cells are used at the wireframe boundary, the better the approximate method becomes at replicating the wireframe shape for the case of sharp grade boundaries.

Comparing Results from Exact and Approximate Evaluation

The results from the faster approximate method can be different from the results obtained by the exact method, and these differences are summarised for each stope output in the log file, reporting the percentage difference in tonnes, grade/value and metal/accumulation calculated between the two methods.

The volumes and tonnes for the approximate and exact methods are identical for a constant model density (with small differences for variable density), but the contained value or contained metal may be different. The differences can all be attributed to the sub-cell approximations used in block modelling of 3D surfaces and shapes (volumes).

Both methods of evaluation are made available, but the runtimes can increase by a factor of 5-10 for the exact method. The run-times for the "approximate" method will also be slower for the case when the rotation angles for the block model and stope-shape framework are different (due to the additional geometry calculations required). Note also that increasing the number of sub-cells will reduce the sampling error at boundaries, but this will be at the cost of significantly increasing the processing time taken.

Interaction of Evaluation Methods with Reporting

While two methods are available for evaluation and annealing, three methods are available for reporting.

  1. Exact Evaluation - Exact Reporting  
Uses the Exact method for wireframe evaluation, and the same results for reporting
  2. Approximate Evaluation - Approximate Reporting  
Uses the Approximate method for wireframe evaluation, and the same results for reporting
  3. Approximate Evaluation - Exact Reporting

Uses the Approximate method for wireframe evaluation, but re-evaluates the final stope wireframes for reporting with the Exact method.

Note that for marginal stopes, the differences in exact and approximate evaluation may result in a stope becoming sub-economic because the exact evaluation can produce a more conservative result.

Care should be taken to ensure that the default value for the optimisation field is realistic for ore-only block models.

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [MSO3_BlockModels_Guidance](<MSO3_BlockModels_Guidance.md>)  
  
Copyright Datamine Corporate Limited  
JMN 20045_00_EN