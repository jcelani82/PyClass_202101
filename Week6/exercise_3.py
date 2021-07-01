import pyeapi
from pprint import pprint
from getpass import getpass
from my_functions import read_yaml, iproute_results

filename = "arista_full.yml"
devices = read_yaml(filename)

password = getpass()

for host, device_dict in devices.items():
    
    if host != "my_devices":
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        iproute_output = device.enable(["show ip route"])

        iproute_results(host, iproute_output)

