import yaml

devices = [
{'host': 'cisco3.lasthop.io', 'username': 'test', 'password': 'test', 'device_type': 'cisco_ios'},
{'host': 'cisco4.lasthop.io', 'username': 'test', 'password': 'test', 'device_type': 'cisco_ios'},
{'host': 'nxos1.lasthop.io', 'username': 'test', 'password': 'test', 'device_type': 'cisco_nxos'},
{'host': 'nxos2.lasthop.io', 'username': 'test', 'password': 'test', 'device_type': 'cisco_nxos'},
]


filename = "outfile_2b.yml"
with open(filename, "wt") as f: 
    yaml.dump(devices, f, default_flow_style=False)

