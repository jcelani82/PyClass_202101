from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
    "session_log": "my_session.txt",
    "global_delay_factor": 2,
}

print("\n")

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

print("\n")

output = net_connect.send_command("show version", use_textfsm=True)
print(output)

print("\n")

output = net_connect.send_command("show lldp neighbors", use_textfsm=True)
print(output)

print("\n\n")

print(f"The Data Type that TEXT FSM sent back is: {type(output)}")
print(
    f"The port number that HPE SW is connected to Cisco4 is: {output[0]['local_interface']}"
)
print(
    f"The port number that Cisco4 is connected to HPE SW is: {output[0]['neighbor_interface']}"
)

print("\n")

net_connect.disconnect()
