from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


device1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
    "session_log": "my_session.txt",
    "fast_cli" : True,
#    "global_delay_factor": 2,
}


net_connect = ConnectHandler(**device1)

print(net_connect.find_prompt())

