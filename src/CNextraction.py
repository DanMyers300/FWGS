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

train_data = []
for sent in doc.sents:
    coded_notes = []
    for i, ent in enumerate(sent.ents):
        if ent.label_ == 'Coded Note' and len(ent.text) <= 5:
            span_start = ent.start_char - sent.start_char
            span_end = ent.end_char - sent.start_char
            coded_notes.append([span_start, span_end, "Coded Note"])
    if coded_notes:
        train_data.append([sent.text, {"entities": coded_notes}])

output = {"TRAIN_DATA": train_data}

output_path = 'data/outputs/coded_notes.json'
with open(output_path, 'w') as f:
    json.dump(output, f, indent=4)

print(f"Output saved to {output_path}")

