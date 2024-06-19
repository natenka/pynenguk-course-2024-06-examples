class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask
        if isinstance(mask, int):
            if 0 <= mask <= 32:
                pass
            else:
                raise ValueError("invalid value")
        else:
            raise TypeError("argument must be an int")

    def info(self):
        print(self.ip)

ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.2.2.2", 24)
