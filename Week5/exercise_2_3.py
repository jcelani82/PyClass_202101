import yaml
import os
import time
import re
from my_devices import nxos1, nxos2 
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
#env.loader = FileSystemLoader("C://Users//John Celani//Documents//Scripts//Python Class//Week5")
env.loader = FileSystemLoader(".")

sw1_vars = {
    "hostname" : "!_nxos1",
    "int" : "Ethernet1/1",
    "ip_add" : "10.1.100.1",
    "ip_subnet" : "24",
    "local_as" : 22,
    "remote_ip" : "10.1.100.2",
    "remote_as" : 22,
}

sw2_vars = {
    "hostname" : "!_nxos2",
    "int" : "Ethernet1/1",
    "ip_add" : "10.1.100.2",
    "ip_subnet" : "24",
    "local_as" : 22,
    "remote_ip" : "10.1.100.1",
    "remote_as" : 22,
}

template_file = 'exercise_2_2.j2'
nxos1["j2_vars"] = sw1_vars
nxos2["j2_vars"] = sw2_vars

for device in (nxos1, nxos2): 
    
    temp_dict = device.copy()
    j2_vars_temp = temp_dict.pop("j2_vars")
    
    template = env.get_template(template_file)
    temp_config = template.render(**j2_vars_temp)
    configs = [temp_config.strip() for temp_config in temp_config.splitlines()]

    netconnect = ConnectHandler(**temp_dict)
    device["net_conn"] = netconnect
    
    print(f"Sending Configurations to {netconnect.find_prompt()}")
    output = netconnect.send_config_set(configs)
    print("Completed")
    print()

print("Waiting 15s for BGP to Converge")
print()
time.sleep(15)

print("Testing BGP and Connectivity")
print()

for device in (nxos1, nxos2):
    
    remote_ip = device["j2_vars"]["remote_ip"]
    netconnect = device["net_conn"]     
    local_ip = device["host"]
    
    print(f"Checking BGP Connectivity on {local_ip} to {remote_ip}")
    bgpoutput = netconnect.send_command(f"show ip bgp summary | include {remote_ip}")
    
    match = re.search(r"\s+(\S+)\s*$", bgpoutput)
    prefix_received = match.group(1)

    try: 
        int(prefix_received)
        print( f"{local_ip} BGP Reached Established state with {remote_ip}")
    
    except ValueError:
        print(f"{local_ip} BGP failed to reach established state with {remote_ip}")
        

    print()
    print(f"Testing connectivity from {local_ip} to {remote_ip}")

    pingoutput = netconnect.send_command(f"ping {remote_ip}", delay_factor=5)

    if "64 bytes from" not in pingoutput:
        print(f"Failed ping test to {remote_ip}")
    else:
        print(f"Conenctivity between {local_ip} to {remote_ip} succesful")
    
    print()
for device in (nxos1, nxos2):
    netconnect = device["net_conn"]
    netconnect.disconnect()    
