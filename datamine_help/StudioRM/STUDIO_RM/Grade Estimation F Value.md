# F Value

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

For overview information on all grade estimation methods in general, see [Grade Estimation Methods](<Grade%20Estimation%20Methods.md>).

### IMETHOD = 101

This method is chosen if the IMETHOD field in the Estimation Parameter file is set to 101.

Whilst not actually a grade estimate, using this method, the value written to the VALUE_OU field in the Output Model is the geostatistical F value i.e. the average value of the variogram in the cell.

The F Value is calculated using the formula F = (SSE1 SSE2 / m) / SSE2 / n-k, where SSE = residual sum of squares, m = number of restrictions and k = number of independent variables. Essentially, an analysis of variance.