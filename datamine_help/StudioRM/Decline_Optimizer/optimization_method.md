# Decline Optimization Method

To access these controls:

  * Display the [Decline Optimizer](<DeclineOptimizerDialog.md>) screen and select the **Path Control** tab.

Define how a calculated decline path is further optimized in terms of maximum path lengths, deviation from preferred orientations and also introduces the concept of cost reporting.

The following methods can be used for optimization:

  * Minimize Total Path Length

  * Minimize Arc Length

  * Minimize Deviation from Preferred Orientations 

  * Minimize Total Cost 

  * Use a weighted sum of the previous four metrics using the four specified weights

The goal of the individual metrics 1 to 4 above are to minimize path length, minimize the length of curved components of the path, minimize the deviation of the straight sections of the path from the specified preferred orientations, or to minimize the total cost. 

The selection of the weights will be specific to each data set, and need to be selected on a trial and error basis.

Generally using the Minimize Total Path Length option is recommended.

Related topics and activities

  * [Decline Optimizer Introduction](<DeclineOptimizerDialog.md>)