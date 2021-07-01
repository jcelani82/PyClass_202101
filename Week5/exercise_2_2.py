from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
#env.loader = FileSystemLoader("C://Users//John Celani//Documents//Scripts//Python Class//Week5")
env.loader = FileSystemLoader(".")

sw1_vars = {
    "hostname" : "nxos1",
    "int" : "Ethernet1/1",
    "ip_add" : "10.1.100.1",
    "ip_subnet" : "24",
    "local_as" : 22,
    "remote_ip" : "10.1.100.2",
    "remote_as" : 22,
}


sw2_vars = {
    "hostname" : "nxos2",
    "int" : "Ethernet1/1",
    "ip_add" : "10.1.100.2",
    "ip_subnet" : "24",
    "local_as" : 22,
    "remote_ip" : "10.1.100.1",
    "remote_as" : 22,
}

template_file = 'exercise_2_2.j2'
template = env.get_template(template_file)
output = template.render(**sw1_vars)
output += "\n"
output += template.render(**sw2_vars)
print(output)
