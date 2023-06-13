"""
This is for labling the entities in the corpus of text. 
This is important for training a custom model.
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

with open(PATTERNS_FILE, "r", encoding="utf-8") as file:
    patterns_data = json.load(file)
patterns = patterns_data["patterns"]

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
matcher.add("RFQ", patterns)
doc = nlp(TEXT)
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)
