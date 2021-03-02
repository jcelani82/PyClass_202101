from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password":  '88newclass',
    "device_type": 'cisco_nxos',
    "session_log": 'my_session.txt',
}

#device2 = {

#    "host": 'cisco4.lasthop.io',
#    "username": 'pyclass',
#    "password":  '88newclass',
#    "device_type": 'cisco_nxos',
#    "session_log": 'my_session.txt',
#}   

net_connect = ConnectHandler(**device1)
print (net_connect.find_prompt())

output = net_connect.send_command("ping", expect_string=r'Protocol', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Target IP address:', strip_command=False, strip_prompt=False)
output += net_connect.send_command("8.8.8.8", expect_string=r'Repeat count', strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Datagram size', strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Timeout in seconds', strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Extended commands', strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'Sweep range of sizes', strip_command=False, strip_prompt=False)
output += net_connect.send_command("\n", expect_string=r'#', strip_command=False, strip_prompt=False)


net_connect.disconnect()

print(output)


