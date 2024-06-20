import paramiko
import time
from pprint import pprint


class CiscoSSH:
    def __init__(self, host, username, password, enable_pass, pause=0.5, max_read=139000):
        self.host = host
        self.username = username
        self.password = password
        self.enable_pass = enable_pass
        self.pause = pause
        self.max_read = max_read

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(
            hostname=self.host,
            username=self.username,
            password=self.password,
            look_for_keys=False,
            allow_agent=False,
        )
        self.ssh = client.invoke_shell()
        self._send("enable")
        self._send(enable_pass)
        self._send("terminal length 0")
        self.ssh.recv(max_read)

    def _send(self, command):
        self.ssh.send(f"{command}\n")
        time.sleep(self.pause)

    def send_command(self, command):
        # CiscoSSH._send(self, command)
        self._send(command)
        output = self.ssh.recv(self.max_read)
        return output.decode("utf-8").replace("\r\n", "\n")

    def __repr__(self):
        return f"<CiscoSSH connection {self.host}>"

    def close(self):
        self.ssh.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


if __name__ == "__main__":
    with CiscoSSH("192.168.139.1", "cisco", "cisco", "cisco") as r1:
        out = r1.send_command("sh clock")
        pprint(out, width=120)
        print(r1)

