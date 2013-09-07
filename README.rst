=====================
ZenPacks.community.f5
=====================

.. image:: https://travis-ci.org/ZCA/ZenPacks.community.f5.png?branch=master
   :target: https://travis-ci.org/ZCA/ZenPacks.community.f5

.. contents::
   :depth: 3

Description
===========
Provides basic F5 BIG-IP monitoring and trending.


Features
==========

Device Classes
--------------
A new device class located at **/Network/f5** will be added

Device Template
---------------
A Device template which graphs many of the same performance stats as would be 
seen in the Overview >> Performance section of the 10.x UI

Component Templates
-------------------
Several new component templates will be added to the system. These templates 
**should not** be bound manually to any devices. They will be automatically 
bound to modeled components.

* Virtual Servers
* Nodes
* Pools
* `OneConnect Profiles`_

Modeler Plugins
---------------

Virtual Servers
+++++++++++++++
A new modeler plugin **BigipLtmVirtualServerMap** will be added to the system 
and automatically bound to the */Network/f5* device class. Filtering can
be accomplished using the zF5BigipVirtualServerNameFilter zProperty discussed
below.

Nodes
+++++
A new modeler plugin **BigipLtmNodeMap** will be added to the system 
and automatically bound to the */Network/f5* device class. Filtering can
be accomplished using the zF5BigipNodesNameFilter zProperty discussed
below.

Pools
+++++
A new modeler plugin **BigipLtmPoolMap** will be added to the system 
and automatically bound to the */Network/f5* device class. Filtering can
be accomplished using the zF5BigipPoolsNameFilter zProperty discussed
below.

OneConnect Profiles
+++++++++++++++++++
A new modeler plugin **BigipLtmConnPoolProfileMap** will be added to the system 
and automatically bound to the */Network/f5* device class.

zProperties
-----------
The following new zProperties will be added.

* **zF5BigipVirtualServerNameFilter** - When set will limit which virtual
  servers are included during a modeling cycle. The syntax should be any valid
  Python regular expression.
* **zF5BigipNodesNameFilter** - When set will limit which nodes are included during 
  a modeling cycle. The syntax should be any valid Python regular expression.
* **zF5BigipPoolsNameFilter** - When set will limit which pools are included during 
  a modeling cycle. The syntax should be any valid Python regular expression.

Requirements
============

* Zenoss Versions Supported: 3.0+
* External Dependencies: None
* ZenPack Dependencies: None
* Configuration: No Special configuration should be necessary.

    
Change Log
==========

* 1.8

  * Initial support for `OneConnect Profiles`_ as a device component
  * Initial integration with `Travis CI`_ (Laying groundwork for future testing)

* 1.7

  * `Issue 3`_ - Properly detect model for Viprion B4300 as well as additional
    models not previously detected
  * `Issue 4`_ - Ensure BipIpUtils no longer appears as a modeler plugin
  * Removal of MIB files from ZenPack, to address unknowns around licensing 
    and/or distribution requirements
  * Documentation updates
  
* 1.6

  * Added support for `Route Domains`_
  * Cleanup and standardization of columns in the various component grids  

* 1.5

  * No actual code changes, just template changes.
    Replaced CFUNC of MAX with AVERAGE on all the graph defs based on some feedback on the forums as well
    as additional testing
    
* 1.4

  * Added the pool and node component templates that had been omitted from previous pack exports
  * minor tweaks to logging during installation time
  * some code cleanup to remove some unnecessary items that got added along the way
  
* 1.3

  * Added some code to the install method so that it rebuilds device relationships on install. This
    this seems be at the root of folks needing to delete/re-add devices to get components show up  

* 1.1

  * Some additional tweaks for better Viprion detection
  * 1.2
  * Pool & Node Component Modeling Added
  * Component Detail Grids update to show more relevant columns for each of the modeled component types.

* 1.0

  * Improved device detection. Should have no more "deprecated" values for
    hardware model
  * Minor updates to support segrated github repos and README.markdown
  * Including zenoss.snmp.DeviceMap & zenoss.snmp.NewDeviceMap plugins on the
    newly created device class so that the base SNMP attributes are collected
  
* 0.82

  * Initial Release


Known Issues
============
* Currently the status of the virtual server component is only detected and
  set at model time. Its not a real time (or near real time) reflection of
  the state of the virtual server on the LTM


.. External References Below. Nothing Below This Line Should Be Rendered

.. _Route Domains: http://devcentral.f5.com/Tutorials/TechTips/tabid/63/articleType/ArticleView/articleId/353/v10--A-Look-at-Route-Domains.aspx
.. _OneConnect Profiles: http://support.f5.com/kb/en-us/solutions/public/7000/200/sol7208.html
.. _Travis CI: https://travis-ci.org/

.. _Issue 3: https://github.com/ZCA/ZenPacks.community.f5/issues/4
.. _Issue 4: https://github.com/ZCA/ZenPacks.community.f5/issues/4
