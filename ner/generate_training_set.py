import json
import spacy

# Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_lg")

def open_file(input_file):
    "Open a text file"
    with open(input_file, "r", encoding="utf-8") as opened_file:
        open_text = opened_file.read()
    return open_text

# Load the patterns from the JSON file
PATTERNS_FILE = "data/formatted_training_data/RFQ.json"
with open(PATTERNS_FILE, "r", encoding="utf-8") as file:
    patterns_data = json.load(file)

# Extract the patterns from the loaded data
patterns = patterns_data["patterns"]

# Sample text
TEXT = open_file("data/outputs/rfq_dump.txt")

corpus = []

doc = nlp(TEXT)
for sent in doc.sents:
    corpus.append(sent.text)

# Build upon the spaCy Small Model
nlp = spacy.blank("en")

# Create the EntityRuler
ruler = nlp.add_pipe("entity_ruler")

# Add the loaded patterns to the EntityRuler
ruler.add_patterns(patterns)

TRAIN_DATA = []

# Iterate over the corpus
for sentence in corpus:
    doc = nlp(sentence)

    # Initialize an empty list to store entities and their corresponding text segments
    entity_segments = []

    # Extract entities and their corresponding text segments
    for ent in doc.ents:
        entity_segments.append([sentence[ent.start_char:ent.end_char], ent.label_])

    # Print the entity and its corresponding text segment
    for segment, entity in entity_segments:
        print("Text Segment:", segment)
        print("Entity:", entity)
        print()

    # Append the sentence and entities to the training data
    if entity_segments:
        entities = [{"start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents]
        TRAIN_DATA.append([sentence, {"entities": entities}])