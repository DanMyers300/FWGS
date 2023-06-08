"""
Process data from .json format to .spacy format
"""
import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")
TRAINING_DATA = "data/formatted_training_data/data.json"
# the DocBin will store the example documents
db = DocBin()
for text, annotations in TRAINING_DATA:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")
