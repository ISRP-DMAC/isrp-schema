import pandas as pd
import yaml
from pathlib import Path

# Paths
csv_file = Path('A_data/people.csv')
yaml_file = Path('A_data/people_data.yaml')

# Load CSV
df = pd.read_csv(csv_file)

# --- Print CSV contents ---
print("CSV data loaded:")
print(df)
print("------")

# Convert CSV rows into dictionaries
persons = []
for _, row in df.iterrows():
    persons.append({
        'name': row['name'],
        'age': int(row['age'])
    })

# Wrap in a collection
collection = {'persons': persons}

# --- Print converted collection ---
print("Converted collection:")
for p in collection['persons']:
    print(f"Name: {p['name']}, Age: {p['age']}")

# Save YAML
with open(yaml_file, 'w') as f:
    yaml.safe_dump(collection, f, sort_keys=False)

print(f"YAML saved to {yaml_file}")
