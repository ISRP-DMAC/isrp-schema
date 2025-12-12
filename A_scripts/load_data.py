from linkml_runtime.loaders import yaml_loader
from person_schema import PersonCollection

# Load the YAML data
data = yaml_loader.load('A_data/people_data.yaml', target_class=PersonCollection)

# Print all people
for person in data.persons:
    print(f"Name: {person.name}, Age: {person.age}")
