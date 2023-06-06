' --- Create Training Set --- '

import json
import spacy
from spacy.lang.en import English
from spacy.pipeline import EntityRuler

def load_data(file):
    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


