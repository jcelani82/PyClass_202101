import pyeapi
import pprint
from getpass import getpass
from my_functions import read_yaml, arp_results

filename = "exercise_2a.yml"
devices = read_yaml(filename)

for host, device_dict in devices.items():

    device_dict["password"] = getpass()
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    arp_output = device.enable(["show ip arp"])

    arp_results(host, arp_output)
