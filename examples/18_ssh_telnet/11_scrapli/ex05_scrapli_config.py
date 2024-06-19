import socket
from pprint import pprint
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException, ScrapliCommandFailure
import yaml


def send_cfg(device, commands, stop_on_error=True):
    if type(commands) == str:
        commands = [commands]
    try:
        with Scrapli(**device) as conn:
            mresponse = conn.send_configs(commands, stop_on_failed=stop_on_error)
            for r in mresponse:
                if r.failed:
                    print(
                        f"Возникла ошибка при выполнении команды {r.channel_input}"
                        f"{r.result}"
                    )
            return mresponse.result
    except ScrapliException as error:
        print(device["host"], error)
    except socket.timeout as error:
        print(device["host"], error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for d in devices:
        pprint(send_cfg(d, ["sdfsdf", "username user2 password 23452352"]), width=120)
        break
