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

class BigipLtmConnPoolProfile(DeviceComponent, ManagedEntity):
    """
    A class to represent a pool running on an LTM
    """
   
    portal_type = meta_type = "BigipLtmConnPoolProfile"
    
    LtmConnPoolProfileNumber = None
    LtmConnPoolProfileName = None
    LtmConnPoolProfileConfigSource = None
    LtmConnPoolProfileDefaultName = None
    LtmConnPoolProfileSrcMaskType = None
    LtmConnPoolProfileSrcMask = None
    LtmConnPoolProfileMaxSize = None
    LtmConnPoolProfileMaxAge = None
    LtmConnPoolProfileMaxReuse = None
    LtmConnPoolProfileIdleTimeout = None
    
    _properties = (
        {'id': 'LtmConnPoolProfileName', 'type': 'string', 'mode': ''},
        {'id': 'LtmConnPoolProfileMaxSize', 'type': 'string', 'mode': ''},
        {'id': 'LtmConnPoolProfileMaxAge', 'type': 'string', 'mode': ''},
        {'id': 'LtmConnPoolProfileMaxReuse', 'type': 'string', 'mode': ''},
        {'id': 'LtmConnPoolProfileIdleTimeout', 'type': 'string', 'mode': ''},
    )

    _relations = (
        ('Ltm', ToOne(ToManyCont,'ZenPacks.community.f5.BigipLtm', 'LtmConnPoolProfiles')),
    )

    #This seems to be the bare minimum required to get the basic 
    #menu items in the component grid
    factory_type_information = (
    {
        'id': 'BigipLtmConnPoolProfile',
        'meta_type': 'BigipLtmConnPoolProfile',
        'description': 'OneConnect Profile Information',
        'product': 'f5',
        'immediate_view' : 'graphs',
        'actions'        : ()
    },
    )
    
    def device(self):
        return self.Ltm()
    
    def monitored(self):
        """
        If a Profile exists, we want to default to monitoring it.
        """ 
        return True
  
         
InitializeClass(BigipLtmConnPoolProfile)