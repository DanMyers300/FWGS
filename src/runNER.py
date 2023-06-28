"""
NER
"""
import re
import json
import spacy
import pyap
from spacy.matcher import Matcher

#
# --- Open file and load spaCy --- #
#

def open_file():
    "Open corpus of text"
    with open(
        "data/outputs/rfq_dump.txt",
        "r",
        encoding="utf-8",
    ) as file:
        contents = file.read()
    return contents
corpus = open_file()
nlp = spacy.load("en_core_web_lg")
doc = nlp(corpus)

#
# --- Define entities to extract --- #
#

class Emails:
    "Extract emails from text"

    def __init__(self):
        self.email_pattern = [{"LIKE_EMAIL": True}]
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add("EMAIL_ADDRESS", [self.email_pattern])
        self.email_matches = None

    def extract_emails(self, output_file):
        "Extract emails then dump to json"
        self.email_matches = self.matcher(doc)
        results = []
        for match in self.email_matches[:10]:
            email_address = str(doc[match[1]])
            results.append({"label": "email", "text": email_address})
            print(match, email_address)

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(results, file)


class URLs:
    "extract URLs from text"

    def parse_urls(self):
        "Parse URLs from text"
        urls = []
        for token in doc:
            if token.like_url:
                urls.append({"label": "URL", "text": token.text})
                print(token.text)
        with open(
            "data/outputs/urls.json",
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
        matcher = Matcher(nlp.vocab)
        pattern_list = [[{"TEXT": {"REGEX": self.pattern}}]]
        matcher.add("DATE", pattern_list)
        matches = matcher(doc)

        for match in matches:
            _, start, end = match
            span = doc[start:end]
            date = {"label": "DATE", "text": span.text}
            self.dates.append(date)
            print(date["text"])

        with open(
            "data/outputs/dates.json",
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(self.dates, file)

        return self.dates


class Addresses:
    "Extract addresses from text"

    def extract_addresses(self):
        "Extract addresses"
        addresses = pyap.parse(corpus, country='US')
        results = []
        for address in addresses:
            if "ONE INTERNATIONAL INC" not in str(address):
                result = {
                    'address': str(address),
                    'address_parts': address.as_dict()
                }
                results.append(result)

        # Save results to a JSON file
        with open('data/outputs/addresses.json', 'w', encoding="utf-8") as file:
            json.dump(results, file, indent=4)

class RFQ:
    def extract_rfq(self):
        rfq_nlp = spacy.load("data/models/rfq_model/model-best")
        rfq_doc = rfq_nlp(corpus)

        entities = []
        for ent in rfq_doc.ents:
            if ent.text.isalnum() and not ent.text.isalpha():  # Select alphanumeric entities with at least one digit
                entities.append({'text': ent.text, 'label': ent.label_})
                print(ent.text, ent.label_)

        with open('data/outputs/rfq.json', 'w', encoding="utf-8") as file:
            json.dump(entities, file, indent=4)

#
# --- Run the extraction --- #
#

# Emails().extract_emails(
#     "data/outputs/emails.json"
# )
# URLs().parse_urls()
# Dates().parse_dates()
# Addresses().extract_addresses()
RFQ().extract_rfq()
