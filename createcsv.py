import pandas as pd

# Read the data from the text file
with open('test.txt', 'r') as f:
    data = f.readlines()

# Create an empty dictionary to store the data
table_data = {}

# Loop over the lines of the file and parse the headers and data
current_header = ''
for line in data:
    line = line.strip()
    if line.endswith(':'):
        current_header = line[:-1]
        table_data[current_header] = []
    elif current_header != '':
        table_data[current_header].append(line)

# Pad the data arrays with empty strings to make them the same length
max_length = max([len(v) for v in table_data.values()])
for k, v in table_data.items():
    if len(v) < max_length:
        table_data[k] += [''] * (max_length - len(v))

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(table_data)

# Write the data to a CSV file
df.to_csv('output.csv', index=False)

# Display a confirmation message
print('Data written to output.csv')
