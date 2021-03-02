from netmiko import ConnectHandler
from getpass import getpass
import os

device1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
}


device2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
}

print("\n")

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output = net_connect.send_config_from_file(config_file='netmiko_5_config.txt', strip_prompt=False, strip_command=False)
print(output)

print("\n")

net_connect = ConnectHandler(**device2)
print(net_connect.find_prompt())
output = net_connect.send_config_from_file(config_file='netmiko_5_config.txt', strip_prompt=False, strip_command=False)
print(output)

print(net_connect.save_config())

net_connect.disconnect()
