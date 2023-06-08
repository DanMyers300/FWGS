import csv
import random
import spacy
from spacy.training import Example
from spacy.training.iob_utils import offsets_to_biluo_tags

def get_labels(row):
    if len(row) >= 4:  # Check if row has enough columns
        start = row[1].strip()  # Remove leading/trailing whitespaces
        end = row[2].strip()  # Remove leading/trailing whitespaces
        label = row[3]
        if start.isdigit() and end.isdigit():  # Check if start and end are numeric
            return int(start), int(end), label
    return None

# Load CSV data and convert to spaCy format
def load_data(csv_file):
    data = []
    with open(csv_file, 'r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            doc_text = row[0]  # Assuming the text is in the first column
            labels = [get_labels(row)]  # Wrap in a list
            if labels[0] is not None:
                data.append((doc_text, {"entities": labels}))
    return data

# Initialize blank spaCy model and add relevant components
nlp = spacy.blank('en')
ner = nlp.add_pipe('ner')

# Load and convert CSV data
try:
    train_data = load_data('data/csv/database.csv')
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit(1)

# Add labels to the NER model
for _, annotations in train_data:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Disable unneeded pipeline components for training
pipe_exceptions = ["ner"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
with nlp.disable_pipes(*unaffected_pipes):
    # Initialize training loop
    nlp.begin_training()
    losses = {}

    # Train the model
    N_ITER = 10  # Number of iterations
    for i in range(N_ITER):
        random.shuffle(train_data)
        for text, annotations in train_data:
            doc = nlp.make_doc(text)
            entities = annotations.get("entities")
            if entities:
                try:
                    example = Example.from_dict(doc, annotations)
                    nlp.update([example], losses=losses, drop=0.5)
                except ValueError as e:
                    print(f"Error: {e}")
                # Print aligned tags for debugging
                entities = [(start, end, label) for start, end, label in entities]
                aligned_tags = offsets_to_biluo_tags(doc, entities)
                print(f"Aligned tags: {aligned_tags}")

        print(f'Iteration {i+1} - Loss: {losses["ner"]}')

# Save the trained model
try:
    nlp.to_disk('trained_model')
except IOError:
    print("Error: Failed to save the trained model.")
    exit(1)
