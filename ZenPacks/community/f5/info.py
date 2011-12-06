"""
"""

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
#from Products.ZenUtils.Utils import convToUnits
from ZenPacks.community.f5 import interfaces

class BigipLtmPoolInfo(ComponentInfo):
    implements(interfaces.IBigipLtmPoolInfo)
    ltmPoolActiveMemberCnt = ProxyProperty("ltmPoolActiveMemberCnt")
    ltmPoolMemberCnt = ProxyProperty("ltmPoolMemberCnt")
    ltmPoolStatusAvailState = ProxyProperty("ltmPoolStatusAvailState")
    ltmPoolStatusEnabledState = ProxyProperty("ltmPoolStatusEnabledState")
    ltmPoolStatusDetailReason = ProxyProperty("ltmPoolStatusDetailReason")
    
class BigipLtmNodeInfo(ComponentInfo):
    implements(interfaces.IBigipLtmNodeInfo)
    ltmNodeAddrAddr = ProxyProperty("ltmNodeAddrAddr")
    ltmNodeAddrScreenName = ProxyProperty("ltmNodeAddrScreenName")
    ltmNodeAddrRouteDomain = ProxyProperty("ltmNodeAddrRouteDomain")
    ltmNodeAddrStatusAvailState = ProxyProperty("ltmNodeAddrStatusAvailState")
    ltmNodeAddrStatusEnabledState = ProxyProperty("ltmNodeAddrStatusEnabledState")
    ltmNodeAddrStatusDetailReason = ProxyProperty("ltmNodeAddrStatusDetailReason")
    
class BigipVirtualServerInfo(ComponentInfo):
    implements(interfaces.IBigipVirtualServerInfo)
    
    vsIP = ProxyProperty("vsIP")
    ltmVirtualServPort = ProxyProperty("ltmVirtualServPort")
    ltmVirtualServAddrRouteDomain = ProxyProperty("ltmVirtualServAddrRouteDomain")
    VsStatusAvailState = ProxyProperty("VsStatusAvailState")
    VsStatusEnabledState = ProxyProperty("VsStatusEnabledState")
    VsStatusDetailReason = ProxyProperty("VsStatusDetailReason")
