"""
Gather F5 LTM Virtual Server Information

@author: David Petzel
@date: 05/06/2011

"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
import re

from BigIpUtils import unpack_address_to_string
from BigIpUtils import avail_status_values, enable_state_values

class BigipLtmVirtualServerMap(SnmpPlugin):
    """
    Handles the modeling of Virtual Servers on the LTM
    
    Custom Properties Added:
    zVirtualServerNameFilter - This will provide a list of regex strings to compare
        the virtual server name against. Only items that match will be returned.
        When left blank all virtual servers will be returned
    
    """
    relname = "LtmVs"
    modname = "ZenPacks.community.f5.BigipVirtualServer"
    deviceProperties = SnmpPlugin.deviceProperties + ('zF5BigipVirtualServerNameFilter',)
   
    # Column dictionaries represent the OID ending for the data point your interested in.
    # This value gets appended to the base issue listed in the snmpGetTableMaps call
    basecolumns = {
        '.1.1': 'ltmVirtualServName',
        '.1.3': 'ltmVirtualServAddr',
        '.1.6': 'ltmVirtualServPort',
    }
    # The VIP Status is provided from a separate table
    status_columns = {
        '.1.1': 'ltmVsStatusName',
        '.1.2': 'ltmVsStatusAvailState',
        '.1.3': 'ltmVsStatusEnabledState',
        '.1.5': 'ltmVsStatusDetailReason',       
    }
    
    
    snmpGetTableMaps = (
        #Virtual Server Table
        GetTableMap('ltmVirtualServTable', '.1.3.6.1.4.1.3375.2.2.10.1.2', basecolumns),
        GetTableMap('ltmVsStatusTable', '.1.3.6.1.4.1.3375.2.2.10.13.2', status_columns)
    )

    
    
    def process(self, device, results, log):
        """
        Just as it sounds
        """
        
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        
        vs_table = tabledata.get("ltmVirtualServTable")
        
        # Grab the second table and append it to the first
        status_table = tabledata.get("ltmVsStatusTable")
        for oid, data in status_table.items():
            for key, value in data.items():
                if key not in vs_table[oid]:
                    vs_table[oid][key] = value
                
        maps = []
        rm = self.relMap()
        # Get the list of name patterns to search for
        VirtualServerNameFilter = getattr(device, 'zF5BigipVirtualServerNameFilter', None)
        log.debug("Picked up Filter List of: %s" , VirtualServerNameFilter)
        for oid, data in vs_table.items():
        #    log.debug("%s : %s\n", oid, data)
        #
            om = self.objectMap(data)
            include_vs = True
            if VirtualServerNameFilter != None and VirtualServerNameFilter != "":
                # If there is a regex filter supplied, lets use it
                if re.search(VirtualServerNameFilter, om.ltmVirtualServName) == None:
                    include_vs = False
            if include_vs == True:
                om.id = self.prepId(om.ltmVirtualServName)
                om.snmpindex = oid
                
                # The value fetched is a packed hex representation of the IP
                # Try and unpack the address, and check if route_domains
                # are in use
                address, route_domain = unpack_address_to_string(oid, 
                                                        om.ltmVirtualServAddr)
                if address != "":
                    om.vsIP = address
                if route_domain != "":
                    om.ltmVirtualServAddrRouteDomain = route_domain

                om.VsStatusEnabledState = enable_state_values[om.ltmVsStatusEnabledState]
                om.VsStatusAvailState = avail_status_values[om.ltmVsStatusAvailState]
                om.VsStatusDetailReason = om.ltmVsStatusDetailReason
                rm.append(om)
        #log.debug(rm)
        return [rm]        
        


    