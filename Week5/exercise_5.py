from netmiko import ConnectHandler
from my_devices import cisco3



net_connect = ConnectHandler(**cisco3)

output = net_connect.send_command("show run")

f = open("cisco3_config.txt", "w")
f.write(output)

net_connect.disconnect()

