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
See the `Change Log <https://github.com/ZCA/ZenPacks.community.f5/blob/master/CHANGELOG.rst>`_
for a detailed change history

Known Issues
============
* Currently the status of the virtual server component is only detected and
  set at model time. Its not a real time (or near real time) reflection of
  the state of the virtual server on the LTM


.. External References Below. Nothing Below This Line Should Be Rendered

.. _Route Domains: http://devcentral.f5.com/Tutorials/TechTips/tabid/63/articleType/ArticleView/articleId/353/v10--A-Look-at-Route-Domains.aspx

.. _Issue 3: https://github.com/ZCA/ZenPacks.community.f5/issues/4
.. _Issue 4: https://github.com/ZCA/ZenPacks.community.f5/issues/4
