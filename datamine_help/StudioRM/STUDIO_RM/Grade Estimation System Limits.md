# System Limits

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

There is no restriction on the number of records in either the Sample Data file or the Input Prototype Model file. However, there are certain restrictions on some variables.

## Number of Zones

There is a limit of 100 on the maximum number of zone combinations in the Sample Data file or the Input Prototype Model files. In only one zone field is defined then this means a maximum of 100 different zones. If there are two zone fields this means 100 unique combinations of zone 1 and zone 2.

## Length of Zone Field

If a zone field is alphanumeric it must be less than or equal to 20 characters (5 words).

## Grade Fields

The maximum number of different grades defined by the VALUE_IN field in the [Estimation Parameter file](<Grade%20Estimation%20Parameter%20File.md>) is 31. There can be more than 31 records in the Estimation Parameter file so long as some of the grade values are the same e.g. different parameters for the same grade field in different zones. There is also a limit of 31 on the number of VALUE_OU fields in the Estimation Parameter file.

## Length of Key Field

If the *KEY field is alphanumeric it must be less than or equal to 40 characters (10 words)

## Samples for Each Estimate

There is no limit to the number of samples within the search volume for the estimation methods [Nearest Neighbor](<Grade%20Estimation%20Nearest%20Neighbour.md>), [Inverse Power Distance](<Grade%20Estimation%20Inverse%20Power%20of%20Distance.md>) or [Sichels t](<Grade%20Estimation%20Sichels%20T%20Estimator.md>). However for Ordinary [Kriging](<Grade%20Estimation%20Kriging.md>) and Simple Kriging there is a limit of 1400 samples. This limit should be taken into account when defining the MAXNUMn fields in the Search Volume Parameter File.

![](../Images/NextExercise.gif)[Go to the next topic](<Grade%20Estimation%20References.md>) (Grade Estimation Bibliography)