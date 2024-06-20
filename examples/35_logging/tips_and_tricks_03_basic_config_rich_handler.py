import logging

from netmiko import Netmiko
from rich.logging import RichHandler


logging.getLogger("netmiko").setLevel(logging.INFO)
logging.getLogger("paramiko").setLevel(logging.INFO)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[RichHandler(show_path=False)]
)


def send_show_netmiko(device_dict, command):
    ip = device_dict["host"]
    logging.info(f"===> Connection: {ip}")

    with Netmiko(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        logging.debug(f"<=== Received: output from {ip}\n{output}")
    return output


if __name__ == "__main__":
    r1 = {
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "timeout": 5,
    }

    send_show_netmiko(r1, "sh ip int br")
