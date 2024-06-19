from pprint import pprint
from netmiko import Netmiko, NetmikoAuthenticationException, NetmikoTimeoutException
import yaml


with open("devices.yaml") as f:
	device_list = yaml.safe_load(f)
r1 = device_list[0]

try:
    with Netmiko(**r1) as ssh:
        ssh.enable()
        output = ssh.send_command("sh ip int br")
        print(output)
except (NetmikoAuthenticationException, NetmikoTimeoutException) as error:
    print(f"Error {r1['host']}", error)

