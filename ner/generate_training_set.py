"""
Generate Training Set
"""
import json

# import spacy
# from spacy.lang.en import English
# from spacy.pipeline import EntityRuler

MAIN_FILE = "data/formatted_training_data/RFQ.json"


def load_data(file):
    "Load Data"
    with open(file, "r", encoding="utf-8") as file:
        load__json_data = json.load(file)
    return load__json_data


def create_training_data(file, label):
    "Create Training Data"
    data = load_data(file)
    patterns = []
    for item in data:
        pattern = {"label": label, "pattern": item}
        patterns.append(pattern)
    return patterns


training_patterns = create_training_data(MAIN_FILE, "RFQ")
print(training_patterns)
