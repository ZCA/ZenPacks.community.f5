===========================
ZenPacks.community.f5 Change Log
===========================

* 1.8

  * Initial support for OneConnect Profiles as a device component

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













