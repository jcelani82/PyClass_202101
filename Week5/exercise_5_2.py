from jinja2 import FileSystemLoader, StrictUndefined, Template
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

j2_vars = {
    "login_server" : "default_local",
    "clock_timezone" : "PST",
    "clock_offset" : 8,
    "clock_dst" : "PDT",
    "ntp_1" : "130.126.24.24",
    "ntp_2" : "152.2.21.1",
}

template_file = 'exercise_5.j2'
template = env.get_template(template_file)
output = template.render(**j2_vars)
print(output)
