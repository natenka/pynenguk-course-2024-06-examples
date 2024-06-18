import re


regex = r"Fast\S+"

with open("show_output/sh_ip_int_br.txt") as f:
    content = f.read()

m = re.findall(regex, content)
print(m)
