# Texture Drape Settings

To access this screen:

  * Right-click a textured wireframe overlay in the Sheets control bar and select **Texture Drape Settings**.

Configure the orientation and position of texture images draped over wireframe surfaces.

There are two main ways to orient a texture on a wireframe surface:

  * Manually configure the texture image's Position, Orientation and Scale.

  * Interactively digitize points on the image and map them to 3D scene coordinates using the **Image Registration** function.

You can use a combination of methods if you like, and can also save a georeference data file (in the same folder as the image texture) to guarantee the same alignment next time the wireframe is loaded.

To orient an existing wireframe texture:

  1. Load or create a texture wireframe in any 3D view. 

Note: Apply a texture to a loaded wireframe using the [Wireframe Properties](<Wireframe_Properties_Dialog.md>) screen. See also [Wireframe Texture Options](<Wireframe-Texture-Options.md>).

  2. Activate the **Sheets** control bar **> > Wireframes** folder.

  3. Right-click the textured wireframe overlay and select **Texture Drape Settings**. 

  4. Orient your wireframe texture:

     1. **To manually orient the texture** :

        1. Define the **Position** of the origin (bottom left) of the image file in XYZ world coordinates.

        2. Set the 3D orientation of the texture using Azimuth, Dip and Roll settings. All values are degrees.

        3. Choose the Width, and if Keep Aspect Ratio is unchecked, the Height of the texture in pixels.

        4. Click **Apply** to update the 3D view. If required, adjust settings and reapply.

     2. **To orient the texture interactively** :

        * Click **Use Points** to display the **Image Registration** screen. 

See [Image Registration](<ImageRegistration_Dialog.md>).

  5. To store a data file with georeferencing information alongside the texture image, ensure Save georef. file is checked. If unchecked, texture orientation is temporary and only lasts for as long as the target wireframe object is loaded.

  6. Click **OK** to complete the texture orientation process.

Related topics and activities

  * [Draping Images onto Wireframes](<Surfaces_Draping%20images.md>)

  * [Image Registration](<ImageRegistration_Dialog.md>)

  * [Image Registration - Example 1](<Image%20Registration%20Worked%20Example.md>)

  * [Image Registration Example 2](<image%20registration%20worked%20example%202.md>)

  * [Wireframe Properties: General](<Wireframe_Properties_Dialog.md>)

  * [Wireframe Texture Options](<Wireframe-Texture-Options.md>)