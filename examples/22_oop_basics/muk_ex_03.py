class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = self._check_mask(mask)

    def _check_mask(self, mask):
        if isinstance(mask, str):
            octets = ""
            for octet in mask.split("."):
                octets += bin(int(octet))[2:]
            if len(octets) != 32:
                raise ValueError("invalid value")
            mask = octets.count("1")
        if isinstance(mask, int):
            if 0 <= mask <= 32:
                pass
            else:
                raise ValueError("invalid value")
        else:
            raise TypeError("argument must be an int")
        return mask

    def __str__(self):
        return f"{self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress({self.ip}, {self.mask})"

ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.2.2.2", 24)
