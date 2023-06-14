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


def convert(lang: str, training_data, output_path: Path):
    nlp = spacy.blank(lang)
    docbin = DocBin()
    for text, annot in training_data:
        doc = nlp.make_doc(text)
        entities = []
        for entity in annot["entities"]:
            start, end, label = entity
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                warnings.warn(msg)
            else:
                entities.append(span)
        doc.ents = entities
        docbin.add(doc)
    docbin.to_disk(output_path)


convert("en", TRAIN_DATA, "ner/spacy/train.spacy")

