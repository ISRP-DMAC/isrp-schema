from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.compile_python import compile_python  # optional, just info
import yaml

# Load the YAML data as a dictionary
with open('A_data/people_data.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Print all people
for person in data['persons']:
    print(f"Name: {person['name']}, Age: {person['age']}")
