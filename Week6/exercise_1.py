import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable([ "show ip arp"])

for arp_entry in output[0]["result"]["ipV4Neighbors"]:
    print(f"{arp_entry['hwAddress']} : {arp_entry['address']}")


