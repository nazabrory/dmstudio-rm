# Dynamic Anisotropy (ESTIMA): Example 2: Macro 2

**Note** : **[COKRIG](<../Process_Help_XML/cokrig.md>)** also provides Dynamic Anisotropy support. See [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)

This macro can been used to recreate the results of [Example 2](<Dynamic%20Anisotropy%20-%20Example%202.md>), using wireframe data.
    
    
    !START M2      Zonal Anisotropy Using Wireframe Data  
  
---  
      
    
    # Zonal Anisotropy Example Using UG Tutorial Data  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Data files used are:  
      
    
    #   - Block Model:     _vsbmgeo  
      
    
    #   - Drillholes:      _vsldhz  
      
    
    #   - Wireframe:       _vsoretr, _vsorept  
      
    
    # ----------------------------------------------------------------------  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Create data subset for zone 1 only  
      
    
    # ----------------------------------------------------------------------  
      
    
    !COPY   &IN(_VSBMGEO),&OUT(MODEL1),ZONE=1  
      
    
    !COPY   &IN(_VSLDHZ),&OUT(HOLES1),ZONE=1  
      
    
    !COPY   &IN(_VSORETR),&OUT(WTR1),ZONE=1  
      
    
    !COPY   &IN(_VSOREPT),&OUT(WPT1)  
      
    
       
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Calculate true dip and true dip direction from wireframe  
      
    
    # ----------------------------------------------------------------------  
      
    
    !ANISOANG &WIRETR(WTR1),&WIREPT(WPT1),&POINTS(POINTS1),  
      
    
              @TRIPTS=1.0,@ADDSYMB=1.0,  
      
    
              @MINDIP=5,@MAXDIP=85,@MINDIRN=20,@MAXDIRN=160,  
      
    
              @WFSYMB=216.0,@WFCOL=3.0,@SYMSIZE=3.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Search volume parameter file for interpolating angles  
      
    
    # ----------------------------------------------------------------------  
      
    
    !INPFIL &OUT(SPAR1)  
      
    
    Search Volume Parameter File  
      
    
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
      
    
    # no system file  
      
    
    1,2,25,25,25,0,0,0,3,1,3,0,1,1,4,2,4,2,2,4,3,1,4,0  
      
    
    !rem  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Estimation parameter file for ESTIMA  
      
    
    #   - EPAR1 for interpolating angles (IMETHOD=8)  
      
    
    # ----------------------------------------------------------------------  
      
    
    !INPFIL &OUT(EPAR1)  
      
    
    Estimation Parameter File for Interpolating Angles  
      
    
    VALUE_IN A 8 Y -  
      
    
    NUMSAM_F A 8 Y -  
      
    
    SREFNUM  N Y 0  
      
    
    IMETHOD  N Y 0  
      
    
    POWER    N Y 0  
      
    
    ]  
      
    
    ok  
      
    
    # no system file  
      
    
    TRDIP,NDIP,1,8,2  
      
    
    TRDIPDIR,NDIPDIR,1,8,2  
      
    
    !rem  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Interpolate APDIP and TRDIPDIR (IMETHOD=8)  
      
    
    # ----------------------------------------------------------------------  
      
    
    !ESTIMA   &PROTO(MODEL1),&IN(POINTS1),&SRCPARM(SPAR1),&ESTPARM(EPAR1),  
      
    
              &MODEL(MODEL2),*X(XPT),*Y(YPT),*Z(ZPT),@DISCMETH=1.0,  
      
    
              @XPOINTS=2.0,@YPOINTS=2.0,@ZPOINTS=2.0,@PARENT=0.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Calculate true dip angle TRDIP.  Not needed when using wireframes!  
      
    
    # ----------------------------------------------------------------------  
      
    
    #!APTOTRUE &IN(MODEL2),&OUT(MODEL3),@APDIPDIR=90  
      
    
    !COPY &IN(MODEL2),&OUT(MODEL3)  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Search volume file for interpolating grade using dynamic anisotropy  
      
    
    # ----------------------------------------------------------------------  
      
    
    !INDATA &IN(SPAR1),&OUT(TEMP1)  
      
    
    # no system file  
      
    
    1,2,50,50,20,91,36,0,3,1,3,0,1,1,4,5,15,2,5,15,3,1,15,0  
      
    
    !rem  
      
    
    !ADDDD    &IN(TEMP1),&OUT(SPAR2)  
      
    
    Adding fields SANGL1_F and SANGL2_F  
      
    
    SANGL1_F A 8 Y TRDIPDIR  
      
    
    SANGL2_F A 8 Y TRDIP  
      
    
    [  
      
    
    ok  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Estimation parameter file for grade using dynamic anisotropy  
      
    
    #   - EPAR2 for interpolating grades (IMETHOD=2)  
      
    
    # ----------------------------------------------------------------------  
      
    
    !INPFIL &OUT(EPAR2)  
      
    
    Estimation Parameter File for Interpolating Grades  
      
    
    VALUE_IN A 8 Y -  
      
    
    VALUE_OU A 8 Y -  
      
    
    SREFNUM  N Y 0  
      
    
    IMETHOD  N Y 0  
      
    
    POWER    N Y 0  
      
    
    ]  
      
    
    ok  
      
    
    # no sys file  
      
    
    AU,AU1,1,2,2  
      
    
    !rem  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Interpolate Grade using Dynamic Anisotropy  
      
    
    # ----------------------------------------------------------------------  
      
    
    !ESTIMA   &PROTO(MODEL3),&IN(HOLES1),&SRCPARM(SPAR2),&ESTPARM(EPAR2),  
      
    
              &MODEL(MODEL4),*X(X),*Y(Y),*Z(Z),@DISCMETH=1.0,  
      
    
              @XPOINTS=2.0,@YPOINTS=2.0,@ZPOINTS=2.0,@PARENT=0.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Search volume file for interpolating grade without dynamic anisotropy  
      
    
    # ----------------------------------------------------------------------  
      
    
    !SELDEL &IN(SPAR2),&OUT(SPAR3),*F1(SANGL1_F),*F2(SANGL2_F)  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Estimation parameter file for grade without dynamic anisotropy  
      
    
    #   - EPAR3 for interpolating grades (IMETHOD=2)  
      
    
    # ----------------------------------------------------------------------  
      
    
    !INPFIL &OUT(EPAR3)  
      
    
    Estimation Parameters for Grade with Dynamic Anisotropy  
      
    
    VALUE_IN A 8 Y -  
      
    
    VALUE_OU A 8 Y -  
      
    
    SREFNUM  N Y 0  
      
    
    IMETHOD  N Y 0  
      
    
    POWER    N Y 0  
      
    
    ]  
      
    
    ok  
      
    
    # no sys file  
      
    
    AU,AU2,1,2,2  
      
    
    !rem  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Interpolate Grade without Dynamic Anisotropy  
      
    
    # ----------------------------------------------------------------------  
      
    
    !ESTIMA   &PROTO(MODEL4),&IN(HOLES1),&SRCPARM(SPAR3),&ESTPARM(EPAR3),  
      
    
              &MODEL(MODEL5),*X(X),*Y(Y),*Z(Z),@DISCMETH=1.0,  
      
    
              @XPOINTS=2.0,@YPOINTS=2.0,@ZPOINTS=2.0,@PARENT=0.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Compare Grades with and without Dynamic Anisotropy  
      
    
    # ----------------------------------------------------------------------  
      
    
    !EXTRA   &IN(MODEL5),&OUT(MODEL6),@PRINT=1  
      
    
    VOL    = XINC*YINC*ZINC  
      
    
    AUDIFF = AU1 - AU2  
      
    
    go  
      
    
    !TONGRAD &IN(MODEL6),&OUT(RESULTS1),*F1(AU1),*F2(AU2),@DENSITY=2.5,@ROW=1  
      
    
    !DMEDIT  &IN(RESULTS1)  
      
    
    C  
      
    
    ROW  
      
    
    SECTION  
      
    
    E  
      
    
    !TONGRAD &IN(MODEL6),&OUT(RESULTS2),*F1(AU1),*F2(AU2),@DENSITY=2.5  
      
    
    !APPEND  &IN1(RESULTS1),&IN2(RESULTS2),&OUT(TEMP2)  
      
    
    !EXTRA   &IN(TEMP2),&OUT(RESULTS3),@PRINT=1  
      
    
    TONNES = int(TONNES)  
      
    
    AU1    = int(AU1*100)/100  
      
    
    AU2    = int(AU2*100)/100  
      
    
    AUDIFF = AU1 - AU2  
      
    
    go  
      
    
    !LIST    &IN(RESULTS3),*F1(SECTION),*F2(TONNES),*F3(AU1),*F4(AU2),  
      
    
             *F5(AUDIFF),@PROMPT=0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Plot AUDIFF by E-W Section  
      
    
    # ----------------------------------------------------------------------  
      
    
    !CHART    &IN(RESULTS3),&PLOT(AUDIFSEC),*X(SECTION),*Y(AUDIFF),@CHARTTYP=2.0,  
      
    
              @HISTTYP=1.0,@BINSIZE=1.0,@BINMIN=0.0,@BINMETH=1.0,  
      
    
              @XTRANS=1.0,@YTRANS=1.0,@LOGMIN=0.01,@FRAMETYP=2.0,  
      
    
              @XFACTOR=1.0,@YFACTOR=1.0,@LINETYP1=1.0,@SYMBOL1=92.0,  
      
    
              @SYMSIZE1=3.0,@COLOUR1=1.0,@LINETYP2=0.0,@SYMBOL2=0.0,  
      
    
              @SYMSIZE2=3.0,@COLOUR2=0.0,@APPEND=0.0,@COLFLAG=1.0,  
      
    
              @LEGCHSIZ=3.0,@TCHARSZ=5.0,@TCOLOUR=1.0,@XINC=100.0,  
      
    
              @YINC=0.5,@NDX=0.0,@NDY=1.0,@IGRID=4.0,@FCHARSZ=5.0,  
      
    
              @FCOLOUR=1.0,@XPAPER=240.0,@YPAPER=200.0,@XMIN=4100.0,  
      
    
              @XMAX=4500.0,@YMIN=-1.0,@YMAX=1.0,@PROGRESS=1.0,  
      
    
              @DISPLAY=1.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Plot AUDIFF Histogram  
      
    
    # ----------------------------------------------------------------------  
      
    
    !CHART    &IN(MODEL6),&PLOT(AUDIFHIS),*X(AUDIFF),@CHARTTYP=3.0,  
      
    
              @HISTTYP=1.0,@BINSIZE=0.5,@BINMIN=-8.0,@BINMAX=8.0,  
      
    
              @BINMETH=1.0,@XTRANS=1.0,@YTRANS=1.0,@LOGMIN=0.01,  
      
    
              @FRAMETYP=2.0,@XFACTOR=1.0,@YFACTOR=1.0,@LINETYP1=1.0,  
      
    
              @SYMBOL1=92.0,@SYMSIZE1=3.0,@COLOUR1=1.0,@LINETYP2=0.0,  
      
    
              @SYMBOL2=0.0,@SYMSIZE2=3.0,@COLOUR2=0.0,@APPEND=0.0,  
      
    
              @COLFLAG=1.0,@LEGCHSIZ=3.0,@TCHARSZ=5.0,@TCOLOUR=1.0,  
      
    
              @XINC=2.0,@YINC=5.0,@NDX=0.0,@NDY=0.0,@IGRID=3.0,  
      
    
              @FCHARSZ=5.0,@FCOLOUR=1.0,@XPAPER=240.0,@YPAPER=200.0,  
      
    
              @PROGRESS=1.0,@DISPLAY=1.0  
      
    
    # ----------------------------------------------------------------------  
      
    
    #  Save the important files  
      
    
    # ----------------------------------------------------------------------  
      
    
    !COPY  &IN(POINTS1),&OUT(POINTS1B)  
      
    
    !COPY  &IN(MODEL6),&OUT(MODEL6B)  
      
    
    !COPY  &IN(RESULTS3),&OUT(RESULT3B)  
      
    
    !COPY  &IN(AUDIFSEC),&OUT(AUDIFSEB)  
      
    
    !COPY  &IN(AUDIFHIS),&OUT(AUDIFHIB)  
      
    
    !END  
  
Related topics and activities

  * [Dynamic Anisotropy - Example 2](<Dynamic%20Anisotropy%20-%20Example%202.md>)

  * [Dynamic Anisotropy - Example 2 Macro 1](<Dynamic%20Anisotropy%20-%20Example%202%20Macro%201.md>)

  * [Dynamic Anisotropy with ESTIMA](<Dynamic%20Anisotropy%20-%20Introduction.md>)

  * [Dynamic Anisotropy with COKRIG](<Dynamic%20Anisotropy-COKRIG-Guidelines.md>)