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

showcmds = [
    "show system uptime",
    "show system resources"
]


output = device.show_list(showcmds)

for cmd in output: 
    print()
    print(etree.tostring(cmd).decode())
    print()

