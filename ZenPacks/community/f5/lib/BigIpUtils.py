"""
A utility class for functions that are common across modelers
Created on Dec 5, 2011
@author: David Petzel
"""

import socket
import logging

log = logging.getLogger('.'.join(['zen', __name__]))

#Types are lifted from http://www.net-snmp.org/docs/mibs/INET-ADDRESS-MIB.txt
ADDR_TYPE_UNKNOWN = "0"
ADDR_TYPE_IPV4 = "1"
ADDR_TYPE_IPV6 = "2"
ADDR_TYPE_IPV4Z = "3"
ADDR_TYPE_IPV6Z = "4"
ADDR_TYPE_DNS = "16"

#The various availability states indicated in color as lifted from MIB.
avail_status_values = {
        0: 'None - Error',
        1: 'Green - available in some capacity',
        2: 'Yellow - not currently available',
        3: 'Red - not available',
        4: 'Blue - availability is unknown',
        5: 'Gray - unlicensed',
    }


#The activity status of the specified virtual server, as specified 
#by the user.
enable_state_values = {
        1: 'Enabled',
        2: 'Disabled',
        3: 'DisabledByParent', 
    }


def _unpack_ipv4(ipv4_packed):
    try:
        return socket.inet_ntoa(ipv4_packed)
    except Exception as e:
        log.error("Unable to unpack address %r", ipv4_packed)
        log.error(e)
        return None
def unpack_address_to_string(oid, packed_address):
    """
    Given a partial OID, and packed address return
    a human readable dotted notataion address
    """
    log.debug("Attempting to unpack %r using OID %s", packed_address, oid)
    address_string = ""
    route_domain = ""
    # If we have a leading period get rid of it
    if oid.startswith("."):
        log.debug("Dropping leading period from oid")
        oid = oid[1:]
    if oid.startswith(ADDR_TYPE_IPV4):
        address_string = _unpack_ipv4(packed_address)
    elif oid.startswith(ADDR_TYPE_IPV4Z):
        #Appears route domain addresses are stored as IPV4Z
        #It will be a SIZE of 8, with the first 4 being the IP4V4 address
        # With the second 4 being the route domain
        address_string = _unpack_ipv4(packed_address[:4])
        route_domain = oid[-1]
    elif oid.startswith(ADDR_TYPE_IPV6) or oid.startswith(ADDR_TYPE_IPV6Z):
        #I started to write this using socket.inet_ntop however the support
        #for that appears limited in platform support I'm not in a position 
        #to test this so rather than break something stub it out
        log.warn("IPV6 not support at this time")
        
    return (address_string, route_domain)
        


        