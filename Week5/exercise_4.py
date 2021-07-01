from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

vrf_dict = {
    "red" : "100:1", 
    "white" : "200:1" , 
    "blue" : "300:1" , 
    "black" : "400:1" , 
    "green" : "500:1"
}

j2_vars = {
    "vrf_name" : vrf_dict,
    "ipv4_enable" : True,
    "ipv6_enable" : True,
}

template_file = 'exercise_4.j2'
template = env.get_template(template_file)
output = template.render(**j2_vars)
print(output)
