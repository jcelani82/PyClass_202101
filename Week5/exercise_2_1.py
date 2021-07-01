from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("C://Users//John Celani//Documents//Scripts//Python Class//Week5")
#env.loader = FileSystemLoader(".")

int_vars = {
    "sw_netmask" : 24,
    "sw_int" : "Ethernet1/1",
}

template_file = 'exercise_2_1.j2'
template = env.get_template(template_file)
output = template.render(**int_vars)
print(output)
