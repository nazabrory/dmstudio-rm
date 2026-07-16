# Advanced Estimation - Case Study  
  
The Advanced Estimation module provides co-Kriging, enhanced variography and Kriging Neighbourhood Analysis (KNA). Estimation is faster than **[ESTIMA](<../Process_Help_XML/estima.md>)** and makes use of multiple cores when they are available.

A study of the differences and similarities between Advanced Estimation and the legacy ESTIMA-ESTIMATE process pair can be found on the Datamine Support Website (login required):

  * **[Support Article 153c: Advanced Estimation vs. ESTIMA](<https://dataminesoftware-my.sharepoint.com/:b:/p/productstore/IQCC3WGiFiWxT6yttm0Pgd2wAWeherYkwc8WkwpmQgUYZi4?download=1>)**

This document explains the key differences between Advanced Estimation (leveraging **[COKRIG](<../Process_Help_XML/cokrig.md>)** and other supporting processes) and the ESTIMA/**[ESTIMATE](<../Process_Help_XML/estimate.md>)** partner processes. In many ways, it offers a justification for moving to the faster and more capable functions available in the Advanced Estimation console.

It also describes examples of the similarities and important differences between the inputs and outputs of estimation functions in Studio RM. It is based on a hypothetical project, the data of which can be downloaded [from here](<https://dataminesoftware-my.sharepoint.com/:u:/p/productstore/IQDYOBBnfVSVS7sbh6oNI_CWAZQgDC5Q3ehXfOToRaZDdrE?download=1>), should you need to perform your own review or just to become more familiar with the tools on offer.

**Note** : You can use output parameter files from Datamine Supervisor instead of generating them in Studio. See [Advanced Estimation & Variography](<Multivariate_Introduction.md>).

Related Topics and Activities

  * [Advanced Estimation Introduction](<Multivariate_Introduction.md>)
  * Grade Estimation Basics