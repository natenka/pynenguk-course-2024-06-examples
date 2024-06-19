from netmiko import Netmiko
import yaml


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

r1, r2, r3 = devices

ssh1 = Netmiko(**r1)
ssh2 = Netmiko(**r2)


def get_netmiko_info(netmiko_session):
    print("PROMPT:", netmiko_session.find_prompt())
    print("HOST:", netmiko_session.host)


get_netmiko_info(ssh1)
get_netmiko_info(ssh2)
