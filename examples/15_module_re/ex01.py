import re
from pprint import pprint

regex = r"^interface .+?!"

with open("configs/config_r1.txt") as f:
    content = f.read()
    m = re.findall(regex, content, re.DOTALL | re.MULTILINE)
    # m = re.findall(regex, content, re.S | re.M)
    pprint(m)
    for i in m:
        print(i)
        print("="*30)
