
from ipaddress import ip_network


class Network:
    def __init__(self, network, mask):
        self.network = network
        self.mask = mask
        net = ip_network(f"{self.network}/{self.mask}")
        self.hosts = [str(ip) for ip in net.hosts()]

    def __iter__(self):
        return iter(self.hosts)

    def __str__(self):
        return f"{self.network}/{self.mask}"

    def __repr__(self):
        return f"Network('{self.network}', {self.mask})"


net1 = Network("10.1.1.0", 29)
