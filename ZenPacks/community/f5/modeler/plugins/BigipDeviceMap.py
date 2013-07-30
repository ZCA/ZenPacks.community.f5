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
        '.1.3.6.1.4.1.3375.2.1.3.5.2.0': 'sysPlatformInfoMarketingName',
         })
    
    def _determine_device_model(self, om):
        """
        Use a series of increasing hackery to attempt to determine the device
        model. We are going to start with "easy" methods, and if we can't
        get it that way (as is the case on many older devices and software
        versions) we will restored to increasing nastiness..
        """
        device_model = "Unknown F5 Device"
        if om.sysPlatformInfoMarketingName is not None:
            device_model = om.sysPlatformInfoMarketingName
        else:
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
               '19': 'bigipViprionPb200', # Not the default, tweaked for readability
               '20': 'bigip1600',
               '21': 'bigip3600',
               '22': 'bigip6900',
               '23': 'bigip8900',
               '24': 'bigip3900',
               '25': 'bigip8950',
               '26': 'em4000',
               '27': 'bigip11050',
               '28': 'em500',
               '29': 'arx1000',
               '30': 'arx2000',
               '31': 'arx4000',
               '32': 'arx500',
               '33': 'bigip3410',
               '34': 'bigipViprionPb100', # Not the default, tweaked for readability
               '35': 'bigipViprionPb100n', # Not the default, tweaked for readability
               '36': 'sam4300',
               '37': 'firepass1200',
               '38': 'firepass4100',
               '39': 'firepass4300',
               '40': 'swanWJ200',
               '41': 'TrafficShield4100',
               '42': 'wa4500',
               '43': 'bigipVirtualEdition',
               '44': 'bigip11000',
               '45': 'bigip11050N',
               '46': 'bigipViprionB2100',
               '47': 'bigipViprionB4300',
               '48': 'bigipViprionC2400',
               '49': 'arx1500',
               '50': 'arx2500',
               '51': 'bigip11000F',
               '52': 'bigip11050F',
               '53': 'bigip6900F',
               '54': 'bigip6900N',
               '55': 'bigip6900S',
               '56': 'bigip8900F',
               '57': 'bigip8950S',
               '58': 'bigipViprion200N',# Not the default, tweaked for readability
               '1000': 'unknown',
            }
            #Drop the OID base, so we are left with the index number
            model_index = om.sysObjectID.replace(model_oids_base,"")
            device_model = sysDeviceModelOIDs.get(model_index, 
                                                       'unknown')
            
            if device_model == "unknown":
                #See if we can figure anything out
                
                # http://www.rootong.com/blog/?tag=installation+bigip+f5+ltm+gtm+tmm
                if om.setHWProductKey == "Z100":
                    device_model = sysDeviceModelOIDs['43']
                elif om.setHWProductKey == "Z99":
                    device_model = "{0} - Trial Edition".format(sysDeviceModelOIDs['43'])
                #To make things more fun, there is an issue on Viprions.
                #http://support.f5.com/kb/en-us/solutions/public/10000/600/sol10635.html
                #http://support.f5.com/kb/en-us/solutions/public/11000/400/sol11441.html
                # This results in om.setHWProductKey and om.sysObjectID coming back as 
                #unknown....Lets try to work around that
                elif om.setHWProductKey == "unknown":
                    #These numbers are from the second link above
                    if om.sysGeneralHwName == 'A100':
                        device_model = sysDeviceModelOIDs['34']
                    elif om.sysGeneralHwName == 'A107':
                        device_model = sysDeviceModelOIDs['19']
                else:
                    #unknown is too vague.. since this value
                    #could get registered as a product, make it unique enough
                    device_model = "Unknown F5 Device"
                    
            # When we collect the model, VIPRIONs don't generally get classified
            # to the model. Lets further clarify the type of Viprion.
            # This is again using the platform codes listed in 
            # http://support.f5.com/content/dam/f5/kb/global/solutions/sol10288_images.html/big-ip-product-matrix-v35.pdf
            if device_model == sysDeviceModelOIDs['19']:
                if om.setHWProductKey == "A103":
                    device_model = device_model + " B2100"
                elif om.setHWProductKey == "A107":
                    device_model = device_model + " B4200"
                if om.setHWProductKey == "A108":
                    device_model = device_model + " B4300"
                elif om.setHWProductKey == "J10x":
                    device_model = device_model + " B4100"
        return device_model
        
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
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
            
        device_model = self._determine_device_model(om)
            

        # Build a product build and version string to populate the OSModel field
        # Also set the manufacturer_name
        os_model = " ".join([om.sysProductName, om.sysProductVersion, 
                             om.sysProductBuild, om.sysProductEdition])
        om.setOSProductKey = MultiArgs(os_model, manufacturer)
        
            
        # Now set it. I'm not entirely up to speed on this method, 
        # But in testing the multiargs stuff will populate two fields in the GUI
      
        om.setHWProductKey = MultiArgs(device_model, manufacturer)
        return om
