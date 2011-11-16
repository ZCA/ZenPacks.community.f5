"""
Gather F5 LTM Node Information

@author: David Petzel
@date: 11/15/2011

"""
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
import re
import binascii
import string
import socket
from pprint import pprint

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
    
    snmpGetTableMaps = (
        #Virtual Server Table
        GetTableMap('ltmNodeAddrTable', '.1.3.6.1.4.1.3375.2.2.4.1.2', basecolumns),
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
                # Use socket to convert to octet based IP
                # http://docs.python.org/library/socket.html#socket.inet_ntoa
                om.ltmNodeAddrAddr = socket.inet_ntoa(om.ltmNodeAddrAddr)
                om.id = self.prepId(om.ltmNodeAddrAddr)
                om.snmpindex = oid
                rm.append(om)
        log.debug(rm)
        return [rm]        
        


    