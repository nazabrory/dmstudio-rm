# Search Volume Parameters

This topic is part of the [Grade Estimation](<Grade%20Estimate%20Overview.md>) range of topics.

The Search Volume Parameter file contains the 24 fields shown in the table. All fields are numeric and are compulsory. The default value for a field is the value used by the process if the field value has been entered as - (absent data).

The following fields are included:

Search Volume Parameters File  
---  
Field Name |  Default |  Description  
SRENUM |  |  Search volume reference number  
SMETHOD |  2 |  Search volume shape (1 = 3D rectangular, 2 = ellipsoid)  
SDIST1 |  100 |  Maximum search distance in direction 1 (X)  
SDIST2 |  100 |  Maximum search distance in direction 2 (Y)  
SDIST3 |  100 |  Maximum search distance in direction 3 (Z)  
SANGLE1 |  0 |  First rotation angle for search volume  
SANGLE2 |  0 |  Second rotation angle for search volume  
SANGLE3 |  0 |  Third rotation angle for search volume  
SAXIS1 |  3 |  Axis for first rotation (1 = X, 2 = Y, 3 = Z)  
SAXIS2 |  1 |  Axis for second rotation  
SAXIS3 |  3 |  Axis for third rotation  
MINNUM1 |  1 |  Minimum number of samples for first dynamic search volume  
MAXNUM1 |  20 |  Maximum number of samples for first dynamic search volume  
SVOLFAC2 |  0 |  Axis multiplying factor for second dynamic search volume  
MINNUM2 |  1 |  Minimum number of samples for second dynamic search volume  
MAXNUM2 |  20 |  Maximum number of samples for second dynamic search volume  
SVOLFAC3 |  0 |  Axis multiplying factor for third dynamic search volume  
MINNUM3 |  1 |  Minimum number of samples for third dynamic search volume  
MAXNUM3 |  20 |  Maximum number of samples for third dynamic search volume  
OCTMETH |  0 |  Octant definition method (0 = do not use, 1 = use octants)  
MINOCT |  2 |  Minimum number of octants to be filled  
MINPEROC |  1 |  Minimum number of samples in an octant  
MAXPEROC |  4 |  Maximum number of samples in an octant  
MAXKEY |  0 |  Maximum number of samples with the same key value within an octant   
  
![](../Images/NextExercise.gif)[Go to the next topic](<Grade%20Estimation%20Dynamic%20Search%20Volumes.md>) (Dynamic Search Volumes)