![](../Images/HeaderCell.gif) |  MSO - Preanneal Reducing the dependence on stope control surfaces  
---|---  
  
# "Preannealing"

Traditionally the generation of optimized stope shapes is directly dependent to the formation of seed-shapes (the combination of seed-slices that meet cut-off and minimum mining width). 

"Preanneal" is an alternative seed optimization method developed to minimize the reliance on a stope control surface(s) to generate seed-shapes. 

Preanneal works by using slices to identify potential seed-shapes, runs a first pass fast-anneal process to produce seed-shapes that are close to the optimum stope shape, and then passes the seed-shapes through a pillar testing routine. Seed-shapes that do not meet the pillar test are re-tested to see if they should be combined, adjusted or dropped to optimize the outcome. 

Activating preanneal has generally proved successful in finding more shapes that are of marginal value and is less dependent on the stope control surface. 

A general rule-of-thumb for returning more stope shapes (with either a higher optimization value if you have selected to optimize metal above cutoff or more metal if maximizing total metal) by increasing order of value is:

  1. Anneal without a stope control surface (default dip and strike settings) 

  2. Anneal with a stope control surface 

  3. Preanneal without a stope control surface 

  4. Preanneal with a stope control surface 

Substope Optimization 

Preanneal for sub-stope optimization works differently to the anneal method. 

Sub-stope optimization produces a list of different sub-stope shape definitions (i.e. size and position within a quad and/or cut-off factor) that are tested for each quad. 

For anneal sub-stope optimization, the singular shape definition that returns the highest optimization value for the quad is output. So, for any quad which may contain two or more stope shapes (i.e. in the case of parallel lodes or multiple stopes separated by waste pillar/s) they would all have the same sub-shape definition. 

For preanneal sub-stope optimization, it is possible that each quad can return a mix of sub-shapes definitions. For example if the list of sub-shape definitions included a three-quarter shape, a half-shape and a quarter-shape, the anneal method may return two half-shapes whereas the preanneal method may return one three-quarter shape, one half-shape and one quarter shape. 

Preanneal is not currently configured to work with the Polytube method. 

![openbook.gif \(910 bytes\)](../Images/openbook.gif) |  Related Topics  
---|---  
| [Stope Shape Selection Wizard](<MSO3_Shape_Stope_Generation_Settings.md>)[Shape Framework Settings](<MSO3_Shape_Shape_Framework_Settings.md>)[Standard Slice Framework Settings](<MSO3_Shape_Framework_Settings_Standard.md>)[Advanced Slice Framework Settings](<MSO3_Shape_Framework_Settings_Advanced.md>)[Prism Framework Settings](<MSO3_Shape_Framework_Settings_Prism.md>)[Boundary Surface Framework Settings](<MSO4_Boundary_Surface_Method.md>)