from pprint import pprint
import yaml

file = "yaml_files/mult_docs.yaml"

with open(file) as f:
    all_data = yaml.safe_load_all(f)
    for doc in all_data:
        print(doc)
