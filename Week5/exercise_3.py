from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

j2_vars = {
    "vrf_name" : "blue",
    "rd_num" : "100:1",
    "ipv4_enable" : True,
    "ipv6_enable" : True,
}

template_file = 'exercise_3.j2'
template = env.get_template(template_file)
output = template.render(**j2_vars)
print(output)
