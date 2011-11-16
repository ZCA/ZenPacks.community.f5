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
    
    _properties = (
        {'id': 'ltmNodeName', 'type': 'string', 'mode': ''},
    )

    _relations = (
        ('Ltm', ToOne(ToManyCont,'ZenPacks.community.f5.BigipLtm', 'LtmNodes')),
    )

    factory_type_information = (
    {
        'id': 'BigipLtmNode',
        'meta_type': 'BigipLtmNode',
        'description': 'LTM Node Information',
        'product': 'f5',
        'immediate_view' : 'graphs',
        'actions'        : (
           # This populates the Dropdown box when viewing virtual servers.
           # Via some magic I don't yet understand, events and details are
           # In the menu without interaction. However The following is needed
           # to add graphs as a menu option. This leverages a native skin
           # And we don't need to provide our own.
           # { 'id'            : 'graphs'
           # , 'name'          : 'Graphs'
           # , 'action'        : 'graphs'
           # , 'permissions'   : (ZEN_VIEW, )
           # },
            # Lets also enable modification history, just cause we can
            # Again this is a default skin, and not one this pack is providing.
            { 'id'            : 'viewHistory'
            , 'name'          : 'Modifications'
            , 'action'        : 'viewHistory'
            , 'permissions'   : (ZEN_VIEW, )
            },
        )
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