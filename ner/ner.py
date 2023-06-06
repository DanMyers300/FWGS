"""
NER
"""
# import json
# import random
import spacy

nlp = spacy.load("en_core_web_lg")
doc = nlp(test)

for ent in doc.ents:
    print(ent.text, ent.label_)
