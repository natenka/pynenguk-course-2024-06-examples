from scrapli import Scrapli
from scrapli.exceptions import ScrapliException, ScrapliAuthenticationFailed
import yaml


def send_show(device, show_command):
    try:
        with Scrapli(**device) as ssh:
            reply = ssh.send_command(show_command)
            return reply.result
    except ScrapliAuthenticationFailed as error:
        print(error)


def send_cfg(device, cfg_commands):
    try:
        with Scrapli(**device) as ssh:
            reply = ssh.send_configs(cfg_commands)
            return reply.result
    except ScrapliException as error:
        print(error, device["host"])


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    output = send_show(r1, "sh ip int br")
    print(output)

    output_cfg = send_cfg(r1, ["interface lo11", "ip address 11.1.1.1 255.255.255.255"])
    print(output_cfg)
