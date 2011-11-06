# ZenPacks.community.f5
## Description
Provides basic F5 BIG-IP monitoring.  
** NOTE: This is my first attempt at writing a ZenPack, so *PLEASE* install on 
a test system first. I've done enough testing to think its ready to share with 
a larger audience, but since its my first attempt, I'd appreciate caution when 
installing as well as feedback.

## Screenshots
![Device Details](https://github.com/zenoss/ZenPacks.community.f5/raw/master/screenshots/zenoss_bigip_DeviceDetails.png)  
![Virtual Server Components](https://github.com/zenoss/ZenPacks.community.f5/raw/master/screenshots/zenoss_bigip_vs_component.png)

## Components
The ZenPack has the following:  

 * Network/f5 Device Class
 * A Device template which graphs many of the same performance stats as would be seen in the Overview >> Performance section of the 10.x UI
 * Virtual servers are represented as components of the device, and like all components are automatically discovered when the device is modeled.
 * A component template for virtual servers.  
 * Virtual Server filtering. This pack adds a new zProperty, *zF5BigipVirtualServerNameFilter*, which when set will limit which virtual servers are included during a modeling event.  

## Requirements
 * Zenoss Versions Supported: 3.0+
 * External Dependencies: None
 * ZenPack Dependencies: None
 * Configuration: No Special configuration should be necessary.

## Installation
### Normal Installation (packaged egg)
Download the appropriate package for your Zenoss version from the list
below.
 * Zenoss 3.0+ [Latest Package for Python 2.6][]
Then copy it to your Zenoss server and run the following commands as the zenoss
user.

    zenpack --install <package.egg>
    zenoss restart
If you don't want to do a full restart, you should be able to just restart
zenhub and zopectl.

	zenhub restart &&  zopectl restart

### Developer Installation (link mode)
If you wish to further develop and possibly contribute back to the f5
ZenPack you should clone the git repository, then install the ZenPack in
developer mode using the following commands.

    git clone git://github.com/zenoss/ZenPacks.community.f5.git
    zenpack --link --install ZenPacks.community.f5
    zenoss restart

## Change History
 * 0.82
  * Initial Release
 * 1.0
  * Improved device detection. Should have no more "deprecated" values for 
  hardware model 
  * Minor updates to support segrated github repos and README.markdown
  * Including zenoss.snmp.DeviceMap & zenoss.snmp.NewDeviceMap plugins on the 
  newly created device class so that the base SNMP attributes are collected

## Known Issues
 *  Currently the status of the virtual server component is only detected and 
 	set at model time. Its not a real time (or near real time) reflection of 
 	the state of the virtual server on the LTM
 	
[Latest Package for Python 2.6]: <https://github.com/downloads/zenoss/ZenPacks.community.f5/ZenPacks.community.f5-1.0-py2.6.egg>