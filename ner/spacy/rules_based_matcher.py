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
            entities.append(
                (sent.text, {"entities": [(start - sent.start, end - sent.start - 1, doc.vocab.strings[match_id])]})
            )
    TRAIN_DATA.extend(entities)

with open(JSON_OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(TRAIN_DATA, f)
