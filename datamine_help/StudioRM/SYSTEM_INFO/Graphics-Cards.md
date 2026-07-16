# Graphics Capabilities

Your choice of graphics hardware depends on the nature of your work, and the environment in which the card is installed. 

Providing the latest drivers are installed, your graphics card capabilities can have a significant effect on the performance of installed applications, including those deployed by Datamine, if 3D data visualization is a core part of your daily routine. 

Although there is no definitive answer with regards to a manufacturer or version of card that will be suitable for Datamine applications, Datamine generally recommends **NVidia Quadro series** or their successor, **NVidia RTX** or **RTX Pro** series cards. 

This is based largely on our experience of reliability; drivers tend to be more stable and therefore produce less support issues, and how our 3D window technology (OpenGL) is supported well by this hardware. 

Datamine routinely test against NVidia Quadro cards. 

Datamine software currently only uses the graphics card for 3D graphics. If you are making use of Datamine's 3D/VR or similar visualization functions and views, then these functions will take advantage of the graphics cards capabilities. If you predominantly work in a non-3D view, such as the Plots or Design windows, then the benefits of a fast graphics card are still worth considering, as some of our more intensive processing can make use of a separate GPU (Graphics Processing Unit) if available.

## OpenGL Support

Studio products use OpenGL technology to provide 3D window visualization of loaded geometric data. We have always endeavoured to ensure entry requirements for this are as low as possible to reach as wide an audience as possible. However, as the world moves on and data grows and grows, and to remain competitive and provide the best we can offer, Studio products require a minimum version of OpenGL to run correctly.

Studio products require hardware that supports OpenGL version 3.3 or later.

If your current graphics card doesn't meet or exceed this standard, you can still continue to open your product, but there may be unexpected results including poor visualization feedback and even system instability.

You can hide the startup message if you like, but we recommend investigating a hardware solution for best results.

## General Recommendations and Guidance

  * It is recommended when purchasing new hardware that integrated ('on board') graphics cards are avoided due to potential system performance degradation. 

  * With all high-performance graphics cards, it is very important to make sure that you obtain and use the latest OpenGL drivers, at least OpenGL 3.1. For advice, contact your local Datamine support office. 

  * NVidia Quadro FX, RTX or RTX Pro cards are recommended for Datamine environments for enhanced visual performance. These cards are routinely used during pre-release testing. 

  * 4GB+ cards are preferred but, as with monitors (see above), the choice will be based on the type of work you need to perform. Your application draws resources from both system and video memory. If you are more inclined to produce complex graphics, particularly if using textured VR-style functions, more graphic memory will show more significant gains than for users working with lower-resolution data sets, spreadsheets etc. 

  * Settings for your card can also affect the running of Datamine applications both positively and adversely; if unexpected (and unwanted) system performance is encountered, it may be necessary to disable (or reduce) certain acceleration options until the optimum performance is found. Screen resolution, for example, has a significant impact on system performance, and can be adjusted downwards in some cases whilst maintaining an acceptable visual feedback. 

  * Drivers for your card must be actively managed; it is not always the case that the latest driver for your card will resolve issues; in fact, it may even introduce issues if new card features are enabled that cannot be interpreted correctly by your Datamine application (an example of this is the "Threaded Optimization" feature introduced with newer NVidia Cards - this must be disabled before using Datamine applications). Video card firmware must also be maintained. 

  * With the sheer volume and variety of graphic cards on the market, your choice will be governed by several factors. Although Datamine do not explicitly state sole support for a specific manufacturer, internal QA testing is performed against a variety of different card environments but using primarily NVidia hardware, including NVidia Quadro cards for high-end textured data process testing. 

#### Which works better, NVidia or AMD cards?

This depends entirely on the graphics card! In the past, our experience was that AMD had more issues with OpenGL support than NVidia, but that has improved in recent times. For example, an AMD FirePro should provide a similar level of performance as an NVidia card of the same performance tier, but as mentioned above, Datamine predominantly test against NVidia cards. 

There are many benchmarks web sites available to compare the performance of different graphics cards (none of which are maintained by Datamine).

####  Can Datamine applications take advantage of multiple video cards? 

Not explicitly, but the graphics card drivers usually have settings to speed up all DirectX and OpenGL applications. There are often issues generally with running multiple graphics cards, however so Datamine's recommendation is for a single graphics card.

Related topics and activities

  * [System Requirements](<Hardware-Requirements.md>)

  * [Studio RM Installation Guidelines](<Installation-Guidelines.md>)

  * [Installation Troubleshooter](<Troubleshooter-Installations.md>)