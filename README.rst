=====================
ZenPacks.community.f5
=====================

.. contents::
   :depth: 3

Description
===========
Provides basic F5 BIG-IP monitoring and trending.

Additional Documentation
========================
Additional documentation including download links and installation instructions
can be found on this ZenPack's page on the 
`Zenoss Community Wiki <http://wiki.zenoss.org/ZenPack:F5_BIG-IP_(Open_Source)>`_


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

* NEXT

  * `Issue 3`_ - Properly detect model for Viprion B4300 as well as additional
    models not previously detected
  * `Issue 4`_ - Ensure BipIpUtils no longer appears as a modeler plugin
  * Removal of MIB files from ZenPack, to address unknowns around licensing 
    and/or distribution requirements
  * Documentation updates

Known Issues
============
* Currently the status of the virtual server component is only detected and
  set at model time. Its not a real time (or near real time) reflection of
  the state of the virtual server on the LTM


.. External References Below. Nothing Below This Line Should Be Rendered

.. _Route Domains: http://devcentral.f5.com/Tutorials/TechTips/tabid/63/articleType/ArticleView/articleId/353/v10--A-Look-at-Route-Domains.aspx

.. _Issue 3: https://github.com/ZCA/ZenPacks.community.f5/issues/4
.. _Issue 4: https://github.com/ZCA/ZenPacks.community.f5/issues/4
