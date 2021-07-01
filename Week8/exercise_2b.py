
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

import sys
from pprint import pprint
from jnpr_devices import srx2


def Check_Connected(device):
    
    if device.connected:
        print()
        print(f"The device {device.hostname} is connected.")
    else:
        print()
        print(f"The device is not connected.")
        sys.exit(1)


def Gather_Routes(device):
    
    route_entries = RouteTable(device)
    route_entries.get()
    return route_entries


def Gather_Arp_Table(device):
    
    arp_entries = ArpTable(device)
    arp_entries.get()

    return arp_entries


def Print_Output(device, routes, arp):

    print()
    print("Device Info: ")
    print()
    print(device.hostname)
    print(device.port)
    print(device.user)
    print()
    print("Routing Table: ")
    print()
    
    for r in routes.items():
        pprint(r)

    print()
    print("Arp Table: ")
    print()
    for a in arp.items():
        print(a)
    

if __name__ == "__main__":

    device = Device(**srx2)
    device.open()
    
    Check_Connected(device)
    
    routes = Gather_Routes(device)
    arp = Gather_Arp_Table(device)

    Print_Output(device, routes, arp)


