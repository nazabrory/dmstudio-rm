# Lagrange Multiplier

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

For overview information on all grade estimation methods in general, see [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>).

## IMETHOD = 102

This method is chosen if the IMETHOD field in the Estimation Parameter file is set to 102.

Whilst not actually a grade estimate, using this method, If **IMETHOD** =102, then the estimated value is the Lagrange multiplier calculated when solving the Ordinary Kriging matrix.

The Lagrange multiplier measures the increase in the objective function (f(x, y) that is obtained through a marginal relaxation in the constraint (an increase in k).