import logging
from pprint import pprint
from netmiko import Netmiko, NetmikoTimeoutException

fmt = logging.Formatter(
    "{asctime} {name} {levelname:10} {lineno} {funcName} {message}",
    style="{"
)

# stderr
stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

# file
filel = logging.FileHandler("log_03.log")
filel.setLevel(logging.DEBUG)
filel.setFormatter(fmt)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[stderr, filel]
)


def send_show_netmiko(device_dict, command):
    ip = device_dict["host"]
    logging.info(f"===> Connection: {ip}")

    try:
        with Netmiko(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            logging.debug(f"\n{result}")
            logging.info(f"<=== Received:   {ip}")
        return result
    except NetmikoTimeoutException:
        logging.exception("ERROR")


if __name__ == "__main__":
    r1 = {
        "host": "192.168.139.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "timeout": 5,
    }

    send_show_netmiko(r1, "sh ip int br")
    print("#" * 50)
