import re

# Read the list of codes from the CSV file
codes = []
with open('data/base_files/coded_notes.csv', 'r') as file:
    lines = file.readlines()[1:]  # Skip the header line
    for line in lines:
        code = line.split(',')[0]
        codes.append(code.strip())

# Remove "APPENDICES" from the list
codes = [code for code in codes if code != "APPENDICES"]

# Extract the codes from rfq_dump.txt
extracted_codes = []
with open('data/outputs/rfq_dump.txt', 'r') as file:
    rfq_dump_content = file.read()
    for code in codes:
        matches = re.findall(code, rfq_dump_content)
        extracted_codes.extend(matches)

# Print the extracted codes
for code in extracted_codes:
    print(code)

