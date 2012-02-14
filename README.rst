=====================
ZenPacks.community.f5
=====================

.. contents::
   :depth: 3

Description
===========
Provides basic F5 BIG-IP monitoring.


***NOTE***: This is my first attempt at writing a ZenPack, so *PLEASE* install on 
a test system first. I've done enough testing to think its ready to share with 
a larger audience, but since its my first attempt, I'd appreciate caution when 
installing as well as feedback.

Components
==========
The ZenPack has the following: 

* /Network/f5 Device Class
* A Device template which graphs many of the same performance stats as 
  would be seen in the Overview >> Performance section of the 10.x UI
* Virtual Server Component Modeling

  * A component template for virtual servers. 
  * Virtual Server filtering. This pack adds a new zProperty, 
    **zF5BigipVirtualServerNameFilter**, which when set will limit which virtual 
    servers are included during a modeling cycle.  

* Node Component Modeling

  * A component template for nodes. 
  * Node filtering. This pack adds a new zProperty, **zF5BigipNodesNameFilter**, which when set will 
    limit which nodes are included during a modeling cycle. 

* Pool Component Modeling

  * A component template for Pools. 
  * Pool filtering. This pack adds a new zProperty, **zF5BigipPoolsNameFilter**, which when set will 
    limit which pools are included during a modeling cycle. 
    
Requirements
============
* Zenoss Versions Supported: 3.0+
* External Dependencies: None
* ZenPack Dependencies: None
* Configuration: No Special configuration should be necessary.

Download
========
Download the appropriate package for your Zenoss version from the list
below.

* Zenoss 3.0+ `Latest Package for Python 2.6`_
* Zenoss 4.1+ `Latest Package for Python 2.7`_

Installation
============
Normal Installation (packaged egg)
----------------------------------
Copy the downloaded .egg to your Zenoss server and run the following commands as the zenoss
user::

    zenpack --install <package.egg>
    zenoss restart
    
If you don't want to do a full restart, you should be able to just restart
zenhub and zopectl::

    zenhub restart &&  zopectl restart
   
Developer Installation (link mode)
----------------------------------
If you wish to further develop and possibly contribute back to the f5
ZenPack you should clone the git repository, then install the ZenPack in
developer mode using the following commands::

    git clone git://github.com/ZCA/ZenPacks.community.f5.git
    zenpack --link --install ZenPacks.community.f5
    zenoss restart
    
Change History
==============
* 0.82

  * Initial Release

* 1.0

  * Improved device detection. Should have no more "deprecated" values for 
    hardware model 
  * Minor updates to support segrated github repos and README.markdown
  * Including zenoss.snmp.DeviceMap & zenoss.snmp.NewDeviceMap plugins on the 
    newly created device class so that the base SNMP attributes are collected

* 1.1

  * Some additional tweaks for better Viprion detection
  * 1.2
  * Pool & Node Component Modeling Added
  * Component Detail Grids update to show more relevant columns for each of the modeled component types.

* 1.3

  * Added some code to the install method so that it rebuilds device relationships on install. This
    this seems be at the root of folks needing to delete/re-add devices to get components show up

* 1.4

  * Added the pool and node component templates that had been omitted from previous pack exports
  * minor tweaks to logging during installation time
  * some code cleanup to remove some unnecessary items that got added along the way

* 1.5

  * No actual code changes, just template changes.
    Replaced CFUNC of MAX with AVERAGE on all the graph defs based on some feedback on the forums as well 
    as additional testing
    
* 1.6

  * Added support for `Route Domains`_
  * Cleanup and standardization of columns in the various component grids
    
Known Issues
============
* Currently the status of the virtual server component is only detected and 
  set at model time. Its not a real time (or near real time) reflection of 
  the state of the virtual server on the LTM



Screenshots
===========
Device Details
--------------
|Device Details|

Virtual Server Components
-------------------------
|Virtual Server Components|

Node Components
---------------
|Node Components|

Pool Components
---------------
|Pool Components|

.. External References Below. Nothing Below This Line Should Be Rendered

.. _Latest Package for Python 2.6: http://github.com/downloads/ZCA/ZenPacks.community.f5/ZenPacks.community.f5-1.6-py2.6.egg
.. _Latest Package for Python 2.7: http://github.com/downloads/ZCA/ZenPacks.community.f5/ZenPacks.community.f5-1.6-py2.7.egg
.. _Route Domains: http://devcentral.f5.com/Tutorials/TechTips/tabid/63/articleType/ArticleView/articleId/353/v10--A-Look-at-Route-Domains.aspx

.. |Device Details| image:: http://github.com/ZCA/ZenPacks.community.f5/raw/master/screenshots/zenoss_bigip_DeviceDetails.png
.. |Virtual Server Components| image:: http://github.com/ZCA/ZenPacks.community.f5/raw/master/screenshots/zenoss_bigip_vs_component.png
.. |Node Components| image:: http://github.com/ZCA/ZenPacks.community.f5/raw/master/screenshots/zenoss_big_node_component.png
.. |Pool Components| image:: http://github.com/ZCA/ZenPacks.community.f5/raw/master/screenshots/zenoss_big_pool_component.png
