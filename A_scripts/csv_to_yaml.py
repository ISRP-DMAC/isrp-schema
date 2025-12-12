import pandas as pd
from pathlib import Path
from linkml_runtime.loaders import yaml_loader, yaml_dumper

# Paths
schema_file = Path('A_schema/person_schema.yaml')
csv_file = Path('A_data/people.csv')
yaml_file = Path('A_data/people_data.yaml')

# Load CSV
df = pd.read_csv(csv_file)

# Dynamically load the schema classes
schema_classes = yaml_loader.load(schema_file, target_class=None)

# Convert CSV rows into dicts matching your schema
persons = []
for _, row in df.iterrows():
    persons.append({
        'name': row['name'],
        'age': int(row['age'])
    })

# Wrap in a collection
collection = {'persons': persons}

# Save to YAML
yaml_file.write_text(yaml_dumper.dumps(collection))

print(f"YAML saved to {yaml_file}")
