# Vein Modelling Outputs

Note: A Datamine [eLearning course](<https://datamine.learnupon.com/>) is available that covers functions described in this topic. Contact your local Datamine office for more details.

The **Create Vein Surface** tool computes any of the following data:

  * A **Hanging wall** (HW) wireframe surface.

  * A **Foot wall** (FW) wireframe surface.

  * A combined, enclosed wireframe volume incorporating **Both** HW and FW surfaces.

  * A **Trend surface** , showing the linear trend of the data throughout the modelled structure.

  * A **Boundary** string representing the outer hull of the structure as viewed via the current **Section Controls**.

  * A **Contact points** object containing all HW or FW intercept points used to construct the output surface or volume data.

Surface creation is dictated by the structure of input drillhole sample values. These values represent a discrete upper and lower bounding surface. Optionally, model a closed volume representing both HW and FW surfaces and control how surfaces interact in pinch and/or swell zones. 

You can either create a new data object, with default formatting, or you can update an existing object. The formatting of the existing object is controlled using **Retain output formatting** :

  * If checked, any previous edits made to a modelled vein structure are retained should you select **Update Vein**.

  * If unchecked, the update vein structure will have default formatting and any prior overlay customization is lost.

If computing a **New Vein** , the status of **Retain output formatting** is not relevant.

Related topics and activities

  * [Create Vein Surface](<Create_Vein_Surface.md>)

  * [Select Data for Implicit Modelling](<Create_Vein_Surfaces_1_Data.md>)

  * [Create a Vein Model](<Create_Vein_Surfaces_2_Activity.md>)