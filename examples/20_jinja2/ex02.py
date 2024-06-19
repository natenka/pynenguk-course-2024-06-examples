import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined


env = Environment(loader=FileSystemLoader("templates"), undefined=StrictUndefined)
data = {
    "all_devices": [
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
}
template = env.get_template("nagios_loop.j2")
print(template.render(data))
#print(template.render(all_devices=data))
