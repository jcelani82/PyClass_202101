from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


device1 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
    "session_log": "my_session.txt",
    "global_delay_factor": 2,
}

# device2 = {

#    "host": 'cisco4.lasthop.io',
#    "username": 'pyclass',
#    "password":  '88newclass',
#    "device_type": 'cisco_nxos',
#    "session_log": 'my_session.txt',
# }

net_connect = ConnectHandler(**device1)

print("Global Delay Factor of 2\n")
T1 = datetime.now()
output = net_connect.send_command("show lldp neighbors")
T2 = datetime.now()
print(output)
T3 = T2 - T1
print("\nExecution Time with Global Delay Factor of 2: {}".format(T2 - T1))

print("\n\n")

print("Send Command Delay Factor of 8")
T1 = datetime.now()
output = net_connect.send_command("show lldp neighbors", delay_factor=8)
T2 = datetime.now()
print(output)
T4 = T2 - T1
print("\n\nExecution Time: {}".format(T2 - T1))
