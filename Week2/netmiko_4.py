from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
import os

starttime = datetime.now()

device1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
#    "fast_cli" : True,
}

config = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']

print("\n")

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

print("\n")

output = net_connect.send_config_set(config, strip_prompt=False, strip_command=False)
print(output)

print("\n")

ping_output = net_connect.send_command_timing("ping google.com", strip_prompt=False, strip_command=False)


if "!!" in output:
    print("Ping Successful: ")
    print(f"\n\nPing Ouput from router:\n{output}")
else:
    raise ValueError(f"\n\nPing Failed:\n{output}")


print("\n")

net_connect.disconnect()

endtime = datetime.now()

print(f"The Execution time is: {endtime-starttime}")


