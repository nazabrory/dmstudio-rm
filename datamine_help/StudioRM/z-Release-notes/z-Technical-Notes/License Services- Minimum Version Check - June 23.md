# License Services - Important Information

Technical Note: TN00399

Datamine Studio products automatically install or upgrade **Datamine License Services** , a support service used to protect your software from unauthorized use.

This update brings two important changes to License Services. Both will affect how you license and activate your software:

  * When a Studio application installs License Services, that version of License Services becomes the _minimum required version to activate the software_. Earlier versions cannot be installed locally, but older server versions are still permitted.

  * **Studio RM Pro has been discontinued**. Studio RM continues and contains all functionality previously hosted by Studio RM Pro. 

**Important** : **To run Studio RM 2.0 and later versions, you will need a "Studio RM 2+" license.** Studio RM 2.0 and later versions can't be activated using licenses previously registered to activate Studio RM or Studio RM Pro.  
  
A "Studio RM 2+" is required for Studio RM 2.0 or later versions. Studio RM Pro is discontinued. Studio RM 2.0 and later versions can be used to upgrade previous Studio RM versions. Data and projects created by legacy product versions can be loaded into Studio RM 2.0 and later versions.  
  
For more information, refer to the following technical note on the Datamine Support Website (login required):  
  
<https://datamine.freshdesk.com/en/support/solutions/articles/19000152442-studio-rm-2-0-licensing-changes>  
  
If you need further information, please contact your local Datamine office.

License Services is a technology that governs access to your installed application through a running background service. It has a dedicated application **Datamine License Manager** to administer licenses on both client and server machines.

Studio products released after July 2023 are connected to the License Services version that comes with the Studio application. You can't go back to an older version of License Services that was installed before the one by your Studio application.

This modification doesn't impact License Services versions on dedicated license servers. Older server versions of License Services can still be used alongside newer versions of License Services on local machines hosting Studio applications.

To put it simply: Studio products created after July 2023 install a version of License Services that can't be downgraded on your local machine.

##### Why are we making this change?

To protect your software from unlicensed use and permit more flexible and accessible methods of licensing to be developed in the future.

##### Will my software work with a newer version of License Services (than Studio originally installed)?

Yes. If the local installation of License Services is newer than the one originally installed, your older Studio product(s) will continue to operate normally. A minimum version of License Services is required to launch your application.

##### Will future License Services versions be compatible with legacy Studio products?

Yes. This change doesn't break compatibility between License Services and versions of Studio products produced prior to July 2023.

##### If a locally-installed version of License Services is incompatible, what happens?

When your application is launched, a message is displayed indicating an upgrade to License Services is required. License Services can be downloaded from the Datamine Support Website as a standalone installation package, or it can be installed with another Studio product.

##### Does this affect servers running License Services (that aren't used to run Studio products)?

No. Server versions, providing they are already supported, continue to serve licenses as before. There's no need to upgrade license servers as a result of this change. This change enforces a minimum _local_ License Services version constraint.

_For more information on License Services, please refer to your help file, the Datamine Support website, or contact your local Datamine representative for assistance._