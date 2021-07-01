import yaml
import pyeapi
import pprint
from getpass import getpass

filename = "exercise_2a.yml"
with open(filename, "r") as f:
    devices = yaml.load(f)

for host, device_dict in devices.items():

    device_dict["password"] = getpass()
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable(["show ip arp"])

    print()
    print()
    print(f"Arp Table for {host}: ")
    for arp_entry in output[0]["result"]["ipV4Neighbors"]:
        print(f"{arp_entry['hwAddress']} : {arp_entry['address']}")
