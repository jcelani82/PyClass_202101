import yaml
import os
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

cisco_obj = CiscoConfParse("configfile_7.txt")

bgpconfig = cisco_obj.find_objects(r"^router bgp")
neiconfig = cisco_obj.find_objects_w_parents(parentspec=r"router bgp",childspec=r"neighbor") 

bgp_peers = []

for nei in neiconfig:
    _, nei_ip = nei.text.split()
    for child in nei.children:
        if "remote-as" in child.text:
            _, nei_as = child.text.split()
    bgp_peers.append((nei_ip, nei_as))


print(f"\nBGP Peers:\n{bgp_peers}\n")
