"""
NER
"""
import spacy
from spacy.matcher import Matcher

def open_file():
    "Open corpus of text"
    with open("../data/corpus.txt", "r", encoding="utf-8") as file:
        contents = file.read()
        return contents

# --- Load the base SpaCy large model --- #
base_nlp_large = spacy.load("en_core_web_lg")
base_large_doc = base_nlp_large(open_file())


# --- Print out the named entities --- #
# for ent in doc.ents:
#     print(ent.text, ent.label_)


# --- Define entities to extract --- #
class Emails:
    "Extract email addresses from a corpus of text"

    def __init__(self):
        self.email_pattern = [{"LIKE_EMAIL": True}]
        self.matcher = Matcher(base_nlp_large.vocab)
        self.matcher.add("EMAIL_ADDRESS", [self.email_pattern])
        self.email_matches = None

    def extract_emails(self, doc_object):
        "Extract email addresses from a corpus of text"
        self.email_matches = self.matcher(doc_object)
        for match in self.email_matches[:10]:
            print(match, doc_object[match[1]])

# --- Extract entities --- #
Emails().extract_emails(base_large_doc)
