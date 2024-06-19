import socket
from pprint import pprint
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException, ScrapliCommandFailure
import yaml


def send_show(device, commands):
    if type(commands) == str:
        commands = [commands]
    host_output_dict = {}
    try:
        with Scrapli(**device) as conn:
            mresponse = conn.send_commands(commands)
            for cmd, res in zip(commands, mresponse):
                out = res.result
                if res.failed:
                    host_output_dict[cmd] = None
                else:
                    host_output_dict[cmd] = out
            # mresponse.raise_for_status()
            return host_output_dict
    except ScrapliCommandFailure:
        raise
    except ScrapliException as error:
        print(device["host"], error)
    except socket.timeout as error:
        print(device["host"], error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for d in devices:
        pprint(send_show(d, ["sh ip int br", "sh clock"]), width=120)
