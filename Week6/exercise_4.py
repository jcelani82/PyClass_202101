import pyeapi
from pprint import pprint
from getpass import getpass
from my_functions import read_yaml, iproute_results
from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

filename = "arista_full.yml"
devices = read_yaml(filename)

password = getpass()

deviceData = {}
tmpDevices = devices['my_devices']
devices.pop('my_devices')

for deviceKey, deviceValue in devices.items():
    
    cmds = []
    data = deviceValue['data']
    deviceValue.pop('data')
    deviceValue["password"] = password

    j2_vars = {
        "intf_name" : data['intf_name'],
        "intf_ip" : data['intf_ip'],
        "intf_mask" : data['intf_mask'],
    }
   
    templateFile = 'exercise_4.j2'
    template = env.get_template(templateFile)
    cfgLines = template.render(**j2_vars)
    cfgLines = cfgLines.strip()
    cfgLines = cfgLines.splitlines()

    connection = pyeapi.client.connect(**deviceValue)
    device = pyeapi.client.Node(connection)
    config_output = device.config(cfgLines)
    print(f"{deviceKey} : {config_output}")

print()
print()

for deviceKey, deviceValue in devices.items():

    connection = pyeapi.client.connect(**deviceValue)
    device = pyeapi.client.Node(connection)
    show_output = device.enable("show ip interface brief")
    
    print()
    print("#" * 80)
    print(f"SHOW IP INT BRIEF for : {deviceKey}")
    pprint(show_output[0]['result']['output']) 
    print("#" * 80)
