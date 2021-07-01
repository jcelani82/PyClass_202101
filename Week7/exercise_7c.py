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

cfgcmds1 = [
    "interface loopback1",
    "description cfgcmds1",
    "ip address 1.1.1.1 255.255.255.255"
]


cfgcmds2 = [
    "interface loopback2",
    "description cfgcmds2",
    "ip address 2.2.2.2 255.255.255.255"
]

output = device.config_list(cfgcmds1)
for cmd in output:
    print()
    print(etree.tostring(cmd).decode())
    print()

output = device.config_list(cfgcmds2)
for cmd in output:
    print()
    print(etree.tostring(cmd).decode())
    print()

