# Rotated Models

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

A Rotated Model is one whose axes, and therefore cells, are rotated with respect to the coordinate system. It is particularly useful in the situation where a stratified orebody is dipping and/or plunging. As can be seen from the diagram below the model cells provide a much better fit when the model is rotated.

![](../Images/GE_RotatedModel1.gif)

Fig 1. The Rotated Model Concept

ESTIMA will automatically recognize if the Input Prototype Model is a rotated model. If it is then ESTIMA will inversely translate and rotate the model cell coordinates back into the world system before calculating the grade estimates. It does this by rotating the actual [discretised](<Grade%20Estimation%20Cell%20Discretisation.md>) points immediately prior to estimation. This is an internal operation only - the coordinates of the cells in the Output Model file will be rotated; i.e. they will be the same as the Input Prototype Model.

Because the process rotates the model cells internally, this means that it is necessary to supply all search volumes, anisotropy parameters, [variogram](<Grade%20Estimation%20Variograms.md>) models, coordinates of the Sample Data, etc. in the world coordinate system. In summary, a rotated model must be supplied as the Input Prototype Model. There are no other files, fields or parameters which need to be set.

**Note** : **[Unfolding](<Grade%20Estimation%20Unfolding.md>)** is not permitted for a rotated model. If this combination is selected the process will terminate with an error message.

![](../Images/NextExercise.gif)[Go to the next topic](<Grade%20Estimation%20Unfolding.md>) (Unfolding)