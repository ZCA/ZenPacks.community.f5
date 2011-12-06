"""
BigIP LTM Device
"""

import Globals
from Globals import InitializeClass
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from copy import deepcopy

class BigipVirtualServer(DeviceComponent, ManagedEntity):
    """
    A class to represent a virtual server running on an LTM
    """
   
    portal_type = meta_type = "BigipVirtualServer"
    
    ltmVirtualServName = "DefaultVirtualServer"
    vsIP = "000.000.000.000"
    ltmVirtualServPort = 0
    VsStatusAvailState = None
    VsStatusEnabledState = None
    VsStatusDetailReason = None
    
    ltmVsStatusName = None
    ltmVsStatusEnabledState = None
    ltmVsStatusAvailState = None
    ltmVirtualServAddr = None
    ltmVsStatusDetailReason = None
    ltmVirtualServAddrRouteDomain = None
    
    _properties = (
        {'id': 'ltmVirtualServName', 'type': 'string', 'mode': ''},
        {'id': 'vsIP', 'type': 'string', 'mode': ''},
        {'id': 'ltmVirtualServPort', 'type': 'integer', 'mode': ''},
    )

    _relations = (
        ('Ltm', ToOne(ToManyCont,'ZenPacks.community.f5.BigipLtm', 'LtmVs')),
    )

    #This seems to be the bare minimum required to get the basic 
    #menu items in the component grid
    factory_type_information = (
    {
        'id': 'BigipVirtualServer',
        'meta_type': 'BigipVirtualServer',
        'description': 'Virtual Server Information',
        'product': 'f5',
        'immediate_view' : 'graphs',
        'actions'        : ()
    },
    )

    def device(self):
        return self.Ltm()
    
    def monitored(self):
        """
        If a virtual server exists, we want to default to monitoring it.
        """ 
        return True
        
InitializeClass(BigipVirtualServer)