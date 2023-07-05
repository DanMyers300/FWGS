import json
import spacy

def load_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

def load_text(file):
    with open(file) as f:
        data = f.read()
    return data

nlp = spacy.load('en_core_web_sm')
ruler = nlp.add_pipe("entity_ruler")

patterns = load_json('data/formatted_training_data/coded_notes.json')
text = load_text('data/outputs/rfq_dump.txt')
ruler.add_patterns(patterns)

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
