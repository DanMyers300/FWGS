"""
NER
"""
import json
import spacy
from spacy.matcher import Matcher


def open_file():
    "Open corpus of text"
    with open(
        "/workspaces/Fort_Worth_Gasket_And_Supply_Project/data/corpus.txt",
        "r",
        encoding="utf-8",
    ) as file:
        contents = file.read()
    return contents


corpus = open_file()

# --- Load the base SpaCy large model --- #
base_nlp_large = spacy.load("en_core_web_lg")
base_large_doc = base_nlp_large(corpus)


# --- Print out the named entities --- #
# for ent in doc.ents:
#     print(ent.text, ent.label_)


# --- Define entities to extract --- #
class Emails:
    "Extract emails from text"

    def __init__(self):
        self.email_pattern = [{"LIKE_EMAIL": True}]
        self.matcher = Matcher(base_nlp_large.vocab)
        self.matcher.add("EMAIL_ADDRESS", [self.email_pattern])
        self.email_matches = None

    def extract_emails(self, doc_object, output_file):
        "Extract emails then dump to json"
        self.email_matches = self.matcher(doc_object)
        results = []
        for match in self.email_matches[:10]:
            email_address = str(doc_object[match[1]])
            results.append({"label": "email", "text": email_address})
            print(match, email_address)

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(results, file)


class Addresses:
    "Extract addresses from text"

    def extract_addresses(self):
        "Extract addresses"
        nlp = spacy.load(
            "/workspaces/Fort_Worth_Gasket_And_Supply_Project/data/models/address_model"
        )
        doc = nlp(corpus)
        ent_list = [(ent.text, ent.label_) for ent in doc.ents]
        print("Parsed address -> " + str(ent_list))


class URLs:
    "extract URLs from text"

    def parse_urls(self):
        "Parse URLs from text"
        urls = []
        for token in base_large_doc:
            if token.like_url:
                urls.append({"label": "URL", "text": token.text})
                print(token.text)
        with open(
            "/workspaces/Fort_Worth_Gasket_And_Supply_Project/data/urls.json",
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(urls, file)
        return urls

class Dates:
    "Extract dates"
    def __init__(self):
        self.dates = []
        self.pattern = r"\b(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[01])/(\d{4})\b"

    def parse_dates(self):
        "Parse dates from text"
        matcher = Matcher(base_nlp_large.vocab)
        pattern_list = [[{"TEXT": {"REGEX": self.pattern}}]]
        matcher.add("DATE", pattern_list)
        matches = matcher(base_large_doc)

        for match in matches:
            _, start, end = match
            span = base_large_doc[start:end]
            self.dates.append({"label": "DATE", "text": span.text})

        with open('/workspaces/Fort_Worth_Gasket_And_Supply_Project/data/outputs_json/dates.json', 'w', encoding="utf-8") as file:
            json.dump(self.dates, file)

        return self.dates


# --- Extract entities --- #
# Emails().extract_emails(
#     base_large_doc, "/workspaces/Fort_Worth_Gasket_And_Supply_Project/data/emails.json"
# )
# Addresses().extract_addresses()
# URLs().parse_urls()
Dates().parse_dates()
