# Dynamic Anisotropy (ESTIMA): Example 1: Macro 1

**Note** : **[COKRIG](<../Process_Help_XML/cokrig.md>)** also provides Dynamic Anisotropy support. See [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)

The following macro can be used to recreate [Example 1](<Dynamic%20Anisotropy%20-%20Example%201.md>).
    
    
    !START M1      Dynamic Anisotropy Example 1# ----------------------------------------------------------------------  
  
---  
      
    
    #  Example of dynamic anisotropy in ESTIMA, as described in example 1 in  
      
    
    #  the user guide.  The following input files are required:  
      
    
    #   -  oretr, orept  The orebody wireframe  
      
    
    #   -  daholes       The drillhole sample file  
      
    
    #  
      
    
    #  
      
    
    #  The macro performs the following functions:  
      
    
    #   - defines a prototype model and fills it with cells using TRIFIL  
      
    
    #   - calculates the azi and dip of all triangles in the orebody wf  
      
    
    #     using ANISOANG  
      
    
    #   - uses IMETHOD 8 in ESTIMA to interpolate azi and dip into the model  
      
    
    #   - uses the dynamic anistropy option in ESTIMA to estimate AU values  
      
    
    #     into the model.  
      
    
    #  
      
    
    # ----------------------------------------------------------------------  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Create block model  
      
    
    # ----------------------------------------------------------------------  
      
    
    !PROTOM   &OUT(PMOD)  
      
    
    n  
      
    
    y  
      
    
    0  
      
    
    0  
      
    
    0  
      
    
    5  
      
    
    5  
      
    
    2.5  
      
    
    40  
      
    
    36  
      
    
    64  
      
    
    !TRIFIL   &PROTO(PMOD),&MODEL(OREMOD1),&WIRETR(ORETR),&WIREPT(OREPT),  
      
    
              @MODLTYPE=5.0,@MAXDIP=0.0,@SPLITS=0.0,@PLANE='XY  ',  
      
    
              @XSUBCELL=1.0,@YSUBCELL=1.0,@ZSUBCELL=1.0,@RESOL=1.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Calculate azi, dip and centre of each triangle  
      
    
    # ----------------------------------------------------------------------  
      
    
    #!COGTRI   &WTRIN(ORETR),&WPTIN(OREPT),&PTNOUT(POINTS1),  
      
    
    #          @VERTEX=0,@SYMBOL=216,@SYMSIZE=2  
      
    
    !ANISOANG &WIRETR(ORETR),&WIREPT(OREPT),&POINTS(POINTS1),  
      
    
              @TRIPTS=1.0,@ADDSYMB=1.0,  
      
    
              @WFSYMB=216.0,@WFCOL=3.0,@SYMSIZE=2.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Define search volume parameter file containing 3 search volumes:  
      
    
    #   1 - for interpolating angles (1st run of ESTIMA)  
      
    
    #   2 - for interpolating grades without dynamic anisotropy (2nd run)  
      
    
    #   3 - for interpolating grades with dynamic anisotropy (2nd run)  
      
    
    # ----------------------------------------------------------------------  
      
    
    !INPFIL &OUT(SPAR1)  
      
    
    Field definition file for search volume  
      
    
    SREFNUM  N  Y  0  
      
    
    SMETHOD  N  Y  0  
      
    
    SDIST1   N  Y  0  
      
    
    SDIST2   N  Y  0  
      
    
    SDIST3   N  Y  0  
      
    
    SANGLE1  N  Y  0  
      
    
    SANGLE2   N  Y  0  
      
    
    SANGLE3   N  Y  0  
      
    
    SAXIS1    N  Y  0  
      
    
    SAXIS2    N  Y  0  
      
    
    SAXIS3    N  Y  0  
      
    
    OCTMETH   N  Y  0  
      
    
    MINOCT    N  Y  0  
      
    
    MINPEROC  N  Y  0  
      
    
    MAXPEROC  N  Y  0  
      
    
    MINNUM1   N  Y  0  
      
    
    MAXNUM1   N  Y  0  
      
    
    SVOLFAC2  N  Y  0  
      
    
    MINNUM2   N  Y  0  
      
    
    MAXNUM2   N  Y  0  
      
    
    SVOLFAC3  N  Y  0  
      
    
    MINNUM3   N  Y  0  
      
    
    MAXNUM3   N  Y  0  
      
    
    MAXKEY    N  Y  0  
      
    
    ]  
      
    
    ok      
      
    
    # no sys file  
      
    
    1,2,25,25,25 ,0,0,0,3,1,3,0,1,1,4,5,10,1.5,5,10,2.5,1,10,0  
      
    
    !rem  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Estimation parameter file for interpolating angles  
      
    
    # ----------------------------------------------------------------------  
      
    
    !INPFIL &OUT(EPAR1)  
      
    
    Field definition file for interpolating angles  
      
    
    VALUE_IN A 8 Y -  
      
    
    NUMSAM_F A 8 Y -  
      
    
    SREFNUM  N Y 0  
      
    
    IMETHOD  N Y 0  
      
    
    POWER    N Y 0  
      
    
    ]  
      
    
    ok  
      
    
        # no sys file  
      
    
    TRDIP,NSAMP,1,8,2  
      
    
    TRDIPDIR,,1,8,2  
      
    
    !rem  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Interpolate dip and dip direction using IMETHOD=8  
      
    
    # ----------------------------------------------------------------------  
      
    
    !ESTIMA   &PROTO(OREMOD1),&IN(POINTS1),&SRCPARM(SPAR1),&ESTPARM(EPAR1),  
      
    
              &MODEL(OREMOD2),*X(XPT),*Y(YPT),*Z(ZPT),@DISCMETH=1.0,  
      
    
              @XPOINTS=3.0,@YPOINTS=3.0,@ZPOINTS=3.0,@PARENT=0.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Search volume parameter file for interpolating grade  
      
    
    #  Need to add the two dynamic anisotropy angle fields  
      
    
    #  - search volume 1 for horizontal search  
      
    
    #  - search volume 2 for dynamic anisotropy  
      
    
    # ----------------------------------------------------------------------  
      
    
    !EXTRA    &IN(SPAR1),&OUT(SPAR2),@PRINT=1  
      
    
    SANGL1_F;a8 = "TRDIPDIR"  
      
    
    SANGL2_F;a8 = "TRDIP"  
      
    
    go  
      
    
    !INDATA   &IN(SPAR2),&OUT(SPAR2)  
      
    
    # no sys file  
      
    
    1,2,25,25,2.5,0,0,0,3,1,3,0,1,1,4,5,10,1.5,5,10,2.5,1,10,0,,  
      
    
    2,2,25,25,2.5,0,0,0,3,1,3,0,1,1,4,5,10,1.5,5,10,2.5,1,10,0,TRDIPDIR,TRDIP  
      
    
    !rem  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Estimation parameter file for interpolating grade  
      
    
    #  AU1 uses search volume 1 - horizontal search volume  
      
    
    #  AU2 uses search volume 2 - orientation defined from model cells  
      
    
    # ----------------------------------------------------------------------  
      
    
    !INPFIL &OUT(EPAR2)  
      
    
    Field definition file for interpolating grade  
      
    
    VALUE_IN A 8 Y -  
      
    
    VALUE_OU A 8 Y -  
      
    
    NUMSAM_F A 8 Y -  
      
    
    SVOL_F   A 8 Y -  
      
    
    SREFNUM  N Y 0  
      
    
    IMETHOD  N Y 0  
      
    
    POWER    N Y 0  
      
    
    ]  
      
    
    ok  
      
    
    # no sys file  
      
    
    AU,AU1,NSAMP1,SVOL1,1,2,2  
      
    
    AU,AU2,NSAMP2,SVOL2,2,2,2  
      
    
    !rem  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Estimate AU using dynamic anisotropy  
      
    
    # ----------------------------------------------------------------------  
      
    
    !ESTIMA   &PROTO(OREMOD2),&IN(DAHOLES),&SRCPARM(SPAR2),&ESTPARM(EPAR2),  
      
    
              &MODEL(OREMOD3),@DISCMETH=1.0,@XPOINTS=3.0,@YPOINTS=3.0,  
      
    
              @ZPOINTS=3.0,@PARENT=0.0  
      
    
    !END  
  
Related topics and activities

  * [Dynamic Anisotropy with ESTIMA](<Dynamic%20Anisotropy%20-%20Introduction.md>)

  * [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)