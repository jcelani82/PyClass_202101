import yaml
import os
from netmiko import ConnectHandler

with open(os.path.expanduser('~/.netmiko.yml'), "r") as f:
    yaml_out = yaml.load(f)

cisco3 = yaml_out['cisco3']
net_connect = ConnectHandler(**cisco3)
print(net_connect.find_prompt())
