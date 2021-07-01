from my_devices import nxos1, nxos2
from netmiko import ConnectHandler

netconnect = ConnectHandler(**nxos1)

print()
print(netconnect.find_prompt())
print()

netconnect.disconnect()

