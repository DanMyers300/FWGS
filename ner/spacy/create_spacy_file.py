"""
Convert the basic text file to a .spacy training file
"""
import json
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin

TRAIN_DATA_FILE = "data/formatted_training_data/RFQ/labeled_rfqs.json"

with open(TRAIN_DATA_FILE, "r", encoding="utf-8") as file:
    TRAIN_DATA = json.load(file)


def convert(lang: str, TRAIN_DATA, output_path: Path):
    "For converting to the training model"
    nlp = spacy.blank(lang)
    db = DocBin()
    for text, annot in TRAIN_DATA:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                warnings.warn(msg)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(output_path)


convert("en", TRAIN_DATA, "ner/spacy/train.spacy")
