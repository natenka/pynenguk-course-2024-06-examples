import json
from pprint import pprint

file = "json_files/sw_templates_new.json"
with open(file) as f:
    data = json.load(f)

pprint(data, sort_dicts=False)
#print(type(data))
#pprint(data["trunk"])
