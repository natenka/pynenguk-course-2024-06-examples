import ipaddress
from pprint import pprint


class IPAddress:
    def __init__(self, ip, mask):
        print(f"__init__ {ip=} {mask=}")
        self.ip = ip
        self.mask = mask

    def __int__(self):
        bits = ""
        for octet in self.ip.split("."):
            bits += f"{int(octet):08b}"
        return int(bits, 2)

    def __lt__(self, other):
        if not isinstance(other, IPAddress):
            raise TypeError(
                f"'<' not supported between instances of "
                f"'IPAddress' and '{type(other).__name__}'"
            )
        return (int(self), self.mask) < (int(other), other.mask)

    def __len__(self):
        return 32

    def __str__(self):
        return f"{self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress('{self.ip}', {self.mask})"


ip1 = IPAddress("10.1.1.1", 23)
ip2 = IPAddress("10.2.2.2", 25)
ip3 = IPAddress("10.1.1.1", 25)
ip4 = IPAddress("10.10.1.1", 25)
