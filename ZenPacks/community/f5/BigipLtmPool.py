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

class BigipLtmPool(DeviceComponent, ManagedEntity):
    """
    A class to represent a pool running on an LTM
    """
   
    portal_type = meta_type = "BigipLtmPool"
  
    ltmPoolName = ""
    ltmPoolActiveMemberCnt = 0
    ltmPoolMemberCnt = 0
    ltmPoolStatusAvailState = None
    ltmPoolStatusEnabledState = None
    ltmPoolStatusDetailReason = None
    
    _properties = (
        {'id': 'ltmPoolName', 'type': 'string', 'mode': ''},
        {'id': 'ltmPoolActiveMemberCnt', 'type': 'string', 'mode': ''},
        {'id': 'ltmPoolMemberCnt', 'type': 'string', 'mode': ''},
    )

    _relations = (
        ('Ltm', ToOne(ToManyCont,'ZenPacks.community.f5.BigipLtm', 'LtmPools')),
    )
    
    #This seems to be the bare minimum required to get the basic 
    #menu items in the component grid
    factory_type_information = (
    {
        'id': 'BigipLtmPool',
        'meta_type': 'BigipLtmPool',
        'description': 'LTM Pool Information',
        'product': 'f5',
        'immediate_view' : 'viewHistory',
        'actions'        : ()
    },
    )
    
    def device(self):
        return self.Ltm()
    
    def monitored(self):
        """
        If a LTM pool exists, we want to default to monitoring it.
        """ 
        return True
         
InitializeClass(BigipLtmPool)