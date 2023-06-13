"""
This script uses spaCy's rule-based matcher to extract RFQs from a text file.
This uses matcher so it will only work off the patterns given. 
However, it can be used to train a custom model.
"""
import json
import spacy
from spacy.matcher import Matcher


def open_file(input_file):
    "Open a text file"
    with open(input_file, "r", encoding="utf-8") as opened_file:
        open_text = opened_file.read()
    return open_text


TEXT = open_file("data/outputs/rfq_dump.txt")
PATTERNS_FILE = "data/formatted_training_data/RFQ.json"

TEXT_OUTPUT_FILE = "data/formatted_training_data/labeled_rfqs.txt"
ENT_OUTPUT_FILE = "data/formatted_training_data/extracted_rfqs.txt"

with open(PATTERNS_FILE, "r", encoding="utf-8") as file:
    patterns_data = json.load(file)
patterns = patterns_data["patterns"]

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
matcher.add("RFQ", patterns)
doc = nlp(TEXT)
matches = matcher(doc)

entities = []
rfqs = []
for match_id, start, end in matches:
    entities.append((start, end - 1, doc.vocab.strings[match_id]))
    rfqs.append(doc[start:end].text)

with open(TEXT_OUTPUT_FILE, "w", encoding="utf-8") as f:
    for i, token in enumerate(doc):
        f.write(token.text_with_ws)
        for start, end, label in entities:
            if i == end:
                f.write(f" (( {start}, {end}, {label} )) ")
    f.write("\n\nExtracted RFQs:\n")
    for rfq in rfqs:
        f.write(f"{rfq}\n")

with open(ENT_OUTPUT_FILE, "w", encoding="utf-8") as f:
    for rfq in rfqs:
        f.write(f"{rfq}\n")

print("Extracted RFQs:")
for rfq in rfqs:
    print(rfq)
