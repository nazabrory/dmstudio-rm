# ANISOANG - New Rotation Input

Technical Note: TN00441

Restricted distribution

## ANISOANG Process - Background

**ANISOANG** calculates the dip direction and dip of a triangle from strings (dip/strike) or surfaces. It is a file-based processed, available in Studio RM.

The calculated orientation is based on the direction of strings or wireframe, and is independent of a variogram or search model that would be used for estimation with dynamic anisotropy. Points (containing dip direction and azimuth) from **ANISOANG** are estimated (using angled IPD/NN) into the block model, and used for grade estimation with dynamic anisotropy.

### What about plunge (Angle 3)?

This leaves ambiguity angles in the block model and the variogram, as variograms models could be modelled in four possible orientations, although these variograms are equivalent to each other. 

Using dynamic anisotropy without checking the angles versus the variogram could result in an estimation error if the angles are not correctly validated. Typically, it was important to check the variogram model was always modelled using positive angles and attaching the variogram Plunge (taken from ANGLE3) as a constant angle when using dynamic anisotropy (DA).

### Changes to ANISOANG

**ANISOANG** now has an additional input rotation, which can be either a search parameter or a variogram model. If a rotation is chosen, the output angles from **ANISOANG** will be aligned with the input rotation.

The * **REFERENCE** , * **ANGLE1** , * **ANGLE2** , * **ANGLE3** , * **AXIS1** , * **AXIS2** , * **AXIS3** fields from the search or variogram should be selected as fields. This rotation must have the input rotation compatible as 3-1-3 (Z-X-Z), as these translate to dip direction, dip and plunge.

The rotation aligns the **ANISOANG** points, and only allow points that fall within the &**THRESH** degrees of the rotation orientation are be included. The points outside of the &**THRESH** are added to an optional &**REJECTED** points file.

## Installing the Pre-release Superprocess

We expect this update to **ANISOANG** to be released in Studio RM 2.1 (Early 2024), so until then we have instructions on how to install the updated superprocess for early access. 

  1. Ensure you are logged into your PC with an account with local administrative privileges. This is required to copy files to your Studio installation folder.

  2. If Studio RM is running, close it.

  3. Download the required ANISOANG patch files from [here](<https://dataminesoftware-my.sharepoint.com/:u:/p/productstore/ETeInFIN3YdHowtMzassg7gBF-00IXoxe-PtFXy7ty80RA?e=MUGkTv>) (full URL below):

**https://dataminesoftware-my.sharepoint.com/:u:/p/productstore/ETeInFIN3YdHowtMzassg7gBF-00IXoxe-PtFXy7ty80RA?e=MUGkTv**

  4. The downloaded archive contains four files:

     * ANISOANG.men

     * ANISOANG.stk

     * sp_anisoang.mac

     * anisoang.xml

Unpack all four files to a temporary location and leave your folder browser open. We'll call this "Window 1".

  5. In a separate folder browser, navigate to your Studio RM installation folder. By default, this is **C:\Program Files\Datamine\StudioRM** , but custom installation locations are possible. We'll call this "Window 2".

  6. In Window 2, open the **Html** folder, then the **Commands** folder.

  7. Copy the file _anisoang.xml_ from Window 1 into Window 2 and confirm your action. Depending on your User Access Control settings, you may need to confirm multiple times.

  8. In Window 2, navigate back to your top-level installation folder (as seen in Step 5).

  9. In Window 2, open the **Menus** folder.

  10. Copy the files _ANISOANG.men_ , _ANISOANG.stk_ and _sp_anisoang.ma_ c from Window 1 into Window 2. As before, confirm as required.

  11. Restart Studio RM. Your updated **ANISOANG** process is now available.

## ANISOANG Update - Worked Example

Consider a geological feature (CU in Shear_A) trending towards the north, dipping towards the east. The wireframe of the vein contains edges, which are generally unsuitable for **ANISOANG** , but are useful to demonstrate this example. 

The data used in this example can be downloaded from the [Datamine Support Website](<https://dataminesoftware-my.sharepoint.com/:u:/p/productstore/ERqeVaiXtBBDvkL2PMW4ciYBndT8SUNOX4xDe43lb0SWJA?e=sTaUrk>). In case this link is blocked, copy the URL below into a browser:

https://dataminesoftware-my.sharepoint.com/:u:/p/productstore/ERqeVaiXtBBDvkL2PMW4ciYBndT8SUNOX4xDe43lb0SWJA?e=sTaUrk

![](../../../Images_STUDIORM_ONLY/Vein_SteepDip.png)

When modelling the anisotropy, there are multiple ways this could be done (all of which are valid):

  * This could be modelled in the horizontal as slightly to the west of north, or slightly to the east of south.

  * This could be modelled in the across strike to the north east or to the south west.

  * The dip plane could be modelled to the south east or the south west.

The result is eight combinations of variograms. Each of these is duplicated, so finally, results in four possible rotations. These rotations have different axes, although they are identical in orientation and magnitude.

![](../../../Images_STUDIORM_ONLY/Anisotropy_Supervisor.png)

_Anisotropy and variograms in Datamine Supervisor (1 of the possible 8 configurations of anisotropy)_

Taking a look at the variogram models as ellipsoids, you can see the four possible combinations:

![](../../../Images_STUDIORM_ONLY/Ellipsoids_Combinations.png)

These equivalent rotations can also be shown in a table as:

| Angle 1 | Angle 2 | Angle 3 | Axis 1 | Axis 2 | Axis 3  
---|---|---|---|---|---|---  
Rotation 1 | 80 | 60 | 50 | 3 | 1 | 3  
Rotation 2 | 80 | 60 | -130 | 3 | 1 | 3  
Rotation 3 | -100 | 120 | 130 | 3 | 1 | 3  
Rotation 4 | -100 | 120 | -50 | 3 | 1 | 3  
  
Depending on which rotation is used, the points from **ANISOANG** fall within a given threshold angles of the rotation. As you can see from some example values from the block model below, these values are similar (with a threshold) to the rotation angles supplied. Angles are converted to equivalent angles that orientate with the rotation, and angles that fall outside are excluded:

![](../../../Images_STUDIORM_ONLY/ANISOANG_Tables.png)

The valid points look like this, and run through the **DAELLIPS** process. For each case, these look like the points below, however, each output has different angle values at each point:

![](../../../Images_STUDIORM_ONLY/DAELLIPS_Points.png)

For any of the runs through Anisotropy, the rejected points look like the image below. These are points from the edge of the wireframe, which do not align with the variogram. It is expected that these points should not be included as they would push grade in the incorrect direction. There are some points that are excluded towards the middle which are also excluded. Its worth investigating these, and perhaps adjust the threshold if these should be included:

![](../../../Images_STUDIORM_ONLY/ANISOANG_rejected.png)

These points are estimated into the block model (using **IMETHOD** =8), and further estimated into the block model. Each of the resultant block models is identical.

For more information on ANISOANG, and dynamic anisotropy in Studio RM, please refer to your help file.