import re
from pprint import pprint

regex = r"^(\S+) +([\d.]+)"

result = []
with open("sh_ip_int_br.txt") as f:
    output = f.read()

m_all = re.finditer(regex, output, re.MULTILINE)
for m in m_all:
    print(m.groups())

pprint(result)

