"""
"""

from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IBigipVirtualServerInfo(IComponentInfo):
    """
    Info adapter for BigipVirtualServer components.
    """
    vsIP = schema.Text(title=u"IP Address", readonly=True, group='Details')
    ltmVirtualServPort = schema.Text(title=u"Port", readonly=True, group='Details')
    VsStatusAvailState = schema.Text(title=u"Availability Status", readonly=True, group='Details')
    VsStatusEnabledState = schema.Text(title=u"Enabled/Disabled", readonly=True, group='Details')
    VsStatusDetailReason = schema.Text(title=u"Status Details", readonly=True, group='Details')
    ltmVirtualServAddrRouteDomain = schema.Text(title=u"route-domain", readonly=True, group='Details')
    
class IBigipLtmPoolInfo(IComponentInfo):
    """
    Info adapter for BigipVirtualServer components.
    """
    name = schema.Text(title=u"Pool Name", readonly=True, group='Details')
    ltmPoolActiveMemberCnt = schema.Text(title=u"Active Members", readonly=True, group='Details')
    ltmPoolMemberCnt = schema.Text(title=u"Total Members", readonly=True, group='Details')
    ltmPoolStatusEnabledState = schema.Text(title=u"Enabled/Disabled", readonly=True, group='Details')
    ltmPoolStatusAvailState = schema.Text(title=u"Availability Status", readonly=True, group='Details')
    ltmPoolStatusDetailReason = schema.Text(title=u"Status Details", readonly=True, group='Details')
    
class IBigipLtmNodeInfo(IComponentInfo):
    """
    Info adapter for BigipVirtualServer components.
    """
    ltmNodeAddrAddr = schema.Text(title=u"IP Address", readonly=True, group='Details')
    ltmNodeAddrScreenName = schema.Text(title=u"Screen Name", readonly=True, group='Details')
    ltmNodeAddrRouteDomain = schema.Text(title=u"route-domain", readonly=True, group='Details')
    ltmNodeAddrStatusEnabledState = schema.Text(title=u"Enabled/Disabled", readonly=True, group='Details')
    ltmNodeAddrStatusAvailState = schema.Text(title=u"Availability Status", readonly=True, group='Details')
    ltmNodeAddrStatusDetailReason = schema.Text(title=u"Status Details", readonly=True, group='Details')
