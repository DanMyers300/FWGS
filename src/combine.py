import os
import json

# Directory path
directory = 'data/outputs/'

# List files in the directory
input_files = os.listdir(directory)

# Dictionary to hold the combined data
combined_data = {}

# Iterate over the input files
for file_name in input_files:
    # Read the contents of each file
    with open(os.path.join(directory, file_name), 'r') as file:
        data = json.load(file)

    # Create an object with the file name as the key
    combined_data[file_name.split('.')[0]] = data

# Write the combined data to the output file
output_path = os.path.join(directory, 'outputs.json')
with open(output_path, 'w') as output_file:
    json.dump(combined_data, output_file, indent=4)

