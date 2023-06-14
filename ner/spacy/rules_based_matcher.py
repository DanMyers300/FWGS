"""
Create a rules-based matcher to extract RFQs from a text file.
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
JSON_OUTPUT_FILE = "data/formatted_training_data/RFQ/labeled_rfqs.json"

nlp = spacy.load("en_core_web_sm")
doc = nlp(TEXT)

with open(PATTERNS_FILE, "r", encoding="utf-8") as file:
    patterns_data = json.load(file)
patterns = patterns_data["patterns"]

matcher = Matcher(nlp.vocab)
matcher.add("RFQ", patterns)
matches = matcher(doc)

TRAIN_DATA = []
for sent in doc.sents:
    entities = []
    for match_id, start, end in matches:
        if start >= sent.start and end <= sent.end:
            entities.append((start - sent.start, end - sent.start, doc.vocab.strings[match_id]))
    if entities:
        TRAIN_DATA.append((sent.text, {"entities": entities}))

formatted_data = []
for text, annotations in TRAIN_DATA:
    entities = []
    for start, end, label in annotations["entities"]:
        entities.append((start, end, label))
    formatted_data.append((text, {"entities": entities}))

with open(JSON_OUTPUT_FILE, "w", encoding="utf-8") as f:
    for data in formatted_data:
        json.dump(data, f)
        f.write('\n')

