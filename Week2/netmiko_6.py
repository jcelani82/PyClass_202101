from netmiko import ConnectHandler
from getpass import getpass
import os
import time

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "secret": "88newclass",
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)

print("\n")

print("Prompt After Login: ")
print(net_connect.find_prompt())

print("\n")

print("Prompt after using <.config_mode()> method:")
net_connect.config_mode()
print(net_connect.find_prompt())

print("\n")

print("Prompt after using <.exit_config_mode()> method:")
net_connect.exit_config_mode()
print(net_connect.find_prompt())

print("\n")

net_connect.write_channel("disable\n")

time.sleep(2)
print(
    "Text Left in the SSH Channel from issueing the <write_channel()> method using the <read.channel()> method: \n"
)
print(net_connect.read_channel())

print("\n")
net_connect.disconnect()
