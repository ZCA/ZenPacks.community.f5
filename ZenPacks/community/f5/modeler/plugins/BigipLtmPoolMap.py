"""
Gather F5 LTM Pool Information

@author: David Petzel
@date: 11/13/2011

"""
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
import re
from BigIpUtils import avail_status_values, enable_state_values

class BigipLtmPoolMap(SnmpPlugin):
    """
    Handles the modeling of Pools on the LTM
    
    Custom Properties Added:
    zF5BigipPoolsNameFilter - This will provide a list of regex strings to compare
        the pool name against. Only items that match will be returned.
        When left blank all pools will be returned
    
    """
    relname = "LtmPools"
    modname = "ZenPacks.community.f5.BigipLtmPool"
    deviceProperties = SnmpPlugin.deviceProperties + ('zF5BigipPoolsNameFilter',)
   
    # Column dictionaries represent the OID ending for the data point your interested in.
    # This value gets appended to the base issue listed in the snmpGetTableMaps call
    basecolumns = {

        '.1.1': 'ltmPoolName',
        '.1.8': 'ltmPoolActiveMemberCnt',
        '.1.23': 'ltmPoolMemberCnt',
    }
    # The pool Status is provided from a separate table
    status_columns = {
        '.1.2': 'ltmPoolStatusAvailState',
        '.1.3': 'ltmPoolStatusEnabledState',
        '.1.5': 'ltmPoolStatusDetailReason',       
    }
    
    snmpGetTableMaps = (
        #Virtual Server Table
        GetTableMap('ltmPoolTable', '.1.3.6.1.4.1.3375.2.2.5.1.2', basecolumns),
        GetTableMap('ltmPoolStatusTable', '.1.3.6.1.4.1.3375.2.2.5.5.2', status_columns)
    )

    def condition(self, device, log):
        """
        Only model pools if someone told us to.
        By default we won't, but if someone has enabled pool
        modeling, than do it
        """
        return True
            
            
    
    
    def process(self, device, results, log):
        """
        Process the fetched results
        """
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        
        ltmpool_table = tabledata.get("ltmPoolTable")
        
        # Grab the second table and append it to the first
        status_table = tabledata.get("ltmPoolStatusTable")
        for oid, data in status_table.items():
            for key, value in data.items():
                if key not in ltmpool_table[oid]:
                    ltmpool_table[oid][key] = value
        
        maps = []
        rm = self.relMap()
        # Get the list of name patterns to search for
        pool_name_filter = getattr(device, 'zF5BigipPoolsNameFilter', None)
        log.debug("Picked up Filter List of: %s" , pool_name_filter)
        for oid, data in ltmpool_table.items():
        #    log.debug("%s : %s\n", oid, data)
        #
            om = self.objectMap(data)
            binclude = True
            if pool_name_filter != None and pool_name_filter != "":
                # If there is a regex filter supplied, lets use it
                if re.search(pool_name_filter, om.ltmPoolName) == None:
                    binclude = False
            if binclude == True:
                om.id = self.prepId(om.ltmPoolName)
                om.snmpindex = oid
                om.ltmPoolStatusEnabledState = \
                        enable_state_values[om.ltmPoolStatusEnabledState]
                om.ltmPoolStatusAvailState = \
                            avail_status_values[om.ltmPoolStatusAvailState]
                rm.append(om)
        log.debug(rm)
        return [rm]        
        


    