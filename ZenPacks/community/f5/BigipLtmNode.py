"""
BigIP Pool Component
"""

import Globals
from Globals import InitializeClass
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from copy import deepcopy

class BigipLtmNode(DeviceComponent, ManagedEntity):
    """
    A class to represent a pool running on an LTM
    """
   
    portal_type = meta_type = "BigipLtmNode"
    
    ltmNodeAddrAddr = None
    ltmNodeAddrScreenName = None
    ltmNodeAddrRouteDomain = None
    ltmNodeAddrStatusAvailState = None
    ltmNodeAddrStatusEnabledState = None
    ltmVsStatusDetailReason = None
    
    _properties = (
        {'id': 'ltmNodeName', 'type': 'string', 'mode': ''},
    )

    _relations = (
        ('Ltm', ToOne(ToManyCont,'ZenPacks.community.f5.BigipLtm', 'LtmNodes')),
    )

    #This seems to be the bare minimum required to get the basic 
    #menu items in the component grid
    factory_type_information = (
    {
        'id': 'BigipLtmNode',
        'meta_type': 'BigipLtmNode',
        'description': 'LTM Node Information',
        'product': 'f5',
        'immediate_view' : 'graphs',
        'actions'        : ()
    },
    )
    
    def device(self):
        return self.Ltm()
    
    def monitored(self):
        """
        If a LTM Node exists, we want to default to monitoring it.
        """ 
        return True
  
         
InitializeClass(BigipLtmNode)