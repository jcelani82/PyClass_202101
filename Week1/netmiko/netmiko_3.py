from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password":  '88newclass',
    "device_type": 'cisco_nxos',
    "session_log": 'my_session.txt',
}

device2 = {

    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password":  '88newclass',
    "device_type": 'cisco_nxos',
    "session_log": 'my_session.txt',
}   

net_connect = ConnectHandler(**device1)
print (net_connect.find_prompt())

output = net_connect.send_command("show version")
print (output)


net_connect = ConnectHandler(**device2)
print (net_connect.find_prompt())


