import json


to_json = {
    "trunk": [
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan",
    ],
    "access": [
        "switchport mode access",
        "switchport access vlan",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ],
    "test": True,
    "cfg": None,
    "line": False,
    "value": (1, 20),
    True: [1, 2, 3],
    1: 100,
    (1, 2): 100,
}

with open("json_files/result2.json", "w") as f:
    json.dump(to_json, f, indent=4, skipkeys=True)
