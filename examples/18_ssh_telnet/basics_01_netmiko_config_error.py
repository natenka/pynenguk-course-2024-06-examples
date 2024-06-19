from pprint import pprint
from netmiko import (
    Netmiko,
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
    ConfigInvalidException,
)
import yaml


with open("devices.yaml") as f:
    device_list = yaml.safe_load(f)
r1 = device_list[0]

try:
    with Netmiko(**r1) as ssh:
        ssh.enable()
        output = ssh.send_config_set("loging 10.1.1.1")
        print(output)
except (ConfigInvalidException) as error:
    print(f"Error {r1['host']}", error)
