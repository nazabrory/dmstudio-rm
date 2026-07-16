# Unfolding

The estimation methods of [Nearest Neighbor](<Grade%20Estimation%20Nearest%20Neighbour.md>), [Inverse Power of Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>) and [Kriging](<Grade%20Estimation%20Kriging.md>) all involve calculating the distance between each sample and either the centre of the cell or the discretisation points. These measurements are usually made in the standard Cartesian XYZ coordinate system.

However, for a folded deposit, where mineralization has occurred pre-folding, a line measured in the pre-folded orebody is required.

![](../Images/GE_Folded.gif)

The problem is illustrated by the simple example above, which shows two samples either side of an anticline. Using the XYZ coordinate system, the standard geometrical distance between A and B is a straight line. However, from a geological point of view the distance separating them is a line following the anticline structure, shown as a broken line in the diagram. This is the distance between samples prior to folding.

The unfolding method allows the sample coordinates and model cells to be transformed into the original unfolded system, grade estimation is carried out in the unfolded system, and then

Convert back to the folded system for reserve evaluation and planning. There is a description in a paper by Dr. M.J.Newton, referenced in [Grade Estimation References](<Grade%20Estimation%20References.md>).

The UNFOLD process must be used prior to grade estimation to calculate the unfolded coordinates of sample data. This file should then be input to ESTIMA as the Sample Data file. All search volumes, anisotropy parameters, variogram models, etc must be specified in the unfolded system. The only exception to this is the Input Prototype Model, which is in the world (i.e. folded) coordinate system. The way ESTIMA works is to unfold the discretisation points so that the estimation is carried out in the unfolded system. The estimated grade and any secondary variables are then assigned back to the corresponding cell in the folded model. The unfolding option is selected by specifying the optional String file. This must contain the string data describing the hangingwall and footwall outlines on two or more sections. It is also necessary to specify the unfolding parameters and fields.

**Note** : Unfolding is not permitted for a [rotated model](<Grade%20Estimation%20Rotated%20Models.md>). If this combination is selected then the process will terminate with an error message.

![](../Images/NextExercise.gif)[Go to the next topic](<Grade%20Estimation%20Output%20and%20Results.md>) (Outputs and results)