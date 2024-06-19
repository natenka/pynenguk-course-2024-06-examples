from pprint import pprint
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException, ScrapliCommandFailure
import yaml


r1 = {
    "host": "192.168.100.1",
    "auth_username": "cisco",
    "auth_password": "cisco",
    # "auth_secondary": "cisco",
    "auth_strict_key": False,
    "timeout_socket": 5,
    "timeout_transport": 10,
    "platform": "cisco_iosxe",
    # указывает что после логина на устройство, scrapli должен быть в exec режиме
    # по умолчанию privilege_exec = enable для Cisco
    "default_desired_privilege_level": "exec",
}


def send_show(device, command):
    try:
        with Scrapli(**device) as conn:
            print(conn.get_prompt())
            # если добавить пароль на enable, то так можно перейти в enable
            # conn.acquire_priv("privilege_exec") # перейти в режим enable
            # print(conn.get_prompt())
            response = conn.send_command(command)
            out = response.result
            return out
    except ScrapliException as error:
        print(device["host"], error)


if __name__ == "__main__":
    pprint(send_show(r1, "sh ip int br"), width=120)
