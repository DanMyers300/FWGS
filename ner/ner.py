"""
NER
"""
# import json
# import random
import spacy

def open_file():
    "Open corpus of text"
    with open("data/corpus.txt", "r", encoding="utf-8") as file:
        contents = file.read()
        return contents

nlp = spacy.load("en_core_web_lg")
doc = nlp(open_file())

for ent in doc.ents:
    print(ent.text, ent.label_)
