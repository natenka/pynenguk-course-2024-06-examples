import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined


env = Environment(loader=FileSystemLoader("templates"), undefined=StrictUndefined)
data = [
    {
        "hostname": "Ivanov",
        "ip": "10.45.130.77",
        "switch_name": "xCentral",
        "type": "phone",
    },
    {
        "hostname": "Halushko",
        "ip": "10.45.30.77",
        "switch_name": "xCentral",
        "type": "pc",
    },
]
with open("data.yaml") as f:
    data_yaml = yaml.safe_load(f)

template = env.get_template("nagios.j2")
for device in data_yaml:
    print(template.render(device))
