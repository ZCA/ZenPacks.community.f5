"""
Gather F5 LTM OneConnect Profile Information

@author: David Petzel
@date: 09/06/2013

"""
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class BigipLtmConnPoolProfileMap(SnmpPlugin):
    """
    Handles the modeling of OneConnect Profiles on the LTM
    
    """
    relname = "LtmConnPoolProfiles"
    modname = "ZenPacks.community.f5.BigipLtmConnPoolProfile"
   
    # Column dictionaries represent the OID ending for the data point your interested in.
    # This value gets appended to the base issue listed in the snmpGetTableMaps call
    basecolumns = {

        '.1.1': 'LtmConnPoolProfileName',
        '.1.2': 'LtmConnPoolProfileConfigSource',
        '.1.3': 'LtmConnPoolProfileDefaultName',
        '.1.4': 'LtmConnPoolProfileSrcMaskType',
        '.1.5': 'LtmConnPoolProfileSrcMask',
        '.1.6': 'LtmConnPoolProfileMaxSize',
        '.1.7': 'LtmConnPoolProfileMaxAge',
        '.1.8': 'LtmConnPoolProfileMaxReuse',
        '.1.9': 'LtmConnPoolProfileIdleTimeout',
    }
   
    snmpGetTableMaps = (
        #Virtual Server Table
        GetTableMap('LtmConnPoolProfileTable', '.1.3.6.1.4.1.3375.2.2.6.4.1.2', basecolumns),
    )

    def condition(self, device, log):
        """
        """
        return True
   
    
    def process(self, device, results, log):
        """
        Process the fetched results
        """
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        
        data_table = tabledata.get("LtmConnPoolProfileTable")
        
        maps = []
        rm = self.relMap()

        for oid, data in data_table.items():
            om = self.objectMap(data)

            om.id = self.prepId(om.LtmConnPoolProfileName)
            om.snmpindex = oid
            rm.append(om)
        log.debug(rm)
        return [rm]        
        


    