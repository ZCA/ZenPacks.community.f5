
import Globals
import os.path
from Products.ZenModel.ZenPack import ZenPackBase
import logging

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

#Create a logger in the "zen" namespace. Creating it as a child of zen
#Ensures we inherit existing logging configuration. We then append the zenpack
#name to create a unique logger
log = logging.getLogger('.'.join(['zen', __name__]))


class ZenPack(ZenPackBase):
    """
    F5 BigIP Loader
    """
    
    #A List of Custom zProperties To Add
    packZProperties = [
                       ('zF5BigipVirtualServerNameFilter', '', 'string'),
                       ('zF5BigipPoolsNameFilter', '', 'string'),
                       ('zF5BigipNodesNameFilter', '', 'string'),
                       ]
    
    def install(self, app):
        """
        F5 BigIP device class, plugins, etc
        """
        f5 = app.dmd.Devices.createOrganizer('/Network/f5')
        # Set snmp version to 2c
        f5.setZenProperty('zSnmpVer', 'v2c')
        
        # Build a list of modeler plugins that we want to apply to our new device class
        plugins=['zenoss.snmp.DeviceMap', 'zenoss.snmp.NewDeviceMap',
                 'BigipLtmVirtualServerMap', 'BigipDeviceMap',
                 'BigipLtmPoolMap', 'BigipLtmNodeMap']
        
        # Apply the list of plugins to the device class. This will overwrite whats there, not append
        f5.setZenProperty('zCollectorPlugins', plugins)
        
        # Register our device class file, with the new device class
        f5.setZenProperty('zPythonClass', 'ZenPacks.community.f5.BigipLtm')
        ZenPackBase.install(self, app)
        #Rebuild Relationships
        self._rebuild_device_relationships(f5)
        
    def _rebuild_device_relationships(self, dev_org):
        log.info("Rebuilding relationships for existing devices in %s", dev_org.getPrimaryDmdId())
        for dev in self.dmd.Devices.getSubDevices():
            log.debug("Rebuilding relationships on %s", dev.id)
            dev.buildRelations()
            
        