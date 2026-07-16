# open-validation-file ("ova")

See this command in the [**command table**.](<COMMAND%20TABLE_O.md#open-validation-file>)

To access this command:

  * Using the **[command line](<../COMMON/Command_Toolbar.md>)** , enter "open-validation-file".

  * Use the quick key combination "ova".

  * Display the **[Find Command](<../COMMON/findcommand.md>)** screen, locate **open-validation-file** and click **Run**.

## Command Overview

Open a [validation file](<../COMMON/filetype.md#Validation_File>) using the [Project Browser](<../COMMON/ProjectBrowser.md>).

[](<../COMMON/filetype.md#Validation_File>)

When a validation file has been opened and it is being used, (see [validate-onthefly-switch](<validate-onthefly-switch.md>)), when data is defined or edited the values you provide are constrained by the contents of the validation file. 

For example, in order to validate or constrain a numeric attribute called **ZONE** between 1 and 6 with a default value of 4 the validation would contain one record for the attribute **ZONE** containing the following values:

  * ATTNAME - ZONE

  * ATTTYPE - N

  * MIN - 1

  * MAX - 6

  * DEFAULT - 4

  * VALUE - Not used for numeric attributes.

As another example, to constrain an alphanumeric attribute called **LITHO** to have values of **LIME** , **GRANITE** or **QUARTZ** the validation file would have three records. For each of the three records:

  * **ATTNAME** would be _LITHO_

**ATTYPE** would be _A_

**VALUE** would be _LIME_ , _GRANITE_ and _QUARTZ_ in each of the records. 

**Note** : MIN and MAX fields are not used for alphanumeric attributes.

For the validation file to be used the **validate-onthefly-switch** must be active and the attributes must exist on the string or point data. Attributes can be added using the [add-attributes](<add-attributes.md>) command.

Related topics and activities

  * [validate-onthefly-switch ("auv")](<validate-onthefly-switch.md>)

  * [Validation File Type](<../COMMON/filetype.md#Validation_File>)

  * open-validation-file ("ova")
  * [open-model-file ("om")](<open-model-file.md>)

  * [open-results-file ("ore")](<open-results-file.md>)

  * [open-rosette-file ("oro")](<open-rosette-file.md>)

  * [open-section-file ("ose")](<open-section-file.md>)