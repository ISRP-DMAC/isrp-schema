import yaml
import plotly.express as px

# Load YAML data
with open('A_data/people_data.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Extract names and ages
names = [person['name'] for person in data['persons']]
ages = [person['age'] for person in data['persons']]

# Create interactive bar chart
fig = px.bar(
    x=names,
    y=ages,
    text=ages,
    labels={'x':'Name', 'y':'Age'},
    title='Ages of People'
)

# Show in browser
fig.show()
