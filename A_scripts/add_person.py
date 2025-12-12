from linkml_runtime.loaders import yaml_loader
import yaml

# Load existing YAML data
with open('A_data/people_data.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Add a new person
new_person = {
    'name': 'Carla',
    'age': 30
}
data['persons'].append(new_person)

# Save updated YAML
with open('A_data/people_data.yaml', 'w') as f:
    yaml.dump(data, f)

# Print all people
for person in data['persons']:
    print(f"Name: {person['name']}, Age: {person['age']}")
