"""
Gather F5 LTM Node Information

@author: David Petzel
@date: 11/15/2011

"""
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
import re

from BigIpUtils import unpack_address_to_string
from BigIpUtils import avail_status_values, enable_state_values

class BigipLtmNodeMap(SnmpPlugin):
    """
    Handles the modeling of Pools on the LTM
    
    Custom Properties Added:
    zF5BigipNodesNameFilter - This will provide a list of regex strings to compare
        the node name against. Only items that match will be returned.
        When left blank all nodes will be returned
    
    """
    relname = "LtmNodes"
    modname = "ZenPacks.community.f5.BigipLtmNode"
    deviceProperties = SnmpPlugin.deviceProperties + ('zF5BigipNodesNameFilter',)
   
    # Column dictionaries represent the OID ending for the data point your interested in.
    # This value gets appended to the base issue listed in the snmpGetTableMaps call
    basecolumns = {

        '.1.2': 'ltmNodeAddrAddr',
        '.1.12': 'ltmNodeAddrScreenName',
    }
    # The node Status is provided from a separate table
    status_columns = {
        '.1.3': 'ltmNodeAddrStatusAvailState',
        '.1.4': 'ltmNodeAddrStatusEnabledState',
        '.1.6': 'ltmNodeAddrStatusDetailReason',       
    }
    
    snmpGetTableMaps = (
        #Virtual Server Table
        GetTableMap('ltmNodeAddrTable', '.1.3.6.1.4.1.3375.2.2.4.1.2', basecolumns),
        GetTableMap('ltmNodeStatusTable', '.1.3.6.1.4.1.3375.2.2.4.3.2', status_columns)
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
        
        ltmnode_table = tabledata.get("ltmNodeAddrTable")
        
        # Grab the second table and append it to the first
        status_table = tabledata.get("ltmNodeStatusTable")
        for oid, data in status_table.items():
            for key, value in data.items():
                if key not in ltmnode_table[oid]:
                    ltmnode_table[oid][key] = value
        
        maps = []
        rm = self.relMap()
        # Get the list of name patterns to search for
        node_name_filter = getattr(device, 'zF5BigipNodesNameFilter', None)
        log.debug("Picked up Filter List of: %s" , node_name_filter)
        for oid, data in ltmnode_table.items():
        #    log.debug("%s : %s\n", oid, data)
        #
            om = self.objectMap(data)
            binclude = True
            if node_name_filter != None and node_name_filter != "":
                # If there is a regex filter supplied, lets use it
                if re.search(node_name_filter, om.ltmNodeAddrScreenName) == None:
                    binclude = False
            if binclude == True:
                # The value fetched is a packed hex representation of the IP
                # Try and unpack the address, and check if route_domains
                # are in use
                address, route_domain = unpack_address_to_string(oid, 
                                                            om.ltmNodeAddrAddr)
                if address != "":
                    om.ltmNodeAddrAddr = address
                if route_domain != "":
                    om.ltmNodeAddrRouteDomain = route_domain
                om.id = self.prepId(om.ltmNodeAddrAddr)
                om.snmpindex = oid

                om.ltmNodeAddrStatusEnabledState = \
                        enable_state_values[om.ltmNodeAddrStatusEnabledState]
                om.ltmNodeAddrStatusAvailState = \
                            avail_status_values[om.ltmNodeAddrStatusAvailState]
                rm.append(om)
        log.debug(rm)
        return [rm]        
        


    