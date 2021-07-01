import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

device = Device (
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")
print(f"Interface: {output['TABLE_interface']['ROW_interface']['interface']}; State: {output['TABLE_interface']['ROW_interface']['admin_state']}; MTU: {output['TABLE_interface']['ROW_interface']['eth_mtu']}")
