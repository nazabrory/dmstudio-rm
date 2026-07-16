# Silent Installations

Studio installers can be run without intervention. 

These unprompted installations can be accessed using command line switches.

This topic outlines the key principles for silent installations of Studio products. You may need to adapt this information to suit your particular group rollout services.

Note: Datamine cannot directly support 3rd party deployment tools used for mass/remote rollout of software applications. For assistance on these infrastructure tools, please contact your vendor directly.

### Command Line Instructions

The actual command line instruction to be used will depend on the mechanism in place for unmanned/remote/silent installations, but this example would allow a Studio RM package to be rolled out without prompts and potentially on remote machines:
    
    
    Datamine Studio RM (64-bit) 1.6.87.0 EN.exe /s /v"/qb ALLUSERS=1 REBOOT=ReallySuppress /norestart /l*v C:\Windows\Temp\Datamine Studio RM (64-bit) 1.6.87.0 EN.log"

Related information

  * [Studio RM Installation Guidelines](<Installation-Guidelines.md>)

  * [Installation Troubleshooter](<Troubleshooter-Installations.md>)