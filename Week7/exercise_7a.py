import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

device = Device (
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")

interface = output.find(".//interface")
state = output.find(".//state")
mtu = output.find(".//eth_mtu")

print()
print(f"Interface: {interface.text}; State: {state.text}; MTU: {mtu.text}")
print()
