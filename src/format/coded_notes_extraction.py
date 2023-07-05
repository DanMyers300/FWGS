import csv
import json

csv_file = "data/coded_notes.csv"
json_file = "data/coded_notes.json"

patterns = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        code = row.get("Code", "")
        if code:
            pattern = {"label": "Coded Note", "pattern": code}
            patterns.append(pattern)

with open(json_file, "w") as file:
    json.dump(patterns, file, indent=4)

