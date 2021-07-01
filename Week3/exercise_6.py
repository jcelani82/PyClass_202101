import yaml
import os
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

with open(os.path.expanduser('~/.netmiko.yml'), "r") as f:
    yaml_out = yaml.load(f)

device = yaml_out['cisco4']
netconnect = ConnectHandler(**device)

print()
print(netconnect.find_prompt())
print()

cisco4_output = netconnect.send_command("show run")

cisco_obj = CiscoConfParse(cisco4_output.splitlines())
cisco_interface = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

x = 0

for interface in cisco_interface:
    print("#" * 80)
    interface = cisco_interface[x].text
    print(f"Interface Line: {interface}")
    y = 0

    for child in cisco_interface[y].children:
        if "ip address" in child.text: 
            ip_address = child.text
            print(f"IP Address Line: {ip_address}")
            print( "#" * 80) 
    x += 1
    print()

netconnect.disconnect()

