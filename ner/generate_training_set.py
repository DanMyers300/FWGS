"""
Generate Training Set
"""
import json
# import spacy
# from spacy.lang.en import English
# from spacy.pipeline import EntityRuler

def load_data(file):
    "Load Data"
    with open(file, "r", encoding="utf-8") as file:
        load__json_data = json.load(file)
    return load__json_data

data = load_data("data/formatted_training_data/RFQ.json")
