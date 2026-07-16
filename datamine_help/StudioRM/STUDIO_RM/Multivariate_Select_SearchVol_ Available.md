# Available Search Volumes

To access this screen:

  * Display the **[Define Search Vol.](<Multivariate_Select_Search_Volumes.md>)** screen. Available search volumes appear in the centre of the screen.

In order to edit any of the search volume parameters select the required search volume in the centre area and then use the panel to the right as described in the **Edit Search Parameters** section below. 

When editing is complete you should make sure that the correct search volume is highlighted in the left area of the panel and then select the **Apply search volume to estimation** button at the bottom of the centre area.

**Tip** : You can also right-click any search volume to apply it to the currently active estimation by right-clicking it and choosing **Apply search parameters to selected estimation**.

To create a new search volume:

  1. Display the **Define Search Vol.** screen.

  2. Below the **Available Search Volumes** list, click **Add**.

A new search volume is added to the list, for further configuration.

**Tip** : Additional search volumes can be created by right clicking in the blank area below the last search volume and selecting **Add new search parameters** from the menu.

To manage the search volumes list:

The following options are available to manage the search volumes for the selected scenario:

  * **Import** : click this button to copy a set of search volume parameters from a DM file. The best way to create the required fields is to export a file first and then load it into the table editor and delete all the records. You can only import [search volume parameter files](<../COMMON/filetype.md#SearchVolAdv>) that are suitable for Advanced Estimation (and specifically, the underlying [COKRIG](<../Process_Help_XML/cokrig.md>) process).

  * **Export** : click this button to save the current search volume parameters to a DM file. File exported can be re-imported into the Advanced Estimation wizard. These files will be listed in the Project Files control bar using a dedicated category: Search Parameters (Adv. Est.).

**Note** : Search volume parameter files exported from the **Advanced Estimation** wizard cannot be used as an input to the [ESTIMA](<../Process_Help_XML/estima.md>) process, or [ESTIMATE](<../Process_Help_XML/estimate.md>) process.  

  * **Import** : save the current search volume parameters to file.

  * **Clear list:** click this button to delete the list of **Available Search Volumes.**.

Related topics and activities

  * [Define Search Volumes](<Multivariate_Select_Search_Volumes.md>)

  * [Define Search Volumes: Select an Estimation](<Multivariate_Select_SearchVol_%20Estimation.md>)

  * [Search Volume Parameters](<Multivariate_Select_SearchVol_Params.md>)