"""
Gather F5 BIG-IP hardware model + serial number and other hardware information

@author: David Petzel
@date: 05/06/2011

"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
from Products.DataCollector.EnterpriseOIDs import EnterpriseOIDs

import re

from pprint import pprint

class BigipDeviceMap(SnmpPlugin):
    """
    Collects the basic hardware information about the Bigip
    """
    
    modname = "ZenPacks.community.f5.BigipLtm"
    
    snmpGetMap = GetMap({ 
        #'.1.3.6.1.4.1.674.10892.1.300.10.1.8' : 'manufacturer',
        '.1.3.6.1.4.1.3375.2.1.3.3.1.0' : 'sysGeneralHwName',
        '.1.3.6.1.4.1.3375.2.1.3.3.2.0' : 'setHWProductKey',
        '.1.3.6.1.4.1.3375.2.1.3.3.3.0' : 'setHWSerialNumber',
        #'.1.3.6.1.4.1.674.10892.1.400.10.1.6.1': 'setOSProductKey',
        # Collect some info to build the setOSProductKey string later
        '.1.3.6.1.2.1.1.2.0': 'sysObjectID',
        '.1.3.6.1.4.1.3375.2.1.4.1.0': 'sysProductName',
        '.1.3.6.1.4.1.3375.2.1.4.2.0': 'sysProductVersion',
        '.1.3.6.1.4.1.3375.2.1.4.3.0': 'sysProductBuild',
        '.1.3.6.1.4.1.3375.2.1.4.4.0': 'sysProductEdition',
         })
    #There has got to be a better way to do this... But I couldn't 
    #figure it out. sysObjectID is going to give us an OID that represents
    #the model of the device. However in the testing I did (with very limited
    #number of devices, the OID isn't actually queryably, nor could I walk
    # That section to build a list. So in a nutshell I'm manually re-creating
    # .1.3.6.1.4.1.3375.2.1.3.4 (sysDeviceModelOIDs) just so I can lookup
    # The value returned in sysObjectID. Seems redundant and wrong, but I
    # Couldnt come up with something else.
    
    model_oids_base = ".1.3.6.1.4.1.3375.2.1.3.4."
    sysDeviceModelOIDs = {
       '1': 'bigip520',
       '2': 'bigip540',
       '3': 'bigip1000',
       '4': 'bigip1500',
       '5': 'bigip2400',
       '6': 'bigip3400',
       '7': 'bigip4100',
       '8': 'bigip5100',
       '9': 'bigip5110',
       '10': 'bigip6400',
       '11': 'bigip6800',
       '12': 'bigip8400',
       '13': 'bigip8800',
       '14': 'em3000',
       '15': 'wj300',
       '16': 'wj400',
       '17': 'wj500',
       '18': 'wj800',
       '19': 'bigipVIPRION',
       '20': 'bigip1600',
       '21': 'bigip3600',
       '22': 'bigip6900',
       '23': 'bigip8900',
       '1000': 'unknown',
    }
    

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        print results
        getdata, tabledata = results
        #if getdata['setHWProductKey'] is None: return None
        om = self.objectMap(getdata)
        #Attempt to determine the registered manufacturer from snmp oid
        #If we cant find a registered name, assign it an identifiable default
        if om.sysObjectID:
            match = re.match(r'(.\d+){7}', om.sysObjectID)
            if match:
                manufacturer = EnterpriseOIDs.get(match.group(0), 
                                                  'F5 Labs, Inc.')
            else:
                manufacturer = None
            #Drop the OID base, so we are left with the index number
            model_index = om.sysObjectID.replace(self.model_oids_base,"")
            device_model = self.sysDeviceModelOIDs.get(model_index, 'unknown')
            
            #Now Attempt to Locate the Model Number
            #snmpGetDeviceModelOid = GetMap({om.sysObjectID: 'sysDeviceModel'})
            #print snmpGetDeviceModelOid.oidmap
            #print self.objectMap(snmpGetDeviceModelOid.oidmap)
            #print dir(snmpGetDeviceModelOid)

        # Build a product build and version string to populate the OSModel field
        # Also set the manufacturer_name
        os_model = " ".join([om.sysProductName, om.sysProductVersion, om.sysProductBuild, om.sysProductEdition])
        om.setOSProductKey = MultiArgs(os_model, manufacturer)
        
        if device_model == "unknown":
            #See if we can figure anything out
            
            #http://www.rootong.com/blog/?tag=installation+bigip+f5+ltm+gtm+tmm
            #http://support.f5.com/content/dam/f5/kb/global/solutions/sol10288_images.html/BIG-IP_Product_Matrix.pdf
            if om.setHWProductKey == "Z100":
                device_model = "bigipVE"
            elif om.setHWProductKey == "Z99":
                device_model = "bigipVE - Trial Edition"
            else:
                #unknown is too vague.. since this value
                #could get registered as a product, make it unique enough
                device_model = "Unknown F5 Device"
                
        #When we collect the model, VIPRIONs don't generally get classified
        # to the model. Lets further clarify the type of Viprion
        if device_model == self.sysDeviceModelOIDs['19']:
            if om.setHWProductKey == "J10x":
                device_model = device_model + " 4400"
            if om.setHWProductKey == "A103":
                device_model = device_model + " 2400"
        
            
        # Now set it. I'm not entirely up to speed on this method, 
        # But in testing the multiargs stuff will populate two fields in the GUI
      
        om.setHWProductKey = MultiArgs(device_model, manufacturer)
        return om
